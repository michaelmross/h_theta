#!/usr/bin/env python3
"""Checkpoint 29: audit a one-prime residual-degree lower weight.

The proof is in ONE_PRIME_DEGREE_POOL_AUDIT_NOTE.md. This program checks
the original arithmetic gates, outward reference prices, and the source
range of the primitive rough-cofactor sieve. It does not instantiate
Iwaniec's universal weights or prove a sharp short comparison.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

from coupled_one_sided import actual_mark, segmented_factors
from structured_frontier import I

ROOT = Path(__file__).resolve().parents[1]
LEVEL = F(1249, 1000)
LEVEL_CEILING = F(5, 4)  # Favorable pricing ceiling; not an admitted endpoint.
ZEXP, AEXP, YEXP = F(1, 4), F(1, 2), F(19, 20)
KAPPA, BUDGET = F(1, 1000), F(1, 10000)
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def save(name, value):
    (ROOT / "results" / name).write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def read_interval(record):
    return I(Decimal(record["lower"]), Decimal(record["upper"]))


def positive_part(v):
    return I(max(Decimal(0), v.lo), max(Decimal(0), v.hi))


def preservation():
    p = ROOT / "results/checkpoint28_preservation_manifest.json"
    old = json.loads(p.read_text())
    demand(old["checkpoint"] == 28, "Frozen checkpoint28 identity")
    count = 0
    for record in old["files"]:
        if record["path"] in MUTABLE:
            continue
        data = (ROOT / record["path"]).read_bytes()
        demand(len(data) == record["size_bytes"] and
               hashlib.sha256(data).hexdigest() == record["sha256"],
               "Preserved " + record["path"])
        count += 1
    demand(count == 283, "All historical nonmutable records")
    return {"checkpoint28_nonmutable_records_verified": count,
            "checkpoint28_manifest_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "negative_frontier_ledger_sha256": hashlib.sha256(
                (ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()}


def source_facets():
    rows = []
    for a in (ZEXP, AEXP):
        beta = LEVEL - a
        demand(a < 1 and beta > 0 and a + beta < LEVEL_CEILING,
               "Fixed WF arbitrary-outer conditions")
        demand(2 * a + beta < 2, "Older RS route also covers all outer primes")
        demand(1 <= beta / a < 4, "Compact primitive lower-sieve ratio")
        rows.append({"outer_prime_exponent": str(a), "beta": str(beta),
                     "s": str(beta / a),
                     "full_level_reserve": str(LEVEL_CEILING - a - beta),
                     "RS_margin": str(2 - 2 * a - beta)})
    demand(LEVEL / 3 == F(1249, 3000), "Exact zero-main boundary")
    # f(s)/(2e^gamma)=log(s-1)/s is increasing on [2,4].
    monotone_margin = F(4, 3) - I.point(3).log()
    demand(monotone_margin.lo > 0, "Lower sieve improves up to favorable level ceiling")
    # For a in [3/8,1/2], even the B=5/4 limiting price is negative.
    rough_upper = 2 * I.point(F(4, 3)).log() / F(3, 4)
    low_degree_lower = (1 + I.point(2).log()) / F(13, 8)
    high_band_gap = low_degree_lower - rough_upper
    demand(high_band_gap.lo > 0, "Entire high least-prime band has negative net price")
    # A narrower certificate for the old four-prime box's least-prime band.
    box_rough_upper = 2 * I.point(F(9, 8)).log() / F(41, 50)
    box_low_lower = (1 + I.point(F(114, 43)).log()) / F(8, 5)
    box_gap = box_low_lower - box_rough_upper
    demand(box_gap.lo > 0, "Old omitted box is now covered but negatively priced")
    return {"coordinate": "a=log_N(p)", "outer_domain": [str(ZEXP), str(AEXP)],
            "vertices": rows, "vertex_count": 2,
            "rough_WF_remainder_source_admitted": True,
            "whole_candidate_comparison_admitted": False,
            "exact_base_comparison_admitted": False,
            "exact_prime_counterweight_comparison_admitted": False,
            "exact_semiprime_counterweight_comparison_admitted": False,
            "minimum_full_level_reserve": str(LEVEL_CEILING - LEVEL),
            "minimum_RS_extra_margin": str(2 - LEVEL - AEXP),
            "primitive_lower_zero_main_from": str(LEVEL / 3),
            "f_monotonicity_margin": monotone_margin.record(),
            "negative_price_band": ["3/8", "1/2"],
            "negative_price_band_gap_lower_enclosure": high_band_gap.record(),
            "old_box_least_prime_band": ["2/5", "43/100"],
            "old_box_negative_price_gap_enclosure": box_gap.record(),
            "endpoint_5_over_4_used_only_as_favorable_price_ceiling": True,
            "all_one_prime_methods_excluded": False}


def integrate(fn, left, right, bins):
    step = (right - left) / bins
    total = I.point(0)
    for j in range(bins):
        a = I.segment(left + j * step, left + (j + 1) * step)
        total = total + fn(a) * step
    return total


def lower_density(a, level):
    # This function is used only on a<=level/3; its logarithm is >=0.
    logterm = positive_part((I.point(level) / a - 2).log())
    return 2 * logterm / (level - a)


def low_degree_density(a):
    return (1 + ((2 - 2 * a) / a).log()) / (2 - a)


def positive_reference(level, bins):
    boundary = level / 3
    part = integrate(lambda a: 2 * positive_part(
        lower_density(a, level) - low_degree_density(a)) / a,
        ZEXP, boundary, bins)
    # On [boundary,1/2], f=0 and the exact exclusions are strictly positive.
    return part


def buchstab_four(bins=4000):
    step, cell_error = F(1, bins), F(1, 6 * bins ** 3)
    values = [I.point(1)] * (bins + 1)
    for i in range(bins, 3 * bins):
        left, right = F(1) + i * step, F(1) + (i + 1) * step
        derivative_left = values[i - bins] / (left - 1)
        derivative_right = values[i - bins + 1] / (right - 1)
        values.append(values[-1] + step / 2 *
                      (derivative_left + derivative_right) +
                      I.segment(-cell_error, cell_error))
    exact_three = 1 + I.point(2).log()
    demand(values[2 * bins].lo <= exact_three.lo and
           values[2 * bins].hi >= exact_three.hi,
           "Buchstab recursion contains exact B(3)")
    return values[-1], {"bins_per_unit": bins, "cell_error": str(cell_error),
                       "omega_second_derivative_bound": "2",
                       "integer_knots_are_grid_boundaries": True,
                       "B3_exact_check": True}


def test_band_reference(bins=160):
    # For a in [.40,.43], q=2/a-1 is in [157/43,4].
    # Residual degree>=3 therefore has the three-prime main, with density
    # (2/[a(2-a)])*integral_1^(2/a-3) log(v)/(v+1) dv.
    # Map its variable inner interval to t in [0,1].
    left, right = F(2, 5), F(43, 100)
    ha, ht = (right - left) / bins, F(1, bins)
    total = I.point(0)
    for j in range(bins):
        a = I.segment(left + j * ha, left + (j + 1) * ha)
        width = 2 / a - 4
        demand(width.lo > 0, "Concrete band has positive residual three-prime volume")
        for k in range(bins):
            t = I.segment(k * ht, (k + 1) * ht)
            v = 1 + t * width
            term = 2 * width * positive_part(v.log()) / (a * (2 - a) * (v + 1))
            total = total + term * ha * ht
    return (1 + KAPPA) * total, {"a_band": [str(left), str(right)],
            "residual_Buchstab_ratio": ["157/43", "4"],
            "bins_per_coordinate": bins, "outward_cells": bins * bins,
            "reference_formula": "(1+kappa)*2*integral_.40^.43 integral_1^(2/a-3) log(v)/(a*(2-a)*(v+1)) dv da",
            "four_prime_main_only": True,
            "degree_five_boundary_and_repetitions_are_o_u": True,
            "sharp_short_lower_comparison_proved": False}


def reference_certificates(bins=12000):
    old = json.loads((ROOT / "results/coupled_one_sided_coefficients.json").read_text())
    target = read_interval(old["positive_complement_reference"])
    base = (1 + KAPPA) * (1 + I.point(F(21, 19)).log())
    higher = target - base
    raw_lower = integrate(lambda a: 2 * lower_density(a, LEVEL) / a,
                          ZEXP, LEVEL / 3, bins)
    prime = I.point(F(7, 3)).log()
    semi = integrate(lambda a: 2 * ((2 - 2 * a) / a).log() / (a * (2 - a)),
                     ZEXP, AEXP, bins)
    low = prime + semi
    full_pool_mean = raw_lower - low
    actual_best = positive_reference(LEVEL, bins)
    limit_best = positive_reference(LEVEL_CEILING, bins)
    scale = 1 + KAPPA
    full_mean = base + scale * full_pool_mean
    full_loss = target - full_mean
    actual_best_mean = base + scale * actual_best
    actual_best_loss = target - actual_best_mean
    limit_best_mean = base + scale * limit_best
    limit_best_loss = target - limit_best_mean
    demand(full_loss.lo > F(94, 100), "Full one-prime candidate fails favorable reference test")
    demand(limit_best_loss.lo > F(18, 100), "Even ceiling-level optimized deletion loses at least .18")
    demand(limit_best_loss.lo > BUDGET, "Best reference budget fails")
    old_box = json.loads((ROOT / "results/switched_minorant_reference.json").read_text())[
        "omitted_four_prime_box"]
    box_lower = F(693, 911600)
    demand(box_lower > BUDGET, "Independent least-prime-band deficit exceeds budget")
    band, band_check = test_band_reference()
    demand(band.lo > box_lower, "Full test-band reference contains the old four-prime box")
    b4, b4_check = buchstab_four()
    b8 = read_interval(old["rough_reference_A0"])
    rough_one = b8 - b4
    identity_error = rough_one - (higher / scale + low)
    demand(identity_error.lo <= 0 <= identity_error.hi,
           "Independent Buchstab reference identity is consistent")
    return {"bins_per_integral": bins,
            "quadrature": "Outward interval Riemann sums; no floating-point tolerance",
            "level_sum": str(LEVEL), "favorable_level_ceiling": str(LEVEL_CEILING),
            "ceiling_is_not_admitted_source_endpoint": True,
            "base_exact_reference_smoothed": base.record(),
            "positive_complement_reference_smoothed": target.record(),
            "higher_degree_reference_smoothed": higher.record(),
            "primitive_lower_rough_reference_unscaled": raw_lower.record(),
            "exact_prime_exclusion_reference_unscaled": prime.record(),
            "exact_semiprime_exclusion_reference_unscaled": semi.record(),
            "total_exact_low_degree_exclusion_reference_unscaled": low.record(),
            "full_candidate_residual_mean_unscaled": full_pool_mean.record(),
            "full_candidate_favorable_mean_smoothed": full_mean.record(),
            "full_candidate_favorable_loss": full_loss.record(),
            "best_block_deletion_residual_mean_unscaled": actual_best.record(),
            "best_block_deletion_favorable_mean_smoothed": actual_best_mean.record(),
            "best_block_deletion_favorable_loss": actual_best_loss.record(),
            "ceiling_best_block_deletion_residual_mean_unscaled": limit_best.record(),
            "ceiling_best_block_deletion_favorable_mean_smoothed": limit_best_mean.record(),
            "ceiling_best_block_deletion_favorable_loss": limit_best_loss.record(),
            "certified_full_candidate_loss_lower_coefficient": "47/50",
            "certified_even_ceiling_optimized_loss_lower_coefficient": "9/50",
            "independent_band_deficit_lower_coefficient": str(box_lower),
            "concrete_coupled_test_band_reference_smoothed": band.record(),
            "concrete_coupled_test_band_reference_certificate": band_check,
            "inherited_four_prime_box_certificate": old_box,
            "Buchstab_B4": b4.record(), "Buchstab_B4_check": b4_check,
            "one_prime_rough_reference_B8_minus_B4": rough_one.record(),
            "Buchstab_identity_cross_check_error": identity_error.record(),
            "finite_tolerance": "Fixed C*epsilon lowers the primitive weight and worsens loss",
            "exact_exclusions_are_optimistic": True,
            "upper_exclusion_majorants_can_only_worsen_reference": True,
            "positive_part_is_applied_to_reference_price_not_integer_weight": True,
            "budget": str(BUDGET), "reference_budget_passed": False,
            "historical_ledgers_changed": False}


def box_index(z, p):
    P = z
    while 2 * P <= p:
        P *= 2
    return P


def arithmetic_checks():
    cases, witnesses = [], []
    sites = 0
    for N in (65536, 160000):
        z = next(t for t in range(1, 100) if t ** 4 == N)
        lo, hi = N * N - N - 1, N * N + N + 1
        counter = Counter()
        mark_mass, complement_mass = F(0), F(0)
        for offset, factors in enumerate(segmented_factors(lo, hi)):
            n = lo + offset
            rough = factors[0] ** 4 >= N
            mark = actual_mark(N, n, factors)
            demand(0 <= mark <= int(rough), "Actual original mark cap on padding")
            complement = int(rough) * (1 - min(F(1), mark))
            base = int(factors[0] ** 20 >= N ** 19)
            pool, strict_bound, r1, r2 = 0, 0, 0, 0
            for p in set(factors):
                if p < z or 2 * p ** 4 > 3 * N * N:
                    continue
                residual = factors.copy()
                residual.remove(p)
                demand(residual and n // p > p, "Physical cofactor exceeds outer prime")
                R = int(residual[0] >= p)
                E1 = int(len(residual) == 1)
                E2 = int(len(residual) == 2 and residual[0] >= p)
                G = int(R and len(residual) >= 3)
                demand(R - E1 - E2 == G, "Exact one-prime degree identity")
                P = box_index(z, p)
                rough_box = int(residual[0] >= 2 * P)
                demand(rough_box - E1 - E2 <= G, "Fixed-box upper bound on candidate")
                pool += G
                strict_bound += rough_box - E1 - E2
                r1 += E1
                r2 += E2
                counter["actual_outer_prime_rows"] += 1
                counter["repeated_outer_prime_rows"] += factors.count(p) > 1
            demand(pool == int(rough and len(factors) >= 4), "Full higher-degree pool covered once")
            demand(base + strict_bound <= complement, "Candidate's proved arithmetic upper envelope")
            correction = complement - base - pool
            demand(correction >= 0, "Original repeated-three correction is nonnegative")
            if correction:
                demand(len(factors) == 3 and len(set(factors)) < 3,
                       "Only repeated-three rows remain outside exact degree partition")
                counter["repeated_three_correction_sites"] += 1
            # The original checkpoint-28 box uses exact exponent tests.
            box = (len(factors) == 4 and len(set(factors)) == 4 and
                   N ** 40 <= factors[0] ** 100 <= N ** 43 and
                   N ** 45 <= factors[1] ** 100 <= N ** 48 and
                   N ** 50 <= factors[2] ** 100 <= N ** 53)
            if box:
                demand(complement == 1 and pool == 1 and base == 0,
                       "Previously omitted four-prime box is in the one-prime pool")
                counter["old_four_prime_box_sites_now_covered"] += 1
                if len(witnesses) < 3:
                    witnesses.append({"N": N, "n": n, "factors": factors,
                                      "positive_complement": str(complement),
                                      "one_prime_degree_pool": pool})
            counter["sites"] += 1
            counter["rough_sites"] += rough
            counter["base_sites"] += base
            counter["higher_degree_sites"] += pool
            counter["prime_exclusion_sites"] += r1
            counter["semiprime_exclusion_sites"] += r2
            mark_mass += mark
            complement_mass += complement
        sites += counter["sites"]
        cases.append({"N": N, **dict(counter), "marked_mass": str(mark_mass),
                      "positive_complement_mass": str(complement_mass),
                      "original_cutoffs_and_canonical_weights_used": True})
    demand(sites == 451078 and witnesses, "Full padding fixture and old-box witnesses")
    return {"cases": cases, "short_padding_sites_checked": sites,
            "old_four_prime_box_covered_witnesses": witnesses,
            "pointwise_bound_checks_exact_pool_not_literal_Iwaniec_weight_values": True,
            "finite_checks_do_not_prove_sharp_short_comparison": True}


def main():
    preserved = preservation()
    facets = source_facets()
    reference = reference_certificates()
    arithmetic = arithmetic_checks()
    checks = {"preservation": preserved, "source_facets": {
                  "rough_WF_remainder_source_admitted": True,
                  "whole_candidate_comparison_admitted": False,
                  "outer_vertex_count": facets["vertex_count"]},
              "arithmetic": arithmetic,
              "outward_reference_integrals_certified": True,
              "all_exact_checks_passed": True, "candidate_accepted": False,
              "optimized_family_accepted": False, "sharp_target_proved": False}
    audit = {"date": "2026-10-12", "checkpoint": 29,
             "candidate": "Exact y-rough base plus one-prime primitive rough lower sieve minus exact prime and semiprime cofactors",
             "pointwise_lower_weight_proved": True,
             "old_four_prime_box_geometrically_covered": True,
             "rough_remainder_source_admitted": True,
             "whole_candidate_short_long_comparison_proved": False,
             "reference_budget_passed": False,
             "candidate_rejected": True,
             "full_candidate_reference_loss_lower_coefficient": "47/50",
             "even_ceiling_optimized_reference_loss_lower_coefficient": "9/50",
             "budget": "1/10000",
             "family_scope": "One primitive rough linear-sieve lower weight per outer prime, followed by exact or upper-majorant low-degree exclusions and weights theta_p in [0,1] independent of the product integer",
             "all_one_prime_methods_excluded": False,
             "next_required_input": "A lower weight or joint centered estimate that targets the rough Omega(m)>=3 pool directly; the least-prime band [.40,.43] is a concrete test block",
             "original_spectral_budget": "1587/200000",
             "original_smoothing_budget": "613/200000",
             "original_total_coefficient": "11/1000",
             "new_global_coefficient_charge": "0",
             "fixed_least_prime_xi_if_used": "Checkpoint22 (23), retained",
             "fixed_frequency_L_if_used": "21147/L, retained",
             "sharp_signed_spectral_bound_proved": False,
             "terminal_0011_estimate_proved": False, "H_theta_proved": False,
             "certified_K": 0}
    for name, result in (("one_prime_degree_pool_facets.json", facets),
                         ("one_prime_degree_pool_reference.json", reference),
                         ("one_prime_degree_pool_checks.json", checks),
                         ("one_prime_degree_pool_audit.json", audit)):
        save(name, result)
    print(json.dumps({"all_exact_checks_passed": True,
                      "preserved_records": preserved["checkpoint28_nonmutable_records_verified"],
                      "short_padding_sites_checked": arithmetic["short_padding_sites_checked"],
                      "candidate_accepted": False, "optimized_family_accepted": False,
                      "full_candidate_loss_lower": "0.94",
                      "even_ceiling_optimized_loss_lower": "0.18",
                      "budget": ".0001", "sharp_target_proved": False}))


if __name__ == "__main__":
    main()
