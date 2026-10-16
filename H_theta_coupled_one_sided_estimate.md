# A one-sided coupled bound and a positive complementary count

Checkpoint 27 — Michael M. Ross's H(ϑ) campaign — 12 October 2026

**The sharp signed .007935u estimate remains unproved.** The entire
three-term expression in checkpoint 26, (24), now has the uniform
one-sided upper bound

\[
\mathcal T_h(N)\le(1.441618+o(1))u.
\tag{1}
\]

This improves its previous 4.945625 envelope while keeping the actual
coefficients together. It is still much larger than the sufficient
.0135582 coefficient.

There is also a useful transfer to a positive complementary count.
The admitted root upper sieve, combined with its ordinary long
reference, bounds the centered **rough-integer** count by .007825257u.
A separate lower comparison for the rough integers not carrying the
original prime marks, allowing a deficit of .0001u, would then prove
the original .007935u integral bound. This lower comparison is not
proved here. The rough count and the marked prime-product count are
different arithmetic objects.

The next investigation is the switched lower-weight construction in
Section 8. Its pointwise, reference-loss and comparison requirements
are explicit; its viability remains unproved.

## 1. Retain the original comparison

Use x=N², Y=N+1, u=N/(2 log N), z=N^(1/4), κ=1/1000 and even N.
Keep the original c_N, all least-prime sectors and every frozen
ordering gate:

\[
c_N(d)=\mathbf1_{d\ {\rm prime},\ z\le d<N^{19/20}}
+\frac12\sum_{pr=d\atop p,r\ge z\ {\rm prime}}
 \mathbf1_{pr\max(p,r)\le x},
\qquad
q_N(n)=\sum_{dq=n,\ q\ {\rm prime}}c_N(d).
\tag{2}
\]

Write Q_N(w)=Σ_n q_N(n)w(n). Retain

\[
H_1=2\lfloor xe^{-3(\log x)^{1/3}}/2\rfloor+1,\qquad
a=Y/H_1,\qquad \rho=H_1/x=N^{-o(1)}.
\]

The inherited smoothed comparison is

\[
I_\kappa=Q_N(\psi_Y)-aQ_N(\psi_{H_1}),
\qquad
I_\kappa=\mathfrak H_\kappa(N)+o(u).
\tag{3}
\]

The original smoothing charge is .003065 and the signed allowance
is .007935, summing to .011. The positive kernel ψ_h is an average
of centered sharp windows with real widths in [h,(1+2κ)h];
its area is (1+κ)h. No transform or frequency-band coefficient
is individually replaced in this argument.

For the checkpoint-26 hybrid union G_h, new double-identity region
G_2 and hybrid core C_h, put

\[
\mathcal T_h=
 \mathcal B_{q,G_h,\ db>N^{461/400}}(\psi_Y)
+\mathcal O_{p,G_2,\ b_p>N^{1/800}}(\psi_Y)
+Q_{C_h}(\psi_Y).
\]

Its exact completed identity is

\[
I_\kappa=\mathcal T_h-(1+\kappa)M_{C_h}u+o(u).
\tag{4}
\]

This is the same three-term expression and the same coefficient-one
coupling as checkpoint 26, (24).

## 2. A valid root upper envelope on all smoothed endpoints

Let

\[
S_N(w;z)=\sum_n w(n)\mathbf1_{P^-(n)\ge z},
\qquad A_0=8\omega(8),
\tag{5}
\]

where ω is Buchstab's function. Checkpoint 25 proves
0≤q_N(n)≤1_(P^-(n)≥z) throughout |n−x|≤Y for even N≥2^16.
The support of ψ_Y is inside this padding. Therefore

\[
Q_N(\psi_Y)\le S_N(\psi_Y;z).
\tag{6}
\]

Use the already admitted well-factorable remainder at outer exponent
γ=0 and level D=N^(5/4−δ), with each fixed δ>0. Its validity,
including squarefree sifting support and the full-level factor choice,
is established in NEGATIVE_FRONTIER_NOTE.md, Sections 2–4.
It is uniform over endpoints within O(Y) of x.

The primary sieve statement is
[Lichtman, arXiv:2109.02851v2, Theorem 2.10 and (2.5)](https://arxiv.org/html/2109.02851v2):
its upper remainder is a finite sum of well-factorable sequences at
the full level D. The theorem supplies the sieve formulation; the
campaign's short-interval remainder is the separately proved
Robert–Sargos transfer. No theorem about primes in arithmetic
progressions is substituted for that remainder.

For each sharp endpoint pair underlying ψ_Y this gives

\[
S_N(1_W;z)
\le |W|_{\mathbb R}V(z)
 \{F(5-4\delta)+O(\varepsilon)\}+o(u),
\quad
V(z)\sim\frac{4e^{-\gamma_0}}{\log N}.
\tag{7}
\]

The finite number of sieve components depends on fixed ε, not on N.
Average the sharp windows, then take the limsup as even N→∞,
followed by ε→0 and δ→0. This is a limiting argument over fixed
positive-margin remainders, not an application at a zero-margin
source endpoint. It proves

\[
S_N(\psi_Y;z)\le((1+\kappa)U_0+o(1))u,
\quad
U_0=8e^{-\gamma_0}F(5)=\frac{16}{5}\mathcal U(5).
\tag{8}
\]

Here \(\mathcal U(s)=sF(s)/(2e^{\gamma_0})\).
On [3,5] its derivative is log(s−2)/(s−1), so

\[
U_0=\frac{16}{5}
 \left(1+\int_1^3\frac{\log v}{v+1}\,dv\right).
\tag{9}
\]

The outward certificate in Section 7 refines, without changing,
the older enclosure of this same constant:

\[
U_0\in
[4.4994931524285722924719982904428152905587,\
 4.4994932857619056258053316237761486238921].
\tag{10}
\]

## 3. Bound the whole coupled sum

Let M be the original full marked reference, unchanged, and M_C the
checkpoint-26 hybrid-core reference. The inherited long PNT gives

\[
aQ_N(\psi_{H_1})=((1+\kappa)M+o(1))u.
\tag{11}
\]

Combine (3), (6), (8) and (11). This proves the uniform bound

\[
I_\kappa\le
 \{(1+\kappa)(U_0-M)+o(1)\}u
\le(1.435994+o(1))u.
\tag{12}
\]

Then (4) gives

\[
\boxed{\mathcal T_h\le
 \{(1+\kappa)(U_0-M+M_C)+o(1)\}u
\le(1.441618+o(1))u.}
\tag{13}
\]

Both decimals are rounded upward using U_0's upper endpoint,
the original M lower endpoint and, in (13), M_C's upper endpoint.
This is a bound on the completed signed sum. No individual
Type II term is assigned this coefficient, and no reference mass
is earned as a short prime lower bound.

This coefficient does not prove checkpoint 26's .0135582 sufficient
bound or the original .007935u integral estimate.

## 4. A positive complement, including the long-window clipping error

Define the nonnegative coefficient

\[
d_N(n)=\mathbf1_{P^-(n)\ge z}
 \left(1-\min\{1,q_N(n)\}\right),\qquad
\mathcal D_N(w)=\sum_n d_N(n)w(n).
\tag{14}
\]

This is a new positive complementary count. It is not the optional
marked estimate from the earlier campaign.

On the short padding the unique-mark lemma gives the exact identity

\[
S_N(\psi_Y;z)=Q_N(\psi_Y)+\mathcal D_N(\psi_Y).
\tag{15}
\]

The broader original long reference can contain several prime-product
marks at one integer. Positivity there requires the clipping in (14).
On either smoothed window, for all sufficiently large N, a nonzero
prime mark implies roughness: d≤N^(4/3), hence its cofactor prime is
at least (x/2)/N^(4/3)≫z. Consequently

\[
\mathcal D_N(\psi_{H_1})
=S_N(\psi_{H_1};z)-Q_N(\psi_{H_1})
+\sum_n(q_N(n)-1)_+\psi_{H_1}(n).
\tag{16}
\]

**Lemma 1.** The last term in (16), multiplied by a, is o(u).

Proof. There cannot be two single-prime marks near x, since their
product would be <N^(19/10). Single and pair marks have different
prime-factor degrees. First remove repeated prime factors in the
long window: summing multiples of b² for b≥z, b≤2N, and normalizing
gives

\[
O(N/z+\rho^{-1})=o(u).
\tag{17}
\]

The global mark cap three keeps this envelope applicable to excess
marks as well.

For distinct primes sort a_1<a_2<a_3. More than one pair mark requires
the alternative pair a_1,a_3 to pass the original frozen gate:

\[
a_1a_3^2\le x,\qquad
n=a_1a_2a_3=x(1+O(\rho)).
\]

Thus a_3/a_2=1+O(ρ) and a_1a_3²=x(1+O(ρ)).
For fixed a_3=r, this restricts a_1 to an interval of relative width
O(ρ) about x/r² and a_2 to one about r. All factors are ≥z.
The inherited PNT, uniform in intervals of relative width ρ on
these prime scales, bounds their numbers by
O(ρx/(r² log N)) and O(ρr/log N), respectively.
Summing over prime r gives

\[
O\left(\frac{\rho^2x}{(\log N)^2}
 \sum_{z\le r\le2N^{7/8}\atop r\ {\rm prime}}\frac1r\right)
=O(\rho^2x/(\log N)^2).
\]

After multiplying by a this is O(Nρ/(log N)²)=o(u).
This proves the lemma. The ordinary long PNT is used at its existing
relative scale; no short prime asymptotic is asserted. □

The same ordinary PNT and finite Buchstab decomposition give

\[
aS_N(\psi_{H_1};z)=((1+\kappa)A_0+o(1))u.
\tag{18}
\]

For completeness, all prime factors in the rough decomposition are
≥z and their number is at most eight near x. After fixing all but
the last prime, its long interval has relative width ρ; the inherited
PNT error is smaller than ρ by an exponential margin.
Repeated factors satisfy (17). Iterated partial summation yields
the ordinary density ω(log x/log z)/log z, giving A_0=8ω(8).
This proves (18) at the original H_1.

Equations (11), (16), (18) and Lemma 1 give

\[
a\mathcal D_N(\psi_{H_1})
=((1+\kappa)(A_0-M)+o(1))u.
\tag{19}
\]

The positive count's ordinary coefficient is enclosed in
[1.42812738782223954808,1.42816857732647018189].
It is not a proved lower bound for its short count.

## 5. An explicit sufficient positive lower comparison

Put

\[
\Delta_{\mathcal D}
=\mathcal D_N(\psi_Y)-a\mathcal D_N(\psi_{H_1}),
\quad
\Delta_S=S_N(\psi_Y;z)-aS_N(\psi_{H_1};z).
\]

By (15)–(18),

\[
I_\kappa=\Delta_S-\Delta_{\mathcal D}+o(u).
\tag{20}
\]

Using (8) and (18) proves

\[
\boxed{\Delta_S\le(C_{\rm rough}+o(1))u,\qquad
 C_{\rm rough}=.007825257.}
\tag{21}
\]

The unrounded enclosure for (1+κ)(U_0−A_0) is
[.00782507608875970477,.00782525659013819276];
the coefficient in (21) is rounded upward.

It follows that the following new input would suffice:

\[
\boxed{\Delta_{\mathcal D}\ge-(.0001+o(1))u.}
\tag{22}
\]

Indeed (20)–(22) would give

\[
I_\kappa\le(.007925257+o(1))u,
\qquad
Q_N(J)-aQ_N(B_1)\le(.010990257+o(1))u.
\tag{23}
\]

This leaves the explicit coefficient reserve .000009743 below
the original .007935 and .011 targets. **Inequality (22) is unproved.**
Equation (23) is a conditional consequence of that missing input.

Positivity alone and (19) currently give only
Δ_D≥−(1.428169+o(1))u. The .0001 deficit in (22) therefore requires
substantial new comparison information about the actual positive count.

The comparison in (22) uses the actual normalized long count.
Substituting only the lower endpoint of the displayed reference
enclosure would spend an additional enclosure error; it is not
the same sufficient condition.

If a subsequent estimate introduces a fixed least-prime power
sector with budget ξ from checkpoint 22, (23), or a fixed multiplier
L with complete-transform tail budget 21147/L, its sufficient
coefficient condition is

\[
C_{\rm rough}+\eta+\xi+21147/L\le .007935.
\tag{24}
\]

The final original coefficient is then at most
.003065+C_rough+η+ξ+21147/L. Here η is the proved deficit allowed for
the full positive complement after completing any discarded sector.
For η=.0001 the remaining combined budget is .000009743.
This continuation introduces neither of those discarded sectors;
its new nonvanishing charge is zero.

## 6. Identify the positive count and the scoped source limitation

On the short padding, every squarefree rough three-prime integer
p<r<q carries its canonical mark. To check the gate directly,
suppose pr²>x. Then

\[
pr(q-r)=n-pr^2\le n-x\le Y,
\qquad (pr)^2=p(pr^2)>zx>Y^2,
\]

a contradiction. A rough two-prime integer p≤q is marked precisely
when its smaller factor is <N^(19/20). A prime and every integer
with at least four prime factors have no original mark.

Thus, up to a nonnegative repeated-three-prime contribution of o(u),
the positive short count consists of these disjoint sets:

| Positive unmarked rough family | Actual condition |
|---|---|
| Primes | n is prime |
| Balanced semiprimes | n=pq, p≤q, p≥N^(19/20) |
| Higher degree | P^-(n)≥z and Ω(n)≥4 |

The repeated-three-prime envelope is
O(N/z+N^(7/8))=o(u): a repeated prime b≥z satisfies
b²≤(x+Y)/z, so count its multiples and sum over b.
For even N≥4 no prime square lies in |n−x|≤Y, since the nearest
possible prime bases N±1 have square distance greater than Y.

The existing direct final-cofactor linear lower sieve does not
supply (22). For primes its limiting s is 5/4<2. For the unmarked
balanced semiprimes, with smaller-prime exponent γ∈[.95,1),
its largest possible ratio is

\[
\frac{5/4-\gamma}{1-\gamma/2}\le\frac47<2.
\]

For four-prime rows, extracting the first three primes gives
γ≥3/4 and a last extracted exponent a_3≥1/4. On the portion
γ<1 where the arbitrary-outer input applies,

\[
(5/4-\gamma)-2a_3\le0.
\tag{25}
\]

Every admitted fixed slack makes this inequality strict in the
wrong direction. Even the necessary rough-cofactor lower sieve
has f(s)=0; adding a prime-certifying restriction cannot improve it.
For five or more primes that extraction has γ≥1 and lies outside
the admitted arbitrary-outer γ<1 interface.

This is a scoped limitation of the direct final-cofactor lower-sieve
route. Switching, joint estimation of the degree pool and other
positive or signed transfers are not excluded.

The signed outer terms cannot instead be dropped by a pointwise
argument. The actual kernel β_U has β_5(30)=2 but β_5(7)=−1.
For the algebraic stress cutoff U=5, p=210 has a positive outer
Type II coefficient from b_p=7,m=30. These are exact kernel
identities, not numerical evidence for uniform short-shell behavior.

## 7. Outward constants, exact checks and preservation

Run python3 src/coupled_one_sided.py.

For (9), the integrand g(v)=log(v)/(v+1) has |g''(v)|≤2 on [1,3].
Indeed g''=−1/[v²(v+1)]−2/[v(v+1)²]+2log(v)/(v+1)³;
using log v≤v−1≤2 bounds the sum of the three absolute terms by 3/2.
The composite trapezoid rule with 8,000 cells has absolute integral
error at most 4/(3·8000²). Every arithmetic and logarithm operation
rounds outward; this produces (10).

For A_0 use B(t)=tω(t), B=1 on [1,2] and
B'(t)=B(t−1)/(t−1) afterward. On the interiors of unit intervals,
|ω''|≤2: 0≤ω≤1, |ω'|≤1, and for t>2
ω''(t)=(ω'(t−1)−2ω'(t))/t. A mesh of width 1/8000 has every
integer knot as a boundary. Each trapezoid cell is enclosed with
error h³/6 and uses already enclosed delayed endpoints.
B(3)=1+log 2 is independently checked. The result is

\[
A_0\in
[4.4916758466109184202577279942469144285867,\
 4.4916758935986425174671832244038744044051].
\tag{26}
\]

The new enclosures lie inside the older frozen enclosures.
No historical mass ledger is overwritten.

Exact arithmetic checks cover 402,157 short-padding sites at
N=65536,65538,70000 using the original cutoffs and gates.
They check the mark cap, positive partition, complete squarefree
three-prime marking and repeated-factor residual.
A separate deliberately broad stress window retains the known
multiple-mark witness N=62,n=2431,q_N(n)=3. It tests clipping;
it is not the actual asymptotic H_1 window.

All 268 nonmutable checkpoint-26 records are preserved byte for byte.
Finite checks certify the stated identities and arithmetic; they do
not prove (22). The regional lemmas of checkpoint 26 are retained.
The original sharp comparison, H(ϑ), the optional marked estimate
and higher-degree allocation remain open; K=0 and milestone7 is deferred.


## 8. Next analytic step: construct and audit a switched lower weight

The next investigation is a **switching audit for a lower weight of the
combined positive complement**. Switching here means changing which
prime factors form the extracted outer product before applying a sieve
or reciprocal-sum estimate. Section 6 rules out the direct
final-cofactor lower-sieve extraction. It does not settle the switched
or jointly weighted alternatives.

The immediate task is to find an actual lower weight with the properties
below. No such weight meeting the quantitative requirements has been
constructed in this campaign.

### 8.1 A precise acceptance criterion

Let w_N(n) be a real lower weight and write
\(\mathcal W_N(\psi)=\sum_n w_N(n)\psi(n)\).
It may be signed, but it must satisfy the actual pointwise inequality

\[
w_N(n)\le d_N(n)\qquad (|n-x|\le Y).
\tag{27}
\]

For two nonnegative fixed coefficients η_loss and η_err, the two analytic
obligations are

\[
a\{\mathcal D_N(\psi_{H_1})-\mathcal W_N(\psi_{H_1})\}
 \le(\eta_{\rm loss}+o(1))u,
\tag{28}
\]

and

\[
\mathcal W_N(\psi_Y)-a\mathcal W_N(\psi_{H_1})
 \ge-(\eta_{\rm err}+o(1))u.
\tag{29}
\]

The first limits the long-reference mass lost by the lower weight.
The second is its required one-sided short-versus-long comparison.
All cutoffs, canonical weights and ordering gates must be retained.
The acceptance budget is

\[
\eta_{\rm loss}+\eta_{\rm err}\le .0001.
\tag{30}
\]

These conditions imply (22), because ψ_Y is nonnegative and (27) gives

\[
\begin{aligned}
\Delta_{\mathcal D}
&\ge \mathcal W_N(\psi_Y)-a\mathcal D_N(\psi_{H_1})\\
&=\{\mathcal W_N(\psi_Y)-a\mathcal W_N(\psi_{H_1})\}
 -a\{\mathcal D_N(\psi_{H_1})-\mathcal W_N(\psi_{H_1})\}\\
&\ge-(\eta_{\rm err}+\eta_{\rm loss}+o(1))u.
\end{aligned}
\tag{31}
\]

This elementary transfer is proved. Constructing a weight satisfying
(27)–(30) is the missing analytic work. Passing source exponent
conditions alone does not establish the reference-loss condition (28).

### 8.2 What to do first

1. Form an exact Buchstab or weighted-sieve decomposition of the
   **combined** raw difference S_N−Q_N. It agrees with the positive
   complement on the short padding; Lemma 1 supplies the o(u) correction
   in its normalized long reference. Keep the prime, unmarked balanced
   semiprime and higher-degree families together, with every signed
   correction required by the identity.
2. For each proposed switching choice, record the actual outer product,
   its exponent γ, the residual sieve level, the remaining arithmetic
   gates, and the source coefficient slots. Audit these before collapsing
   factors. The existing γ<1 well-factorable interface and the
   Robert–Sargos/Fouvry–Iwaniec coefficient restrictions remain binding;
   a prime coefficient cannot be described as a free unit-weight slot.
3. For every candidate lower weight, prove (27), enclose the complete
   long-reference loss in (28), and establish the one-sided comparison
   in (29) with its coefficient. The next deliverable is a table of these
   obligations for the actual switched terms, with an explicit total
   loss/error budget.

If a candidate satisfies (30), the transfer proves (22) and closes the
original signed comparison through (23). If the admitted engines leave
an unsupported component or the reference loss exceeds the budget,
record that component and the additional estimate it requires.
The viability of this switching route remains unproved.

This is the recommended next investigation. Refining the existing
coarse upper coefficient does not by itself establish (28) or (29).
There is no established closing argument at checkpoint 27.

If a candidate also introduces a fixed least-prime power budget ξ
from checkpoint 22, (23), or a fixed complete-transform tail charge
21147/L, the full criterion is

\[
.007825257+\eta_{\rm loss}+\eta_{\rm err}
 +\xi+21147/L\le .007935.
\tag{32}
\]

The corresponding original comparison coefficient retains every charge:
.003065+.007825257+η_loss+η_err+ξ+21147/L.
