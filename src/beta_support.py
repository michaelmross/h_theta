#!/usr/bin/env python3
"""Checkpoint 17: exact checks for a uniform partial logarithmic saving.

Standard library only. Finite identities do not prove the analytic density
bound. The proof in BETA_SUPPORT_ESTIMATE_NOTE.md uses the all-interval
uniform Shiu input and the inherited actual-beta second moment.
This script writes only this checkpoint's two result files.
"""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json

from structured_frontier import I

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-10-08"
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}
LEDGER_HASH = "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def provenance():
    manifest = json.loads((ROOT / "results/checkpoint16_preservation_manifest.json").read_text())
    demand(manifest["checkpoint"] == 16, "Frozen checkpoint 16")
    count = 0
    for record in manifest["files"]:
        if record["path"] in MUTABLE:
            continue
        payload = (ROOT / record["path"]).read_bytes()
        demand(len(payload) == record["size_bytes"], record["path"] + " size")
        demand(sha256(payload).hexdigest() == record["sha256"], record["path"] + " hash")
        count += 1
    demand(count == 199, "199 historical records")
    demand(sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
           == LEDGER_HASH, "Historical analytic ledger")
    sources = json.loads((ROOT / "sources/beta_support/SOURCE_MANIFEST.json").read_text())
    for record in sources["records"]:
        payload = (ROOT / record["path"]).read_bytes()
        demand(len(payload) == record["size_bytes"], "New source size")
        demand(sha256(payload).hexdigest() == record["sha256"], "New source hash")
    return {"checkpoint_16_nonmutable_records_verified": count,
            "new_source_records_verified": len(sources["records"]),
            "negative_frontier_ledger_sha256": LEDGER_HASH,
            "historical_analytic_ledger_unchanged": True}


def factor_table(limit):
    """Sieve of smallest primes; multiplicities retained independently of beta."""
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    factors = [()] * (limit + 1)
    for n in range(2, limit + 1):
        m = n
        fs = []
        while m > 1:
            p = spf[m]
            exponent = 0
            while m % p == 0:
                m //= p
                exponent += 1
            fs.append((p, exponent))
        factors[n] = tuple(fs)
    return factors


def squarefree_divisors(fs):
    """Independent Mobius divisor expansion from subsets of distinct primes."""
    ds = [(1, 1, ())]
    for p, _ in fs:
        ds += [(d * p, -mu, ps + (p,)) for d, mu, ps in ds]
    return ds


def omega_u(fs, u):
    return sum(p <= u for p, _ in fs)


def exact_arithmetic():
    limit = 60000
    cutoffs = [2, 3, 5, 8, 16, 32, 64, 128, 256, 4096]
    factors = factor_table(limit)
    beta_rows = prime_pair_rows = witness_rows = overlap_rows = 0
    repeated_q_rows = shared_d_rows = 0
    examples = []
    beta_values = {u: [0] * (limit + 1) for u in cutoffs}
    for k in range(2, limit + 1):
        fs = factors[k]
        ds = squarefree_divisors(fs)
        q = fs[0][0]
        for u in cutoffs:
            # Defining large-divisor sum, as opposed to a short-sum routine.
            beta = sum(mu for d, mu, _ in ds if d > u)
            short = -sum(mu for d, mu, _ in ds if d <= u)
            demand(beta == short, "Large/short beta identity")
            beta_values[u][k] = beta
            beta_rows += 1
            for r, _ in fs:
                paired = -sum(mu for d, mu, _ in ds if d % r and u < r * d and d <= u)
                demand(beta == paired, "Arbitrary-prime pairing identity")
                prime_pair_rows += 1
            Q = isqrt(isqrt(u))
            if q > Q:
                continue
            eligible = [(d, mu, ps) for d, mu, ps in ds
                        if d % q and u < q * d and d <= u]
            if beta:
                demand(bool(eligible), "Boundary divisor exists")
                demand(all(not ps or min(ps) > q for _, _, ps in eligible),
                       "Divisor has primes strictly above least prime")
                witness_rows += 1
            for d, _, ps in eligible:
                m = k // (q * d)
                demand(k == q * d * m and m >= 1, "Exact product")
                demand(not factors[m] or factors[m][0][0] >= q, "Remaining m is q-rough")
                lhs = omega_u(fs, u)
                g_exponent = omega_u(factors[m], u) - len(factors[gcd(m, d * q)])
                demand(g_exponent >= 0, "Nonnegative envelope exponent")
                demand(lhs == 1 + len(ps) + g_exponent, "Exact overlap exponent identity")
                overlap_rows += 1
                repeated = m % q == 0
                shared = gcd(d, m) > 1
                repeated_q_rows += repeated
                shared_d_rows += shared
                if (repeated or shared) and len(examples) < 12:
                    examples.append({"k": k, "U": u, "q": q, "d": d, "m": m,
                                     "q_divides_m": repeated, "gcd_d_m": gcd(d, m),
                                     "omega_U_k": lhs, "g_exponent": g_exponent})
    demand(repeated_q_rows > 0 and shared_d_rows > 0, "Both overlap types exercised")
    fixtures = []
    for u, lo, length in [(8, 10000, 2501), (16, 18000, 12001),
                          (32, 5000, 45001), (64, 100, 55000)]:
        bs = beta_values[u][lo:lo + length]
        support = sum(b != 0 for b in bs)
        first = sum(bs)
        absolute = sum(abs(b) for b in bs)
        second = sum(b * b for b in bs)
        demand(absolute * absolute <= support * second, "Support Cauchy identity")
        centered = sum((F(b) - F(first, length)) ** 2 for b in bs)
        demand(centered == F(second) - F(first * first, length), "Exact centered energy")
        fixtures.append({"U": u, "first_site": lo, "site_count": length,
                         "support_count": support, "sum_beta": first,
                         "sum_abs_beta": absolute, "sum_beta_squared": second,
                         "support_Cauchy_slack": support * second - absolute * absolute,
                         "centered_energy": str(centered),
                         "scope": "Finite identity fixture; not an asymptotic density test"})
    return {"integer_range": [2, limit], "stress_cutoffs": cutoffs,
            "large_vs_short_beta_rows": beta_rows,
            "arbitrary_prime_pairing_rows": prime_pair_rows,
            "nonzero_least_prime_witness_rows": witness_rows,
            "exact_overlap_exponent_rows": overlap_rows,
            "q_divides_m_rows": repeated_q_rows,
            "gcd_d_m_greater_than_one_rows": shared_d_rows,
            "overlap_examples": examples,
            "finite_support_and_energy_fixtures": fixtures}


def parameter_certificate():
    log2 = I.point(2).log()
    lam = 1 / log2
    t = lam / 2
    delta = 1 - lam + lam * lam.log()
    original_delta = 1 - (1 + log2.log()) / log2
    high = lam - 1 - lam * lam.log()
    low = 2 * t - 2 - lam * t.log()
    demand(lam.lo > 1 and lam.hi < 2, "1 < lambda < 2")
    demand(t.lo > F(1, 2) and t.hi < 1, "1/2 < t < 1")
    demand(delta.lo > 0 and delta.hi < 1, "0 < delta < 1")
    for interval in [delta - original_delta, high + delta, low + delta, lam * log2 - 1]:
        demand(interval.lo <= 0 <= interval.hi, "Outward algebra consistency")
    vertices = []
    for a in [F(1, 4), F(19, 20)]:
        for s in [F(0), F(1, 80)]:
            width = 1 - a - s
            center = 2 - a - s
            margin = width - center / 30
            demand(margin >= F(7, 2400), "Uniform scaled Shiu width margin")
            demand(center > F(1, 100), "U below every scaled center")
            demand(1 - a - F(2, 100) >= F(3, 100), "Inherited beta2 floor margin")
            vertices.append({"a": str(a), "s": str(s), "width_exponent": str(width),
                             "center_exponent": str(center), "Shiu_margin": str(margin)})
    return {"lambda": lam.record(), "t": t.record(), "delta": delta.record(),
            "covariance_log_saving_exponent": (delta / 2).record(),
            "high_support_exponent": high.record(), "low_support_exponent": low.record(),
            "scaled_interval_vertices": vertices,
            "minimum_Shiu_width_margin": "7/2400",
            "fixed_Shiu_interval_exponent": "1/30",
            "prime_series_block_exponent": lam.record(),
            "remaining_log_power_to_reach_u": (1 - delta / 2).record(),
            "transcendental_values_enclosed_outward": True}


def main():
    p = provenance()
    arithmetic = exact_arithmetic()
    parameters = parameter_certificate()
    checks = {"date": DATE, "checkpoint": 17, "all_checks_passed": True,
              "provenance": p, "arithmetic": arithmetic, "parameters": parameters,
              "analytic_claims_verified_by_finite_tests": False,
              "analytic_proof_note": "BETA_SUPPORT_ESTIMATE_NOTE.md"}
    estimate = {
        "date": DATE, "checkpoint": 17,
        "actual_U": "floor(N^(1/100))",
        "uniformity": "Every sufficiently large even N; all actual first-prime stopped intervals",
        "new_source_input": {"author": "Alexander P. Mangerel", "year": 2023,
                             "statement": "Lemma 3.2 (Shiu), fixed divisor-bound parameters B=2,C=1",
                             "url": "https://doi.org/10.1007/s40687-023-00376-0",
                             "source_page": "PDF page 13", "all_interval_bound": True,
                             "almost_all_theorem_used": False},
        "support_bound": "#{k in I_p: beta_U(k)!=0} << H_p/(log U)^delta",
        "absolute_beta_bound": "sum_(I_p)|beta_U| << H_p/(log U)^(delta/2)",
        "actual_covariance_bound": "|C_N| << N/(log N)^(delta/2)",
        "delta_formula": "1-(1+log(log(2)))/log(2)",
        "parameters": parameters,
        "actual_beta_support_bound_proved": True,
        "actual_beta_L1_log_saving_proved": True,
        "actual_covariance_partial_log_saving_proved": True,
        "actual_gates_retained": True,
        "repeated_and_shared_prime_factors_retained": True,
        "beta_treated_as_multiplicative": False,
        "historical_second_moment_input_strengthened": False,
        "new_numeric_core_mass_credit": 0,
        "remaining_interface": "Delta_2+Delta_3=C_N-(M_core+o(1))*u",
        "required_one_sided_bound": "C_N <= (M_core+.011+o(1))*u",
        "terminal_0011_estimate_proved": False,
        "covariance_estimated_at_u_scale": False,
        "higher_degree_cap_proved": False, "H_theta_proved": False, "certified_K": 0,
        "next_analytic_target": "Signed actual continuation/core estimate on the small-prime boundary-divisor configurations; recover the remaining logarithmic power and terminal coefficient",
        "checks": "results/beta_support_checks.json", "provenance": p,
        "proof_note": "BETA_SUPPORT_ESTIMATE_NOTE.md"}
    for name, data in [("beta_support_checks.json", checks), ("beta_support_estimate.json", estimate)]:
        (ROOT / "results" / name).write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"all_checks_passed": True,
                      "beta_identity_rows": arithmetic["large_vs_short_beta_rows"],
                      "prime_pairing_rows": arithmetic["arbitrary_prime_pairing_rows"],
                      "overlap_rows": arithmetic["exact_overlap_exponent_rows"],
                      "delta": parameters["delta"],
                      "covariance_log_exponent": parameters["covariance_log_saving_exponent"],
                      "historical_records_unchanged": p["checkpoint_16_nonmutable_records_verified"],
                      "terminal_0011_estimate_proved": False}, indent=2))


if __name__ == "__main__":
    main()
