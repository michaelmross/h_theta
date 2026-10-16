#!/usr/bin/env python3
"""Exact finite consistency checks for the two supplied Ross manuscripts.

The general identities are proved in ROSS_GEOMETRY_AUDIT.md. These finite
checks neither prove uniform cancellation nor validate the papers' large
computations. Historical numerical results are read, never rewritten.
"""

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
from itertools import product
from math import isqrt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_HASHES = {
    "sources/ross_square_shells_original.zip":
        "3df0a2191ed4aa81bc2dda72d422087ef2afc71c6c5c96d123b1b5fed2f67bdf",
    "sources/ross_square_shells/main.tex":
        "9a42d1f61f924d0ce3b6dee89b43cd2aafc602ad65a215c0afa463c8137f0d25",
    "sources/ross_factor_rays_original.zip":
        "e8f4bdabddce21908abc56c24ecda4a3df59f8c2e681bbc978a2ccb4a18417f9",
    "sources/ross_factor_rays/main.tex":
        "3c37b0c8a22daf9dec2a597dc5aa90e30bb95b547badd1efd50e948e181ed828",
}
HISTORICAL_LEDGER_HASH = (
    "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def primes_up_to(limit):
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start:limit + 1:p] = b"\x00" * ((limit - start) // p + 1)
    return [p for p in range(2, limit + 1) if flags[p]]


def factor_integer(m, primes):
    factors = {}
    for p in primes:
        if p * p > m:
            break
        exponent = 0
        while m % p == 0:
            m //= p
            exponent += 1
        if exponent:
            factors[p] = exponent
    if m > 1:
        factors[m] = factors.get(m, 0) + 1
    return factors


def factor_band(lo, hi, primes):
    residual = list(range(lo, hi + 1))
    factors = [{} for _ in residual]
    for p in primes:
        if p * p > hi:
            break
        for m in range(((lo + p - 1) // p) * p, hi + 1, p):
            i = m - lo
            exponent = 0
            while residual[i] % p == 0:
                residual[i] //= p
                exponent += 1
            factors[i][p] = exponent
    for i, value in enumerate(residual):
        if value > 1:
            factors[i][value] = 1
    return {lo + i: value for i, value in enumerate(factors)}


def liouville(factors):
    return (-1) ** sum(factors.values())


def squarefree_divisors(primes):
    values = [(1, 1)]
    for p in primes:
        values += [(d * p, -mu) for d, mu in values]
    return values


def rough(factors, n, numerator, denominator):
    return not factors or min(factors) ** denominator >= n ** numerator


def offset_checks():
    records = []
    for p in primes_up_to(43):
        if p == 2:
            continue
        inv16 = pow(16, -1, p)
        center = Counter((-n * n) % p for n in range(0, 2 * p, 2))
        left = Counter((-(n * n - n // 2)) % p
                       for n in range(0, 2 * p, 2))
        for n in range(0, 2 * p, 2):
            r = (-(n * n - n // 2)) % p
            require((16 * r - 1 + (4 * n - 1) ** 2) % p == 0,
                    "Translated offset identity")
        center_expected = Counter((-v * v) % p for v in range(p))
        left_expected = Counter((inv16 - v * v) % p for v in range(p))
        require(center == center_expected, "Center QR multiplicities")
        require(left == left_expected, "Left QR multiplicities")
        require(left[inv16] == 1 and len(left) == (p + 1) // 2,
                "Shifted QR special value")
        for t in range(-10, 11):
            residue = (-t) % p
            character = 0 if residue == 0 else (
                1 if pow(residue, (p - 1) // 2, p) == 1 else -1)
            solutions = sum((n * n + t) % p == 0
                            for n in range(0, 2 * p, 2))
            require(solutions == 1 + character, "Fixed-offset quadratic roots")
        records.append({
            "p": p, "center_counts": dict(sorted(center.items())),
            "left_counts": dict(sorted(left.items())),
            "left_single_preimage_value": inv16,
        })
    q, ps = 105, (3, 5, 7)
    joint = Counter(tuple((-(n * n - n // 2)) % p for p in ps)
                    for n in range(0, 2 * q, 2))
    marginals = [
        Counter((pow(16, -1, p) - v * v) % p for v in range(p))
        for p in ps
    ]
    for vector in product(*(list(c) for c in marginals)):
        multiplicity = 1
        for i, value in enumerate(vector):
            multiplicity *= marginals[i][value]
        require(joint[vector] == multiplicity, "CRT product multiplicity")
    return {"prime_checks": records, "CRT_modulus": q,
            "CRT_period_in_even_N": 2 * q,
            "CRT_observed_vectors": len(joint),
            "all_passed": True,
            "pointwise_prime_cancellation_inferred": False}


def full_model(n, lo, hi, band):
    """Direct exact rational model for small N; includes only odd moduli."""
    primes = primes_up_to(isqrt(hi))
    yodd = sum(m % 2 for m in band)
    model = Fraction(0)
    remainder = Fraction(0)
    count = 0
    for d in range(1, hi + 1, 2):
        factors = factor_integer(d, primes)
        if any(e > 1 for e in factors.values()):
            continue
        if factors and max(factors) > n:
            continue
        mu = (-1) ** len(factors)
        first = ((lo + d - 1) // d) * d
        if first % 2 == 0:
            first += d
        hits = max(0, (hi - first) // (2 * d) + 1)
        density = Fraction(yodd, d)
        model += Fraction(mu, d)
        remainder += mu * (hits - density)
        count += 1
    pi = sum(len(f) == 1 and next(iter(f.values())) == 1
             for m, f in band.items() if m % 2)
    require(yodd * model + remainder == pi, "Exact full-depth model identity")
    shell_tail = Fraction(0)
    for d in range(hi + 1, (n + 1) ** 2):
        if d % 2 == 0:
            continue
        factors = factor_integer(d, primes_up_to(n + 1))
        if any(e > 1 for e in factors.values()):
            continue
        if factors and max(factors) > n:
            continue
        shell_tail += Fraction((-1) ** len(factors), d)
    tail_bound = Fraction((n + 1) ** 2 - 1 - hi, hi)
    require(abs(shell_tail) <= tail_bound, "Centered/shell model cutoff bound")
    return {"odd_positions": yodd, "admissible_moduli": count,
            "truncated_reciprocal": str(model),
            "signed_floor_remainder": str(remainder),
            "ordinary_shell_model_minus_centered_model": str(shell_tail),
            "absolute_cutoff_difference_bound": str(tail_bound),
            "prime_count": pi, "identity_passed": True}


def band_checks(n):
    lo, hi = n * n - n // 2, n * n + n // 2
    primes = primes_up_to(n + 1)
    band = factor_band(lo, hi, primes)
    pi = sum(len(f) == 1 and next(iter(f.values())) == 1
             for f in band.values())
    root = {m for m, f in band.items() if rough(f, n, 1, 4)}
    high = {m for m, f in band.items() if rough(f, n, 19, 20)}
    marked = {
        m for m, f in band.items()
        if min(f) ** 4 >= n and min(f) ** 20 < n ** 19
    }
    require(marked == root - high, "Buchstab first-frontier identity")
    selected_primes = [p for p in primes
                       if p ** 4 >= n and p ** 20 < n ** 19]
    waves = {r: defaultdict(list) for r in (1, 2, 8)}
    frontier_pairs = []
    for p in selected_primes:
        for q in range((lo + p - 1) // p, hi // p + 1):
            fq = factor_integer(q, primes)
            if not fq or min(fq) >= p:
                require(q >= p, "Least-factor orientation")
                frontier_pairs.append((p, q))
                for r in waves:
                    waves[r][q + r * p].append((p, q))
    require(len(frontier_pairs) == len(marked), "Prime-anchored wave count")
    require({p * q for p, q in frontier_pairs} == marked,
            "Prime-anchored wave support")
    for r, blocks in waves.items():
        require(sum(len(v) for v in blocks.values()) == len(marked),
                "No wave multiplicity")
        for s, pairs in blocks.items():
            for p, q in pairs:
                require(s * s - 4 * r * p * q == (q - r * p) ** 2,
                        "Wave discriminant")
    squares = [m for m in band if isqrt(m) ** 2 == m]
    require(squares == [n * n], "Only the central square")
    require(not any(m % 2 for m in squares), "No odd fixed locus")
    difference_of_squares = [
        n * n - a * a for a in range(1, isqrt(n // 2) + 1)
    ]
    for a, m in enumerate(difference_of_squares, start=1):
        require(lo <= m <= hi and m == (n - a) * (n + a),
                "Square-offset composite factorization")
        require(sum(band[m].values()) >= 2, "Square-offset row is composite")
    post = [p for p in primes if p * p > lo]
    require(post == ([n + 1] if n + 1 in primes else []),
            "Post-parabola prime range")
    if post:
        p = n + 1
        hits = [m for m in band if m % p == 0]
        require(hits == [n * n - 1], "Single redundant ray hit")
    for d in (1, 3, 5, 7, 15, 21, 35, 105, n + 1):
        r_d = (-lo) % d
        hits = (n - r_d) // d + 1 if r_d <= n else 0
        require(hits == sum(m % d == 0 for m in band), "Exact offset floor")
        require(abs(Fraction(hits) - Fraction(n + 1, d)) < 1,
                "Untwisted individual floor bound")
        if d % 2:
            require((16 * r_d - 1 + (4 * n - 1) ** 2) % d == 0,
                    "Odd composite-modulus offset identity")

    signed_cutoffs = {}
    for name, a, b in (("base", 1, 4), ("frontier", 19, 20),
                       ("prime_detector", 1, 1)):
        actual = 0
        divisor_sum = 0
        by_range = Counter()
        for m, f in band.items():
            if not m % 2:
                continue
            lam_m = liouville(f)
            if rough(f, n, a, b):
                actual += lam_m
            active = [p for p in f if p ** b < n ** a]
            for d, _ in squarefree_divisors(active):
                lam_q = liouville(factor_integer(m // d, primes))
                divisor_sum += lam_q
                if d <= n:
                    range_name = "d<=N"
                elif d ** 4 <= n ** 5:
                    range_name = "N<d<=N^(5/4)"
                else:
                    range_name = "d>N^(5/4)"
                by_range[range_name] += lam_q
        require(actual == divisor_sum, "Actual-support rough Liouville checksum")
        if name == "prime_detector":
            require(actual == -pi, "Full Liouville checksum is -prime count")
        signed_cutoffs[name] = {
            "rough_signed_sum": actual, "divisor_signed_sum": divisor_sum,
            "signed_divisor_ranges": dict(by_range),
        }
    semiprimes_high = sum(sum(band[m].values()) == 2 for m in high)
    require(len(high) == pi + semiprimes_high, "High-cutoff prime/semiprime split")
    signed_high = signed_cutoffs["frontier"]["rough_signed_sum"]
    require(signed_high == semiprimes_high - pi, "High-cutoff parity split")
    require(len(high) - signed_high == 2 * pi, "Exact two-sign prime recovery")

    odd = [m for m in band if m % 2]
    twist = []
    for d in (1, 3, 5, 7, 15, 21, 35, 105):
        hits = [m for m in odd if m % d == 0]
        original = Fraction(len(hits)) - Fraction(len(odd), d)
        twisted = Fraction(sum(1 + liouville(band[m]) for m in hits))
        twisted -= Fraction(len(odd), d)
        extra = liouville(factor_integer(d, primes)) * sum(
            liouville(factor_integer(m // d, primes)) for m in hits)
        require(twisted == original + extra, "Twist divisor identity")
        twist.append({"d": d, "untwisted_remainder": str(original),
                      "Liouville_extra": extra, "twisted_remainder": str(twisted),
                      "twisted_absolute_remainder_exceeds_one": abs(twisted) > 1})
    total_wave_incidences = 0
    for f in band.values():
        tau = 1
        for exponent in f.values():
            tau *= exponent + 1
        total_wave_incidences += (tau - 1) // 2
    answer = {
        "N": n, "endpoints": [lo, hi], "Y": n + 1,
        "prime_count": pi, "root_rough_count": len(root),
        "R_095": len(marked), "high_rough_count": len(high),
        "high_rough_semiprimes": semiprimes_high,
        "unweighted_ordinary_wave_row_incidences": total_wave_incidences,
        "prime_anchored_wave_counts": {str(r): len(marked) for r in waves},
        "weighted_wave_indices_used": {str(r): len(w) for r, w in waves.items()},
        "max_rp_over_q": {
            str(r): str(max((Fraction(r * p, q) for p, q in frontier_pairs),
                           default=Fraction(0)))
            for r in waves
        },
        "post_parabola_primes": post, "squares": squares,
        "difference_of_squares_rows": len(difference_of_squares),
        "odd_difference_of_squares_rows": sum(m % 2 for m in difference_of_squares),
        "Liouville_cutoffs": signed_cutoffs,
        "actual_twist_divisor_examples": twist, "all_checks_passed": True,
    }
    if n <= 120:
        answer["full_depth_odd_model"] = full_model(n, lo, hi, band)
    return answer


def main():
    sources = []
    for relative, expected in SOURCE_HASHES.items():
        path = ROOT / relative
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == expected, "Supplied source hash mismatch")
        sources.append({"path": relative, "size_bytes": path.stat().st_size,
                        "sha256": digest})
    ledger = ROOT / "results/negative_frontier_ledger.json"
    require(hashlib.sha256(ledger.read_bytes()).hexdigest() == HISTORICAL_LEDGER_HASH,
            "Historical ledger changed")
    cases = [band_checks(n) for n in (20, 40, 80, 120, 200, 400, 1000, 2000, 10000)]
    require(any(t["twisted_absolute_remainder_exceeds_one"]
                for c in cases for t in c["actual_twist_divisor_examples"]),
            "Missing concrete qualification of the twist remainder")
    result = {
        "date": "2026-10-06", "checkpoint": 8, "supplied_sources": sources,
        "source_reading": "Both supplied main.tex files read; source identities recorded",
        "not_reproduced": [
            "The authors' dense shell scans and exact samples through 10^9",
            "Complete-wave FFT covariance tables; the referenced scripts/CSV are not in these ZIPs",
        ],
        "square_offset_checks": offset_checks(), "finite_band_checks": cases,
        "cutoff_method": "Exact integer powers; no floating cutoff rounding",
        "finite_checks_prove_uniform_estimates": False,
        "general_proofs": "ROSS_GEOMETRY_AUDIT.md",
        "new_arithmetic_estimate_admitted": False,
        "centered_frontier_allowed_excess": "0.338",
        "centered_frontier_estimate_proved": False,
        "certified_K": 0, "H_theta_proved": False,
        "historical_ledger_sha256": HISTORICAL_LEDGER_HASH,
    }
    destination = ROOT / "results/ross_geometry_audit.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    state_path = ROOT / "results/campaign_state.json"
    state = json.loads(state_path.read_text())
    state.update({
        "checkpoint": 8,
        "latest_investigation_note": "ROSS_GEOMETRY_AUDIT.md",
        "ross_geometry_audit": "results/ross_geometry_audit.json",
        "ross_papers_integrated": [
            "Multiplication Geometry in Square Shells",
            "Factor Rays and the Self-Conjugate Parabola",
        ],
        "ross_geometry_status": (
            "Exact centered offsets, truncated model transfer, prime-anchored "
            "wave rewrite and actual-support Liouville checksum; no new "
            "restricted-frontier estimate"
        ),
        "new_arithmetic_estimate_from_ross_papers": False,
        "numerical_bounds_changed_in_checkpoint8": False,
        "lower_bound_status": (
            "K=0; exact geometry and actual-support parity diagnostics added; "
            "centered frontier estimate remains unproved"
        ),
    })
    state["milestones"]["4"] = (
        "FI Theorems 1-7 interfaces and supplied Ross geometry/parity bridges "
        "checked; full tool inventory incomplete"
    )
    state["milestones"]["6"] = (
        "Long-carrier witness preserved; actual-interval Liouville check and "
        "twisted-error qualification supplied; arithmetic comparison still needed"
    )
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "source_hashes_passed": len(sources),
        "exact_band_cases_passed": len(cases),
        "prime_anchored_wave_weights_checked": [1, 2, 8],
        "actual_support_Liouville_checks_passed": True,
        "twist_remainder_qualification_observed": True,
        "historical_ledger_unchanged": True, "certified_K": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
