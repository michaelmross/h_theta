#!/usr/bin/env python3
"""Checkpoint 13: actual cofactor weights, uniform Gram bounds, Type I strips.

The uniform analytic arguments are in COFACTOR_ESTIMATE_NOTE.md. These
checks verify exact identities and all vertices of the continuous source
regions. Finite fixtures do not prove the remaining .011u estimate.
"""

from __future__ import annotations

from collections import defaultdict, Counter
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json

from joint_remainder import (
    vertices, rs_margins, fi_margins, factor_divisor, subtract_factors,
    vaughan_vectors,
)
from ross_geometry_audit import factor_band, primes_up_to
from structured_frontier import I, NEAR
from two_three_frontier import divisors, mu_from_factors, outer_coefficient

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-10-07"
NU = F(1, 10000)
SIGMA_MAX = F(113, 100)
TOTAL_MAX = F(1153, 1000)
TYPEII_PRODUCT_MAX = F(1143, 1000)
MUTABLE = {
    "README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
    "results/campaign_state.json",
}


def demand(value, label):
    if not value:
        raise AssertionError(label)


def hash_file(path):
    return sha256(path.read_bytes()).hexdigest()


def provenance():
    previous = json.loads(
        (ROOT / "results/checkpoint12_preservation_manifest.json").read_text()
    )
    demand(previous["checkpoint"] == 12, "Frozen checkpoint 12")
    checked = 0
    for rec in previous["files"]:
        if rec["path"] in MUTABLE:
            continue
        path = ROOT / rec["path"]
        demand(path.stat().st_size == rec["size_bytes"], rec["path"])
        demand(hash_file(path) == rec["sha256"], rec["path"])
        checked += 1
    sources = json.loads(
        (ROOT / "sources/cofactor_estimation/SOURCE_MANIFEST.json").read_text()
    )
    for rec in sources["records"]:
        path = ROOT / rec["path"]
        demand(path.stat().st_size == rec["size_bytes"], rec["path"])
        demand(hash_file(path) == rec["sha256"], rec["path"])
    demand(hash_file(ROOT / "results/negative_frontier_ledger.json") ==
           "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
           "Frozen analytic ledger")
    return {"historical_files_verified_unchanged": checked,
            "new_primary_sources_verified": len(sources["records"]),
            "historical_numerical_ledger_unchanged": True}


def constraint(row, bound):
    # Every entry must be Fraction before Gaussian elimination: integer
    # division in the reused vertex routine would otherwise produce floats.
    return tuple(F(v) for v in row), F(bound)


def facet_certificates():
    base = [
        constraint((-1, 0, 0), -F(19, 20)),
        constraint((1, 0, 0), SIGMA_MAX),
        constraint((0, -1, 0), -F(1, 4)),
        constraint((-F(1, 2), 1, 0), 0),
        constraint((0, 0, -1), 0),
        constraint((1, 0, 1), TOTAL_MAX),
    ]
    # alpha = ((15*Sigma-13)/14)+(3/2)*nu, the midpoint between
    # the strongest FI upper facet and RS lower facet in this region.
    split = constraint((-F(15, 14), 1, -F(15, 14)),
                       -F(13, 14) + 3 * NU / 2)
    domains = [
        ("RS_low_total", "RS",
         base + [constraint((1, 0, 1), F(11, 10))]),
        ("FI_high_total_small_prime", "FI6",
         base + [constraint((-1, 0, -1), -F(11, 10)), split]),
        ("RS_high_total_larger_prime", "RS",
         base + [constraint((-1, 0, -1), -F(11, 10)),
                 constraint(tuple(-v for v in split[0]), -split[1])]),
    ]
    result = []
    for name, engine, cs in domains:
        branches = [(cs, "above_one")]
        if engine == "RS":
            branches = [
                (cs + [constraint((1, 0, 1), 1)], "below_one"),
                (cs + [constraint((-1, 0, -1), -1)], "above_one"),
            ]
        points, minima = [], {}
        for branch, side in branches:
            for sigma, alpha, delta in vertices(branch):
                demand(all(isinstance(v, F) for v in (sigma, alpha, delta)),
                       "Only exact rational vertices")
                eta = max(F(0), sigma + delta - 1) + NU
                margins = (rs_margins if engine == "RS" else fi_margins)(
                    sigma, alpha, delta, eta)
                demand(all(v > 0 for v in margins.values()), "Strict source margins")
                for term, value in margins.items():
                    minima[term] = min(minima.get(term, value), value)
                points.append({
                    "sigma": str(sigma), "alpha": str(alpha),
                    "delta": str(delta), "eta_top": str(eta), "branch": side,
                    "margins": {k: str(v) for k, v in margins.items()},
                })
        demand(bool(points), "Nonempty source region")
        result.append({
            "region": name, "engine": engine,
            "constraints": [{"A": [str(v) for v in a], "bound": str(b)}
                            for a, b in cs],
            "vertices": points,
            "minimum_margins": {k: str(v) for k, v in minima.items()},
            "minimum_over_all_facets": str(min(minima.values())),
        })
    demand(SIGMA_MAX + F(1, 50) <= TOTAL_MAX, "Both Type I truncations fit")
    demand(TYPEII_PRODUCT_MAX + F(1, 100) == TOTAL_MAX, "Type II strip fits")
    demand(F(49, 50) + F(1, 100) < 1, "Elementary product strip saves")
    demand(min(F(r["minimum_over_all_facets"]) for r in result) == F(3, 5600),
           "Source-region minimum")
    return {
        "coordinates": ["outer prime-pair sigma", "smaller-prime alpha",
                        "remaining denominator-product delta"],
        "frequency_extension": str(NU), "total_denominator_max": str(TOTAL_MAX),
        "complete_TypeI_outer_cutoff": str(SIGMA_MAX),
        "TypeII_product_strip_max": str(TYPEII_PRODUCT_MAX),
        "regions": result, "all_margins_strictly_positive": True,
        "affine_vertex_checks": sum(len(r["vertices"]) for r in result),
        "moving_ordering_gate_requires_Mellin_separation": True,
        "separation_argument": "COFACTOR_ESTIMATE_NOTE.md section 6",
        "terminal_full_remainder_proved": False,
    }


def partitions(total, minimum=1):
    if total == 0:
        yield ()
    for first in range(minimum, total + 1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def combinatorial_outer_bound():
    count = 0
    maximum = F(0)
    for omega in range(8):
        for es in partitions(omega):
            distinct = len(es)
            unrestricted = F(distinct + distinct * (distinct - 1) // 2)
            unrestricted += F(sum(e >= 2 for e in es), 2)
            demand(unrestricted <= omega + F(omega * (omega - 1), 2),
                   "Actual prime/square/two-prime weights")
            maximum = max(maximum, unrestricted)
            count += 1
    demand(maximum == 28, "Seven-large-factor extremum")
    return {"multiplicity_patterns_checked": count,
            "maximum_unrestricted_sum_c": str(maximum),
            "gamma_over_c_upper": "3/2", "proper_outer_weight_upper": "42"}


def beta_from_factors(fs, u):
    return sum(mu_from_factors(factor_divisor(fs, d))
               for d in divisors(fs) if d > u)


def mobius_table(u):
    fs = factor_band(1, u, primes_up_to(isqrt(u)))
    return {n: mu_from_factors(fs[n]) for n in range(1, u + 1)}


def overlap(n, u, q, k, ell):
    low = max(q + 1, u + 1, (n * n - n // 2 + k - 1) // k,
              (n * n - n // 2 + ell - 1) // ell)
    high = min(2 * q, (n * n + n // 2) // k,
               (n * n + n // 2) // ell)
    return max(0, high - low + 1)


def sqrt_interval(value):
    demand(value.lo >= 0, "Nonnegative square root")
    lo = NEAR.sqrt(value.lo)
    hi = NEAR.sqrt(value.hi)
    return I(max(I.point(0).lo, NEAR.next_minus(lo)), NEAR.next_plus(hi))


def exact_fixture(n, u, actual_truncation):
    demand(n % 2 == 0 and u ** 4 < n, "Outer factors exceed truncation")
    if actual_truncation:
        demand(u ** 100 <= n < (u + 1) ** 100, "Exact campaign truncation")
    low, high = n * n - n // 2, n * n + n // 2
    factors = factor_band(low, high, primes_up_to(isqrt(high)))
    mu = mobius_table(u)
    alpha_u = sum((F(mu[t], t) for t in mu), F(0))
    q_u = sum((F(mu[s] * mu[t], s * t // gcd(s, t))
               for s in mu for t in mu), F(0))
    bs = [beta_from_factors(f, u) for f in factors.values()]
    energy = sum(v * v for v in bs)
    first = sum(bs)
    demand(abs(F(energy) - (n + 1) * q_u) <= u * u,
           "Actual-window beta second-moment floor error")
    demand(abs(F(first) + (n + 1) * alpha_u) <= u,
           "Actual-window beta first-moment floor error")

    outer_cache = {}
    alpha_cache = {}
    gamma_cache = {}
    coefficient_checks = 0
    sign_values = set()
    rows = defaultdict(list)

    def c(d, df):
        if d not in outer_cache:
            outer_cache[d] = outer_coefficient(df, n)
        return outer_cache[d]

    def alpha_data(k, kf):
        nonlocal coefficient_checks
        if k in alpha_cache:
            return alpha_cache[k]
        beta_k = beta_from_factors(kf, u)
        proper = {}
        direct = {}
        for d in divisors(kf):
            df = factor_divisor(kf, d)
            coefficient = c(d, df)
            if not coefficient:
                continue
            m = k // d
            mf = subtract_factors(kf, df)
            if m > u:
                b_m = beta_from_factors(mf, u)
                demand(b_m == beta_k, "Small divisor invariance under rough d")
                if b_m:
                    direct[d] = b_m
            if d < k:
                proper[d] = beta_k
        proper = {d: v for d, v in proper.items() if v}
        demand(direct == proper, "Aggregated coefficient identity in independent weights")
        total_c = sum((outer_cache[d] for d in proper), F(0))
        demand(total_c <= 28, "Actual bounded divisor weight")
        value = sum((F(3, 2) * outer_cache[d] * v
                     for d, v in proper.items()), F(0))
        coefficient_checks += 1
        sign_values.add(beta_k)
        alpha_cache[k] = value, proper
        return value, proper

    core_rows = core_zero_rows = 0
    for value, nf in factors.items():
        for b in divisors(nf):
            if b <= u:
                continue
            bf = factor_divisor(nf, b)
            kf = subtract_factors(nf, bf)
            k = value // b
            proxy, terms = alpha_data(k, kf)
            if proxy:
                rows[b].append(k)
        for d in divisors(nf):
            df = factor_divisor(nf, d)
            cd = c(d, df)
            if not cd or d ** 100 <= n ** 113:
                continue
            qf = subtract_factors(nf, df)
            q_value = value // d
            if q_value <= u:
                continue
            one, two, ii, target, _ = vaughan_vectors(qf, u, u)
            keys = set(one) | set(two) | set(ii) | set(target)
            demand(all(one[p] + two[p] + ii[p] == target.get(p, 0)
                       for p in keys), "Joint high-outer identity")
            core_rows += 1
            if not target:
                demand(all(one[p] + two[p] + ii[p] == 0 for p in keys),
                       "Joint composite-row cancellation")
                core_zero_rows += 1

    def actual_alpha(k):
        result = I.point(0)
        for d, scale in alpha_cache[k][1].items():
            if d not in gamma_cache:
                gamma_cache[d] = outer_cache[d] * I.point(n).log() / I.point(F(n * n, d)).log()
            result += scale * gamma_cache[d]
        return result

    ps = primes_up_to(4 * n)
    prime_set = set(ps)
    blocks = []
    pair_checks = 0
    gram_checks = 0
    for q in sorted({max(u, n // 8), n // 2, n, 2 * n}):
        active = {b: ks for b, ks in rows.items() if q < b <= 2 * q}
        counts = Counter()
        direct_energy = F(0)
        diagonal = F(0)
        for b, ks in active.items():
            vb = sum((alpha_cache[k][0] for k in ks), F(0))
            direct_energy += vb * vb
            diagonal += sum((alpha_cache[k][0] ** 2 for k in ks), F(0))
            for k in ks:
                for ell in ks:
                    counts[k, ell] += 1
        gram = F(0)
        for (k, ell), count in counts.items():
            demand(count == overlap(n, u, q, k, ell), "Actual closed overlap count")
            gram += alpha_cache[k][0] * alpha_cache[ell][0] * count
            pair_checks += 1
        demand(gram == direct_energy, "Actual-coefficient Gram identity")
        if q >= n:
            demand(direct_energy == diagonal, "Exact diagonal large-b region")
        gram_checks += 1
        e_prime, t_prime = I.point(0), I.point(0)
        norm = I.point(0)
        for p in ps:
            if not q < p <= 2 * q or p <= u:
                continue
            lp = I.point(p).log()
            norm += lp * lp
            vb = sum((actual_alpha(k) for k in active.get(p, [])), I.point(0))
            e_prime += (vb * vb).nonnegative()
            t_prime += lp * vb
        cauchy = 2 * sqrt_interval(norm * e_prime) / n
        signed = 2 * t_prime / n
        # Directed intervals enclose the actual frozen logarithmic weights.
        demand(signed.hi <= cauchy.hi and signed.lo.copy_negate() <= cauchy.hi,
               "Finite Cauchy diagnostic")
        blocks.append({
            "Q": q, "all_integer_b_proxy_energy_exact": str(direct_energy),
            "proxy_diagonal_exact": str(diagonal),
            "proxy_off_diagonal_exact": str(direct_energy - diagonal),
            "actual_prime_b_energy": e_prime.record(),
            "actual_prime_b_signed_contribution_over_u": signed.record(),
            "actual_prime_b_Cauchy_bound_over_u": cauchy.record(),
            "scope": "Finite diagnostic; actual c and gamma, frozen log denominator",
        })
    return {
        "N": n, "U_V": u, "campaign_truncation": actual_truncation,
        "fixture_note": ("Campaign floor(N^(1/100))" if actual_truncation else
                         "Larger U stress fixture; does not change campaign truncation"),
        "beta_first_moment_exact": first, "beta_energy_exact": energy,
        "beta_density_first_exact": str(-alpha_u), "beta_density_second_exact": str(q_u),
        "alpha_coefficient_identities": coefficient_checks,
        "beta_sign_values_seen": sorted(sign_values),
        "joint_core_rows_checked": core_rows,
        "joint_non_prime_power_rows_cancelled": core_zero_rows,
        "overlap_pair_checks": pair_checks, "Gram_checks": gram_checks,
        "blocks": blocks,
    }


def update_state():
    path = ROOT / "results/campaign_state.json"
    state = json.loads(path.read_text())
    demand(state["H_theta_proved"] is False, "No H claim")
    demand(state["chosen_target"]["certified_K_from_current_inputs"] == 0,
           "No prime mass credit")
    state.update({
        "date": DATE, "checkpoint": 13,
        "latest_investigation_note": "COFACTOR_ESTIMATE_NOTE.md",
        "cofactor_estimation": "results/cofactor_estimation.json",
        "cofactor_checks": "results/cofactor_checks.json",
        "cofactor_source_facets": "results/cofactor_facets.json",
        "actual_cofactor_weight_factorization_proved": True,
        "uniform_Gram_upper_bounds_proved": True,
        "uniform_Gram_bound_sufficient_for_0011": False,
        "proper_b_prime_power_TypeII_negligible": True,
        "complete_centered_TypeI_outer_cutoff": "N^(113/100)",
        "TypeII_removed_region": "db<=N^(49/50), or N^(19/20)<d<=N^(113/100) and db<=N^(1143/1000)",
        "remaining_TypeII_is_weighted_beta_covariance": True,
        "next_gate": "Estimate B_remaining(J)+R_I,d>N^(113/100)(J)<=(.011+o(1))*u, with the actual remaining weight and ordering gate",
        "next_gate_status": "Unproved; explicit uniform Gram bounds, enlarged TypeI range and a signed TypeII product strip proved",
        "lower_bound_status": "K=0; TypeI through N^(113/100) and selected TypeII product strip proved; remaining signed covariance and TypeI core unestimated",
        "numerical_bounds_changed_in_checkpoint13": "New finite identity/diagnostic fixtures only; historical analytic ledger unchanged",
        "new_terminal_comparison_estimate_admitted": False,
    })
    state["milestones"]["3"] = "Long normalized remainders removed; complete TypeI below exponent 113/100 proved"
    state["milestones"]["4"] = "Actual cofactor factorization, uniform Gram bounds and a TypeII product strip proved; terminal signed covariance pending"
    path.write_text(json.dumps(state, indent=2) + "\n")


def estimation_record():
    return {
        "date": DATE, "checkpoint": 13, "note": "COFACTOR_ESTIMATE_NOTE.md",
        "coefficients": "Actual frozen c_N, gamma_N and beta_U; U=V=floor(N^(1/100)) unchanged",
        "actual_cofactor_factorization": {
            "identity": "alpha_N(k)=beta_U(k)*sum_(d|k,d<k) gamma_N(d)",
            "proper_divisor_condition_essential": True,
            "proper_outer_weight_bound": "42",
            "extra_unrestricted_divisor_loss_removed": True,
        },
        "local_beta_moments": {
            "any_translated_integer_interval": True,
            "first": "-H*alpha_U+O(U)",
            "second": "H*q(U)+O(U^2)",
            "actual_J_first": "o(u)",
            "actual_J_second": "(L+o(1))*Y, L>0",
        },
        "uniform_Gram_estimate": {
            "proved": True,
            "bound": "(1+N/Q)*min(N+Q*U^2,(1+Q/N)*(N^2/Q+U^2))",
            "low_range": "E_Q=O(N^2/Q) for U<=Q<=N/U^2",
            "large_b_range": "E_Q=O(N), and exact diagonal kernel, for Q>=N in the contributing range",
            "prime_b_bound": "E_Q^p=O((1+N/Q)*(N+Q*U^2)/log(2Q))",
            "arbitrary_b_dependent_bounded_outer_subsets_allowed": True,
            "supplies_required_vanishing_log_saving": False,
        },
        "proper_prime_power_b_removal": {
            "uniform": True,
            "error": "O_epsilon(N^epsilon*(N*U^(-1/2)+sqrt(S))), S=O(N^(7/4)/U)",
            "example_leading_power": "N^(249/250)",
        },
        "signed_covariance_reduction": {
            "proved": True,
            "weight": "sum_(p|n,p>U prime) log(p)*sum_(d|n/p,d<n/p) gamma_N(d)",
            "weight_upper": "(36+o(1))*log(N)",
            "unweighted_beta_centering_complete": True,
            "uniform_full_TypeII_bound": "O(N), insufficient for u=N/(2log(N))",
        },
        "new_source_coverage": {
            "complete_TypeI_outer_exponent": str(SIGMA_MAX),
            "total_denominator_exponent_max": str(TOTAL_MAX),
            "minimum_continuous_source_margin": "3/5600",
            "new_ordering_gate_retained_by_Mellin_separation": True,
            "source_certificate": "results/cofactor_facets.json",
        },
        "TypeII_region_proved_negligible": [
            "db<=N^(49/50)",
            "N^(19/20)<d<=N^(113/100), db<=N^(1143/1000)",
        ],
        "remaining_target": "B_remaining(J)+R_I,d>N^(113/100)(J)<=(.011+o(1))*u",
        "remaining_numerator_target": "sum_J beta_U(n)*(W_remaining(n)-mean(W_remaining)) + log(N)*R_I,new <=(.0055+o(1))*N",
        "remaining_weight_depends_on_b_after_region_removal": True,
        "original_b_independent_Gram_formula_retained_after_removal": False,
        "joint_core_identity": "B_core+R_I,new=A_core-integral(G_core)",
        "remaining_signed_covariance_estimated_at_target_scale": False,
        "remaining_TypeI_core_estimated_at_target_scale": False,
        "terminal_uniform_0011_estimate_proved": False,
        "positive_K_credited": 0, "H_theta_proved": False,
        "higher_degree_cap_proved": False,
        "openai007_kernel_matched": False,
        "global_impossibility_claim": False,
        "historical_numerical_ledger_changed": False,
    }


def main():
    source = provenance()
    facets = facet_certificates()
    comb = combinatorial_outer_bound()
    fixtures = [exact_fixture(n, u, actual) for n, u, actual in (
        (100, 1, True), (200, 3, False), (1000, 3, False),
        (2000, 5, False), (10000, 1, True), (10000, 8, False),
    )]
    checks = {
        "date": DATE, "checkpoint": 13, "provenance": source,
        "outer_bound": comb, "source_vertex_checks": facets["affine_vertex_checks"],
        "actual_fixtures": fixtures,
        "totals": {
            "coefficient_identities": sum(r["alpha_coefficient_identities"] for r in fixtures),
            "overlap_pair_checks": sum(r["overlap_pair_checks"] for r in fixtures),
            "Gram_checks": sum(r["Gram_checks"] for r in fixtures),
            "joint_core_rows": sum(r["joint_core_rows_checked"] for r in fixtures),
            "joint_non_prime_power_rows_cancelled": sum(r["joint_non_prime_power_rows_cancelled"] for r in fixtures),
        },
        "all_checks_passed": True, "uniform_terminal_0011_estimate_proved": False,
        "H_theta_proved": False, "positive_K_credited": 0,
        "proof_note": "COFACTOR_ESTIMATE_NOTE.md",
    }
    (ROOT / "results/cofactor_facets.json").write_text(json.dumps(facets, indent=2) + "\n")
    (ROOT / "results/cofactor_checks.json").write_text(json.dumps(checks, indent=2) + "\n")
    (ROOT / "results/cofactor_estimation.json").write_text(
        json.dumps(estimation_record(), indent=2) + "\n")
    update_state()
    print(json.dumps({"all_checks_passed": True, "historical_files_unchanged": source["historical_files_verified_unchanged"],
                      "source_vertices": facets["affine_vertex_checks"], "totals": checks["totals"],
                      "terminal_estimate_proved": False}, indent=2))


if __name__ == "__main__":
    main()
