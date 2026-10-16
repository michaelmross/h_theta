#!/usr/bin/env python3
"""Checkpoint 7: a negative branch improvement and scoped source tests.

Standard library only. Interval computations enclose asymptotic main-term
constants; they are not numerical proofs of short-interval distribution.
Historical results are read, never rewritten.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

from campaign import verify_baseline
from structured_frontier import I, ROOT, write_json


def read_interval(record):
    return I(Decimal(record['lower']), Decimal(record['upper']))


def intersect(a, b):
    return I(max(a.lo, b.lo), min(a.hi, b.hi))


def sieve_grid_to_eight(bins):
    """Causal outward enclosure of normalized U,L on [1,8].

    Explicit initial data: U=1 through 3; L=0 through 2 and
    L=log(s-1) through 4. Later cell integrands use an already
    enclosed cell shifted by one. No floating point ODE solver.
    """
    h = F(1, bins)
    us, ls = [], []
    uprefix, lprefix = [I.point(0)], [I.point(0)]
    for i in range(7 * bins):
        a, b = 1 + i*h, 1 + (i+1)*h
        if i < 2*bins:
            u, uint = I.point(1), I.point(0)
        else:
            uint = ls[i-bins] / I.segment(a-1, b-1) * h
            u = I((1+uprefix[-1]).lo, (1+uprefix[-1]+uint).hi)
        if i < bins:
            l = lint = I.point(0)
        elif i < 3*bins:
            l, lint = I.segment(a-1, b-1).log(), I.point(0)
        else:
            lint = us[i-bins] / I.segment(a-1, b-1) * h
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
    return 1+uprefix[-1], lprefix[-1], 1+uprefix[4*bins], lprefix[4*bins]


def negative_third_branch(bins):
    """Upper main terms for 3/4 <= sigma <= 19/20, ordered outer primes.

    rho3(sigma)=(1/3)*int_(1/4)^(sigma-1/2)
                  log(4*(sigma-v)-1)/(v*(sigma-v)) dv.
    Map v=1/4+(sigma-3/4)*r so no moving interval remains.
    The upper-sieve coefficient is 4/beta. The direct positive
    difference is enclosed separately to avoid cancellation losses.
    """
    low, high = F(3,4), F(19,20)
    hs, hr = (high-low)/bins, F(1,bins)
    old, new, gain = I.point(0), I.point(0), I.point(0)
    for i in range(bins):
        sigma = I.segment(low+i*hs, low+(i+1)*hs)
        gap = (sigma-low).nonnegative()
        old_beta, new_beta = 2-2*sigma, F(5,4)-sigma
        # 1/old_beta-1/new_beta has numerator sigma-3/4.
        beta_gain = gap/(old_beta*new_beta)
        for j in range(bins):
            r = I.segment(j*hr, (j+1)*hr)
            v = F(1,4)+gap*r
            integrand = F(4,3)*gap*(1+4*gap*(1-r)).log()/(v*(sigma-v))
            cell = integrand.nonnegative()*hs*hr
            old = old + cell/old_beta
            new = new + cell/new_beta
            gain = gain + cell*beta_gain
    return dict(
        arithmetic_term='sum over p1>p2>p3>=N^(1/4), p1*p2*p3<=N^(19/20), of S_(p1*p2*p3)(p3)',
        sign_in_third_buchstab_lower_ledger='negative',
        outer_exponent_range=['3/4','19/20'],
        old_level='min(5/4-sigma,2-2*sigma), minus fixed slack',
        new_level='5/4-sigma, minus fixed slack',
        upper_coefficient_density='4*rho3(sigma)/beta(sigma)',
        rho3_formula='(1/3)*int_(1/4)^(sigma-1/2) log(4*(sigma-v)-1)/(v*(sigma-v)) dv',
        normalized_by='u=N/(2 log N)',
        old_upper_coefficient=old.record(), new_upper_coefficient=new.record(),
        coefficient_reduction=gain.record(), grid_per_coordinate=bins,
        new_positive_branch_region=False,
        whole_frontier_095_upper_improved=False,
        unestimated_third_frontier_products='sigma>19/20',
        endpoints_sigma_equal_one_admitted=False,
        parent_accounting_identity='(4/beta)*log((beta-b)/b)-int_b^c 4/[t*(beta-t)] dt=(4/beta)*log((beta-c)/c)',
        parent_accounting_scope='1/2<=sigma2<3/4; b<=c<beta; full child range covered',
        parent_direct_sieve_gain_must_not_be_double_counted=True,
        proof_location='FRONTIER_INVESTIGATION_NOTE.md Section 2')


# Affine exponent vectors: constant, eta, Sigma, standalone denominator a.
def add(*vectors):
    return tuple(sum(v[j] for v in vectors) for j in range(4))


def scale(c, vector):
    return tuple(F(c)*x for x in vector)


def vector_record(v):
    return dict(zip(('constant','eta','Sigma','a'), map(str,v)))


def source_certificates():
    eta, sigma, a = (F(0),F(1),F(0),F(0)), (F(0),F(0),F(1),F(0)), (F(0),F(0),F(0),F(1))
    xi = add((F(2),F(0),F(0),F(0)), eta, scale(-1,sigma))
    pair = add(eta,sigma,scale(-1,a))
    thm3 = [
        add(scale(F(1,4),xi),scale(F(1,2),a),scale(F(3,4),pair)),
        add(scale(F(7,10),a),pair),
        add(a,scale(F(3,4),pair)),
        add(scale(F(-1,4),xi),scale(F(11,10),a),pair)]
    assert thm3 == [(F(1,2),F(1),F(1,2),F(-1,4)),
                    (F(0),F(1),F(1),F(-3,10)),
                    (F(0),F(3,4),F(3,4),F(1,4)),
                    (F(-1,2),F(3,4),F(5,4),F(1,10))]
    thm4 = [
        add(eta,scale(F(1,8),xi),scale(F(3,4),sigma)),
        add(eta,sigma,scale(F(-1,5),a)),
        add(eta,scale(F(17,20),sigma),scale(F(3,20),a)),
        add(eta,scale(F(-1,8),xi),scale(F(21,20),sigma))]
    assert thm4[0] == (F(1,4),F(9,8),F(5,8),F(0))
    assert thm4[3] == (F(-1,4),F(7,8),F(47,40),F(0))
    thm2_first = scale(F(1,2),add(xi,eta,sigma))
    thm5_first = add(scale(F(1,2),xi),scale(F(3,4),add(sigma,scale(-1,a))),a)
    assert thm2_first == (F(1),F(1),F(0),F(0))
    assert add(thm5_first,scale(-1,sigma)) == (F(1),F(1,2),F(-3,4),F(1,4))
    source = ROOT/'sources/fi1989_monomials.pdf'
    return dict(
        primary_source='Fouvry-Iwaniec, Exponential sums with monomials, JNT 33 (1989), 311-333',
        source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        equations_read_on_page_images=[313,314,315,317,323,324],
        campaign_phase='h*N^2/(denominator product)',
        source_phase_exponent='xi=eta+2-Sigma',
        raw_remainder_target='o(N^Sigma), with all fixed losses absorbed',
        theorem1=dict(page=313, bound='X^(-1/2)*(X+M)^(1/2)*(X+B)^(1/2)*norm2(phi)*norm2(psi)',
            application='h versus collapsed denominator product',
            unit_coefficient_exponent='max(eta+1,Sigma+eta/2)',
            fixed_h_alternative_at_top='Exponent at least (3/2)*Sigma-1/2, exceeding Sigma for Sigma>1',
            top_frequency='eta=Sigma-1',
            status='No generic power saving at that height; prime sparsity alone has not been analyzed as a new spacing theorem'),
        theorem2=dict(page=314, coefficients='arbitrary separate joint coefficients phi_(m1,m2), psi_(m3,m4)',
            phase_exponents='all alpha_j != 0; exponent 1 permitted',
            first_term='(X*M1*M2*M3*M4)^(1/2)',
            first_remainder_exponent=vector_record(thm2_first),
            at_top_frequency='equals Sigma for every grouping',
            fixing_h_and_summing_absolutely='First term exponent eta+(xi+Sigma)/2=1+(3/2)*eta, exceeding Sigma at eta=Sigma-1 and Sigma>1',
            direct_prime3_fourier=dict(period='T comparable to N^2',
                product_of_lengths='H*N^2', phase_parameter='X comparable to H',
                first_term='H*N', at_H_equal_N='N^2, with an additional logarithmic factor in the printed bound',
                sufficient_target='N^2 times a sufficiently negative power of log N',
                conclusion='The printed bound does not supply the requested comparison')),
        theorem3=dict(page=315, standalone_phase_exponent='alpha != 0,1',
            coefficients='phi_m separate from arbitrary joint psi_(m1,m2)',
            exponents=list(map(vector_record,thm3)),
            necessary_caps=['a>=4*eta+2-2*Sigma','a>=(10/3)*eta',
                            'a<=Sigma-3*eta','a<=5-(15/2)*eta-(5/2)*Sigma'],
            necessary_total_level_at_top='Sigma<=19/16',
            fixing_h_alternative='Second and third terms require a>=(10/3)*eta and a<=Sigma-4*eta; at top Sigma<=22/19',
            first_three_caps_are_stronger_than_RS=True,
            direct_prime_product_status='Inadmissible: each unreworked product-phase exponent is 1'),
        theorem4=dict(page=317, phase_exponents='both alpha_j != 0,1',
            exact_bound_terms=['X^(1/8)*(M1*M2)^(3/4)','M1^(4/5)*M2',
                               'M1*M2^(17/20)','X^(-1/8)*(M1*M2)^(21/20)'],
            fixed_h_summed_exponents=list(map(vector_record,thm4)),
            first_term_necessary_at_top='Sigma<=7/6',
            fourth_term_necessary_at_top='Sigma<=15/14',
            direct_prime_product_status='Inadmissible: both unreworked product-phase exponents are 1'),
        theorem5=dict(pages=[323,324],phase='m1^alpha1*m2^alpha2*(m3/m4)^alpha',
            coefficients='phi_(m1,m2), psi_m3; m4 has unit coefficient',
            printed_hypothesis='alpha != 1, alpha*alpha1*alpha2 != 0',
            proof_hypothesis='Lemma 7 applied with -alpha requires alpha != -1; beta=alpha/(alpha+1)',
            discrepancy_at_reciprocal_alpha_minus_one=True,
            admitted_at_alpha_minus_one=False,
            formal_free_h_mapping='m4=h, alpha=-1, m3 one denominator variable',
            first_term_exponent=vector_record(thm5_first),
            formal_top_excess_over_target='(a+2-Sigma)/4 > 0 for Sigma<2',
            direct_prime_product_status='No opposite exponent pair; the free slot cannot be replaced by a prime indicator'),
        equality_is_not_a_power_saving=True,
        scope='These direct mappings and the published unit-coefficient bounds; not every possible use of the paper or its spacing lemmas',
        new_prime_comparison_admitted=False)


def mass_certificate(bins):
    upper8, lower8, upper5, lower5 = sieve_grid_to_eight(bins)
    old = json.loads((ROOT/'results/negative_frontier_ledger.json').read_text())
    reference = json.loads((ROOT/'results/signed_mass_ledger.json').read_text())
    # Independent delay equations must overlap the preserved root and Buchstab enclosures.
    root5_lower = F(16,5)*lower5
    root5_upper = F(16,5)*upper5
    intersect(root5_lower,read_interval(old['root']['lower']))
    intersect(root5_upper,read_interval(old['root']['upper']))
    ordinary_root = intersect(lower8+upper8,read_interval(reference['reference']['A0']))
    theta = I.point(F(19,20))
    logtail = ((2-theta)/theta).log()
    ordinary_frontier = ordinary_root-(1+logtail)
    witness_root = 2*lower8
    witness_frontier = witness_root-2*logtail
    frontier_gap = witness_frontier-ordinary_frontier
    assert witness_frontier.lo>Decimal('4.29')
    delta = F(169,500)  # 0.338, a sufficient one-sided centered target.
    centered_upper = ordinary_frontier+delta
    assert centered_upper.hi<Decimal('3.73')
    prime_margin = read_interval(old['target095']['critical_upper'])-centered_upper
    assert prime_margin.lo>0
    return dict(
        bins_per_unit=bins,
        normalized_sieve_functions=dict(U8=upper8.record(),L8=lower8.record()),
        identity='L(s)+U(s)=s*omega(s)',
        independent_buchstab_overlap_verified=True,
        preserved_level_5_root_overlap_verified=True,
        ordinary_root=ordinary_root.record(), ordinary_frontier_095=ordinary_frontier.record(),
        parity_witness=dict(sequence='(Y/H)*(1+lambda(m))*1_B(m)',
            carrier='B centered at N^2, H=N^2/(log(N^2))^10',
            root_asymptotic_coefficient='2*L(8)', root=witness_root.record(),
            frontier_asymptotic_coefficient='2*L(8)-2*log(21/19)',
            frontier=witness_frontier.record(), excess_above_373=(witness_frontier-F(373,100)).record(),
            centered_excess=frontier_gap.record(),
            exact_short_support=False, individual_floor_bound=False, stronger_power_error=False,
            applicable_scope='Extracted o(u) divisor axioms and one-sided signed branch mass inequalities'),
        proposed_centered_target=dict(kappa='19/20',allowed_excess='169/500',
            reference='centered B_N of length Y1=N^2*exp(-3*(log(N^2))^(1/3)); scaled by Y/Y1',
            arithmetic_inequality='R_0.95(J_N)-(Y/Y1)*R_0.95(B_N)<=(0.338+o(1))*u',
            quantifier='every sufficiently large even N',
            implied_upper_coefficient=centered_upper.record(),
            conditional_prime_margin=prime_margin.record(),
            proved=False,full_H_implied=False),
        no_new_positive_sieve_region=dict(reason='beta>2*c>=1/2 and beta<=5/4-sigma force sigma<3/4',
                                         all_chains_cutoff_at_least='1/4'),
        certified_K=0,H_theta_proved=False)


def update_state():
    path=ROOT/'results/campaign_state.json'
    state=json.loads(path.read_text())
    state.update(checkpoint=7,date='2026-10-06',source_audit_note='FRONTIER_INVESTIGATION_NOTE.md',
        frontier_investigation='results/frontier_investigation.json',
        negative_third_branch='results/third_frontier_upper.json',
        remaining_fi_source_audit='results/fi_remaining_bounds.json',
        lower_bound_status='K=0; a fixed negative third-frontier piece has a lower upper cost; no aggregate target proved',
        numerical_bounds_changed_in_checkpoint7='New regional negative-branch costs and sharper parity diagnostics; frozen aggregate ledger unchanged',
        next_gate='Prove the actual centered R_0.95 comparison with allowed excess 0.338u, or supply another parity-sensitive signed comparison',
        next_gate_status='Unproved; sufficient for a positive prime coefficient, not full H',
        full_tool_inventory_complete=False,full_mass_optimization_complete=False,H_theta_proved=False)
    state['milestones']['4']='FI Theorems 1-7 direct interfaces checked; focused recent literature checked; full inventory incomplete'
    state['milestones']['5']='A fixed third-frontier negative branch upper cost improved; aggregate frontier target remains unproved'
    state['milestones']['6']='Parity witness mass sharpened; scoped source endpoint certificates supplied; actual arithmetic comparison still needed'
    state['active_frontier_target']['centered_allowed_excess']='0.338'
    state['active_frontier_target']['centered_upper_bound_proved']=False
    write_json(path,state)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sieve-bins',type=int,default=20000)
    parser.add_argument('--branch-bins',type=int,default=384)
    parser.add_argument('--out',type=Path,default=ROOT/'results')
    args=parser.parse_args()
    if min(args.sieve_bins,args.branch_bins)<1:
        raise ValueError('Grid sizes must be positive')
    verify_baseline()
    source=source_certificates()
    mass=mass_certificate(args.sieve_bins)
    branch=negative_third_branch(args.branch_bins)
    assert read_interval(branch['coefficient_reduction']).lo>0
    assert read_interval(branch['old_upper_coefficient']).lo>read_interval(branch['new_upper_coefficient']).hi
    args.out.mkdir(parents=True,exist_ok=True)
    write_json(args.out/'fi_remaining_bounds.json',source)
    write_json(args.out/'frontier_investigation.json',mass)
    write_json(args.out/'third_frontier_upper.json',branch)
    if args.out.resolve()==(ROOT/'results').resolve():
        update_state()
    print('New third-frontier upper coefficient:',branch['new_upper_coefficient'])
    print('Regional cost reduction:',branch['coefficient_reduction'])
    print('Parity witness frontier:',mass['parity_witness']['frontier'])
    print('Centered target conditional prime margin:',mass['proposed_centered_target']['conditional_prime_margin'])
    print('K=0; aggregate frontier comparison and H remain unproved.')


if __name__=='__main__':
    main()
