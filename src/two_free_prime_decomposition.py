#!/usr/bin/env python3
"""Checkpoint 26: a two-free-variable prime decomposition and source audit.

Uniform proofs and the unresolved sharp comparison are in
TWO_FREE_PRIME_DECOMPOSITION_NOTE.md. Finite exact identities and rational
facet checks do not prove the remaining .007935 coefficient.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from decimal import Decimal
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import isqrt, comb
from pathlib import Path
import json

from cofactor_estimation import mobius_table
from joint_remainder import factor_divisor, subtract_factors, vaughan_vectors
from joint_signed_comparison import prime_cofactor_marks, psi
from ross_geometry_audit import factor_band, primes_up_to
from structured_frontier import I, enclose_integral
from two_three_frontier import divisors

ROOT = Path(__file__).resolve().parents[1]
TAU = F(1, 1000)
RHO = 2 * TAU
OUTER_B_CUT = F(1, 800)
NU = F(1, 10000)
GATE = F(3987, 2000)
DELTA = 2 - GATE
KAPPA = F(1, 1000)
SMOOTH, BUDGET = F(613, 200000), F(1587, 200000)
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def preservation():
    raw = (ROOT / "results/checkpoint25_preservation_manifest.json").read_bytes()
    previous = json.loads(raw)
    demand(previous["checkpoint"] == 25, "Frozen checkpoint 25")
    count = 0
    for rec in previous["files"]:
        if rec["path"] in MUTABLE:
            continue
        data = (ROOT / rec["path"]).read_bytes()
        demand(len(data) == rec["size_bytes"] and sha256(data).hexdigest() == rec["sha256"],
               "Historical preservation: " + rec["path"])
        count += 1
    ledger = sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
    demand(ledger == "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
           "Frozen historical mass ledger")
    return {"checkpoint25_nonmutable_records_verified": count,
            "checkpoint25_manifest_sha256": sha256(raw).hexdigest(),
            "negative_frontier_ledger_sha256": ledger}


def solve(rows):
    dimension = len(rows)
    matrix = [list(a) + [b] for a, b in rows]
    for col in range(dimension):
        pivot = next((i for i in range(col, dimension) if matrix[i][col]), None)
        if pivot is None:
            return None
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        scale = matrix[col][col]
        matrix[col] = [v / scale for v in matrix[col]]
        for i in range(dimension):
            if i != col:
                scale = matrix[i][col]
                matrix[i] = [x - scale * y for x, y in zip(matrix[i], matrix[col])]
    return tuple(row[-1] for row in matrix)


def vertices(constraints):
    dimension = len(constraints[0][0])
    points = set()
    for indices in combinations(range(len(constraints)), dimension):
        point = solve([constraints[i] for i in indices])
        if point is not None and all(sum(a * x for a, x in zip(row, point)) <= bound
                                     for row, bound in constraints):
            points.add(point)
    return sorted(points)


def constraint(row, bound):
    return tuple(map(F, row)), F(bound)


def facet_certificates():
    # Coordinates S=log_N(pr), a=log_N(p), alpha/beta small products
    # for the outer and cofactor Type I terms respectively.
    cs = [
        constraint((-1, 0, 0, 0), -F(1, 2)),
        constraint((1, 0, 0, 0), F(4, 3)),
        constraint((0, -1, 0, 0), -F(1, 4)),
        constraint((-F(1, 2), 1, 0, 0), 0),
        constraint((2, -1, 0, 0), GATE),
        constraint((0, 0, -1, 0), 0),
        constraint((0, 0, 1, 0), RHO),
        constraint((0, 0, 0, -1), 0),
        constraint((0, 0, 0, 1), RHO)]
    rows, minima = [], {}
    for s, a, alpha, beta in vertices(cs):
        sigma, free = s + beta, a - alpha
        margins = {"L9_first_and_second": free - 2 * sigma + 2,
                   "L9_third": 3 - 2 * sigma,
                   "free_slot_positive": free}
        demand(all(v > 0 for v in margins.values()), "All direct Lemma9 facets")
        for term, value in margins.items():
            minima[term] = min(minima.get(term, value), value)
        rows.append({"S": str(s), "a": str(a), "alpha": str(alpha), "beta": str(beta),
                     "Sigma": str(sigma), "free_slot_A": str(free),
                     "margins": {k: str(v) for k, v in margins.items()}})
    demand(rows, "Nonempty two-free domain")
    demand(minima["L9_first_and_second"] == F(1, 2000), "Direct strict source margin")
    demand(minima["L9_third"] == F(169, 500), "Direct inverse-phase reserve")
    # Also audit the earlier top-frequency transfer for comparison. It is
    # not needed when using the direct fractional-part Lemma9.
    critical, critical_min = [], {}
    high = cs + [constraint((-1, 0, 0, -1), -1)]
    for s, a, alpha, beta in vertices(high):
        sigma, free = s + beta, a - alpha
        eta = sigma - 1 + NU
        margins = {"RS3_T1": free - (4 * eta + 2 - 2 * sigma),
                   "RS3_T2": free - 2 * eta,
                   "RS3_T3": 2 - sigma}
        demand(all(v > 0 for v in margins.values()), "Critical RS3 transfer match")
        for term, value in margins.items():
            critical_min[term] = min(critical_min.get(term, value), value)
        critical.append({"S": str(s), "a": str(a), "alpha": str(alpha), "beta": str(beta),
                         "eta": str(eta), "margins": {k: str(v) for k, v in margins.items()}})
    demand(critical_min["RS3_T1"] == NU, "Conservative critical-frequency margin")
    witness = {"S": F(13, 10), "a": F(13, 20), "alpha": RHO, "beta": RHO}
    witness_sigma = witness["S"] + witness["beta"]
    witness_free = witness["a"] - witness["alpha"]
    witness_margins = {"first_and_second": witness_free - 2 * witness_sigma + 2,
                       "third": 3 - 2 * witness_sigma}
    demand(witness_sigma == F(651, 500) and witness_free == F(81, 125),
           "Balanced witness derived coordinates")
    demand(witness_margins["first_and_second"] == F(11, 250), "Balanced free-slot witness")
    demand(2 * witness["S"] - witness["a"] < GATE, "Balanced actual pair gate")
    low_cs = [constraint(row, bound if row != (F(0), F(0), F(1), F(0))
                         else TAU + OUTER_B_CUT) for row, bound in cs]
    low_rows, low_minima = [], {}
    for s, a, alpha, beta in vertices(low_cs):
        sigma, free = s + beta, a - alpha
        margins = {"L9_first_and_second": free - 2 * sigma + 2,
                   "L9_third": 3 - 2 * sigma}
        demand(all(v > 0 for v in margins.values()), "Low outer-TypeII direct facets")
        for term, value in margins.items():
            low_minima[term] = min(low_minima.get(term, value), value)
        low_rows.append({"S": str(s), "a": str(a), "alpha": str(alpha), "beta": str(beta),
                         "Sigma": str(sigma), "A": str(free),
                         "margins": {k: str(v) for k, v in margins.items()}})
    demand(low_minima["L9_first_and_second"] == F(1, 4000),
           "Low outer-TypeII strict source margin")
    return {"coordinate_order": ["S", "a", "alpha", "beta"],
            "source": "Robert-Sargos2006, Theorem3 and direct Lemma9",
            "reciprocal_phase_exponents": [-1, -1],
            "standalone_slot_is_unit_or_log_weighted_free_integer": True,
            "arbitrary_standalone_coefficients_used": False,
            "constraints": [{"A": list(map(str, a)), "bound": str(b)} for a, b in cs],
            "direct_vertices": rows, "direct_vertex_count": len(rows),
            "direct_minimum_facets": {k: str(v) for k, v in minima.items()},
            "raw_term_minimum_power_reserve": str(F(1, 8000)),
            "critical_vertices": critical, "critical_vertex_count": len(critical),
            "critical_minimum_facets": {k: str(v) for k, v in critical_min.items()},
            "outer_TypeII_small_Mangoldt_factor": {
                "b_p_exponent_cut": str(OUTER_B_CUT),
                "outer_small_product_upper": str(TAU + OUTER_B_CUT),
                "vertices": low_rows, "vertex_count": len(low_rows),
                "minimum_facets": {k: str(v) for k, v in low_minima.items()},
                "raw_term_minimum_power_reserve": str(F(1, 16000)),
                "uses_direct_Lemma9_not_conservative_Y_over_Q_frequency_envelope": True},
            "balanced_witness": {**{k: str(v) for k, v in witness.items()},
                                 "Sigma": str(witness_sigma), "A": str(witness_free),
                                 "margins": {k: str(v) for k, v in witness_margins.items()}}}


def cofactor_only_certificate():
    s = F(13, 10)
    demand(5 - 4 * s - 7 * NU < 0, "RS1 weighted slot gap")
    demand((5 - 4 * s - 3 * NU) / 2 < 0, "FI6 weighted slot gap")
    # If ell is eliminated and f remains a free cofactor variable,
    # A+ell<=2-S, Sigma=2-ell:
    # A-(2*Sigma-2)<=ell-S<=2-2*S.
    demand(2 - 2 * F(5, 4) == -F(1, 2), "Depth-independent cofactor-only gap")
    ell, free = F(2, 5), F(1, 5)
    sigma = 2 - ell
    demand(free + ell <= 2 - s, "Actual retained cofactor resources")
    return {"scope": "Any cofactor-only exact identity followed by one-free-variable elimination and the audited RS1/FI6/RS3-L9 mappings",
            "S_ge_5_4_L9_first_margin_upper": "-1/2",
            "depth_independent": True,
            "balanced_witness": {"p_exponent": "13/20", "r_exponent": "13/20",
                "mu1_exponent": "1/20", "mu2_exponent": "1/20",
                "free_f_exponent": str(free), "free_ell_exponent": str(ell),
                "Sigma": str(sigma), "L9_first_margin": str(free - 2 * sigma + 2)},
            "all_other_methods_excluded": False,
            "outer_prime_expansion_excluded": False}


def hb_identity_checks():
    records, total_rows = [], 0
    for z in (1, 2, 3, 5, 8):
        limit = min((z + 1) ** 4 - 1, 5000)
        mu = mobius_table(z)
        fs = factor_band(1, limit, primes_up_to(isqrt(limit)))
        g = [0] * (limit + 1)
        for a in range(1, min(z, limit) + 1):
            g[a] = mu[a]
        full = [defaultdict(int) for _ in range(limit + 1)]
        for order in range(1, 5):
            coefficient = (-1) ** (order - 1) * comb(4, order)
            for d in range(1, limit + 1):
                if not g[d]:
                    continue
                for k in range(2, limit // d + 1):
                    for p, exponent in fs[k].items():
                        full[d * k][p] += coefficient * g[d] * exponent
            if order < 4:
                small = [0] * (limit + 1)
                for a in range(1, z + 1):
                    if mu[a]:
                        for k in range(1, limit // a + 1):
                            small[a * k] += mu[a] * g[k]
                next_g = [0] * (limit + 1)
                for d in range(1, limit + 1):
                    if small[d]:
                        for n in range(d, limit + 1, d):
                            next_g[n] += small[d]
                g = next_g
        prime_rows, power_rows, composite_rows = 0, 0, 0
        for n in range(1, limit + 1):
            target = {next(iter(fs[n])): 1} if len(fs[n]) == 1 else {}
            demand({p: v for p, v in full[n].items() if v} == target,
                   "Independent exact HB4 convolution coefficients")
            if len(fs[n]) == 1:
                if next(iter(fs[n].values())) == 1:
                    prime_rows += 1
                else:
                    power_rows += 1
            elif n > 1:
                composite_rows += 1
        records.append({"Z": z, "n_max": limit, "support_ceiling": (z + 1) ** 4,
                        "primes": prime_rows, "proper_powers": power_rows,
                        "non_power_composites_cancelled": composite_rows})
        total_rows += limit
    return {"identity_depth": 4, "signed_binomial_coefficients": [4, -6, 4, -1],
            "row_checks": total_rows, "cases": records,
            "all_terms_retained": True, "original_least_prime_cutoff_changed": False}


def integer_root(value, degree, upper):
    lo, hi = 0, upper + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** degree <= value:
            lo = mid
        else:
            hi = mid
    demand(lo ** degree <= value < (lo + 1) ** degree, "Exact integer monomial threshold")
    return lo


def tensor(first, second):
    result = defaultdict(int)
    for p, a in first.items():
        if a:
            for q, b in second.items():
                if b:
                    result[tuple(sorted((p, q)))] += a * b
    return {k: v for k, v in result.items() if v}


def add(*vectors):
    result = defaultdict(int)
    for vec in vectors:
        for k, v in vec.items():
            result[k] += v
    return {k: v for k, v in result.items() if v}


def tensor_identity_checks():
    records, total, cancelled, repeated, unit_gates = [], 0, 0, 0, 0
    for n, u in ((100, 1), (1000, 3), (10000, 8)):
        lo, hi = n * n - n // 2, n * n + n // 2
        factors = factor_band(lo, hi, primes_up_to(isqrt(hi)))
        gate = integer_root(n ** GATE.numerator, GATE.denominator, n * n)
        cache = {}
        count, comp_count, power_count, diag_count = 0, 0, 0, 0
        exact_target_mass, proper_power_mass = F(0), F(0)
        for value, nf in factors.items():
            for r in sorted(nf):
                if r ** 4 < n:
                    continue
                remaining = dict(nf)
                remaining[r] -= 1
                if not remaining[r]:
                    del remaining[r]
                for p in divisors(remaining):
                    if p <= u or p ** 4 < n or p > r or p * r * r > gate:
                        continue
                    q = value // (p * r)
                    if q <= u:
                        continue
                    pf = factor_divisor(remaining, p)
                    qf = subtract_factors(remaining, pf)
                    if p not in cache:
                        one, two, bilinear, target, _ = vaughan_vectors(pf, u, u)
                        cache[p] = (add(one, two), dict(bilinear), dict(target))
                    if q not in cache:
                        one, two, bilinear, target, _ = vaughan_vectors(qf, u, u)
                        cache[q] = (add(one, two), dict(bilinear), dict(target))
                    ip, bp, lp = cache[p]
                    iq, bq, lq = cache[q]
                    four = (tensor(ip, iq), tensor(ip, bq), tensor(bp, iq), tensor(bp, bq))
                    demand(add(*four) == tensor(lp, lq), "Exact tensor Vaughan identity")
                    demand(add(four[1], four[3]) == tensor(lp, bq),
                           "Recombine actual outer detector before q-TypeII removal")
                    demand(add(four[0], tensor(lp, bq), four[2]) == tensor(lp, lq),
                           "Coefficient-one three-family remaining identity")
                    # Independent stress partition of the new outer Type II
                    # Mangoldt factor. The asymptotic cut is N^(1/800); these
                    # finite stress cuts exercise both signs and partitions.
                    stress_cut = 2 * u
                    small_bp, large_bp = defaultdict(int), defaultdict(int)
                    for b in divisors(pf):
                        if b <= u or p // b <= u:
                            continue
                        bf = factor_divisor(pf, b)
                        if len(bf) != 1:
                            continue
                        mf = subtract_factors(pf, bf)
                        mu = mobius_table(u)
                        beta = -sum(mu[t] for t in divisors(mf) if t <= u)
                        (small_bp if b <= stress_cut else large_bp)[next(iter(bf))] += beta
                    demand(add(small_bp, large_bp) == add(bp), "Independent outer-b partition")
                    demand(add(four[0], tensor(lp, bq), tensor(small_bp, iq),
                               tensor(large_bp, iq)) == tensor(lp, lq),
                           "Retain both outer-b pieces with coefficient one")
                    count += 1
                    if not lp or not lq:
                        demand(not add(*four), "Non-prime-power rows cancel exactly")
                        comp_count += 1
                    weight = F(1, 2) if p == r else F(1)
                    if lp and lq:
                        exponent_p = next(iter(pf.values()))
                        exponent_q = next(iter(qf.values()))
                        mass = weight / (exponent_p * exponent_q)
                        exact_target_mass += mass
                        if exponent_p > 1 or exponent_q > 1:
                            proper_power_mass += mass
                            power_count += 1
                            repeated += 1
                    if p == r:
                        diag_count += 1
                    # The new good/core split is auxiliary, not a redefinition
                    # of the original outer gate pr^2<=N^2.
                    demand(p * r * r <= n * n, "Original outer gate remains")
                    unit_gates += 1
            # Compare original prime pair marks with direct canonical rows.
            mark, original = prime_cofactor_marks(value, nf, n)
            original_pairs = F(0)
            for d, q, df, weight in original:
                if sum(df.values()) == 2:
                    ps = sorted(p for p, exponent in df.items() for _ in range(exponent))
                    if ps[0] * ps[1] ** 2 <= gate:
                        original_pairs += weight
            direct_pairs = F(0)
            ps = sorted(nf)
            for i, p in enumerate(ps):
                for r in ps[i:]:
                    if p == r and nf[p] < 2:
                        continue
                    if p ** 4 < n or p * r * r > gate:
                        continue
                    df = {p: 2} if p == r else {p: 1, r: 1}
                    qf = subtract_factors(nf, df)
                    if sum(qf.values()) == 1:
                        direct_pairs += F(1, 2) if p == r else F(1)
            demand(original_pairs == direct_pairs, "Independent original canonical pair count")
        records.append({"N": n, "auxiliary_U": u,
                        "stress_cutoff": u != 1, "rows": count,
                        "composite_rows_cancelled": comp_count,
                        "proper_power_rows_retained": power_count,
                        "diagonal_rows_retained": diag_count,
                        "full_prime_power_detector_mass": str(exact_target_mass),
                        "explicit_proper_power_detector_mass": str(proper_power_mass)})
        total += count
        cancelled += comp_count
    return {"cases": records, "tensor_rows": total,
            "composite_rows_cancelled": cancelled,
            "proper_power_rows_retained": repeated,
            "original_gate_checks": unit_gates,
            "finite_checks_are_not_a_uniform_sharp_estimate": True}


def hybrid_reference(bins):
    gate, delta = GATE, DELTA
    cuts = [(gate + F(1, 4)) / 2, F(9, 8), 2 * gate / 3, F(4, 3)]
    demand(cuts == [F(4487, 4000), F(9, 8), F(1329, 1000), F(4, 3)], "Exact strip cuts")
    pieces = [
        ((F(0), F(1, 4)), (F(2), -gate), (F(2), -gate - F(1, 4))),
        ((F(2), F(-2)), (F(2), -gate), (F(0), delta)),
        ((F(2), F(-2)), (F(1, 2), F(0)), (-F(3, 2), F(2)))]
    total, records = I.point(0), []
    for (left, right), (low, high, width) in zip(zip(cuts, cuts[1:]), pieces):
        for s in (left, right):
            ell, upper = low[0] * s + low[1], high[0] * s + high[1]
            demand(0 < ell <= upper <= s / 2 and ell >= max(F(1, 4), 2 * s - 2),
                   "Boundary-strip actual geometry")
            demand(upper - ell == width[0] * s + width[1], "Exact width identity")
        def integrand(s):
            ell = low[0] * s + low[1]
            opposite = (1 - high[0]) * s - high[1]
            w = width[0] * s + width[1]
            # Two positive log(1+...) terms avoid interval dependency loss
            # from taking a logarithm of a ratio close to one.
            return 2 * ((1 + w / ell).log() + (1 + w / opposite).log()) / (s * (2 - s))
        mass = enclose_integral(integrand, left, right, bins)
        total += mass
        records.append({"S": [str(left), str(right)],
                        "a_lower": list(map(str, low)), "a_upper": list(map(str, high)),
                        "width": list(map(str, width)), "reference_mass": mass.record()})
    strip_total, strip_records = total, records
    # Retain all checkpoint24 cofactor-only Type I coverage on the complement
    # of the new two-free-variable domain, rather than abandoning old cells.
    hybrid_cuts = [F(4609, 4000), F(49891, 40000), F(49911, 40000),
                   F(1329, 1000), F(4, 3)]
    ell, lb = (F(2), F(-2)), (F(2), -F(799, 400))
    la, ub = (F(2), -F(3991, 2000)), (-F(2), F(1871, 625))
    ua, strip = (-F(2), F(7489, 2500)), (F(2), -GATE)
    high = (F(1, 2), F(0))
    hybrid_pieces = [[(ell, lb)], [(ell, lb), (ub, la), (ua, strip)],
                     [(ell, strip)], [(ell, high)]]
    total, records = I.point(0), []
    for (left, right), pairs in zip(zip(hybrid_cuts, hybrid_cuts[1:]), hybrid_pieces):
        subtotal = I.point(0)
        intervals = []
        for low, high in pairs:
            width = high[0] - low[0], high[1] - low[1]
            for s in (left, right):
                l, r = low[0] * s + low[1], high[0] * s + high[1]
                demand(0 < l <= r <= s / 2 and l >= 2 * s - 2,
                       "Hybrid actual pair geometry")
                demand(r <= 2 * s - GATE or r == s / 2,
                       "Hybrid strip intersection")
            def integrand(s):
                l = low[0] * s + low[1]
                opposite = (1 - high[0]) * s - high[1]
                w = width[0] * s + width[1]
                return 2 * ((1 + w / l).log() + (1 + w / opposite).log()) / (s * (2 - s))
            mass = enclose_integral(integrand, left, right, bins)
            subtotal += mass
            intervals.append({"a_lower": list(map(str, low)), "a_upper": list(map(str, high)),
                              "reference_mass": mass.record()})
        total += subtotal
        records.append({"S": [str(left), str(right)], "intervals": intervals,
                        "reference_mass": subtotal.record()})
    previous = json.loads((ROOT / "results/spectral_coverage_reference.json").read_text())[
        "auxiliary_core_reference"]
    old = I(Decimal(previous["lower"]), Decimal(previous["upper"]))
    demand(total.hi < strip_total.lo < old.lo, "Retained coverage gives smaller hybrid core")
    rhs = (1 + KAPPA) * I.point(F(total.lo)) + BUDGET
    # The eventual downward-rounded sufficient coefficient is selected only
    # after an outward enclosure, rather than inserted as an asserted bound.
    scale = 10 ** 7
    safe = F((F(rhs.lo) * scale).__floor__(), scale)
    if I.point(safe).hi >= rhs.lo:
        safe -= F(1, scale)
    demand(I.point(safe).hi < rhs.lo, "Downward-rounded sufficient coefficient")
    demand(SMOOTH + BUDGET == F(11, 1000), "Original smoothing/spectral budget")
    full = json.loads((ROOT / "results/two_three_reference_and_samples.json").read_text())[
        "joint_reference_mass"]
    coarse = (1 + KAPPA) * (8 - F(full["lower"]) + F(total.hi))
    demand(coarse < F(39565, 8000), "Conservative joint coefficient rounds upward")
    return {"bins_per_piece": bins, "new_outer_gate_exponent": str(gate),
            "remaining_strip_width_in_gate_exponent": str(delta),
            "new_strip_pieces": strip_records, "new_strip_reference": strip_total.record(),
            "hybrid_core_pieces": records, "new_hybrid_core_reference": total.record(),
            "checkpoint24_auxiliary_core_reference": previous,
            "reference_reduction": (old - total).record(),
            "safe_coupled_rhs_using_hybrid_lower_endpoint": rhs.record(),
            "downward_rounded_sufficient_coupled_coefficient": str(safe),
            "new_coupled_term_introduced": "Outer-TypeII times cofactor-TypeI",
            "coarse_joint_upper_coefficient": "4.945625",
            "coarse_joint_upper_uses_full_reference_lower_and_hybrid_reference_upper": True,
            "new_hybrid_core_reference_is_short_count_cap": False,
            "new_coupled_sharp_estimate_proved": False}


def hybrid_geometry_certificate():
    forms = {
        "quarter": (F(0), F(1, 4)), "lower": (F(2), F(-2)),
        "upper": (F(1, 2), F(0)), "new_lower": (F(2), -GATE),
        "old_A_lower": (F(2), -F(3991, 2000)),
        "old_B_lower": (F(2), -F(799, 400)),
        "old_A_upper": (-F(2), F(7489, 2500)),
        "old_B_upper": (-F(2), F(1871, 625))}
    def at(form, s):
        a, b = forms[form]
        return a * s + b
    cuts = {F(1, 2), F(4, 3), F(4609, 4000),
            F(49891, 40000), F(49911, 40000), F(1329, 1000)}
    for first, second in combinations(forms.values(), 2):
        if first[0] != second[0]:
            s = (second[1] - first[1]) / (first[0] - second[0])
            if F(1, 2) < s < F(4, 3):
                cuts.add(s)
    cells, order_checks = [], 0
    ordered = sorted(cuts)
    for left, right in zip(ordered, ordered[1:]):
        mid = (left + right) / 2
        # Every possible endpoint-order transition is included in the cuts.
        # Affine endpoint signs certify that the order chosen at the rational
        # midpoint persists throughout the whole open cell.
        for first, second in combinations(forms, 2):
            d0, d1 = at(first, left) - at(second, left), at(first, right) - at(second, right)
            demand(d0 * d1 >= 0, "No omitted affine endpoint crossing")
            order_checks += 1
        lower, upper = max(F(1, 4), 2 * mid - 2), mid / 2
        if mid < F(4609, 4000):
            generic = []
        else:
            good = []
            for a, b in (("old_A_lower", "old_A_upper"), ("old_B_lower", "old_B_upper")):
                l, r = max(lower, at(a, mid)), min(upper, at(b, mid))
                if l < r:
                    good.append((l, r))
            l = max(lower, at("new_lower", mid))
            if l < upper:
                good.append((l, upper))
            generic = [(lower, upper)]
            for l, r in sorted(good):
                new = []
                for a, b in generic:
                    if r <= a or l >= b:
                        new.append((a, b))
                    else:
                        if a < l:
                            new.append((a, l))
                        if r < b:
                            new.append((r, b))
                generic = new
        if mid < F(4609, 4000):
            predicted = []
        elif mid < F(49891, 40000):
            predicted = [(at("lower", mid), at("old_B_lower", mid))]
        elif mid < F(49911, 40000):
            predicted = [(at("lower", mid), at("old_B_lower", mid)),
                         (at("old_B_upper", mid), at("old_A_lower", mid)),
                         (at("old_A_upper", mid), at("new_lower", mid))]
        elif mid < F(1329, 1000):
            predicted = [(at("lower", mid), at("new_lower", mid))]
        else:
            predicted = [(at("lower", mid), at("upper", mid))]
        demand(generic == predicted, "Independent union-complement interval identity")
        cells.append({"S": [str(left), str(right)], "ordered_endpoint_guards_verified": True,
                      "independent_interval_count": len(generic)})
    return {"affine_cells": cells, "endpoint_order_checks": order_checks,
            "continuous_geometry_proved_by_affine_order_guards": True,
            "numerical_sampling_used_as_proof": False}


def status_record(reference):
    return {"checkpoint": 26, "date": "2026-10-11",
            "proof_note": "TWO_FREE_PRIME_DECOMPOSITION_NOTE.md",
            "cofactor_only_deep_identity_balanced_gap_certified": True,
            "cofactor_only_gap_scope": "One-free-variable elimination and the audited reciprocal engines",
            "smaller_outer_prime_detector_expanded": True,
            "auxiliary_tau": str(TAU),
            "actual_double_TypeI_centered_error_o_u_proved": True,
            "actual_outer_TypeII_small_Mangoldt_times_cofactor_TypeI_o_u_proved": True,
            "new_outer_Mangoldt_cutoff_exponent": str(OUTER_B_CUT),
            "new_physical_pair_good_region": "p<=r, p,r>=N^(1/4), pr^2<=N^(3987/2000)",
            "balanced_S_13_10_source_family_covered": True,
            "new_remaining_outer_TypeII_times_cofactor_TypeI": "Retained jointly; sharp estimate open",
            "old_TypeI_coverage_retained_on_new_domain_complement": True,
            "new_remaining_interface": "I_kappa=B_q,hybrid_good,large_db+O_pII,new_good,b_p>N^(1/800),qI+Q_hybrid_core-(1+kappa)*M_hybrid_core*u+o(u)",
            "new_sufficient_coupled_coefficient": reference[
                "downward_rounded_sufficient_coupled_coefficient"],
            "new_nonvanishing_coefficient_charge": "0",
            "original_signed_spectral_allowance": str(BUDGET),
            "original_target": "11/1000",
            "short_scale_tail_and_fixed_L_budget_unchanged": True,
            "fixed_least_prime_power_budget_if_used": "xi from checkpoint22 (23), retained in final coefficient",
            "all_HB_and_Vaughan_terms_retained": True,
            "final_identity": "Complete auxiliary Vaughan identity on both the smaller outer factor and the cofactor",
            "whole_good_prime_count_negligible_from_double_TypeI_inferred": False,
            "sharp_signed_spectral_bound_proved": False,
            "terminal_0011_estimate_proved": False,
            "H_theta_proved": False, "certified_K": 0}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bins", type=int, default=12000)
    args = parser.parse_args()
    demand(args.bins >= 1000, "Outward integration resolution")
    facets = facet_certificates()
    print(json.dumps({"stage": "source_facets",
                      "direct_vertices": facets["direct_vertex_count"],
                      "minimum_facets": facets["direct_minimum_facets"]}), flush=True)
    checks = {"preservation": preservation(), "HB4": hb_identity_checks(),
              "tensor_identities": tensor_identity_checks(),
              "hybrid_geometry": hybrid_geometry_certificate(),
              "all_exact_checks_passed": True,
              "sharp_target_proved": False}
    reference = hybrid_reference(args.bins)
    for name, data in (
            ("two_free_prime_facets.json", facets),
            ("two_free_prime_cofactor_only_gap.json", cofactor_only_certificate()),
            ("two_free_prime_checks.json", checks),
            ("two_free_prime_reference.json", reference),
            ("two_free_prime_decomposition.json", status_record(reference))):
        (ROOT / "results" / name).write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"all_exact_checks_passed": True,
                     "preserved_records": checks["preservation"]["checkpoint25_nonmutable_records_verified"],
                     "HB4_rows": checks["HB4"]["row_checks"],
                     "tensor_rows": checks["tensor_identities"]["tensor_rows"],
                     "hybrid_core_reference": reference["new_hybrid_core_reference"],
                     "safe_sufficient_coefficient": reference[
                         "downward_rounded_sufficient_coupled_coefficient"],
                     "larger_new_outer_TypeII_sharp_bound_proved": False,
                     "sharp_target_proved": False}, indent=2), flush=True)


if __name__ == "__main__":
    main()
