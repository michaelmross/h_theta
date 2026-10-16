#!/usr/bin/env python3
"""Checkpoint 3: signed reference ledger and a family-wide endpoint check.

Reference masses are not credited to the short interval.  The enclosure
algorithm is a forward interval integration of Buchstab's delay equation.
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

from structured_frontier import I, ROOT, constants_interval, write_json


def buchstab_grid(bins: int, upper: int = 8):
    """Enclose omega on every closed cell in [1,upper].

    omega(u)=1/u on [1,2]; u*omega(u)=1+int_1^(u-1)omega(v)dv
    thereafter.  At step i, the latest prefix used is i-bins+1<i,
    so this is a causal enclosure and has no numerical ODE assumption.
    """
    h = F(1, bins)
    cells = []
    prefix = [I.point(0)]
    for i in range((upper - 1) * bins):
        left, right = 1 + i * h, 1 + (i + 1) * h
        if i < bins:
            omega = 1 / I.segment(left, right)
        else:
            numerator = I(Decimal(1), Decimal(1)) + I(
                prefix[i-bins].lo, prefix[i-bins+1].hi)
            omega = numerator / I.segment(left, right)
        cells.append(omega)
        prefix.append(prefix[-1] + omega * h)
    return cells, prefix


def point_omega(u: F, bins: int, prefix):
    if 1 <= u <= 2:
        return 1 / I.point(u)
    index = (u - 2) * bins
    if index.denominator != 1:
        raise ValueError("Requested point must be aligned to the grid")
    return (1 + prefix[int(index)]) / u


def reference_ledger(theta: F, bins: int, frontier: dict):
    b = F(1, 4)
    cells, prefix = buchstab_grid(bins)
    for known_u in (F(2),F(5,2),F(3)):
        known = I.point(F(1,2)) if known_u==2 else (1+I.point(known_u-1).log())/known_u
        actual = point_omega(known_u,bins,prefix)
        assert actual.lo<=known.lo<=known.hi<=actual.hi
    A0 = 8 * point_omega(F(8), bins, prefix)
    low_u, high_u = (2 - theta) / b, F(7)
    first = (low_u-1) * bins
    last = (high_u-1) * bins
    if first.denominator != 1 or last.denominator != 1:
        raise ValueError("Use a grid aligned with the target exponent")
    A1 = I.point(0)
    h = F(1, bins)
    for i in range(int(first), int(last)):
        domain = I.segment(1+i*h, 1+(i+1)*h)
        A1 = A1 + 2*cells[i]/(2-b*domain)*h
    m, C, budget = constants_interval(theta)
    R2 = m - A0 + A1
    terminal = I(Decimal(frontier['reference_mass']['lower']),
                 Decimal(frontier['reference_mass']['upper']))
    L0 = 4 * I.point(3).log()
    U1 = 4 * (3 * I.point(theta) / (1-I.point(theta))).log()
    root_loss = A0-L0
    negative_loss = U1-A1
    raw_if_all_R2_transfers = L0-U1+R2
    ideal_negative_upper_needed = L0 + R2 - C
    # This is an actual sign-safe implication from the frozen upper tail,
    # not a transfer of a positive restoration term.  The baseline tail
    # theorem's independent source audit remains partial.
    split=F(877,1000)
    assert F(4,5)<split<theta
    low_negative_upper=4*(3*I.point(split)/(1-I.point(split))).log()
    _, high_tail_upper, _ = constants_interval(split)
    hybrid_raw=L0-low_negative_upper-high_tail_upper
    regional_high_upper=high_tail_upper-C
    regional_raw=L0-low_negative_upper-regional_high_upper
    target_split=F(19,20)
    target_m,target_C,_=constants_interval(target_split)
    target_reference=A0-target_m
    allowed_extra=target_m-target_C-root_loss
    proposed_extra=F(1,10)
    conditional_prime_margin=allowed_extra-proposed_extra
    assert conditional_prime_margin.lo>0
    return dict(theta=str(theta),base="1/4",bins_per_unit=bins,
                normalization="u=N/(2 log N)",
                formulas={"A0":"8*omega(8)",
                          "A1":"8*integral_(1/4)^theta omega(8-4*t)/t dt = 2*integral_(8-4*theta)^7 omega(v)/(2-v/4) dv",
                          "R2":"m(theta)-A0+A1"},
                reference={"A0":A0.record(),"A1":A1.record(),"R2":R2.record(),
                           "terminal_prime_R2":terminal.record(),
                           "other_R2":(R2-terminal).record(),"final_m":m.record()},
                admitted={"A0_lower":L0.record(),"A1_upper":U1.record(),"R2_lower":0},
                error_ledger={"root_shortfall":root_loss.record(),
                              "negative_upper_excess":negative_loss.record(),
                              "allowed_total_loss":budget.record()},
                hypothetical_full_R2_transfer_with_current_TypeI=raw_if_all_R2_transfers.record(),
                sufficient_negative_upper_threshold_if_full_R2_transfers=ideal_negative_upper_needed.record(),
                hybrid_negative_frontier=dict(split=str(split),
                    exact_identity="S(z)=A0-R1_low-R1_high",
                    low_TypeI_upper=low_negative_upper.record(),
                    high_frozen_tail_upper=high_tail_upper.record(),
                    combined_R1_upper=(low_negative_upper+high_tail_upper).record(),
                    raw_lower=hybrid_raw.record(),
                    improvement_over_original_raw=(hybrid_raw-(L0-U1)).record(),
                    regional_tail_upper=regional_high_upper.record(),
                    regional_raw_lower=regional_raw.record(),
                    regional_improvement_over_original_raw=(regional_raw-(L0-U1)).record(),
                    regional_requires="The frozen proof's positive per-slice bound, restricted to the large-prime band; not subtraction of two global upper bounds",
                    optimal_split_expression="5-sqrt(17), when below theta",
                    status="Valid implication conditional on the frozen tail theorem, whose source audit remains partial",
                    short_TypeII_transfer_required=False,positive_K_proved=False),
                concrete_upper_lemma_target=dict(split=str(target_split),
                    arithmetic_term="sum_(N^(1/4)<=p<N^(19/20)) S_p(p)",
                    reference_mass=target_reference.record(),
                    allowed_additional_loss=allowed_extra.record(),
                    proposed_additional_loss=str(proposed_extra),
                    required_upper=(target_reference+proposed_extra).record(),
                    simpler_sufficient_upper="349/100",
                    critical_upper_threshold=(L0-target_C).record(),
                    conditional_H_095_lower=(L0-F(349,100)).record(),
                    conditional_prime_margin_for_simple_target=(L0-F(349,100)-target_C).record(),
                    conditional_H_097_lower_for_simple_target=(L0-F(349,100)-target_C+C).record(),
                    current_regional_tail_and_TypeI_upper=(low_negative_upper+high_tail_upper-target_C).record(),
                    conditional_prime_lower_margin=conditional_prime_margin.record(),
                    conditional_H_theta_lower=(C+conditional_prime_margin).record(),
                    proof_status="Unproved target; positive conclusion is conditional on this lemma and the frozen slice theorem"),
                full_R2_transfer_assumed_only_for_diagnosis=True,
                full_R2_transfer_proved=False,certified_K=0,
                priority="Tighten the negative A1 branches; even full R2 reference recovery does not close the present Type I design")


def moment_family():
    """A symbolic rational identity, plus representative admissible tuples.

    delta1=2, sum(1/delta_j)=1.  Source thresholds replace the last
    2/delta_n by 2/(delta_n-1), making the total strictly greater than 2.
    """
    examples = [(2,4,8,8),(2,4,6,12),(2,4,6,14,86,3612)]
    examples_out=[]
    for ds in examples:
        assert sum((F(1,d) for d in ds),F(0)) == 1
        total = 1 + sum((F(2,d) for d in ds[1:-1]),F(0)) + F(2,ds[-1]-1)
        excess = F(2,ds[-1]*(ds[-1]-1))
        assert total == 2+excess
        examples_out.append(dict(moment_orders=list(ds),threshold_coefficient_sum=str(total),
                                 root_sum_excess=str(excess/2),
                                 necessary_lambda_lower_bound=str(1-1/total)))
    four = []
    for case,c in enumerate((F(57,28),F(133,66),F(61,15),F(27,13)),1):
        # Case 3 combines its cross inequality and is compared with 2;
        # the other cases compare a sum or complementary pair with 1.
        rhs=2 if case==3 else 1
        gap=c/2-rhs
        assert gap>0
        four.append(dict(case=case,combined_coefficient=str(c),rhs=rhs,
                         contradiction_gap_at_lambda_half=str(gap),
                         necessary_lambda_lower_bound=str(1-rhs/c)))
    return dict(source="Li arXiv:2308.04458v8, Lemma 4.2 and proof following Lemma 4.5",
                source_url="https://arxiv.org/html/2308.04458v8",
                source_interval_not_extended=True,
                general_hypotheses=["delta_1=2", "sum_j 1/delta_j=1", "all delta_j finite and delta_n>1"],
                coefficient_sum_identity="1+sum_(2<=j<n) 2/delta_j+2/(delta_n-1) = 2+2/[delta_n*(delta_n-1)]",
                lambda_half_contradiction="sum_j alpha_j >= 1+1/[delta_n*(delta_n-1)] > 1",
                necessary_lambda_lower_bound="1/2+1/[2*(delta_n*(delta_n-1)+1)]",
                covered_displayed_box_families={"Lemma 4.4":9,"Lemma 4.5":87},
                examples=examples_out,all_four_Lemma42_cases=four,
                scope="The unchanged finite Holder/moment family and the four displayed Lemma 4.2 cases; not every existing method",
                endpoint_theorem_applied=False,global_impossibility_claim=False)


def update_state(path: Path, ledger: dict):
    state=json.loads(path.read_text()) if path.exists() else {}
    state.update(date='2026-10-05',checkpoint=3,
                 lower_bound_status='K=0; a conditional negative-frontier upper improvement is established; no positive K proved',
                 H_theta_proved=False,typeII_tools_admitted_for_lower_bound=[],
                 signed_mass_ledger='results/signed_mass_ledger.json',
                 negative_frontier_reduction='Frozen positive slice estimates restrict to the semiprime band; original source audit partial',
                 conditional_raw_lower_bound=ledger['hybrid_negative_frontier']['regional_raw_lower'],
                 next_gate='Refine the negative frontier sum_(N^(1/4)<=p<N^(19/20)) S_p(p); sufficient aggregate upper coefficient 3.49',
                 next_gate_status='Unproved; the displayed positive consequence is conditional',
                 moment_endpoint_certificate='results/moment_family_endpoint.json')
    state.setdefault('milestones',{})['4']='Signed upper-tail reuse derived; finite Holder/moment family endpoint collapse proved; complete tool inventory pending'
    state['milestones']['5']='Two-step reference ledger enclosed; conditional upper reduction optimized; full signed optimization pending'
    write_json(path,state)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bins',type=int,default=20000)
    parser.add_argument('--out',type=Path,default=ROOT/'results')
    args=parser.parse_args()
    if args.bins<=0 or args.bins%25:
        raise ValueError('Use a positive multiple of 25 for the fixed theta=97/100')
    frontier=json.loads((ROOT/'results/structured_frontier_mass.json').read_text())
    assert frontier['theta']=='97/100'
    ledger=reference_ledger(F(97,100),args.bins,frontier)
    args.out.mkdir(parents=True,exist_ok=True)
    write_json(args.out/'signed_mass_ledger.json',ledger)
    write_json(args.out/'moment_family_endpoint.json',moment_family())
    update_state(args.out/'campaign_state.json',ledger)
    for name,bounds in ledger['reference'].items():
        print(name, bounds['lower'],bounds['upper'])
    print('Negative upper excess:',ledger['error_ledger']['negative_upper_excess'])
    print('Hypothetical full R2 recovery:',ledger['hypothetical_full_R2_transfer_with_current_TypeI'])
    print('No positive K or short-interval comparison admitted.')


if __name__=='__main__':
    main()
