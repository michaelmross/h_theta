#!/usr/bin/env python3
"""Exact identities and source-scope checks for the 007 audit.

This does not compile Lean, validate the imported proof closure, or estimate
the campaign's signed remainder. Continuous proofs are in OPENAI007_AUDIT.md.
"""

from fractions import Fraction
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "openai007"
DATE = "2026-10-07"
COMMIT = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
MUTABLE_INDEXES = {
    "README.md",
    "CONSTRAINT_INVENTORY.md",
    "TOOL_REGISTRY.json",
    "results/campaign_state.json",
}


def file_hash(path):
    return sha256(path.read_bytes()).hexdigest()


def verify_provenance():
    source_manifest = json.loads((SOURCE / "SOURCE_MANIFEST.json").read_text())
    assert source_manifest["commit"] == COMMIT
    for record in source_manifest["records"]:
        path = ROOT / record["path"]
        assert path.stat().st_size == record["size_bytes"], record["path"]
        assert file_hash(path) == record["sha256"], record["path"]
    old = json.loads(
        (ROOT / "results/checkpoint11_preservation_manifest.json").read_text()
    )
    unchanged = []
    for record in old["files"]:
        if record["path"] in MUTABLE_INDEXES:
            continue
        path = ROOT / record["path"]
        assert path.stat().st_size == record["size_bytes"], record["path"]
        assert file_hash(path) == record["sha256"], record["path"]
        unchanged.append(record["path"])
    assert file_hash(ROOT / "results/negative_frontier_ledger.json") == (
        "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"
    )
    return {
        "commit": COMMIT,
        "source_records_verified": len(source_manifest["records"]),
        "historical_files_verified_unchanged": len(unchanged),
        "main_pdf_sha256": file_hash(SOURCE / "final.pdf"),
        "frozen_numerical_ledger_unchanged": True,
    }


def strip_lean_comments(text):
    """Remove line and nested block comments, retaining token separation."""
    result = []
    i = 0
    depth = 0
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                depth += 1
                i += 2
            elif text.startswith("-/", i):
                depth -= 1
                i += 2
            else:
                i += 1
        elif text.startswith("/-", i):
            result.append(" ")
            depth = 1
            i += 2
        elif text.startswith("--", i):
            end = text.find("\n", i)
            i = len(text) if end < 0 else end
            result.append(" ")
        else:
            result.append(text[i])
            i += 1
    assert depth == 0
    return "".join(result)


def normalized(text):
    return re.sub(r"\s+", "", text)


def theorem_signature(text, name):
    text = strip_lean_comments(text)
    match = re.search(r"\btheorem\s+" + re.escape(name) + r"\b", text)
    assert match, name
    end = text.index(":=", match.end())
    return normalized(text[match.end():end])


def definition_rhs(text, name):
    text = strip_lean_comments(text)
    match = re.search(r"\bdef\s+" + re.escape(name) + r"\b", text)
    assert match, name
    begin = text.index(":=", match.end()) + 2
    following = re.search(
        r"\n\s*(?:@\[|(?:noncomputable\s+)?def\b|lemma\b|theorem\b|end\b)",
        text[begin:],
    )
    assert following, name
    return normalized(text[begin:begin + following.start()])


def verify_lean_source_scope():
    challenge = (
        SOURCE / "lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.lean"
    ).read_text()
    solution = (
        SOURCE / "lean/OAI/NumberTheory/TwoPointCorrelations/FinalMain.lean"
    ).read_text()
    names = [
        "liouville_log_saving",
        "binary_corrected_elliott",
        "affine_corrected_elliott",
    ]
    for name in names:
        assert theorem_signature(solution, name) == theorem_signature(
            challenge, name
        ), name
    basic = (
        SOURCE / "lean/OAI/NumberTheory/TwoPoint/Basic.lean"
    ).read_text()
    distance = (
        SOURCE / "lean/OAI/NumberTheory/TwoPoint/PretentiousDistance.lean"
    ).read_text()
    definitions = [
        "liouville", "correlationSum", "affineSum", "Multiplicative", "OneBounded",
        "primesUpTo", "squaredDistance", "characterTwist",
        "UniformlyNonpretentious",
    ]
    for name in definitions:
        source = basic if name in definitions[:5] else distance
        assert definition_rhs(source, name) == definition_rhs(
            challenge, name
        ), name
    clean = strip_lean_comments(solution)
    assert not re.search(r"\b(?:sorry|admit|axiom)\b", clean)
    assert len(re.findall(r"\bsorry\b", strip_lean_comments(challenge))) == 3
    config = json.loads(
        (SOURCE / "lean/ComparatorChallenges/OrdinaryTwoPointCorrelations.json")
        .read_text()
    )
    assert config["solution_module"] == (
        "OAI.NumberTheory.TwoPointCorrelations.FinalMain"
    )
    assert config["theorem_names"] == [
        "OAI.OrdinaryTwoPointCorrelations." + name for name in names
    ]
    assert set(config["permitted_axioms"]) == {
        "propext", "Quot.sound", "Classical.choice",
    }
    assert config["enable_nanoda"] is False
    return {
        "exported_statement_types_matched_textually": names,
        "definition_bodies_matched_textually": definitions,
        "final_forwarding_module_has_no_placeholder_or_axiom_declaration": True,
        "challenge_placeholder_count": 3,
        "permitted_axioms": config["permitted_axioms"],
        "lean_toolchain": (
            SOURCE / "lean/lean-toolchain"
        ).read_text().strip(),
        "lean_or_comparator_run": False,
        "transitive_axiom_audit_completed": False,
        "note": "Textual source matches are not kernel verification.",
    }


def mobius(n):
    value = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        value = -value
    return value


def divisors(n):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return out


def beta_direct(n, cutoff):
    return sum(mobius(t) for t in divisors(n) if t > cutoff)


def beta_short(n, cutoff):
    assert n > 1
    return -sum(mobius(t) for t in range(1, cutoff + 1) if n % t == 0)


def is_prime(n):
    if n < 2:
        return False
    return all(n % t for t in range(2, isqrt(n) + 1))


def prime_detector(n):
    """Exact Lambda(n)/log(n) on n>1, as a rational prime-power weight."""
    assert n > 1
    primes = [p for p in divisors(n) if is_prime(p)]
    if len(primes) != 1:
        return Fraction(0)
    p = primes[0]
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    assert n == 1
    return Fraction(1, exponent)


def coefficient_witnesses():
    witnesses = []
    for cutoff in [1, 2, 3, 5, 10, 100]:
        primes = [p for p in range(cutoff + 1, 4 * cutoff + 20) if is_prime(p)]
        p, q = primes[:2]
        values = [beta_direct(n, cutoff) for n in [p, q, p * q]]
        assert values == [-1, -1, -1]
        assert values == [beta_short(n, cutoff) for n in [p, q, p * q]]
        assert values[2] != values[0] * values[1]
        assert p > cutoff and q > cutoff
        witnesses.append({"U": cutoff, "p": p, "q": q, "beta_values": values})
    assert beta_direct(30, 5) == beta_short(30, 5) == 2
    assert prime_detector(7) == prime_detector(11) == 1
    assert prime_detector(77) == 0
    assert prime_detector(49) == Fraction(1, 2)
    return {
        "beta_nonmultiplicative_witnesses": witnesses,
        "beta_not_one_bounded_witness": {"U": 5, "m": 30, "beta": 2},
        "prime_detector_values": {"7": "1", "11": "1", "77": "0", "49": "1/2"},
    }


def singleton_center_checks():
    beta = Fraction(1, 2)
    theta = beta * beta
    extras = [[], [2], [1, 1], [4], [3, 1], [2, 2], [4, 2, 2]]
    checked = 0
    for prime in [53, 101, 211]:
        for extra in extras:
            counts = [2] + extra + [0] * (prime - 1 - len(extra))
            length = sum(counts)
            assert prime >= 2 * (length + 1)
            # Independent direct sum of the lit and every unlit residue.
            direct = (
                beta ** 2 * (1 - theta / prime)
                - sum(theta * beta ** value / prime for value in counts[1:])
            ) / prime
            formula = theta / (prime * prime) * (
                1 - theta + sum(1 - beta ** value for value in counts[1:])
            )
            assert direct == formula
            assert 0 <= direct <= theta / (2 * prime)
            checked += 1
    assert beta ** 2 - theta == 0
    assert beta ** 2 - beta == Fraction(-1, 4)
    return {
        "exact_primewise_fixtures": checked,
        "beta_Z": "1/2",
        "theta": "1/4",
        "leading_coefficient_beta_squared_minus_theta": "0",
        "scope": "Local rational factor identity, not a high-trace verification.",
    }


def ceiling_div(a, b):
    return (a + b - 1) // b


def overlap_formula(N, Q, V, k, ell):
    low = N * N - N // 2
    high = N * N + N // 2
    lower = max(Q + 1, V + 1, ceiling_div(low, k), ceiling_div(low, ell))
    upper = min(2 * Q, high // k, high // ell)
    return max(0, upper - lower + 1)


def overlap_checks():
    pair_checks = 0
    quadratic_checks = 0
    for N in [10, 20, 50, 100]:
        low, high = N * N - N // 2, N * N + N // 2
        for Q in [1, 2, 4, 8, 16]:
            for V in [1, 3, 10]:
                bs = list(range(max(Q, V) + 1, 2 * Q + 1))
                ks = {1, N, N * N, N * N + 1}
                for b in bs:
                    for seed in [ceiling_div(low, b), high // b, N * N // b]:
                        ks.update(k for k in [seed - 1, seed, seed + 1] if k > 0)
                ks = sorted(ks)
                incidences = {
                    k: {b for b in bs if low <= k * b <= high} for k in ks
                }
                weights = {
                    k: Fraction(k % 11 - 5, 1 + k % 5) for k in ks
                }
                direct = sum(
                    sum(weights[k] for k in ks if b in incidences[k]) ** 2
                    for b in bs
                )
                via_kernel = Fraction(0)
                for k in ks:
                    for ell in ks:
                        actual = len(incidences[k] & incidences[ell])
                        formula = overlap_formula(N, Q, V, k, ell)
                        assert actual == formula, (N, Q, V, k, ell)
                        if actual:
                            b = min(incidences[k] & incidences[ell])
                            assert abs(k - ell) * b <= N
                        via_kernel += weights[k] * weights[ell] * formula
                        pair_checks += 1
                assert direct == via_kernel and direct >= 0
                quadratic_checks += 1
    return {
        "independent_overlap_pair_checks": pair_checks,
        "exact_signed_quadratic_form_checks": quadratic_checks,
        "N_fixtures": [10, 20, 50, 100],
        "scope": "Exact integer geometry and Gram identity; no asymptotic bound.",
    }


def prefix_local_witness_checks():
    Ns = [2 ** (2 ** j) for j in range(1, 6)]
    checked = 0
    accumulated = 0
    for N in Ns:
        accumulated += N + 1
        assert accumulated <= 2 * N
        low, high = N * N - N // 2, N * N + N // 2
        for endpoint in [low - 1, low, N * N, high, high + 1]:
            total = sum(
                max(0, min(endpoint, M * M + M // 2) - (M * M - M // 2) + 1)
                for M in Ns
            )
            assert total * total <= 9 * endpoint
            checked += 1
    return {
        "arithmetic_prefix_endpoint_fixtures": checked,
        "sequence_multiplicative": False,
        "scope": "Logical prefix-to-window obstruction, not a counterexample to 007.",
    }


def exponent_and_scope_checks():
    c_upper = Fraction(1, 1200 * 10 * 1000)
    assert c_upper == Fraction(1, 12_000_000) < 1
    assert 1 / (2 - Fraction(4, 3)) == Fraction(3, 2)
    finite_law = normalized(
        (SOURCE / "build/quantitative/02-finite-law.tex").read_text()
    )
    rough = normalized(
        (SOURCE / "build/quantitative/03-analytic.tex").read_text()
    )
    assert r"|I|\ge\exp(L^A/2)" in finite_law
    assert r"Y\ge\exp(L^A/2)" in rough
    assert r"\exp(L^{A/2})" not in finite_law
    state = json.loads((ROOT / "results/campaign_state.json").read_text())
    assert state["chosen_target"]["certified_K_from_current_inputs"] == 0
    assert state["H_theta_proved"] is False
    assert state["two_three_uniform_0011_estimate_proved"] is False
    assert state["prime_terminal_comparison_tools_admitted"] == []
    return {
        "printed_construction_c_upper": str(c_upper),
        "gamma_N_bound": "3/2",
        "finite_law_exponent_parentheses_checked_against_TeX": True,
        "positive_K_credited": 0,
        "terminal_estimate_proved": False,
        "H_theta_proved": False,
    }


def update_state():
    path = ROOT / "results/campaign_state.json"
    state = json.loads(path.read_text())
    state.update({
        "date": DATE,
        "checkpoint": 12,
        "latest_investigation_note": "OPENAI007_AUDIT.md",
        "openai007_audit": "results/openai007_audit.json",
        "openai007_checks": "results/openai007_checks.json",
        "openai007_source_commit": COMMIT,
        "openai007_terminal_estimate_admitted": False,
        "openai007_derived_local_graph_bound": True,
        "openai007_kernel_matched_to_Vaughan_remainder": False,
        "openai007_comparator_rerun": False,
        "next_gate": (
            "Estimate the actual square-centered cofactor-overlap kernel with "
            "c_N and beta_U, or prove B_N(J)+R_I,core(J)<=(.011+o(1))*u "
            "uniformly for every sufficiently large even N"
        ),
        "next_gate_status": (
            "Unproved; 007 supplies auxiliary graph tools, with analytic "
            "centering and actual-kernel matching unresolved"
        ),
        "numerical_bounds_changed_in_checkpoint12": False,
    })
    path.write_text(json.dumps(state, indent=2) + "\n")


def main():
    results = {
        "date": DATE,
        "checkpoint": 12,
        "provenance": verify_provenance(),
        "lean_source_scope": verify_lean_source_scope(),
        "coefficient_witnesses": coefficient_witnesses(),
        "singleton_center_identity": singleton_center_checks(),
        "cofactor_overlap": overlap_checks(),
        "prefix_to_window_witness": prefix_local_witness_checks(),
        "exponent_and_admission": exponent_and_scope_checks(),
        "all_checks_passed": True,
        "mathematical_proof_note": "OPENAI007_AUDIT.md",
        "uniform_signed_remainder_estimate_proved": False,
    }
    (ROOT / "results/openai007_checks.json").write_text(
        json.dumps(results, indent=2) + "\n"
    )
    update_state()
    print(json.dumps({
        "all_checks_passed": True,
        "source_records": results["provenance"]["source_records_verified"],
        "historical_files_unchanged": results["provenance"]["historical_files_verified_unchanged"],
        "overlap_pairs": results["cofactor_overlap"]["independent_overlap_pair_checks"],
        "quadratic_forms": results["cofactor_overlap"]["exact_signed_quadratic_form_checks"],
        "singleton_fixtures": results["singleton_center_identity"]["exact_primewise_fixtures"],
        "terminal_estimate_proved": False,
        "Lean_comparator_run": False,
    }, indent=2))


if __name__ == "__main__":
    main()
