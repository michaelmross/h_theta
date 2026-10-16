#!/usr/bin/env python3
"""Checkpoint 32: test modern generic bounds after exact recombination.

The required short-window lower bound remains unproved. This verifies
the continuous mixed-moment source obstruction and the reference cost
of omitting its physical box. No actual large-value states or negative
short discrepancies are asserted to occur.
"""
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOX = ((F(2, 5), F(43, 100)), (F(9, 20), F(47, 100)),
       (F(101, 200), F(21, 40)))
TAU, LEVEL = F(1, 2), F(3, 10)
LOWER_LENGTH, UPPER_LENGTH = F(199, 400), F(201, 400)
MIN_PROFILE, BOX_REF_ROUND = F(301, 1000), F(351, 10**6)
REMAINING = F(99, 10**6)
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}


def demand(value, message):
    if not value:
        raise AssertionError(message)


def save(name, value):
    (ROOT / "results" / name).write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def decimal_enclosure(q):
    values = []
    for rounding in (ROUND_FLOOR, ROUND_CEILING):
        with localcontext() as c:
            c.prec, c.rounding = 55, rounding
            values.append(str(Decimal(q.numerator)/Decimal(q.denominator)))
    return {"exact_fraction": str(q), "lower": values[0], "upper": values[1],
            "scope": "enclosure of the rational lower certificate, not the full reference mass"}


def preservation():
    p = ROOT / "results/checkpoint31_preservation_manifest.json"
    old = json.loads(p.read_text())
    demand(old["checkpoint"] == 31, "Frozen checkpoint31 identity")
    count = 0
    for record in old["files"]:
        if record["path"] in MUTABLE:
            continue
        data = (ROOT / record["path"]).read_bytes()
        demand(len(data) == record["size_bytes"] and
               hashlib.sha256(data).hexdigest() == record["sha256"],
               "Preserved " + record["path"])
        count += 1
    demand(count == 305, "All nonmutable checkpoint31 records")
    return {"checkpoint31_nonmutable_records_verified": count,
            "checkpoint31_manifest_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "negative_frontier_ledger_sha256": hashlib.sha256(
                (ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()}


def source_K(b, v, tau):
    k0 = min(tau+b*(6*v-2),
             max(tau+b*(4*v-F(8, 5)), tau/2+b*(4*v-1)),
             tau+b*(2*v-1))
    return min(tau, max(2*b*v, k0))


def reduced_K(b, tau=TAU):
    return min(tau, max(F(3, 5)*b, tau-F(2, 5)*b))


def moments():
    return [ks for ks in product(range(5), repeat=4) if 0 < sum(ks) <= 4]


def source_formula_checks():
    rows = 0
    for tau in (F(2, 5), F(49, 100), F(999, 2000), TAU, F(51, 100)):
        for n in range(1, 501):
            beta = F(n, 200)
            demand(source_K(beta, LEVEL, tau) == reduced_K(beta, tau),
                   "Exact critical-level profile simplification")
            rows += 1
    return {"rational_profile_rows": rows,
            "critical_source_level": "3/10",
            "reduced_profile": "min(tau,max(3*b/5,tau-2*b/5))",
            "unrestricted_beta_minimum_at_tau_half": "3/10, attained only at b=1/2",
            "test_is_of_available_upper_envelopes_not_actual_level_set_sizes": True}


def source_facets():
    vertices = []
    for a, b, c in product(*BOX):
        d = 2-a-b-c
        demand(F(23, 40) <= d <= F(129, 200), "Fourth physical exponent envelope")
        demand(a < b < c < d and sum((a, b, c, d)) == 2,
               "Sorted physical prime quartet, all original band gates")
        vertices.append(tuple(t/2 for t in (a, b, c, d)))
    ks_list = moments()
    demand(len(ks_list) == comb(8, 4)-1 == 69, "All fixed mixed moments through degree four")
    intervals, corner_rows = [], 0
    for ks in ks_list:
        degree = sum(ks)
        lengths = [sum(k*t for k, t in zip(ks, beta)) for beta in vertices]
        low, high = min(lengths), max(lengths)
        if degree <= 2:
            demand(high <= LOWER_LENGTH or low >= UPPER_LENGTH,
                   "Continuous exclusion of the critical half-length")
        else:
            demand(low >= F(3, 5), "Analytic higher-moment lower length")
        # No interval straddles tau=1/2, so the profile minimum is at
        # the appropriate endpoint. The analytic proof is in the note.
        demand(high < TAU or low > TAU, "Profile monotonic on the complete length interval")
        envelope_min = reduced_K(high) if high < TAU else reduced_K(low)
        interior_tau = F(999, 2000)
        envelope_min_interior = (reduced_K(high, interior_tau) if high < interior_tau
                                 else reduced_K(low, interior_tau))
        demand(envelope_min >= MIN_PROFILE, "Uniform limiting positive source gap")
        demand(envelope_min_interior >= F(601, 2000), "Gap below source endpoint")
        for beta in lengths:
            demand(source_K(beta, LEVEL, TAU) == reduced_K(beta), "All source terms kept")
            demand(reduced_K(beta) >= MIN_PROFILE, "Every corner profile gap")
            corner_rows += 1
        intervals.append({"mixed_powers": list(ks), "degree": degree,
                          "length_interval": [str(low), str(high)],
                          "profile_minimum": str(envelope_min),
                          "profile_minimum_at_tau_999_over_2000": str(envelope_min_interior)})
    # Higher degrees are not a finite-sampling claim: every primitive
    # beta is >=1/5, so degree >=3 gives b>=3/5 and K>=9/25.
    demand(reduced_K(F(3, 5)) == F(9, 25), "Infinite higher-degree certificate")
    demand(min(F(v["profile_minimum"]) for v in intervals) == MIN_PROFILE,
           "Uniform certificate is attained at a corner")
    examples = []
    physical = [(F(83, 200), F(23, 50), F(103, 200), F(61, 100)),
                (F(2, 5), F(8, 15), F(8, 15), F(8, 15))]
    for alpha in physical:
        beta = tuple(v/2 for v in alpha)
        values = [(reduced_K(sum(k*t for k, t in zip(ks, beta))), ks)
                  for ks in ks_list]
        best, winner = min(values)
        examples.append({"physical_N_exponents": list(map(str, alpha)),
                         "source_x_exponents": list(map(str, beta)),
                         "best_profile": str(best), "winning_mixed_powers": list(winner),
                         "source_upper_envelope_integral_exponent": str(best+F(1, 5)),
                         "strict_gap_relative_to_required_half": str(best-LEVEL)})
    demand(F(examples[0]["best_profile"]) == F(61, 200), "Interior illustration")
    demand(F(examples[1]["best_profile"]) == F(47, 150), "Earlier physical vertex illustration")
    return {"physical_sorted_box": [[str(lo), str(hi)] for lo, hi in BOX],
            "fourth_physical_exponent_range": ["23/40", "129/200"],
            "physical_vertices": [list(map(str, tuple(2*t for t in b))) for b in vertices],
            "mixed_moment_families_through_degree_four": len(ks_list),
            "exact_corner_rows": corner_rows,
            "critical_source_profile_lower": str(MIN_PROFILE),
            "required_critical_level_set_exponent": str(LEVEL),
            "source_upper_envelope_power_loss_in_x": "1/1000",
            "source_upper_envelope_integral_exponent_lower": "501/1000",
            "interior_tau": "999/2000", "interior_source_profile_lower": "601/2000",
            "all_fixed_higher_mixed_integer_moments_covered_analytically": True,
            "actual_integral_or_cardinality_lower_bound_asserted": False,
            "other_joint_or_phase_sensitive_methods_excluded": False,
            "examples": examples, "continuous_length_intervals": intervals}


def reference_budget_checks():
    volume = F(3, 100)*F(1, 50)*F(1, 50)
    denominator = F(43, 100)*F(47, 100)*F(21, 40)*F(129, 200)
    defect = F(5, 32)**5
    raw = 2*volume/denominator
    weighted = (1+F(1, 1000))*(1-defect)*raw
    demand(raw == F(640, 1824963), "Unsmoothed unweighted rational box lower bound")
    demand(weighted == F(1599278967, 4556220006400), "Smoothed actual-weight rational lower bound")
    demand(weighted > BOX_REF_ROUND > REMAINING, "Omission exceeds all remaining budget")
    initial_kernel = F(1, 10**6)
    rough, smoothing = F(7825257, 10**9), F(3065, 10**6)
    total = rough+smoothing+initial_kernel+REMAINING
    reserve = F(11, 1000)-total
    demand(total == F(10990257, 10**9) and reserve == F(9743, 10**9),
           "Frozen conditional global coefficients and reserve")
    return {"box_volume": str(volume), "denominator_product_upper": str(denominator),
            "kernel_defect_upper": str(defect),
            "unweighted_unsmoothed_reference_lower_certificate": decimal_enclosure(raw),
            "actual_weight_smoothed_reference_lower_certificate": decimal_enclosure(weighted),
            "actual_weight_smoothed_reference_downward_round": ".000351",
            "remaining_comparison_and_rest_allowance": ".000099",
            "reference_lower_over_remaining_budget": str(weighted/REMAINING),
            "whole_reference_mass_not_reestimated": True,
            "actual_short_negative_deficit_asserted": False,
            "box_omission_charge_added_to_global_ledger": False,
            "conditional_kernel_charge_retained": ".000001",
            "original_spectral_allowance": ".007935", "original_final_allowance": ".011",
            "conditional_original_coefficient_before_later_xi_or_tail": str(total),
            "conditional_remaining_xi_or_fixed_tail_reserve": str(reserve)}


def multiplier_checks():
    first_arg, second_arg = F(51, 100), F(1, 1000)
    lower = (1-first_arg**2/6)*(1-second_arg**2/6)
    demand(lower > F(95, 100) > F(9, 10), "Sinc lower bound survives asymptotic O(1/N) error")
    return {"critical_frequency_block": "[N/2,N]",
            "trapezoid_rectangular_convolution_lengths": ["(1+kappa)*Y", "kappa*Y"],
            "sinc_argument_upper_bounds_for_large_N": [str(first_arg), str(second_arg)],
            "rational_leading_sinc_product_lower": str(lower),
            "exact_Mellin_approximation_uniform_error": "O(1/N)",
            "actual_Mellin_multiplier_lower_for_sufficiently_large_N": ".9",
            "frequency_block_discarded": False,
            "actual_centered_integral_lower_bound_asserted": False}


def source_audit():
    return {"date": "2026-10-13", "checkpoint": 32,
            "primary_source": {"authors": "K. Matomaki, M. Pandey, J. Pliego, J. Teravainen and M. Wang",
                "title": "Higher order uniformity of the primes and cancellation of the Mobius function in shorter intervals",
                "version": "arXiv:2610.09567v1",
                "url": "https://arxiv.org/html/2610.09567v1",
                "checked_items": ["Definition 2.2", "Lemma 2.3(i) and proof, including powers and dyadic splitting", "Lemma 2.3(ii) actual coefficient class", "Lemma 3.1", "Proposition 3.2 and its strict tau<1/2 and positivity hypotheses"],
                "generic_LV_coefficient_class": "Fixed divisor-order and logarithm bounded coefficients",
                "generic_LV_height_range": "0<tau<=1; critical tau=1/2 admitted for Lemma2.3",
                "mean_value_proposition_height_range": "0<tau<1/2; no endpoint invocation asserted",
                "free_coefficient_refinement_admitted_for_recombined_prime_slots": False,
                "all_fixed_mixed_integer_moments_included_in_test": True,
                "strict_source_positivity_on_retained_box_passed": False},
            "actual_coupling_retained_before_absolute_source_test": True,
            "actual_80_and_325_terms_recombined": True,
            "actual_large_value_states_shown_to_exist": False,
            "original_weight_or_sector_changed": False,
            "uniform_sharp_short_lower_estimate_proved": False,
            "general_impossibility_result_claimed": False,
            "remaining_options": ["Actual-prime joint large-value information", "One-sided estimate retaining the oscillatory phase", "Different source-complete decomposition retaining the original coefficient"]}


def main():
    protected = preservation()
    formula = source_formula_checks()
    facets = source_facets()
    budget = reference_budget_checks()
    multiplier = multiplier_checks()
    sources = source_audit()
    checks = {"preservation": protected, "source_formula": formula,
              "continuous_mixed_moment_certificate": facets,
              "box_reference_and_budget": budget, "critical_multiplier": multiplier,
              "checks_do_not_prove_actual_short_inequality": True}
    result = {"date": "2026-10-13", "checkpoint": 32,
              "proof_note": "SHARP_SHORT_WINDOW_TEST_NOTE.md",
              "status": "Sharp short comparison remains unproved; recombined generic mixed-moment route fails its sufficient source criterion",
              "actual_short_input": "P_N(psi_Y)-C_N(psi_Y)>=-(eta_W+o(1))*u",
              "equivalent_coupled_input": "L_N(psi_Y)+B_N(psi_Y)>=-(eta_W+o(1))*u",
              "sharp_actual_short_input_proved": False,
              "actual_deficit_coefficient_improved": False,
              "coarse_centered_kernel_lower_coefficient_unchanged": "-.010008",
              "new_source_profile_gap_in_x": ".001",
              "gap_is_in_an_upper_envelope_not_the_actual_error": True,
              "box_smoothed_actual_weight_reference_lower": budget["actual_weight_smoothed_reference_lower_certificate"],
              "box_can_be_omitted_within_current_budget": False,
              "actual_short_counterexample_found": False,
              "original_least_prime_or_frequency_sector_discarded": False,
              "new_nonvanishing_charge_added": "0",
              "retained_conditional_kernel_charge": ".000001",
              "eta_W_plus_eta_rest_allowance": ".000099",
              "K": 0, "H_theta_proved": False, "milestone7": "deferred",
              "next_actual_analytic_input": "Prime-specific joint or one-sided phase-sensitive estimate on the retained box, or its contribution in the full coupled short comparison",
              "preserved_checkpoint31_nonmutable_records": 305}
    save("sharp_short_window_test.json", result)
    save("sharp_short_window_test_checks.json", checks)
    save("sharp_short_window_source_audit.json", sources)
    print(json.dumps({"checkpoint": 32, "preserved_records": 305,
                      "source_formula_rows": formula["rational_profile_rows"],
                      "mixed_moment_families": facets["mixed_moment_families_through_degree_four"],
                      "source_corners": facets["exact_corner_rows"],
                      "box_reference_lower": budget["actual_weight_smoothed_reference_downward_round"],
                      "sharp_actual_short_input_proved": False}, indent=2), flush=True)


if __name__ == "__main__":
    main()
