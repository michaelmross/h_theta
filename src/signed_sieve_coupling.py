#!/usr/bin/env python3
"""Checkpoint 22: exact identities for coefficient-preserving signed sifting.

These finite checks certify coefficients, positive terminal errors, source
facet perturbations and gates. The asymptotic theorem is proved in the note,
not inferred from samples. Historical modules and result files are read-only.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import isqrt, prod
from pathlib import Path
import json

from beta_support import factor_table
from cofactor_estimation import beta_from_factors
from delta_grouping import NU, pow_le
from joint_remainder import fi_margins, rs_margins
from ross_geometry_audit import factor_band, primes_up_to
from signed_core_continuation import actual_weights, cleaned

ROOT = Path(__file__).resolve().parents[1]
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}
LEDGER = "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def provenance():
    prior = json.loads((ROOT / "results/checkpoint21_preservation_manifest.json").read_text())
    demand(prior["checkpoint"] == 21 and len(prior["files"]) == 236,
           "Authoritative checkpoint 21 manifest")
    checked = 0
    for rec in prior["files"]:
        if rec["path"] in MUTABLE:
            continue
        raw = (ROOT / rec["path"]).read_bytes()
        demand(len(raw) == rec["size_bytes"] and sha256(raw).hexdigest() == rec["sha256"],
               rec["path"] + " unchanged")
        checked += 1
    demand(checked == 232, "232 historical nonmutable records")
    demand(sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
           == LEDGER, "Frozen analytic ledger")
    return {"checkpoint21_nonmutable_records_verified": checked,
            "negative_frontier_ledger_sha256": LEDGER}


def sieve_data(primes, level, beta):
    """Independent finite combinatorial construction, decreasing prime order.

    1 is included in both coefficient sets. A terminal belongs to one parity
    if its first failure among predicates of that parity occurs at its end.
    """
    ps = tuple(sorted(primes))
    plus, minus, terminal_plus, terminal_minus = {}, {}, {}, {}
    all_products = {}
    for size in range(len(ps) + 1):
        for selected in combinations(ps, size):
            mask = sum(1 << ps.index(p) for p in selected)
            descending = selected[::-1]
            d = prod(selected)
            all_products[mask] = d
            conditions = [prod(descending[:r - 1]) * descending[r - 1] ** (beta + 1) <= level
                          for r in range(1, size + 1)]
            coefficient = (-1) ** size
            if all(conditions[r - 1] for r in range(1, size + 1, 2)):
                plus[mask] = coefficient
            if all(conditions[r - 1] for r in range(2, size + 1, 2)):
                minus[mask] = coefficient
            if size and not conditions[-1] and all(conditions[r - 1]
                    for r in range(size % 2 or 2, size, 2)):
                (terminal_plus if size % 2 else terminal_minus)[mask] = min(selected)
    for weights in (plus, minus):
        demand(weights.get(0) == 1 and all(d <= level for mask, d in all_products.items()
               if mask in weights), "Coefficient level support including lambda_1=1")
    if beta >= 2 and max(ps, default=1) ** 2 <= level:
        demand(all(all_products[mask] <= level for mask in terminal_plus | terminal_minus),
               "Positive terminal products also lie below level")
    return ps, all_products, plus, minus, terminal_plus, terminal_minus


def zeta_transform(weights, k):
    result = [weights.get(mask, 0) for mask in range(1 << k)]
    for bit in range(k):
        for mask in range(1 << k):
            if mask & (1 << bit):
                result[mask] += result[mask ^ (1 << bit)]
    return result


def sieve_identity_fixture(primes, level, beta, u):
    ps, products, plus, minus, tplus, tminus = sieve_data(primes, level, beta)
    vp, vm = (zeta_transform(weights, len(ps)) for weights in (plus, minus))
    model = {mask: F(2 ** mask.bit_count(), d) for mask, d in products.items()}
    v_model = prod((1 - F(2, p) for p in ps), start=F(1))
    totals = {"plus": F(0), "minus": F(0)}
    for name, weights, terminals, orientation in (("plus", plus, tplus, 1),
                                                  ("minus", minus, tminus, -1)):
        summed = sum((coefficient * model[mask] for mask, coefficient in weights.items()), F(0))
        gap = sum((model[mask] * prod((1 - F(2, p) for p in ps if p < q), start=F(1))
                   for mask, q in terminals.items()), F(0))
        demand(summed == v_model + orientation * gap,
               "Exact model Euler-product terminal identity")
        totals[name] = gap
    terminal_checks = repeated_checks = 0
    signed_positive = signed_negative = 0
    small_mu = []
    for divisor, factorization in enumerate(factor_table(u)):
        if divisor:
            mu = 0 if any(exponent > 1 for _, exponent in factorization) else (-1) ** len(factorization)
            small_mu.append((divisor, mu))
    for active in range(1 << len(ps)):
        chi = int(active == 0)
        def terminal_count(terms):
            return sum(mask & active == mask and not any(active & (1 << i)
                       for i, p in enumerate(ps) if p < q) for mask, q in terms.items())
        gp, gm = terminal_count(tplus), terminal_count(tminus)
        demand(vp[active] - chi == gp and chi - vm[active] == gm,
               "Pointwise positive terminal expansion")
        demand(vm[active] <= chi <= vp[active], "Pointwise sieve ordering")
        fs = {p: (2 if i % 2 else 3) for i, p in enumerate(ps) if active & (1 << i)}
        value = prod(p ** exponent for p, exponent in fs.items())
        bet = -sum(mu for divisor, mu in small_mu if value % divisor == 0) if fs else 0
        if fs and len(ps) <= 6:
            demand(bet == beta_from_factors(fs, u), "Independent small-divisor beta agrees with full divisor expansion")
        fval = 2 ** sum(p <= u for p in fs)
        demand(abs(bet) <= fval, "Actual beta bounded by small-prime factor majorant")
        signed_positive += bet > 0
        signed_negative += bet < 0
        for mask, q in (tplus | tminus).items():
            if mask & active != mask:
                continue
            d = products[mask]
            mfs = {p: exponent - int(d % p == 0) for p, exponent in fs.items()}
            fmf = 2 ** sum(p <= u and exponent > 0 for p, exponent in mfs.items())
            demand(fval <= 2 ** mask.bit_count() * fmf,
                   "Terminal factor majorant permits repeated primes")
            repeated_checks += 1
        terminal_checks += 1
    return {"primes": ps, "level": str(level), "beta_sieve": beta,
            "U_for_beta_sign_fixture": u, "prime_divisibility_patterns": terminal_checks,
            "repeated_prime_majorant_checks": repeated_checks,
            "plus_coefficients": len(plus), "minus_coefficients": len(minus),
            "positive_upper_terminals": len(tplus), "positive_lower_terminals": len(tminus),
            "dimension2_upper_model_gap": str(totals['plus']),
            "dimension2_lower_model_gap": str(totals['minus']),
            "positive_beta_patterns": signed_positive, "negative_beta_patterns": signed_negative,
            "support_and_pointwise_identities_passed": True,
            "exponential_asymptotic_bound_inferred_from_fixtures": False}


def phase_margins(total, slot, eta, kappa, engine):
    if engine == "RS":
        return {"T1": slot - (4 * eta + 2 - kappa - 2 * total),
                "T2": total - 3 * eta - slot, "T3": slot - 2 * eta,
                "T4": 2 - kappa - total - eta}
    return {"T1": (8 * total - 7 * eta - 6 + 3 * kappa) / 7 - slot,
            "T2": (6 * total - 5 * eta - 4 + 2 * kappa) / 7 - slot,
            "T3": (5 * total - 5 * eta - 2 + kappa) / 8 - slot,
            "T4": (4 * total - 5 * eta - 2 + kappa) / 5 - slot,
            "T5": slot - eta,
            "T6": (2 - kappa - total - eta) / 2 - slot}


def facet_perturbations():
    old = json.loads((ROOT / "results/delta_grouping_facets.json").read_text())
    tau = min(F(r['minimum_margin']) for r in old['regions'])
    demand(tau == F(1, 10000), "Inherited minimum strict condition margin")
    cap = tau / 16
    records, term_checks = [], 0
    for region in old['regions']:
        minimum = None
        for v in region['vertices']:
            s, delta, slot, eta = map(F, (v['S'], v['delta'], v['standalone_exponent'], v['eta']))
            baseline = phase_margins(s + delta, slot, eta, F(0), region['engine'])
            demand(baseline == {k: F(value) for k, value in v['margins'].items()},
                   "Unperturbed facet reproduces frozen certificate")
            for kappa in (F(0), cap):
                for height_shift in (F(0), kappa):
                    new = phase_margins(s + delta, slot, eta + height_shift,
                                        kappa, region['engine'])
                    for term, margin in new.items():
                        demand(margin >= baseline[term] - 4 * kappa and margin >= 3 * tau / 4,
                               "Continuous slab retains strict source margin")
                        minimum = margin if minimum is None else min(minimum, margin)
                        term_checks += 1
        records.append({"region": region['name'], "engine": region['engine'],
                        "verified_slab_minimum": str(minimum)})
    # Analytic raw term savings are fixed positive multiples of the condition margins.
    rs_factors = [F(1, 4), F(1, 4), F(1, 2), F(1, 2)]
    fi_factors = [F(7, 12), F(7, 8), F(1), F(5, 8), F(1, 2), F(1, 2)]
    demand(min(rs_factors + fi_factors) == F(1, 4), "Minimum raw saving factor")
    bound = F(2) * F(11, 4) * F(1, 31) * F(32, 31) ** 2
    demand(bound < F(4, 11), "beta=32 satisfies sufficient dimension-two fundamental condition")
    return {"frozen_vertices_checked": old['vertex_records'], "facet_term_checks": term_checks,
            "phase_kappa_cap": str(cap), "uniform_slab_margin_lower_bound": str(3 * tau / 4),
            "raw_term_saving_lower_bound_before_transfer_losses": str(3 * tau / 16),
            "continuous_slab_certified_by_affinity_and_Lipschitz_bound": True,
            "final_aggregate_modulus_exponent_numerically_selected": False,
            "final_delta_requirement": "0<delta0<min(tau/32,1/100,c_star/(2(C+1))); c_star,C are fixed transfer constants",
            "dimension_two_beta32_condition_rational_upper_bound": str(bound),
            "regions": records}


def actual_continuation_fixture(n, u, wide=False):
    demand(u ** 4 < n, "Stress U below all actual outer primes")
    width = 3 * n if wide else n
    lo, hi = n * n - width // 2, n * n + width // 2
    bands = factor_band(lo, hi, primes_up_to(isqrt(hi)))
    # Finite stress parameters; these do not assert an asymptotic sieve level.
    ps, products, plus, minus, tplus, tminus = sieve_data((3, 5), 64, 2)
    demand(max(ps) <= u, "Sieve primes belong to beta truncation")
    needed = {2} | {products[mask] for mask in plus if mask}
    needed |= {2 * products[mask] for mask in plus if mask}
    masked = {e: defaultdict(F) for e in needed}
    small, gap, envelope = defaultdict(F), defaultdict(F), defaultdict(F)
    even, marked, comp, other = (defaultdict(F) for _ in range(4))
    counts = defaultdict(int)
    for value, fs in bands.items():
        vec, _, _ = actual_weights(value, fs, n, u)
        if not vec:
            continue
        bet = beta_from_factors(fs, u)
        fval = 2 ** sum(p <= u for p in fs)
        demand(abs(bet) <= fval, "Absolute beta terminal majorant on actual sites")
        chi = int(all(value % p for p in ps))
        nu = sum(coef for mask, coef in plus.items() if value % products[mask] == 0)
        error = nu - chi
        terminal = sum(value % products[mask] == 0 and all(value % p for p in ps if p < q)
                       for mask, q in tplus.items())
        demand(error == terminal and error >= 0, "Actual site positive terminal identity")
        counts['active_sites'] += 1
        counts['positive_signed_sites'] += bet > 0
        counts['negative_signed_sites'] += bet < 0
        for key, coef in vec.items():
            d, b = key
            weighted = bet * coef
            for e in needed:
                if value % e == 0:
                    masked[e][key] += weighted
            if min(fs) <= 5:
                small[key] += weighted
            if value % 2:
                gap[key] += weighted * error
                envelope[key] += fval * coef * error
            else:
                even[key] += weighted
                residual = value // (d * b)
                df = {p: k for p, k in fs.items() if d % p == 0}
                prime_outer = len(df) == 1 and d == next(iter(df))
                p_band = prime_outer and pow_le(d, n, F(7, 20)) and pow_le(n ** 3, d, F(10))
                # Exact enlarged residual cut, explicitly a finite stress fixture.
                in_mark = p_band and 2 * u < residual <= 32 * u
                target = marked if in_mark else comp if p_band else other
                target[key] += weighted
                counts['marked_rows'] += in_mark
                counts['marked_positive_rows'] += in_mark and bet > 0
                counts['marked_negative_rows'] += in_mark and bet < 0
                counts['repeated_b_rows'] += fs[b] > 1
    rhs = defaultdict(F)
    for key, coefficient in masked[2].items():
        rhs[key] += coefficient
    for mask, coef in plus.items():
        if not mask:
            continue
        e = products[mask]
        for key in set(masked[e]) | set(masked[2 * e]):
            rhs[key] -= coef * (masked[e][key] - masked[2 * e][key])
    for key, coefficient in gap.items():
        rhs[key] += coefficient
    demand(cleaned(rhs) == cleaned(small), "Exact signed small-prime sieve coupling, coefficient one")
    keys = set(even) | set(marked) | set(comp) | set(other)
    demand(all(even[key] == marked[key] + comp[key] + other[key] for key in keys),
           "Marked slice, complementary residuals and other even outer rows retain coefficient one")
    demand(all(abs(coef) <= envelope[key] for key, coef in gap.items()),
           "Signed error bounded by positive terminal majorant without ordering signed sums")
    return {"N": n, "U": u, "T_for_finite_identity": 5, "level_for_finite_identity": 64,
            "stress_U": True, "residual_cut_enlarged": True,
            "artificial_reference_width": width if wide else None, "counts": dict(counts),
            "small_block_identity_vector_terms": len(cleaned(small)),
            "signed_gap_vector_terms": len(cleaned(gap)),
            "marked_complement_partition_vector_terms": len(keys),
            "all_exact_coefficient_checks_passed": True,
            "asymptotic_bounds_inferred_from_samples": False}


def main():
    fixtures = [sieve_identity_fixture((3, 5, 7, 11, 13, 17), level, 2, 16)
                for level in (361, 1000, 4096)]
    fixtures.append(sieve_identity_fixture(tuple(p for p in primes_up_to(41) if p > 2),
                                            42 ** 32, 32, 32))
    demand(all(any(r[key] > 0 for r in fixtures) for key in
               ('positive_upper_terminals', 'positive_lower_terminals',
                'positive_beta_patterns', 'negative_beta_patterns')),
           "Both sieve errors and both beta signs exercised")
    actual = [actual_continuation_fixture(18000, 5),
              actual_continuation_fixture(18000, 5, wide=True),
              actual_continuation_fixture(100000, 16)]
    demand(sum(r['counts']['marked_positive_rows'] for r in actual) > 0 and
           sum(r['counts']['marked_negative_rows'] for r in actual) > 0,
           "Actual continuation stress fixtures exercise both marked signs")
    checks = {"checkpoint": 22, "date": "2026-10-09", "provenance": provenance(),
              "combinatorial_sieve_fixtures": fixtures,
              "source_phase_perturbations": facet_perturbations(),
              "actual_continuation_fixtures": actual, "all_exact_checks_passed": True,
              "finite_checks_prove_asymptotic_theorem": False}
    result = {"checkpoint": 22, "date": "2026-10-09", "proof_note": "SIGNED_SIEVE_COUPLING_NOTE.md",
              "growing_mask_aggregate_uniform_bound": "sum_(1<e<=2*N^delta0,squarefree)|B_e(J)| + a*sum|B_e(B1)| = o(u), some fixed delta0>0",
              "small_least_prime_signed_coefficient_limit": "lim_(epsilon->0+) limsup_(N->infinity,even) (|S_<=U^epsilon(J)|+a*|S_<=U^epsilon(B1)|)/u = 0",
              "uniform_sieve_error": "C*(log(N)/log(T+1/2))^2*exp(-delta0*log(N)/log(T+1/2))*u + o(u), T->infinity, T<=N^(delta0/64) eventually",
              "growing_subpower_least_prime_cutoff_negligible": True,
              "subpower_scope": "Every T_N->infinity with log(T_N)=o(log(N)); all original outer and continuation gates frozen at x",
              "explicit_cutoff": "T_N=U^(1/log(log(N)))",
              "explicit_cutoff_small_block_discrepancy": "o(u)",
              "fixed_power_epsilon_o_u_claimed": False,
              "fixed_power_error_can_use_arbitrarily_small_budget": True,
              "concrete_epsilon_for_0001_budget_numerically_certified": False,
              "coefficient_preserving_remaining_target": "E_(T_N<q<=U)-E_R <= (.011+o(1))*u",
              "original_0011_coefficient_retained": True,
              "signed_weights_compared_by_unsigned_sieve_inequality": False,
              "marked_residual_slice_separate_uniform_u_scale_proved": False,
              "marked_complement_coupling_scope": "All even marked/complementary residual rows are summed with original coefficient one; separately they remain open",
              "terminal_0011_estimate_proved": False, "higher_degree_cap_proved": False,
              "H_theta_proved": False, "certified_K": 0,
              "old_eta_scope": "Direct absolute-beta L1 estimate; completed full signed covariance remains O(u)"}
    for name, data in (("signed_sieve_coupling_checks.json", checks),
                       ("signed_sieve_coupling.json", result)):
        (ROOT / "results" / name).write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"all_exact_checks_passed": True,
                      "sieve_prime_patterns": sum(r['prime_divisibility_patterns'] for r in fixtures),
                      "phase_term_checks": checks['source_phase_perturbations']['facet_term_checks'],
                      "actual_active_sites": sum(r['counts']['active_sites'] for r in actual),
                      "marked_positive_rows": sum(r['counts']['marked_positive_rows'] for r in actual),
                      "marked_negative_rows": sum(r['counts']['marked_negative_rows'] for r in actual),
                      "checkpoint21_records_preserved": 232,
                      "terminal_0011_estimate_proved": False}))


if __name__ == "__main__":
    main()
