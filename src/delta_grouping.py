#!/usr/bin/env python3
"""Checkpoint 14: regrouped small factors in the signed delta estimate.

Exact affine facet certificates, outward reference integrals, and independent
arithmetic partition checks. No terminal .011u estimate is asserted.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

from cofactor_estimation import beta_from_factors, mobius_table
from joint_remainder import vertices, rs_margins, fi_margins, factor_divisor, subtract_factors, vaughan_vectors
from ross_geometry_audit import factor_band, primes_up_to
from structured_frontier import I, enclose_integral
from two_three_frontier import divisors, outer_coefficient

ROOT = Path(__file__).resolve().parents[1]
NU = F(1, 10000)
RESERVE = F(1, 10000)
CI = F(457, 400)
CB = F(459, 400)
RHO_I = F(1, 50)
RHO_B = F(1, 100)
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json", "results/campaign_state.json"}


def demand(value, label):
    if not value:
        raise AssertionError(label)


def provenance():
    previous = json.loads((ROOT / "results/checkpoint13_preservation_manifest.json").read_text())
    demand(previous["checkpoint"] == 13, "Frozen checkpoint 13")
    count = 0
    for rec in previous["files"]:
        if rec["path"] in MUTABLE:
            continue
        path = ROOT / rec["path"]
        demand(path.stat().st_size == rec["size_bytes"], rec["path"])
        demand(sha256(path.read_bytes()).hexdigest() == rec["sha256"], rec["path"])
        count += 1
    demand(sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest() ==
           "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e", "Frozen ledger")
    return {"historical_files_verified_unchanged": count, "historical_ledger_unchanged": True}


def con(row, rhs):
    return tuple(F(v) for v in row), F(rhs)


def base(lo, hi, rho, typeii=False):
    result = [con((-1, 0, 0), -lo), con((1, 0, 0), hi),
              con((-F(1, 2), 1, 0), 0), con((0, 0, -1), 0), con((0, 0, 1), rho)]
    result.append(con((1, -1, 0), F(19, 20)) if typeii else con((0, -1, 0), -F(1, 4)))
    return result


def split_constraint(rho):
    # a <= s_rho(S) = (15*S-13)/14 + rho/2 + 3*nu/2.
    return con((-F(15, 14), 1, 0), -F(13, 14) + rho / 2 + 3 * NU / 2)


def certificate(name, engine, cs, augment=False):
    records = []
    minima = {}
    for side, extra in (("below_one", con((1, 0, 1), 1)),
                        ("above_one", con((-1, 0, -1), -1))):
        for s, a, delta in vertices(cs + [extra]):
            eta = max(F(0), s + delta - 1) + NU
            slot = a + delta if augment else a
            margins = (rs_margins if engine == "RS" else fi_margins)(s, slot, delta, eta)
            demand(all(v > 0 for v in margins.values()), name + " strict facets")
            for term, value in margins.items():
                minima[term] = min(minima.get(term, value), value)
            records.append({"S": str(s), "a": str(a), "delta": str(delta),
                            "standalone_exponent": str(slot), "eta": str(eta), "branch": side,
                            "margins": {k: str(v) for k, v in margins.items()}})
    demand(records, name + " nonempty")
    return {"name": name, "engine": engine, "small_product_with_standalone": augment,
            "constraints": [{"A": [str(v) for v in row], "rhs": str(rhs)} for row, rhs in cs],
            "vertices": records, "minimum_facets": {k: str(v) for k, v in minima.items()},
            "minimum_margin": str(min(minima.values()))}


def facet_certificates():
    result = [certificate("TypeI_low_RS", "RS", base(F(19, 20), F(11, 10), RHO_I))]
    for label, lo, hi, rho, typeii in (("TypeI_high", F(11, 10), CI, RHO_I, False),
                                      ("TypeII_product", F(49, 50), CB, RHO_B, True)):
        b = base(lo, hi, rho, typeii)
        split = split_constraint(rho)
        result.append(certificate(label + "_FI", "FI6", b + [split]))
        result.append(certificate(label + "_RS_augmented", "RS",
                                  b + [con(tuple(-v for v in split[0]), -split[1])], True))
    for name, augment in (("TypeI_partial_other", False), ("TypeI_partial_augmented", True)):
        rho = RHO_I
        b = base(CI, F(4, 3), rho)
        b.append(con((2, -1, 0), 2))  # Actual pair-ordering gate: a >= 2*S-2.
        lower = (rho if augment else 2 * rho) + 4 * NU + RESERVE
        upper_loss = (3 * rho if augment else 2 * rho) + 3 * NU + RESERVE
        b.extend([con((2, -1, 0), 2 - lower), con((2, 1, 0), 3 - upper_loss)])
        rec = certificate(name, "RS", b, augment)
        demand(F(rec["minimum_margin"]) >= RESERVE, "Partial TypeI reserve")
        result.append(rec)
    demand(F(result[1]["minimum_margin"]) == F(1, 3500), "TypeI FI minimum")
    demand(F(result[2]["minimum_margin"]) == F(1, 3500), "TypeI RS minimum")
    demand(F(result[3]["minimum_margin"]) == F(9, 14000), "TypeII FI minimum")
    demand(F(result[4]["minimum_margin"]) == F(9, 14000), "TypeII RS minimum")
    demand(CB < CI + F(1, 100), "No large-core TypeII row is removed asymptotically")
    return {"checkpoint": 14, "frequency_extension": str(NU), "partial_reserve": str(RESERVE),
            "complete_TypeI_exponent": str(CI), "complete_TypeII_product_exponent": str(CB),
            "vertex_records": sum(len(r["vertices"]) for r in result), "regions": result,
            "all_continuous_regions_certified": True}


def pow_le(value, n, exponent):
    """Compare value <= N**exponent with integers only."""
    return value ** exponent.denominator <= n ** exponent.numerator


def good_outer(d, df, n):
    if pow_le(d, n, CI):
        return True
    primes = sorted(p for p, e in df.items() for _ in range(e))
    demand(len(primes) == 2, "Only two-prime outer products above CI")
    p, r = primes
    for augment in (False, True):
        lower_loss = (RHO_I if augment else 2 * RHO_I) + 4 * NU + RESERVE
        upper_loss = (3 * RHO_I if augment else 2 * RHO_I) + 3 * NU + RESERVE
        if pow_le(p * r * r, n, 2 - lower_loss) and pow_le(p ** 3 * r ** 2, n, 3 - upper_loss):
            return True
    return False


def arithmetic_fixture(n, u, actual):
    demand(n % 2 == 0 and u ** 4 < n, "Fixture truncation below outer factors")
    if actual:
        demand(u ** 100 <= n < (u + 1) ** 100, "Actual campaign U")
    lo, hi = n * n - n // 2, n * n + n // 2
    fs = factor_band(lo, hi, primes_up_to(isqrt(hi)))
    mu = mobius_table(u)
    counts = defaultdict(int)
    cache = {}
    for value, nf in fs.items():
        for d in divisors(nf):
            df = factor_divisor(nf, d)
            cd = outer_coefficient(df, n)
            if not cd:
                continue
            if d not in cache:
                cache[d] = good_outer(d, df, n)
            good = cache[d]
            qf = subtract_factors(nf, df)
            q = value // d
            one, two, old_b, target, _ = vaughan_vectors(qf, u, u)
            small, large = defaultdict(int), defaultdict(int)
            for b in divisors(qf):
                bf = factor_divisor(qf, b)
                if b <= u or len(bf) != 1:
                    continue
                m = q // b
                if m <= u:
                    continue
                mf = subtract_factors(qf, bf)
                beta = beta_from_factors(mf, u)
                p = next(iter(bf))
                selected = pow_le(d * b, n, CB)
                (small if selected else large)[p] += beta
                if selected:
                    demand(m > u, "Covered product region retains free m>U")
                    floor_beta = -sum(mu[t] for t in divisors(mf) if t <= u)
                    demand(beta == floor_beta, "Exact small-divisor expansion in selected region")
                    counts["selected_beta_expansions"] += 1
                    demand(good, "No core row removed in this finite fixture")
                if sum(bf.values()) == 1:
                    beta_n = beta_from_factors(nf, u)
                    demand(beta == beta_n, "Remaining prime-b covariance coefficient")
                    counts["remaining_covariance_identities"] += not selected
                else:
                    counts["proper_b_rows"] += 1
            keys = set(one) | set(two) | set(old_b) | set(target) | set(small) | set(large)
            demand(all(old_b[k] == small[k] + large[k] for k in keys), "Independent product partition")
            demand(all(one[k] + two[k] + small[k] + large[k] == target.get(k, 0) for k in keys),
                   "Exact joint signed partition in log-prime coefficients")
            counts["joint_rows"] += 1
            if not good:
                demand(all(one[k] + two[k] + large[k] == target.get(k, 0) for k in keys),
                       "Joint remaining-core identity")
                counts["core_rows"] += 1
                if not target:
                    demand(all(one[k] + two[k] + large[k] == 0 for k in keys), "Composite core cancellation")
                    counts["non_prime_power_core_rows_cancelled"] += 1
    return {"N": n, "U": u, "actual_truncation": actual,
            "stress_truncation": not actual, "exact_checks": dict(counts), "all_passed": True,
            "scope": "Arithmetic identities, not evidence for an asymptotic delta bound"}


def reference_enclosure(bins):
    rho, nu, tau = RHO_I, NU, RESERVE
    cuts = [CI, (3 - 2 * rho - 3 * nu - tau) / F(5, 2),
            (5 - 5 * rho - 7 * nu - 2 * tau) / 4,
            (5 - 4 * rho - 7 * nu - 2 * tau) / 4, F(4, 3)]
    # Affine inner interval boundaries (slope, intercept), rational throughout.
    low, high = (F(2), F(-2)), (F(1, 2), F(0))
    lb = (F(2), -2 + rho + 4 * nu + tau)
    la = (F(2), -2 + 2 * rho + 4 * nu + tau)
    ub = (F(-2), 3 - 3 * rho - 3 * nu - tau)
    ua = (F(-2), 3 - 2 * rho - 3 * nu - tau)
    regions = [[(low, lb)], [(low, lb), (ua, high)],
               [(low, lb), (ub, la), (ua, high)], [(low, high)]]
    total = I.point(0)
    pieces = []
    for j, (left, right) in enumerate(zip(cuts, cuts[1:])):
        subtotal = I.point(0)
        for ell, upper in regions[j]:
            for s in (left, right):
                l, r = ell[0] * s + ell[1], upper[0] * s + upper[1]
                demand(0 < l <= r < s and low[0] * s + low[1] <= l and r <= s / 2,
                       "Exact nonnegative inner residual interval")
            def fn(s, ell=ell, upper=upper):
                l, r = ell[0] * s + ell[1], upper[0] * s + upper[1]
                ratio = r * (s - l) / (l * (s - r))
                return 2 * ratio.log() / (s * (2 - s))
            value = enclose_integral(fn, left, right, bins)
            subtotal += value
        total += subtotal
        pieces.append({"sigma_interval": [str(left), str(right)],
                       "inner_intervals": [[list(map(str, a)), list(map(str, b))] for a, b in regions[j]],
                       "reference_mass": subtotal.record()})
    def full(s):
        return 2 * ((2 - s) / (2 * s - 2)).log() / (s * (2 - s))
    old = enclose_integral(full, F(113, 100), F(4, 3), bins)
    only_cut = enclose_integral(full, CI, F(4, 3), bins)
    demand(total.hi < only_cut.lo < old.lo, "Outward certificate confirms reference-core shrinkage")
    return {"bins_per_inner_interval": bins, "old_113_100_core": old.record(),
            "new_complete_cutoff_only_core": only_cut.record(), "new_partial_region_core": total.record(),
            "piecewise_sigma_breaks": list(map(str, cuts)), "pieces": pieces,
            "saved_reference_mass": (old - total).record(),
            "reference_mass_is_an_actual_short_upper_bound": False,
            "reference_mass_is_an_admitted_delta_budget": False}


def reduction_record():
    return {"checkpoint": 14, "date": "2026-10-07", "U_V": "floor(N^(1/100)) unchanged",
            "complete_TypeI_outer_cutoff": "N^(457/400)",
            "additional_TypeI_domain": "Pair outer d=p*r, p<=r: either robust RS wedge in DELTA_GROUPING_NOTE.md",
            "complete_TypeII_removed_product": "db<=N^(459/400), all actual outer coefficients",
            "remaining_reduction": "Delta2+Delta3=B_(db>N^(459/400))+R_I,core+o(u)",
            "joint_core": "B_core+R_I,core=A_core-integral(G_core), exact for sufficiently large N",
            "equivalent_remaining_interface": "B_(good outer,db>N^(459/400)) + A_core - integral(G_core)",
            "terminal_target": "Signed joint remainder<=(.011+o(1))*u, uniformly for all sufficiently large even N",
            "complete_TypeI_minimum_source_margin": "1/3500",
            "complete_TypeII_minimum_source_margin": "9/14000",
            "partial_TypeI_minimum_source_margin": str(RESERVE),
            "sources": ["Robert-Sargos 2006 Theorem 1", "Fouvry-Iwaniec 1989 Theorem 6"],
            "new_grouping": "Small Vaughan product moves into standalone prime slot in RS branches",
            "ordering_gate_preserved": True, "signed_boundary_envelopes_preserved": True,
            "prime_b_proper_powers_removed_absolutely": True,
            "remaining_covariance_weight_changes_with_product_cutoff": True,
            "uniform_0011_estimate_proved": False, "remaining_covariance_estimated_at_target_scale": False,
            "remaining_core_estimated_at_target_scale": False, "H_theta_proved": False,
            "higher_degree_cap_proved": False, "positive_K_credited": 0,
            "historical_numerical_ledger_changed": False, "global_impossibility_claim": False,
            "proof_note": "DELTA_GROUPING_NOTE.md"}


def source_ceiling():
    # At the retained top frequency eta=Sigma-1+nu, necessary facets
    # already have incompatible endpoints on the whole ray Sigma>=5/4.
    rows = []
    for sigma in (F(5, 4), F(13, 10), F(4, 3)):
        eta = sigma - 1 + NU
        rs_low, rs_high = 4 * eta + 2 - 2 * sigma, sigma - 3 * eta
        fi_low, fi_high = eta, (2 - sigma - eta) / 2
        demand(rs_high - rs_low == 5 - 4 * sigma - 7 * NU, "RS affine width identity")
        demand(fi_high - fi_low == (5 - 4 * sigma - 3 * NU) / 2, "FI affine width identity")
        demand(rs_high < rs_low and fi_high < fi_low, "Empty source windows")
        rows.append({"Sigma": str(sigma), "eta": str(eta),
                     "RS_necessary_slot_interval": [str(rs_low), str(rs_high)],
                     "FI_necessary_slot_interval": [str(fi_low), str(fi_high)]})
    demand(-7 * NU < 0 and -3 * NU / 2 < 0, "Negative widths at 5/4")
    return {"RS_width": "5-4*Sigma-7*nu", "FI_width": "(5-4*Sigma-3*nu)/2",
            "widths_strictly_decrease_with_Sigma": True, "no_source_window_for_Sigma_ge_5_4": True,
            "rows": rows, "actual_interior_core_witness": {"sigma": "13/10", "a": "13/20", "delta": "0"},
            "scope": "These two raw reciprocal engines at the top transfer frequency; not all methods or joint cancellation"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bins", type=int, default=12000)
    args = parser.parse_args()
    demand(args.bins >= 1000, "Reference interval bins")
    prov = provenance()
    facets = facet_certificates()
    print(json.dumps({"stage": "facets", "vertex_records": facets["vertex_records"],
                      "minima": {r["name"]: r["minimum_margin"] for r in facets["regions"]}}), flush=True)
    fixtures = [arithmetic_fixture(n, u, actual) for n, u, actual in
                ((100, 1, True), (1000, 3, False), (10000, 8, False))]
    print(json.dumps({"stage": "arithmetic", "fixtures_passed": len(fixtures)}), flush=True)
    reference = reference_enclosure(args.bins)
    checks = {"checkpoint": 14, "provenance": prov, "fixtures": fixtures, "source_ceiling": source_ceiling(),
              "all_checks_passed": True, "terminal_0011_estimate_proved": False}
    for name, value in (("delta_grouping_facets.json", facets), ("delta_grouping_checks.json", checks),
                        ("delta_grouping_reference.json", reference), ("delta_grouping_reduction.json", reduction_record())):
        (ROOT / "results" / name).write_text(json.dumps(value, indent=2) + "\n")
    print(json.dumps({"all_checks_passed": True, "historical_files_unchanged": prov["historical_files_verified_unchanged"],
                      "remaining_core_reference": reference["new_partial_region_core"],
                      "uniform_terminal_estimate_proved": False}, indent=2))


if __name__ == "__main__":
    main()
