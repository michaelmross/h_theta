#!/usr/bin/env python3
"""Exact source-to-constraint audit for FI (1989), not an analytic prover."""

import ast
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "sources/fi1989_monomials.pdf"
SOURCE_SHA = "eb87421df0d868cd8c63ea163dc3be0ed7b5346ddba88f9028223cfba09afc71"
LEDGER_SHA = "c7a2b69b438c5a426bafab83c0cba2aeb0fa703046659798c1da8460e7e1378e"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(relative):
    return json.loads((ROOT / relative).read_text())


def write_json(relative, value):
    (ROOT / relative).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def add(*rows):
    return tuple(sum(items, F(0)) for items in zip(*rows))


def scale(k, row):
    return tuple(k * x for x in row)


def evaluate(row, *values):
    return sum(a * b for a, b in zip(row, (*values, F(1))))


def normalized_integer_row(row):
    from math import lcm, gcd
    denominator = lcm(*(x.denominator for x in row))
    integers = [int(x * denominator) for x in row]
    divisor = 0
    for x in integers:
        divisor = gcd(divisor, abs(x))
    return tuple(x // divisor for x in integers)


def theorem_terms():
    # Manually transcribed powers of (H,A,B,X) from printed p.325.
    # The H+B contribution is B^(1/2) after the T5 condition eta<n0.
    raw = [
        (F(-1,6), F(1,12), F(1,6), F(1,4), True),
        (F(-1,8), F(0), F(3,8), F(1,4), True),
        (F(0), F(0), F(1,2), F(1,8), True),
        (F(0), F(1,8), F(1,4), F(1,8), True),
        (F(0), F(1,2), F(0), F(0), False),
        (F(0), F(1,2), F(1), F(-1,4), False),
    ]
    # Affine coordinates below are (eta,Sigma_prime,n0,constant).
    eta = (F(1), F(0), F(0), F(0))
    total = (F(0), F(1), F(0), F(0))
    n0 = (F(0), F(0), F(1), F(0))
    m0 = add(total, scale(F(-1), n0))
    xi = (F(1), F(-1), F(0), F(2))
    prefix = scale(F(1,2), add(eta, total))
    rows = []
    q_powers = []
    for h,a,b,x,has_half in raw:
        row = add(prefix, scale(h,eta), scale(a,m0), scale(b,n0), scale(x,xi), scale(F(-1),total))
        if has_half:
            row = add(row, scale(F(1,2), n0))
        rows.append(row)
        # Free A and B lengths each shrink by q. Use H+B/q<=H+B,
        # with no claimed q saving from that half-power.
        q_powers.append(-F(1)-a-b)
    expected = [
        (7,-8,7,6), (5,-6,7,4), (5,-5,8,2),
        (5,-4,5,2), (1,0,-1,0), (1,1,2,-2),
    ]
    require([normalized_integer_row(r) for r in rows] == expected, "Theorem 6 cap derivation mismatch")
    require(all(p < -1 for p in q_powers), "Gcd powers must be summable")
    return rows, q_powers, expected


def audit_frozen_atoms():
    # Load only the two relevant definitions; do not execute the frozen
    # script's expensive enumeration or NumPy/SciPy imports.
    tree = ast.parse((ROOT / "baseline/fm_exact.py").read_text())
    definitions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in {"C","failure_atoms"}]
    namespace = {"F":F}
    exec(compile(ast.Module(body=definitions, type_ignores=[]), "frozen_FI_atoms", "exec"), namespace)
    expected = [
        [[(0,-1,1,0,0)],[(0,-3,-1,-2,1)],[(0,-12,6,4,-6)]],
        [[(1,-1,1,0,0)],[(-2,-1,-1,-2,1)],[(-7,-5,6,4,-6)]],
        [[(-1,-1,1,0,-1)],[(2,-1,-1,-2,3)],[(7,-5,6,4,1)]],
    ]
    for type_ii in [False, True]:
        actual = namespace["failure_atoms"](F(11,10), type_ii)[:3]
        require(actual == expected, "Frozen FI atom transcription mismatch")
    return {"FI0":expected[0], "FI1":expected[1], "FI2":expected[2]}


def new_region_examples(rows):
    examples = []
    for gamma,beta in [(F(19,20),F(29,100)), (F(4,5),F(11,25)),
                       (F(77,100),F(47,100)), (F(99,100),F(259,1000))]:
        total = gamma+beta
        rho = F(5,4)-total
        tau = min(1-gamma,rho,gamma-F(3,4)+7*rho,F(1))/100
        nu = tau/10
        s = total-1+tau
        require(tau>0 and 0<s<beta, "Bad full-level capacities")
        minimum = None
        endpoints = []
        # For retained products Sigma_prime>=1-nu, these linear
        # inequalities attain their extrema at the following endpoints.
        for beta_prime in [1-nu-gamma,beta]:
            delta = beta-beta_prime
            total_prime = gamma+beta_prime
            lower = s-delta
            for eta in [F(0),total_prime-1+nu]:
                for n0 in [lower,s]:
                    differences = [-evaluate(row,eta,total_prime,n0) for row in rows]
                    require(all(d>0 for d in differences), "Actual factor box fails a strict source cap")
                    smallest = min(differences)
                    minimum = smallest if minimum is None else min(minimum,smallest)
                    endpoints.append({"beta_prime":str(beta_prime),"eta":str(eta),"n0":str(n0),"minimum_exponent_saving":str(smallest)})
        require(2*gamma+beta>2, "Example should demonstrate extension beyond old arbitrary-outer region")
        examples.append({"gamma":str(gamma),"beta":str(beta),"Sigma":str(total),"rho":str(rho),
                         "full_second_capacity_exponent":str(s),"tau":str(tau),"nu":str(nu),
                         "old_second_condition_fails":True,"minimum_exponent_saving":str(minimum),
                         "affine_endpoint_checks":endpoints})
    return examples


def continuous_identities(rows):
    # Substitute the entire balanced line using affine vectors in
    # (beta,gamma,constant), rather than sampling gamma values.
    eta=(F(1),F(1),F(-1))
    total=(F(1),F(1),F(0))
    middle_base=(F(0),F(1,2),F(0))
    constant=(F(0),F(0),F(1))
    def substitute(row,n0):
        return add(scale(row[0],eta),scale(row[1],total),
                   scale(row[2],n0),scale(row[3],constant))
    middle_T6=substitute(rows[5],middle_base)
    require(middle_T6==(F(1,2),F(3,4),F(-3,4)),"Balanced T6 identity mismatch")
    lower_gap=add(eta,scale(F(-1),(F(1),F(0),F(0))))
    require(lower_gap==(F(0),F(1),F(-1)),"Balanced zero-base lower edge mismatch")
    zero_T6=substitute(rows[5],eta)
    at_gamma1=(zero_T6[0],zero_T6[1]+zero_T6[2])
    require(at_gamma1==(F(1),F(-1,4)),"Gamma-one T6 identity mismatch")
    # Coordinates (gamma,rho,constant) for beta=(6-5*gamma)/4-rho.
    beta_on_facet=(F(-5,4),F(-1),F(3,2))
    width=add((F(-4),F(0),F(5)),scale(F(-4),beta_on_facet))
    require(width==(F(1),F(4),F(-1)),"Tail uncertainty identity mismatch")
    return {"middle_T6_excess":[str(x) for x in middle_T6],
            "zero_family_lower_gap":[str(x) for x in lower_gap],
            "gamma1_zero_family_T6_excess":[str(x) for x in at_gamma1],
            "tail_uncertainty_width_lower":[str(x) for x in width]}


def main():
    require(sha(ROOT/SOURCE)==SOURCE_SHA,"1989 source hash mismatch")
    require((ROOT/SOURCE).stat().st_size==845096,"1989 source size mismatch")
    baseline = read_json("baseline/manifest.json")
    for item in baseline["files"]:
        require(sha(ROOT/item["path"])==item["sha256"],f"Baseline changed: {item['path']}")
    require(sha(ROOT/"results/negative_frontier_ledger.json")==LEDGER_SHA,"Numerical ledger changed")
    rows,q_powers,integer_rows = theorem_terms()
    frozen_atoms = audit_frozen_atoms()
    examples = new_region_examples(rows)
    identities=continuous_identities(rows)
    ledger=read_json("results/negative_frontier_ledger.json")
    require(ledger["certified_K"]==0 and not ledger["H_theta_proved"],"Unexpected proof status")
    with localcontext() as ctx:
        ctx.prec=80
        margin=Decimal(ledger["target095"]["critical_upper"]["lower"])-Decimal("3.73")
        require(margin==Decimal(ledger["target095"]["conditional_prime_margin"]["lower"]),"Conditional margin changed")
    audit={
        "checkpoint":6,"date":"2026-10-05",
        "source":{"path":SOURCE,"sha256":SOURCE_SHA,"size_bytes":845096,
                  "title":"Exponential sums with monomials","authors":"E. Fouvry and H. Iwaniec",
                  "journal":"Journal of Number Theory 33 (1989), 311-333",
                  "page_image_checks":[{"printed":324,"pdf":14,"item":"special sum and additive character"},
                    {"printed":325,"pdf":15,"item":"Theorem 6 statement and all six terms"},
                    {"printed":330,"pdf":20,"item":"Lemma 9 reciprocal-weighted sum and transfer"},
                    {"printed":331,"pdf":21,"item":"Theorem 7 conditions; epsilon_prime=48*epsilon"},
                    {"printed":332,"pdf":22,"item":"auxiliary conditions and corollary"}]},
        "source_statements_manually_verified":True,
        "printed_statements_not_verified_by_hash_or_OCR":True,
        "theorem6_integer_cap_rows_eta_Sigma_n0_constant":integer_rows,
        "theorem6_gcd_q_powers":[str(p) for p in q_powers],
        "gcd_powers_summable_without_assuming_H_le_B_over_q":True,
        "frozen_pruned_FI_atoms_match":frozen_atoms,
        "frozen_atom_scope":"Correct on Sigma<=5/4, eta<=Sigma-1; outside this region the encoding contains relaxations",
        "balanced_block_continuous_certificate":{
            "point":"mu=gamma/2, eta=beta+gamma-1",
            "FI0_lower_edge":"eta<=beta iff gamma<=1; gamma>1 fails",
            "FI0_at_gamma1_T6":"4*beta<=1; fails beyond beta=1/4",
            "FI1_and_FI2_T6":"2*beta+3*gamma<=3; impossible for gamma>=1,beta>0",
            "exact_affine_identities_checked":identities,
            "scope":"Fixed Vaughan decomposition and grouping toolkit; no universal optimality claim"},
        "pipeline_clarifications":[
            "Lemma 9 includes a_m*b_n/(mn)",
            "Three separated factors require fixed divisor-order collapse with a small loss",
            "Use signed boundary estimates or divisor-bound envelopes; Fourier weights need not be monotone",
            "State rectangular partial-sum uniformity or uniformity over the bounded coefficient families",
            "Use real initial weights or control both frequency signs via coefficient-family conjugation"],
        "theorem7":{"length":"2<=y<=sqrt(x)","epsilon_prime":"48*epsilon",
                    "N_base_conditions":["m0<1","6*n0<m0+1","2*m0+4*n0<3"],
                    "campaign_endpoint_length_handling":"Split into two comparable subintervals for literal packaged application",
                    "undecomposed_large_prime_application":False},
        "new_arbitrary_outer_reduction":{
            "condition":"0<=gamma<1; beta>0; gamma+beta<5/4; fixed margins",
            "coefficients":"Arbitrary bounded c_d; fixed full-level WF modulus weight; exact e|P(z) retained",
            "error":"O(N^(1-c)), some fixed c>0",
            "old_extra_condition_removed":"2*gamma+beta<2",
            "arbitrary_prime_weight_gamma1_endpoint_admitted":False,
            "full_capacity":"s=Sigma-1+tau for Sigma>=1",
            "actual_factor_interval":"[s-Delta,s] on retained product boxes",
            "proof":"FI_1989_AUDIT.md Section 5; examples are checks, not the uniform proof",
            "rational_examples":examples},
        "reconstructed_frozen_tail":{
            "condition":"1<=gamma<6/5, beta<(6-5*gamma)/4, fixed margins",
            "source_route":"Fixed WF sieve + Vaughan + RS + full-level coverage + gcd expansion + signed sharp transfer",
            "uncertainty_width_minus_Delta_lower":"5-4*gamma-4*beta=gamma-1+4*rho>0",
            "tail_integral":"4*integral_1^(2-theta) 1/[gamma*((6-5*gamma)/4)] dgamma = (8/3)*log((2-theta)/(5*theta-4))",
            "relevant_source_route_verified_with_addenda":True,
            "unamended_frozen_manuscript_fully_endorsed":False},
        "numerical_ledger_unchanged":{"sha256":LEDGER_SHA,"certified_K":0,"H_theta_proved":False,
                                      "conditional_target095_prime_margin_lower":str(margin)},
        "full_tool_inventory_complete":False,
        "next_gate":"Parity-sensitive estimate for the actual short interval; stronger signed upper frontier or terminal prime comparison",
        "note":"FI_1989_AUDIT.md",
    }
    state=read_json("results/campaign_state.json")
    state.update({"checkpoint":6,"fi1989_source_audit":"results/fi1989_source_audit.json",
                  "source_audit_note":"FI_1989_AUDIT.md","numerical_bounds_changed_in_checkpoint6":False,
                  "analytic_input_status":"Relevant 1989 source statements checked; reconstructed frozen tail route supplied with explicit addenda; new arbitrary-outer coefficient extension derived; no prime lower bound",
                  "negative_frontier_reduction":"Frozen positive slices reconstructed with fixed-WF/full-level/support/transfer addenda; original negative-band reuse now source-supported",
                  "new_tail_source_route":"Independent RS/WF smaller-prime route unchanged; original larger-prime source route separately reconstructed",
                  "lower_bound_status":"K=0; new arbitrary-outer coefficient range admitted; root, tail and first restoration numbers unchanged",
                  "new_arbitrary_outer_cofactor_level":"5/4-gamma, fixed loss, 0<=gamma<1",
                  "original_1989_source_available":True})
    if "WF_FI_ARBITRARY_OUTER" not in state["typeII_tools_admitted_for_lower_bound"]:
        state["typeII_tools_admitted_for_lower_bound"].append("WF_FI_ARBITRARY_OUTER")
    state["baseline"]["independent_tail_theorem_audit"]="Relevant original source statements checked; independent reconstruction supplied with explicit fixed-weight/full-level/support/signed-transfer addenda"
    state["milestones"]["1"]="Frozen inputs preserved; relevant source route checked and reconstructed with addenda"
    state["milestones"]["4"]="FI1989 source audited; arbitrary-outer level extended to 5/4-gamma below gamma=1; full tool inventory incomplete"
    require(not state["H_theta_proved"] and state["chosen_target"]["certified_K_from_current_inputs"]==0,"Unexpected campaign proof status")
    write_json("results/fi1989_source_audit.json",audit)
    write_json("results/campaign_state.json",state)
    print("Checkpoint 6: source identity, 6 exact caps, 9 frozen FI atoms and 4 full-factor examples checked; numerical ledger unchanged; K=0.")


if __name__=="__main__":
    main()
