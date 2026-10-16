#!/usr/bin/env python3
"""Checkpoint 24: spectral localization and auxiliary identity coverage.

Analytic proofs are in SPECTRAL_COVERAGE_NOTE.md. Exact certificates and
outward quadrature here do not prove the remaining .007935u inequality.
All historical modules and results are read without rewriting them.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

from delta_grouping import base, certificate, con, split_constraint
from joint_remainder import vaughan_vectors
from joint_signed_comparison import prime_cofactor_marks
from ross_geometry_audit import factor_band, primes_up_to
from structured_frontier import I, enclose_integral

ROOT = Path(__file__).resolve().parents[1]
TAU = F(1, 1000)
RHO_I, RHO_B = 2 * TAU, TAU
NU = RESERVE = F(1, 10000)
CI, CB = F(4609, 4000), F(461, 400)
KAPPA, SMOOTH, BUDGET = F(1, 1000), F(613, 200000), F(1587, 200000)
MUTABLE = {"README.md", "CONSTRAINT_INVENTORY.md", "TOOL_REGISTRY.json",
           "results/campaign_state.json"}


def demand(ok, label):
    if not ok:
        raise AssertionError(label)


def preservation():
    old = json.loads((ROOT / "results/checkpoint23_preservation_manifest.json").read_text())
    demand(old["checkpoint"] == 23, "Frozen checkpoint 23")
    count = 0
    for rec in old["files"]:
        if rec["path"] in MUTABLE:
            continue
        data = (ROOT / rec["path"]).read_bytes()
        demand(len(data) == rec["size_bytes"] and sha256(data).hexdigest() == rec["sha256"],
               "Historical preservation: " + rec["path"])
        count += 1
    ledger = sha256((ROOT / "results/negative_frontier_ledger.json").read_bytes()).hexdigest()
    demand(ledger == "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
           "Frozen negative-frontier ledger")
    return {"checkpoint23_nonmutable_records_verified": count,
            "negative_frontier_ledger_sha256": ledger}


def facet_certificates():
    rows = [certificate("Aux_TypeI_low_RS", "RS",
                        base(F(19, 20), F(11, 10), RHO_I))]
    for label, lo, hi, rho, typeii in (
            ("Aux_TypeI_high", F(11, 10), CI, RHO_I, False),
            ("Aux_TypeII_small_product", F(49, 50), CB, RHO_B, True)):
        b = base(lo, hi, rho, typeii)
        split = split_constraint(rho)
        rows.append(certificate(label + "_FI", "FI6", b + [split]))
        rows.append(certificate(label + "_RS_augmented", "RS",
                    b + [con(tuple(-v for v in split[0]), -split[1])], True))
    for name, augment in (("Aux_TypeI_wedge_A", False), ("Aux_TypeI_wedge_B", True)):
        b = base(CI, F(4, 3), RHO_I)
        b.append(con((2, -1, 0), 2))
        lower = (RHO_I if augment else 2 * RHO_I) + 4 * NU + RESERVE
        upper = (3 * RHO_I if augment else 2 * RHO_I) + 3 * NU + RESERVE
        b.extend([con((2, -1, 0), 2 - lower), con((2, 1, 0), 3 - upper)])
        rows.append(certificate(name, "RS", b, augment))
        demand(F(rows[-1]["minimum_margin"]) >= RESERVE, "Wedge reserve")
    demand(F(rows[1]["minimum_margin"]) == F(13, 56000), "New complete TypeI margin")
    demand(F(rows[3]["minimum_margin"]) == F(1, 2000), "New TypeII product margin")
    demand(CB < CI + TAU, "Core has no small-product TypeII rows eventually")
    return {"tau": str(TAU), "auxiliary_identity_cutoffs": "floor(N^(1/1000))",
            "original_least_prime_cutoff_changed": False,
            "source_nu": str(NU), "TypeI_cutoff": str(CI), "TypeII_db_cutoff": str(CB),
            "regions": rows, "vertex_records": sum(len(r["vertices"]) for r in rows),
            "full_centered_prime_product_regions_certified": False}


def residual_reference(bins):
    rho, nu, reserve = RHO_I, NU, RESERVE
    cuts = [CI, (3 - 2 * rho - 3 * nu - reserve) / F(5, 2),
            (5 - 5 * rho - 7 * nu - 2 * reserve) / 4,
            (5 - 4 * rho - 7 * nu - 2 * reserve) / 4, F(4, 3)]
    demand(cuts == sorted(cuts) and len(set(cuts)) == len(cuts), "Ordered rational cuts")
    low, high = (F(2), F(-2)), (F(1, 2), F(0))
    lb = (F(2), -2 + rho + 4 * nu + reserve)
    la = (F(2), -2 + 2 * rho + 4 * nu + reserve)
    ub = (F(-2), 3 - 3 * rho - 3 * nu - reserve)
    ua = (F(-2), 3 - 2 * rho - 3 * nu - reserve)
    regions = [[(low, lb)], [(low, lb), (ua, high)],
               [(low, lb), (ub, la), (ua, high)], [(low, high)]]
    total, pieces = I.point(0), []
    for j, (left, right) in enumerate(zip(cuts, cuts[1:])):
        subtotal = I.point(0)
        for ell, upper in regions[j]:
            for s in (left, right):
                l, r = ell[0] * s + ell[1], upper[0] * s + upper[1]
                demand(0 < l <= r < s and low[0] * s + low[1] <= l and r <= s / 2,
                       "Residual interval geometry")
            def integrand(s, ell=ell, upper=upper):
                l, r = ell[0] * s + ell[1], upper[0] * s + upper[1]
                return 2 * (r * (s - l) / (l * (s - r))).log() / (s * (2 - s))
            subtotal += enclose_integral(integrand, left, right, bins)
        total += subtotal
        pieces.append({"sigma": [str(left), str(right)],
                       "a_intervals": [[list(map(str, a)), list(map(str, b))]
                                       for a, b in regions[j]],
                       "reference_mass": subtotal.record()})
    def full(s):
        return 2 * ((2 - s) / (2 * s - 2)).log() / (s * (2 - s))
    blocked = enclose_integral(full, F(5, 4), F(4, 3), bins)
    old_rec = json.loads((ROOT / "results/delta_grouping_reference.json").read_text())[
        "new_partial_region_core"]
    from decimal import Decimal
    old = I(Decimal(old_rec["lower"]), Decimal(old_rec["upper"]))
    demand(total.hi < old.lo, "Certified auxiliary core shrinkage")
    demand(blocked.lo > I.point(BUDGET).hi, "Blocked-band reference exceeds spectral allowance")
    safe_rhs = I.point(1 + KAPPA) * I.point(F(total.lo)) + BUDGET
    safe_decimal = F(343069, 5000000)  # .0686138, rounded downward.
    demand(I.point(safe_decimal).hi < safe_rhs.lo, "Downward-rounded coupled coefficient")
    diagnostic_ratio = 1 + KAPPA + BUDGET / blocked
    return {"bins_per_inner_interval": bins, "sigma_cuts": list(map(str, cuts)),
            "pieces": pieces, "auxiliary_core_reference": total.record(),
            "old_frozen_core_reference": old.record(),
            "saved_reference_mass": (old - total).record(),
            "blocked_sigma_ge_5_4_reference": blocked.record(),
            "conditional_isolated_block_upper_ratio_ceiling": diagnostic_ratio.record(),
            "safe_coupled_rhs_using_core_lower_endpoint": safe_rhs.record(),
            "downward_rounded_sufficient_coupled_coefficient": ".0686138",
            "downward_rounding_reserve": (safe_rhs - safe_decimal).record(),
            "core_reference_is_a_short_upper_bound": False,
            "full_Vaughan_TypeII_contribution_estimated": False}


def identity_checks():
    factors = factor_band(1, 1200, primes_up_to(35))
    cases, switches = 0, 0
    for n in range(9, 1201):
        targets = []
        for u in (1, 3, 8):
            one, two, bilinear, target, _ = vaughan_vectors(factors[n], u, u)
            demand(all(one[p] + two[p] + bilinear[p] == target.get(p, 0)
                       for p in set(one) | set(two) | set(bilinear) | set(target)),
                   "Complete exact identity at each auxiliary cutoff")
            targets.append(dict(target))
            cases += 1
        demand(targets[0] == targets[1] == targets[2], "Changing identity cutoff preserves Lambda")
        switches += 1
    return {"rowwise_Vaughan_checks": cases, "independent_cutoff_switches": switches,
            "finite_cutoffs_are_identity_stress_tests": True,
            "asymptotic_terminal_estimate_tested": False}


def padding_checks():
    records, sites = [], 0
    for n in (62, 100, 200):
        lo, hi = n * n // 2, 3 * n * n // 2
        from math import isqrt
        fs = factor_band(lo, hi, primes_up_to(isqrt(hi)))
        largest, witness = F(0), None
        for value, ff in fs.items():
            mark, _ = prime_cofactor_marks(value, ff, n)
            demand(0 <= mark <= 3, "Global product coefficient cap three")
            if mark > largest:
                largest, witness = mark, value
            sites += 1
        records.append({"N": n, "sites": hi - lo + 1,
                        "maximum_mark": str(largest), "witness": witness})
    demand(records[0]["maximum_mark"] == "3", "Cap-one must not be used on product padding")
    # The explicit independent witness is 11*13*17 at N=62, outside J.
    value = 11 * 13 * 17
    demand(F(62 * 62, 2) < value < F(3 * 62 * 62, 2), "Broad-support witness")
    demand(prime_cofactor_marks(value, {11: 1, 13: 1, 17: 1}, 62)[0] == 3,
           "Independent triple-mark witness")
    # Exact rational exponent/log-power accounting for the elementary tail.
    demand(3 - F(3, 2) * F(4, 3) == 1, "First tail N exponent")
    demand(F(1, 2) - F(3, 2) * 2 == -F(5, 2), "First tail log exponent")
    demand(2 - F(4, 3) == F(2, 3), "Second tail N exponent")
    demand(SMOOTH + BUDGET == F(11, 1000), "Original coefficient budget")
    demand(CI > F(457, 400) and CB > F(459, 400), "Auxiliary complete regions enlarged")
    for old, new in ((F(3919, 2000), F(3991, 2000)),
                     (F(7399, 2500), F(7489, 2500)),
                     (F(3959, 2000), F(799, 400)),
                     (F(7349, 2500), F(1871, 625))):
        demand(old < new, "Every old TypeI wedge is contained in the auxiliary wedge")
    return {"product_padding_sites_checked": sites, "cases": records,
            "cap_three_witness": {"N": 62, "n": value, "primes": [11, 13, 17]},
            "absolute_tail_bound": "282/kappa*N^3*sqrt(log N)/T^(3/2) + 54/kappa*N^2/T",
            "T_star": "N^(4/3)*(log N)^2",
            "tail_at_T_star": "O_kappa(N/(log N)^(5/2)+N^(2/3)/(log N)^2)=o(u)",
            "tail_bound_is_for_product_localized_polynomial": True,
            "original_unlocalized_high_bands_individually_declared_negligible": False}


def coverage_record():
    return {"checkpoint": 24, "date": "2026-10-11", "kappa": str(KAPPA),
            "original_target": "11/1000", "smoothing_charge": str(SMOOTH),
            "remaining_signed_spectral_allowance": str(BUDGET),
            "new_nonvanishing_coefficient_charge": "0",
            "new_frequency_identity": "H_original = (1/pi)*Re integral_[T0,T_star] F_chi(t)*psi_Y_hat(1+it) dt + o(u)",
            "original_unlocalized_upper_limit": "N^(21/10)",
            "localized_upper_limit": "N^(4/3)*(log N)^2",
            "frequency_regions": [
                {"region": "abs(t)<=T0", "bound": "o(u)", "method": "Long PNT and paired areas", "proved": True},
                {"region": "Normalized long reference, abs(t)>T0", "bound": "o(u)", "method": "Kernel decay", "proved": True},
                {"region": "Localized short polynomial, abs(t)>T_star", "bound": "o(u)", "method": "Elementary mean square plus kernel decay", "proved": True},
                {"region": "T0<t<=T_star", "bound": "Required .007935u", "method": "Signed prime-product estimate missing", "proved": False}],
            "factor_regions": [
                {"region": "All single-prime outers z<=d<N^.95", "TypeI": "o(u)", "TypeII_small_db": "o(u) through N^(461/400)", "full_centered_prime_count": "Open"},
                {"region": "Pair outers d<=N^(4609/4000), and two rational wedges", "TypeI": "o(u)", "TypeII_small_db": "o(u) through N^(461/400)", "full_centered_prime_count": "Open"},
                {"region": "Auxiliary pair core", "TypeI": "Open", "remaining_TypeII": "Open", "full_centered_prime_count": "Open"}],
            "coupled_remaining_inequality": "B_aux,good,db>N^(461/400)(psi_Y)+Q_aux,core(psi_Y) <= ((1+kappa)*M_aux,core+.007935+o(1))*u",
            "conservative_sufficient_coupled_coefficient": ".0686138 using lower core reference endpoint",
            "fixed_least_prime_cutoff_budget_if_used": "xi from checkpoint22 (23), remaining spectral allowance .007935-xi",
            "auxiliary_Vaughan_parameter_is_a_discarded_least_prime_sector": False,
            "original_joint_0011_target_proved": False, "sharp_spectral_0007935_proved": False,
            "H_theta_proved": False, "positive_K_credited": 0,
            "proof_note": "SPECTRAL_COVERAGE_NOTE.md"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--bins", type=int, default=12000)
    args = p.parse_args()
    demand(args.bins >= 1000, "Outward integration resolution")
    prov = preservation()
    facets = facet_certificates()
    print(json.dumps({"stage": "facets", "vertices": facets["vertex_records"],
                      "margins": {r["name"]: r["minimum_margin"] for r in facets["regions"]}}), flush=True)
    checks = {"preservation": prov, "identities": identity_checks(),
              "padding": padding_checks(), "all_checks_passed": True,
              "sharp_spectral_0007935_proved": False}
    reference = residual_reference(args.bins)
    for name, result in (("spectral_coverage_facets.json", facets),
                         ("spectral_coverage_checks.json", checks),
                         ("spectral_coverage_reference.json", reference),
                         ("spectral_coverage.json", coverage_record())):
        (ROOT / "results" / name).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"all_checks_passed": True,
                      "auxiliary_core_reference": reference["auxiliary_core_reference"],
                      "blocked_band_reference": reference["blocked_sigma_ge_5_4_reference"],
                      "safe_coupled_rhs": reference["safe_coupled_rhs_using_core_lower_endpoint"],
                      "sharp_target_proved": False}, indent=2), flush=True)


if __name__ == "__main__":
    main()
