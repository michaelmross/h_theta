#!/usr/bin/env python3
"""Checkpoint 20: exact small-prime identities and actual continuation rows.

Checks do not certify asymptotic source theorems, reference PNT, or .011u.
Historical modules are imported read-only. Only two new result files change.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import comb, isqrt
from pathlib import Path
import json

from beta_support import factor_table, omega_u
from cofactor_estimation import beta_from_factors
from delta_grouping import CB, pow_le
from ross_geometry_audit import factor_band, primes_up_to
from signed_core_continuation import actual_weights, cleaned
from structured_frontier import I

ROOT = Path(__file__).resolve().parents[1]
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}
LEDGER_HASH = "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"
DATE = "2026-10-09"


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def provenance():
    prior = json.loads((ROOT / "results/checkpoint19_preservation_manifest.json").read_text())
    demand(prior["checkpoint"] == 19 and len(prior["files"]) == 224,
           "Frozen checkpoint 19 has 224 records")
    count = 0
    for record in prior["files"]:
        if record["path"] in MUTABLE:
            continue
        data = (ROOT / record["path"]).read_bytes()
        demand(len(data) == record["size_bytes"] and sha256(data).hexdigest() == record["sha256"],
               record["path"] + " unchanged")
        count += 1
    demand(count == 220, "220 historical nonmutable records")
    demand(sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
           == LEDGER_HASH, "Frozen negative-frontier ledger")
    return {"checkpoint19_nonmutable_records_verified": count,
            "negative_frontier_ledger_sha256": LEDGER_HASH,
            "historical_analytic_ledger_unchanged": True}


def mu_from_factors(fs):
    return 0 if any(e > 1 for _, e in fs) else (-1) ** len(fs)


def even_pairing_checks():
    limit = 12000
    table = factor_table(limit)
    rows = []
    identity_count = 0
    repeated_two = 0
    positive = negative = 0
    for u in (1, 2, 3, 5, 8, 16, 32, 64):
        ds = [(d, mu_from_factors(table[d])) for d in range(u // 2 + 1, u + 1)
              if d % 2 == 1]
        prefix = [0] * (limit + 1)
        cumulative = 0
        hplus = hminus = F(0)
        for c in range(2, limit + 1):
            if c % 2 == 0:
                fs = dict(table[c])
                beta = beta_from_factors(fs, u)
                paired = -sum(mu for d, mu in ds if c % d == 0)
                demand(beta == paired, "Exact even divisor pairing")
                cumulative += beta
                identity_count += 1
                repeated_two += fs.get(2, 0) > 1
                positive += beta > 0
                negative += beta < 0
                hplus += F(max(beta, 0), c)
                hminus += F(max(-beta, 0), c)
            prefix[c] = cumulative
        m2 = sum((F(mu, d) for d, mu in ds), F(0))
        means = []
        for t in (127, 1000, 4096, limit):
            exact = -sum(mu * (t // (2 * d)) for d, mu in ds)
            demand(prefix[t] == exact, "Exact even floor mean")
            error = F(exact) + F(t, 2) * m2
            cost = sum(abs(mu) for _, mu in ds)
            demand(abs(error) <= cost, "Uniform even floor error at most O(U)")
            means.append({"t": t, "signed_sum": exact, "m2_U": str(m2),
                          "floor_error": str(error), "absolute_floor_envelope": cost})
        rows.append({"U": u, "even_checks": limit // 2,
                     "positive_harmonic_mass": str(hplus),
                     "negative_harmonic_mass": str(hminus),
                     "signed_harmonic_difference": str(hplus - hminus),
                     "floor_mean_records": means})
    demand(positive > 0 and negative > 0, "Both signs exercised")
    return {"identity_checks": identity_count,
            "repeated_two_power_checks": repeated_two,
            "positive_beta_sites": positive, "negative_beta_sites": negative,
            "fixtures": rows, "asymptotic_density_or_constants_tested": False}


def moment_checks():
    limit = 24000
    table = factor_table(limit)
    fixtures = []
    envelopes = 0
    for u, t in ((3, 2), (8, 2), (16, 4), (32, 5), (64, 8)):
        total = low = high = 0
        moments = {j: 0 for j in (1, 2, 3, 4)}
        for value in range(2, limit + 1):
            fs = table[value]
            beta = beta_from_factors(dict(fs), u)
            q = fs[0][0]
            total += beta * beta
            if q <= t:
                low += beta * beta
            else:
                high += beta * beta
            w = omega_u(fs, u)
            for j in (1, 2, 3, 4):
                B = 2 ** j
                f = B ** w if q > t else 0
                target = abs(beta) ** j if q > t else 0
                divisor = 1
                for _, e in fs:
                    divisor *= comb(e + B - 1, e)
                demand(target <= f <= divisor, "Actual-beta fixed moment multiplicative majorant")
                if q > t:
                    moments[j] += target
                envelopes += 1
        demand(total == low + high, "Exact full-interval energy partition")
        fixtures.append({"U": u, "T": t, "sites": limit - 1,
                         "total_beta_energy": total, "small_prime_energy": low,
                         "large_prime_energy": high,
                         "large_prime_absolute_moments": moments,
                         "asymptotic_selected_energy_bound_tested": False})
    return {"moment_envelope_checks": envelopes, "fixtures": fixtures,
            "selected_weighted_energy_inferred": False}


def exponent_certificates():
    stop = F(1) - F(19, 20) - (F(2) - F(19, 20)) / 30
    energy = F(1) - F(19, 20) - F(2, 100)
    alpha0, alpha1 = F(1, 5), F(1, 4)
    p0, p1 = F(3, 10), F(7, 20)
    product_margin = F(2) - alpha1 - CB
    bmin, bmax = F(2) - alpha1 - p1, F(2) - alpha0 - p0
    relmin = (F(1) - alpha1 - p1) / bmin
    relmax = (F(1) - alpha0 - p0) / bmax
    demand(stop == F(3, 200) and energy == F(3, 100), "Uniform full-stop margins")
    demand(product_margin == F(241, 400), "Actual large product gate margin")
    demand(p0 > F(1, 4) and p1 < F(19, 20) and alpha0 > F(1, 100),
           "Actual marked continuation cutoffs")
    demand(bmin == F(7, 5) and bmax == F(3, 2), "Reference prime cofactor exponents")
    demand(relmin == F(2, 7) and relmax == F(1, 3), "Short prime interval exponents")
    kappa = I.point(F(119, 99)).log() / 2
    delta = 1 - (1 + I.point(2).log().log()) / I.point(2).log()
    demand(kappa.lo > 0 and delta.lo > 0 and delta.hi < 1,
           "Outward coefficient and mass-scale gap")
    return {"full_stop_Shiu_margin": str(stop), "full_stop_beta_floor_margin": str(energy),
            "marked_outer_exponent_range": [str(p0), str(p1)],
            "marked_residual_exponent_range": [str(alpha0), str(alpha1)],
            "marked_product_gate_margin": str(product_margin),
            "reference_prime_center_exponents": [str(bmin), str(bmax)],
            "short_prime_relative_length_exponents": [str(relmin), str(relmax)],
            "kappa": kappa.record(), "source_support_exponent_delta": delta.record(),
            "reference_signed_floor_error_exponent": "81/100",
            "full_reference_PNT_required_relative_width": "rho=N^(-o(1)); not the short interval width",
            "all_rational_and_outward_checks_passed": True}


def is_prime(value, primes):
    if value < 2:
        return False
    for p in primes:
        if p * p > value:
            break
        if value % p == 0:
            return value == p
    return True


def marked_fixture(n, u, alow, ahigh, pvalues, wide=False):
    """Actual coefficients; enlarged c ranges are explicitly stress fixtures."""
    diameter = 3 * n if wide else n
    lo, hi = n * n - diameter // 2, n * n + diameter // 2
    prime_table = primes_up_to(isqrt(hi) + 1)
    small_table = factor_table(ahigh)
    demand(u ** 4 < n, "Stress U remains below z in this fixture")
    demand(alow >= u and all(is_prime(p, prime_table) and p > u for p in pvalues),
           "Stress marked residual and prime gates")
    by_tuples = defaultdict(F)
    positive = defaultdict(F)
    negative = defaultdict(F)
    tuple_sites = set()
    candidate_count = active = positive_rows = negative_rows = repeated_outer = 0
    for c in range(alow + 1, ahigh + 1):
        if c % 2:
            continue
        beta = beta_from_factors(dict(small_table[c]), u)
        for p in pvalues:
            multiplier = c * p
            first, last = (lo + multiplier - 1) // multiplier, hi // multiplier
            for b in range(first, last + 1):
                candidate_count += 1
                if not is_prime(b, prime_table):
                    continue
                value = multiplier * b
                fs = {}
                tmp = value
                for q in prime_table:
                    if q * q > tmp:
                        break
                    while tmp % q == 0:
                        fs[q] = fs.get(q, 0) + 1
                        tmp //= q
                if tmp > 1:
                    fs[tmp] = fs.get(tmp, 0) + 1
                demand(min(fs) == 2 and beta_from_factors(fs, u) == beta,
                       "Actual even beta invariance with both large primes removed")
                demand(not pow_le(p * b, n, CB), "Actual marked product gate")
                v, _, _ = actual_weights(value, fs, n, u)
                demand(v.get((p, b), 0) == 1, "Marked row coefficient exactly one in actual V")
                by_tuples[(p, b)] += beta
                positive[(p, b)] += max(beta, 0)
                negative[(p, b)] += max(-beta, 0)
                tuple_sites.add(value)
                active += 1
                positive_rows += beta > 0
                negative_rows += beta < 0
                repeated_outer += c % p == 0
    # Independent shell-factor enumeration reconstructs the selected rows.
    by_shell = defaultdict(F)
    nband = factor_band(lo, hi, prime_table)
    shell_sites = set()
    shell_rows = 0
    for value, fs in nband.items():
        if value % 2:
            continue
        beta = beta_from_factors(fs, u)
        for p in pvalues:
            if value % p:
                continue
            for b in fs:
                if b <= u or (value // p) % b:
                    continue
                c = value // (p * b)
                if c % 2 or not alow < c <= ahigh:
                    continue
                demand(not pow_le(p * b, n, CB), "Independent marked product gate")
                by_shell[(p, b)] += beta
                shell_sites.add(value)
                shell_rows += 1
    demand(cleaned(by_shell) == cleaned(by_tuples) and shell_sites == tuple_sites,
           "Independent exact prime-tuple/shell identity")
    demand(shell_rows == active, "Marked row enumeration counts agree")
    reconstructed = {key: positive[key] - negative[key] for key in set(positive) | set(negative)}
    demand(cleaned(reconstructed) == cleaned(by_tuples), "Actual marked sign decomposition")
    return {"N": n, "U": u, "stress_truncation": True,
            "actual_campaign_truncation": False,
            "stress_c_range": [alow + 1, ahigh], "marked_outer_primes": pvalues,
            "window": "artificial wider identity fixture" if wide else "actual square shell",
            "asymptotic_c_exponent_range_used": False,
            "shell_sites": hi - lo + 1, "prime_candidates": candidate_count,
            "active_marked_rows": active, "positive_beta_rows": positive_rows,
            "negative_beta_rows": negative_rows, "outer_prime_divides_residual_rows": repeated_outer,
            "formal_log_coefficients": len(cleaned(by_tuples)),
            "all_exact_row_checks_passed": True,
            "asymptotic_reference_lower_bounds_or_cancellation_tested": False}


def main():
    preservation = provenance()
    checks = {"checkpoint": 20, "date": DATE, "provenance": preservation,
              "even_pairing": even_pairing_checks(), "fixed_moments": moment_checks(),
              "exponent_certificates": exponent_certificates()}
    checks["marked_continuation_fixtures"] = [
        marked_fixture(1000, 3, 3, 60, [7, 11]),
        marked_fixture(100000, 16, 16, 240, [37, 41, 43, 47, 53]),
        marked_fixture(100000, 16, 16, 240, [37, 41, 43, 47, 53], wide=True),
    ]
    fixtures = checks["marked_continuation_fixtures"]
    demand(sum(x["positive_beta_rows"] for x in fixtures) > 0
           and sum(x["negative_beta_rows"] for x in fixtures) > 0,
           "Both actual marked beta signs exercised")
    demand(sum(x["outer_prime_divides_residual_rows"] for x in fixtures) > 0,
           "No spurious coprimality inserted in marked rows")
    checks["totals"] = {name: sum(x[name] for x in fixtures) for name in
                        ("shell_sites", "prime_candidates", "active_marked_rows",
                         "positive_beta_rows", "negative_beta_rows",
                         "outer_prime_divides_residual_rows")}
    checks["all_exact_checks_passed"] = True
    checks["terminal_0011_estimate_tested"] = False
    result = {
        "checkpoint": 20, "date": DATE,
        "note": "SMALL_PRIME_CANCELLATION_NOTE.md",
        "large_least_prime_all_fixed_absolute_moments_proved": True,
        "large_prime_moment_bound": "sum_rough_T |beta_U|^j <<_j H*(log U)^(2^j-1)/(log T)^(2^j); fixed T=U^epsilon gives <<_j epsilon^(-2^j)*H/log U",
        "small_prime_full_interval_beta_energy_localized": True,
        "small_prime_full_interval_beta_energy": "(L+o(1))*H on Pminus<=U^epsilon, for every fixed epsilon>0; full intervals only",
        "small_prime_selected_continuation_energy_bound_inferred": False,
        "actual_small_prime_reference_signed_u_scale_proved": True,
        "actual_small_prime_reference_signed_u_scale": "a*S_<=U^epsilon(B1)=O_epsilon(u)",
        "actual_even_continuation_reference_opposing_masses_proved": True,
        "reference_opposing_lower_bound": "Each sign >= c*N/((log U)^delta*(log log U)^(3/2)) on an actual q=2 continuation subweight",
        "reference_signed_subweight_cancellation_proved": True,
        "reference_signed_subweight_cancellation": "a*sum_B1 beta_U*W_N=o(u), W_N<=V_N; original coefficients and gates retained",
        "additional_source_input": "GKM 2021 Section1.1 isolated-divisor lower-bound construction, based on Ford2008; accepted published input, not independently reproved here",
        "separate_unsigned_reference_mass_charging_at_u_scale_excluded": True,
        "absolute_subtracted_kernel_discrepancy_excluded": False,
        "small_least_prime_short_signed_block_estimated_at_u_scale": False,
        "remaining_target": "E_small+E_large-E_rough <= (.011+o(1))*u with the unchanged original reference",
        "next_concrete_subproblem": "Signed short/reference estimate for the actual even marked rows (18), followed by all remaining small-q continuation sectors and their joint coefficient",
        "global_partial_log_exponent_unchanged": "0.06024782442318413...",
        "new_positive_prime_mass_credited": 0,
        "terminal_0011_estimate_proved": False, "H_theta_proved": False, "certified_K": 0,
        "higher_degree_cap_proved": False,
        "provenance": preservation,
        "finite_checks_scope": "Exact identities, formal prime/log row coefficients and rational hypotheses; asymptotic source inputs and constants are not computationally certified",
    }
    for name, data in (("small_prime_cancellation_checks.json", checks),
                       ("small_prime_cancellation.json", result)):
        (ROOT / "results" / name).write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"all_exact_checks_passed": True,
                      "even_pairing_checks": checks["even_pairing"]["identity_checks"],
                      "fixed_moment_envelope_checks": checks["fixed_moments"]["moment_envelope_checks"],
                      "marked_totals": checks["totals"],
                      "historical_records_preserved": preservation["checkpoint19_nonmutable_records_verified"],
                      "terminal_0011_estimate_proved": False}, indent=2))


if __name__ == "__main__":
    main()
