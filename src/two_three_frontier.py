#!/usr/bin/env python3
"""Checkpoint 10: centered two/three-prime bilinear and Vaughan reductions.

General uniform proofs are in TWO_THREE_BILINEAR_NOTE.md. Finite checks
verify exact identities; they do not establish the .011u target.
Standard library only.
"""

from __future__ import annotations

import argparse
from bisect import bisect_left, bisect_right
from collections import Counter
from decimal import Decimal
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json

from ross_geometry_audit import factor_band, primes_up_to, require
from restricted_frontier import integer_root_ceiling, rounded_reference_length
from structured_frontier import I, ROOT, enclose_integral


def divisors(factors):
    values = [1]
    for p, exponent in factors.items():
        old = list(values)
        power = 1
        for _ in range(exponent):
            power *= p
            values.extend(d * power for d in old)
    return sorted(values)


def mu_from_factors(factors):
    return 0 if any(e > 1 for e in factors.values()) else (-1) ** len(factors)


def lambda_log_vector(factors):
    return {next(iter(factors)): 1} if len(factors) == 1 else {}


def add_vector(target, source, scale):
    for p, exponent in source.items():
        target[p] += scale * exponent


def vaughan_vector_checks(limit=4000):
    """Exact equality of coefficients of log(prime), with no rounding."""
    factors = factor_band(1, limit, primes_up_to(isqrt(limit)))
    divs = {n: divisors(factors[n]) for n in range(1, limit + 1)}
    mu = {n: mu_from_factors(factors[n]) for n in factors}
    mangoldt = {n: lambda_log_vector(factors[n]) for n in factors}
    fixtures = []
    for u, v in ((1, 1), (2, 3), (4, 5), (6, 7)):
        beta = {m: sum(mu[a] for a in divs[m] if a > u) for m in factors}
        for n in range(1, limit + 1):
            value = Counter()
            for a in divs[n]:
                if a <= u:
                    add_vector(value, factors[n // a], mu[a])
                    for b in divs[n // a]:
                        if b <= v:
                            add_vector(value, mangoldt[b], -mu[a])
            for b in divs[n]:
                m = n // b
                if m > u and b > v:
                    add_vector(value, mangoldt[b], beta[m])
            if n <= v:
                add_vector(value, mangoldt[n], 1)
            cleaned = {p: e for p, e in value.items() if e}
            require(cleaned == mangoldt[n], "Formal Vaughan identity")
        fixtures.append({"U": u, "V": v, "all_n_through": limit, "passed": True})
    return fixtures


def outer_coefficient(factors, n):
    """Frozen coefficient c_N(d), computed from d's prime factorization."""
    if not factors or any(p ** 4 < n for p in factors):
        return F(0)
    degree = sum(factors.values())
    if degree == 1:
        p = next(iter(factors))
        return F(int(p ** 20 < n ** 19))
    if degree != 2:
        return F(0)
    d = 1
    for p, exponent in factors.items():
        d *= p ** exponent
    if d * max(factors) > n * n:
        return F(0)
    return F(1, 2) if len(factors) == 1 else F(1)


def factor_band_counts(n, lo, hi):
    values = {key: F(0) for key in (
        "M2", "M3", "oriented_T3", "diagonal", "frozen_prime",
        "Mangoldt_kernel", "prime_power_contamination")}
    ps = primes_up_to(isqrt(hi))
    for start in range(lo, hi + 1, 20000):
        band = factor_band(start, min(hi, start + 19999), ps)
        for m, factors in band.items():
            degree = sum(factors.values())
            rough = min(factors) ** 4 >= n
            if rough and degree in (2, 3):
                denominator = 1
                for exponent in factors.values():
                    denominator *= factorial(exponent)
                if degree == 2 and min(factors) ** 20 < n ** 19:
                    values["M2"] += F(1, denominator)
                if degree == 3:
                    values["M3"] += F(1, denominator)
                    expanded = sorted(p for p, e in factors.items() for _ in range(e))
                    p, r, q = expanded
                    values["oriented_T3"] += F(1, 2) if p == r else F(1)
                    if r == q:
                        values["diagonal"] += F(1, 3) if p == r else F(1, 2)
            for base, exponent in factors.items():
                for k in range(1, exponent + 1):
                    remaining = dict(factors)
                    remaining[base] -= k
                    if not remaining[base]:
                        del remaining[base]
                    coefficient = outer_coefficient(remaining, n)
                    if not coefficient:
                        continue
                    term = coefficient / k  # Lambda(base^k)/log(base^k)=1/k.
                    values["Mangoldt_kernel"] += term
                    if k == 1:
                        values["frozen_prime"] += term
                    else:
                        values["prime_power_contamination"] += term
    require(values["oriented_T3"] - values["M3"] == values["diagonal"],
            "Largest-factor diagonal correction")
    require(values["Mangoldt_kernel"] == values["frozen_prime"] +
            values["prime_power_contamination"], "Mangoldt power correction")
    values["freeze_error"] = values["frozen_prime"] - values["M2"] - values["oriented_T3"]
    values["total_error"] = values["Mangoldt_kernel"] - values["M2"] - values["M3"]
    require(values["total_error"] == values["prime_power_contamination"] +
            values["freeze_error"] + values["diagonal"], "Full rowwise reduction")
    return values


def direct_outer_enumeration(n, lo, hi):
    """Independent prime-pair and prime-power enumeration on small bands."""
    x = n * n
    first = integer_root_ceiling(n, 4)
    limit = hi // first
    ps = primes_up_to(limit)
    coefficients = {p: F(1) for p in ps if p ** 4 >= n and p ** 20 < n ** 19}
    for i, p in enumerate(ps):
        if p ** 4 < n:
            continue
        if p ** 3 > x:
            break
        last = isqrt(x // p)
        for r in ps[bisect_left(ps, p):bisect_right(ps, last)]:
            d = p * r
            require(d not in coefficients, "Outer coefficient uniqueness")
            coefficients[d] = F(1, 2) if p == r else F(1)
    powers = {}
    for p in ps[:bisect_right(ps, isqrt(limit))]:
        value, k = p * p, 2
        while value <= limit:
            require(value not in powers, "Prime-power representation uniqueness")
            powers[value] = F(1, k)
            value *= p
            k += 1
    prime, contam = F(0), F(0)
    for d, coefficient in coefficients.items():
        lower, upper = (lo + d - 1) // d, hi // d
        prime += coefficient * (bisect_right(ps, upper) - bisect_left(ps, lower))
        contam += coefficient * sum((weight for q, weight in powers.items()
                                     if lower <= q <= upper), F(0))
    return prime, contam


def arithmetic_fixtures():
    fixtures = []
    for n in (20, 40, 80, 120, 200, 5000, 10000, 18000):
        x, y = n * n, n + 1
        h, _ = rounded_reference_length(n)
        bands = []
        for label, lo, hi in (
                ("short", x - n // 2, x + n // 2),
                ("long", x - h // 2, x + h // 2)):
            values = factor_band_counts(n, lo, hi)
            independently_enumerated = n <= 200
            if independently_enumerated:
                prime, contam = direct_outer_enumeration(n, lo, hi)
                require(prime == values["frozen_prime"], "Independent frozen prime count")
                require(contam == values["prime_power_contamination"],
                        "Independent Mangoldt power count")
            bands.append({"label": label, "endpoints": [lo, hi],
                          "independent_outer_enumeration": independently_enumerated,
                          "counts": {k: str(v) for k, v in values.items()}})
        scale = F(y, h)
        short, long = bands[0]["counts"], bands[1]["counts"]
        centered_original = F(short["M2"]) + F(short["M3"]) - scale * (
            F(long["M2"]) + F(long["M3"]))
        centered_kernel = F(short["Mangoldt_kernel"]) - scale * F(long["Mangoldt_kernel"])
        centered_error = F(short["total_error"]) - scale * F(long["total_error"])
        require(centered_kernel - centered_original == centered_error,
                "Centered bilinear transfer")
        fixtures.append({"N": n, "Y": y, "H1": h, "bands": bands,
                         "centered_original_exact": str(centered_original),
                         "centered_Mangoldt_exact": str(centered_kernel),
                         "centered_correction_exact": str(centered_error),
                         "all_identities_passed": True})
        print("Bilinear fixtures completed: N=" + str(n), flush=True)
    return fixtures


def reference_and_sample_audit(bins):
    old = json.loads((ROOT / "results/frontier_prime_product_mass.json").read_text())
    c2 = I(Decimal(old["frontier_groups"]["two_prime_frontier"]["lower"]),
           Decimal(old["frontier_groups"]["two_prime_frontier"]["upper"]))
    c3 = I(Decimal(old["frontier_groups"]["three_prime_frontier"]["lower"]),
           Decimal(old["frontier_groups"]["three_prime_frontier"]["upper"]))
    low3 = enclose_integral(
        lambda s: 2 * (4 * s - 1).log() / (s * (2 - s)),
        F(1, 2), F(19, 20), bins)
    samples = json.loads((ROOT / "results/frontier_centered_experiments.json").read_text())
    records = []
    for e in samples["experiments"]:
        short, long = e["short"], e["long"]
        value = sum((F(short["factorial_frontier_degrees"][str(j)]) -
                     F(e["Y"], e["rounded_long_length"]) *
                     F(long["factorial_frontier_degrees"][str(j)])
                     for j in (2, 3)), F(0))
        u = e["N"] / (2 * I.point(e["N"]).log())
        normalized = I.point(value) / u
        records.append({"N": e["N"], "exact_joint_excess": str(value),
                        "normalized_joint_excess": normalized.record(),
                        "finite_0011_allocation_holds": normalized.hi <= Decimal(".011")})
    return {
        "bins": bins, "joint_reference_mass": (c2 + c3).record(),
        "low_outer_triprime_reference_mass": low3.record(),
        "remaining_triprime_reference_mass": (c3 - low3).record(),
        "fraction_of_joint_reference_in_TypeI_easy_outer_range": (
            (c2 + low3) / (c2 + c3)).record(),
        "these_reference_masses_are_actual_caps": False,
        "samples": records,
        "samples_failing_finite_0011_allocation": sum(
            not r["finite_0011_allocation_holds"] for r in records),
        "maximum_sample_upper": str(max(
            Decimal(r["normalized_joint_excess"]["upper"]) for r in records)),
        "finite_allocation_failures_disprove_asymptotic_estimate": False,
    }


def analytic_certificate():
    sigma, eta = F(4, 3), F(1, 3)
    cap6 = (3 - 2 * sigma) / 2
    require(cap6 < eta, "Balanced triple FI6 endpoint contradiction")
    truncation, outer = F(1, 100), F(19, 20)
    low_floor = outer + 2 * truncation
    require(low_floor < 1, "Low-outer Type I saving")
    return {
        "truncation_exponent_N": str(truncation),
        "U_V": "floor(N^(1/100))",
        "low_outer_cutoff": "N^(19/20)",
        "low_TypeI_floor_error_exponent": str(low_floor),
        "low_TypeI_centered_error": "O(N^(97/100))+O(Y*(H1/x)^2*log(N)^4)=o(u)",
        "all_semiprime_TypeI_terms_in_low_range": True,
        "high_outer_coefficients": "Only frozen two-prime products; N^.95<d<=N^(4/3)",
        "balanced_triple_reciprocal_FI6": {
            "Sigma": str(sigma), "eta": str(eta),
            "necessary_B_slot_lower": str(eta),
            "necessary_B_slot_upper": str(cap6),
            "all_factor_groupings_fail_these_two_facets": True,
            "scope": "Direct generic reciprocal Theorem 6 mapping only"},
        "TypeII_additive_FI2": {
            "frequency_height_N_exponent": "1",
            "weighted_product_N_exponent": "2",
            "phase_size_N_exponent": "1",
            "first_term_raw_N_exponent": "2",
            "Fourier_coefficient_N_exponent": "-1",
            "resulting_error_N_exponent": "1",
            "uniform_o_u_saving_supplied": False,
            "actual_sparse_norm_or_spacing_refinement_excluded": False},
        "Li_Lemma_4_1_at_half": {
            "necessary_facet": "abs(alpha1-alpha2)<2*eta-1=0",
            "formal_region_empty": True,
            "theorem_extended_to_endpoint": False},
        "new_terminal_comparison_admitted": False,
        "uniform_0011_joint_estimate_proved": False,
    }


def write_json(name, value):
    (ROOT / "results" / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bins", type=int, default=20000)
    args = parser.parse_args()
    require(args.bins >= 1000, "At least 1000 reference cells")
    ledger = ROOT / "results/negative_frontier_ledger.json"
    require(hashlib.sha256(ledger.read_bytes()).hexdigest() ==
            "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
            "Historical ledger changed")
    exact = {"formal_Vaughan_log_vector_fixtures": vaughan_vector_checks(),
             "actual_bilinear_fixtures": arithmetic_fixtures(),
             "finite_checks_prove_uniform_target": False}
    mass = reference_and_sample_audit(args.bins)
    analytic = analytic_certificate()
    reduction = {
        "date": "2026-10-06", "checkpoint": 10,
        "outer_coefficient": "prime z<=d<w, plus c3(d)=1/2*sum_ordered_prime_p,r>=z 1_(pr=d)1_(pr*max(p,r)<=N^2)",
        "outer_coefficient_bound": "0<=c_N(d)<=1; prime and semiprime supports disjoint",
        "outer_support_N_exponents": ["1/4", "4/3"],
        "cofactor_support_N_exponents": ["2/3", "7/4"],
        "frozen_prime_bilinear_kernel": "sum_d c_N(d)*sum_prime_q 1_W(dq)",
        "frozen_ordering_centered_error": "O(N^(3/4))+O(Y*(H1/x)*log(N))=o(u)",
        "proper_prime_power_count_bound": "P(t)<=5*sqrt(t)",
        "proper_prime_power_reciprocal_bound": "sum_(r>=R,r proper_prime_power)1/r<=25/sqrt(R)",
        "Mangoldt_kernel": "A_N(W)=sum_d c_N(d)*sum_q Lambda(q)/log(q)*1_W(dq)",
        "Mangoldt_centered_transfer_error": "O(N^(7/8))=o(u)",
        "full_centered_transfer": "Delta2+Delta3=Delta A_N+O(N^(7/8))+O(Y*(H1/x)*log(N))",
        "beta_U": "sum_(a|m,a>U)mu(a)",
        "Vaughan_TypeII": "B_N(W)=sum_d c_N(d)*sum_(m>U,b>V)beta_U(m)*Lambda(b)/log(m*b)*1_W(d*m*b)",
        "remaining_high_TypeI_floor_error": "R_I,high(W)=I1_high(W)+I2_high(W)-integral_W G_high(v)dv, d>N^.95",
        "final_uniform_reduction": "Delta2+Delta3=Delta B_N+Delta R_I,high+o(u)",
        "required_remaining_estimate": "Delta B_N+Delta R_I,high<=(.011+o(1))*u for every sufficiently large even N",
        "general_proof": "TWO_THREE_BILINEAR_NOTE.md",
        "uniform_0011_estimate_proved": False,
        "certified_K": 0, "H_theta_proved": False,
    }
    write_json("two_three_bilinear_reduction.json", reduction)
    write_json("two_three_vaughan_checks.json", exact)
    write_json("two_three_reference_and_samples.json", mass)
    write_json("two_three_analytic_audit.json", analytic)
    state_path = ROOT / "results/campaign_state.json"
    state = json.loads(state_path.read_text())
    state.update({
        "checkpoint": 10, "latest_investigation_note": "TWO_THREE_BILINEAR_NOTE.md",
        "two_three_bilinear_reduction": "results/two_three_bilinear_reduction.json",
        "two_three_analytic_audit": "results/two_three_analytic_audit.json",
        "two_three_vaughan_checks": "results/two_three_vaughan_checks.json",
        "two_three_reference_and_samples": "results/two_three_reference_and_samples.json",
        "all_semiprime_centered_TypeI_terms_negligible": True,
        "two_three_uniform_0011_estimate_proved": False,
        "next_gate": "Prove the joint centered Vaughan TypeII plus high-outer TypeI floor-error estimate <=(.011+o(1))u, or another sufficient joint allocation",
        "lower_bound_status": "K=0; uniform bilinear and Vaughan reductions proved; centered TypeII and high-outer triprime TypeI remainder unestimated",
        "numerical_bounds_changed_in_checkpoint10": "New reference subregion enclosure and exact reduction checks only; historical analytic ledger unchanged",
        "new_terminal_comparison_estimate_admitted": False,
    })
    state["milestones"]["3"] = "Frozen centered bounded outer coefficient and uniform prime-power/Vaughan reductions proved"
    state["milestones"]["4"] = "Actual Vaughan coefficient families specified; direct FI and printed TypeII endpoint audits supplied; inventory incomplete"
    state["milestones"]["6"] = "Exact formal log-vector Vaughan checks and independent frozen bilinear fixtures passed; uniform terminal estimate still open"
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "formal_Vaughan_identities": 4 * 4000,
        "bilinear_actual_fixtures": len(exact["actual_bilinear_fixtures"]),
        "low_outer_triprime_reference_mass": mass["low_outer_triprime_reference_mass"],
        "low_TypeI_error_exponent": analytic["low_TypeI_floor_error_exponent"],
        "finite_0011_allocation_failures": mass["samples_failing_finite_0011_allocation"],
        "uniform_joint_estimate_proved": False,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
