#!/usr/bin/env python3
"""Checkpoint 4: signed frontier and well-factorable remainder calculations.

The analytic proofs are in NEGATIVE_FRONTIER_NOTE.md. This program checks exact
coverage algebra, arithmetic identities, and outward numerical integrals. A
finite numerical test is never treated as proof of an interval estimate.
Python standard library only.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from decimal import Decimal
from fractions import Fraction as F

from campaign import least_prime_factor, primes_upto, verify_baseline
from structured_frontier import I, ROOT, enclose_integral, write_json


def sieve_grid(bins: int):
    """Enclose U=sF/(2 exp(Euler)), L=sf/(2 exp(Euler)) on [1,5].

    U=1 on [1,3]; L=0 on [1,2]; L=log(s-1) on [2,4].
    U'=L(s-1)/(s-1), L'=U(s-1)/(s-1) thereafter. Each
    nonexplicit cell only refers to already enclosed cells shifted by 1.
    """
    h = F(1, bins)
    us, ls = [], []
    uprefix, lprefix = [I.point(0)], [I.point(0)]
    for i in range(4*bins):
        a, b = 1+i*h, 1+(i+1)*h
        if i < 2*bins:
            u = I.point(1)
            uint = I.point(0)
        else:
            uint = ls[i-bins] / I.segment(a-1,b-1) * h
            u = I((1+uprefix[-1]).lo, (1+uprefix[-1]+uint).hi)
        if i < bins:
            l = I.point(0)
            lint = I.point(0)
        elif i < 3*bins:
            l = I.segment(a-1,b-1).log()
            lint = I.point(0)  # explicit prefix values are used at these knots
        else:
            lint = us[i-bins] / I.segment(a-1,b-1) * h
            l = I(lprefix[-1].lo, (lprefix[-1]+lint).hi)
        us.append(u)
        ls.append(l)
        uprefix.append(uprefix[-1]+uint)
        if b <= 2:
            lprefix.append(I.point(0))
        elif b <= 4:
            lprefix.append(I.point(b-1).log())
        else:
            lprefix.append(lprefix[-1]+lint)
    return us, ls, uprefix, lprefix


def grid_value(s: F, bins: int, cells, points):
    if not 1 <= s <= 5:
        raise ValueError('Sieve function lookup outside [1,5]')
    k=(s-1)*bins
    if k.denominator==1:
        return points[int(k)]
    return cells[k.numerator//k.denominator]


def small_tail(theta: F):
    t=I.point(theta)
    return F(16,5)*((5-4*t)/t).log()


def frozen_tail(theta: F):
    t=I.point(theta)
    return F(8,3)*((2-t)/(5*t-4)).log()


def rs_box(gamma: F, beta: F, actual_beta: F, eta: F, a: F):
    """A fixed full-level factorization, valid for every smaller dyadic box.

    If standalone includes a Vaughan group of exponent a, choose the full
    sieve-factor capacity S. Its *actual* exponent is in
    [max(0,S-(beta-actual_beta)),S]. We enclose the entire range, instead
    of pretending actual exponents can be freely chosen after factoring.
    """
    sigma=gamma+actual_beta
    lower=max(2*eta,4*eta+2-2*sigma)
    upper=sigma-3*eta
    gap=beta-actual_beta
    capacity=F(0) if a>=lower else lower-a+gap
    lo=a+max(F(0),capacity-gap)
    hi=a+capacity
    ok=(0<=capacity<=beta and lower<=lo<=hi<=upper and eta<=2-sigma)
    return ok,dict(group=str(a),factor_capacity=str(capacity),
                   actual_standalone_range=[str(lo),str(hi)],
                   RS_required=[str(lower),str(upper)])


def exact_coverage_checks():
    tested=0
    tools=Counter()
    representative=[]
    # Strict-margin analytic statements use beta<cap. Equality is tested
    # only as the closed exponent geometry; no saving is claimed there.
    for gamma in [F(3,4)+F(j,40) for j in range(11)]:
        for multiplier in (F(1,2),F(3,4),F(1)):
            beta=(F(5,4)-gamma)*multiplier
            for actual_multiplier in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                actual=beta*actual_multiplier
                sigma=gamma+actual
                if sigma<1:
                    continue
                for frequency in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
                    eta=(sigma-1)*frequency
                    # Vaughan I and II parameter ranges, including endpoints.
                    for piece,low,high in [('I',F(0),2*gamma/3),('II',gamma/3,gamma/2)]:
                        for j in range(25):
                            mu=low+(high-low)*F(j,24)
                            if piece=='I' and 3*eta+2*mu<=actual+3*gamma-2:
                                tools['elementary']+=1
                            else:
                                witnesses=[]
                                for a in (F(0),mu,gamma-mu):
                                    ok,w=rs_box(gamma,beta,actual,eta,a)
                                    if ok:witnesses.append(w)
                                if not witnesses:
                                    raise AssertionError(('coverage',piece,gamma,beta,actual,eta,mu))
                                tools['RS']+=1
                                if len(representative)<8 and actual<beta:
                                    representative.append(dict(gamma=str(gamma),beta=str(beta),
                                        actual_beta=str(actual),eta=str(eta),mu=str(mu),
                                        piece=piece,witness=witnesses[0]))
                            tested+=1
    # General bounded outer coefficients: the sieve factor alone is standalone.
    arbitrary_tested=0
    for gamma in [F(j,40) for j in range(40)]:
        cap=min(F(5,4)-gamma,2-2*gamma)
        for multiplier in (F(1,2),F(1)):
            beta=cap*multiplier
            for j in range(9):
                actual=beta*F(j,8)
                sigma=gamma+actual
                if sigma<1:continue
                for k in range(9):
                    eta=(sigma-1)*F(k,8)
                    ok,w=rs_box(gamma,beta,actual,eta,F(0))
                    if not ok:raise AssertionError(('arbitrary',gamma,beta,actual,eta))
                    arbitrary_tested+=1
    return dict(proof='Symbolic facet identities in the note; this finite sweep is a consistency check',
        prime_piece_cases=tested,arbitrary_outer_cases=arbitrary_tested,
        tools_used=dict(tools),smaller_modulus_examples=representative,
        symbolic_certificates={
            'V1_gap':'(1-gamma)/2+2*rho+2*deficit',
            'V2_and_V5_gap':'1/12+(2/3)*(1-gamma)+rho+deficit',
            'V3_and_RS_window_width':'4*rho+4*deficit',
            'V4_gap':'1-gamma+4*rho+4*deficit',
            'full_level':'beta=5/4-gamma-rho; actual_beta=beta-deficit',
            'subblock_robustness':'window_width>=4*(rho+deficit); required uncertainty at most deficit'},
        exponent_boundaries_not_asserted_as_power_savings=True)


def finite_identities():
    cases=[]
    for N in (10,20,40,80,120):
        low,high=N*N-N//2,N*N+N//2
        ps=primes_upto(high)
        pset=set(ps)
        for w,z in ((2,N),(3,N//2+1),(5,N)):
            if w>=z:continue
            def S(d,c):
                return sum(least_prime_factor(m//d)>=c
                           for m in range(low,high+1) if m%d==0)
            outer=[p for p in ps if w<=p<z]
            R1=sum(S(p,p) for p in outer)
            A1=sum(S(p,w) for p in outer)
            R2=sum(S(p*q,q) for p in outer for q in outer if q<p)
            root,final=S(1,w),S(1,z)
            assert R1==root-final==A1-R2
            assert R1<=root
            multiplicities=Counter()
            for m in range(low,high+1):
                lp=least_prime_factor(m)
                if w<=lp<z:
                    r=m;k=0
                    for p in ps:
                        if p*p>r:break
                        while r%p==0:k+=1;r//=p
                    if r>1:k+=1
                    assert k>=2
                    multiplicities[k]+=1
            assert sum(multiplicities.values())==R1
            # The high first frontier really is semiprime whenever m<p^3.
            prime_residual=sum(1 for p in outer for m in range(low,high+1)
                if m%p==0 and m<p**3 and least_prime_factor(m//p)>=p)
            same_prime=sum(1 for p in outer for m in range(low,high+1)
                if m%p==0 and m<p**3 and m//p in pset)
            assert prime_residual==same_prime
            cases.append(dict(N=N,w=w,z=z,root=root,frontier=R1,
                restored=R2,Omega_counts=dict(multiplicities),identities_verified=True,
                frontier_has_unique_least_prime_mark=True,prime_powers_retained=True))
    return cases


def restored_mass(bins: int):
    """2D outward enclosure on a rectangular parametrization of the triangle.

    q exponent v in [1/4,5/16], p exponent t=v+(5/4-4v)*r, r in [0,1].
    beta=2v+(5/4-4v)*(1-r); exact log argument stays >=1.
    """
    mass=I.point(0)
    hv=F(1,16*bins);hr=F(1,bins)
    for i in range(bins):
        v=I.segment(F(1,4)+i*hv,F(1,4)+(i+1)*hv)
        gap=(F(5,4)-4*v).nonnegative()
        for j in range(bins):
            r=I.segment(j*hr,(j+1)*hr)
            t=v+gap*r
            beta=2*v+gap*(1-r)
            log_arg=1+gap*(1-r)/v
            integrand=4*gap*log_arg.log()/(v*t*beta)
            mass=mass+integrand.nonnegative()*hv*hr
    return mass


def make_ledger(sieve_bins: int, quadrature_bins: int, triangle_bins: int):
    us,ls,uprefix,lprefix=sieve_grid(sieve_bins)
    upoints=[1+v for v in uprefix]
    lpoints=lprefix
    assert upoints[2*sieve_bins].lo<=1<=upoints[2*sieve_bins].hi
    assert lpoints[3*sieve_bins].lo<=I.point(3).log().lo
    assert lpoints[3*sieve_bins].hi>=I.point(3).log().hi
    u4=upoints[3*sieve_bins]
    u5,l5=upoints[4*sieve_bins],lpoints[4*sieve_bins]
    old_root_lower=4*I.point(3).log()
    old_root_upper=4*u4
    root_lower=F(16,5)*l5
    root_upper=F(16,5)*u5
    def U_range(s: I):
        a,b=F(s.lo),F(s.hi)
        a=max(F(1),min(F(5),a));b=max(F(1),min(F(5),b))
        left=grid_value(a,sieve_bins,us,upoints)
        right=grid_value(b,sieve_bins,us,upoints)
        # U is monotone increasing: its derivative is nonnegative.
        return I(left.lo,right.hi)
    low=enclose_integral(lambda t:4*U_range((F(5,4)-t)/t)/(t*(F(5,4)-t)),
                         F(1,4),F(5,16),quadrature_bins)
    # The excess of A1 upper over direct R1 upper is exactly the restored
    # lower contribution, by the differential equation for U and L.
    excess=enclose_integral(lambda t:4*(U_range(5-4*t)-U_range((F(5,4)-t)/t)).nonnegative()
                            /(t*(F(5,4)-t)),F(1,4),F(5,16),quadrature_bins)
    excess=excess+enclose_integral(lambda t:4*(U_range(5-4*t)-1).nonnegative()
                                  /(t*(F(5,4)-t)),F(5,16),F(1,2),quadrature_bins)
    r2=restored_mass(triangle_bins)
    assert not (excess.hi<r2.lo or r2.hi<excess.lo), 'Restoration and direct bound must agree'
    combined_r2=I(max(excess.lo,r2.lo),min(excess.hi,r2.hi))
    old_state=json.loads((ROOT/'results/signed_mass_ledger.json').read_text())
    ref095=I(Decimal(old_state['concrete_upper_lemma_target']['reference_mass']['lower']),
             Decimal(old_state['concrete_upper_lemma_target']['reference_mass']['upper']))
    rows=[]
    for theta in (F(9,10),F(37,40),F(19,20),F(97,100),F(99,100)):
        t=I.point(theta)
        tail=small_tail(theta)
        frozen=frozen_tail(theta)
        negative=low+F(16,5)*(3*t/(F(5,4)-t)).log()
        m=1+((2-t)/t).log()
        rows.append(dict(theta=str(theta),new_tail=tail.record(),frozen_tail=frozen.record(),
            tail_improvement=(frozen-tail).record(),direct_frontier_upper=negative.record(),
            first_expansion_raw_lower=(root_lower-negative).record(),
            whole_frontier_cap=root_upper.record(),cap_raw_lower=(root_lower-root_upper).record(),
            full_H_model_loss_budget=(m-tail).record(),certified_K=0))
    lo,hi=F(4,5),F(1)
    for _ in range(45):
        mid=(lo+hi)/2
        m=1+((2-I.point(mid))/I.point(mid)).log()
        difference=m-small_tail(mid)
        if difference.lo>0:hi=mid
        elif difference.hi<0:lo=mid
        else:raise AssertionError('Increase precision for threshold')
    threshold=I.segment(lo,hi)
    tail095=small_tail(F(19,20))
    critical_new=root_lower-tail095
    margin=critical_new-F(373,100)
    critical_frozen=root_lower-frozen_tail(F(19,20))
    margin_frozen=critical_frozen-F(179,50)
    assert margin.lo>0
    assert margin_frozen.lo>0
    return dict(checkpoint=4,normalization='u=N/(2 log N)',
        analytic_status='Derived propositions with proofs in NEGATIVE_FRONTIER_NOTE.md; no H or positive K',
        computations_are_not_analytic_proofs=True,
        numerical_grid=dict(sieve_bins_per_unit=sieve_bins,integral_bins=quadrature_bins,
                            restored_triangle_bins_per_coordinate=triangle_bins),
        root=dict(old_level='1',new_well_factorable_level='5/4 minus fixed slack',
                  old_lower=old_root_lower.record(),old_upper=old_root_upper.record(),
                  lower=root_lower.record(),upper=root_upper.record(),
                  lower_gain=(root_lower-old_root_lower).record()),
        levels=dict(arbitrary_outer='min(5/4-gamma,2-2*gamma), strict',
                    prime_outer='5/4-gamma, strict, for 1/4<=gamma<=1',
                    squarefree_sifting_restriction='Handled by complete multiplicative prime cutoff and Mobius expansion of gcd(e1,e2)=1',
                    gcd_expansion_q_powers=['-5/4','-7/4','-3/2','-2'],
                    arbitrary_weights_at_the_higher_total_level=False),
        restored_R2=dict(domain='1/4<=v<=t; t+3v<5/4',
                          formula='integral 4 log((5/4-t-2v)/v)/(t*v*(5/4-t-v)) dt dv',
                          coefficient=combined_r2.record(),two_dimensional_enclosure=r2.record(),
                          same_direct_sieve_gain=excess.record(),
                          must_not_add_both_gains=True),
        small_prime_tail=dict(formula='C_small(theta)=(16/5)*log((5-4*theta)/theta)',
                              new_full_H_threshold=threshold.record(),
                              frozen_baseline_replaced=False,
                              raw_source_tail_proof_still_independently_partially_audited=True),
        target095=dict(original_frontier_target='3.49',new_sufficient_target='3.73',
                       upper_bound_proved=False,critical_upper=critical_new.record(),
                       conditional_prime_margin=margin.record(),
                       sufficient_target_with_frozen_tail='3.58',
                       critical_upper_with_frozen_tail=critical_frozen.record(),
                       conditional_prime_margin_with_frozen_tail=margin_frozen.record(),
                       reference_frontier=ref095.record(),
                       allowed_reference_excess=(critical_new-ref095).record()),
        target_table=rows,certified_K=0,H_theta_proved=False)


def parity_mass_witness(ledger):
    """Numerical consequences of the abstract mass witness proved in the note.

    It lives on a long interval, not the actual indicator of J_N. It matches
    the one-sided mass interfaces and o(u) divisor axioms, not the exact
    floor remainder bound or the stronger power error of our RS reduction.
    """
    theta=F(19,20)
    t=I.point(theta)
    L0=I(Decimal(ledger['root']['lower']['lower']),Decimal(ledger['root']['lower']['upper']))
    doubled_semiprime=2*((2-t)/t).log()
    lower_frontier=L0-doubled_semiprime
    assert lower_frontier.lo>F(373,100)
    return dict(carrier='B=[N^2-H/2,N^2+H/2], H=N^2/(log(N^2))^10',
        sequence='a_m^*=(Y/H)*(1+lambda(m))*1_B(m); lambda(m)=(-1)^Omega(m)',
        nonnegative=True,prime_mass=0,
        compatible_interface='Asymptotic divisor axioms and all admitted one-sided branch mass inequalities',
        does_not_match=['Exact indicator of J_N','Individual integer floor remainders bounded by 1',
                       'The stronger power saving remainder error'],
        rough_095_mass=doubled_semiprime.record(),
        frontier_095_lower=lower_frontier.record(),
        excess_above_373_target=(lower_frontier-F(373,100)).record(),
        new_tail_gap=(small_tail(theta)-doubled_semiprime).record(),
        universal_parity_tail_gap_derivative='d(C_small-2*log((2-theta)/theta))/dtheta = -12/[theta*(5-4*theta)*(2-theta)]',
        regional_tail_bounds_also_compatible=True,
        conclusion='The mass interfaces alone cannot force K>C_small; an extra arithmetic estimate is required for this campaign',
        every_existing_mathematical_method_ruled_out=False)


def update_state(ledger):
    path=ROOT/'results/campaign_state.json'
    state=json.loads(path.read_text())
    state.update(checkpoint=4,negative_frontier_ledger='results/negative_frontier_ledger.json',
        negative_frontier_coverage='results/negative_frontier_coverage.json',
        lower_bound_status='K=0; root and small-prime cofactor sieve bounds sharpened by the derived well-factorable reduction',
        analytic_input_status='Detailed new reductions from verified RS and well-factorable sieve source statements; no prime lower bound',
        newly_derived_tail='(16/5)*log((5-4*theta)/theta)',
        frozen_tail_benchmark_unchanged=True,
        next_gate='Add a structured parity-sensitive estimate; sufficient upper bound for R_0.95 is now 3.73u using the derived root and tail bounds',
        next_gate_status='Unproved; the new 3.73 upper frontier lemma is a sufficient research target',
        full_mass_optimization_complete=False,H_theta_proved=False)
    state['milestones']['4']='New well-factorable outer and small-prime remainder reductions written; full inventory still incomplete'
    state['milestones']['5']='Direct cofactor levels and first restoration checked; whole-frontier cap applied; no full adaptive optimization'
    state['milestones']['6']='Small-modulus factorability handled; mass-only parity witness specified; no universal impossibility claim'
    state['typeII_tools_admitted_for_lower_bound']=['WF_RS_ARBITRARY_OUTER']
    state['sifting_restriction_status']='Squarefree moduli and small-prime support retained; gcd expansion has summable q powers -5/4,-7/4,-3/2,-2'
    state['active_frontier_target']=dict(kappa='19/20',new_tail_target='3.73',
        frozen_tail_target='3.58',upper_bound_proved=False)
    if 'conditional_raw_lower_bound' in state:
        state['checkpoint3_conditional_raw_lower_bound']=state.pop('conditional_raw_lower_bound')
    state['new_tail_source_route']='Independent RS plus modern well-factorable sieve formulation; original citation-chain audit remains partial'
    state['prime_terminal_comparison_tools_admitted']=[]
    state['parity_mass_witness']='results/negative_frontier_parity_witness.json'
    write_json(path,state)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sieve-bins',type=int,default=20000)
    parser.add_argument('--integral-bins',type=int,default=20000)
    parser.add_argument('--triangle-bins',type=int,default=384)
    parser.add_argument('--out',type=str,default=str(ROOT/'results'))
    args=parser.parse_args()
    if min(args.sieve_bins,args.integral_bins,args.triangle_bins)<1:
        raise ValueError('All grid sizes must be positive')
    from pathlib import Path
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    verify_baseline()
    coverage=exact_coverage_checks()
    arithmetic=finite_identities()
    ledger=make_ledger(args.sieve_bins,args.integral_bins,args.triangle_bins)
    write_json(out/'negative_frontier_coverage.json',coverage)
    write_json(out/'negative_frontier_arithmetic.json',arithmetic)
    write_json(out/'negative_frontier_ledger.json',ledger)
    write_json(out/'negative_frontier_parity_witness.json',parity_mass_witness(ledger))
    if out.resolve()==(ROOT/'results').resolve():update_state(ledger)
    print('Coverage consistency checks:',coverage['prime_piece_cases'],coverage['arbitrary_outer_cases'])
    print('Exact arithmetic identities:',len(arithmetic))
    print('New root lower:',ledger['root']['lower'])
    print('New root upper:',ledger['root']['upper'])
    print('Restored positive R2:',ledger['restored_R2']['coefficient'])
    print('New 0.95 frontier threshold:',ledger['target095']['critical_upper'])
    print('Conditional 3.73-target prime margin:',ledger['target095']['conditional_prime_margin'])
    print('Current certified K=0. No short-interval prime comparison proved.')


if __name__=='__main__':main()
