#!/usr/bin/env python3
"""Checkpoint 30: a direct lower kernel for the coupled degree pool.

The uniform proofs are in COUPLED_DEGREE_KERNEL_NOTE.md. Exact fixtures
check convolution multiplicities, the polynomial correction, original
marks, and a continuous obstruction to one particular RS comparison
mapping. The sharp actual centered comparison remains unproved.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from decimal import Decimal
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path

from coupled_one_sided import actual_mark, segmented_factors
from joint_remainder import vaughan_vectors
from structured_frontier import I
from two_free_prime_decomposition import constraint, vertices

ROOT = Path(__file__).resolve().parents[1]
LOW, HIGH = F(2, 5), F(43, 100)
LEVEL, KAPPA = F(1249, 1000), F(1, 1000)
ORDER, EPSILON = 5, F(5, 32)
REF_CHARGE, SHORT_CHARGE, TOTAL = F(1, 10**6), F(33, 10**6), F(1, 10000)
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
    p = ROOT / "results/checkpoint29_preservation_manifest.json"
    old = json.loads(p.read_text())
    demand(old["checkpoint"] == 29, "Frozen checkpoint29 identity")
    count = 0
    for record in old["files"]:
        if record["path"] in MUTABLE:
            continue
        data = (ROOT / record["path"]).read_bytes()
        demand(len(data) == record["size_bytes"] and
               hashlib.sha256(data).hexdigest() == record["sha256"],
               "Preserved " + record["path"])
        count += 1
    demand(count == 291, "All historical nonmutable records")
    return {"checkpoint29_nonmutable_records_verified": count,
            "checkpoint29_manifest_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "negative_frontier_ledger_sha256": hashlib.sha256(
                (ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()}


def convolution_polynomial(factors, cutoff):
    """Direct ordered three-prime-power composition of an integer.

    Keys are formal degree-three monomials in log(prime); multiplicities
    count all positive exponent compositions, not a squarefree proxy.
    """
    ps = sorted(factors)
    if not ps or ps[0] < cutoff:
        return {}
    result = defaultdict(int)
    for slots in product(ps, repeat=3):
        multiplicities = Counter(slots)
        if set(multiplicities) != set(ps):
            continue
        coefficient = 1
        for p, k in multiplicities.items():
            a = factors[p]
            coefficient *= comb(a - 1, k - 1) if a >= k else 0
        result[tuple(sorted(slots))] += coefficient
    return {m: c for m, c in result.items() if c}


def closed_polynomial(factors, cutoff):
    ps = sorted(factors)
    if not ps or ps[0] < cutoff:
        return {}
    if len(ps) == 1:
        p = ps[0]
        c = comb(factors[p] - 1, 2) if factors[p] >= 3 else 0
        return {(p, p, p): c} if c else {}
    if len(ps) == 2:
        p, q = ps
        values = {(p, p, q): 3 * (factors[p] - 1),
                  (p, q, q): 3 * (factors[q] - 1)}
        return {m: c for m, c in values.items() if c}
    if len(ps) == 3:
        return {tuple(ps): 6}
    return {}


def exact_convolution_checks():
    rows, below_cutoff, positive = 0, 0, 0
    for distinct in range(1, 5):
        ps = (2, 3, 5, 7)[:distinct]
        # Positive rational substitutions check formal algebra exactly;
        # these are not asserted to be literal logarithms of the primes.
        logs = {p: F(p + 1, p) for p in ps}
        for exponents in product(range(1, 7), repeat=distinct):
            factors = dict(zip(ps, exponents))
            for cutoff in (2, 3):
                direct = convolution_polynomial(factors, cutoff)
                closed = closed_polynomial(factors, cutoff)
                demand(direct == closed, "Exact prime-power convolution multiplicities")
                denominator = sum((a * logs[p] for p, a in factors.items()), F(0))
                numerator = sum((c * logs[m[0]] * logs[m[1]] * logs[m[2]]
                                 for m, c in direct.items()), F(0))
                nu = F(9, 2) * numerator / denominator**3
                demand(0 <= nu <= 1, "Kernel normalization on exact formal fixtures")
                lifted = 1 - (1 - nu)**ORDER
                expanded = sum(((-1)**(j + 1) * comb(ORDER, j) * nu**j
                                for j in range(1, ORDER + 1)), F(0))
                demand(lifted == expanded and 0 <= nu <= lifted <= 1,
                       "Exact polynomial lift")
                pool = min(ps) >= cutoff and sum(exponents) >= 3
                demand(lifted <= int(pool), "Exact coupled degree support")
                rows += 1
                below_cutoff += min(ps) < cutoff
                positive += lifted > 0
    return {"formal_factor_and_cutoff_rows": rows,
            "below_cutoff_zero_rows": below_cutoff, "positive_kernel_rows": positive,
            "formal_log_multiplicities_checked": True,
            "positive_rational_log_substitutions_not_literal_prime_logs": True,
            "all_distinct_and_repeated_cases_retained": True}


def coefficients():
    old = json.loads((ROOT / "results/one_prime_degree_pool_reference.json").read_text())
    reference = read_interval(old["concrete_coupled_test_band_reference_smoothed"])
    demand(reference.hi < F(1251, 125000), "Coarse actual centered lower coefficient rounded outward")
    upper = (1 + KAPPA) * 4 / LEVEL * I.point(
        HIGH * (LEVEL - LOW) / (LOW * (LEVEL - HIGH))).log()
    demand(upper.hi < F(348, 1000), "Upward-rounded admitted rough upper band coefficient")
    rows = []
    for k in range(1, ORDER + 1):
        error = EPSILON**k
        ref_loss, short_loss = error * reference, error * upper
        rows.append({"order": k, "relative_defect": str(error),
                     "reference_defect_upper_enclosure": ref_loss.record(),
                     "short_defect_upper_enclosure": short_loss.record()})
    selected = rows[-1]
    demand(F(selected["reference_defect_upper_enclosure"]["upper"]) < REF_CHARGE,
           "Fixed fifth-degree reference charge certified")
    demand(F(selected["short_defect_upper_enclosure"]["upper"]) < SHORT_CHARGE,
           "Fixed fifth-degree uniform short defect certified")
    demand(F(rows[-2]["short_defect_upper_enclosure"]["lower"]) > TOTAL,
           "Fifth degree is the first order passing this uniform short-defect envelope")
    minimum_seed = F(27, 32)
    lifted_floor = 1 - (1 - minimum_seed)**ORDER
    return {"band": [str(LOW), str(HIGH)], "lift_order": ORDER,
            "normalizing_multiplier": "9/2",
            "squarefree_triple_seed_minimum": str(minimum_seed),
            "relative_seed_defect_maximum": str(EPSILON),
            "relative_lifted_defect_maximum": str(EPSILON**ORDER),
            "squarefree_triple_lifted_weight_floor": str(lifted_floor),
            "polynomial_coefficients_ascending": [(-1)**(j + 1) * comb(ORDER, j)
                                                    for j in range(1, ORDER + 1)],
            "preserved_actual_pool_reference": reference.record(),
            "rough_band_upper_formula": "(1+kappa)*(4/B)*log(b*(B-a)/(a*(B-b)))",
            "rough_band_upper_enclosure": upper.record(),
            "rough_band_upper_upward_coefficient": ".348",
            "orders": rows, "selected_reference_loss_charge": str(REF_CHARGE),
            "selected_uniform_short_defect_charge": str(SHORT_CHARGE),
            "actual_reference_loss_budget_passed": True,
            "centered_pool_minus_kernel_lower_coefficient": str(-REF_CHARGE),
            "centered_pool_minus_kernel_upper_coefficient": str(SHORT_CHARGE),
            "comparison_plus_remaining_budget": str(TOTAL - REF_CHARGE),
            "coarse_actual_centered_kernel_lower_coefficient": str(-F(1251, 125000)),
            "coarse_actual_centered_kernel_upper_coefficient": "87/250",
            "comparison_still_uses_actual_normalized_long_count": True,
            "reference_enclosure_width_discarded_as_o_u": False,
            "sharp_centered_kernel_lower_bound_proved": False}


def source_facets():
    # Physical quartet exponents: a<=b<=c<=d, sum=2, a in [.40,.43].
    cs = [constraint((-1, 0, 0), -LOW), constraint((1, 0, 0), HIGH),
          constraint((1, -1, 0), 0), constraint((0, 1, -1), 0),
          constraint((1, 1, 2), 2)]
    vs = vertices(cs)
    demand(len(vs) == 6, "Full coupled band has six rational vertices")
    physical, mapping, small_mapping = [], [], []
    for a, b, c in vs:
        d = 2 - a - b - c
        q = (a, b, c, d)
        seed = 27 * b * c * d / (2 - a)**3
        demand(F(27, 32) <= seed <= 1, "Vertex seed range")
        physical.append({"exponents": list(map(str, q)), "squarefree_seed": str(seed),
                         "best_optimistic_RS_first_margin": str(c + 2 * d - 2),
                         "continuous_margin_ceiling": str(2 - 5 * a)})
        for standalone in range(4):
            for eliminated in range(4):
                if standalone == eliminated:
                    continue
                margin = q[standalone] + 2 * q[eliminated] - 2
                demand(margin <= c + 2 * d - 2 <= 2 - 5 * a <= 0,
                       "Every one-free-after-elimination mapping fails strict first facet")
                mapping.append({"exponents": list(map(str, q)),
                                "standalone_slot": standalone, "eliminated_slot": eliminated,
                                "first_margin": str(margin)})
                for hs, he in product((F(0), F(1, 500)), repeat=2):
                    free = q[standalone] - hs
                    sigma = 2 - q[eliminated] + he
                    first = free - 2 * sigma + 2
                    errors = ((sigma + 1)/2 - free/4, sigma - free/2, 2*sigma-2)
                    demand(first == margin - hs - 2*he and first <= 0,
                           "Small TypeI products cannot improve the source facet")
                    demand(errors[0] >= 1 and errors[1] >= 1,
                           "First two direct RS error powers have no strict saving")
                    small_mapping.append({"first_margin": str(first),
                                          "error_exponents": list(map(str, errors))})
    # Also test Theorem3 per external Fourier frequency with the three
    # remaining factors free (one parameter and two inner variables).
    # The required top height has phase exponent chi>=1. For a fixed
    # small-product row, its first two source terms have powers
    # (3*S_free+chi-M_free)/4 and (3*S_free+chi-N_free)/4.
    three_free_count, three_free_minimum = 0, None
    for a, b, c in vs:
        q = (a, b, c, 2-a-b-c)
        for eliminated in range(4):
            remaining = [i for i in range(4) if i != eliminated]
            for parameter in remaining:
                inner = [i for i in remaining if i != parameter]
                for small in product((F(0), F(1, 500)), repeat=3):
                    free = {i:q[i]-h for i,h in zip(remaining,small)}
                    sf, cf = sum(free.values()), free[parameter]
                    errors = [(3*sf+1-free[i])/4 for i in inner]
                    worst = max(errors)
                    lower = (5*sf+cf+2)/8
                    demand(worst >= lower >= F(523,500) > 1,
                           "Per-frequency three-free Theorem3 also has no strict saving")
                    three_free_minimum = worst if three_free_minimum is None else min(three_free_minimum,worst)
                    three_free_count += 1
    demand(three_free_count == 576 and three_free_minimum == F(523,500),
           "Exact three-free critical-frequency source certificate")
    upper_rows = []
    for a in (LOW, HIGH):
        beta = LEVEL - a
        demand(LEVEL < F(5, 4) and a < 1 and beta > 0 and 2*a + beta < 2,
               "Rough upper-band WF transfer remains admitted")
        demand(1 < beta/a < 3, "Primitive upper function is in its explicit branch")
        upper_rows.append({"outer_exponent": str(a), "beta": str(beta),
                           "s": str(beta/a), "full_level_reserve": "1/1000",
                           "RS_extra_margin": str(2 - 2*a - beta)})
    return {"coordinate_order": ["a", "b", "c"],
            "constraints": [{"A": list(map(str, row)), "bound": str(bound)}
                            for row, bound in cs],
            "physical_vertices": physical, "physical_vertex_count": len(vs),
            "optimistic_mapping_rows": mapping, "optimistic_mapping_count": len(mapping),
            "small_product_mapping_count": len(small_mapping),
            "small_product_mapping_summary": {
                "largest_first_margin": str(max(F(v["first_margin"]) for v in small_mapping)),
                "smallest_first_error_exponent": str(min(F(v["error_exponents"][0]) for v in small_mapping)),
                "smallest_second_error_exponent": str(min(F(v["error_exponents"][1]) for v in small_mapping))},
            "continuous_RS_first_margin_ceiling": "c+2d-2=2-2a-2b-c<=2-5a<=0",
            "mapping_scope": "Eliminate one free factor; retain one different original factor as a free standalone variable; collapse remaining factors in the arbitrary other slot",
            "standalone_product_of_two_free_factors_declared_unit_weight": False,
            "simultaneous_three_free_variable_methods_excluded": False,
            "source_power_saving_for_actual_weighted_kernel_proved": False,
            "three_free_per_frequency_Theorem3": {
                "mapping_rows": three_free_count,
                "critical_phase_exponent": "1",
                "minimum_maximum_first_two_error_exponents": str(three_free_minimum),
                "continuous_lower_bound": "max(E1,E2)>=(5*S_free+C_free+2*chi)/8>=(16*a-16*.002+2)/8>=523/500",
                "mapping_rejected": True,
                "joint_frequency_and_product_methods_excluded": False},
            "rough_upper_band_source_vertices": upper_rows,
            "rough_upper_band_source_admitted": True}


def interval_power(value, exponent):
    result = I.point(1)
    for _ in range(exponent):
        result = result * value
    return result


def actual_kernel_interval(factors, cutoff, cache):
    polynomial = closed_polynomial(factors, cutoff)
    if not polynomial:
        return I.point(0)
    for p in factors:
        if p not in cache:
            cache[p] = I.point(p).log()
    logarithm = sum((a * cache[p] for p, a in factors.items()), I.point(0))
    numerator = sum((c * cache[m[0]] * cache[m[1]] * cache[m[2]]
                     for m, c in polynomial.items()), I.point(0))
    nu = F(9, 2) * numerator / interval_power(logarithm, 3)
    # Intersect with the independent globally proved range [0,1].
    demand(nu.hi >= 0 and nu.lo <= 1, "Computed kernel is consistent with proved range")
    nu = I(max(Decimal(0), nu.lo), min(Decimal(1), nu.hi))
    return 1 - interval_power(1 - nu, ORDER)


def arithmetic_checks():
    cases, witnesses, sites = [], [], 0
    band_cache, log_cache = {}, {}
    for N in (65536, 160000):
        lo, hi = N*N - N - 1, N*N + N + 1
        counter = Counter()
        mass = I.point(0)
        band_cache.clear()
        for offset, fs in enumerate(segmented_factors(lo, hi)):
            n = lo + offset
            rough = fs[0]**4 >= N
            mark = actual_mark(N, n, fs)
            complement = int(rough) * (1 - min(F(1), mark))
            pool, kernel = 0, I.point(0)
            for p in set(fs):
                if p not in band_cache:
                    band_cache[p] = p**5 >= N**2 and p**100 <= N**43
                if not band_cache[p]:
                    continue
                mf = Counter(fs)
                mf[p] -= 1
                if mf[p] == 0:
                    del mf[p]
                good = bool(mf) and min(mf) >= p and sum(mf.values()) >= 3
                w = actual_kernel_interval(mf, p, log_cache)
                demand(w.lo >= 0 and w.hi <= int(good), "Actual prime-log kernel lower bound")
                pool += good
                kernel = kernel + w
            demand(pool <= complement and kernel.hi <= pool,
                   "Original canonical complement contains the coupled lower kernel")
            counter["sites"] += 1
            counter["coupled_band_pool_sites"] += pool
            if pool:
                counter["repeated_band_pool_sites"] += len(set(fs)) < len(fs)
                counter["degree_five_band_sites"] += len(fs) == 5
                if len(fs) == 4 and len(set(fs)) == 4:
                    counter["squarefree_four_prime_band_sites"] += 1
            box = (len(fs) == 4 and len(set(fs)) == 4 and
                   N**40 <= fs[0]**100 <= N**43 and
                   N**45 <= fs[1]**100 <= N**48 and
                   N**50 <= fs[2]**100 <= N**53)
            if box:
                demand(pool == 1 and kernel.lo > 0, "Old omitted box receives positive kernel weight")
                counter["old_box_sites_with_positive_kernel"] += 1
                if len(witnesses) < 3:
                    witnesses.append({"N": N, "n": n, "factors": fs,
                                      "kernel_interval": kernel.record()})
            mass = mass + kernel
        cases.append({"N": N, **dict(counter), "kernel_mass_on_full_padding": mass.record(),
                      "original_cutoffs_and_half_diagonal_unchanged": True})
        sites += counter["sites"]
    demand(sites == 451078 and len(witnesses) == 3, "Full actual padding fixtures")
    return {"cases": cases, "short_padding_sites_checked": sites,
            "old_box_positive_kernel_witnesses": witnesses,
            "actual_prime_log_weights_evaluated_outward": True,
            "fixtures_do_not_prove_centered_short_comparison": True}


def multiply_polynomials(first, second):
    result = defaultdict(int)
    for a, c in first.items():
        for b, d in second.items():
            result[tuple(sorted(a+b))] += c*d
    return {m: c for m, c in result.items() if c}


def tensor(vectors):
    value = {(): 1}
    for vector in vectors:
        value = multiply_polynomials(value, {(p,): c for p, c in vector.items() if c})
    return value


def factor_integer(n):
    result, p = {}, 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def tensor_identity_checks():
    rows, composite = 0, 0
    for U in (2, 3, 5):
        for j in range(24):
            integers = tuple(U+1+(a*j+b) % 24 for a, b in ((1,0),(5,1),(7,2),(11,3)))
            records = [vaughan_vectors(factor_integer(n), U, U) for n in integers]
            full = defaultdict(int)
            for choice in product(range(3), repeat=4):
                part = tensor([records[k][choice[k]] for k in range(4)])
                for monomial, coefficient in part.items():
                    full[monomial] += coefficient
            full = {m: c for m, c in full.items() if c}
            target = tensor([record[3] for record in records])
            demand(full == target, "All 81 signed tensor Vaughan terms recombine exactly")
            rows += 1
            composite += any(len(factor_integer(n)) > 1 for n in integers)
    return {"four_slot_formal_log_fixtures": rows,
            "fixtures_with_composite_slots": composite,
            "signed_terms_per_log_moment": 3**4,
            "log_moment_count": ORDER, "retained_signed_term_count": ORDER*3**4,
            "grouped_TypeI_TypeII_patterns_per_moment": 2**4,
            "no_prime_mask_retained_on_expanded_free_integer_slots": True,
            "all_TypeII_and_all_TypeI_terms_kept": True,
            "sharp_405_term_centered_estimate_proved": False}


def main():
    preserved = preservation()
    coefficient = coefficients()
    facets = source_facets()
    convolution = exact_convolution_checks()
    arithmetic = arithmetic_checks()
    identities = tensor_identity_checks()
    checks = {"preservation": preserved, "exact_convolution": convolution,
              "arithmetic": arithmetic, "exact_tensor_identity": identities,
              "source_mapping_vertices_checked": facets["physical_vertex_count"],
              "source_mapping_rows_checked": facets["small_product_mapping_count"],
              "three_free_critical_source_rows_checked": facets["three_free_per_frequency_Theorem3"]["mapping_rows"],
              "all_exact_checks_passed": True, "reference_test_passed": True,
              "pointwise_test_passed": True, "actual_comparison_source_admitted": False,
              "sharp_original_target_proved": False}
    kernel = {"date": "2026-10-12", "checkpoint": 30,
              "definition": "lambda_p(v)=Lambda(v)*1_(Pminus(v)>=p); nu_p(m)=(9/2)*(lambda_p*lambda_p*lambda_p)(m)/log(m)^3; w_p(m)=1-(1-nu_p(m))^5",
              "lift_order": ORDER, "band": [str(LOW), str(HIGH)],
              "global_nu_range_proved": ["0", "1"],
              "automatic_rough_degree_support_proved": True,
              "pointwise_lower_weight_proved": True,
              "reference_loss_upper_coefficient": str(REF_CHARGE),
              "uniform_short_defect_upper_coefficient": str(SHORT_CHARGE),
              "uniform_centered_pool_minus_kernel_bounds_proved": True,
              "actual_centered_kernel_lower_comparison_proved": False,
              "centered_comparison_flag_scope": "Required .000099 budget; coarse actual lower coefficient -.010008 is proved",
              "coarse_actual_centered_kernel_lower_coefficient": "-1251/125000",
              "arithmetic_reference_candidate_passed": True,
              "fully_admitted_comparison_weight": False,
              "tested_two_free_RS_mapping_rejected": True,
              "tested_three_free_per_frequency_RS_mapping_rejected": True,
              "all_multilinear_methods_rejected": False,
              "remaining_interface": "Delta_W5>=-(eta_W+o(1))*u, with eta_W+eta_rest<=99/1000000; keep all 405 signed Vaughan terms",
              "new_actual_count_was_replaced_by_its_reference_main": False,
              "original_spectral_budget": "1587/200000", "original_smoothing_budget": "613/200000",
              "original_total_coefficient": "11/1000", "original_global_allowance_changed": False,
              "new_fixed_power_or_frequency_sector_discarded": False,
              "conditional_kernel_transfer_charge": "1/1000000",
              "fixed_least_prime_xi_if_used": "Checkpoint22 (23), retained",
              "fixed_frequency_tail_if_used": "21147/L, retained",
              "terminal_0011_estimate_proved": False, "H_theta_proved": False,
              "certified_K": 0}
    for name, value in (("coupled_degree_kernel.json", kernel),
                        ("coupled_degree_kernel_coefficients.json", coefficient),
                        ("coupled_degree_kernel_facets.json", facets),
                        ("coupled_degree_kernel_checks.json", checks)):
        save(name, value)
    print(json.dumps({"all_exact_checks_passed": True,
                      "preserved_records": preserved["checkpoint29_nonmutable_records_verified"],
                      "short_padding_sites_checked": arithmetic["short_padding_sites_checked"],
                      "formal_convolution_rows": convolution["formal_factor_and_cutoff_rows"],
                      "source_mapping_rows": facets["small_product_mapping_count"] + facets["three_free_per_frequency_Theorem3"]["mapping_rows"],
                      "reference_loss_charge": str(REF_CHARGE),
                      "short_defect_charge": str(SHORT_CHARGE),
                      "pointwise_and_reference_tests_passed": True,
                      "actual_centered_comparison_proved": False,
                      "sharp_original_target_proved": False}))


if __name__ == "__main__":
    main()
