#!/usr/bin/env python3
"""Checkpoint 16: first-outer-prime stopping with the actual delta weights.

Checks exact arithmetic and coefficients of the formal symbols
X_(d,b)=log(b)/log(N^2/d). No floating logarithms enter the identity checks.
Finite fixtures do not prove the remaining one-sided covariance estimate.
Only this checkpoint's result files are written; historical inputs are read.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json

from cofactor_estimation import beta_from_factors, mobius_table
from delta_grouping import CB, good_outer, pow_le
from joint_remainder import factor_divisor, subtract_factors
from ross_geometry_audit import factor_band, primes_up_to
from two_three_frontier import divisors, outer_coefficient

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-10-08"
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}
LEDGER_HASH = "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"
CONSTANT = (0, 0)


def demand(condition, label):
    if not condition:
        raise AssertionError(label)


def cleaned(vector):
    return {key: value for key, value in vector.items() if value}


def add_vector(target, source, scale=F(1)):
    for key, value in source.items():
        target[key] += scale * value


def prime_factors(fs):
    """Distinct prime divisors, independent of their multiplicities."""
    return sorted(fs)


def is_prime_factorization(fs):
    return len(fs) == 1 and next(iter(fs.values())) == 1


def provenance():
    previous = json.loads((ROOT / "results/checkpoint15_preservation_manifest.json").read_text())
    demand(previous["checkpoint"] == 15, "Frozen checkpoint 15")
    count = 0
    for record in previous["files"]:
        if record["path"] in MUTABLE:
            continue
        path = ROOT / record["path"]
        demand(path.stat().st_size == record["size_bytes"], record["path"] + " size")
        demand(sha256(path.read_bytes()).hexdigest() == record["sha256"], record["path"] + " hash")
        count += 1
    demand(sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
           == LEDGER_HASH, "Frozen analytic ledger")
    return {"checkpoint_15_nonmutable_records_verified": count,
            "negative_frontier_ledger_sha256": LEDGER_HASH,
            "historical_analytic_ledger_unchanged": True}


def arithmetic_fixture(n, u, actual):
    demand(n % 2 == 0 and u ** 4 < n, "Fixture has p>U on actual outer support")
    if actual:
        demand(u ** 100 <= n < (u + 1) ** 100, "Exact campaign U")
    lo, hi = n * n - n // 2, n * n + n // 2
    all_primes = primes_up_to(isqrt(hi))
    factors = factor_band(lo, hi, all_primes)
    beta_n = {value: beta_from_factors(fs, u) for value, fs in factors.items()}
    mu = mobius_table(u)
    alpha = sum((F(mu[t], t) for t in mu), F(0))
    q = sum((F(mu[s] * mu[t], s * t // gcd(s, t)) for s in mu for t in mu), F(0))
    stop_primes = [p for p in all_primes if p ** 4 >= n and p ** 20 < n ** 19]
    good_cache, large_cache = {}, {}

    def good(d, df):
        if d not in good_cache:
            good_cache[d] = good_outer(d, df, n)
        return good_cache[d]

    def large(product):
        if product not in large_cache:
            large_cache[product] = not pow_le(product, n, CB)
        return large_cache[product]

    # Direct enumeration uses the historical outer coefficient and m>U.
    direct_b = defaultdict(F)
    direct_core = defaultdict(F)
    counts = Counter()
    for value, nf in factors.items():
        for d in divisors(nf):
            df = factor_divisor(nf, d)
            cd = outer_coefficient(df, n)
            if not cd:
                continue
            p = min(df)
            demand(p in stop_primes, "Every actual outer product has a safe first prime")
            k = value // p
            qf = subtract_factors(nf, df)
            cofactor = value // d
            if not good(d, df):
                if is_prime_factorization(qf):
                    direct_core[p, k] += cd
                    counts["direct_core_prime_rows"] += 1
                continue
            for b in prime_factors(qf):
                m = cofactor // b
                if b <= u or m <= u or not large(d * b):
                    continue
                mf = subtract_factors(qf, {b: 1})
                direct_b[p, k, d, b] += cd * beta_from_factors(mf, u)
                counts["direct_prime_b_rows"] += 1

    # Independent enumeration stops at p, retains all k in its full interval,
    # and puts the pair, continuation prime and sharp gates inside the weight.
    stopped_b = defaultdict(F)
    stopped_core = defaultdict(F)
    node_vectors = {}
    node_betas = {}
    local_moments = []
    beta_values = set()
    for p in stop_primes:
        k_lo, k_hi = (lo + p - 1) // p, hi // p
        h = k_hi - k_lo + 1
        demand(h >= 1 and h in (n // p, n // p + 1),
               "Exact progression site count")
        local_first = local_second = 0
        for k in range(k_lo, k_hi + 1):
            nf = factors[p * k]
            kf = subtract_factors(nf, {p: 1})
            beta = beta_from_factors(kf, u)
            demand(beta == beta_n[p * k], "Actual large-prime beta invariance")
            beta_values.add(beta)
            node_betas[p, k] = beta
            local_first += beta
            local_second += beta * beta
            vector = defaultdict(F)

            # Prime outer p: all these rows are in D_good.
            demand(good(p, {p: 1}), "Single-prime family is completely controlled")
            for b in prime_factors(kf):
                m = k // b
                if b <= u or m <= 1 or not large(p * b):
                    continue
                if m <= u:
                    demand(beta == 0, "The extended 1<m<=U rows vanish")
                    counts["zero_extension_rows"] += 1
                vector[p, b] += 1
                stopped_b[p, k, p, b] += beta
                counts["stopped_prime_b_rows"] += 1

            # Canonical pair outer pr, including the half-weight diagonal.
            for r in prime_factors(kf):
                if r < p or r ** 4 < n or p * r * r > n * n:
                    continue
                d = p * r
                df = {p: 2} if p == r else {p: 1, r: 1}
                cd = F(1, 2) if p == r else F(1)
                rf = subtract_factors(kf, {r: 1})
                if not good(d, df):
                    if is_prime_factorization(rf):
                        stopped_core[p, k] += cd
                        demand(beta == -1, "Core prime-cofactor rows have beta=-1")
                        vector[CONSTANT] -= cd
                        counts["stopped_core_prime_rows"] += 1
                    continue
                for b in prime_factors(rf):
                    m = k // (r * b)
                    if b <= u or m <= 1 or not large(d * b):
                        continue
                    if m <= u:
                        demand(beta == 0, "Extended pair rows vanish")
                        counts["zero_extension_rows"] += 1
                    vector[d, b] += cd
                    stopped_b[p, k, d, b] += cd * beta
                    counts["stopped_prime_b_rows"] += 1
            demand(stopped_core[p, k] <= 1, "At most one marked core cofactor per stopped site")
            node_vectors[p, k] = cleaned(vector)
            counts["stopped_sites"] += 1

        e1, e2 = F(local_first) + h * alpha, F(local_second) - h * q
        demand(abs(e1) <= u, "Uniform local first-moment floor error")
        demand(abs(e2) <= u * u, "Uniform local second-moment floor error")
        variance = F(local_second) - F(local_first * local_first, h)
        variance_error = variance - h * (q - alpha * alpha)
        demand(abs(variance_error) <= 4 * u * u, "Uniform centered-variance error")
        local_moments.append({"p": p, "H": h, "first_error": str(e1),
                              "second_error": str(e2), "variance_error": str(variance_error)})

    demand(cleaned(direct_b) == cleaned(stopped_b), "Independent formal Type II coefficient identity")
    demand(cleaned(direct_core) == cleaned(stopped_core), "Independent core prime count identity")

    # Verify joint identity in a separate per-node representation.
    direct_joint = defaultdict(F)
    for (p, k, d, b), coefficient in direct_b.items():
        direct_joint[p, k, (d, b)] += coefficient
    for (p, k), coefficient in direct_core.items():
        direct_joint[p, k, CONSTANT] += coefficient
    stopped_joint = defaultdict(F)
    for (p, k), vector in node_vectors.items():
        for symbol, coefficient in vector.items():
            stopped_joint[p, k, symbol] += node_betas[p, k] * coefficient
    demand(cleaned(direct_joint) == cleaned(stopped_joint), "Joint B+A=beta*(v-P) identity")

    # Formal exact centering: every X_(d,b) keeps its actual logarithmic factor.
    total_joint, total_covariance, total_means = defaultdict(F), defaultdict(F), defaultdict(F)
    for p in stop_primes:
        k_lo, k_hi = (lo + p - 1) // p, hi // p
        h = k_hi - k_lo + 1
        sum_beta = sum(node_betas[p, k] for k in range(k_lo, k_hi + 1))
        sum_z = defaultdict(F)
        for k in range(k_lo, k_hi + 1):
            add_vector(sum_z, node_vectors[p, k])
            add_vector(total_joint, node_vectors[p, k], node_betas[p, k])
        bar_z = {symbol: coefficient / h for symbol, coefficient in sum_z.items()}
        bar_beta = F(sum_beta, h)
        for k in range(k_lo, k_hi + 1):
            centered_z = defaultdict(F, node_vectors[p, k])
            add_vector(centered_z, bar_z, -1)
            add_vector(total_covariance, centered_z, node_betas[p, k] - bar_beta)
        add_vector(total_means, bar_z, sum_beta)
    restored = defaultdict(F, total_covariance)
    add_vector(restored, total_means)
    demand(cleaned(total_joint) == cleaned(restored), "Joint exact local-centering identity")

    return {"N": n, "U": u, "actual_campaign_truncation": actual,
            "fixture_scope": "exact prime-b frozen kernel; stress U is not an asymptotic campaign result",
            "stop_primes": len(stop_primes), "minimum_H": min(r["H"] for r in local_moments),
            "alpha_U": str(alpha), "q_U": str(q), "beta_values": sorted(beta_values),
            "counts": dict(counts), "nonzero_direct_formal_coefficients": len(cleaned(direct_b)),
            "maximum_first_error": str(max(abs(F(r["first_error"])) for r in local_moments)),
            "maximum_second_error": str(max(abs(F(r["second_error"])) for r in local_moments)),
            "maximum_centered_variance_error": str(max(abs(F(r["variance_error"])) for r in local_moments)),
            "all_independent_identities_passed": True, "terminal_covariance_estimate_tested": False}


def comparison_checks():
    lower, upper = F(34, 100), F(33, 100)
    epsilon = F(1, 100)
    margin = lower - upper * (1 + epsilon)
    demand(margin == F(67, 10000), "Flat positive weight margin")
    demand(lower - upper * (1 + F(1, 33)) == 0, "Exact flatness threshold")
    s, r, t = [F(0), F(17, 25)], [upper, upper], [F(1), F(1)]
    demand(sum(s) == lower * sum(t), "Counterexample satisfies grouped lower hypothesis")
    demand(all(ri <= upper * ti for ri, ti in zip(r, t)), "Counterexample reference caps")
    selected = s[0] - r[0]
    demand(selected == -upper and sum(s) - sum(r) == F(1, 50),
           "Sharp nonnegative selection can destroy the comparison")
    for p in (13, 17):
        fs = {7: 1, 11: 1, p: 1}
        demand(beta_from_factors(fs, 5) == -1, "Actual signed rough beta weight")
    return {"source_margins": {"grouped_lower": str(lower), "individual_reference_upper": str(upper)},
            "maximum_nonnegative_weight_ratio": "34/33",
            "epsilon_1_over_100_margin": str(margin),
            "selection_counterexample": {"S": [str(v) for v in s], "R": [str(v) for v in r],
                                         "T": [str(v) for v in t], "weights": [1, 0],
                                         "unweighted_correction": "1/50", "weighted_correction": str(selected),
                                         "scope": "counterexample to unrestricted weighted inference, not to result 021"},
            "signed_beta_example": {"U": 5, "k": 77, "tag_primes": [13, 17], "beta_pk": -1,
                                    "scope": "a positive correction changes sign under this actual beta weight"}}


def exponent_checks():
    minimum_width = 1 - F(19, 20)
    mean_error = F(1, 100) - minimum_width
    energy_error = F(2, 100) - minimum_width
    demand(minimum_width == F(1, 20), "Safe real progression width")
    demand(mean_error == -F(1, 25), "Uniform mean error exponent")
    demand(energy_error == -F(3, 100), "Uniform variance error exponent")
    demand(F(19, 20) + F(1, 100) == F(24, 25), "Summed first-moment floor loss")
    demand(F(19, 20) + F(2, 100) == F(97, 100), "Summed energy floor loss")
    return {"single_prime_stop_max_exponent": "19/20", "pair_first_prime_max_exponent": "2/3",
            "minimum_real_progression_width_exponent": str(minimum_width),
            "local_mean_error_exponent": str(mean_error), "local_variance_error_exponent": str(energy_error),
            "summed_first_moment_floor_exponent": "24/25", "summed_second_moment_floor_exponent": "97/100",
            "reference_sum_H_over_N": "log(19/5)", "moment_limit": "L>0 (previously admitted BDT input)",
            "progression_length_obstruction_avoided_at_first_prime": True,
            "conditional_continuation_weights_estimated": False}


def main():
    history = provenance()
    exponents = exponent_checks()
    comparisons = comparison_checks()
    fixtures = [arithmetic_fixture(n, u, actual) for n, u, actual in
                ((100, 1, True), (1000, 1, True), (10000, 1, True),
                 (1000, 3, False), (2000, 5, False), (10000, 5, False), (10000, 8, False))]
    checks = {"date": DATE, "checkpoint": 16, "all_checks_passed": True,
              "proof_note": "WEIGHTED_STOPPING_NOTE.md", "provenance": history,
              "exponent_certificates": exponents, "comparison_certificates": comparisons,
              "arithmetic_fixtures": fixtures,
              "aggregate_stopped_sites": sum(f["counts"]["stopped_sites"] for f in fixtures),
              "aggregate_direct_prime_b_rows": sum(f["counts"]["direct_prime_b_rows"] for f in fixtures),
              "aggregate_core_prime_rows": sum(f["counts"]["direct_core_prime_rows"] for f in fixtures),
              "terminal_0011_estimate_proved": False, "H_theta_proved": False, "certified_K": 0}
    state = json.loads((ROOT / "results/campaign_state.json").read_text())
    reduction = {"date": DATE, "checkpoint": 16,
                 "actual_parameters": {"x": "N^2", "J": "[N^2-N/2,N^2+N/2] intersect Z, even N",
                                       "U": "floor(N^(1/100))", "z": "N^(1/4)", "u": "N/(2 log N)"},
                 "stop": "canonical first outer prime p; full I_p={k:pk in J}",
                 "coefficients": "Z_p(k)=v_p(k)-P_core,p(k), all outer, ordering and db gates retained",
                 "exact_identity": "B_good,large + A_core = sum_(p,k) beta_U(k)*Z_p(k) + o(u)",
                 "centered_identity": "Delta_2+Delta_3 = C_N - (M_core+o(1))*u",
                 "C_N": "sum_p sum_(k in I_p) (beta_U(k)-mean_Ip(beta))*(Z_p(k)-mean_Ip(Z))",
                 "uniform_local_moments_proved": True, "uniform_moment_errors": exponents,
                 "summed_centering_error": "O(N*exp(-c*sqrt(log N))+N^(24/25))=o(u)",
                 "summed_centered_beta_energy": "(L*log(19/5)+o(1))*N",
                 "remaining_reference_coefficient": state["remaining_TypeI_core_reference"],
                 "remaining_one_sided_target": "C_N <= (M_core+11/1000+o(1))*u",
                 "optional_Cauchy_sufficient_variance": "sum_p sum_Ip |Z-mean_Ip(Z)|^2 <= ((M_core+.011)^2/(4*L*log(19/5))+o(1))*N/log(N)^2",
                 "positive_flat_weight_021_extension": "Ratio<=34/33 preserves the source grouped sign, under the same complete-owner hypotheses",
                 "actual_log_weight_extension_requires": "nonnegative weights, a full eligible bin and constant support/selection gates",
                 "signed_beta_or_sharp_selection_extension_proved": False,
                 "uniform_terminal_covariance_bound_proved": False, "terminal_0011_estimate_proved": False,
                 "new_lower_bound_mass_admitted": False, "H_theta_proved": False, "certified_K": 0}
    for name, value in (("weighted_stopping_checks.json", checks), ("weighted_stopping_reduction.json", reduction)):
        (ROOT / "results" / name).write_text(json.dumps(value, indent=2) + "\n")
    print(json.dumps({"checkpoint": 16, "all_checks_passed": True, "fixtures": len(fixtures),
                      "stopped_sites": checks["aggregate_stopped_sites"],
                      "prime_b_rows": checks["aggregate_direct_prime_b_rows"],
                      "core_prime_rows": checks["aggregate_core_prime_rows"],
                      "historical_records": history["checkpoint_15_nonmutable_records_verified"],
                      "terminal_estimate_proved": False}, indent=2))


if __name__ == "__main__":
    main()
