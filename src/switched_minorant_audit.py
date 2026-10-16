#!/usr/bin/env python3
"""Checkpoint 28: reject one explicit two-prime switched minorant.

The analytic argument is in SWITCHED_MINORANT_AUDIT_NOTE.md. This program
certifies gates, rational source ranges and outward reference losses.
It does not numerically instantiate Iwaniec's universal sieve weights.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from decimal import Decimal
from fractions import Fraction as F
from itertools import combinations
from math import factorial, isqrt
from pathlib import Path

from coupled_one_sided import actual_mark, segmented_factors
from structured_frontier import I
from two_free_prime_decomposition import constraint, vertices

ROOT = Path(__file__).resolve().parents[1]
DELTA = F(1, 1000)
LEVEL = F(5, 4) - DELTA
ZEXP, YEXP = F(1, 4), F(19, 20)
KAPPA = F(1, 1000)
BUDGET = F(1, 10000)
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


def preservation():
    p = ROOT / "results/checkpoint27_preservation_manifest.json"
    old = json.loads(p.read_text())
    demand(old["checkpoint"] == 27, "Frozen checkpoint27 identity")
    count = 0
    for record in old["files"]:
        if record["path"] in MUTABLE:
            continue
        data = (ROOT / record["path"]).read_bytes()
        demand(len(data) == record["size_bytes"] and
               hashlib.sha256(data).hexdigest() == record["sha256"],
               "Preserved " + record["path"])
        count += 1
    demand(count == 275, "All historical nonmutable records")
    return {"checkpoint27_nonmutable_records_verified": count,
            "checkpoint27_manifest_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "negative_frontier_ledger_sha256": hashlib.sha256(
                (ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()}


def source_facets():
    # Coordinates a1=log_N p, a2=log_N r, p<=r; beta=LEVEL-a1-a2.
    cs = [constraint((-1, 0), -ZEXP), constraint((1, -1), 0),
          constraint((1, 2), LEVEL)]
    points = vertices(cs)
    demand(len(points) == 3, "Active triangle vertices")
    rows = []
    for a1, a2 in points:
        gamma, beta = a1 + a2, LEVEL - a1 - a2
        demand(beta >= a2 and gamma < 1 and beta > 0,
               "Lower-sieve ratio and arbitrary-outer source domain")
        demand(F(5, 4) - gamma - beta == DELTA, "Strict full-level reserve")
        demand(1 <= beta / a2 <= 4 * LEVEL - 2, "Continuous sieve-ratio bound")
        rows.append({"a1": str(a1), "a2": str(a2), "gamma": str(gamma),
                     "beta": str(beta), "s": str(beta / a2),
                     "full_level_reserve": str(DELTA),
                     "gamma_below_one_margin": str(1 - gamma)})
    demand(max(F(v["gamma"]) for v in rows) == 2 * LEVEL / 3,
           "Maximum active outer product exponent")
    rs = vertices(cs + [constraint((1, 1), F(3, 4))])
    fi = vertices(cs + [constraint((-1, -1), -F(3, 4))])
    for a1, a2 in rs:
        gamma, beta = a1 + a2, LEVEL - a1 - a2
        demand(2 - 2 * gamma - beta >= DELTA, "RS arbitrary-outer extra margin")
    tau, nu = DELTA / 100, DELTA / 1000
    fi_margins = {
        "actual_standalone_minus_frequency": tau - nu,
        "C6_minus_capacity": 2 * DELTA - nu / 2 - tau,
        "C2_minus_capacity": (7 * DELTA - 5 * nu - 7 * tau) / 7,
        "C1_minus_capacity": (7 * DELTA - 7 * nu - 7 * tau) / 7,
        "second_factor_capacity_positive": 1 - 2 * LEVEL / 3 - tau,
        "C3_minus_C2": F(1, 32),
        "C4_minus_C2": (1 - 10 * nu) / 35}
    demand(all(v > 0 for v in fi_margins.values()), "Full FI capacities have strict reserves")
    logcap = I.point(4 * LEVEL - 3).log()
    demand(logcap.hi < 1, "Every cofactor leading mean is negative")
    # Minimum level for even one positive separately priced cofactor block.
    k = 30
    e_lower = sum((F(1, factorial(j)) for j in range(k + 1)), F(0))
    e_upper = e_lower + F(1, k * factorial(k))
    threshold = I.segment((3 + e_lower) / 4, (3 + e_upper) / 4)
    demand(threshold.lo > F(5, 4) and threshold.hi < F(143, 100),
           "Scoped necessary positive-price level")
    return {"coordinate_order": ["a1", "a2"], "constraints": [
                {"A": list(map(str, row)), "bound": str(bound)} for row, bound in cs],
            "vertices": rows, "vertex_count": len(rows),
            "RS_branch_vertex_count": len(rs), "FI_branch_vertex_count": len(fi),
            "FI_capacity_margins": {k: str(v) for k, v in fi_margins.items()},
            "maximum_gamma": str(2 * LEVEL / 3),
            "minimum_beta": str(LEVEL / 3),
            "minimum_full_level_reserve": str(DELTA),
            "s_max": str(4 * LEVEL - 2),
            "normalized_lower_sieve_L_max": logcap.record(),
            "cofactor_price_deficit_lower_enclosure": (1 - logcap).record(),
            "positive_cofactor_price_necessary_level_formula": "B>(3+e)/4",
            "positive_cofactor_price_necessary_level": threshold.record(),
            "necessary_level_scope": "Separately priced lower rough cofactor minus upper prime cofactor, original z exponent 1/4; not a sufficient sharp comparison",
            "base_actual_rough_count_comparison_admitted": False,
            "switched_WF_components_source_admitted": True,
            "all_switching_methods_excluded": False}


def reference_loss(bins=240):
    # Positive magnitude of the negative most-favorable cofactor mean.
    # Map the triangular active domain to (a1,t), t in [0,1].
    ha = (LEVEL / 3 - ZEXP) / bins
    ht = F(1, bins)
    cap = I.point(4 * LEVEL - 3).log()
    total = I.point(0)
    for j in range(bins):
        a1 = I.segment(ZEXP + j * ha, ZEXP + (j + 1) * ha)
        width = ((LEVEL - 3 * a1) / 2).nonnegative()
        for k in range(bins):
            t = I.segment(k * ht, (k + 1) * ht)
            a2 = a1 + t * width
            beta = LEVEL - a1 - a2
            ratio = (LEVEL - a1 - 2 * a2) / a2
            positive_ratio = I(max(Decimal(1), ratio.lo), max(Decimal(1), ratio.hi))
            L = positive_ratio.log()
            L = I(max(Decimal(0), L.lo), min(cap.hi, L.hi))
            integrand = 4 * (1 - L) * width / (a1 * a2 * beta)
            demand(integrand.lo >= 0, "Positive reference-loss integrand")
            total = total + integrand * ha * ht
    cp27 = json.loads((ROOT / "results/coupled_one_sided_coefficients.json").read_text())
    complement = read_interval(cp27["positive_complement_reference"])
    base_unscaled = 1 + I.point(F(21, 19)).log()
    base = (1 + KAPPA) * base_unscaled
    higher = complement - base
    negative_cofactor = (1 + KAPPA) * total
    ideal_mean = base - negative_cofactor
    ideal_loss = complement - ideal_mean
    full_WF_base_loss = complement + negative_cofactor
    demand(ideal_loss.lo > F(156, 100), "Reference loss already exceeds 1.56u")
    demand(higher.lo > F(3, 10), "Deleting all switched blocks still fails the budget")
    demand(full_WF_base_loss.lo > F(266, 100), "Minorizing base worsens the loss")
    return {"bins_per_coordinate": bins, "outward_cells": bins * bins,
            "level_reserve": str(DELTA), "level_sum": str(LEVEL),
            "negative_cofactor_mean_magnitude_unscaled": total.record(),
            "negative_cofactor_mean_magnitude_smoothed": negative_cofactor.record(),
            "actual_base_reference_unscaled": base_unscaled.record(),
            "actual_base_reference_smoothed": base.record(),
            "positive_complement_reference_smoothed": complement.record(),
            "higher_degree_reference_smoothed": higher.record(),
            "most_favorable_candidate_mean_smoothed": ideal_mean.record(),
            "most_favorable_candidate_reference_loss": ideal_loss.record(),
            "certified_candidate_reference_loss_lower_coefficient": "39/25",
            "if_base_also_WF_minorized_reference_loss_lower_enclosure": full_WF_base_loss.record(),
            "finite_sieve_tolerance_corrections": "Increase reference loss; displayed favorable enclosure is the epsilon->0 coefficient limit, not an epsilon=0 source application",
            "budget": str(BUDGET), "reference_budget_passed": False,
            "old_coefficients_or_ledgers_changed": False}


def omitted_four_prime_box():
    ranges = [(F(2, 5), F(43, 100)), (F(9, 20), F(12, 25)),
              (F(1, 2), F(53, 100))]
    a4lo = 2 - sum((hi for _, hi in ranges), F(0))
    a4hi = 2 - sum((lo for lo, _ in ranges), F(0))
    volume = F(1)
    dmax, dmin = a4hi, a4lo
    for lo, hi in ranges:
        volume *= hi - lo
        dmax *= hi
        dmin *= lo
    lower, upper = 2 * volume / dmax, 2 * volume / dmin
    scale = 1 + KAPPA
    gate_margin = ranges[0][0] + 2 * ranges[1][0] - LEVEL
    demand(gate_margin == F(51, 1000), "Four-prime box is strictly outside active gate")
    demand(a4lo > ranges[2][1], "Fourth factor ordering has fixed margin")
    demand(scale * lower > BUDGET, "Omitted box alone exceeds total acceptance budget")
    return {"independent_exponent_ranges": [list(map(str, q)) for q in ranges],
            "fourth_factor_exponent_range": [str(a4lo), str(a4hi)],
            "a1_plus_twice_a2_minus_level_minimum": str(gate_margin),
            "fourth_factor_ordering_margin": str(a4lo - ranges[2][1]),
            "canonical_distinct_four_prime_reference": I.segment(lower, upper).record(),
            "smoothed_reference": I.segment(scale * lower, scale * upper).record(),
            "smoothed_reference_exact_lower_bound": str(scale * lower),
            "weight_vanishes_pointwise_on_this_box": True,
            "box_loss_exceeds_budget_even_with_perfect_active_transfer": True,
            "same_box_still_outside_level_5_4_gate": True}


def dyadic_lower(value, start):
    base = start
    while 2 * base <= value:
        base *= 2
    return base


def structural_checks():
    cases = []
    sites = 0
    box_witnesses = []
    for N in (65536, 160000):
        z = isqrt(isqrt(N))
        demand(z ** 4 == N, "Fixture original cutoff has exact integer fourth root")
        lo, hi = N * N - N - 1, N * N + N + 1
        level_power = N ** 1249
        demand(lo ** 1000 > level_power, "All active cofactors exceed their sifting prime")
        cache = {}
        counter = Counter()
        mark_total, complement_total = F(0), F(0)
        for offset, factors in enumerate(segmented_factors(lo, hi)):
            n = lo + offset
            rough = factors[0] >= z
            mark = actual_mark(N, n, factors)
            demand(0 <= mark <= int(rough), "Original short-padding prime marks retained")
            complement = int(rough) * (1 - min(F(1), mark))
            base_indicator = int(factors[0] ** 20 >= N ** 19)
            pool, stricter_pool = 0, 0
            pairs = set((factors[i], factors[j]) for i, j in combinations(range(len(factors)), 2))
            for p, r in pairs:
                if p < z:
                    continue
                P, R = dyadic_lower(p, z), dyadic_lower(r, z)
                if (P, R) not in cache:
                    cache[P, R] = (8 * P * R * R) ** 1000 <= level_power
                if not cache[P, R]:
                    continue
                remaining = factors.copy()
                remaining.remove(p)
                remaining.remove(r)
                m = n // (p * r)
                demand(m > r and m > 2 * R and remaining,
                       "Selected cofactor satisfies the exact physical gates")
                is_prime = int(len(remaining) == 1)
                contribution = int(remaining[0] >= r) - is_prime
                stricter = int(remaining[0] >= 2 * R) - is_prime
                demand(0 <= stricter <= contribution <= 1,
                       "Both exact composite-cofactor pools are nonnegative")
                pool += contribution
                stricter_pool += stricter
                counter["selected_outer_pair_rows"] += 1
                counter["p_equals_r_selected_rows"] += int(p == r)
            demand(base_indicator + pool <= complement,
                   "Two-smallest-prime pool is below the exact positive complement")
            demand(base_indicator + stricter_pool <= complement,
                   "Fixed-box sifting pool is below the exact positive complement")
            demand(pool <= 1, "Canonical two-smallest-prime selection counts once")
            first_prime_pool = 0
            for p in set(factors):
                remaining = factors.copy()
                remaining.remove(p)
                if p >= z and len(remaining) >= 3 and remaining[0] >= p:
                    first_prime_pool += 1
            demand(first_prime_pool == int(rough and len(factors) >= 4),
                   "One-smallest-prime higher-degree identity")
            residual = complement - base_indicator - first_prime_pool
            demand(residual >= 0 and (not residual or
                   (len(factors) == 3 and len(set(factors)) < 3)),
                   "Full first-prime pool leaves only repeated-three-prime correction")
            if len(factors) == 4:
                first_three_in_box = all(
                    N ** low <= p ** 100 < N ** high
                    for p, (low, high) in zip(factors, ((40, 43), (45, 48), (50, 53))))
                if first_three_in_box:
                    demand(complement == 1 and base_indicator == 0 and pool == 0,
                           "Omitted four-prime box has unit complement and no candidate support")
                    counter["omitted_four_prime_box_sites"] += 1
                    if len(box_witnesses) < 3:
                        box_witnesses.append({"N": N, "n": n, "factors": factors,
                                              "positive_complement": "1", "selected_pool": "0"})
            counter["sites"] += 1
            counter["rough_sites"] += int(rough)
            counter["base_sites"] += base_indicator
            counter["selected_composite_pool_sites"] += pool
            counter["fixed_box_composite_pool_sites"] += stricter_pool
            counter["one_smallest_prime_higher_degree_sites"] += first_prime_pool
            mark_total += mark
            complement_total += complement
        sites += counter["sites"]
        cases.append({"N": N, **dict(counter), "marked_mass": str(mark_total),
                      "positive_complement_mass": str(complement_total),
                      "original_cutoffs_and_gates_used": True})
    demand(box_witnesses, "At least one omitted-box arithmetic witness")
    return {"cases": cases, "short_padding_sites_checked": sites,
            "omitted_box_witnesses": box_witnesses,
            "tests_cover_exact_switching_pool_not_literal_Iwaniec_weight_values": True,
            "one_smallest_prime_next_interface_identity_checked": True,
            "finite_sites_do_not_prove_uniform_short_comparison": True}


def main():
    preserved = preservation()
    facets = source_facets()
    reference = reference_loss()
    omitted = omitted_four_prime_box()
    reference["omitted_four_prime_box"] = omitted
    print(json.dumps({"stage": "reference_loss", "most_favorable_loss": reference[
        "most_favorable_candidate_reference_loss"], "budget": str(BUDGET),
        "omitted_box_smoothed_lower": omitted["smoothed_reference_exact_lower_bound"]}), flush=True)
    arithmetic = structural_checks()
    checks = {"preservation": preserved, "source_facets": {
                  "vertex_count": facets["vertex_count"],
                  "switched_WF_components_source_admitted": True,
                  "base_actual_rough_count_comparison_admitted": False},
              "arithmetic": arithmetic, "outward_reference_cells": reference["outward_cells"],
              "all_exact_checks_passed": True,
              "candidate_accepted": False, "sharp_target_proved": False}
    status = {"date": "2026-10-12", "checkpoint": 28,
              "proof_note": "SWITCHED_MINORANT_AUDIT_NOTE.md",
              "candidate": "Two-smallest-prime switch; exact unmarked rough base plus lower rough-cofactor sieve minus upper prime-cofactor sieve",
              "level_sum": str(LEVEL), "level_reserve": str(DELTA),
              "pointwise_lower_weight_validity_proved": True,
              "switched_WF_components_source_admitted": True,
              "base_actual_rough_count_comparison_admitted": False,
              "whole_candidate_short_long_comparison_proved": False,
              "candidate_reference_budget_passed": False,
              "candidate_rejected": True,
              "reference_loss_certified_lower_coefficient": "39/25",
              "acceptance_budget": str(BUDGET),
              "omitted_positive_box_alone_exceeds_budget": True,
              "different_switching_or_coupled_composite_estimates_excluded": False,
              "original_terminal_coefficient": "11/1000",
              "original_spectral_budget": "1587/200000",
              "fixed_power_xi_and_fixed_L_tail_if_used_retained": True,
              "new_nonvanishing_global_coefficient_charge": "0",
              "sharp_signed_spectral_bound_proved": False,
              "terminal_0011_estimate_proved": False, "H_theta_proved": False, "certified_K": 0}
    save("switched_minorant_facets.json", facets)
    save("switched_minorant_reference.json", reference)
    save("switched_minorant_checks.json", checks)
    save("switched_minorant_audit.json", status)
    print(json.dumps({"all_exact_checks_passed": True,
                      "preserved_records": preserved["checkpoint27_nonmutable_records_verified"],
                      "short_padding_sites_checked": arithmetic["short_padding_sites_checked"],
                      "candidate_accepted": False,
                      "reference_loss_lower_coefficient": "1.56", "budget": ".0001",
                      "sharp_target_proved": False}, indent=2))


if __name__ == "__main__":
    main()
