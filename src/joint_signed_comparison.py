#!/usr/bin/env python3
"""Checkpoint 23: exact joint-comparison, multiplicity and Mellin checks.

The analytic deductions are proved in JOINT_SIGNED_COMPARISON_NOTE.md.
Finite fixtures do not prove its remaining .007935u spectral inequality.
Historical modules and results are read without rewriting them.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from decimal import Decimal
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, isqrt
from pathlib import Path
import json

from cofactor_estimation import beta_from_factors
from restricted_frontier import rounded_reference_length
from ross_geometry_audit import factor_band, primes_up_to
from signed_core_continuation import actual_weights, cleaned
from structured_frontier import I
from two_three_frontier import outer_coefficient

ROOT = Path(__file__).resolve().parents[1]
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}
KAPPA = F(1, 1000)
SMOOTH_BUDGET = F(613, 200000)
SPECTRAL_BUDGET = F(1587, 200000)
TARGET = F(11, 1000)


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def preservation():
    prior = json.loads((ROOT / "results/checkpoint22_preservation_manifest.json").read_text())
    demand(prior["checkpoint"] == 22, "Recovered checkpoint 22")
    count = 0
    for rec in prior["files"]:
        if rec["path"] in MUTABLE:
            continue
        data = (ROOT / rec["path"]).read_bytes()
        demand(len(data) == rec["size_bytes"] and sha256(data).hexdigest() == rec["sha256"],
               "Preservation: " + rec["path"])
        count += 1
    demand(count == 238, "238 historical nonmutable files")
    ledger = ROOT / "results/negative_frontier_ledger.json"
    digest = sha256(ledger.read_bytes()).hexdigest()
    demand(digest == "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
           "Frozen negative-frontier ledger")
    return {"checkpoint22_nonmutable_records_verified": count,
            "negative_frontier_ledger_sha256": digest}


def prime_cofactor_marks(value, fs, n):
    # Removing each distinct prime independently enumerates every prime cofactor.
    total, rows = F(0), []
    for q in fs:
        df = dict(fs)
        df[q] -= 1
        if not df[q]:
            del df[q]
        weight = outer_coefficient(df, n)
        if weight:
            total += weight
            rows.append((value // q, q, df, weight))
    return total, rows


def counted_weight(fs, n):
    degree = sum(fs.values())
    if min(fs) ** 4 < n or degree not in (2, 3):
        return F(0)
    if degree == 2 and min(fs) ** 20 >= n ** 19:
        return F(0)
    denom = 1
    for exponent in fs.values():
        denom *= factorial(exponent)
    return F(1, denom)


def sector_fixture(n, u, use_actual_reference=True):
    demand(n % 2 == 0 and u ** 4 < n, "Every original outer prime exceeds stress U")
    reference, _ = rounded_reference_length(n)
    reference = reference if use_actual_reference else 3 * n + 1
    cuts = sorted({2, 3, 5, u // 2, u})
    cuts = [t for t in cuts if 1 <= t <= u]
    record = {"N": n, "U": u, "actual_campaign_U": u == 1,
              "artificial_reference": not use_actual_reference, "H1_fixture": reference,
              "cutoffs": cuts, "windows": []}
    for name, width in (("J", n + 1), ("B1", reference)):
        lo, hi = n * n - width // 2, n * n + width // 2
        trial = primes_up_to(isqrt(hi))
        counts = Counter()
        largest_mark = F(0)
        total_marks = factorial_marks = F(0)
        error_sites = repeated_sites = 0
        for start in range(lo, hi + 1, 10000):
            band = factor_band(start, min(hi, start + 9999), trial)
            for value, fs in band.items():
                beta = beta_from_factors(fs, u)
                v, core, _ = actual_weights(value, fs, n, u)
                counts["sites"] += 1
                counts["positive_beta_active_sites"] += bool(v) and beta > 0
                counts["negative_nonrough_active_sites"] += bool(v) and min(fs) <= u and beta < 0
                counts["core_mark_sites"] += bool(core)
                counts["half_weight_core_sites"] += core == F(1, 2)
                counts["repeated_prime_active_sites"] += bool(v) and any(k > 1 for k in fs.values())
                for (d, b), coefficient in v.items():
                    counts["active_original_continuation_rows"] += 1
                    residual = dict(fs)
                    for p, exponent in fs.items():
                        j = d
                        multiplicity = 0
                        while j % p == 0:
                            j //= p
                            multiplicity += 1
                        residual[p] -= multiplicity + int(p == b)
                    residual = {p: k for p, k in residual.items() if k}
                    demand(value // (d * b) > 1, "Original nonunit continuation gate")
                    demand(beta_from_factors(residual, u) == beta, "Original residual-beta invariance")
                full = {("V", d, b): beta * c for (d, b), c in v.items()}
                full[("core", 0, 0)] = core
                full = cleaned(full)
                if core:
                    demand(min(fs) > u, "Original core marks are rough")
                for cut in cuts:
                    pieces = defaultdict(F)
                    if min(fs) <= cut:
                        for (d, b), c in v.items():
                            pieces[("V", d, b)] += beta * c
                    elif min(fs) <= u:
                        for (d, b), c in v.items():
                            pieces[("V", d, b)] += beta * c
                    else:
                        demand(beta == -1, "Exact rough beta value")
                        for (d, b), c in v.items():
                            pieces[("V", d, b)] -= c
                        pieces[("core", 0, 0)] += core
                    demand(cleaned(pieces) == full, "Small + high - rough, all coefficients one")
                    counts["joint_signed_sector_identity_checks"] += 1
                marks, rows = prime_cofactor_marks(value, fs, n)
                original = counted_weight(fs, n)
                total_marks += marks
                factorial_marks += original
                if marks != original:
                    error_sites += 1
                    if name == "J":
                        demand(any(k > 1 for k in fs.values()),
                               "Only repeated-prime rows can differ in the actual short orientation")
                    elif all(k == 1 for k in fs.values()):
                        demand(sum(fs.values()) == 3, "Reference non-diagonal error is triprime")
                        witnesses = []
                        for q in fs:
                            outer = sorted(p for p in fs if p != q)
                            p, r = outer
                            threshold = p * r * r
                            if (q >= r) != (threshold <= n * n):
                                demand(lo <= threshold <= hi, "Retained reference ordering threshold")
                                witnesses.append(threshold)
                        demand(witnesses, "Explicit reference freezing-error witness")
                if name == "J":
                    rough_z = min(fs) ** 4 >= n
                    demand(0 <= marks <= int(rough_z), "Pointwise mark cap one on the actual shell")
                    demand(len(rows) <= 1, "Unique actual-shell prime-cofactor mark")
                    for _, q, df, _ in rows:
                        if sum(df.values()) == 2:
                            demand(q >= max(df), "Actual shell selects two smallest factors")
                    largest_mark = max(largest_mark, marks)
                    counts["pointwise_cap_one_checks"] += 1
                # g=1 on [N^(3/5), N^(9/5)] for all active cofactor rows here.
                for _, q, _, _ in rows:
                    demand(q ** 5 >= n ** 3 and q ** 5 <= n ** 9,
                           "Smooth prime padding equals one on every counted cofactor")
                    counts["prime_padding_checks"] += 1
                repeated_sites += any(k > 1 for k in fs.values())
        record["windows"].append({
            "name": name, "endpoints": [lo, hi], "counts": dict(counts),
            "Q_all_exact": str(total_marks), "M2_plus_M3_exact": str(factorial_marks),
            "orientation_or_diagonal_error_exact": str(total_marks - factorial_marks),
            "orientation_or_diagonal_error_sites": error_sites,
            "repeated_prime_sites": repeated_sites, "maximum_short_mark": str(largest_mark)
        })
        print("Joint signed fixture: N=" + str(n) + ", " + name, flush=True)
    return record


def psi(value, x, h, kappa=KAPPA):
    distance = abs(F(value) - x)
    if distance <= h / 2:
        return F(1)
    return max(F(0), (h / 2 + kappa * h - distance) / (kappa * h))


def endpoints(x, h, kappa=KAPPA):
    return (x - h / 2 - kappa * h, x - h / 2,
            x + h / 2, x + h / 2 + kappa * h)


def mellin_integer_moment(x, h, s):
    a, b, c, d = endpoints(x, h)
    return (a ** (s + 1) - b ** (s + 1) - c ** (s + 1) + d ** (s + 1)) / (
        KAPPA * h * s * (s + 1))


def independent_piecewise_moment(x, h, s):
    a, b, c, d = endpoints(x, h)
    first = ((b ** (s + 1) - a ** (s + 1)) / (s + 1)
             - a * (b ** s - a ** s) / s) / (KAPPA * h)
    middle = (c ** s - b ** s) / s
    last = (d * (d ** s - c ** s) / s
            - (d ** (s + 1) - c ** (s + 1)) / (s + 1)) / (KAPPA * h)
    return first + middle + last


def smoothing_checks():
    records, count = [], 0
    for n in (20, 100, 5000, 10000, 80000):
        x, y = F(n * n), F(n + 1)
        ref, _ = rounded_reference_length(n)
        h = F(ref)
        scale = y / h
        for width in (y, h):
            for s in (1, 2, 3, 4):
                demand(mellin_integer_moment(x, width, s) ==
                       independent_piecewise_moment(x, width, s),
                       "Exact Mellin moment against independent piecewise integration")
                count += 1
            demand(mellin_integer_moment(x, width, 1) == (1 + KAPPA) * width,
                   "Exact trapezoid area")
            count += 1
        contrast = mellin_integer_moment(x, y, 1) - scale * mellin_integer_moment(x, h, 1)
        demand(contrast == 0, "Exact paired zero-frequency cancellation")
        for value in range(n * n - n // 2, n * n + n // 2 + 1):
            demand(psi(F(value), x, y) == 1, "Positive majorant covers each original site")
            count += 1
        records.append({"N": n, "Y": str(y), "H1": str(h), "a": str(scale),
                        "short_area": str((1 + KAPPA) * y),
                        "normalized_long_area": str(scale * (1 + KAPPA) * h),
                        "contrast_mass": str(contrast)})
    # Smootherstep transition has H'=30t^2(1-t)^2 and H'' vanishes at both ends.
    for t in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
        h0 = 10 * t ** 3 - 15 * t ** 4 + 6 * t ** 5
        derivative = 30 * t ** 2 - 60 * t ** 3 + 30 * t ** 4
        demand(derivative == 30 * t ** 2 * (1 - t) ** 2 and 0 <= h0 <= 1,
               "C2 compact prime-padding transition")
    return {"exact_smoothing_checks": count, "paired_kernels": records,
            "smooth_prime_padding": {"support_exponents": ["1/2", "19/10"],
                                     "plateau_exponents": ["3/5", "9/5"],
                                     "transition_polynomial": "10t^3-15t^4+6t^5",
                                     "regularity": "C2, piecewise polynomial"},
            "finite_checks_prove_spectral_bound": False}


def coefficient_budget():
    source = json.loads((ROOT / "results/two_three_reference_and_samples.json").read_text())
    mr = source["joint_reference_mass"]
    mass = I(Decimal(mr["lower"]), Decimal(mr["upper"]))
    spent = KAPPA * mass
    available = TARGET - spent
    demand(spent.hi < I.point(SMOOTH_BUDGET).lo, "Rational smoothing budget encloses actual reference loss")
    demand(I.point(SPECTRAL_BUDGET).hi < available.lo, "Rational spectral budget preserves target")
    demand(SMOOTH_BUDGET + SPECTRAL_BUDGET == TARGET, "Original .011 exactly retained")
    fixed_budget = F(1, 1000)
    demand(TARGET - fixed_budget == F(1, 100), "Fixed-power .001 budget leaves .010")
    # Scales: x=N^2, Y~N, T_max=N^(21/10).
    tail_exponent = 4 - 1 - F(21, 10)
    demand(tail_exponent == F(9, 10) and tail_exponent < 1, "Absolute Mellin tail is o(u)")
    return {"original_target": str(TARGET), "kappa": str(KAPPA),
            "original_joint_reference_mass": mr,
            "long_smoothing_cost_enclosure": spent.record(),
            "rational_smoothing_budget": str(SMOOTH_BUDGET),
            "rational_high_frequency_budget": str(SPECTRAL_BUDGET),
            "unrounded_remaining_budget": available.record(),
            "fixed_power_example_budget": str(fixed_budget),
            "fixed_power_remaining_target": str(TARGET - fixed_budget),
            "fixed_power_cutoff_recipe": "A=100*delta0; s=max(128,2*log(max(1,Cprime/(xi*A^2)))); epsilon=A/s",
            "numerical_delta0_or_Cprime_invented": False,
            "high_frequency_upper_truncation_exponent": "21/10",
            "absolute_tail_N_exponent": str(tail_exponent),
            "terminal_0011_estimate_proved": False}


def main():
    check = {
        "date": "2026-10-10", "checkpoint": 23,
        "preservation": preservation(),
        "coefficient_budget": coefficient_budget(),
        "smoothing": smoothing_checks(),
        "original_weight_fixtures": [
            sector_fixture(5000, 8),
            sector_fixture(10000, 8),
            sector_fixture(80000, 16, use_actual_reference=False)
        ],
        "finite_fixture_scope": "Original outer/continuation gates; stress U and one artificial long window are labeled. No finite sample proves an asymptotic estimate."
    }
    (ROOT / "results/joint_signed_comparison_checks.json").write_text(json.dumps(check, indent=2) + "\n")
    result = {
        "date": "2026-10-10", "checkpoint": 23,
        "original_joint_signed_target": "E_(T_N<q<=U)-E_R <= (.011+o(1))*u",
        "cutoff_free_equivalent_target": "Q_all(J)-a*Q_all(B1) <= (.011+o(1))*u",
        "equivalence_scope": "Deduction from checkpoint21 completion and checkpoint22 small-block o(u); not a new proof of the sharp target",
        "actual_shell_prime_cofactor_pointwise_cap": "0<=Q_all({n})<=1_(Pminus(n)>=N^(1/4))",
        "actual_shell_mark_cap_one_proved": True,
        "paired_positive_mellin_smoothing_proved": True,
        "low_mellin_frequency_o_u_from_admitted_long_PNT_proved": True,
        "normalized_smooth_reference_high_frequency_o_u_proved": True,
        "absolute_frequency_tail_beyond_N_21_10_o_u_proved": True,
        "remaining_signed_frequency_range": "exp((c0/4)*sqrt(log N))<|t|<=N^(21/10)",
        "remaining_high_frequency_target": "H_kappa(N) <= (.007935+o(1))*u, kappa=1/1000",
        "original_0011_coefficient_retained": True,
        "coefficient_budget": check["coefficient_budget"],
        "high_frequency_sharp_bound_proved": False,
        "terminal_0011_estimate_proved": False,
        "marked_residual_slice_separate_uniform_u_scale_proved": False,
        "higher_degree_cap_proved": False,
        "H_theta_proved": False, "certified_K": 0,
        "historical_analytic_ledger_unchanged": True
    }
    (ROOT / "results/joint_signed_comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"checkpoint": 23, "historical_records_preserved": 238,
                      "smoothing_budget": str(SMOOTH_BUDGET),
                      "remaining_spectral_budget": str(SPECTRAL_BUDGET),
                      "terminal_0011_estimate_proved": False}))


if __name__ == "__main__":
    main()

