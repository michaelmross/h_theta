"""Exact checks supporting the scoped 021 manuscript audit.

These checks certify arithmetic margins and translation/completion identities.
They do not prove the analytic theorem or replay its Lean formalization.
Run from the campaign directory: python3 src/openai021_audit.py
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rational(value: F) -> dict:
    return {"exact": str(value), "decimal_display": float(value)}


def reference_margins() -> dict:
    b = F(693147180559946, 10**15)
    log_lower = sum((F(2, (2*j+1)*3**(2*j+1)) for j in range(16)), F(0))
    log_upper = log_lower + F(2, 33*3**33) / (1-F(1, 9))
    assert F(69, 100) < log_lower < log_upper < b
    # gamma <= H_6-log(6), and this explicit partial series bounds log(6) below.
    log6_lower = 2*sum((F(5, 7)**(2*j+1)/F(2*j+1) for j in range(32)), F(0))
    gamma_upper = sum((F(1, j) for j in range(1, 7)), F(0))-log6_lower
    assert gamma_upper < F(66, 100)
    v = F(66, 100)
    exp_upper = sum((v**j/F(math.factorial(j)) for j in range(15)), F(0))
    exp_upper += v**15/F(math.factorial(15))/(1-v/16)
    assert exp_upper < F(195, 100)

    def term(m: int) -> F:
        return F((m+1)**2, 2*math.factorial(m)) * (
            (1-F(1, m))*b**(m-2) + F(3, 2*m)*b**(m-1))

    ratio = F(225, 2744)*b
    assert 0 < ratio < 1
    j_b = F(517, 432)-F(17, 12)*b+F(2, 3)*b*b
    sharp = j_b-sum((term(m) for m in range(4, 13)), F(0))-term(13)/(1-ratio)
    assert sharp > F(222979373, 10**9)
    coarse = F(8, 3)-1-F(66, 100)-F(52, 100)-F(34, 100)
    assert coarse > F(14, 100)
    root = -F(1, 100)+F(28, 100)/(4*F(195, 100))
    assert root > F(2, 100)
    # A <= 3.9, and log(1+t) <= t-t^2/2+t^3/3 for t=0.18.
    t = F(18, 100)
    f_upper = F(39, 10)*(t-t*t/2+t*t*t/3)/F(218, 100)
    assert f_upper < F(30, 100)
    stopped = F(94, 100)*F(95, 100)/(F(219, 100)+F(2, 100))
    assert stopped > F(39, 100)
    assert F(34, 100) > F(33, 100)
    return {
        "log2_upper_series_bound": rational(log_upper),
        "log2_decimal_upper": rational(b),
        "gamma_upper": rational(gamma_upper),
        "exp_at_0_66_upper": rational(exp_upper),
        "correction_integral_rational_lower": rational(sharp),
        "published_sharp_margin": rational(sharp-F(222979373, 10**9)),
        "coarse_correction_integral_lower": rational(coarse),
        "coarse_scaled_reference_lower": rational(root),
        "f_at_2_18_upper": rational(f_upper),
        "stop_family_lower_coefficient_before_rounding": rational(stopped),
        "stop_after_missing_primes_minus_reference": rational(F(1, 100)),
    }


def crt_translations() -> dict:
    primes = (2, 3, 5)
    modulus = math.prod(primes)
    arbitrary_rows = 0
    translation_rows = 0
    for classes in itertools.product(*(range(p) for p in primes)):
        b = next(n for n in range(modulus) if all(n % p == a for p, a in zip(primes, classes)))
        for n in range(-73, 84):
            avoided = all(n % p != a for p, a in zip(primes, classes))
            assert avoided == (math.gcd(n-b, modulus) == 1)
            arbitrary_rows += 1
    for start in (-1007, -73, -1, 0, 1, 73, 1007):
        classes = [(1-start) % p for p in primes]
        for j in range(1, 92):
            avoided = all(j % p != a for p, a in zip(primes, classes))
            assert avoided == (math.gcd(start+j-1, modulus) == 1)
            translation_rows += 1
    return {"arbitrary_class_rows": arbitrary_rows, "signed_translation_rows": translation_rows}


def restricted_hyperbola_completion() -> dict:
    """Check the exact residue decomposition with full interval multiplicities."""
    cases = 0
    pairs = 0
    long_intervals = 0
    negative_translations = 0
    for h, t0 in ((4, 1), (4, 2), (6, 6), (8, 2), (10, 10), (12, 6), (18, 6)):
        n = h*t0
        t1 = next(t for t in (3, 5, 7, 11) if math.gcd(t, n) == 1)
        units = [a for a in range(n) if math.gcd(a, n) == 1]
        for c0 in (1, -1, h+1):
            assert math.gcd(c0, h) == 1
            for k0 in (0, t0-1):
                c = (c0+h*k0) % n
                for l in (1, next(v for v in (2, 3, 5, 7, 11, 13) if math.gcd(v, h*t1) == 1)):
                    for a0 in (1 % t0, (-1) % t0):
                        for lo, hi, mlo, mhi in ((-n-2, 2*n+5, -3, n+7),
                                                  (1, n//2+1, -n, 2*n+1),
                                                  (-5, 2, 1, 6)):
                            p1, m1 = 1 % t1, 2 % t1
                            direct = 0
                            for p in range(lo, hi+1):
                                if p % l or p % t0 != a0 or p % t1 != p1:
                                    continue
                                for m in range(mlo, mhi+1):
                                    if m % t1 == m1 and (p*m-c) % n == 0:
                                        direct += 1
                            ac = [0]*n
                            bc = [0]*n
                            for p in range(lo, hi+1):
                                if p % l == 0 and p % t1 == p1:
                                    ac[(p//l) % n] += 1
                            for m in range(mlo, mhi+1):
                                if m % t1 == m1:
                                    bc[m % n] += 1
                            a0_changed = (a0*pow(l, -1, t0)) % t0 if t0 > 1 else 0
                            cp = c*pow(l, -1, n) % n
                            completed = sum(ac[v]*bc[(cp*pow(v, -1, n)) % n]
                                            for v in units if v % t0 == a0_changed)
                            assert direct == completed, (h, t0, t1, c0, k0, l, lo, hi)
                            assert sum(v % t0 == a0_changed for v in units) == len(units)//sum(
                                math.gcd(v, t0) == 1 for v in range(t0))
                            cases += 1
                            pairs += direct
                            long_intervals += (hi-lo > n or mhi-mlo > n)
                            negative_translations += (lo < 0 or mlo < 0)
    return {"cases": cases, "solutions": pairs, "long_interval_cases": long_intervals,
            "negative_translation_cases": negative_translations,
            "scope": "exact decomposition only; no test of Weil's analytic bound"}


def shell_geometry() -> dict:
    # For T=log N >= 8, T/2 <= L <= 5T/8 follows from
    # 0 <= log(T/4) <= T/8 (differentiate; check T=8 with log 2 < 1).
    # Hence 4N/25-1 <= floor(z^2/L^2) <= N/4, z=(sqrt N)*T/4.
    length_lower = F(4, 25)
    length_upper = F(1, 4)
    four_factor_ratio_lower = F(8**4, 4**4)
    assert four_factor_ratio_lower > F(5, 4)  # J upper/N^2 <= 5/4 for N>=2.
    assert length_lower-F(1, 29) > F(1, 8)
    assert length_upper < 1
    return {
        "cutoff": "z=(1/4)*sqrt(N)*log(N)",
        "geometry_assumptions": "log(N)>=8; covering theorem also needs its unspecified large-z threshold",
        "unrounded_block_lower_ratio": rational(length_lower),
        "block_upper_ratio": rational(length_upper),
        "rounded_block_lower_ratio_for_N_ge_29": "1/8",
        "z_fourth_over_N_squared_lower": rational(four_factor_ratio_lower),
        "shell_upper_over_N_squared_upper_for_N_ge_2": "5/4",
        "maximum_Omega_of_survivor": 3,
        "guaranteed_count_scale": "N*log(log(N))/log(N)^2",
        "guaranteed_lower_bound_scale_relative_to_u": "2*log(log(N))/log(N) -> 0",
        "prime_count_lower_bound_supplied": False,
        "remaining_TypeI_progression_length_exponent": str(1-F(457, 400)),
        "remaining_TypeII_progression_length_exponent": str(1-F(459, 400)),
        "direct_021_positive_node_length_hypothesis_satisfied_on_delta_core": False,
    }


def verify_records(manifest: Path, key: str) -> int:
    data = json.loads(manifest.read_text())
    for record in data[key]:
        p = ROOT/record["path"]
        content = p.read_bytes()
        assert len(content) == record["size_bytes"], record["path"]
        assert hashlib.sha256(content).hexdigest() == record["sha256"], record["path"]
    return len(data[key])


def main() -> None:
    result = {
        "date": "2026-10-08",
        "status": "passed",
        "scope": "exact arithmetic and source-preservation checks; analytical arguments reviewed separately",
        "reference_margins": reference_margins(),
        "translation_checks": crt_translations(),
        "hyperbola_checks": restricted_hyperbola_completion(),
        "square_shell_geometry": shell_geometry(),
        "unchanged_checkpoint14_records": verify_records(
            ROOT/"results/checkpoint14_preservation_manifest.json", "unchanged_historical_records"),
        "source_records": verify_records(ROOT/"sources/openai021/manifest.json", "files"),
        "Lean_comparator_replayed": False,
        "uniform_delta_0011_estimate_proved": False,
        "certified_K": 0,
        "H_theta_proved": False,
    }
    output = ROOT/"results/openai021_checks.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in (
        "status", "translation_checks", "hyperbola_checks", "unchanged_checkpoint14_records",
        "source_records", "Lean_comparator_replayed", "H_theta_proved")}, indent=2))


if __name__ == "__main__":
    main()
