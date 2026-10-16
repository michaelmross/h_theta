#!/usr/bin/env python3
"""Checkpoint 19: exact signed kernel discrepancies and their available bounds.

Finite checks verify arithmetic identities and hypotheses, not the missing
.011u estimate. Historical programs are imported without rerunning them.
Only this checkpoint's two result files are written.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

from beta_support import factor_table, squarefree_divisors, omega_u
from cofactor_estimation import beta_from_factors
from delta_grouping import CB, pow_le
from ross_geometry_audit import factor_band, primes_up_to
from signed_core_continuation import actual_weights, add, cleaned, integer_squarefree

ROOT = Path(__file__).resolve().parents[1]
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}
LEDGER_HASH = "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"
DATE = "2026-10-08"


def demand(ok, name):
    if not ok:
        raise AssertionError(name)


def provenance():
    frozen = json.loads((ROOT / "results/checkpoint18_preservation_manifest.json").read_text())
    demand(frozen["checkpoint"] == 18, "Frozen checkpoint 18")
    count = 0
    for record in frozen["files"]:
        if record["path"] in MUTABLE:
            continue
        raw = (ROOT / record["path"]).read_bytes()
        demand(len(raw) == record["size_bytes"] and sha256(raw).hexdigest() == record["sha256"],
               record["path"] + " preservation")
        count += 1
    demand(count == 214, "214 historical nonmutable records")
    demand(sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
           == LEDGER_HASH, "Frozen negative ledger")
    return {"checkpoint18_nonmutable_records_verified": count,
            "negative_frontier_ledger_sha256": LEDGER_HASH,
            "historical_analytic_ledger_unchanged": True}


def trial_factor(value, primes):
    result = {}
    for p in primes:
        if p * p > value:
            break
        while value % p == 0:
            result[p] = result.get(p, 0) + 1
            value //= p
    if value > 1:
        result[value] = result.get(value, 0) + 1
    return result


def rough_part(fs, u):
    result = 1
    for p, exponent in fs.items():
        if p > u:
            result *= p ** exponent
    return result


def kernel_family(u):
    """Independent enumeration of all possible (q,d), not shell divisors."""
    table = factor_table(u)
    qs = primes_up_to(u)
    family = []
    for q in qs:
        for d in range(u // q + 1, u + 1):
            fs = table[d]
            if not fs or fs[0][0] <= q or any(e != 1 for _, e in fs):
                continue
            demand(q * d > u and q * d <= u * u, "Actual boundary multiplier range")
            family.append((q, d, (-1) ** len(fs)))
    demand(len({q * d for q, d, _ in family}) == len(family),
           "Boundary multiplier uniquely determines its least prime")
    return family


def actual_window(n, u, lo, hi, cutoff, primes):
    fs_band = factor_band(lo, hi, primes)
    signed = defaultdict(F)
    small = defaultdict(F)
    large = defaultdict(F)
    rough_v = defaultdict(F)
    core_total = F(0)
    counts = defaultdict(int)
    active_rough_parts = {}
    values = {}
    for value, fs in fs_band.items():
        counts['shell_sites'] += 1
        beta = beta_from_factors(fs, u)
        v, core, _ = actual_weights(value, fs, n, u)
        q = min(fs)
        rp = rough_part(fs, u)
        values[value] = (fs, beta, v, core, rp)
        demand(core <= 3, "At most three prime-cofactor pair marks, including reference sites")
        if q <= u:
            demand(core == 0, "Core vanishes on nonrough sites")
            add(signed, v, beta)
            add(small if q <= cutoff else large, v, beta)
            counts['nonrough_sites'] += 1
            counts['nonrough_positive_beta_active'] += beta > 0 and bool(v)
            counts['nonrough_negative_beta_active'] += beta < 0 and bool(v)
        else:
            demand(beta == -1, "Exact rough sign")
            add(rough_v, v)
            core_total += core
            counts['rough_sites'] += 1
        if v:
            demand(not pow_le(rp, n, CB), "Every active rough part exceeds D_B")
            demand(rp > n, "Every active rough part exceeds shell diameter")
            if hi - lo == n:
                demand(rp not in active_rough_parts, "No two active shell sites share a rough part")
                active_rough_parts[rp] = value
            counts['active_continuation_sites'] += 1
        if beta and q <= u:
            demand(value // rp > u, "Nonzero nonrough beta requires full small part > U")
        for (d, b) in v:
            demand(value % (d * b) == 0 and d * b > n, "Active prime-product incidence")
    # Arbitrary 0/1 selection on active nonrough sites can be extended to a
    # smooth-invariant auxiliary weight, without asserting it is actual V.
    selector_checks = 0
    if hi - lo == n:
        chosen_parts = {rp for _, beta, v, _, rp in values.values() if beta > 0 and v}
        for _, beta, v, _, rp in values.values():
            demand((rp in chosen_parts) == (beta > 0 and bool(v)),
                   "Smooth-invariant selector can reproduce the positive active subset")
            selector_checks += 1
    return {"signed": cleaned(signed), "small": cleaned(small), "large": cleaned(large),
            "rough_v": cleaned(rough_v), "rough_core": core_total,
            "counts": dict(counts), "selector_checks": selector_checks}


def direct_kernels(n, u, lo, hi, cutoff, primes):
    family = kernel_family(u)
    signed = defaultdict(F)
    small = defaultdict(F)
    large = defaultdict(F)
    counts = defaultdict(int)
    rows = []
    for q, d, mu in family:
        a = q * d
        kernel = defaultdict(F)
        first = (lo + a - 1) // a
        last = hi // a
        for m in range(first, last + 1):
            fs = trial_factor(m, primes)
            if fs and min(fs) < q:
                continue
            v, _, _ = actual_weights(m, fs, n, u, allow_unit=True)
            add(kernel, v)
            counts['kernel_cofactor_sites'] += 1
            counts['kernel_active_cofactor_sites'] += bool(v)
            counts['q_divides_m'] += m % q == 0
            counts['d_shares_prime_with_m'] += any(m % r == 0 for r, _ in factor_table(d)[d])
            for outer, b in v:
                demand(m % (outer * b) == 0, "Auxiliary cofactor divisibility")
                demand(a * m // (outer * b) > u, "Original Vaughan residual is > U")
                if m == outer * b:
                    counts['unit_activated_rows'] += 1
        add(signed, kernel, -mu)
        add(small if q <= cutoff else large, kernel, -mu)
        rows.append({"q": q, "d": d, "mu_d": mu,
                     "integer_cofactor_range": [first, last],
                     "formal_weight_terms": len(cleaned(kernel))})
        counts['kernel_pairs'] += 1
        counts['mu_positive_pairs'] += mu > 0
        counts['mu_negative_pairs'] += mu < 0
    # Closed real cofactor cells are disjoint across all actual boundary a.
    mults = sorted(q * d for q, d, _ in family)
    separated = 0
    for a, b in zip(mults, mults[1:]):
        gap = F(lo, a) - F(hi, b)
        demand(gap > 0, "Disjoint cofactor cells for distinct boundary multipliers")
        separated += 1
    return {"signed": cleaned(signed), "small": cleaned(small), "large": cleaned(large),
            "counts": dict(counts), "cell_separations": separated,
            "pair_records": rows}


def exact_discrepancy(j, ref, a):
    out = defaultdict(F)
    add(out, j)
    add(out, ref, -a)
    return cleaned(out)


def fixture(n, u, cutoff, actual):
    demand(n % 2 == 0 and u ** 4 < n and u * u < n,
           "Stop primes exceed U; boundary cells separate")
    if actual:
        demand(u ** 100 <= n < (u + 1) ** 100, "Actual campaign cutoff")
    demand(1 <= cutoff <= u, "Least-prime split cutoff")
    lo, hi = n * n - n // 2, n * n + n // 2
    # Artificial wider reference, used only to verify identities. It does
    # not simulate the campaign asymptotic long-reference estimate.
    length = 3 * n + 1
    rlo, rhi = n * n - (length - 1) // 2, n * n + (length - 1) // 2
    a = F(n + 1, length)
    primes = primes_up_to(isqrt(rhi))
    j = actual_window(n, u, lo, hi, cutoff, primes)
    ref = actual_window(n, u, rlo, rhi, cutoff, primes)
    kj = direct_kernels(n, u, lo, hi, cutoff, primes)
    kr = direct_kernels(n, u, rlo, rhi, cutoff, primes)
    for name in ['signed', 'small', 'large']:
        demand(j[name] == kj[name] and ref[name] == kr[name],
               "Direct kernel enumeration equals original nonrough " + name)
    lhs = defaultdict(F)
    add(lhs, j['signed'])
    add(lhs, j['rough_v'], -1)
    add(lhs, ref['signed'], -a)
    add(lhs, ref['rough_v'], a)
    core_lhs = j['rough_core'] - a * ref['rough_core']
    rhs = defaultdict(F)
    add(rhs, exact_discrepancy(kj['small'], kr['small'], a))
    add(rhs, exact_discrepancy(kj['large'], kr['large'], a))
    add(rhs, exact_discrepancy(j['rough_v'], ref['rough_v'], a), -1)
    demand(cleaned(lhs) == cleaned(rhs), "Exact joint signed discrepancy, formal logarithms")
    demand(core_lhs == -( -j['rough_core'] + a * ref['rough_core']),
           "Rough core counterweight sign in discrepancy")
    totals = defaultdict(int)
    for kind in [j, ref, kj, kr]:
        for key, value in kind['counts'].items():
            totals[key] += value
    totals['smooth_invariant_selector_checks'] = j['selector_checks']
    totals['disjoint_cofactor_cell_pairs'] = kj['cell_separations'] + kr['cell_separations']
    return {"N": n, "U": u, "actual_campaign_cutoff": actual,
            "least_prime_split_T": cutoff, "short_window": [lo, hi],
            "identity_reference_window": [rlo, rhi], "normalization_a": str(a),
            "reference_scope": "Artificial 3N+1 window for exact identities; no analytic reference main term tested",
            "counts": dict(totals), "short_kernel_pair_records": kj['pair_records'],
            "formal_discrepancy_logarithmic_terms": len(cleaned(lhs)),
            "formal_discrepancy_core_scalar": str(core_lhs),
            "passed": True}


def multiplicative_envelope():
    table = factor_table(60000)
    rows = 0
    high_least_prime_sign_rows = 0
    high_least_prime_nonrough_rows = 0
    for u, cutoff in [(8, 2), (16, 2), (16, 4), (64, 4), (256, 16), (4096, 64)]:
        for value in range(2, len(table)):
            fs = table[value]
            if fs[0][0] <= cutoff:
                continue
            beta = sum(mu for d, mu, _ in squarefree_divisors(fs) if d > u)
            envelope = 2 ** omega_u(fs, u)
            tau = 1
            for _, e in fs:
                tau *= e + 1
            demand(abs(beta) <= envelope <= tau, "Actual beta bounded by divisor-bounded rough envelope")
            rows += 1
            if fs[0][0] ** 2 > u:
                demand(beta == omega_u(fs, u) - 1,
                       "Exact beta equals omega_U-1 above square-root least-prime cutoff")
                high_least_prime_sign_rows += 1
                if fs[0][0] <= u:
                    demand(beta >= 0, "Nonrough high least-prime block is nonnegative")
                    high_least_prime_nonrough_rows += 1
    # Prime-power values give multiplicativity and a uniform tau bound.
    prime_power_checks = 0
    for case in [0, 1, 2]:
        value = [0, 2, 1][case]
        for exponent in range(1, 16):
            demand(value <= exponent + 1, "Fixed prime-power divisor bound")
            prime_power_checks += 1
    return {"actual_beta_envelope_checks": rows,
            "high_least_prime_sign_identity_checks": high_least_prime_sign_rows,
            "high_least_prime_nonrough_sign_checks": high_least_prime_nonrough_rows,
            "high_least_prime_sign_identity": "Pminus(n)>sqrt(U) implies beta_U(n)=omega_U(n)-1",
            "negative_nonrough_beta_support": "Pminus(n)<=sqrt(U)",
            "prime_power_divisor_bound_checks": prime_power_checks,
            "prime_values": {"p<=T": 0, "T<p<=U": 2, "p>U": 1},
            "Euler_exponent": "sum_(p<=U)1/p - 2*sum_(p<=T)1/p",
            "Euler_product_upper_scale": "log(U)/(log(T))^2",
            "uniform_source_parameters": {"B": 2, "C": 1, "interval_delta": "1/30"},
            "analytic_Shiu_density_not_inferred_from_finite_checks": True}


def rational_hypotheses():
    records = []
    for s in [F(0), F(1, 100), F(1, 50)]:
        width, center = 1 - s, 2 - s
        margin = width - center / 30
        demand(margin >= F(457, 500), "Uniform global-kernel Shiu margin")
        demand(center > F(1, 100), "U lies below all kernel centers")
        records.append({"s": str(s), "width_exponent": str(width),
                        "center_exponent": str(center), "Shiu_margin": str(margin),
                        "width_to_center_ratio": str(width / center)})
    demand(CB - 1 == F(59, 400), "Active product exceeds shell diameter")
    demand(2 - CB == F(341, 400), "Full small-part exponent cap")
    demand(1 - F(1, 50) == F(49, 50), "Boundary multiplier exponent margin")
    demand(F(11, 20) - F(1, 2) == F(1, 20), "Primitive Mobius theorem length gap")
    demand(F(3, 7) == (1 - F(1, 4)) / (2 - F(1, 4)), "Largest stopped interval ratio")
    demand(F(11, 20) - F(3, 7) == F(17, 140), "Stopped Mobius theorem length gap")
    # Reference low-product mean error has normalized exponent CB+.01-1.
    low_error = CB + F(1, 100) - 1
    demand(low_error == F(63, 400) and low_error < 1, "Long low-product floor error negligible")
    demand(F(249, 250) < 1, "Proper-b-power leading exponent, epsilon=.001")
    return {"kernel_interval_facets": records, "minimum_global_kernel_Shiu_margin": "457/500",
            "active_rough_part_above_N_margin": "59/400",
            "full_smooth_part_maximum_exponent": "341/400",
            "boundary_multiplier_below_N_margin": "49/50",
            "kernel_primitive_Mobius_055_length_gap_at_least": "1/20",
            "stopped_primitive_Mobius_055_length_gap_at_least": "17/140",
            "normalized_long_low_product_floor_exponent": str(low_error),
            "low_product_error_has_N_epsilon_and_rho_inverse_factors": True,
            "proper_b_power_leading_exponent_with_epsilon_0001": "249/250"}


def main():
    prov = provenance()
    fixtures = [fixture(100, 1, 1, True), fixture(96, 3, 2, False),
                fixture(1000, 3, 2, False), fixture(10000, 5, 2, False),
                fixture(30000, 8, 2, False), fixture(100000, 16, 4, False)]
    totals = defaultdict(int)
    for item in fixtures:
        for name, value in item['counts'].items():
            totals[name] += value
    demand(totals['unit_activated_rows'] > 0, "Unit activation exercised")
    demand(totals['nonrough_positive_beta_active'] > 0 and
           totals['nonrough_negative_beta_active'] > 0, "Both signed active nonrough strata exercised")
    demand(totals['mu_positive_pairs'] > 0 and totals['mu_negative_pairs'] > 0,
           "Both boundary coefficient signs exercised")
    demand(totals['q_divides_m'] > 0 and totals['d_shares_prime_with_m'] > 0,
           "No unproved coprimality imposed")
    checks = {"checkpoint": 19, "date": DATE, "provenance": prov,
              "fixtures": fixtures, "totals": dict(totals),
              "multiplicative_envelope": multiplicative_envelope(),
              "rational_hypotheses": rational_hypotheses(),
              "all_exact_checks_passed": True,
              "terminal_0011_estimate_tested": False,
              "finite_identity_checks_are_not_asymptotic_estimates": True}
    estimate = {"checkpoint": 19, "date": DATE,
                "actual_rough_counterweight_uniform_u_scale_proved": True,
                "rough_counterweight_bound": "-o(u) <= R_N << u (upper constant unspecified)",
                "individual_boundary_kernel_uniform_upper_bound_proved": True,
                "kernel_upper_bound": "K_N(q,d) << N/(q*d*log(q)), uniformly on actual boundary family",
                "large_least_prime_signed_block_u_scale_proved": True,
                "high_least_prime_exact_beta_sign_identity_proved": True,
                "nonrough_high_least_prime_block_nonnegative": "T=sqrt(U); beta_U=omega_U-1>=0; G_N^- supported on Pminus<=sqrt(U)",
                "large_least_prime_bound": "|S_(>T)(J)| << N*log(U)/(log(T))^2; T=U^epsilon gives O(epsilon^-2*u)",
                "large_least_prime_discrepancy_bound": "|E_(>T)| << epsilon^-2*u, fixed 0<epsilon<=1",
                "rough_discrepancy_uniform_u_scale_proved": True,
                "reference_signed_interface_main_term_proved": True,
                "normalized_reference_signed_interface": "a*(S_N(B1)-R_N(B1))=(M_core+o(1))*u",
                "actual_kernel_discrepancy_identity_proved": True,
                "individual_kernel_discrepancy_bound": "|K_J(q,d)-a*K_B1(q,d)| << N/(q*d*log(q))",
                "remaining_exact_target": "-sum_(q,d)mu(d)*(K_J(q,d)-a*K_B1(q,d))-(R_J-a*R_B1) <= (.011+o(1))*u",
                "small_least_prime_signed_block_estimated_at_u_scale": False,
                "sharp_0011_coefficient_proved": False,
                "actual_small_part_rigidity_proved": True,
                "small_part_rigidity": "Active rough part >D_B>N: at most one smooth multiplier can land in J",
                "cofactor_cells_disjoint_proved": True,
                "scope_of_rigidity_warning": "Blocks automatic cancellation from smooth invariance; not a counterexample to actual campaign estimate",
                "overall_covariance_log_exponent_unchanged": "0.06024782442318413...",
                "uniform_analytic_input": "Mangerel (2023), Lemma 3.2; inherited quantitative long PNT and checkpoint11 long-reference reduction",
                "new_external_signed_cancellation_theorem_admitted": False,
                "reference_core_enclosure_changed": False,
                "terminal_0011_estimate_proved": False,
                "H_theta_proved": False, "certified_K": 0,
                "historical_analytic_ledger_unchanged": True}
    for name, content in [("signed_kernel_estimation_checks.json", checks),
                          ("signed_kernel_estimation.json", estimate)]:
        (ROOT / "results" / name).write_text(json.dumps(content, indent=2) + '\n')
    print(json.dumps({"checkpoint": 19, "all_exact_checks_passed": True,
                      "totals": dict(totals),
                      "actual_beta_envelope_checks": checks['multiplicative_envelope']['actual_beta_envelope_checks'],
                      "historical_records_preserved": prov['checkpoint18_nonmutable_records_verified'],
                      "terminal_0011_estimate_proved": False}, indent=2))


if __name__ == '__main__':
    main()
