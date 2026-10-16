#!/usr/bin/env python3
"""Checkpoint 9: actual prime-product reduction of the first frontier.

General proofs are in RESTRICTED_FRONTIER_NOTE.md. Finite experiments are
consistency checks, not uniform asymptotic estimates. Standard library only.
"""

from __future__ import annotations

import argparse
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from decimal import Decimal
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json

from ross_geometry_audit import factor_band, primes_up_to, require
from structured_frontier import DOWN, UP, NEAR, I, ROOT


def sum_intervals(values):
    total = I.point(0)
    for value in values:
        total = total + value
    return total


def interval_from_record(value):
    return I(Decimal(value["lower"]), Decimal(value["upper"]))


def intersection(a, b):
    return I(max(a.lo, b.lo), min(a.hi, b.hi))


def integer_root_ceiling(value, degree):
    lo, hi = 0, 1
    while hi ** degree < value:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** degree >= value:
            hi = mid
        else:
            lo = mid
    return hi


def exp_interval(value):
    # Decimal.exp is correctly rounded to nearest; adjacent numbers enclose.
    lo, hi = NEAR.exp(value.lo), NEAR.exp(value.hi)
    return I(NEAR.next_minus(lo), NEAR.next_plus(hi))


def rounded_reference_length(n):
    x = n * n
    cube_root = exp_interval(I.point(x).log().log() / 3)
    real_length = x * exp_interval(-3 * cube_root)
    half = real_length / 2
    require(int(half.lo) == int(half.hi),
            "Reference length rounding is not decided at current precision")
    length = 2 * int(half.lo) + 1
    return length, real_length


def large_square_bound(n, lo, hi):
    h = hi - lo + 1
    first = integer_root_ceiling(n, 4)
    total = F(0)
    d = first
    while d * d <= hi:
        total += 2 * F(h, d) + min(F(d), F(hi, d * d))
        d *= 2
    simplified = 4 * F(h, first) + F(10, 3) * integer_root_ceiling(hi, 3)
    require(total <= simplified, "Dyadic large-square bound")
    return total, simplified


def band_degree_counts(n, lo, hi, chunk_size=20000):
    primes = primes_up_to(isqrt(hi))
    raw, weighted = Counter(), defaultdict(F)
    frontier_raw, frontier_weighted = Counter(), defaultdict(F)
    lam_root = lam_frontier = repeated = repeated_frontier = 0
    for begin in range(lo, hi + 1, chunk_size):
        band = factor_band(begin, min(hi, begin + chunk_size - 1), primes)
        for m, factors in band.items():
            least = min(factors)
            if least ** 4 < n:
                continue
            degree = sum(factors.values())
            require(degree <= 8, "Unexpected rough degree beyond eight")
            denominator = 1
            for exponent in factors.values():
                denominator *= factorial(exponent)
            weight = F(1, denominator)
            raw[degree] += 1
            weighted[degree] += weight
            lam_root += (-1) ** degree
            squareful = any(e > 1 for e in factors.values())
            repeated += squareful
            is_frontier = least ** 20 < n ** 19
            if degree >= 3:
                require(is_frontier, "Cutoff must be vacuous beyond degree two")
            if is_frontier:
                require(degree >= 2, "A prime cannot enter this frontier")
                frontier_raw[degree] += 1
                frontier_weighted[degree] += weight
                repeated_frontier += squareful
                lam_frontier += (-1) ** degree
    front = sum(frontier_raw.values())
    kernel = sum((frontier_weighted[j] for j in range(2, 8)), F(0))
    signed_kernel = sum(
        ((-1) ** j * frontier_weighted[j] for j in range(2, 8)), F(0))
    correction = F(front) - kernel
    signed_correction = F(lam_frontier) - signed_kernel
    require(0 <= correction <= repeated_frontier + frontier_raw[8],
            "Positive repeated-factor/degree-eight correction")
    require(abs(signed_correction) <= correction, "Signed parity correction")
    bound, simple = large_square_bound(n, lo, hi)
    require(repeated <= bound, "Uniform repeated-prime bound")
    return {
        "endpoints": [lo, hi], "integer_positions": hi - lo + 1,
        "raw_rough_degrees": {str(j): raw[j] for j in range(1, 9)},
        "factorial_rough_degrees": {str(j): str(weighted[j]) for j in range(1, 9)},
        "raw_frontier_degrees": {str(j): frontier_raw[j] for j in range(2, 9)},
        "factorial_frontier_degrees": {
            str(j): str(frontier_weighted[j]) for j in range(2, 9)},
        "R095": front, "seven_degree_kernel": str(kernel),
        "nonnegative_kernel_correction": str(correction),
        "rough_Liouville_sum": lam_root, "frontier_Liouville_sum": lam_frontier,
        "signed_kernel": str(signed_kernel), "signed_correction": str(signed_correction),
        "repeated_rough_rows": repeated, "repeated_frontier_rows": repeated_frontier,
        "large_square_dyadic_bound": str(bound),
        "large_square_simplified_bound": str(simple),
    }


def direct_prime_tuple_checks(n):
    """Independent nondecreasing tuple enumeration on four small fixtures."""
    lo, hi = n * n - n // 2, n * n + n // 2
    smallest = integer_root_ceiling(n, 4)
    primes = [p for p in primes_up_to(hi // smallest) if p ** 4 >= n]
    observed = defaultdict(F)
    rows = set()

    def visit(prefix, partial, start, remaining):
        if remaining == 1:
            lower = max(primes[start], (lo + partial - 1) // partial)
            upper = hi // partial
            for index in range(bisect_left(primes, lower),
                               bisect_right(primes, upper)):
                values = prefix + [primes[index]]
                if values[0] ** 20 >= n ** 19:
                    continue
                multiplicities = Counter(values)
                denominator = 1
                for count in multiplicities.values():
                    denominator *= factorial(count)
                degree = len(values)
                observed[degree] += F(1, denominator)
                rows.add(partial * primes[index])
            return
        for index in range(start, len(primes)):
            p = primes[index]
            if partial * p ** remaining > hi:
                break
            visit(prefix + [p], partial * p, index, remaining - 1)

    for degree in range(2, 8):
        visit([], 1, 0, degree)
    counted = band_degree_counts(n, lo, hi)
    for degree in range(2, 8):
        require(observed[degree] == F(counted["factorial_frontier_degrees"][str(degree)]),
                "Tuple enumeration disagrees with factorization")
    require(len(rows) == counted["R095"], "Tuple support differs from frontier")
    require(counted["raw_rough_degrees"]["8"] == 0, "Actual depth-eight exclusion")
    actual_square_hits = sum(
        hi // (d * d) - (lo - 1) // (d * d)
        for d in range(smallest, isqrt(hi) + 1))
    require(actual_square_hits <= F(counted["large_square_dyadic_bound"]),
            "Direct large-square incidence check")
    return {"N": n, "direct_tuple_weights": dict((str(j), str(observed[j]))
             for j in range(2, 8)), "all_checks_passed": True}


def component_masses(bins):
    """Outward positive-convolution integrals at s=8.

g1(s)=1/s on s>=1. For j>=2,
g_j(s)=(1/s)*integral_(j-1)^(s-1) g_(j-1)(v) dv.
On a cell, bound its increasing numerator integral by endpoint prefixes,
and its positive denominator by the reversed endpoints. g2 is used in
closed form to remove uncertainty from the degree-two mass.
"""
    h = F(1, bins)
    size = 8 * bins
    zero = I.point(0)
    cells = [zero] * size
    for index in range(2 * bins, size):
        a, b = index * h, (index + 1) * h
        cells[index] = I.segment(a - 1, b - 1).log() / I.segment(a, b)
    degree_values = {1: I.point(1), 2: I.point(7).log()}
    for degree in range(3, 8):
        prefix = [zero]
        for cell in cells:
            prefix.append(prefix[-1] + h * cell)
        value = prefix[7 * bins] / 8
        degree_values[degree] = 8 * value
        new_cells = [zero] * size
        for index in range(degree * bins, size):
            low = prefix[index - bins].lo
            high = prefix[index + 1 - bins].hi
            new_cells[index] = I(low, high) / I.segment(index * h, (index + 1) * h)
        cells = new_cells
    degree_values[8] = zero
    high_semiprime = (I.point(F(21, 19))).log()
    front_two = degree_values[2] - high_semiprime
    tail = sum_intervals(degree_values[j] for j in range(4, 8))
    raw_root = sum_intervals(degree_values.values())
    old = json.loads((ROOT / "results/frontier_investigation.json").read_text())
    overlap = intersection(raw_root, interval_from_record(old["ordinary_root"]))
    frontier = overlap - 1 - high_semiprime
    require(tail.hi < Decimal(".3268"), "Higher-degree budget guide too loose")
    grouped = {
        "two_prime_frontier": front_two,
        "three_prime_frontier": degree_values[3],
        "four_to_seven_prime_frontier": tail,
    }
    budget = I.point(F(169, 500)) - tail
    parity_model_components = {
        "two_prime_excess": front_two,
        "three_prime_excess": -degree_values[3],
        "higher_degree_excess": sum_intervals(
            ((-1) ** j * degree_values[j]) for j in range(4, 8)),
    }
    parity_excess = sum_intervals(parity_model_components.values())
    require(parity_excess.lo > Decimal(".89"), "Parity mass diagnosis mismatch")
    return {
        "bins_per_unit": bins, "normalization": "u=N/(2 log N)",
        "recursion": "s*g_j(s)=int_(j-1)^(s-1) g_(j-1)(v) dv",
        "reference_argument": "s=8; c_j=8*g_j(8)",
        "degree_coefficients": {str(j): degree_values[j].record()
                                for j in range(1, 9)},
        "rough_semiprime_high_cutoff": high_semiprime.record(),
        "frontier_groups": {key: value.record() for key, value in grouped.items()},
        "ordinary_root_raw": raw_root.record(),
        "ordinary_root_checkpoint7_overlap": overlap.record(),
        "ordinary_frontier_095": frontier.record(),
        "budget_left_if_higher_short_count_is_at_most_twice_reference": budget.record(),
        "factor_two_higher_short_cap_proved": False,
        "parity_mass_model": {
            "degree_excesses": {
                key: value.record() for key, value in parity_model_components.items()},
            "total_excess": parity_excess.record(),
            "actual_short_support_or_power_error_matched": False,
        },
        "component_masses_are_short_upper_bounds": False,
    }


def four_factor_certificate():
    coefficients = (F(57, 28), F(133, 66), F(61, 30), F(27, 13))
    source_derivations = (
        "Sum of four individual lower bounds",
        "Sum of four individual lower bounds",
        "alpha4+2*alpha3>=w and alpha4>=2*w/5 imply alpha3+alpha4>=7*w/10",
        "alpha1>=w and 1-alpha1>=14*w/13",
    )
    records = []
    for index, coefficient in enumerate(coefficients):
        threshold = 1 - 1 / coefficient
        excess = coefficient / 2 - 1
        require(excess > 0, "Four-factor endpoint inequality not contradictory")
        records.append({
            "case": index + 1, "coefficient_of_w": str(coefficient),
            "necessary_interval_exponent": str(threshold),
            "contradiction_at_interval_exponent_one_half": str(excess),
            "derivation": source_derivations[index],
        })
    require(min(1 - 1 / c for c in coefficients) == F(67, 133),
            "Four-factor minimum threshold")
    return {
        "source": "Li arXiv:2308.04458v8 Lemma 4.2, four printed cases",
        "url": "https://arxiv.org/html/2308.04458v8",
        "exponent_units": "x; w=1-interval_exponent",
        "constraints_used": "alpha_j>0; sum alpha_j=1; printed necessary facets",
        "all_groupings_and_all_positive_factor_decompositions_excluded_at_endpoint": True,
        "four_cases": records,
        "minimum_necessary_interval_exponent": "67/133",
        "source_applied_at_endpoint": False,
        "necessary_conditions_are_sufficient": False,
        "other_large_values_methods_excluded": False,
    }


def finite_centered_experiment(n):
    x, y = n * n, n + 1
    h, h_record = rounded_reference_length(n)
    short = band_degree_counts(n, x - n // 2, x + n // 2)
    long = band_degree_counts(n, x - h // 2, x + h // 2)
    require(short["raw_rough_degrees"]["8"] == 0, "Short degree-eight exclusion")
    scale = F(y, h)
    degree_excesses = {}
    for degree in range(2, 8):
        key = str(degree)
        degree_excesses[key] = (
            F(short["factorial_frontier_degrees"][key])
            - scale * F(long["factorial_frontier_degrees"][key]))
    kernel_excess = sum(degree_excesses.values(), F(0))
    raw_excess = F(short["R095"]) - scale * long["R095"]
    correction_excess = F(short["nonnegative_kernel_correction"]) - scale * F(
        long["nonnegative_kernel_correction"])
    require(raw_excess == kernel_excess + correction_excess,
            "Centered correction identity")
    u = n / (2 * I.point(n).log())
    normalized = I.point(raw_excess) / u
    groups = {
        "two_prime": degree_excesses["2"],
        "three_prime": degree_excesses["3"],
        "higher_prime": sum((degree_excesses[str(j)] for j in range(4, 8)), F(0)),
        "controlled_correction": correction_excess,
    }
    return {
        "N": n, "Y": y, "rounded_long_length": h,
        "unrounded_long_length_enclosure": h_record.record(),
        "short": short, "long": long,
        "centered_frontier_excess_exact": str(raw_excess),
        "centered_kernel_excess_exact": str(kernel_excess),
        "centered_correction_exact": str(correction_excess),
        "normalized_excess": normalized.record(),
        "grouped_normalized_excess": {
            key: (I.point(value) / u).record() for key, value in groups.items()},
        "finite_0338_bound_holds": normalized.hi <= Decimal(".338"),
        "asymptotic_conclusion_inferred": False,
    }


def write_json(relative, value):
    (ROOT / relative).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bins", type=int, default=20000)
    parser.add_argument("--skip-experiments", action="store_true")
    args = parser.parse_args()
    require(args.bins >= 4000, "At least 4000 cells per unit required")
    ledger = ROOT / "results/negative_frontier_ledger.json"
    require(hashlib.sha256(ledger.read_bytes()).hexdigest() ==
            "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
            "Historical ledger changed")
    tuple_checks = [direct_prime_tuple_checks(n) for n in (20, 40, 80, 120)]
    masses = component_masses(args.bins)
    write_json("results/frontier_prime_product_mass.json", masses)
    four = four_factor_certificate()
    write_json("results/frontier_four_factor_certificate.json", four)
    experiments = []
    if not args.skip_experiments:
        ns = sorted(set([5000, 14640, 28560, 50000, 83520, 100000] +
                        list(range(10000, 20001, 1000))))
        for n in ns:
            result = finite_centered_experiment(n)
            experiments.append(result)
            print("Exact centered experiment completed: N=" + str(n), flush=True)
        require(any(e["long"]["raw_rough_degrees"]["8"] > 0 for e in experiments),
                "The long-reference degree-eight boundary was not exercised")
        finite = {
            "method": "Segmented exact factorization; exact factorial weights and normalization",
            "reference_rounding": "Nearest odd integer to the defined Y1; rounding enclosed",
            "quantifiers": "Only the listed finite even N",
            "experiments": experiments,
            "finite_tests_prove_uniform_bound": False,
            "experiments_all_below_0338": all(
                e["finite_0338_bound_holds"] for e in experiments),
            "sample_maximum_upper_normalized_excess": str(max(
                Decimal(e["normalized_excess"]["upper"]) for e in experiments)),
            "sample_maximum_N": max(experiments, key=lambda e:
                Decimal(e["normalized_excess"]["upper"]))["N"],
        }
        write_json("results/frontier_centered_experiments.json", finite)
    reduction = {
        "date": "2026-10-06", "checkpoint": 9,
        "large_square_bound": "4*H/ceil(N^(1/4))+(10/3)*B^(1/3)",
        "large_square_bound_scope": "Any positive integer interval [A,B], H=B-A+1",
        "short_repeated_factor_error": "O(N^(3/4))=o(u), uniformly for every even N",
        "short_rough_degree_maximum": 7,
        "degree_maximum_scope": "Every even N>=18 on the actual J_N",
        "factorial_kernel": "(P_b^2-P_kappa^2)/2! + sum_(j=3)^7 P_b^j/j!",
        "kernel_interpretation": "Coefficient sums with product restricted to the window",
        "reference_degree_eight_normalized_bound": "O(N*epsilon1^7)=o(u)",
        "epsilon1": "Y1/(2*N^2)",
        "centered_kernel_reduction": "R095(J)-(Y/Y1)*R095(B)=DeltaK+o(u)",
        "one_sided_centered_kernel_reduction": "R095(J)-(Y/Y1)*R095(B)<=DeltaK+O(N^(3/4)); the nonnegative reference correction is subtracted",
        "general_proof": "RESTRICTED_FRONTIER_NOTE.md",
        "direct_tuple_fixtures": tuple_checks,
        "parity_reduction": "Frontier signed kernel has degree signs (-1)^j; absolute correction bounded by the nonnegative count correction",
        "wave_reweighting_identity": "Any nonnegative per-pair r weights summing to one preserve both row count and lambda(product)",
        "sharp_endpoint_rounding_error": "O(Y/Y1)=o(u)",
        "mellin_tail_height": "T=x^2",
        "per_box_perron_tail": "O_j(x*log(x)/T)=O_j(log(x)/x)",
        "low_frequency_cutoff": "T0=exp((log x)^(1/3))",
        "low_frequency_per_box": "O_j(Y*exp(-3*(log x)^(1/3)))",
        "necessary_per_box_log_saving_if_used": "A>8 for O((log x)^7) boxes",
        "high_frequency_signed_integral_estimate_proved": False,
        "positive_prime_mass_credited": 0, "certified_K": 0,
        "H_theta_proved": False,
        "whole_frontier_target_proved": False,
    }
    write_json("results/restricted_frontier_reduction.json", reduction)
    state_path = ROOT / "results/campaign_state.json"
    state = json.loads(state_path.read_text())
    state.update({
        "checkpoint": 9, "latest_investigation_note": "RESTRICTED_FRONTIER_NOTE.md",
        "restricted_frontier_reduction": "results/restricted_frontier_reduction.json",
        "frontier_prime_product_mass": "results/frontier_prime_product_mass.json",
        "frontier_four_factor_certificate": "results/frontier_four_factor_certificate.json",
        "actual_rough_degree_maximum": 7,
        "short_repeated_prime_error": "O(N^(3/4)) uniformly on actual J_N",
        "next_gate": "Prove the .338u one-sided centered comparison for the actual two-, three- and four-to-seven-prime factorial kernel",
        "lower_bound_status": "K=0; actual frontier reduced to seven-degree prime products with controlled o(u) error; high-frequency comparison unproved",
        "numerical_bounds_changed_in_checkpoint9": "New component reference enclosures and finite experiments only; historical analytic ledger unchanged",
        "new_actual_arithmetic_reduction_admitted": True,
        "new_terminal_comparison_estimate_admitted": False,
    })
    if not args.skip_experiments:
        state["frontier_centered_experiments"] = "results/frontier_centered_experiments.json"
    state["milestones"]["3"] = (
        "Exact backbone sharpened: actual rough degree<=7; factorial prime-product "
        "frontier reduction with uniform O(N^(3/4)) correction; adaptive design pending")
    state["milestones"]["4"] = (
        "Ross bridges and all-grouping printed four-factor endpoint certificate "
        "supplied; full inventory incomplete")
    state["milestones"]["6"] = (
        "Actual-support squareful error and parity checks supplied; finite centered "
        "experiments recorded; uniform arithmetic comparison still needed")
    write_json("results/campaign_state.json", state)
    print(json.dumps({
        "direct_tuple_fixtures_passed": len(tuple_checks),
        "higher_reference_mass": masses["frontier_groups"]["four_to_seven_prime_frontier"],
        "four_factor_endpoint_cases_excluded": 4,
        "finite_centered_experiments": len(experiments),
        "new_short_interval_power_error_proved": "O(N^(3/4))",
        "certified_K": 0,
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
