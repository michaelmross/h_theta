#!/usr/bin/env python3
"""Checkpoint 33: exact checks for the dyadic variance test.

The note proves a uniform O bound, not the required little-o estimate.
The sampled-norm example is a function-space construction, not prime data.
Historical mathematical files and results are never rewritten here.
"""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json

from short_scale_localization import selberg_weights
from ross_geometry_audit import primes_up_to

ROOT = Path(__file__).resolve().parents[1]
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}


def demand(condition, message):
    if not condition:
        raise AssertionError(message)


def power_checks():
    vertices = [(F(2, 5), F(2, 5)), (F(43, 100), F(43, 100)),
                (F(43, 100), F(157, 300)), (F(2, 5), F(8, 15))]
    rows = []
    for a, b in vertices:
        sigma = a + b
        gamma = 1 - sigma
        rows.append({"a": str(a), "b": str(b), "pair_exponent": str(sigma),
                     "window_exponent": str(gamma),
                     "residual_window_fraction": str(gamma / (1 + gamma)),
                     "roughness_minus_sieve_radius": str(b - gamma / 4),
                     "diagonal_ratio_power": str(sigma - 1),
                     "Selberg_error_relative_power": str(-gamma / 2)})
    count = 0
    for k in range(41):
        a = F(2, 5) + F(k, 40) * F(3, 100)
        for t in range(41):
            b = a + F(t, 40) * ((2 - a) / 3 - a)
            sigma, gamma = a + b, 1 - a - b
            demand(F(4, 5) <= sigma <= F(143, 150), "Pair exponent range")
            demand(F(7, 150) <= gamma <= F(1, 5), "Window power margin")
            demand(b - gamma / 4 >= F(7, 20), "Selberg radius below roughness")
            demand(sigma - 1 <= -F(7, 150), "Uniform diagonal ratio power")
            demand(-gamma / 2 <= -F(7, 300), "Uniform Selberg remainder power")
            theta = gamma / (1 + gamma)
            demand(F(7, 157) <= theta <= F(1, 6), "Residual interval exponent")
            count += 1
    # The vertex proof handles the continuous affine inequalities; the ratio
    # gamma/(1+gamma) is increasing. The grid is supplementary only.
    return {"vertices": rows, "rational_grid_rows": count,
            "continuous_affine_extrema_certified_at_vertices": True,
            "interior_example": {"a": "83/200", "b": "23/50",
                                 "pair": "7/8", "window": "1/8",
                                 "a_plus_3b": "359/200"}}


def interval_sieve_checks():
    records = []
    for radius in (3, 5, 8, 13):
        _, _, norm, _, weights = selberg_weights(radius)
        length = radius ** 4
        start = 10 ** 12 + 17
        actual = F(0)
        for d, ad in weights.items():
            for e, ae in weights.items():
                modulus = lcm(d, e)
                multiples = (start + length) // modulus - start // modulus
                actual += ad * ae * multiples
        main = F(length) / norm
        floor_error = sum((abs(v) for v in weights.values()), F(0)) ** 2
        primorial = 1
        for p in primes_up_to(radius):
            primorial *= p
        rough_proxy = sum(gcd(n, primorial) == 1
                          for n in range(start + 1, start + length + 1))
        demand(rough_proxy <= actual, "Actual interval square majorant")
        demand(abs(actual - main) <= floor_error, "Exact signed floor remainder")
        records.append({"radius": radius, "length": length,
                        "rough_proxy_count": rough_proxy,
                        "Selberg_square": str(actual),
                        "main_term": str(main), "floor_error_bound": str(floor_error)})
    return {"intervals": records,
            "uses_existing_checkpoint25_weights": True,
            "new_little_o_prime_variance_verified": False}


def sampled_norm_check():
    # A finite exact geometry instance using actual, small certified primes.
    # It verifies a functional norm example, not their semiprime residuals.
    N, P, R = 2 ** 40, 2 ** 16, 2 ** 18
    Y, M, x = N + 1, P * R, N * N
    primes = primes_up_to(2 * R)
    ps = [p for p in primes if P <= p < 2 * P][:4]
    rs = [r for r in primes if R <= r < 2 * R][:4]
    products = sorted(p * r for p in ps for r in rs)
    demand(len(set(products)) == 16, "Unique sorted prime-pair products")
    for p in ps:
        demand(P <= p < 2 * P, "First dyadic gate")
        demand(p ** 5 >= N ** 2, "Original p lower gate")
        demand(p ** 100 <= N ** 43, "Original p upper gate")
        for r in rs:
            demand(p < r and p * r ** 3 < x, "Sorted pair and residual volume")
    h, B = F(Y, M), F(x, M)
    centers = sorted(F(x, m) for m in products)
    demand(all(v - u > 2 * h for u, v in zip(centers, centers[1:])),
           "Disjoint h-neighborhoods")
    demand(all(v - u >= F(x, 16 * M * M)
               for u, v in zip(centers, centers[1:])), "Reciprocal spacing")
    left, right = B / 8, 2 * B
    demand(centers[0] - h > left and centers[-1] + h < right, "Interior bump support")
    span, count = right - left, len(centers)
    offset = count * h / span  # Unit bump amplitude; h/log N is restored analytically.
    integral = -count * h + offset * span
    square_integral = F(2, 3) * count * h - (count * h) ** 2 / span
    sampled_square = count * (1 - offset) ** 2
    demand(integral == 0, "Exact zero long mean")
    demand(square_integral > 0, "Positive continuous squared norm")
    demand(offset < F(1, 100), "Negligible mean correction")
    demand(sampled_square >= F(9, 10) * count, "Large sampled norm after centering")
    # Independently integrate the piecewise-linear tent square and the
    # constant offset over each tent plus its complement.
    tent_part = count * (F(2, 3) * h - 2 * offset * h + 2 * h * offset ** 2)
    complement = (span - 2 * count * h) * offset ** 2
    demand(tent_part + complement == square_integral, "Independent exact norm integral")
    return {"N": N, "P": P, "R": R, "sampled_prime_pairs": count,
            "h": str(h), "interval_length": str(span), "offset": str(offset),
            "long_integral": str(integral),
            "continuous_squared_norm_unit_amplitude": str(square_integral),
            "sampled_squared_norm_unit_amplitude": str(sampled_square),
            "all_center_to_sample_transfer_counterexample_only": True,
            "actual_prime_pair_count_counterexample": False}


def preservation():
    raw = (ROOT / "results/checkpoint32_preservation_manifest.json").read_bytes()
    previous = json.loads(raw)
    demand(previous["checkpoint"] == 32, "Frozen checkpoint 32")
    count = 0
    for rec in previous["files"]:
        if rec["path"] in MUTABLE:
            continue
        data = (ROOT / rec["path"]).read_bytes()
        demand(len(data) == rec["size_bytes"] and sha256(data).hexdigest() == rec["sha256"],
               "Historical preservation: " + rec["path"])
        count += 1
    demand(count == 311, "Every nonmutable checkpoint-32 record preserved")
    return {"checkpoint32_nonmutable_records_verified": count,
            "checkpoint32_manifest_sha256": sha256(raw).hexdigest()}


def main():
    checks = {"checkpoint": 33, "date": "2026-10-14",
              "power_geometry": power_checks(),
              "interval_Selberg": interval_sieve_checks(),
              "sampled_norm": sampled_norm_check(),
              "preservation": preservation(), "all_exact_checks_passed": True,
              "actual_little_o_variance_verified": False}
    result = {"checkpoint": 33, "proof_note": "DYADIC_VARIANCE_TEST_NOTE.md",
              "block_variance_O_scale_proved": True,
              "block_variance_upper_scale": "O_j(N^2/(PR*(log N)^4))",
              "block_variance_little_o_proved": False,
              "local_diagonal_upper": "O_j(N/(log N)^3)",
              "local_diagonal_uniformly_negligible_at_target_scale": True,
              "required_uniform_off_diagonal_little_o_proved": False,
              "all_center_log_saving_automatic_transfer_valid": False,
              "functional_model_is_actual_prime_counterexample": False,
              "original_masks_gates_and_five_moments_retained": True,
              "actual_deficit_coefficient_improved": False,
              "new_nonvanishing_error_charge": "0",
              "comparison_plus_rest_budget": ".000099",
              "original_allowance": ".011", "spectral_allowance": ".007935",
              "sharp_short_window_inequality_proved": False,
              "H_theta_proved": False, "certified_K": 0,
              "any_global_impossibility_claim": False}
    for name, obj in (("dyadic_variance_test_checks.json", checks),
                      ("dyadic_variance_test.json", result)):
        (ROOT / "results" / name).write_text(json.dumps(obj, indent=2) + "\n")
    print(json.dumps({"exact_checks_passed": True,
                      "grid_rows": checks["power_geometry"]["rational_grid_rows"],
                      "interval_sieve_fixtures": len(checks["interval_Selberg"]["intervals"]),
                      "sampled_norm_pairs": checks["sampled_norm"]["sampled_prime_pairs"],
                      "preserved_records": checks["preservation"]["checkpoint32_nonmutable_records_verified"],
                      "sharp_estimate_proved": False}))


if __name__ == "__main__":
    main()
