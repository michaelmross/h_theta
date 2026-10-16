#!/usr/bin/env python3
"""Checkpoint 21: exact checks for completed signed sums and fixed masks.

Finite checks verify arithmetic, coefficients, floors and proof scope.
They do not prove asymptotic cancellation, the marked slice, or .011u.
Historical modules are imported read-only. Only two new result files change.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json

from beta_support import factor_table, squarefree_divisors
from cofactor_estimation import beta_from_factors
from delta_grouping import CB, good_outer, pow_le
from joint_remainder import factor_divisor, subtract_factors, vaughan_vectors
from ross_geometry_audit import factor_band, primes_up_to
from signed_core_continuation import actual_weights, cleaned
from two_three_frontier import divisors, mu_from_factors, outer_coefficient

ROOT = Path(__file__).resolve().parents[1]
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}
LEDGER_HASH = "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def provenance():
    old = json.loads((ROOT / "results/checkpoint20_preservation_manifest.json").read_text())
    demand(old["checkpoint"] == 20 and len(old["files"]) == 230, "Frozen checkpoint 20")
    count = 0
    for rec in old["files"]:
        if rec["path"] in MUTABLE:
            continue
        raw = (ROOT / rec["path"]).read_bytes()
        demand(len(raw) == rec["size_bytes"] and sha256(raw).hexdigest() == rec["sha256"],
               rec["path"] + " unchanged")
        count += 1
    demand(count == 226, "226 unchanged historical nonmutable records")
    demand(sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
           == LEDGER_HASH, "Frozen negative-frontier ledger")
    return {"checkpoint20_nonmutable_records_verified": count,
            "negative_frontier_ledger_sha256": LEDGER_HASH}


def fixed_mask_algebra():
    table = factor_table(64)
    mu = [mu_from_factors(dict(fs)) for fs in table]
    fixtures = []
    for u in (3, 8, 16, 32, 64):
        def a(e):
            return sum((F(mu[t] * gcd(e, t), e * t) for t in range(1, u + 1)), F(0))
        for e in (1, 2, 3, 5, 6, 10, 30):
            es = dict(table[e])
            edivs = divisors(es)
            paired_a = F(0)
            paired_g, direct_g = defaultdict(F), defaultdict(F)
            for t in range(1, u + 1):
                for p, k in table[t]:
                    direct_g[p] += F(mu[t] * gcd(e, t) * k, e * t)
            for divisor in edivs:
                for s in range(1, u // divisor + 1):
                    if gcd(s, e) != 1:
                        continue
                    scale = F(mu[divisor] * mu[s], e * s)
                    paired_a += scale
                    for p, k in table[s]:
                        paired_g[p] += scale * k
                    for p, k in table[divisor]:
                        paired_g[p] += scale * k
            demand(a(e) == paired_a and cleaned(direct_g) == cleaned(paired_g),
                   "Exact coprime factorization of masked Type I density")
            direct_b, split_b = defaultdict(F), defaultdict(F)
            powers_in_e = 0
            for b in range(2, u + 1):
                if len(table[b]) != 1:
                    continue
                p, _ = table[b][0]
                inner = sum((F(mu[t] * gcd(e, t * b), e * t)
                             for t in range(1, u + 1)), F(0))
                direct_b[p] += inner / b
                split_b[p] += a(e // p if e % p == 0 else e) / b
                powers_in_e += e % p == 0
            demand(cleaned(direct_b) == cleaned(split_b),
                   "Exact prime-power Euler split including bases dividing e")
            fixtures.append({"U": u, "e": e, "a_e_exact": str(a(e)),
                             "g_e_log_coefficients": {str(p): str(v) for p, v in cleaned(direct_g).items()},
                             "b_e_log_coefficients": {str(p): str(v) for p, v in cleaned(direct_b).items()},
                             "small_prime_power_bases_dividing_e_exercised": powers_in_e,
                             "asymptotic_fixed_mask_hypotheses": max(es, default=1) <= u})
    return {"density_fixtures": fixtures, "exact_density_checks": 3 * len(fixtures)}


def lattice_and_union_checks():
    checks = floor_checks = 0
    for e in (1, 2, 3, 5, 6, 10, 30):
        for t in (1, 2, 3, 4, 5, 8, 15, 32, 64):
            for b in (1, 2, 4, 8, 9, 25, 49):
                h = e // gcd(e, t * b)
                for ell in range(1, 257):
                    demand((t * b * ell) % e == 0 if ell % h == 0
                           else (t * b * ell) % e != 0, "Exact fixed-modulus lattice")
                    checks += 1
                for lo, hi in ((1000, 1057), (9001, 9099), (40000, 40101)):
                    start, stop = (lo + t * b - 1) // (t * b), hi // (t * b)
                    exact = sum((t * b * ell) % e == 0 for ell in range(start, stop + 1))
                    floor = hi // (t * b * h) - (lo - 1) // (t * b * h)
                    demand(exact == floor, "Masked floor retains exact endpoints")
                    demand(abs(F(exact) - F(hi - lo + 1, t * b * h)) < 1,
                           "Uniform lattice discrepancy less than one")
                    floor_checks += 1
    table = factor_table(20000)
    union_checks = 0
    for q in (2, 3, 5, 7):
        ps = primes_up_to(q)
        mask = squarefree_divisors(tuple((p, 1) for p in ps))
        for value in range(2, len(table)):
            inclusion = -sum(mu for e, mu, _ in mask if e > 1 and value % e == 0)
            demand(inclusion == int(table[value][0][0] <= q), "Exact fixed least-prime union")
            union_checks += 1
    return {"fixed_lattice_checks": checks, "endpoint_floor_checks": floor_checks,
            "least_prime_union_checks": union_checks, "growing_moduli_estimate_inferred": False}


def actual_shell_fixture(n, u, wide=False):
    demand(u ** 4 < n, "Stress truncation below every outer prime")
    width = 3 * n if wide else n
    lo, hi = n * n - width // 2, n * n + width // 2
    bands = factor_band(lo, hi, primes_up_to(isqrt(hi)))
    es = [e for e in (2, 3, 5, 6, 10, 30) if max(dict(factor_table(30)[e])) <= u]
    sums = {e: {key: defaultdict(F) for key in ("A", "I", "B")} for e in es}
    counts = defaultdict(int)
    signed_even, signed_mark, signed_complement = defaultdict(F), defaultdict(F), defaultdict(F)
    positive = negative = repeated = 0
    for value, fs in bands.items():
        prime_count = F(0)
        beta = beta_from_factors(fs, u)
        v, _, _ = actual_weights(value, fs, n, u)
        for d, b in v:
            df = factor_divisor(fs, d)
            mf = subtract_factors(subtract_factors(fs, df), {b: 1})
            demand(beta == beta_from_factors(mf, u), "Actual residual beta invariance")
            repeated += fs.get(b, 0) > 1
            if value % 2 == 0:
                signed_even[d, b] += beta * v[d, b]
                c = value // (d * b)
                # Explicit enlarged residual cut, solely an exact identity fixture.
                marked = len(df) == 1 and sum(df.values()) == 1 and c % 2 == 0 and 2 * u < c <= 32 * u
                (signed_mark if marked else signed_complement)[d, b] += beta * v[d, b]
                positive += marked and beta > 0
                negative += marked and beta < 0
        for d in divisors(fs):
            df = factor_divisor(fs, d)
            weight = outer_coefficient(df, n)
            if not weight:
                continue
            qf = subtract_factors(fs, df)
            q = value // d
            prime = len(qf) == 1 and next(iter(qf.values())) == 1
            prime_count += weight if prime else F(0)
            if not good_outer(d, df, n):
                continue
            active = [e for e in es if value % e == 0]
            if not active:
                continue
            first, second, bilinear, target, _ = vaughan_vectors(qf, u, u)
            for e in active:
                demand(gcd(e, d) == 1, "Fixed mask is coprime to actual outer support")
                if target:
                    demand(len(dict(factor_table(30)[e])) == 1 and
                           next(iter(qf)) == e and next(iter(qf.values())) > 1,
                           "Masked Mangoldt cofactor is a proper power of the fixed prime")
                    counts['masked_proper_cofactor_power_rows'] += 1
                for p in qf:
                    sums[e]["A"][q, p] += weight * target.get(p, 0)
                    sums[e]["I"][q, p] += weight * (first[p] + second[p])
                    sums[e]["B"][q, p] += weight * bilinear[p]
                counts['masked_outer_cofactor_rows'] += 1
        rough = min(fs) ** 4 >= n
        demand(0 <= prime_count <= (3 if rough else 0), "Actual prime-cofactor mark bounded by 3*rough_z")
        counts['prime_mark_cap_sites'] += 1
        counts['prime_marked_sites'] += prime_count > 0
    for e, terms in sums.items():
        keys = set().union(*(set(v) for v in terms.values()))
        demand(all(terms['A'][k] == terms['I'][k] + terms['B'][k] for k in keys),
               "Completed masked Vaughan sum with original logarithmic coefficients")
    keys = set(signed_even) | set(signed_mark) | set(signed_complement)
    demand(all(signed_even[k] == signed_mark[k] + signed_complement[k] for k in keys),
           "Marked residual slice plus complementary continuation, exact coefficients")
    return {"N": n, "U": u, "actual_shell": not wide,
            "stress_U": u != 1, "artificial_reference_width": width if wide else None,
            "mask_values": es, "counts": dict(counts),
            "signed_marked_log_coefficients_positive": sum(v > 0 for v in signed_mark.values()),
            "signed_marked_log_coefficients_negative": sum(v < 0 for v in signed_mark.values()),
            "marked_positive_rows": positive, "marked_negative_rows": negative,
            "repeated_prime_b_rows": repeated,
            "marked_slice_asymptotic_estimate_inferred": False}


def marked_floor_fixture():
    n, u, alow, ahigh = 200000, 16, 64, 512
    ps = [p for p in primes_up_to(72) if 41 <= p <= 71]
    lo, hi = n * n - n // 2, n * n + n // 2
    table = factor_table(ahigh)
    trial = primes_up_to(isqrt(hi // ((alow + 1) * min(ps))) + 1)
    prime_cache = {}
    def prime(b):
        if b not in prime_cache:
            prime_cache[b] = b >= 2 and all(b % p for p in trial if p * p <= b)
        return prime_cache[b]
    direct, paired = defaultdict(F), defaultdict(F)
    all_pb = set()
    counts = defaultdict(int)
    for c in range(alow + 1, ahigh + 1):
        if c % 2:
            continue
        beta = beta_from_factors(dict(table[c]), u)
        for p in ps:
            demand(outer_coefficient({p: 1}, n) == 1, "Marked original outer coefficient")
            for b in range((lo + c * p - 1) // (c * p), hi // (c * p) + 1):
                counts['prime_candidates'] += 1
                if not prime(b):
                    continue
                demand(b > u and not pow_le(p * b, n, CB), "Marked original continuation gates")
                fs = dict(table[c]); fs[p] = fs.get(p, 0) + 1; fs[b] = fs.get(b, 0) + 1
                demand(beta_from_factors(fs, u) == beta, "Marked original beta weight")
                direct[p, b] += beta
                all_pb.add((p, b))
                counts['marked_prime_rows'] += 1
                counts['positive_rows'] += beta > 0
                counts['negative_rows'] += beta < 0
                counts['outer_prime_divides_residual'] += c % p == 0
    for p, b in sorted(all_pb):
        for d in range(u // 2 + 1, u + 1):
            if d % 2 == 0:
                continue
            mu = mu_from_factors(dict(table[d]))
            denominator = 2 * d * p * b
            ell_lo = max(alow // (2 * d) + 1, (lo + denominator - 1) // denominator)
            ell_hi = min(ahigh // (2 * d), hi // denominator)
            count = max(0, ell_hi - ell_lo + 1)
            demand(hi - lo < denominator and count <= 1, "Spiky marked floor interval")
            paired[p, b] -= mu * count
            counts['marked_endpoint_floor_rows'] += 1
    demand(cleaned(direct) == cleaned(paired), "Independent original marked sum equals paired endpoint floors")
    demand(counts['positive_rows'] > 0 and counts['negative_rows'] > 0, "Both marked signs exercised")
    return {"N": n, "U": u, "even_residual_stress_range": [alow, ahigh],
            "prime_outer_values": ps, "counts": dict(counts),
            "original_weights_and_gates_retained": True,
            "enlarged_residual_range_is_stress_fixture": True,
            "short_prime_PNT_or_marked_cancellation_inferred": False}


def exponent_checks():
    sigma_lo, sigma_hi = F(2) - F(1, 4) + F(1, 100), F(2) - F(1, 5) + F(1, 100)
    demand((sigma_lo, sigma_hi) == (F(44, 25), F(181, 100)), "Marked paired floor denominator exponents")
    raw_barrier = sigma_lo - F(5, 4)
    demand(raw_barrier == F(51, 100), "Direct reciprocal-source top-frequency gap")
    margins = {"minimum_TypeI_source_margin": F(1, 10000),
               "minimum_low_product_TypeII_source_margin": F(9, 14000)}
    # A fixed h changes every exponent by O_e(1/log N); finite positive margins survive.
    demand(all(m > 0 for m in margins.values()), "Strict inherited margins for fixed masks")
    return {"paired_marked_denominator_exponents": [str(sigma_lo), str(sigma_hi)],
            "direct_RS_FI_top_frequency_gap": str(raw_barrier),
            "fixed_mask_strict_inherited_source_margins": {k: str(v) for k, v in margins.items()},
            "fixed_mask_modulus": "e fixed; h=e/gcd(e,t*b) is a divisor of e",
            "growing_Q_or_modulus_uniformity_proved": False}


def main():
    checks = {"checkpoint": 21, "date": "2026-10-09", "provenance": provenance(),
              "fixed_mask_density": fixed_mask_algebra(),
              "lattice_and_union": lattice_and_union_checks(),
              "actual_shell_fixtures": [actual_shell_fixture(5000, 3),
                                        actual_shell_fixture(5000, 3, wide=True),
                                        actual_shell_fixture(18000, 5),
                                        actual_shell_fixture(100000, 16)],
              "marked_floor_identity": marked_floor_fixture(),
              "exponent_certificates": exponent_checks(), "all_exact_checks_passed": True,
              "finite_tests_prove_asymptotic_estimates": False}
    estimate = {"checkpoint": 21, "date": "2026-10-09",
                "proof_note": "MARKED_EVEN_COMPLETION_NOTE.md",
                "actual_covariance_completed_uniform_bound": "O(u)",
                "small_least_prime_signed_block_estimated_at_u_scale": True,
                "small_least_prime_signed_discrepancy_bound": "O_epsilon(u), T=U^epsilon, fixed epsilon>0",
                "complete_even_continuation_uniform_signed_bound": "o(u)",
                "each_fixed_squarefree_divisibility_mask_uniform_signed_bound": "o_e(u), e>1 fixed",
                "fixed_least_prime_union_signed_bound": "o_Q(u), Q fixed",
                "complete_marked_outer_prime_band_even_sector_bound": "o(u), with all even residuals and original continuation gates",
                "marked_and_complementary_residual_discrepancy_relation": "E_mark=-E_complement+o(u)",
                "marked_residual_slice_uniform_u_scale_proved": False,
                "marked_residual_slice_completed_o_u_inferred": False,
                "growing_least_prime_cutoff_negligibility_proved": False,
                "growing_cutoff_flag_scope": "No explicit quantitative range; a non-effective sufficiently slowly growing cutoff follows by diagonalization",
                "old_eta_scope": "Direct actual-beta absolute L1 estimate; no longer the best bound for the completed signed covariance",
                "terminal_0011_estimate_proved": False, "sharp_0011_coefficient_proved": False,
                "higher_degree_cap_proved": False, "H_theta_proved": False, "certified_K": 0}
    for name, data in (("marked_even_completion_checks.json", checks),
                       ("marked_even_completion.json", estimate)):
        (ROOT / "results" / name).write_text(json.dumps(data, indent=2) + "\n")
    total = sum(r['counts']['prime_mark_cap_sites'] for r in checks['actual_shell_fixtures'])
    print(json.dumps({"all_exact_checks_passed": True, "prime_mark_cap_sites": total,
                      "masked_outer_rows": sum(r['counts']['masked_outer_cofactor_rows'] for r in checks['actual_shell_fixtures']),
                      "density_checks": checks['fixed_mask_density']['exact_density_checks'],
                      "marked_floor_rows": checks['marked_floor_identity']['counts'],
                      "terminal_0011_estimate_proved": False}))


if __name__ == "__main__":
    main()
