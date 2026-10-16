#!/usr/bin/env python3
"""Checkpoint 18: rough-core absorption and a stronger actual-beta L1 bound.

Checks exact arithmetic, formal logarithmic coefficients, rational domains
and outward transcendental enclosures. They do not prove the remaining
one-sided u-scale estimate. Writes only this checkpoint's result files.
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
from delta_grouping import CB, CI, good_outer, pow_le
from joint_remainder import vertices
from ross_geometry_audit import factor_band, primes_up_to
from structured_frontier import I
from two_three_frontier import divisors, outer_coefficient

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-10-08"
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}
LEDGER_HASH = "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"
OUTER_CACHE = {}


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def cleaned(v):
    return {key: value for key, value in v.items() if value}


def add(v, other, scale=F(1)):
    for key, value in other.items():
        v[key] += scale * value


def provenance():
    prior = json.loads((ROOT / "results/checkpoint17_preservation_manifest.json").read_text())
    demand(prior["checkpoint"] == 17, "Frozen checkpoint 17")
    count = 0
    for r in prior["files"]:
        if r["path"] in MUTABLE:
            continue
        b = (ROOT / r["path"]).read_bytes()
        demand(len(b) == r["size_bytes"] and sha256(b).hexdigest() == r["sha256"],
               r["path"] + " preservation")
        count += 1
    demand(count == 209, "209 unchanged historical records")
    demand(sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
           == LEDGER_HASH, "Frozen analytic ledger")
    return {"checkpoint_17_nonmutable_records_verified": count,
            "negative_frontier_ledger_sha256": LEDGER_HASH,
            "historical_analytic_ledger_unchanged": True}


def optimizer():
    """Certified root of decreasing F(rho)=3-rho+rho*log(rho/4)."""
    def fn(x):
        return 3 - x + x * (x / 4).log()
    lo, hi = F(3, 2), F(31, 20)
    demand(fn(I.point(lo)).lo > 0 and fn(I.point(hi)).hi < 0, "Root bracket signs")
    for _ in range(140):
        mid = (lo + hi) / 2
        y = fn(I.point(mid))
        if y.lo > 0:
            lo = mid
        elif y.hi < 0:
            hi = mid
        else:
            break
    rho = I.segment(lo, hi)
    demand(fn(I.point(lo)).lo > 0 and fn(I.point(hi)).hi < 0, "Outward root signs retained")
    t = rho / 2
    eta_high = (1 - rho + rho * rho.log()) / 2
    eta_low = 2 - rho + rho * (rho / 2).log()
    delta = 1 - (1 + I.point(2).log().log()) / I.point(2).log()
    difference = eta_high - eta_low
    demand(difference.lo <= 0 <= difference.hi, "Root balances the two exponents")
    demand(rho.lo > 1 and rho.hi < 2 and t.lo > F(1, 2) and t.hi < 1,
           "Uniform fixed divisor-bound parameters")
    demand(eta_high.lo > (delta / 2).hi and eta_high.hi < F(1, 2),
           "Strict improvement and rough-stratum reserve")
    return {"root_equation": "3-rho+rho*log(rho/4)=0; unique root in (1,2)",
            "rational_root_bracket": [str(lo), str(hi)],
            "rho": rho.record(), "t": t.record(),
            "new_log_saving_exponent": eta_high.record(),
            "low_stratum_exponent": eta_low.record(),
            "old_log_saving_exponent": (delta / 2).record(),
            "strict_log_exponent_gain": (eta_high - delta / 2).record(),
            "remaining_log_power_to_reach_u": (1 - eta_high).record(),
            "root_lower_sign": fn(I.point(lo)).record(),
            "root_upper_sign": fn(I.point(hi)).record(),
            "monotonicity": "F'(rho)=log(rho/4)<0 on (1,2)",
            "outward_enclosure_verified": True}


def core_facets():
    cs = [((F(1), F(1), F(1)), F(2)),
          ((F(-1), F(-1), F(-1)), F(-2)),
          ((F(-1), F(0), F(0)), F(-1, 4)),
          ((F(1), F(-1), F(0)), F(0)),
          ((F(0), F(1), F(-1)), F(0)),
          ((F(-1), F(-1), F(0)), -CI)]
    records = []
    for a, b, c in vertices(cs):
        upper_margin = F(19, 20) - c
        product_margin = b + c - CB
        demand(upper_margin >= F(37, 400), "All core primes are eligible single outers")
        demand(product_margin >= F(223, 1200), "Middle/largest product passes db gate")
        residual = c / (a + c) + b / (a + b) - 1
        demand(residual == (c - a) / (2 * (a + c)) + (b - a) / (2 * (a + b)),
               "Symbolic nonnegative log-ratio decomposition")
        demand(residual >= 0, "Ordered core ratios cover unit core weight")
        records.append({"a": str(a), "b": str(b), "c": str(c),
                        "single_upper_cutoff_margin": str(upper_margin),
                        "continuation_product_margin": str(product_margin),
                        "log_ratio_residual": str(residual)})
    demand(records, "Core superset nonempty")
    return {"constraints": [{"A": [str(x) for x in row], "rhs": str(rhs)}
                             for row, rhs in cs],
            "vertices": records,
            "minimum_single_upper_cutoff_margin": "37/400",
            "minimum_continuation_product_margin": "223/1200",
            "nonlinear_ratio_proof": "Residual=(c-a)/(2(a+c))+(b-a)/(2(a+b))>=0 throughout ordered domain",
            "exact_arithmetic_rounding_handled_in_proof": True,
            "source_length_margin_for_boundary_envelopes": "7/2400 (inherited)"}


def factor_subdivisor(d, fs):
    result = {}
    for p, exponent in fs.items():
        power = 0
        while d % p == 0:
            d //= p
            power += 1
        if power:
            demand(power <= exponent, "Actual divisor multiplicity")
            result[p] = power
    demand(d == 1, "Divisor factored")
    return result


def remainder(fs, ds):
    return {p: e - ds.get(p, 0) for p, e in fs.items() if e - ds.get(p, 0)}


def actual_weights(value, fs, n, u, allow_unit=False):
    """Independent original-outer enumeration; formal X_(d,b) coefficients."""
    v = defaultdict(F)
    core = F(0)
    core_rows = []
    for d in divisors(fs):
        df = factor_subdivisor(d, fs)
        if (n, d) not in OUTER_CACHE:
            c = outer_coefficient(df, n)
            OUTER_CACHE[(n, d)] = (c, good_outer(d, df, n) if c else False)
        weight, admitted = OUTER_CACHE[(n, d)]
        if not weight:
            continue
        after = remainder(fs, df)
        if admitted:
            for b in after:
                if b <= u or pow_le(d * b, n, CB):
                    continue
                if not allow_unit and value // (d * b) <= 1:
                    continue
                v[(d, b)] += weight
        elif len(after) == 1 and next(iter(after.values())) == 1:
            ell = next(iter(after))
            ps = sorted(p for p, e in df.items() for _ in range(e))
            demand(len(ps) == 2, "Core is a pair outer")
            p, r = ps
            core += weight
            core_rows.append((p, r, ell, weight))
    return cleaned(v), core, core_rows


def integer_squarefree(fs):
    return squarefree_divisors(tuple(sorted(fs.items())))


def fixture(n, u, actual, selected=None):
    demand(n % 2 == 0 and u ** 4 < n, "Stop primes exceed stress or actual U")
    if actual:
        demand(u ** 100 <= n < (u + 1) ** 100, "Actual campaign truncation")
    lo, hi = n * n - n // 2, n * n + n // 2
    fs_band = factor_band(lo, hi, primes_up_to(isqrt(hi)))
    if selected is not None:
        fs_band = {value: fs_band[value] for value in selected}
    counts = defaultdict(int)
    raw = defaultdict(F)
    positive = defaultdict(F)
    negative = defaultdict(F)
    rough_v = defaultdict(F)
    rough_core = F(0)
    absorption_lowers = []
    for value, fs in fs_band.items():
        counts['shell_sites'] += 1
        v, core, core_rows = actual_weights(value, fs, n, u)
        beta = beta_from_factors(fs, u)
        rough = min(fs) > u
        add(raw, v, beta)
        if rough:
            demand(beta == -1, "Exact rough beta sign")
            add(rough_v, v)
            rough_core += core
            counts['rough_sites'] += 1
        else:
            demand(core == 0, "Nonrough core vanishes")
            if beta > 0:
                add(positive, v, beta)
                counts['positive_beta_sites'] += 1
            elif beta < 0:
                add(negative, v, -beta)
                counts['negative_nonrough_beta_sites'] += 1
            small = 1
            large_fs = {}
            for p, e in fs.items():
                if p <= u:
                    small *= p ** e
                else:
                    large_fs[p] = e
            m = value // small
            star, _, _ = actual_weights(m, large_fs, n, u, allow_unit=True)
            demand(v == star, "Exact smooth multiplication invariance with activated unit rows")
            counts['smooth_invariance_rows'] += 1
            # Exact signed boundary representation, independently expanded.
            q = min(fs)
            paired = defaultdict(F)
            for d, mu, ps in integer_squarefree(fs):
                if d > u or d % q == 0 or q * d <= u:
                    continue
                demand(not ps or min(ps) > q, "Boundary least-prime restriction")
                mf = factor_subdivisor(value // (q * d), fs)
                kernel, _, _ = actual_weights(value // (q * d), mf, n, u, allow_unit=True)
                add(paired, kernel, -mu)
                counts['signed_boundary_divisor_rows'] += 1
            target = {key: beta * val for key, val in v.items() if beta * val}
            demand(cleaned(paired) == target, "Exact signed boundary kernel identity")
        if core:
            demand(rough and core <= 1 and len(core_rows) == 1, "Unique rough core mark")
            p, r, ell, weight = core_rows[0]
            demand(p <= r <= ell, "Actual core ordering")
            counts['core_sites'] += 1
            counts['core_p_equals_r'] += p == r
            if r == ell:
                counts['repeated_largest_exception_sites'] += 1
                demand(p ** 3 <= hi, "Repeated largest indexed by p<=shell cube root")
                continue
            demand(outer_coefficient({r: 1}, n) == 1 and
                   outer_coefficient({ell: 1}, n) == 1, "Two actual single outers")
            demand(not pow_le(r * ell, n, CB), "Actual cross-product gate")
            demand(v.get((r, ell), 0) >= 1 and v.get((ell, r), 0) >= 1,
                   "Both absorbing rows exist in actual continuation")
            lower = I.point(ell).log() / I.point(F(n * n, r)).log()
            lower = lower + I.point(r).log() / I.point(F(n * n, ell)).log()
            permitted = 1 - 2 / (I.point(n).log() * n)
            demand(lower.lo >= permitted.hi, "Outward actual frozen-log absorption inequality")
            absorption_lowers.append(str(lower.lo))
            counts['core_absorption_rows'] += 1
    reconstructed = defaultdict(F)
    add(reconstructed, positive)
    add(reconstructed, negative, -1)
    add(reconstructed, rough_v, -1)
    demand(cleaned(raw) == cleaned(reconstructed), "Exact aggregate signed continuation decomposition")
    return {"N": n, "U": u, "actual_campaign_truncation": actual,
            "scope": "Selected core sites" if selected is not None else "Complete actual square shell",
            "counts": dict(counts), "core_weight": str(rough_core),
            "minimum_absorbing_log_ratio_lower": min(absorption_lowers, default=None),
            "signed_decomposition_formal_coefficients": len(cleaned(raw)),
            "all_identities_passed": True,
            "terminal_u_scale_estimate_tested": False}


def crafted_core_sites():
    """Exercise both repeated-prime patterns on actual even-N square shells."""
    ps = primes_up_to(1000)
    chosen = {}
    for p in ps:
        if p < 17:
            continue
        for r in ps:
            if r < p or r > 2 * p:
                continue
            for value in [p * p * r, p * r * r]:
                root = isqrt(value)
                for n in {root - root % 2, root + 2 - root % 2}:
                    if n <= 1 or abs(value - n * n) > n // 2:
                        continue
                    fs = factor_band(value, value, ps)[value]
                    _, core, rows = actual_weights(value, fs, n, 1)
                    if core and rows:
                        a, b, c, _ = rows[0]
                        pattern = 'small_repeat' if a == b and b < c else 'large_repeat' if b == c else 'other'
                        if pattern not in chosen:
                            chosen[pattern] = (n, value)
                    if 'small_repeat' in chosen and 'large_repeat' in chosen:
                        return [fixture(n, 1, True, [value]) for n, value in chosen.values()]
    raise AssertionError("Both repeated-prime patterns must be exercised")


def boundary_envelope_checks():
    """Low-count |beta| is bounded directly by boundary divisor multiplicity."""
    fs = factor_table(30000)
    rows = witnesses = 0
    for k in range(2, len(fs)):
        ds = squarefree_divisors(fs[k])
        q = fs[k][0][0]
        for u in [16, 64, 256, 4096]:
            if q > isqrt(isqrt(u)):
                continue
            beta = sum(mu for d, mu, _ in ds if d > u)
            boundary = [(d, mu, ps) for d, mu, ps in ds if d % q and d <= u < q * d]
            odd = sum(mu < 0 for _, mu, _ in boundary)
            even = sum(mu > 0 for _, mu, _ in boundary)
            demand(beta == odd - even and abs(beta) <= len(boundary), "Exact signed boundary count")
            demand(max(beta, 0) <= odd, "Positive beta uses odd boundary marks")
            for d, _, ps in boundary:
                m = k // (q * d)
                exponent = omega_u(fs[m], u) - len(fs[gcd_value(m, d * q)])
                demand(omega_u(fs[k], u) == 1 + len(ps) + exponent, "Weighted boundary exponent")
                witnesses += 1
            rows += 1
    return {"signed_even_odd_boundary_rows": rows,
            "weighted_boundary_witnesses": witnesses,
            "stress_cutoffs": [16, 64, 256, 4096],
            "direct_L1_inequality_verified": True,
            "asymptotic_density_test": False}


def gcd_value(a, b):
    while b:
        a, b = b, a % b
    return a


def activation_witness():
    n, u, value, m = 96, 3, 9174, 1529
    fs = {2: 1, 3: 1, 11: 1, 139: 1}
    mfs = {11: 1, 139: 1}
    actual, _, _ = actual_weights(value, fs, n, u)
    ordinary, _, _ = actual_weights(m, mfs, n, u)
    star, _, _ = actual_weights(m, mfs, n, u, allow_unit=True)
    demand(actual == star and actual != ordinary, "Unit rows must be activated in boundary kernel")
    demand(u ** 4 < n and abs(value - n * n) <= n // 2, "Activation is on actual shell support")
    demand(beta_from_factors(fs, u) == 1, "Activated row has positive actual stress beta")
    return {"N": n, "stress_U": u, "actual_shell_site": value,
            "smooth_factor": 6, "boundary_q": 2, "boundary_d": 3,
            "beta_U_n": 1, "remaining_m": m,
            "activated_formal_rows": [{'d': d, 'b': b, 'coefficient': str(c)}
                                      for (d, b), c in actual.items()],
            "ordinary_continuation_on_m_is_zero": not ordinary,
            "scope": "Exact signed-boundary unit-activation illustration; U=3 is a stress cutoff"}


def main():
    p = provenance()
    parameters = optimizer()
    facets = core_facets()
    arithmetic = [fixture(n, u, actual) for n, u, actual in
                  [(100, 1, True), (1000, 3, False), (10000, 5, False),
                   (30000, 8, False), (100000, 16, False)]]
    arithmetic += crafted_core_sites()
    envelope = boundary_envelope_checks()
    activation = activation_witness()
    totals = defaultdict(int)
    for f in arithmetic:
        for k, v in f['counts'].items():
            totals[k] += v
    demand(totals['core_p_equals_r'] > 0 and totals['repeated_largest_exception_sites'] > 0,
           "Both repeated core patterns checked")
    demand(totals['negative_nonrough_beta_sites'] > 0, "Nonrough negative-beta counterweight exercised")
    checks = {"date": DATE, "checkpoint": 18, "all_checks_passed": True,
              "provenance": p, "parameters": parameters, "core_facets": facets,
              "arithmetic_fixtures": arithmetic, "aggregate_counts": dict(totals),
              "boundary_envelope_checks": envelope, "unit_activation_witness": activation,
              "proof_note": "SIGNED_CORE_CONTINUATION_NOTE.md",
              "terminal_u_scale_estimate_verified_by_finite_tests": False}
    estimate = {
        "date": DATE, "checkpoint": 18, "proof_note": "SIGNED_CORE_CONTINUATION_NOTE.md",
        "actual_U": "floor(N^(1/100))",
        "uniformity": "Every sufficiently large even N; actual gates unchanged",
        "rough_core_absorption": "sum_(n in J,Pminus(n)>U)(P_N(n)-V_N(n)) <= O(N^(2/3)+1/log N)=o(u)",
        "rough_core_absorption_proved": True,
        "rough_core_absorption_is_pointwise_except_sparse_repeated_largest_cases": True,
        "repeated_largest_error": "O(N^(2/3))",
        "signed_interface": "C_N=F_N^+-G_N^--R_N+o(u); F_N^+,G_N^->=0 and R_N>=-o(u)",
        "positive_beta_weighted_sum": "F_N^+=sum_(n in J,beta_U(n)>0)beta_U(n)*V_N(n)",
        "signed_boundary_kernel": "sum_(nonrough n) beta_U(n)V_N(n)=-sum_(q<=U)sum_(U/q<d<=U,mu^2(d)=1,Pminus(d)>q)mu(d)*sum_(q*d*m in J,Pminus(m)>=q)V_N^*(m)",
        "activated_unit_rows_required_in_V_star": True,
        "actual_beta_L1_bound": "sum_(I_p)|beta_U| << H_p/(log U)^eta",
        "actual_covariance_absolute_bound": "|C_N| << N/(log N)^eta",
        "parameters": parameters,
        "new_partial_log_saving_proved": True,
        "old_beta_support_sparsity_bound_retained": True,
        "actual_gates_retained": True,
        "new_u_scale_signed_cancellation_estimate_proved": False,
        "remaining_one_sided_target": "F_N^+-G_N^--R_N <= (M_core+.011+o(1))*u",
        "source_input": "Inherited Mangerel (2023), Lemma 3.2, uniform Shiu upper bound; inherited beta second moment",
        "source_url": "https://doi.org/10.1007/s40687-023-00376-0",
        "terminal_0011_estimate_proved": False, "H_theta_proved": False,
        "higher_degree_cap_proved": False, "certified_K": 0,
        "core_reference_enclosure_changed": False, "historical_mass_credit": 0,
        "provenance": p, "checks": "results/signed_core_continuation_checks.json"}
    for name, data in [('signed_core_continuation_checks.json', checks),
                       ('signed_core_continuation_estimate.json', estimate)]:
        (ROOT / 'results' / name).write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({"all_checks_passed": True, "aggregate_counts": dict(totals),
                      "new_log_exponent": parameters['new_log_saving_exponent'],
                      "boundary_counts": envelope, "historical_records_unchanged": 209,
                      "terminal_0011_estimate_proved": False}, indent=2))


if __name__ == '__main__':
    main()
