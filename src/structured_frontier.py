#!/usr/bin/env python3
"""Checkpoint 2: marked three-prime frontier, outward mass enclosures.

No short-interval Type II estimate is asserted by this program.  It checks
the exact arithmetic reduction, reference integrals and a specified
published criterion's necessary facets.  Python standard library only.
"""
from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
from pathlib import Path

from campaign import constants, least_prime_factor, primes_upto, verify_baseline


ROOT = Path(__file__).resolve().parents[1]
PRECISION = 50
DOWN = Context(prec=PRECISION, rounding=ROUND_FLOOR)
UP = Context(prec=PRECISION, rounding=ROUND_CEILING)
NEAR = Context(prec=PRECISION)


@dataclass(frozen=True)
class I:
    """Closed Decimal interval; every operation rounds outward."""
    lo: Decimal
    hi: Decimal

    def __post_init__(self):
        if not self.lo.is_finite() or not self.hi.is_finite() or self.lo > self.hi:
            raise ValueError("Invalid finite interval")

    @staticmethod
    def point(value) -> "I":
        if isinstance(value, I):
            return value
        q = F(value)
        a, b = Decimal(q.numerator), Decimal(q.denominator)
        return I(DOWN.divide(a, b), UP.divide(a, b))

    @staticmethod
    def segment(a: F, b: F) -> "I":
        return I(I.point(a).lo, I.point(b).hi)

    def __add__(self, other):
        other = I.point(other)
        return I(DOWN.add(self.lo, other.lo), UP.add(self.hi, other.hi))

    __radd__ = __add__

    def __neg__(self):
        # copy_negate does not apply the ambient Decimal context.
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + (-I.point(other))

    def __rsub__(self, other):
        return I.point(other) - self

    def __mul__(self, other):
        other = I.point(other)
        pairs = tuple(itertools.product((self.lo, self.hi), (other.lo, other.hi)))
        return I(min(DOWN.multiply(a, b) for a, b in pairs),
                 max(UP.multiply(a, b) for a, b in pairs))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("Interval contains zero")
        return I(DOWN.divide(Decimal(1), self.hi),
                 UP.divide(Decimal(1), self.lo))

    def __truediv__(self, other):
        return self * I.point(other).reciprocal()

    def __rtruediv__(self, other):
        return I.point(other) / self

    def log(self):
        if self.lo <= 0:
            raise ValueError("Log requires a positive interval")
        # Decimal.ln is correctly rounded to nearest (ROUND_HALF_EVEN),
        # independently of the context rounding setting.  Neighboring
        # representable numbers therefore enclose its exact value.
        a, b = NEAR.ln(self.lo), NEAR.ln(self.hi)
        return I(NEAR.next_minus(a), NEAR.next_plus(b))

    def nonnegative(self):
        if self.hi < 0:
            raise AssertionError("Expected a nonnegative integrand")
        return I(max(Decimal(0), self.lo), self.hi)

    def record(self):
        return dict(lower=str(self.lo), upper=str(self.hi),
                    width=str(UP.subtract(self.hi, self.lo)))


def enclose_integral(fn, a: F, b: F, bins: int) -> I:
    """Interval Riemann sum, not a floating-point quadrature tolerance."""
    width = (b - a) / bins
    result = I.point(0)
    for j in range(bins):
        domain = I.segment(a + j * width, a + (j + 1) * width)
        result = result + fn(domain).nonnegative() * width
    return result


def frontier_mass(theta: F, bins: int):
    if not F(4, 5) < theta < 1:
        raise ValueError("This piecewise formula assumes 4/5 < theta < 1, b=1/4.")
    boundaries = [(2 - theta) / 3, F(1, 2), (2 - theta) / 2, F(2, 3)]
    lower = [lambda t: 2 - 3 * t, lambda t: t, lambda t: t]
    upper = [lambda t: I.point(theta), lambda t: I.point(theta), lambda t: 2 - 2 * t]
    pieces = []
    mass = I.point(0)
    for j, (a, b) in enumerate(zip(boundaries, boundaries[1:])):
        def integrand(t, j=j):
            ell, high = lower[j](t), upper[j](t)
            ratio = high * (2 - t - ell) / (ell * (2 - t - high))
            return 2 * ratio.log() / (t * (2 - t))
        enclosure = enclose_integral(integrand, a, b, bins)
        pieces.append(dict(t2=[str(a), str(b)], bins=bins,
                           t1_lower=["2-3*t2", "t2", "t2"][j],
                           t1_upper=["theta", "theta", "2-2*t2"][j],
                           integral=enclosure.record()))
        mass = mass + enclosure
    return mass, pieces


def box_mass(bins: int):
    a, b = F(39, 50), F(81, 100)
    def integrand(t):
        ratio = b * (2 - t - a) / (a * (2 - t - b))
        return 2 * ratio.log() / (t * (2 - t))
    return enclose_integral(integrand, F(57, 100), F(59, 100), bins)


def constants_interval(theta: F):
    th = I.point(theta)
    m = 1 + ((2 - th) / th).log()
    C = F(8, 3) * ((2 - th) / (5 * th - 4)).log()
    return m, C, m - C


def arithmetic_checks():
    """Compare rough cofactors with primes under the exact q<p2^2 filter.

    These finite checks exercise the algebra, not the asymptotic H claim.
    In particular they preserve q=p2 and q=p1 when permitted.
    """
    results = []
    for N in (10, 20, 40, 80, 120):
        lo, hi = N * N - N // 2, N * N + N // 2
        for w, z in ((2, N), (3, N // 2 + 1), (5, N)):
            ps = primes_upto(hi)
            pset = set(ps)
            outer = [p for p in ps if w <= p < z]
            rough, prime, repeated = 0, 0, 0
            for p1 in outer:
                for p2 in outer:
                    if p2 >= p1:
                        break
                    d = p1 * p2
                    first, last = max(p2, (lo + d - 1) // d), min(p2 * p2 - 1, hi // d)
                    for q in range(first, last + 1):
                        rough += least_prime_factor(q) >= p2
                        prime += q in pset
                        repeated += (q in pset and q in (p1, p2))
            if rough != prime:
                raise AssertionError("The forced-prime identity failed")
            results.append(dict(N=N, w=w, z=z, interval=[lo, hi],
                                terminal_rough_count=rough, marked_prime_count=prime,
                                repeated_prime_marks=repeated, identity_verified=True))
    # An integer can carry two distinct marks; omitting this multiplicity
    # would give the wrong reference integral.
    marks = [(p1, p2, q) for p1, p2, q in itertools.product((5, 7, 11), repeat=3)
             if p2 < p1 < 13 and q >= p2 and q < p2 * p2 and p1 * p2 * q == 385]
    assert sorted(marks) == [(7, 5, 11), (11, 5, 7)]
    return dict(cases=results, double_mark_witness=dict(integer=385, marks=marks),
                scope="Exact finite arithmetic; no analytic short-interval estimate")


def interval_sanity():
    # Exact rational comparisons catch outward-rounding mistakes in the
    # arithmetic on which the integration certificate depends.
    points = [F(-7, 3), F(-1, 7), F(0), F(2, 3), F(17, 11)]
    checked = 0
    for a, b in itertools.product(points, repeat=2):
        pairs = [(I.point(a) + b, a + b), (I.point(a) - b, a - b),
                 (I.point(a) * b, a * b)]
        if b:
            pairs.append((I.point(a) / b, a / b))
        for interval, q in pairs:
            assert F(interval.lo) <= q <= F(interval.hi)
            checked += 1
    # Independent rational atanh-series log enclosures for positive points.
    log_checked = 0
    for q in (F(1), F(6, 5), F(3, 2), F(2), F(3)):
        z = (q - 1) / (q + 1)
        terms = 100
        partial = 2 * sum((z ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), F(0))
        tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
        interval = I.point(q).log()
        assert F(interval.lo) <= partial and partial + tail <= F(interval.hi)
        log_checked += 1
    return dict(exact_rational_arithmetic_cases=checked,
                independent_rational_log_enclosures=log_checked,
                decimal_precision=PRECISION)


def geometry_certificate(theta: F):
    """Exact nonnegative combinations of the selected region's facets.

    A linear form is encoded as (coefficient of t1, coefficient of t2,
    constant).  Each displayed strict conclusion uses a positive multiple
    of a strict facet, or a strictly positive constant.
    """
    facets = {"g1": (F(1), F(-1), F(0)),       # t1-t2 >= 0
              "g2": (F(1), F(3), F(-2)),       # t1+3*t2-2 > 0
              "g3": (F(-1), F(-2), F(2)),      # 2-t1-2*t2 > 0
              "g4": (F(-1), F(0), theta)}      # theta-t1 >= 0
    d = (2 - theta) / 3
    witnesses = [
        ("t2 > (2-theta)/3", (0, 1, -d), {"g2": F(1,3), "g4": F(1,3)}, 0),
        ("t1 > (2-theta)/3", (1, 0, -d), {"g1": 1, "g2": F(1,3), "g4": F(1,3)}, 0),
        ("t3 > (2-theta)/3", (-1, -1, 2-d), {"g3": 1, "g2": F(1,3), "g4": F(1,3)}, 0),
        ("t2 < 2/3", (0, -1, F(2,3)), {"g1": F(1,3), "g3": F(1,3)}, 0),
        ("t3 < 1; t1+t2 > 1", (1, 1, -1), {"g1": F(1,2), "g2": F(1,2)}, 0),
        ("t1 < 1", (-1, 0, 1), {"g4": 1}, 1-theta),
        ("t1+t3 > 1", (0, -1, 1), {"g1": F(1,3), "g3": F(1,3)}, F(1,3)),
        ("t2+t3 > 1", (-1, 0, 1), {"g4": 1}, 1-theta),
        ("t1+2*t2 > 4/3", (1, 2, F(-4,3)), {"g2": 1, "g1": F(1,3), "g3": F(1,3)}, 0),
    ]
    records = []
    for conclusion, target, weights, constant in witnesses:
        target = tuple(F(a) for a in target)
        actual = tuple(sum((F(w) * facets[g][i] for g, w in weights.items()), F(0))
                       + (F(constant) if i == 2 else 0) for i in range(3))
        assert actual == target
        assert all(F(w) >= 0 for w in weights.values()) and constant >= 0
        assert constant > 0 or any(F(weights.get(g, 0)) > 0 for g in ("g2", "g3"))
        records.append(dict(conclusion=conclusion, form=[str(a) for a in target],
                            nonnegative_combination={g: str(w) for g, w in weights.items()},
                            added_positive_constant=str(constant), identity_verified=True))
    return dict(facet_forms={g: [str(a) for a in form] for g, form in facets.items()},
                strict_facets=["g2", "g3"], witnesses=records, verified_count=len(records))


def balanced_certificate(theta: F):
    smallest_N_exponent = (2 - theta) / 3
    smallest_x_exponent = smallest_N_exponent / 2
    required_lambda = (2 + smallest_x_exponent) / 4
    center = [F(159, 400), F(29, 100), F(5, 16)]
    assert sum(center) == 1
    permutations = []
    for first, second, residual in itertools.permutations(center):
        gap = abs(first - second)
        cap_threshold = (2 + residual) / 4
        balance_threshold = (1 + gap) / 2
        permutations.append(dict(alpha1=str(first), alpha2=str(second),
                                 residual=str(residual), balance_gap=str(gap),
                                 lambda_must_exceed=str(max(cap_threshold, balance_threshold))))
    return dict(
        id="R2_THREE_PRIMES_BALANCED_CAP",
        source="Baker-Harman-Pintz (2001), Lemma 9; Li arXiv:2308.04458v8, Lemma 4.1",
        exponent_base="x=N^2",
        source_url="https://arxiv.org/html/2308.04458v8",
        exact_geometry_proof=geometry_certificate(theta),
        necessary_facets=["abs(alpha1-alpha2) < 2*lambda-1", "alpha_residual < Gamma_g(lambda) <= 4*lambda-2"],
        all_three_factors_strictly_below_N=True,
        all_two_factor_divisor_N_exponents_strictly_above="1",
        plain_two_factor_floor_class_outside_admitted_TypeI=True,
        p1_plus_2_t2_strictly_above="4/3",
        single_p1_lower_linear_sieve_requires="t1+2*t2 < 1",
        all_factor_N_exponents_strictly_above=str(smallest_N_exponent),
        all_factor_x_exponents_strictly_above=str(smallest_x_exponent),
        root_lambda="1/2", root_cap="0", root_criterion_empty=True,
        actual_length_correction=f"lambda_N=log(N+1)/(2 log N)=1/2+o(1); residual cap=o(1) stays below fixed {smallest_x_exponent}",
        lambda_0525="21/40", lambda_0525_cap="1/10",
        lambda_0525_exclusion=(smallest_x_exponent > F(1, 10)),
        whole_region_necessary_lambda_strict_lower_bound=str(required_lambda),
        whole_region_necessary_lambda_float=float(required_lambda),
        center_x_exponents=[str(a) for a in center], center_permutations=permutations,
        best_center_two_facet_threshold=str(min(F(p["lambda_must_exceed"]) for p in permutations)),
        theorem_applied_at_endpoint=False,
        grouping_scope="Permutations or groupings of whole original prime factors with a nonempty residual",
        sufficiency_claim=False, universal_impossibility_claim=False)


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theta", default="97/100")
    parser.add_argument("--bins", type=int, default=40000,
                        help="Interval bins per smooth piece; larger means tighter enclosures")
    parser.add_argument("--out", type=Path, default=ROOT / "results")
    args = parser.parse_args()
    theta = F(args.theta)
    if args.bins < 100:
        raise ValueError("Use at least 100 interval bins per piece")
    baseline = verify_baseline()
    sanity = interval_sanity()
    mass, pieces = frontier_mass(theta, args.bins)
    box = box_mass(args.bins)
    m, C, budget = constants_interval(theta)
    excess = mass - budget
    arithmetic = arithmetic_checks()
    args.out.mkdir(parents=True, exist_ok=True)
    reference = dict(date="2026-10-05", theta=str(theta), b="1/4", normalization="u=N/(2 log N)",
                     frontier="positive R2, marked three-prime subterm",
                     region=["b <= t2 <= t1 <= theta", "t1+3*t2 > 2", "t1+2*t2 < 2"],
                     mass_formula="2*integral_D dt1 dt2/[t1*t2*(2-t1-t2)]",
                     method="Closed interval Riemann sums, outward Decimal arithmetic and logarithms",
                     rounding_sanity=sanity, pieces=pieces, reference_mass=mass.record(),
                     interior_box=dict(t1=["39/50", "81/100"], t2=["57/100", "59/100"],
                                       t3=["3/5", "13/20"], mass=box.record(),
                                       contained_in_theta_region=(theta >= F(81, 100))),
                     m=m.record(), frozen_C=C.record(), allowed_model_loss=budget.record(),
                     reference_mass_minus_budget=excess.record(),
                     dropping_this_region_exceeds_budget_if_all_other_mass_matches=(excess.lo > 0),
                     certified_short_interval_mass=0,
                     mass_admission_status="Reference mass only; interval-transfer hypothesis unproved",
                     baseline_verified=baseline)
    write_json(args.out / "structured_frontier_mass.json", reference)
    write_json(args.out / "terminal_prime_checks.json", arithmetic)
    write_json(args.out / "structured_frontier_obstruction.json", balanced_certificate(theta))
    state_path = args.out / "campaign_state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    if state.get("theta") != str(theta):
        state = {}
    state.update(date="2026-10-05", checkpoint=2, theta=str(theta), base_exponent="1/4",
                 baseline=baseline, chosen_target=constants(float(theta)),
                 lower_bound_status="K=0 from nonnegativity; no positive K proved",
                 typeII_tools_admitted_for_lower_bound=[], H_theta_proved=False,
                 structured_input="Marked three-prime subterm of positive R2; centered comparison specified",
                 structured_reference_mass=reference["reference_mass"],
                 structured_reference_mass_admitted_to_short_lower_bound=False,
                 arithmetic_terminal_cases=len(arithmetic["cases"]),
                 exact_rational_facet_witnesses=9,
                 next_gate="Prove or source the centered high-frequency comparison (13), starting with the explicit interior box",
                 full_tool_inventory_complete=False, full_mass_optimization_complete=False,
                 milestones={"1": "frozen; arithmetic reproduced; source audit partial",
                             "2": "complete",
                             "3": "exact backbone complete; positive R2 terminal region selected; adaptive design pending",
                             "4": "structured input specified; balanced residual-cap exclusion proved; other tool-specific regions pending",
                             "5": "reference mass rigorously enclosed; no short Type II mass admitted; full optimization pending",
                             "6": "method-specific obstructions only; no universal certificate",
                             "7": "deferred"})
    write_json(state_path, state)
    print(f"Outward reference mass enclosure: [{mass.lo}, {mass.hi}]")
    print(f"Interior box mass enclosure: [{box.lo}, {box.hi}]")
    print(f"Reference mass minus final planning loss budget: [{excess.lo}, {excess.hi}]")
    print(f"Forced-prime arithmetic checks: {len(arithmetic['cases'])} passed; multiplicity witness passed.")
    print("No short-interval Type II estimate or positive K admitted.")


if __name__ == "__main__":
    main()
