#!/usr/bin/env python3
"""Checkpoint 25: local Selberg envelopes and a centered short-scale tail.

Uniform analytic proofs are in SHORT_SCALE_LOCALIZATION_NOTE.md.
Exact finite checks and rounding certificates do not prove the .007935
central signed estimate or the .0686138 coupled estimate.
Historical modules/results are read without rewriting them.
"""
from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt, lcm
from pathlib import Path
import json

from joint_signed_comparison import prime_cofactor_marks, psi
from ross_geometry_audit import factor_band, primes_up_to

ROOT = Path(__file__).resolve().parents[1]
KAPPA = F(1, 1000)
ALPHA = F(1, 2) + KAPPA
AREA_RATIO = 1 + ALPHA
BUDGET = F(1587, 200000)
SMOOTH = F(613, 200000)
TAIL = 21147
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}


def demand(condition, label):
    if not condition:
        raise AssertionError(label)


def decimal_enclosure(value, places=45):
    """Outward decimals for one exact rational."""
    scale = 10 ** places
    low = value.numerator * scale // value.denominator
    high = -((-value.numerator * scale) // value.denominator)
    with localcontext() as ctx:
        ctx.prec = places + 30
        return {"lower": str(Decimal(low) / Decimal(scale)),
                "upper": str(Decimal(high) / Decimal(scale))}


def preservation():
    raw = (ROOT / "results/checkpoint24_preservation_manifest.json").read_bytes()
    previous = json.loads(raw)
    demand(previous["checkpoint"] == 24, "Frozen checkpoint 24")
    count = 0
    for rec in previous["files"]:
        if rec["path"] in MUTABLE:
            continue
        data = (ROOT / rec["path"]).read_bytes()
        demand(len(data) == rec["size_bytes"]
               and sha256(data).hexdigest() == rec["sha256"],
               "Historical preservation: " + rec["path"])
        count += 1
    ledger = sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
    demand(ledger == "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
           "Frozen historical mass ledger")
    return {"checkpoint24_nonmutable_records_verified": count,
            "checkpoint24_manifest_sha256": sha256(raw).hexdigest(),
            "negative_frontier_ledger_sha256": ledger}


def arithmetic(limit):
    """Independent elementary table of Mobius and Euler-phi coefficients."""
    mu, phi = [0] * (limit + 1), [0] * (limit + 1)
    mu[1] = phi[1] = 1
    for n in range(2, limit + 1):
        m, p, distinct, square, ph = n, 2, 0, False, n
        while p * p <= m:
            if m % p == 0:
                exponent = 0
                while m % p == 0:
                    m //= p
                    exponent += 1
                distinct += 1
                square |= exponent > 1
                ph = ph // p * (p - 1)
            p += 1
        if m > 1:
            distinct += 1
            ph = ph // m * (m - 1)
        mu[n] = 0 if square else (-1) ** distinct
        phi[n] = ph
    return mu, phi


def selberg_weights(radius):
    mu, phi = arithmetic(radius)
    norm = sum((F(mu[r] ** 2, phi[r]) for r in range(1, radius + 1)), F(0))
    y = {r: F(mu[r], phi[r]) / norm for r in range(1, radius + 1) if mu[r]}
    weights = {
        d: d * sum((mu[r // d] * yr for r, yr in y.items() if r % d == 0), F(0))
        for d in range(1, radius + 1)
    }
    demand(weights[1] == 1, "Selberg lambda_1")
    for d, value in weights.items():
        demand(abs(value) <= F(d, phi[d]), "Selberg divisor coefficient bound")
        demand(mu[d] != 0 or value == 0, "Squarefree support")
    return mu, phi, norm, y, weights


def selberg_checks():
    records, pair_checks, inversion_checks = [], 0, 0
    for radius in (1, 2, 8, 17, 37, 100, 257):
        mu, phi, norm, y, weights = selberg_weights(radius)
        for r in range(1, radius + 1):
            row = sum((v / d for d, v in weights.items() if d % r == 0), F(0))
            demand(row == y.get(r, 0), "Independent Mobius inversion")
            inversion_checks += 1
        quad = F(0)
        for d, ad in weights.items():
            for e, ae in weights.items():
                quad += ad * ae / lcm(d, e)
                pair_checks += 1
        diagonal = sum((phi[r] * yr ** 2 for r, yr in y.items()), F(0))
        demand(quad == diagonal == 1 / norm, "Exact optimized Selberg quadratic form")
        # Independently check the Dirichlet-convolution normalization g=(1/n)*h.
        def h_coeff(n):
            result, remaining, p = F(1), n, 2
            while p * p <= remaining:
                exponent = 0
                while remaining % p == 0:
                    remaining //= p
                    exponent += 1
                if exponent:
                    if exponent >= 3:
                        return F(0)
                    result *= F(1 if exponent == 1 else -1, p * (p - 1))
                p += 1
            if remaining > 1:
                result *= F(1, remaining * (remaining - 1))
            return result
        for n in range(1, radius + 1):
            conv = sum((h_coeff(d) / (n // d) for d in range(1, n + 1)
                        if n % d == 0), F(0))
            demand(conv == F(mu[n] ** 2, phi[n]), "Selberg norm convolution")
        records.append({"R": radius, "G_R": str(norm),
                        "quadratic_minimum": str(quad),
                        "nonzero_weights": sum(v != 0 for v in weights.values())})
    return {"radii": records, "quadratic_pair_checks": pair_checks,
            "mobius_inversion_rows": inversion_checks,
            "all_exact_checks_passed": True}


def smootherstep(s):
    return 10 * s ** 3 - 15 * s ** 4 + 6 * s ** 5


def chi(value, x, y):
    offset = abs(F(value) - x)
    if offset <= ALPHA * y:
        return F(1)
    if offset >= y:
        return F(0)
    return smootherstep((y - offset) / ((1 - ALPHA) * y))


def shape_and_lattice_checks():
    integral_h = F(10, 4) - F(15, 5) + F(6, 6)
    demand(integral_h == F(1, 2), "Exact polynomial taper area")
    area = 2 * ALPHA + 2 * (1 - ALPHA) * integral_h
    demand(area == AREA_RATIO == F(1501, 1000), "Local cutoff area")
    for s in (F(0), F(1)):
        demand(30 * s ** 2 - 60 * s ** 3 + 30 * s ** 4 == 0,
               "C1 matching")
        demand(60 * s - 180 * s ** 2 + 120 * s ** 3 == 0,
               "C2 matching")
    rows = 0
    for n in (62, 100, 1000):
        x, y = n * n, n + 1
        for divisor in range(1, 258):
            values = range((x - y + divisor - 1) // divisor,
                           (x + y) // divisor + 1)
            actual = sum((chi(k * divisor, x, y) for k in values), F(0))
            model = AREA_RATIO * F(y, divisor)
            demand(abs(actual - model) <= 2, "Independent bounded-variation lattice envelope")
            rows += 1
        for value in range(x - y, x + y + 1):
            weight = psi(value, x, y)
            demand(chi(value, x, y) * weight == weight,
                   "Exact local cutoff on every smoothed counted row")
    # Check the expanded Selberg square with both signed off-diagonal terms.
    n, radius = 100, 17
    x, y = n * n, n + 1
    _, _, norm, _, weights = selberg_weights(radius)
    actual_square = F(0)
    rough_mass = F(0)
    small_primes = primes_up_to(radius)
    for value in range(x - y, x + y + 1):
        weight = chi(value, x, y)
        divisor_sum = sum((ad for d, ad in weights.items() if value % d == 0), F(0))
        actual_square += weight * divisor_sum ** 2
        if all(value % p for p in small_primes):
            rough_mass += weight
            demand(divisor_sum == 1, "Pointwise square majorant on rough rows")
    main = AREA_RATIO * y / norm
    error = 2 * sum(abs(a) for a in weights.values()) ** 2
    demand(rough_mass <= actual_square, "Nonnegative Selberg upper envelope")
    demand(abs(actual_square - main) <= error, "Full signed quadratic lattice remainder")
    return {"independent_lattice_rows": rows,
            "local_area_over_Y": str(area),
            "total_variation": 2,
            "signed_quadratic_fixture": {"N": n, "R": radius,
                "actual_square": str(actual_square), "main_term": str(main),
                "absolute_lattice_error_bound": str(error)},
            "finite_fixtures_are_not_uniform_prime_estimates": True}


def narrow_mark_checks():
    records, sites, repeated = [], 0, 0
    for n in (62, 100, 200, 1000, 10000):
        x, y = n * n, n + 1
        factors = factor_band(x - y, x + y, primes_up_to(isqrt(x + y)))
        largest, count = F(0), 0
        for value, fs in factors.items():
            mark, _ = prime_cofactor_marks(value, fs, n)
            demand(0 <= mark <= 1, "Unique mark in local padding")
            if mark:
                demand(all(p ** 4 >= n for p in fs), "Actual rough indicator")
                count += 1
                repeated += any(exponent > 1 for exponent in fs.values())
            largest = max(largest, mark)
            sites += 1
        records.append({"N": n, "sites": len(factors), "marked_sites": count,
                        "maximum_mark": str(largest)})
    # Certificate for the inequalities used in the uniform proof, not a sample
    # extrapolation. N>=2^16 ensures z>=16 and N^(1/10)>=2.
    n0 = 2 ** 16
    demand(n0 >= 2 ** 10, "N^(1/10)>=2")
    demand(n0 * n0 - (n0 + 1) > F(n0 * n0, 2), "x-Y>x/2")
    demand(16 * F(1, 2) > 4, "z*(x-Y)>Y^2 using Y<=2N")
    witness_n, witness = 62, 11 * 13 * 17
    demand(abs(witness - witness_n ** 2) > witness_n + 1,
           "Previous three-mark witness excluded by specified short support")
    return {"cases": records, "sites": sites, "marked_repeated_factor_rows": repeated,
            "uniform_analytic_cap_threshold": n0,
            "broad_support_cap_one_claimed": False}


def arctan_bounds(q, even_terms):
    demand(even_terms % 2 == 0, "Alternating-series lower partial sum")
    lower = sum((F((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
                 for k in range(even_terms)), F(0))
    upper = lower + F(1, (2 * even_terms + 1) * q ** (2 * even_terms + 1))
    return lower, upper


def coefficient_certificates():
    # Exact tangent arithmetic proves Machin's angle identity; the positive
    # angle is pi/4 since it lies in (0,pi/2) and has tangent one.
    tangent = F(1, 5)
    tangent = 2 * tangent / (1 - tangent ** 2)
    tangent = 2 * tangent / (1 - tangent ** 2)
    tangent = (tangent - F(1, 239)) / (1 + tangent * F(1, 239))
    demand(tangent == 1, "Machin tangent identity")
    a_lo, a_hi = arctan_bounds(5, 20)
    b_lo, b_hi = arctan_bounds(239, 4)
    demand(0 < 4 * a_lo - b_hi < 4 * a_hi - b_lo < 1,
           "Machin angle lies in (0,1), inside (0,pi/2)")
    pi_lo, pi_hi = 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo
    demand(F(314159, 100000) < pi_lo < pi_hi < F(314160, 100000),
           "Certified rational pi enclosure")
    full = json.loads((ROOT / "results/two_three_reference_and_samples.json").read_text())[
        "joint_reference_mass"]
    core = json.loads((ROOT / "results/spectral_coverage_reference.json").read_text())[
        "auxiliary_core_reference"]
    m_lo, m_hi = F(full["lower"]), F(full["upper"])
    c_lo, c_hi = F(core["lower"]), F(core["upper"])
    local_upper = 8 * AREA_RATIO
    density_upper = AREA_RATIO * m_hi
    tail_upper = 4 * (local_upper + density_upper) / (KAPPA * pi_lo)
    demand(tail_upper < F(21146634266, 1000000) < TAIL,
           "Outward absolute-tail coefficient")
    signed_upper = (1 + KAPPA) * (8 - m_lo)
    coupled_upper = (1 + KAPPA) * (8 - m_lo + c_hi)
    demand(signed_upper < F(2470001, 500000), "Signed coefficient rounds up to 4.940002")
    demand(coupled_upper < F(2500357, 500000), "Coupled coefficient rounds up to 5.000714")
    sufficient_core_rhs = (1 + KAPPA) * c_lo + BUDGET
    demand(F(343069, 5000000) < sufficient_core_rhs, "Original .0686138 remains sufficient")
    fixed_l = 100_000_000
    fixed_tail = F(TAIL, fixed_l)
    fixed_central = BUDGET - fixed_tail
    demand(SMOOTH + fixed_tail + fixed_central == F(11, 1000), "Fixed multiplier ledger")
    demand(fixed_central == F(772353, 100000000), ".00772353 central example")
    xi = F(1, 1000)
    demand(SMOOTH + fixed_tail + xi + (fixed_central - xi) == F(11, 1000),
           "Separate fixed-power least-prime budget remains charged")
    return {
        "pi_certificate": {"machin_identity": "pi=16*atan(1/5)-4*atan(1/239)",
                           "bounds": decimal_enclosure(pi_lo) | {
                               "upper": decimal_enclosure(pi_hi)["upper"]}},
        "full_reference_enclosure": full,
        "auxiliary_core_reference_enclosure": core,
        "local_cutoff_area_over_Y": str(AREA_RATIO),
        "local_actual_mass_upper_coefficient": str(local_upper),
        "local_density_mass_upper_coefficient": decimal_enclosure(density_upper),
        "asymptotic_tail_constant_upper": decimal_enclosure(tail_upper),
        "uniform_eventual_tail_constant": TAIL,
        "tail_cutoff": "L*x/Y",
        "tail_upper": "(21147/L)*u for sufficiently large even N, uniformly L>=1",
        "original_spectral_allowance": str(BUDGET),
        "signed_Selberg_upper": decimal_enclosure(signed_upper),
        "upward_rounded_signed_coefficient": "4.940002",
        "actual_coupled_Selberg_upper": decimal_enclosure(coupled_upper),
        "upward_rounded_coupled_coefficient": "5.000714",
        "required_sufficient_coupled_coefficient_unchanged": ".0686138",
        "fixed_multiplier_example": {"L": fixed_l, "tail": str(fixed_tail),
                                      "central": str(fixed_central),
                                      "smoothing": str(SMOOTH),
                                      "total": "11/1000"},
        "fixed_least_prime_budget_if_used": "xi from checkpoint22 (23)",
        "growing_L_nonvanishing_coefficient_charge": "0",
        "sharp_spectral_bound_proved": False,
        "sharp_coupled_bound_proved": False}


def status_record():
    return {
        "checkpoint": 25, "date": "2026-10-11",
        "proof_note": "SHORT_SCALE_LOCALIZATION_NOTE.md",
        "short_padding_unique_mark": "|n-N^2|<=N+1, even N>=2^16",
        "new_transform": "Actual short-localized prime marks minus localized long-reference density",
        "new_signed_interface": "H_original=(1/pi)*Re integral_[T0,(x/Y)*log N] Phi_N(t)*psi_Y_hat(1+it) dt+o(u)",
        "general_growing_upper_limit": "L_N*x/Y for any L_N->infinity",
        "comparison_uses_original_reference": True,
        "earlier_individual_frequency_bands_declared_negligible": False,
        "uniform_abs_tail_above_N_log_N_proved": True,
        "low_local_centered_frequencies": "o(u) absolutely",
        "new_nonvanishing_coefficient_charge": "0",
        "central_signed_coefficient_required": ".007935",
        "central_signed_coefficient_proved": False,
        "actual_coupled_conservative_upper_coefficient": "5.000714",
        "actual_coupled_sharp_upper_coefficient_required": ".0686138",
        "actual_coupled_sharp_upper_coefficient_proved": False,
        "least_prime_sector_discarded": False,
        "original_Vaughan_and_auxiliary_cutoffs_changed": False,
        "terminal_0011_estimate_proved": False,
        "H_theta_proved": False, "certified_K": 0}


def main():
    checks = {
        "preservation": preservation(),
        "selberg": selberg_checks(),
        "shape_and_lattice": shape_and_lattice_checks(),
        "narrow_marks": narrow_mark_checks(),
        "all_exact_checks_passed": True,
        "finite_checks_prove_sharp_target": False}
    coefficients = coefficient_certificates()
    for name, data in (("short_scale_localization_checks.json", checks),
                       ("short_scale_localization_coefficients.json", coefficients),
                       ("short_scale_localization.json", status_record())):
        (ROOT / "results" / name).write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({
        "all_exact_checks_passed": True,
        "preserved_records": checks["preservation"]["checkpoint24_nonmutable_records_verified"],
        "selberg_quadratic_pairs": checks["selberg"]["quadratic_pair_checks"],
        "lattice_rows": checks["shape_and_lattice"]["independent_lattice_rows"],
        "local_mark_sites": checks["narrow_marks"]["sites"],
        "tail_constant_upper": coefficients["asymptotic_tail_constant_upper"],
        "tail_cutoff": "(x/Y)*log N",
        "conservative_coupled_coefficient": "5.000714",
        "sharp_target_proved": False}, indent=2), flush=True)


if __name__ == "__main__":
    main()
