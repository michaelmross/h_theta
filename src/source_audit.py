#!/usr/bin/env python3
"""Reproduce source-audit metadata; printed statements were checked manually.

This checks file identity and arithmetic consistency. It is not a theorem prover
and does not validate a source statement from OCR or from a PDF hash.
"""

from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    {
        "path": "sources/aa37127.pdf",
        "authors": "H. Iwaniec",
        "title": "A new form of the error term in the linear sieve",
        "journal": "Acta Arithmetica 37 (1980), 307-320",
        "sha256": "a6a962b15345953fe522160e0323df2bee9b29a93102c9fba2ad2c9b047d70e9",
        "size_bytes": 613790,
        "page_image_evidence": [
            {"printed_page": 308, "pdf_page": 2, "half": "left",
             "statement": "Dimension-one density and prime-power conditions (1)-(2)"},
            {"printed_page": 309, "pdf_page": 2, "half": "right",
             "statement": "Theorem 1; signed bilinear remainder, s>=2, capacities>1; optional mn|P(z)"},
            {"printed_page": 312, "pdf_page": 4, "half": "left",
             "statement": "Lemma 1 prime-box partition and subsequent capacity enlargement"},
        ],
        "manual_audit_status": "Relevant theorem hypotheses and remainder statement verified on page images",
        "fixed_weight_quantifier_note": "Theorem 1 coefficients explicitly depend on the prescribed capacities; use the explicit WF formulation for adaptive splits",
    },
    {
        "path": "sources/aa36210.pdf",
        "authors": "H. Iwaniec",
        "title": "Rosser's sieve",
        "journal": "Acta Arithmetica 36 (1980), 171-202",
        "sha256": "6b799768bafdea2952ce84c82b944ef9e320195631e3bbdc6b95be7b8607f91a",
        "size_bytes": 1193655,
        "page_image_evidence": [
            {"printed_page": 172, "pdf_page": 2, "half": "left",
             "statement": "Theorem 1; absolute divisor remainder"},
        ],
        "manual_audit_status": "Relevant ordinary sieve statement verified on page image",
        "higher_level_admitted_from_this_statement": False,
    },
    {
        "path": "sources/aa4226.pdf",
        "authors": "E. Fouvry and H. Iwaniec",
        "title": "Primes in arithmetic progressions",
        "journal": "Acta Arithmetica 42 (1983), 197-218",
        "sha256": "0c6d409366e531638112a7cba82c1120dcf4ec6d9531c65b9fc3e67d6dd2ad22",
        "size_bytes": 961135,
        "page_image_evidence": [
            {"printed_page": 199, "pdf_page": 2, "half": "right",
             "statement": "Fixed well-factorability, Q=x^(9/17-epsilon) theorem, sieve remainders (1.2)-(1.3) of order 2"},
            {"printed_page": 203, "pdf_page": 4, "half": "right",
             "statement": "Proposition 1, divisor bounds (A1), Siegel-Walfisz condition (A2)"},
            {"printed_page": 213, "pdf_page": 9, "half": "right",
             "statement": "Proposition 2, interval-indicator condition (A3), power-saving conclusion"},
            {"printed_page": 216, "pdf_page": 11, "half": "left",
             "statement": "Factor capacities chosen according to the fixed bilinear block using well-factorability"},
        ],
        "manual_audit_status": "Relevant formulation and candidate hypotheses verified on page images",
        "is_the_1989_monomial_paper": False,
        "new_short_interval_input_admitted": False,
    },
]

FROZEN_INPUTS = {
    "CAMPAIGN_NOTE.md": "908826cf477947bd7e357a27e953d7428f99226641d932b68f07b1b0d7c6698c",
    "STRUCTURED_FRONTIER_NOTE.md": "05674b14dc5128273a47075ceec01c872cc77299cb608b819998a7ce876dbe47",
    "SIGNED_LEDGER_NOTE.md": "97eb7d016f67d238e19c2b31311746993ce215214cd376d0d69ca0fe6975e860",
    "NEGATIVE_FRONTIER_NOTE.md": "3ca350fa7e90402792d2197055653ca3664eb49d51735bc2f199f1254d2aa391",
    "results/negative_frontier_ledger.json": "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def write_json(relative, value):
    (ROOT / relative).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main():
    verified = []
    for source in SOURCES:
        path = ROOT / source["path"]
        require(path.stat().st_size == source["size_bytes"], f"Size mismatch: {path}")
        require(digest(path) == source["sha256"], f"Source hash mismatch: {path}")
        verified.append(source["path"])

    baseline = read_json("baseline/manifest.json")
    for item in baseline["files"]:
        path = ROOT / item["path"]
        require(digest(path) == item["sha256"], f"Frozen baseline hash mismatch: {path}")
        require(path.stat().st_size == item["size_bytes"], f"Baseline size mismatch: {path}")
        verified.append(item["path"])

    for relative, expected in FROZEN_INPUTS.items():
        require(digest(ROOT / relative) == expected, f"Frozen checkpoint hash mismatch: {relative}")
        verified.append(relative)

    require(2 * Fraction(9, 17) == Fraction(18, 17), "Exponent conversion failed")
    require(Fraction(5, 4) / Fraction(1, 4) == 5, "Root sieve parameter failed")
    t, v = Fraction(3, 8), Fraction(1, 4)
    restored_s = (Fraction(5, 4) - t - v) / v
    require(Fraction(2) < restored_s <= Fraction(3), "Restoration example out of source range")

    ledger = read_json("results/negative_frontier_ledger.json")
    require(ledger["certified_K"] == 0 and not ledger["H_theta_proved"], "Unexpected proof status")
    target = ledger["target095"]
    require(not target["upper_bound_proved"], "Frontier target must remain unproved")
    with localcontext() as ctx:
        ctx.prec = 80
        margin = Decimal(target["critical_upper"]["lower"]) - Decimal("3.73")
        frozen_margin = Decimal(target["critical_upper_with_frozen_tail"]["lower"]) - Decimal("3.58")
        require(margin == Decimal(target["conditional_prime_margin"]["lower"]), "Conditional margin mismatch")
        require(frozen_margin == Decimal(target["conditional_prime_margin_with_frozen_tail"]["lower"]), "Frozen-tail margin mismatch")
        require(margin > Decimal(".00619"), "Recorded sufficient target lost its strict margin")
        require(frozen_margin > Decimal(".00650"), "Recorded frozen target lost its strict margin")

    audit = {
        "date": "2026-10-05",
        "checkpoint": 5,
        "method": "OCR for navigation; theorem statements and listed hypotheses manually checked against page images",
        "manual_reading_is_not_automatically_verified": True,
        "sources": SOURCES,
        "file_integrity_checks_passed": verified,
        "rational_parameter_checks": {
            "x_to_N_exponent_conversion": "2*(9/17)=18/17; loss epsilon in x becomes 2*epsilon in N",
            "root_s": "5",
            "tail_upper_s": "2",
            "restoration_range": "2<s<=3 from t>=v>=1/4 and t+3v<5/4",
            "restoration_identity": "s-2=(5/4-t-3*v)/v; 3-s=(t+4*v-5/4)/v>=0",
            "restoration_rational_example": {"t": str(t), "v": str(v), "s": str(restored_s)},
            "zero_exponent_factor": "Use constant capacity >1; complementary capacity D/constant; O(1/log N) exponent shift",
            "checks_do_not_prove_analytic_applicability": True,
        },
        "density_check": {
            "g": "1/d",
            "omega_prime_power": "1",
            "prime_power_tail": "sum_(p>=w) 1/[p*(p-1)] <= 1/(ceil(w)-1) by telescoping over integers",
            "dimension_one_product": "Mertens product condition",
        },
        "fixed_weight_interface": {
            "iwaniec_1980_theorem_1": "Prescribed-split bilinear coefficients depend on the capacities",
            "original_explicit_corroboration": "Fouvry-Iwaniec 1983 p.199 equations (1.2)-(1.3), fixed WF weights of order 2",
            "modern_formulation_already_used": "Lichtman arXiv:2109.02851v2 Definition 2.1 and Theorem 2.10",
            "blockwise_representations_of_fixed_weights": True,
            "restriction_to_smaller_modulus_box_is_not_releveled": True,
            "combined_squarefree_sifting_support_retained": True,
        },
        "progression_candidate": {
            "main_theorem_error": "O(x/(log x)^A) for each fixed A",
            "campaign_u": "asymp sqrt(x)/log x",
            "endpoint_subtraction_error_is_not_o_u": True,
            "fixed_nonzero_coprime_residue_required": True,
            "prop1_requires_A2_Siegel_Walfisz": True,
            "prop2_has_power_saving_but_requires_A3_interval_indicator": True,
            "new_short_interval_input_admitted": False,
            "universal_inapplicability_claim": False,
        },
        "unchanged_numerical_ledger": {
            "path": "results/negative_frontier_ledger.json",
            "sha256": FROZEN_INPUTS["results/negative_frontier_ledger.json"],
            "target095_conditional_prime_margin_lower": str(margin),
            "target095_frozen_conditional_prime_margin_lower": str(frozen_margin),
            "certified_K": 0,
            "H_theta_proved": False,
        },
        "pending": [
            "Primary-text audit of Fouvry-Iwaniec 1989, Exponential sums with monomials, Lemma 9 and Theorem 6",
            "Actual short-interval arithmetic reduction for any new 1983 progression-paper candidate",
            "Parity-sensitive structured estimate improving the negative frontier or terminal prime comparison",
        ],
        "note": "ORIGINAL_SOURCE_AUDIT.md",
    }

    state = read_json("results/campaign_state.json")
    state.update({
        "checkpoint": 5,
        "original_source_audit": "results/original_source_audit.json",
        "source_audit_note": "ORIGINAL_SOURCE_AUDIT.md",
        "analytic_input_status": "Checkpoint 4 reductions unchanged; original Iwaniec signed remainder verified; fixed WF formulation corroborated by Fouvry-Iwaniec 1983; no prime lower bound",
        "new_tail_source_route": "Independent RS plus explicit WF sieve formulation, now corroborated by the uploaded originals; original 1989 pipeline audit pending",
        "negative_frontier_reduction": "Frozen positive slice estimates restrict to the semiprime band; original sieve interface checked, 1989 monomial pipeline still pending",
        "original_1983_progression_tool_admitted": False,
        "numerical_bounds_changed_in_checkpoint5": False,
        "lower_bound_status": "K=0; source interfaces clarified; checkpoint 4 root and small-prime cofactor bounds unchanged",
    })
    state["baseline"]["independent_tail_theorem_audit"] = "Original Iwaniec sieve statement checked; fixed WF formulation corroborated; 1989 monomial-sum pipeline audit pending"
    state["milestones"]["1"] = "frozen; arithmetic reproduced; original sieve interface checked, 1989 pipeline audit pending"
    state["milestones"]["4"] = "Checkpoint 4 reductions unchanged; original sieve/WF formulations audited; full analytic tool inventory incomplete"
    require(state["chosen_target"]["certified_K_from_current_inputs"] == 0, "Unexpected campaign K")
    require(not state["H_theta_proved"], "Unexpected campaign H status")
    write_json("results/original_source_audit.json", audit)
    write_json("results/campaign_state.json", state)
    print(f"Checkpoint 5: {len(verified)} file identities verified; ledger unchanged; K=0; H unproved.")


if __name__ == "__main__":
    main()
