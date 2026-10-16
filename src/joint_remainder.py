#!/usr/bin/env python3
"""Checkpoint 11: long remainder removal, wider Type I range, beta energy.

Uniform analytic proofs are in JOINT_REMAINDER_NOTE.md. These exact checks
verify identities and all vertices of the stated exponent regions; they do
not prove the remaining .011u short-window estimate. Standard library only.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from decimal import Decimal
from fractions import Fraction as F
from itertools import combinations
from math import gcd, isqrt
import hashlib
import json

from ross_geometry_audit import factor_band, primes_up_to, require
from structured_frontier import I, ROOT, enclose_integral
from two_three_frontier import (
    add_vector, divisors, lambda_log_vector, mu_from_factors,
    outer_coefficient,
)


def solve3(rows):
    matrix = [list(a) + [b] for a, b in rows]
    for col in range(3):
        pivot = next((i for i in range(col, 3) if matrix[i][col]), None)
        if pivot is None:
            return None
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        scale = matrix[col][col]
        matrix[col] = [v / scale for v in matrix[col]]
        for i in range(3):
            if i != col:
                scale = matrix[i][col]
                matrix[i] = [x - scale * y for x, y in zip(matrix[i], matrix[col])]
    return tuple(row[3] for row in matrix)


def vertices(constraints):
    found = set()
    for indices in combinations(range(len(constraints)), 3):
        point = solve3([constraints[i] for i in indices])
        if point is not None and all(
                sum(a * x for a, x in zip(row, point)) <= bound
                for row, bound in constraints):
            found.add(point)
    return sorted(found)


def region(sigma_lo, sigma_hi, alpha_lo, alpha_hi=None):
    # Coordinates: sigma (two-prime product), alpha (smaller prime), delta
    # (a, or ab, Vaughan small-variable product), with 0<=delta<=.02.
    result = [
        ((F(-1), F(0), F(0)), -sigma_lo),
        ((F(1), F(0), F(0)), sigma_hi),
        ((F(0), F(-1), F(0)), -alpha_lo),
        ((F(-1, 2), F(1), F(0)), F(0)),
        ((F(0), F(0), F(-1)), F(0)),
        ((F(0), F(0), F(1)), F(1, 50)),
    ]
    if alpha_hi is not None:
        result.append(((F(0), F(1), F(0)), alpha_hi))
    return result


def rs_margins(sigma, alpha, delta, eta):
    total = sigma + delta
    return {
        "T1": alpha - (4 * eta + 2 - 2 * total),
        "T2": total - 3 * eta - alpha,
        "T3": alpha - 2 * eta,
        "T4": 2 - total - eta,
    }


def fi_margins(sigma, alpha, delta, eta):
    total = sigma + delta
    return {
        "T1": (8 * total - 7 * eta - 6) / 7 - alpha,
        "T2": (6 * total - 5 * eta - 4) / 7 - alpha,
        "T3": (5 * total - 5 * eta - 2) / 8 - alpha,
        "T4": (4 * total - 5 * eta - 2) / 5 - alpha,
        "T5": alpha - eta,
        "T6": (2 - total - eta) / 2 - alpha,
    }


def facet_certificates():
    nu = F(1, 10000)
    split = F(59, 200)
    domains = [
        ("RS_lower", "RS", region(F(19, 20), F(11, 10), F(1, 4))),
        ("FI_small_prime", "FI6",
         region(F(11, 10), F(9, 8), F(1, 4), split)),
        ("RS_larger_prime", "RS",
         region(F(11, 10), F(9, 8), split)),
    ]
    records = []
    for name, engine, constraints in domains:
        branches = [(constraints, "above_one")]
        if engine == "RS":
            branches = [
                (constraints + [((F(1), F(0), F(1)), F(1))], "below_one"),
                (constraints + [((F(-1), F(0), F(-1)), F(-1))], "above_one"),
            ]
        points, minima = [], {}
        for branch, side in branches:
            for sigma, alpha, delta in vertices(branch):
                total = sigma + delta
                eta = nu if side == "below_one" else total - 1 + nu
                margins = (rs_margins if engine == "RS" else fi_margins)(
                    sigma, alpha, delta, eta)
                require(all(v > 0 for v in margins.values()), "Strict source facets")
                for term, value in margins.items():
                    minima[term] = min(minima.get(term, value), value)
                points.append({
                    "sigma": str(sigma), "alpha": str(alpha),
                    "delta": str(delta), "eta_top": str(eta),
                    "branch": side, "margins": {k: str(v) for k, v in margins.items()},
                })
        require(bool(points), "Nonempty exponent region")
        records.append({
            "region": name, "engine": engine,
            "constraints": [{"A": [str(v) for v in a], "bound": str(b)}
                            for a, b in constraints],
            "vertices": points,
            "minimum_margins": {k: str(v) for k, v in minima.items()},
            "minimum_over_all_facets": str(min(minima.values())),
            "continuous_region_certified_by_affine_vertex_minima": True,
        })
    return {
        "U_V_N_exponent": "1/100", "small_product_delta_range": ["0", "1/50"],
        "frequency_extension_nu": str(nu), "small_prime_split": str(split),
        "complete_outer_TypeI_cutoff": "N^(9/8)",
        "regions": records,
        "all_current_TypeI_terms_below_cutoff_controlled": True,
        "all_terminal_TypeII_terms_controlled": False,
    }


def beta_energy_checks():
    limit = 128
    factors = factor_band(1, limit, primes_up_to(isqrt(limit)))
    mu = {n: mu_from_factors(v) for n, v in factors.items()}
    records = []
    for u in (1, 2, 3, 4, 8, 16, 32, 64, 128):
        quadratic = sum((F(mu[a] * mu[b], a * b // gcd(a, b))
                         for a in range(1, u + 1)
                         for b in range(1, u + 1)), F(0))
        diagonal = F(0)
        for r in range(1, u + 1):
            phi = sum(gcd(j, r) == 1 for j in range(1, r + 1))
            inner = sum((F(mu[d], d) for d in range(r, u + 1, r)), F(0))
            diagonal += phi * inner * inner
        require(quadratic == diagonal and quadratic >= 0, "Energy diagonalization")
        m = 1000
        upper = 2 * m
        truncated = [0] * (upper + 1)
        for a in range(1, u + 1):
            for n in range(a, upper + 1, a):
                truncated[n] += mu[a]
        direct = sum(value * value for value in truncated[m + 1:])
        floor = sum(mu[a] * mu[b] * (
                    (2 * m) // (a * b // gcd(a, b)) -
                    m // (a * b // gcd(a, b)))
                    for a in range(1, u + 1)
                    for b in range(1, u + 1))
        require(direct == floor, "Exact beta energy floor expansion")
        require(abs(F(direct) - m * quadratic) <= u * u,
                "Elementary finite energy error")
        records.append({
            "U": u, "M": m, "dyadic_energy_exact": direct,
            "quadratic_form_exact": str(quadratic),
            "quadratic_form_decimal": str(Decimal(quadratic.numerator) /
                                          Decimal(quadratic.denominator)),
            "diagonalization_passed": True,
            "floor_expansion_passed": True,
        })
    return {
        "fixtures": records,
        "analytic_input": "Bretèche-Dress-Tenenbaum (2020), (1.5) and Theorem 1.1",
        "source_url": "https://tenenb.perso.math.cnrs.fr/PPP/Sxz.pdf",
        "uniform_dyadic_bound": "sum_(M<m<=2M)|beta_U(m)|^2=O(M)",
        "positive_limit": "For U->infinity and M/U->infinity, energy/M->L>0",
        "vanishing_beta_norm_factor_supplied": False,
        "fixed_center_nearby_product_correlations_estimated": False,
    }


def subtract_factors(left, right):
    result = dict(left)
    for p, e in right.items():
        result[p] -= e
        if not result[p]:
            del result[p]
    return result


def factor_divisor(q_factors, d):
    result = {}
    for p in q_factors:
        exponent = 0
        while d % p == 0:
            d //= p
            exponent += 1
        if exponent:
            result[p] = exponent
    require(d == 1, "Divisor factorization")
    return result


def vaughan_vectors(q_factors, u, v):
    q = 1
    for p, e in q_factors.items():
        q *= p ** e
    first, second, bilinear = defaultdict(int), defaultdict(int), defaultdict(int)
    divs = divisors(q_factors)
    for a in divs:
        if a > u:
            continue
        af = factor_divisor(q_factors, a)
        scale = mu_from_factors(af)
        rem = subtract_factors(q_factors, af)
        add_vector(first, rem, scale)
        for b in divisors(rem):
            if b <= v:
                add_vector(second, lambda_log_vector(factor_divisor(rem, b)), -scale)
    for b in divs:
        if b <= v or q // b <= u:
            continue
        bf = factor_divisor(q_factors, b)
        lv = lambda_log_vector(bf)
        if not lv:
            continue
        mf = subtract_factors(q_factors, bf)
        beta = sum(mu_from_factors(factor_divisor(mf, a))
                   for a in divisors(mf) if a > u)
        add_vector(bilinear, lv, beta)
    target = lambda_log_vector(q_factors)
    require(q > v, "Small Mangoldt term absent in the actual fixture")
    for p in q_factors:
        require(first[p] + second[p] + bilinear[p] == target.get(p, 0),
                "Independent rowwise Vaughan terms")
    return first, second, bilinear, target, q


def actual_signed_checks():
    records = []
    for n, u, v in ((20, 1, 1), (40, 3, 3), (80, 4, 5),
                    (120, 3, 3), (200, 4, 5), (5000, 1, 1), (18000, 1, 1)):
        lo, hi = n * n - n // 2, n * n + n // 2
        bands = factor_band(lo, hi, primes_up_to(isqrt(hi)))
        formal = {k: defaultdict(F) for k in ("A", "I_low", "I_core", "B")}
        incidences, core_rows = 0, 0
        rational_a = F(0)
        for row, row_factors in bands.items():
            candidates = [{p: 1} for p in row_factors]
            ps = sorted(row_factors)
            for i, p in enumerate(ps):
                if row_factors[p] >= 2:
                    candidates.append({p: 2})
                for r in ps[i + 1:]:
                    candidates.append({p: 1, r: 1})
            for df in candidates:
                coefficient = outer_coefficient(df, n)
                if not coefficient:
                    continue
                d = 1
                for p, e in df.items():
                    d *= p ** e
                qf = subtract_factors(row_factors, df)
                first, second, bilinear, target, q = vaughan_vectors(qf, u, v)
                incidences += 1
                high = d ** 8 > n ** 9
                require(not high or sum(df.values()) == 2,
                        "Only two-prime products in the remaining Type I core")
                core_rows += high
                dest = "I_core" if high else "I_low"
                for p in qf:
                    formal["A"][q, p] += coefficient * target.get(p, 0)
                    formal[dest][q, p] += coefficient * (first[p] + second[p])
                    formal["B"][q, p] += coefficient * bilinear[p]
                if len(qf) == 1:
                    rational_a += coefficient / next(iter(qf.values()))
        keys = set().union(*(set(t) for t in formal.values()))
        require(all(formal["A"][key] == formal["I_low"][key] +
                    formal["I_core"][key] + formal["B"][key] for key in keys),
                "Exact signed aggregate, coefficients of log(p)/log(q)")
        sign_counts = {
            name: {"positive": sum(value > 0 for value in terms.values()),
                   "negative": sum(value < 0 for value in terms.values())}
            for name, terms in formal.items()
        }
        records.append({
            "N": n, "U": u, "V": v,
            "parameters_forced_to_exercise_identity": (u, v) != (1, 1),
            "outer_cofactor_incidences": incidences,
            "core_incidences": core_rows,
            "A_N_short_exact": str(rational_a),
            "aggregate_formal_identity_passed": True,
            "coefficient_sign_counts": sign_counts,
        })
    return records


def reference_enclosure(bins):
    old = json.loads((ROOT / "results/frontier_prime_product_mass.json").read_text())
    def group(name):
        v = old["frontier_groups"][name]
        return I(Decimal(v["lower"]), Decimal(v["upper"]))
    c2, c3 = group("two_prime_frontier"), group("three_prime_frontier")
    low3 = enclose_integral(
        lambda s: 2 * (4 * s - 1).log() / (s * (2 - s)),
        F(1, 2), F(9, 8), bins)
    return {
        "bins": bins, "triprime_TypeI_controlled_reference": low3.record(),
        "triprime_TypeI_core_reference": (c3 - low3).record(),
        "joint_reference_TypeI_controlled_share": ((c2 + low3) / (c2 + c3)).record(),
        "actual_short_count_cap_supplied_by_these_masses": False,
        "TypeII_bound_supplied_by_this_reference_share": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bins", type=int, default=20000)
    args = parser.parse_args()
    require(args.bins >= 1000, "Reference interval cells")
    ledger = ROOT / "results/negative_frontier_ledger.json"
    require(hashlib.sha256(ledger.read_bytes()).hexdigest() ==
            "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
            "Frozen ledger changed")
    facets = facet_certificates()
    energy = beta_energy_checks()
    checks = actual_signed_checks()
    reference = reference_enclosure(args.bins)
    reduction = {
        "date": "2026-10-06", "checkpoint": 11,
        "U_V": "floor(N^(1/100))",
        "TypeI_short_controlled_outer_range": "d<=N^(9/8)",
        "all_semiprime_TypeI_controlled": True,
        "all_triprime_TypeI_controlled": False,
        "remaining_TypeI_outer_range": "N^(9/8)<d<=N^(4/3), only two-prime products",
        "normalized_all_long_TypeI_floor_error":
            "O(N^(53/150)*(H1/x)^(-1))=o(u)",
        "normalized_long_TypeII": "(Y/H1)*B_N(B1)=o(u)",
        "long_reference_input": "Classical quantitative PNT for Lambda and mu; no short prime asymptotic",
        "short_only_joint_reduction": "Delta2+Delta3=B_N(J)+R_I,core(J)+o(u)",
        "remaining_sufficient_estimate": "B_N(J)+R_I,core(J)<=(.011+o(1))*u, every sufficiently large even N",
        "beta_uniform_energy": "sum_(M<m<=2M)|beta_U(m)|^2=O(M)",
        "short_TypeII_log_freeze_error": "O(N^epsilon/log(N))=o(u)",
        "short_TypeI_free_weight_freeze_error": "O(N^(53/150)*log(N)^C)=o(u)",
        "exact_center_outer_divisors":
            "d|N^2 contribute o(u) to TypeII and TypeI floor error; nearby products not estimated",
        "remaining_uniform_0011_estimate_proved": False,
        "H_theta_proved": False, "certified_K": 0,
        "general_proof": "JOINT_REMAINDER_NOTE.md",
    }
    outputs = {
        "joint_remainder_reduction.json": reduction,
        "joint_remainder_facets.json": facets,
        "joint_remainder_beta_energy.json": energy,
        "joint_remainder_checks_and_reference.json":
            {"exact_signed_short_fixtures": checks, "reference": reference,
             "finite_checks_prove_uniform_target": False},
    }
    for name, value in outputs.items():
        (ROOT / "results" / name).write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    state_path = ROOT / "results/campaign_state.json"
    state = json.loads(state_path.read_text())
    state.update({
        "checkpoint": 11, "latest_investigation_note": "JOINT_REMAINDER_NOTE.md",
        "joint_remainder_reduction": "results/joint_remainder_reduction.json",
        "joint_remainder_facets": "results/joint_remainder_facets.json",
        "joint_remainder_beta_energy": "results/joint_remainder_beta_energy.json",
        "joint_remainder_checks_and_reference": "results/joint_remainder_checks_and_reference.json",
        "complete_centered_TypeI_outer_cutoff": "N^(9/8)",
        "normalized_long_TypeII_negligible": True,
        "two_three_uniform_0011_estimate_proved": False,
        "lower_bound_status": "K=0; short-only joint reduction and TypeI through N^(9/8) proved; TypeII and balanced-triprime floor remainder unestimated",
        "next_gate": "Prove B_N(J)+R_I,core(J)<=(.011+o(1))*u uniformly on every sufficiently large even square center",
        "new_terminal_comparison_estimate_admitted": False,
        "numerical_bounds_changed_in_checkpoint11": "New TypeI reference subregion enclosure; historical ledger unchanged",
    })
    state["milestones"]["3"] = "Long normalized remainders removed; complete TypeI below outer exponent 9/8 proved"
    state["milestones"]["4"] = "Explicit short TypeII coefficients with uniform beta energy bound; terminal correlation estimate pending"
    state["milestones"]["6"] = "Continuous rational facet certificates, exact signed short fixtures and energy diagonalizations passed"
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "continuous_facet_regions": len(facets["regions"]),
        "exact_energy_fixtures": len(energy["fixtures"]),
        "exact_signed_short_fixtures": len(checks),
        "triprime_TypeI_controlled_reference": reference["triprime_TypeI_controlled_reference"],
        "uniform_0011_estimate_proved": False,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
