#!/usr/bin/env python3
"""Checkpoint 31: exact normalization and retained short comparison.

Uniform proofs are in FOUR_FACTOR_NORMALIZATION_NOTE.md. Finite checks
verify Jacobian-weighted small-coefficient collapse, the full signed
Vaughan tensor on composite slots, the fixed coarea geometry, and the
budget. They do not prove the remaining short lattice/Type-II estimate.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOW, HIGH, DELTA, KAPPA = F(2, 5), F(43, 100), F(1, 1000), F(1, 1000)
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}


def demand(ok, message):
    if not ok:
        raise AssertionError(message)


def save(name, data):
    (ROOT / "results" / name).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def preservation():
    p = ROOT / "results/checkpoint30_preservation_manifest.json"
    old = json.loads(p.read_text())
    demand(old["checkpoint"] == 30, "Frozen checkpoint 30 identity")
    count = 0
    for record in old["files"]:
        if record["path"] in MUTABLE:
            continue
        raw = (ROOT / record["path"]).read_bytes()
        demand(len(raw) == record["size_bytes"] and
               hashlib.sha256(raw).hexdigest() == record["sha256"],
               "Preserved " + record["path"])
        count += 1
    demand(count == 299, "All 299 nonmutable checkpoint 30 records")
    return {"checkpoint30_nonmutable_records_verified": count,
            "checkpoint30_manifest_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "negative_frontier_ledger_sha256": hashlib.sha256(
                (ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()}


@lru_cache(maxsize=None)
def factors(n):
    answer, p = [], 2
    while p*p <= n:
        exponent = 0
        while n % p == 0:
            exponent += 1
            n //= p
        if exponent:
            answer.append((p, exponent))
        p += 1
    if n > 1:
        answer.append((n, 1))
    return tuple(answer)


def mobius(n):
    fs = factors(n)
    return 0 if any(a > 1 for _, a in fs) else (-1)**len(fs)


def formal_prime_log(p):
    # Positive rational substitutions preserve log multiplicities. They
    # are not claimed to equal the literal logarithms of the primes.
    return F(p + 1, p)


@lru_cache(maxsize=None)
def formal_log(n):
    return sum((a*formal_prime_log(p) for p, a in factors(n)), F(0))


def mangoldt(n):
    fs = factors(n)
    return formal_prime_log(fs[0][0]) if len(fs) == 1 else F(0)


def mul(values):
    value = F(1)
    for v in values:
        value *= v
    return value


def phi(v):
    return 1 - (1-v)**5


@lru_cache(maxsize=None)
def vaughan(n, U):
    divisors = [d for d in range(1, n+1) if n % d == 0]
    first = sum((mobius(d)*formal_log(n//d)
                 for d in divisors if d <= U), F(0))
    second = -sum((mobius(d)*mangoldt(b)
                   for d in range(1, U+1) for b in range(1, U+1)
                   if n % (d*b) == 0), F(0))
    third = F(0)
    for m in divisors:
        b = n//m
        if m > U and b > U:
            beta = -sum(mobius(d) for d in range(1, U+1) if m % d == 0)
            third += beta*mangoldt(b)
    target = mangoldt(n)
    demand(first + second + third == target, "Complete scalar Vaughan identity")
    return first, second, third, target


def density_checks():
    one_slot, quartets = 0, 0
    rows = []
    for U in (1, 2, 3, 5, 9, 12, 24):
        m = sum((F(mobius(d), d) for d in range(1, U+1)), F(0))
        ell = sum((F(mobius(d), d)*formal_log(d)
                   for d in range(1, U+1)), F(0))
        s = sum((mangoldt(b)/b for b in range(1, U+1)), F(0))
        branches = []
        for physical_log in (F(4), F(9, 2), F(5), F(13, 2)):
            first = sum((F(mobius(d), d)*(physical_log-formal_log(d))
                         for d in range(1, U+1)), F(0))
            second = -sum((F(mobius(d), d)*mangoldt(b)/b
                           for d in range(1, U+1) for b in range(1, U+1)), F(0))
            demand(first+second == m*(physical_log-s)-ell,
                   "Exact physical-variable Jacobian density")
            branches.append((first, second))
            one_slot += 1
        expanded = sum((mul(branches[i][a] for i, a in enumerate(choice))
                        for choice in product(range(2), repeat=4)), F(0))
        closed = mul(m*(v-s)-ell for v in (F(4), F(9, 2), F(5), F(13, 2)))
        demand(expanded == closed, "All 16 continuum branches collapse exactly")
        quartets += 1
        rows.append({"U": U, "m_U": str(m), "formal_l_U": str(ell),
                     "formal_s_U": str(s), "continuum_product": str(closed)})
    return {"exact_one_slot_density_rows": one_slot,
            "exact_four_slot_continuum_expansions": quartets,
            "all_1_over_d_and_1_over_db_Jacobians_kept": True,
            "rational_substitutions_are_formal_logs_not_literal_prime_logs": True,
            "finite_rows_do_not_verify_asymptotic_density_one": True,
            "rows": rows}


def tensor_checks():
    scalar, quartet, composite, zero_targets = 0, 0, 0, 0
    negative, positive, witnesses = 0, 0, []
    I_patterns = [c for c in product(range(3), repeat=4) if all(a < 2 for a in c)]
    II_patterns = [c for c in product(range(3), repeat=4) if any(a == 2 for a in c)]
    demand(len(I_patterns) == 16 and len(II_patterns) == 65, "80/325 grouped accounting")
    for U in (2, 3, 5, 9):
        for n in range(U+1, U+181):
            vaughan(n, U)
            scalar += 1
        for j in range(32):
            ns = tuple(U+1+(a*j+b) % 72 for a, b in ((1, 0), (5, 1), (7, 2), (11, 3)))
            vs = [vaughan(n, U) for n in ns]
            all_I = sum((mul(vs[i][a] for i, a in enumerate(c))
                         for c in I_patterns), F(0))
            all_II = sum((mul(vs[i][a] for i, a in enumerate(c))
                          for c in II_patterns), F(0))
            I_product = mul(v[0]+v[1] for v in vs)
            Lambda_product = mul(v[3] for v in vs)
            demand(all_I == I_product and all_I+all_II == Lambda_product,
                   "All 81 terms, including composite cancellations")
            logs = tuple(formal_log(n) for n in ns)
            frozen_denominator = sum(logs[1:])+F(1, 8)
            weight = F(0)
            for moment in range(1, 6):
                g = mul(v**(moment-1) for v in logs[1:]) / (logs[0]*frozen_denominator**(3*moment))
                coefficient = F((-1)**(moment+1)*comb(5, moment)*27**moment, 6)
                demand(coefficient*g*(I_product+all_II) == coefficient*g*Lambda_product,
                       "Common physical weights do not drop Type-II terms")
                weight += coefficient*g
            seed = 27*mul(logs[1:])/frozen_denominator**3
            demand(weight == phi(seed)/(6*mul(logs)), "Exact five-moment weight recombination")
            demand(weight*(I_product+all_II) == weight*Lambda_product,
                   "Complete 405-term family retained")
            negative += all_II < 0
            positive += all_II > 0
            if all_II != 0 and (not witnesses or (all_II < 0) != (F(witnesses[0]["signed_II_aggregate"]) < 0)):
                if len(witnesses) < 2:
                    witnesses.append({"U": U, "slots": list(ns),
                                      "all_I_product": str(I_product),
                                      "signed_II_aggregate": str(all_II),
                                      "Lambda_product": str(Lambda_product)})
            composite += any(mangoldt(n) == 0 for n in ns)
            zero_targets += Lambda_product == 0
            quartet += 1
    demand(negative > 0, "At least one negative Type-II aggregate: no positivity assumption")
    return {"exact_scalar_Vaughan_rows": scalar,
            "exact_four_slot_tensor_rows": quartet,
            "quartets_with_nonprimepower_slot": composite,
            "zero_full_detector_product_rows": zero_targets,
            "all_I_patterns_per_moment": 16, "with_II_patterns_per_moment": 65,
            "all_I_signed_subterms": 80, "with_II_signed_subterms": 325,
            "total_signed_subterms": 405,
            "negative_II_aggregate_fixtures": negative,
            "positive_II_aggregate_fixtures": positive,
            "formal_signed_witnesses": witnesses,
            "does_not_prove_short_comparison": True}


def geometry_checks():
    rows = 0
    for alpha in (LOW, F(41, 100), F(42, 100), HIGH):
        for tau in (F(199, 100), F(2), F(201, 100)):
            R = tau-4*alpha
            demand(F(27, 100) <= R <= F(41, 100), "Fixed simplex is nondegenerate")
            for a in range(9):
                for b in range(9-a):
                    s, t = F(a, 8), F(b, 8)
                    beta, gamma, omega = alpha+R*s, alpha+R*t, alpha+R*(1-s-t)
                    demand(min(beta, gamma, omega) >= alpha and
                           alpha+beta+gamma+omega == tau, "Exact original ordering gates")
                    demand(max(beta, gamma, omega) <= F(81, 100), "Compact exponent ceiling")
                    nu = 27*beta*gamma*omega/(2-alpha)**3
                    demand(0 < nu <= F(158, 157)**3 < 2, "AM-GM continuum seed bound")
                    base = phi(nu)/(alpha*beta*gamma*omega)
                    for ell in (F(13), F(19)):
                        logs = tuple(ell*v for v in (alpha, beta, gamma, omega))
                        folded = sum(((-1)**(j+1)*comb(5, j)*27**j *
                                      mul(v**(j-1) for v in logs[1:]) /
                                      (logs[0]*(ell*(2-alpha))**(3*j))
                                      for j in range(1, 6)), F(0))
                        demand(folded*ell**3 == base/ell, "Three reciprocal coarea factors")
                    rows += 1
    Q = 27*F(81, 100)**2/F(157, 100)**3
    derivative = (HIGH-LOW)/(2*LOW**4) * (4*F(41, 100)+F(41, 100)**2*(5*Q+2/LOW))
    demand(derivative < 4, "Uniform analytic derivative cap, no quadrature")
    return {"exact_compact_geometry_rows": rows,
            "R_range": ["27/100", "41/100"], "simplex_area": "1/2",
            "physical_exponent_ceiling": "81/100",
            "maximum_continuum_seed_upper": str(F(158, 157)**3),
            "J_derivative_rational_upper": str(derivative),
            "J_derivative_roundup": 4,
            "coarea_density": "J(log_N(t))/(6*log(N))",
            "reference_mass_not_numerically_reestimated": True}


def margin_budget_checks():
    unscaled = 2-LOW+2*DELTA
    normalized = unscaled-1
    margin = 1-normalized
    demand(unscaled == F(801, 500) and normalized == F(301, 500)
           and margin == F(199, 500), "Long lattice exponent and strict margin")
    kernel, rest = F(1, 10**6), F(99, 10**6)
    rough, spectral, smoothing, original = F(7825257, 10**9), F(7935, 10**6), F(3065, 10**6), F(11, 1000)
    demand(kernel+rest == F(1, 10000), "Existing complement budget unchanged")
    total = smoothing+rough+kernel+rest
    reserve = original-total
    demand(reserve == F(9743, 10**9) and spectral-(rough+kernel+rest) == reserve,
           "Original signed spectral and terminal reserve")
    return {"unscaled_lattice_bound_exponent": str(unscaled),
            "normalized_long_lattice_exponent": str(normalized),
            "strict_long_margin_before_rho_and_logs": str(margin),
            "coarse_short_bound_does_not_prove_o_u": unscaled > 1,
            "new_normalization_nonvanishing_charge": "0",
            "retained_kernel_reference_charge": ".000001",
            "eta_W_plus_eta_rest_allowance": ".000099",
            "retained_complement_total_budget": ".0001",
            "conditional_final_coefficient_before_later_xi_or_fixed_tail": str(total),
            "conditional_remaining_xi_and_fixed_tail_reserve": str(reserve),
            "original_spectral_allowance": ".007935",
            "original_final_allowance": ".011",
            "original_least_prime_or_frequency_sector_discarded": False}


def source_audit():
    return {"date": "2026-10-13", "checkpoint": 31,
            "primary_sources": [
                {"authors": "Ethan S. Lee and Nicol Leong", "version": "2208.06141v4",
                 "url": "https://arxiv.org/html/2208.06141v4", "item": "Theorem 1.1",
                 "used_bound": "M(T) << T*exp(-c*sqrt(log(T))) for a fixed c>0",
                 "role": "Harmonic Mobius tails; whole Type-I continuous density",
                 "source_checked": True, "RH_assumed": False},
                {"authors": "Daniel R. Johnston and Andrew Yang", "version": "2204.01980v2",
                 "url": "https://arxiv.org/html/2204.01980v2", "item": "Theorem 1.1",
                 "used_bound": "sum_(v<=T) Lambda(v)=T+O(T*exp(-c*sqrt(log(T)))) after absorbing fixed log powers",
                 "role": "Full detector versus continuum only on normalized original long window",
                 "source_checked": True, "short_square_root_PNT_assumed": False},
                {"authors": "M. Z. Garaev, F. Luca and W. G. Nowak",
                 "url": "https://link.springer.com/article/10.1007/s00013-005-1447-2",
                 "item": "Primary publisher abstract; full article unavailable",
                 "stated_range": "length large compared with sqrt(X)*log(X)",
                 "direct_mapping_accepted": False,
                 "reason": "At X=x/D and length Y/D, the ratio is asymptotic to 1/(sqrt(D)*log(x/D)), uniformly D<=U^8; already tends to zero at D=1",
                 "full_article_finer_statements_excluded": False,
                 "restricted_box_extension_assumed": False}],
            "new_uniform_analytic_results": [
                "exact harmonic all-Type-I density with original gates",
                "centered all-Type-I continuous term o(u)",
                "normalized long all-Type-I lattice error o(u)",
                "normalized long 325-term signed Type-II aggregate o(u)"],
            "required_short_joint_lower_estimate_proved": False,
            "previous_RS_failures_preserved_not_retested": True,
            "other_four_variable_methods_excluded": False}


def main():
    protected = preservation()
    density = density_checks()
    print("Exact physical density/Jacobian collapse checked", flush=True)
    tensors = tensor_checks()
    print("Full signed 80/325 tensor partition checked", flush=True)
    geometry = geometry_checks()
    budgets = margin_budget_checks()
    sources = source_audit()
    checks = {"preservation": protected, "density": density,
              "signed_tensors": tensors, "coarea_geometry": geometry,
              "margin_and_budget": budgets,
              "short_sharp_estimate_proved": False}
    result = {"date": "2026-10-13", "checkpoint": 31,
              "proof_note": "FOUR_FACTOR_NORMALIZATION_NOTE.md",
              "new_exact_interface": "Delta W_N = L_N(psi_Y) + B_N(psi_Y) + o(u)",
              "L_N": "Full all-Type-I integer product sum minus its actual continuous product integral",
              "B_N": "All 325 signed subterms containing at least one Type II",
              "centered_continuous_o_u_proved": True,
              "normalized_long_all_TypeI_lattice_o_u_proved": True,
              "normalized_long_signed_TypeII_aggregate_o_u_proved": True,
              "TypeII_terms_individually_absolute_o_u_asserted": False,
              "remaining_actual_short_input": "L_N(psi_Y)+B_N(psi_Y)>=-(eta_W+o(1))*u",
              "remaining_actual_short_input_proved": False,
              "short_all_TypeI_lattice_o_u_proved": False,
              "new_nonvanishing_normalization_charge": "0",
              "eta_W_plus_eta_rest_allowance": ".000099",
              "kernel_reference_charge_retained": ".000001",
              "complete_full_complement_lower_comparison_proved": False,
              "original_007935_0011_targets_proved": False,
              "K": 0, "milestone7": "deferred",
              "preserved_checkpoint30_nonmutable_records": 299}
    save("four_factor_normalization.json", result)
    save("four_factor_normalization_checks.json", checks)
    save("four_factor_normalization_source_audit.json", sources)
    print(json.dumps({"checkpoint": 31,
                      "protected_records": 299,
                      "scalar_identity_rows": tensors["exact_scalar_Vaughan_rows"],
                      "four_slot_rows": tensors["exact_four_slot_tensor_rows"],
                      "geometry_rows": geometry["exact_compact_geometry_rows"],
                      "normalization_charge": "0",
                      "sharp_short_estimate_proved": False}, indent=2), flush=True)


if __name__ == "__main__":
    main()
