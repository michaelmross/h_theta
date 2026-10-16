# Normalizing the four-factor comparison

Checkpoint 31 — Michael M. Ross's H(ϑ) campaign — 13 October 2026

**The continuous all-Type-I contribution and the normalized long
Type-II aggregate are now removed at cost o(u). The sharp short-window
comparison remains unproved.**

This is a normalization lemma for the actual checkpoint-30 weight.
It supplies no lower estimate for its remaining short count. All five
logarithmic moments, all physical gates, and the complete Vaughan
identity are retained. The original .007935/.011 coefficients are unchanged.

## 1. Exact arithmetic interface

Keep x=N², Y=N+1, u=N/(2 log N), even N, κ=1/1000, the original
H₁=2 floor(x exp(−3(log x)^(1/3))/2)+1, a_N=Y/H₁, and
ρ=H₁/x=N^(−o(1)). The auxiliary detector cutoff is
U=floor(N^(1/1000)); it is not a discarded original least-prime sector.

Write ℓ=log N and let

\[
\mathcal D_N=\{\boldsymbol v:N^{2/5}\le v_1\le N^{43/100},
                     \ v_2,v_3,v_4\ge v_1\}.
\]

For j=1,…,5 put c_j=(−1)^(j+1) binomial(5,j) and

\[
g_{j,N}(\boldsymbol v)=\frac1{\log v_1}
 \frac{\prod_{i=2}^4(\log v_i)^{j-1}}{(\log(x/v_1))^{3j}}.
\tag{1}
\]

The exact integer detector count is

\[
\mathcal P_N(\psi)=\frac16\sum_{j=1}^5c_j27^j
 \sum_{\boldsymbol v\in\mathcal D_N\cap\mathbb Z^4}
 g_{j,N}(\boldsymbol v)\prod_{i=1}^4\Lambda(v_i)
 \psi(v_1v_2v_3v_4).
\tag{2}
\]

Checkpoint 30 proves W_N(ψ_Y)=P_N(ψ_Y)+o(u) and
a_N W_N(ψ_H₁)=a_N P_N(ψ_H₁)+o(u), including proper-power padding
and denominator freezing. These complete-count estimates are used before
any detector expansion.

Let A_U=I₁+I₂, with the complete identity Λ=A_U+II:

\[
\begin{aligned}
I_1(v)&=\sum_{d\mid v,\ d\le U}\mu(d)\log(v/d),\\
I_2(v)&=-\sum_{db\mid v,\ d,b\le U}\mu(d)\Lambda(b),\\
II(v)&=\sum_{mb=v,\ m>U,\ b>U}\beta_U(m)\Lambda(b),
\quad \beta_U(m)=-\sum_{d\mid m,\ d\le U}\mu(d).
\end{aligned}
\tag{3}
\]

Every physical variable is greater than U for all sufficiently large N.
Define A_N(ψ) by replacing the four Λ factors in (2) by A_U.
Define B_N(ψ)=P_N(ψ)−A_N(ψ). The fully expanded A_N has
5·2⁴=80 signed subterms; B_N contains the other
5·(3⁴−2⁴)=325 signed subterms. Each of these 325 has at least one II.
No prime mask is placed on a free integer variable. In particular B_N
is a signed aggregate, not a nonnegative count.

## 2. Combine the small coefficients before integration

Define the finite harmonic sums

\[
m_U=\sum_{d\le U}\frac{\mu(d)}d,\quad
l_U=\sum_{d\le U}\frac{\mu(d)\log d}d,\quad
s_U=\sum_{b\le U}\frac{\Lambda(b)}b.
\]

Changing each free variable v=df or v=dbf to its physical variable
in the continuous integrals gives exactly the one-slot density

\[
\begin{aligned}
\mathfrak a_U(t)
 &=\sum_{d\le U}\frac{\mu(d)}d\log(t/d)
   -\sum_{d,b\le U}\frac{\mu(d)\Lambda(b)}{db}\\
 &=m_U(\log t-s_U)-l_U.
\end{aligned}
\tag{4}
\]

The Jacobians 1/d and 1/(db) are necessary. Once expressed in physical
variables, the band and ordering gates are independent of d,b. Finite
expansion and integration therefore commute with those exact gates.

The quantitative long Möbius PNT gives M(T)≪T exp(−c√log T).
A checked primary formulation is [Lee–Leong, arXiv:2208.06141v4,
Theorem 1.1](https://arxiv.org/html/2208.06141v4).
Partial summation implies, for every fixed A>0,

\[
m_U=O_A((\log U)^{-A}),\qquad
l_U=-1+O_A((\log U)^{-A}),\qquad s_U\ll\log U.
\tag{5}
\]

For clarity, the constants 0 and −1 in (5) follow from the limits at
s=1 of 1/ζ(s) and −(1/ζ)'(s). The bound on M(T) makes the associated
series and their logarithmic derivatives converge at s=1 by partial
summation; these are not absolutely convergent sums of |μ(d)|/d.
For example, M(T)≪_B T/(log T)^B bounds the two tails by
O_B((log U)^(1−B)) and O_B((log U)^(2−B)). Choose B larger than A.

On the physical support of either window,
N^(2/5)≤t_i≪N^(4/5), and log U∼ℓ/1000. Consequently

\[
\boxed{\mathfrak a_U(t_i)=1+O_A(\ell^{-A})}
\tag{6}
\]

uniformly for every fixed A. The small-coefficient cancellation is
performed before bounding the continuous mean; no factor N^ε is
multiplied by the slowly vanishing ρ in this step.

## 3. The exact continuous comparison

Let

\[
\mathcal C_N(\psi)=\frac16\sum_{j=1}^5c_j27^j
 \int_{\mathcal D_N}g_{j,N}(\boldsymbol t)
     \prod_{i=1}^4\mathfrak a_U(t_i)\,
     \psi(t_1t_2t_3t_4)\,d\boldsymbol t,
\tag{7}
\]

and let C_N⁰ have all four densities in (7) replaced by 1.
This C_N is the sum of the actual all-Type-I continuous integrals,
not a newly chosen reference.

The five moment weights recombine exactly to

\[
\sum_{j=1}^5c_j27^jg_{j,N}(\boldsymbol t)
 =\frac{\Phi_5\left(27\log t_2\log t_3\log t_4/
                              (\log(x/t_1))^3\right)}
        {\log t_1\log t_2\log t_3\log t_4}.
\tag{8}
\]

To make the dependence on the product explicit, set τ=log_N t for
t=t₁t₂t₃t₄, α=log_N t₁, b=log_N t₂, c=log_N t₃,
d=τ−α−b−c. Coarea, with dt₄=dt/(t₁t₂t₃), yields

\[
\mathcal C_N^0(\psi)=\int_0^\infty\psi(t)\frac{J(\log_N t)}{6\ell}\,dt,
\tag{9}
\]

where the fixed function is

\[
J(\tau)=\int_{.40}^{.43}
 \iint_{b,c\ge\alpha,\ d=\tau-\alpha-b-c\ge\alpha}
 \frac{\Phi_5(27bcd/(2-\alpha)^3)}{\alpha bcd}\,db\,dc\,d\alpha.
\tag{10}
\]

For |τ−2|≤.01, put R=τ−4α and transform the triangular domain by
b=α+Rs, c=α+Rt, d=α+R(1−s−t), where s,t≥0 and s+t≤1.
Here .27≤R≤.41 and all four exponents are bounded away from zero.
The Jacobian is R². The resulting integrand and its τ derivative are
bounded on this fixed compact domain. Thus J is continuously
differentiable there, and J(τ)=J(2)+O(|τ−2|).

An explicit derivative bound is available without quadrature. The
three residual exponents are at most .81, ν≤(158/157)³<2 by AM–GM,
and 0≤Φ₅(ν)≤2, |Φ₅′(ν)|≤5. The transformed ν derivative is at
most Q=27(.81)²/(1.57)³. Bounding the derivative of the reciprocal
product by 1/.40 times itself gives

\[
|J'(\tau)|\le\frac{.03}{2(.40)^4}
 \{4(.41)+(.41)^2(5Q+2/.40)\}<4.
\tag{10a}
\]

The original trapezoids have the exact areas
∫ψ_Y=(1+κ)Y and a_N∫ψ_H₁=(1+κ)Y. Their supports satisfy
|log(t/x)|≪ρ+1/N. Applying (9), the constant terms cancel exactly:

\[
\mathcal C_N^0(\psi_Y)-a_N\mathcal C_N^0(\psi_{H_1})
 =O\left(\frac{N(\rho+1/N)}{\ell^2}\right)=o(u).
\tag{11}
\]

Each individual moment integral with absolute coefficients is O(H/ℓ)
on ψ_H. This follows from the same coarea change, since g_j scales
as ℓ^(−4) and the three reciprocal integrations contribute ℓ³.
Equation (6) therefore gives

\[
\mathcal C_N(\psi_Y)-a_N\mathcal C_N(\psi_{H_1})=o(u).
\tag{12}
\]

In addition to (11), the bound is O_A(N/ℓ^(A+1)). No fixed
reference-enclosure width is discarded: the proof uses the continuous
density itself and the actual normalized long count below.

## 4. A uniform long-window lattice bound

Define the exact discrepancy L_N(ψ)=A_N(ψ)−C_N(ψ).
Here each all-Type-I row has four free integer factors with
v_i=h_i f_i and h_i≤U². Its physical band, ordering gates and smooth
logarithms remain in the discrepancy.

**Lemma 1.** For either original trapezoid,

\[
|\mathcal L_N(\psi_H)|\ll
 N^{8/5}U^2\ell^{12}\le N^{801/500}\ell^{12}.
\tag{13}
\]

Proof. Partition the physical factors into dyadic boxes
v_i∈[V_i,2V_i]. There are O(ℓ⁴) boxes, all V_i≳N^(2/5);
a box meeting the product support has V₁V₂V₃V₄≪x. For a fixed
small-coefficient row put F_i=V_i/h_i. All F_i≫N^(.398).

After the four detector logarithms or small Λ(b) coefficients are
included, the weight of this row is O(1), with bounded total variation
in each free variable. Indeed, g_j contributes ℓ^(−4), the four
detector factors contribute at most ℓ⁴, and the remaining logarithmic
ratios have bounded variation on the physical boxes. The exact ordering
gates cut each one-variable section into an interval. The trapezoid
has bounded variation independently of H: a narrow ramp changes its
derivative, but not its total variation.

Telescoping four one-dimensional sum-minus-integral comparisons,
including mixed sums and integrals over the other axes, bounds the
row by

\[
C\sum_i\prod_{k\ne i}F_k
 \ll N^{8/5}\sum_i\frac1{\prod_{k\ne i}h_k}.
\tag{14}
\]

This is the bounded-variation Euler summation bound. No mixed
derivative bound or smooth replacement of a gate is assumed.

In the i-th summand, the offending slot has at most U+U² choices
of its I₁ divisor or I₂ pair (d,b). Each other slot contributes at most
Σ_(d≤U)1/d+Σ_(d,b≤U)1/(db)≪ℓ². Keeping absolute row coefficients
only at this lattice-error step, summing (14) and the boxes gives
O(N^(8/5)U²ℓ^10). The displayed ℓ¹² is a harmless upper envelope.
The finite five-moment constants do not depend on N. □

Since a_N≍1/(Nρ), Lemma 1 proves

\[
\boxed{a_N\mathcal L_N(\psi_{H_1})
 \ll N^{301/500}\rho^{-1}\ell^{12}=o(u).}
\tag{15}
\]

The available power margin is 199/500 before the subpower and
logarithmic factors. This proof does not give L_N(ψ_Y)=o(u): the
unscaled short bound (13) is larger than the target scale N/ℓ.

## 5. The normalized long Type-II aggregate

**Lemma 2.** The complete 325-term aggregate satisfies

\[
\boxed{a_N\mathcal B_N(\psi_{H_1})=o(u).}
\tag{16}
\]

Proof. First compare the full Λ detector count (2) on the long window
with C_N⁰. For a fixed physical dyadic box and three fixed variables,
the remaining section is an interval with the exact gates and a
bounded-variation weight. Ordinary long PNT in the form

\[
\sum_{v\le T}\Lambda(v)=T+O(T e^{-c\sqrt{\log T}})
\tag{17}
\]

allows replacement of its Λ measure by Lebesgue measure with
error O(V_i e^(−c′√ℓ)ℓ^(−4)). This follows by partial summation
using the summatory error at the section endpoints; it does not
assume a PNT on the square-root short window.

One primary quantitative formulation is [Johnston–Yang,
arXiv:2204.01980v2, Theorem 1.1](https://arxiv.org/html/2204.01980v2).
Its fixed polynomial factor in log T can be absorbed in a slightly
smaller c. Summing or integrating the other axes uses their O(V_k)
Λ masses. Telescoping the four replacements and summing the dyadic
boxes therefore bounds |P_N(ψ_H₁)−C_N⁰(ψ_H₁)| by
O(x e^(−c′√ℓ)ℓ^12). In the prescribed normalization this is

\[
O(N\rho^{-1} e^{-c'\sqrt\ell}\ell^{12})=o(u),
\tag{18}
\]

because the original ρ⁻¹ has logarithm O(ℓ^(1/3)). This last
comparison needs that actual H₁, not just an arbitrary subpower width.

Equations (6) and (15) give
a_N A_N(ψ_H₁)=a_N C_N⁰(ψ_H₁)+o(u). Subtract this from the
full-detector comparison (18) to obtain (16). This proves the signed
aggregate statement; it makes no assertion about separate absolute
values of its 325 terms. □

## 6. New short-window form of the remaining estimate

The exact identities P_N=A_N+B_N and A_N=C_N+L_N, together with
(12), (15), (16) and checkpoint-30 padding, prove the new interface

\[
\boxed{\Delta\mathcal W_N
 =\mathcal L_N(\psi_Y)+\mathcal B_N(\psi_Y)+o(u).}
\tag{19}
\]

Thus the actual band comparison is reduced to

\[
\boxed{\mathcal L_N(\psi_Y)+\mathcal B_N(\psi_Y)
 \ge-(\eta_W+o(1))u.}
\tag{20}
\]

This is a signed, coupled inequality. Bounds with
L_N(ψ_Y)≥−(η_I+o(1))u and B_N(ψ_Y)≥−(η_II+o(1))u would suffice
with η_W=η_I+η_II, but no such bounds are proved here. A direct
estimate for their sum may retain cancellations lost by separation.

The ordinary unrestricted d₄ short-interval theorem does not fill the
gap. The checked primary publisher abstract of [Garaev–Luca–Nowak,
Archiv der Mathematik 86 (2006), 60–66](https://link.springer.com/article/10.1007/s00013-005-1447-2)
states an asymptotic when the length is large compared with
√X log X. Our original length is Y∼√x. Even after fixing the small
product D=∏h_i, the proposed free-product interval has X=x/D and
length Y/D, with

\[
\frac{Y/D}{\sqrt{x/D}\log(x/D)}
 =\frac{1+o(1)}{\sqrt D\log(x/D)}\longrightarrow0
\quad(1\le D\le U^8).
\tag{21}
\]

Its stated range fails already at D=1, and the physical gates are
an additional requirement. Only the publisher's abstract was
available; no finer statement from the inaccessible full article is
asserted or excluded. This check rejects the direct invocation of that
stated result, not other four-variable methods.

## 7. Unchanged coefficient ledger and next task

| Input | Checkpoint 31 status |
|---|---|
| Exact all-Type-I continuous density | (4), proved with all small coefficients and gates |
| Centered continuous contribution | o(u), proved |
| Normalized long all-Type-I lattice error | o(u), proved |
| Normalized long signed Type-II aggregate | o(u), proved collectively |
| Short all-Type-I lattice error at scale u | Unproved; (13) is only a coarse bound |
| Short signed Type-II aggregate with sharp coefficient | Unproved |
| Sharp lower bound for their coupled sum | (20), unproved |
| New nonvanishing normalization charge | Zero |

The next analytic task is (20) on the actual short window. Retain all
physical gates, all five moments and the 325 signed Type-II subterms.
The previous two Robert–Sargos source obstructions are preserved;
this normalization is not a successful new mapping of their bounds.

As before, the exact base and other degree bands remain in η_rest,
and η_W+η_rest≤.000099 is required. The already proved reference
loss .000001 is retained inside the existing .0001 complement budget.
The sufficient original coefficient remains

\[
.003065+.007825257+.000001+\eta_W+\eta_{\rm rest}
             +\xi+21147/L\le .011.
\tag{22}
\]

The spectral version omits .003065 and has allowance .007935.
Any later fixed original least-prime power deletion still requires ξ
from checkpoint 22, (23). A fixed complete-transform multiplier still
requires 21147/L; a growing multiplier gives o(u). Neither deletion
is introduced here. The full sharp comparison, H(ϑ), the exact
base/rest comparisons and the optional marked task remain open;
K=0 and milestone 7 remains deferred.

Run `python3 src/four_factor_normalization.py` for the exact finite
coefficient, tensor, coarea and budget checks. These check the
identities and the recorded margins; the uniform statements above
are analytic proofs, not inferences from the fixtures. All 299
nonmutable checkpoint-30 records are preserved byte for byte.
