#!/usr/bin/env python3
"""Checkpoint 27: a joint upper envelope and positive complement transfer.

The analytic arguments are in COUPLED_ONE_SIDED_NOTE.md. Finite arithmetic
checks and outward quadrature certify identities and constants, not the sharp
short-interval comparison. Python standard library only.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

from campaign import primes_upto
from structured_frontier import I

ROOT = Path(__file__).resolve().parents[1]
KAPPA = F(1, 1000)
SPECTRAL = F(1587, 200000)
SMOOTHING = F(613, 200000)
COMPLEMENT_DEFICIT = F(1, 10000)
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}


def demand(ok, message):
    if not ok:
        raise AssertionError(message)


def read_interval(record):
    return I(Decimal(record["lower"]), Decimal(record["upper"]))


def save(name, value):
    (ROOT / "results" / name).write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def preservation():
    path = ROOT / "results/checkpoint26_preservation_manifest.json"
    old = json.loads(path.read_text())
    demand(old["checkpoint"] == 26, "Frozen checkpoint 26 identity")
    count = 0
    for record in old["files"]:
        if record["path"] in MUTABLE:
            continue
        data = (ROOT / record["path"]).read_bytes()
        demand(len(data) == record["size_bytes"] and
               hashlib.sha256(data).hexdigest() == record["sha256"],
               "Preserved " + record["path"])
        count += 1
    demand(count == 268, "All historical nonmutable records")
    return {"checkpoint26_nonmutable_records_verified": count,
            "checkpoint26_manifest_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "negative_frontier_ledger_sha256": hashlib.sha256(
                (ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()}


def upper_sieve_constant(bins):
    # U(5)=1+integral_1^3 log(v)/(v+1) dv. |integrand''|<=2.
    step = F(2, bins)
    integral = I.point(0)
    for j in range(bins + 1):
        v = F(1) + j * step
        term = I.point(v).log() / (v + 1)
        integral = integral + term * (step / 2 if j in (0, bins) else step)
    error = F(4, 3 * bins * bins)
    value = 1 + integral + I.segment(-error, error)
    return F(16, 5) * value, {
        "bins": bins, "second_derivative_absolute_bound": "2",
        "integral_trapezoid_absolute_error": str(error),
        "normalized_U5": value.record()}


def rough_reference(bins):
    # B(u)=u*omega(u): B=1 on [1,2], B'=B(u-1)/(u-1) afterward.
    # On every grid cell (integer knots are grid boundaries), |omega''|<=2.
    step = F(1, bins)
    error = F(1, 6 * bins ** 3)
    values = [I.point(1)] * (bins + 1)
    for i in range(bins, 7 * bins):
        left = F(1) + i * step
        right = left + step
        derivative_left = values[i - bins] / (left - 1)
        derivative_right = values[i - bins + 1] / (right - 1)
        values.append(values[-1] + step / 2 *
                      (derivative_left + derivative_right) + I.segment(-error, error))
    explicit_three = 1 + I.point(2).log()
    demand(values[2 * bins].lo <= explicit_three.lo and
           values[2 * bins].hi >= explicit_three.hi,
           "Buchstab recursion contains exact B(3)=1+log(2)")
    return values[-1], {"bins_per_unit": bins, "trapezoid_cells": 6 * bins,
                       "cell_integral_error": str(error),
                       "omega_second_derivative_bound_on_unit_interiors": "2",
                       "integer_knots_are_grid_boundaries": True,
                       "explicit_B3_check_passed": True}


def coefficient_certificates(bins=8000):
    upper, upper_check = upper_sieve_constant(bins)
    a0, reference_check = rough_reference(bins)
    older_root = json.loads((ROOT / "results/negative_frontier_ledger.json").read_text())
    older_a0 = json.loads((ROOT / "results/signed_mass_ledger.json").read_text())
    prior_upper = read_interval(older_root["root"]["upper"])
    prior_a0 = read_interval(older_a0["reference"]["A0"])
    demand(prior_upper.lo <= upper.lo and upper.hi <= prior_upper.hi,
           "New upper constant enclosure refines frozen enclosure")
    demand(prior_a0.lo <= a0.lo and a0.hi <= prior_a0.hi,
           "New rough reference enclosure refines frozen enclosure")
    joint = json.loads((ROOT / "results/joint_signed_comparison.json").read_text())
    full = read_interval(joint["coefficient_budget"]["original_joint_reference_mass"])
    core = read_interval(json.loads((ROOT / "results/two_free_prime_reference.json").read_text())[
        "new_hybrid_core_reference"])
    scale = 1 + KAPPA
    centered = scale * (upper - full)
    coupled = centered + scale * core
    rough_discrepancy = scale * (upper - a0)
    available = SPECTRAL - rough_discrepancy
    reserve = available - COMPLEMENT_DEFICIT
    demand(reserve.lo > 0, "Explicit 1/10000 complement deficit leaves original spectral reserve")
    def rounded_up(interval, scale_unit=10 ** 6):
        q = F(interval.hi) * scale_unit
        return F(-(-q.numerator // q.denominator), scale_unit)
    c_center, c_coupled = rounded_up(centered), rounded_up(coupled)
    c_rough = rounded_up(rough_discrepancy, 10 ** 9)
    demand(c_rough + COMPLEMENT_DEFICIT < SPECTRAL,
           "Upward-rounded rough coefficient retains explicit transfer reserve")
    rest_reference = scale * (a0 - full)
    absolute_rest_lower = centered - SPECTRAL
    transferred = rough_discrepancy + COMPLEMENT_DEFICIT
    return {"bins": bins,
            "root_upper_formula": "(16/5)*(1+integral_1^3 log(v)/(v+1) dv)",
            "root_upper_coefficient": upper.record(),
            "rough_reference_A0_formula": "8*omega(8)",
            "rough_reference_A0": a0.record(),
            "original_marked_reference": full.record(),
            "hybrid_core_reference": core.record(),
            "whole_centered_coarse_upper_enclosure": centered.record(),
            "whole_centered_coarse_upper_coefficient": str(c_center),
            "whole_coupled_coarse_upper_enclosure": coupled.record(),
            "whole_coupled_coarse_upper_coefficient": str(c_coupled),
            "rough_centered_upper_enclosure": rough_discrepancy.record(),
            "rough_centered_upper_coefficient": str(c_rough),
            "positive_complement_reference": rest_reference.record(),
            "positive_complement_absolute_sufficient_lower_enclosure": absolute_rest_lower.record(),
            "positive_complement_maximum_deficit_enclosure": available.record(),
            "chosen_positive_complement_deficit": str(COMPLEMENT_DEFICIT),
            "transferred_spectral_coefficient_if_complement_input_holds": transferred.record(),
            "unused_spectral_reserve_after_chosen_deficit": reserve.record(),
            "upward_rounded_conditional_spectral_coefficient": str(c_rough + COMPLEMENT_DEFICIT),
            "upward_rounded_conditional_original_coefficient": str(
                c_rough + COMPLEMENT_DEFICIT + SMOOTHING),
            "guaranteed_reserve_after_rounding": str(SPECTRAL - c_rough - COMPLEMENT_DEFICIT),
            "smoothing_budget": str(SMOOTHING), "spectral_budget": str(SPECTRAL),
            "original_target": str(SMOOTHING + SPECTRAL),
            "fixed_power_and_fixed_L_criterion": "eta+xi+21147/L <= .007935-C_rough; xi from checkpoint22 (23)",
            "upper_quadrature_certificate": upper_check,
            "Buchstab_quadrature_certificate": reference_check,
            "sharp_target_proved": False}


def segmented_factors(lo, hi):
    residues = list(range(lo, hi + 1))
    factors = [[] for _ in residues]
    from math import isqrt
    for p in primes_upto(isqrt(hi)):
        first = (-lo) % p
        for i in range(first, len(residues), p):
            while residues[i] % p == 0:
                factors[i].append(p)
                residues[i] //= p
    for i, remainder in enumerate(residues):
        if remainder > 1:
            factors[i].append(remainder)
    return factors


def actual_mark(N, n, factors):
    # Direct canonical encoding of original c_N. No stress cutoffs here.
    total = F(0)
    if len(factors) == 2:
        for p in set(factors):
            if p ** 4 >= N and p ** 20 < N ** 19:
                total += 1
    elif len(factors) == 3:
        for q in set(factors):
            pair = factors.copy()
            pair.remove(q)
            p, r = sorted(pair)
            if p ** 4 >= N and r ** 4 >= N and p * r * r <= N * N:
                total += F(1, 2) if p == r else F(1)
    return total


def complement_checks():
    cases = []
    sites = 0
    for N in (65536, 65538, 70000):
        lo, hi = N * N - N - 1, N * N + N + 1
        counter = Counter()
        mass, complement = F(0), F(0)
        for offset, factors in enumerate(segmented_factors(lo, hi)):
            n = lo + offset
            rough = factors[0] ** 4 >= N
            mark = actual_mark(N, n, factors)
            demand(F(0) <= mark <= int(rough), "Actual narrow-padding mark cap")
            positive = int(rough) * (1 - min(F(1), mark))
            demand(positive == int(rough) - mark, "Exact short positive complement identity")
            degree = len(factors)
            base = int(rough and (degree == 1 or degree >= 4 or
                       (degree == 2 and factors[0] ** 20 >= N ** 19)))
            residual = positive - base
            demand(residual >= 0, "Positive unmarked degree decomposition")
            if residual:
                demand(degree == 3 and len(set(factors)) < 3,
                       "Only repeated three-prime rows contribute decomposition residual")
                counter["repeated_three_prime_residual_rows"] += 1
            if rough and degree == 3 and len(set(factors)) == 3:
                demand(mark == 1, "Every squarefree three-prime row carries its canonical mark")
                counter["squarefree_three_prime_rows"] += 1
            counter["sites"] += 1
            counter["rough_sites"] += int(rough)
            mass += mark
            complement += positive
        demand(mass + complement == counter["rough_sites"], "Total short partition")
        sites += counter["sites"]
        cases.append({"N": N, **dict(counter), "marked_mass": str(mass),
                      "positive_complement_mass": str(complement),
                      "original_cutoffs_used": True})
    # A broad window intentionally contains multiple marks; positivity uses clipping.
    N = 62
    lo, hi = N * N // 2, 3 * N * N // 2
    long_rows, excess, max_mark = 0, F(0), F(0)
    witness = None
    for offset, factors in enumerate(segmented_factors(lo, hi)):
        n = lo + offset
        rough = factors[0] ** 4 >= N
        mark = actual_mark(N, n, factors)
        demand(mark == 0 or rough, "Prime-mark rough support on broad comparison window")
        raw = int(rough) - mark
        positive = int(rough) * (1 - min(F(1), mark))
        demand(positive >= 0 and positive - raw == max(F(0), mark - 1),
               "Positive clipping identity on broad window")
        if mark > 1:
            long_rows += 1
            excess += mark - 1
        max_mark = max(max_mark, mark)
        if n == 2431:
            witness = {"n": n, "mark": str(mark), "raw_complement": str(raw),
                       "positive_complement": str(positive)}
    demand(witness is not None and witness["mark"] == "3", "Historical multiple-mark witness retained")
    return {"short_cases": cases, "short_padding_sites_checked": sites,
            "broad_stress_window": {"N": N, "window": [lo, hi],
               "artificial_window_not_the_asymptotic_long_reference": True,
               "multiple_mark_sites": long_rows, "excess_mark_mass": str(excess),
               "maximum_mark": str(max_mark), "witness": witness},
            "finite_rows_do_not_prove_a_uniform_sharp_estimate": True}


def signed_and_lower_scope_checks():
    from campaign import least_prime_factor
    def mu(n):
        sign = 1
        while n > 1:
            p = least_prime_factor(n)
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        return sign
    def beta(m, U):
        return -sum(mu(t) for t in range(1, U + 1) if m % t == 0)
    demand(beta(30, 5) == 2 and beta(7, 5) == -1, "Actual beta kernel has both signs")
    # For prime b=7 in p=210, the stress U=5 Vaughan TypeII term is positive.
    # The identity is algebraic; this is not the asymptotic N-dependent cutoff.
    positive_numerator = beta(30, 5)
    demand(positive_numerator > 0, "Positive TypeII coefficient exists")
    demand(F(5, 4) < 2, "Final prime lower sieve is below its positive f range")
    demand((F(5, 4) - F(19, 20)) / (1 - F(19, 40)) == F(4, 7),
           "Unmarked balanced semiprime final-cofactor upper s")
    # Four-prime support: gamma>=3/4 and third-prime exponent>=1/4.
    demand(F(5, 4) - F(3, 4) - 2 * F(1, 4) == 0,
           "Four-prime lower-sieve positive margin absent at limiting corner")
    return {"actual_beta_both_signs": {"U": 5, "beta_30": 2, "beta_7": -1},
            "positive_outer_TypeII_stress_witness": {"p": 210, "b_p": 7, "m": 30,
                "U": 5, "coefficient_numerator": positive_numerator,
                "stress_cutoff_only_not_uniform_shell_evidence": True},
            "direct_final_cofactor_lower_sieve": {
                "unmarked_prime_limiting_s": "5/4 < 2",
                "unmarked_balanced_semiprime_maximum_s": "4/7 < 2",
                "four_prime_limiting_level_minus_twice_last_sifting_exponent": "0",
                "fixed_slack_four_prime_margin": "negative",
                "five_or_more_prime_outer_gamma": ">=1, outside gamma<1 input",
                "scope": "Direct final-cofactor linear lower sieve with the admitted 5/4-gamma level",
                "all_other_transfers_excluded": False}}


def main():
    old = preservation()
    coefficients = coefficient_certificates()
    print(json.dumps({"stage": "coefficient_certificates",
                      "root_upper": coefficients["root_upper_coefficient"],
                      "rough_transfer_reserve": coefficients["unused_spectral_reserve_after_chosen_deficit"]}), flush=True)
    arithmetic = complement_checks()
    scope = signed_and_lower_scope_checks()
    checks = {"preservation": old, "arithmetic": arithmetic, "source_scope": scope,
              "outward_quadrature": {"root_upper": coefficients["upper_quadrature_certificate"],
                                     "rough_reference": coefficients["Buchstab_quadrature_certificate"]},
              "all_exact_checks_passed": True, "sharp_target_proved": False}
    status = {"date": "2026-10-12", "checkpoint": 27, "proof_note": "COUPLED_ONE_SIDED_NOTE.md",
              "whole_coupled_one_sided_envelope_proved": True,
              "whole_coupled_upper_coefficient": coefficients["whole_coupled_coarse_upper_coefficient"],
              "whole_centered_upper_coefficient": coefficients["whole_centered_coarse_upper_coefficient"],
              "positive_short_complement_identity_proved": True,
              "normalized_long_positive_clipping_error_o_u_proved": True,
              "positive_complement_sufficient_lower_deficit": "1/10000",
              "rough_centered_upper_coefficient": coefficients["rough_centered_upper_coefficient"],
              "conditional_spectral_upper_coefficient": coefficients[
                  "upward_rounded_conditional_spectral_coefficient"],
              "positive_complement_sharp_lower_comparison_proved": False,
              "original_spectral_budget": str(SPECTRAL), "original_smoothing_budget": str(SMOOTHING),
              "new_nonvanishing_coefficient_charge": "0",
              "original_target": "11/1000", "sharp_signed_spectral_bound_proved": False,
              "terminal_0011_estimate_proved": False, "H_theta_proved": False, "certified_K": 0}
    save("coupled_one_sided_coefficients.json", coefficients)
    save("coupled_one_sided_checks.json", checks)
    save("coupled_one_sided.json", status)
    print(json.dumps({"all_exact_checks_passed": True, "preserved_records": old[
        "checkpoint26_nonmutable_records_verified"], "short_padding_sites_checked": arithmetic[
        "short_padding_sites_checked"], "coupled_coarse_upper": status["whole_coupled_upper_coefficient"],
        "complement_deficit_input_proved": False, "sharp_target_proved": False}, indent=2))


if __name__ == "__main__":
    main()
