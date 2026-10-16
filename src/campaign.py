#!/usr/bin/env python3
"""Reproduce the first H(theta) campaign checkpoint; Python standard library.

The program certifies algebra and finite identities, not a new analytic estimate.
No unproved Type II tool is credited with lower-bound mass.
"""
from __future__ import annotations

import argparse
import cmath
import csv
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def constants(theta: float) -> dict:
    if not 0.8 < theta < 1:
        raise ValueError("The frozen tail benchmark requires 4/5 < theta < 1.")
    t = math.log((2 - theta) / theta)
    tail = (8 / 3) * math.log((2 - theta) / (5 * theta - 4))
    return dict(theta=theta, m=1 + t, C=tail, allowed_model_loss=1 + t - tail,
                hypothetical_linear_ceiling=2 * t, C_minus_linear=tail - 2 * t,
                certified_K_from_current_inputs=0.0)


def threshold() -> float:
    lo, hi = 0.85, 0.99
    for _ in range(70):
        mid = (lo + hi) / 2
        if constants(mid)["allowed_model_loss"] > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def first_typeI_pass(theta: F, b: F) -> dict:
    """One Buchstab step at b=1/4 using only rigorous linear-sieve bounds."""
    if b != F(1, 4):
        return dict(status="not implemented for this base; no mass credited", certified_K=0.0)
    th = float(theta)
    root = 4 * math.log(3)
    negative = 4 * math.log(3 * th / (1 - th))
    raw = root - negative
    return dict(base_exponent="1/4", theta=str(theta), root_lower_constant=root,
                first_negative_upper_constant=negative, raw_lower_constant=raw,
                certified_K=max(0.0, raw),
                formula="K_raw = 4*log((1-theta)/theta)",
                scope="One-step Type I design, not optimization over all analytic methods")


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\1") * (limit + 1)
    sieve[:2] = b"\0\0"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p:limit + 1:p] = b"\0" * ((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def least_prime_factor(n: int) -> float | int:
    if n == 1:
        return math.inf
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            return p
    return n


def check_buchstab(lo: int, hi: int, w: int, z: int) -> dict:
    """Exact ordered-prime expansion, including residual 1 and prime powers.

    S_d(t) uses P^-(m/d) >= t. For a descending chain p1 > ... > pj,
    base[j] sums S_d(w); remainder[j] sums S_d(pj).
    """
    if not 2 <= w <= z:
        raise ValueError("Require 2 <= w <= z.")
    primes = [p for p in primes_upto(z - 1) if p >= w]

    @lru_cache(None)
    def S(d: int, cutoff: int) -> int:
        return sum(1 for m in range(lo, hi + 1)
                   if m % d == 0 and least_prime_factor(m // d) >= cutoff)

    base, remainder = defaultdict(int), defaultdict(int)
    base[0] = S(1, w)

    def descend(d: int, upper: int, depth: int) -> None:
        for p in primes:
            if p >= upper or d * p > hi:
                break
            nd, j = d * p, depth + 1
            base[j] += S(nd, w)
            remainder[j] += S(nd, p)
            descend(nd, p, j)

    descend(1, z, 0)
    depth = max(base)
    actual = S(1, z)
    partial = 0
    for r in range(depth + 1):
        partial += (-1) ** r * base[r]
        signed_remainder = (-1) ** (r + 1) * remainder[r + 1]
        if partial + signed_remainder != actual:
            raise AssertionError((lo, hi, w, z, r, "Buchstab identity"))
        if r % 2 and partial > actual:
            raise AssertionError("Odd truncation must be a lower bound.")
        if not r % 2 and partial < actual:
            raise AssertionError("Even truncation must be an upper bound.")
    return dict(interval=[lo, hi], w=w, z=z, count=actual, depth=depth,
                identity_verified=True, alternating_bounds_verified=True,
                base_terms={str(j): base[j] for j in range(depth + 1)},
                remainder_terms={str(j): remainder[j] for j in range(1, depth + 2)})


def exact_buchstab_checks() -> list[dict]:
    cases = [(8, 90, 2, 13), (1, 80, 2, 17), (25, 110, 3, 19),
             (64, 150, 5, 23)]
    for n in (2, 3, 5, 9, 15, 23, 35):
        for w, z in ((2, 11), (3, 19), (5, 31)):
            cases.append((4 * n * n - n, 4 * n * n + n, w, z))
    return [check_buchstab(*case) for case in cases]


def rs_boundary_checks() -> list[dict]:
    """Check the balanced witness in the *frozen tail* exponent model."""
    answers = []
    for gamma in (F(1), F(21, 20), F(11, 10), F(23, 20), F(6, 5)):
        beta = (6 - 5 * gamma) / 4
        sigma = beta + gamma
        eta, mu = sigma - 1, gamma / 2
        lower = max(2 * eta, 4 * eta + 2 - 2 * sigma)
        upper = sigma - 3 * eta
        assert upper == mu and lower <= upper
        assert 5 * eta <= sigma and eta <= 2 - sigma
        assert 4 * beta + 5 * gamma == 6
        answers.append({k: str(v) for k, v in dict(
            gamma=gamma, beta=beta, mu=mu, eta=eta,
            RS_lower=lower, RS_upper=upper).items()})
    return answers


def resonance_demo(N: int) -> dict:
    """Finite illustration of the note's arbitrary-coefficient obstruction.

    This is not evidence for or against H(theta). The proof is in the note.
    The broad comparator is (Y/x) 1_[x,2x].
    """
    if N % 2:
        raise ValueError("N must be even.")
    x, Y = N * N, N + 1
    lo, hi = x - N // 2, x + N // 2
    M = int(N ** 0.6)
    K = x // (2 * M)
    t = x / (10 * Y)
    short = 0j
    broad = 0j
    count = 0
    for m in range(math.ceil(5 * M / 4), math.floor(7 * M / 4) + 1):
        first = max(K + 1, (lo + m - 1) // m)
        last = min(2 * K, hi // m)
        for k in range(first, last + 1):
            short += cmath.exp(1j * t * math.log(m * k / x))
            count += 1
        first = max(K + 1, (x + m - 1) // m)
        last = min(2 * K, (2 * x) // m)
        for k in range(first, last + 1):
            broad += cmath.exp(1j * t * math.log(m * k / x))
    broad *= Y / x
    return dict(N=N, M=M, K=K, t=t, pair_count=count,
                short_real_over_Y=short.real / Y,
                broad_abs_over_Y=abs(broad) / Y,
                discrepancy_abs_over_Y=abs(short - broad) / Y,
                purpose="Illustration only; analytical obstruction is proved in note.")


def region_inventory(b: F, theta: F) -> dict:
    """Closed domain atoms, with tool inequalities kept strict where necessary."""
    if not 0 < b < theta < 1:
        raise ValueError("Require 0 < base exponent < theta < 1.")
    # b=1/4 gives depth at most eight for large N: any nine-prime product is too large.
    terminal_depth = math.floor(2 / b)
    nodes = []
    for j in range(1, terminal_depth + 1):
        names = [f"t{i}" for i in range(1, j + 1)]
        sigma = "+".join(names)
        atoms = [dict(lhs=f"t{j}", op=">=", rhs=str(b)),
                 dict(lhs="t1", op="<", rhs=str(theta))]
        atoms += [dict(lhs=f"t{i + 1}-t{i}", op="<=", rhs="0")
                  for i in range(1, j)]
        atoms.append(dict(lhs=sigma, op="<=", rhs="2",
                          caveat="Asymptotic box domain; keep boundary strata in arithmetic sums."))
        nodes.append(dict(id=f"B{j}", sign=(-1) ** j, variables=names,
                          sigma=sigma, domain=atoms,
                          base_cutoff=str(b), frontier_cutoff=f"t{j}",
                          typeI_upper_condition=dict(lhs=sigma, op="<", rhs="1"),
                          typeI_positive_lower_condition=dict(
                              lhs=f"{sigma}+2*c", op="<", rhs="1",
                              c="b for a base term; tj for a frontier term"),
                          cofactor_prime_region=[
                              dict(lhs=f"{sigma}+t{j}", op="<=", rhs="2"),
                              dict(lhs=f"{sigma}+2*t{j}", op=">", rhs="2")],
                          terminal_unit_stratum="d belongs to J_N; retain separately",
                          uncovered_positive="may discard for a lower bound",
                          uncovered_negative="must upper-bound or expand; may not discard"))
    return dict(exponent_base="N", x_exponent="2", interval_length_exponent="1",
                base_exponent=str(b), theta=str(theta),
                note="An algebraic region template, not a completed Harman mass optimization.",
                complete_large_N_depth=terminal_depth, nodes=nodes)


def verify_baseline() -> dict:
    manifest = json.loads((ROOT / "baseline/manifest.json").read_text())
    for item in manifest["files"]:
        actual = hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
        if actual != item["sha256"]:
            raise AssertionError(f"Frozen source changed: {item['path']}")
    log = (ROOT / "results/fm_original_run.txt").read_text()
    expected = [("1", "1/4"), ("21/20", "3/16"), ("11/10", "1/8"),
                ("23/20", "1/16"), ("6/5", "0")]
    for g, level in expected:
        if not any(f"gamma={g} " in line and f"=> zeta={level} " in line
                   for line in log.splitlines()):
            raise AssertionError(f"Original reproduction missing gamma={g}")
    if "mu = 11/20  eta = 9/40" not in log:
        raise AssertionError("Original balanced witness was not reproduced.")
    return dict(source_hashes_verified=True, original_five_slice_table_verified=True,
                independent_tail_theorem_audit="partial; see CAMPAIGN_NOTE.md",
                original_log="results/fm_original_run.txt")


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theta", default="97/100", help="Exact rational target, e.g. 99/100")
    parser.add_argument("--base", default="1/4", help="Fixed base cutoff exponent")
    parser.add_argument("--out", type=Path, default=ROOT / "results")
    parser.add_argument("--skip-resonance", action="store_true")
    args = parser.parse_args()
    theta, b = F(args.theta), F(args.base)
    chosen = constants(float(theta))
    inventory = region_inventory(b, theta)
    args.out.mkdir(parents=True, exist_ok=True)
    baseline = verify_baseline()
    checks = exact_buchstab_checks()
    rows = [constants(th) for th in (0.94, 0.95, 0.97, 0.98, 0.99, 0.995)]
    with (args.out / "target_table.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    write_json(args.out / "region_inventory.json", inventory)
    write_json(args.out / "first_typeI_pass.json", first_typeI_pass(theta, b))
    write_json(args.out / "buchstab_checks.json", checks)
    write_json(args.out / "tail_boundary_checks.json", rs_boundary_checks())
    resonance = [] if args.skip_resonance else [resonance_demo(N) for N in (200, 500, 1000, 2000)]
    write_json(args.out / "resonance_demo.json", resonance)
    endpoint = dict(id="DP_LIMIT_1", lambda_value="1/2",
                    source="Runbo Li arXiv:2308.04458v8, Lemma 4.1 (candidate family)",
                    source_url="https://arxiv.org/html/2308.04458v8",
                    theorem_at_endpoint="NOT APPLICABLE; this is a formal-limit certificate",
                    necessary_inequalities=["abs(alpha1-alpha2) >= 0",
                                            "abs(alpha1-alpha2) < 2*lambda-1 = 0"],
                    contradiction="nonnegative number strictly less than zero",
                    scope="Only this displayed criterion without a changed inequality",
                    claims_about_all_existing_tools=False)
    write_json(args.out / "endpoint_certificate.json", endpoint)
    state = dict(date="2026-10-04", theta=str(theta), base_exponent=str(b),
                 baseline=baseline, theta_star=threshold(), chosen_target=chosen,
                 exact_buchstab_cases=len(checks),
                 lower_bound_status="K=0 is certified by nonnegativity; no positive K proved",
                 typeII_tools_admitted_for_lower_bound=[],
                 next_gate="Specify a structured coefficient class and prove its interval estimate",
                 full_tool_inventory_complete=False, full_mass_optimization_complete=False,
                 H_theta_proved=False,
                 milestones={"1": "frozen; arithmetic reproduced; source audit partial",
                             "2": "complete", "3": "exact algebraic backbone complete; adaptive design pending",
                             "4": "starter inventory complete; tool-specific regions pending",
                             "5": "pending", "6": "two method-specific obstructions; no universal certificate",
                             "7": "deferred"})
    write_json(args.out / "campaign_state.json", state)
    print(f"Baseline hashes and original five-slice table verified.")
    print(f"Exact Buchstab identities and alternating bounds: {len(checks)} cases passed.")
    print(f"theta** = {state['theta_star']:.12f}")
    print(f"theta={theta}: require K > {chosen['C']:.9f}; model loss budget < {chosen['allowed_model_loss']:.9f}.")
    print(f"Hypothetical linear-sieve ceiling: {chosen['hypothetical_linear_ceiling']:.9f}.")
    print("No positive lower-bound constant or new Type II estimate is certified.")


if __name__ == "__main__":
    main()
