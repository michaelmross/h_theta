# Continuing the signed delta estimate by regrouping small factors

Michael M. Ross's H(ϑ) campaign. Checkpoint 14, 7 October 2026.

**Result.** The complete Type I error is uniformly negligible through
**d≤N^(457/400)=N^1.1425**, improving checkpoint 13's N^1.13. The
actual Type II term is uniformly negligible on **db≤N^(459/400)=N^1.1475**
for every supported outer coefficient, including the single-prime outer
family. Additional explicitly defined Type I regions extend into the
large-d range. They reduce the remaining triprime reference coefficient
from about **0.22758 to 0.088514**.

These are new deductions from the previously admitted Robert–Sargos and
Fouvry–Iwaniec bounds, with a different coefficient grouping. They are not
new statements quoted from those papers. The actual remaining covariance
and centered prime count are still unestimated at the required scale.
The uniform .011u bound, higher-degree cap, positive K and H(ϑ) remain
unproved. The numerical reference mass is not a cap on the short count.

## 1. Keep the original arithmetic and target

All notation and coefficients of COFACTOR_ESTIMATE_NOTE.md are unchanged:
\[
x=N^2,\quad J=[x-N/2,x+N/2]\cap\mathbb Z,\quad Y=N+1,
\quad u=N/(2\log N),\quad z=N^{1/4},
\quad U=V=\lfloor N^{1/100}\rfloor.
\]
The supported coefficient is
\[
c_N(d)=\mathbf1_{d\ {
\rm prime},\ z\le d<N^{19/20}}
+\frac12\sum_{\substack{p,r\ge z\ {
\rm prime}\\pr=d}}\mathbf1_{pr\max(p,r)\le x},
\quad \gamma_N(d)=c_N(d)\frac{\log N}{\log(x/d)}.
\]
The actual Type II sum is
\[
B_N(J)=\sum_d c_N(d)\sum_{m>U,b>U}
\frac{\beta_U(m)\Lambda(b)}{\log(mb)}\mathbf1_J(dmb),
\quad \beta_U(m)=-\sum_{\substack{t\mid m\\t\le U}}\mu(t)
\quad(m>1).
\]
The normalized long-reference terms and density centering were already
controlled in JOINT_REMAINDER_NOTE.md. A Type I assertion here always
means the signed lattice-minus-integral error R_I, rather than the
uncentered Type I count. We seek the joint one-sided estimate
\[
\Delta_2+\Delta_3\le(.011+o(1))u
\]
uniformly for all sufficiently large even N.

## 2. The grouping improvement

On a factorized reciprocal-sum block let S be the exponent of the
denominator product *before* the small Vaughan variables. Let a be the
exponent of a selected prime, and let δ be the exponent of the small
product. Thus the total denominator exponent is Σ=S+δ. Retain
\[
\nu=1/10000,\qquad \eta\le\max(0,\Sigma-1)+\nu.
\]
The source facets for a standalone exponent A are
\[
\begin{split}
\text{RS}:&\quad A>4\eta+2-2\Sigma,\quad
A<\Sigma-3\eta,\quad A>2\eta,\quad \eta<2-\Sigma;\\
\text{FI6}:&\quad A<\frac{8\Sigma-7\eta-6}{7},\quad
A<\frac{6\Sigma-5\eta-4}{7},\quad
A<\frac{5\Sigma-5\eta-2}{8},\\
&\quad A<\frac{4\Sigma-5\eta-2}{5},\quad
A>\eta,\quad A<\frac{2-\Sigma-\eta}{2}.
\end{split} \tag{1}
\]
These are the audited inequalities in FI_1989_AUDIT.md and
JOINT_REMAINDER_NOTE.md. Their primary sources are
[Robert–Sargos (2006), Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)
and Fouvry–Iwaniec, *Exponential sums with monomials* (1989), Theorem 6;
the latter's original PDF is sources/fi1989_monomials.pdf. The source
bytes and earlier audits are retained unchanged.

Checkpoint 13 kept A=a while putting the small product in the other
coefficient slot. In the new RS branches put the selected prime **and
the entire small product** in the standalone slot instead:
\[
A=a+\delta. \tag{2}
\]
For example a Type I denominator prtb becomes (ptb)r, rather than
p(rtb). The standalone coefficient is a convolution of a prime
coefficient, μ(t), and Λ(b). It has fixed divisor growth, which costs
an arbitrarily small fixed power after normalization. The other
coefficient remains independent after separating the cutoffs and smooth
weights. Robert–Sargos allows arbitrary bounded complex coefficients,
so primality of the *collapsed* variable ptb is not required.

For S≥1 and 0≤δ≤ρ, the worst RS lower edge under (2) is
\[
a>2S-2+\rho+4\nu. \tag{3}
\]
Keeping A=a would instead require a>2S−2+2ρ+4ν. FI is most useful
with the small product in the other slot; its first upper facet,
uniform in δ, is
\[
a<(S+1)/7-\nu. \tag{4}
\]
Consequently these two edges overlap whenever
\[
\boxed{13S<15-7\rho-35\nu.} \tag{5}
\]
The other facets must also be checked; (5) alone is not a general
admission criterion. The continuous certificates below check them all.
The source choice uses the fixed split
\[
s_\rho(S)=\frac{15S-13}{14}+\frac\rho2+\frac{3\nu}2:
\quad a\le s_\rho(S)\text{ uses FI6 with }A=a,
\quad a\ge s_\rho(S)\text{ uses RS with }A=a+\delta.
\tag{6}
\]
This is the midpoint of (3) and (4); both sides have positive reserve.

## 3. Coefficient separation and sharp transfer are retained

The improvement changes a grouping, not the interval transfer. The
sharp signed transfer and its positive absolute-coefficient boundary
envelopes are those proved in NEGATIVE_FRONTIER_NOTE.md, Section 3.
Raw reciprocal sums have a saving relative to the total denominator
scale. Poisson's factor Y/Q converts it to O(N^(1−c)); fixed logarithms
and divisor losses are absorbed by the positive source margins.
The FI frequency coefficient remains an additive character, with the
already audited interval completion. No arbitrary frequency/denominator
joint coefficient is introduced into FI.

Retain the frozen ordering gate
\[
pr\max(p,r)\le x
\iff p^2r<x+1/2\text{ and }pr^2<x+1/2.
\]
Separate it by the same truncated Mellin inversion as checkpoint 13,
**before** collapsing a coefficient. The two resulting prime twists
remain separate from the small-variable weights and are then included
in the convolution coefficient. The source phase itself remains
hz′/(prtb). Thus the gate is not dropped when ptb is collapsed.

Order the outer pair p≤r when selecting its smaller prime. Exact order
indicators can likewise be separated using a ratio with a half-integer
shift, such as p<r+1/2. Arbitrary source coefficient sequences absorb
the shifted-r twist. The diagonal p=r has its original half weight.
It can be removed in these estimates at o(u): the number of multiples
of p² in J, for N^(1/4)≤p≤N^(2/3), is
\[
O(N/z+N^{2/3})=O(N^{3/4}).
\]
Fixed divisor losses absorb Type II multiplicities; for Type I, the
additional small factors cost at most U² in the endpoint error, giving
O(N^(2/3+1/50)(log N)^C)=o(u). The corresponding integral errors have
the same bounds. The exact remaining joint identity still retains all
diagonal weights.

All new cuts are finite rational linear inequalities in logarithmic
exponents. Clear their rational denominators to obtain inequalities on
integer monomials. Replace a real threshold T by floor(T)+1/2 when
separating an integer monomial. This preserves the exact cut and gives
a positive distance from its boundary. A polynomially large Mellin
truncation gives an arbitrarily small pointwise power error and fixed
logarithmic coefficient mass, as in checkpoint 13. There is no
assumption of a uniformly separated irrational threshold.

Uniformity for partial boxes, conjugate frequencies, logarithmic
weights and the absolute boundary envelopes is unchanged. Lower
frequencies improve every source facet. The same grouping chosen at
the top retained frequency therefore handles the whole frequency sum.

## 4. Complete Type I through N^1.1425

For I₁ the small product is t≤U; for I₂ it is tb with t,b≤U.
Use the common range 0≤δ≤ρ_I=1/50. Write
\[
S=\sigma=\log_N(pr),\qquad
a=\log_N\min(p,r),\qquad1/4\le a\le S/2.
\]
The elementary proof still handles low outer products. On
19/20≤S≤11/10 use RS without augmentation, as before. On
11/10≤S≤457/400 use (6), with ρ=1/50, and augment the RS slot by
the actual small-product exponent δ.

Every original source facet is affine after splitting at Σ=1. Exact
rational vertex evaluation gives the following continuous certificates.
Shared boundaries are included and have strict positive margins.

| Covered family | Source/grouping | Minimum facet margin |
|---|---|---:|
| Type I, .95≤S≤1.10 | RS, A=a | 6/625 |
| Type I, 1.10≤S≤1.1425, a≤s_(.02)(S) | FI6, A=a | 1/3500 |
| Type I, 1.10≤S≤1.1425, a≥s_(.02)(S) | RS, A=a+δ | 1/3500 |

The full gate and logarithmic freezing remain as in Section 3. Hence
\[
\boxed{R_{I,\,d\le N^{457/400}}(J)=O(N^{1-c})=o(u)}
\tag{7}
\]
for some fixed c>0. The cutoffs U,V are unchanged.

## 5. A complete Type II product region

Define B_small by the actual restriction
\[
db\le N^{459/400}. \tag{8}
\]
This applies to *both* the prime outer and two-prime outer families;
it does not require d>N^.95 or d≤N^1.13.

Throughout (8), m∼N²/(db)≫N^.8525>U. Thus the full small-divisor
expansion is valid, with m=tℓ a free-integer variable, and the frozen
sum is
\[
-\frac1{\log N}\sum_{db\le N^{459/400}}\gamma_N(d)\Lambda(b)
\sum_{t\le U}\mu(t)\sum_{dtb\ell\in J}1+o(u). \tag{9}
\]
Its integral part is
\[
-\frac{Y\alpha_U}{\log N}
\sum_{db\le N^{459/400}}\frac{\gamma_N(d)\Lambda(b)}{db}=o(u),
\quad \alpha_U=\sum_{t\le U}\mu(t)/t.
\]
The harmonic sum has only fixed logarithmic growth, and the admitted
quantitative long Möbius estimate makes α_U smaller than every fixed
inverse logarithm. This is not an individual short prime theorem.

For db≤N^(49/50), the elementary floor error is
O(N^(.98+.01)(log N)^C)=o(u). For larger db, remove proper prime powers
in b using checkpoint 13's absolute subset estimate, and let b be
prime. Put S=log_N(db), δ=log_N t, with 0≤δ≤ρ_B=1/100.

If d is a single prime below N^.95, choose the smaller of d and b as
the selected prime. Its exponent a satisfies
\[
S-.95\le a\le S/2.
\]
If d=pr, choose the smaller outer prime. Then a≥1/4 and a≤S/2;
since S≤1.1475, this also implies a≥S−.95. The other prime(s), and
the remaining small factor t, are collapsed in the other coefficient
slot for FI, or t joins the selected prime for RS. Λ(b)/log N is
bounded and the collapsed coefficients have fixed divisor order.
The comparison choosing the smaller prime in the first case is
separated as in Section 3.

Thus every relevant block lies in the common polytope
\[
.98\le S\le459/400,\quad S-.95\le a\le S/2,
\quad0\le\delta\le1/100. \tag{10}
\]
Use (6) on this whole polytope. Below Σ=1, the original six/four
facets, rather than their high-frequency simplifications (3)–(4),
are checked directly. The certificate gives

| Covered Type II branch | Source/grouping | Minimum facet margin |
|---|---|---:|
| a≤s_(.01)(S) | FI6, A=a | 9/14000 |
| a≥s_(.01)(S) | RS, A=a+δ | 9/14000 |

Consequently the signed floor errors in (9) have a uniform power
saving. Proper-b powers and the freezing error are already o(u).
We conclude
\[
\boxed{B_{\,db\le N^{459/400}}(J)=o(u)}. \tag{11}
\]
No positive norm estimate is used to claim cancellation here; the
small-divisor expansion and reciprocal-sum transfer carry its sign.

## 6. Additional Type I regions inside the large-d core

Keep σ=log_N(pr), a=log_N p with p≤r, and set
\[
\rho=1/50,\qquad\tau=1/10000.
\]
Above σ=457/400, either of the following two regions also controls
the *complete* Type I error, uniformly for all actual δ≤ρ:
\[
\begin{split}
\mathcal D_A:\quad&2\sigma-2+2\rho+4\nu+\tau\le a
\le3-2\sigma-2\rho-3\nu-\tau;\\
\mathcal D_B:\quad&2\sigma-2+\rho+4\nu+\tau\le a
\le3-2\sigma-3\rho-3\nu-\tau.
\end{split} \tag{12}
\]
Intersect these with the actual pair domain
\[
\max(1/4,2\sigma-2)\le a\le\sigma/2,\quad\sigma\le4/3.
\]
Region A uses RS with all small variables in the other slot. Region B
uses RS with all small variables in the standalone slot. Substitution
in every RS facet shows a margin at least τ; the script also certifies
every vertex of both continuous regions. Each region automatically
becomes empty above σ=49191/40000=1.229775. They do not control the
balanced end near σ=4/3.

In exact prime variables, the two tests in (12) are respectively
\[
\begin{array}{ll}
\mathcal D_A:& pr^2\le N^{3919/2000},\quad p^3r^2\le N^{7399/2500};\\
\mathcal D_B:& pr^2\le N^{3959/2000},\quad p^3r^2\le N^{7349/2500}.
\end{array} \tag{13}
\]
Let D_good include all supported d≤N^(457/400) and the two-prime
products satisfying either test (13). All original outer gates are
retained. Let C be its complement in the actual outer support. Then
\[
\boxed{R_{I,D_{\rm good}}(J)=o(u).} \tag{14}
\]
The set C is the new Type I core; it is smaller than a simple interval
of outer products.

## 7. Reference mass of the new core

The normalized prime-density measure for an ordered pair of exponents
a≤σ−a, with a≥1/4 and the frozen ordering gate a≥2σ−2, is
\[
\frac{2\,da\,d\sigma}{a(\sigma-a)(2-\sigma)}.
\]
For affine inner endpoints L(σ)≤R(σ), its inner integral is
\[
\frac{2}{\sigma(2-\sigma)}
\log\frac{R(\sigma-L)}{L(\sigma-R)}. \tag{15}
\]
This is the same long-reference normalization as earlier checkpoints.
It gives the coefficient M_C in ∫G_C=(M_C+o(1))u, using the already
admitted long Möbius density centering and prime harmonic asymptotics.

For σ≥457/400 put
\[
L=2\sigma-2,\ H=\sigma/2,\quad
L_B=L+\rho+4\nu+\tau,\ L_A=L+2\rho+4\nu+\tau,
\]
\[
U_B=3-2\sigma-3\rho-3\nu-\tau,\quad
U_A=3-2\sigma-2\rho-3\nu-\tau.
\]
The complement of (12) has exactly these intervals:

| σ range | Remaining inner intervals |
|---|---|
| [457/400, 7399/6250] | [L,L_B] |
| [7399/6250, 48991/40000] | [L,L_B], [U_A,H] |
| [48991/40000, 49191/40000] | [L,L_B], [U_B,L_A], [U_A,H] |
| [49191/40000, 4/3] | [L,H] |

Exact endpoint comparisons certify that each interval is nonnegative
and belongs to the actual pair domain. Outward Decimal interval
integration, with 12,000 cells per inner-interval piece, encloses
\[
\boxed{0.0884954626805<M_C<0.0885320794086.} \tag{16}
\]
The center is approximately 0.08851377. The former cutoff-only core
at d>N^1.13 had coefficient approximately 0.22757995. Merely changing
the complete cutoff to N^1.1425 leaves approximately 0.19818494;
the additional regions in (12) account for most of the reduction.
The JSON gives outward enclosures for all three, not just the rounded
centers stated here.

Equation (16) is a **reference coefficient**, not an upper bound for
A_C(J) or for its centered discrepancy. It does not pay the .011u
budget. If the other signed term were proved o(u), the remaining
core would need an actual upper count at most (M_C+.011+o(1))u;
that conditional requirement is still unproved.

## 8. Exact remaining interface and the unresolved estimate

Let B_large retain db>N^(459/400). The proved subterms give
\[
\boxed{\Delta_2+\Delta_3=B_{\rm large}(J)+R_{I,C}(J)+o(u).}
\tag{17}
\]
Here C retains the two-prime outer gate and the complement of both
new Type I tests. The sufficient terminal inequality remains
\[
B_{\rm large}(J)+R_{I,C}(J)\le(.011+o(1))u. \tag{18}
\]

No Type II row with outer d∈C was removed: d>N^1.1425 and b>U imply
b≥U+1>N^.01, hence db>N^1.1525>N^1.1475. Thus the exact joint identity
is preserved on the whole core:
\[
B_C(J)+R_{I,C}(J)=A_C(J)-\int_{J_{\mathbb R}}G_C(v)\,dv.
\tag{19}
\]
Every non-prime-power cofactor still cancels between the discrete
Vaughan terms. The exact frozen counts, rather than separate positive
charges for their composite rows, must be used here.

Combining (17)–(19) gives a more informative interface:
\[
\boxed{\Delta_2+\Delta_3=
B_{D_{\rm good},\,db>N^{459/400}}(J)
+A_C(J)-(M_C+o(1))u.} \tag{20}
\]
Proper prime powers in A_C have the previously proved o(u) error.
The two still-open inputs in (20) are the signed Type II contribution
on the *controlled outer* family and the centered prime-cofactor
count on C.

The first term retains the actual weighted β covariance. After
the already proved proper-b-power removal, define
\[
\mathcal W_{D,\rm large}(n)=
\sum_{\substack{p\mid n\\p>U\ {\rm prime}}}\log p
\sum_{\substack{d\mid n/p\\d<n/p\\d\in D_{\rm good}}}
\gamma_N(d)\mathbf1_{dp>N^{459/400}}.
\]
Then
\[
B_{D_{\rm good},\,db>N^{459/400}}(J)=\frac1{\log N}
\sum_{n\in J}\beta_U(n)(\mathcal W_{D,\rm large}(n)-\overline{\mathcal W}_{D,\rm large})+o(u).
\tag{21}
\]
The bar may be the mean on J. The nonnegative weight is bounded by
(36+o(1))log N, and centering costs o(u), as in checkpoint 13.
Those facts still do not estimate its covariance. The old
b-independent α_N cannot be reused after the product restriction.

For example, the remaining numerator requirement is
\[
\sum_J\beta_U(n)(\mathcal W_{D,\rm large}(n)-\overline{\mathcal W}_{D,\rm large})
+(\log N)A_C(J)
\le\left(\frac{M_C+.011}{2}+o(1)\right)N. \tag{22}
\]
Neither (18) nor (22) is proved. The positive β second moment and
the diagonal overlap above b>N remain. Regrouping has enlarged
the cancellable part, but has not supplied the needed signed
dispersion estimate for the remaining covariance.

There is a precise limitation on continuing this particular regrouping
method. At the retained top frequency η=Σ−1+ν, necessary RS facets
require a standalone exponent between 2Σ−2+4ν and 3−2Σ−3ν. Their
window has width **5−4Σ−7ν**. Necessary FI facets require it between
Σ−1+ν and (3−2Σ−ν)/2, with width **(5−4Σ−3ν)/2**. Both are empty
for every Σ≥5/4, regardless of which variables are collapsed.
The actual interior core contains, for example, σ=13/10 and
a=13/20: two outer primes of exponent .65 with a cofactor of
exponent .70. Its ordering gate holds with room to spare, while the
two source windows already fail with δ=0. The script checks these
affine widths and the rational witness.

This explains why enlarging the same two-slot source regions cannot
finish the delta estimate. A further advance must estimate the
remaining signed covariance/joint core by another input, rather than
assign reference mass to the missing source blocks. It is a limitation
of these two raw reciprocal bounds and this transfer, not a global
impossibility claim about arithmetic methods or joint cancellation.

## 9. Verification and admission

Run from the campaign directory:

    python3 src/delta_grouping.py

The program certifies **80 rational vertex records** over seven
continuous source regions. Minimum source margins are 1/3500 for
the enlarged complete Type I range, 9/14000 for the complete Type II
product range, and 1/10000 for the additional Type I regions. These
are rational proofs of source applicability, not sampled exponent
tests or a proof of the final discrepancy estimate.

Three arithmetic fixtures use (N,U)=(100,1),(1000,3),(10000,8).
The first has the actual campaign truncation. The other two are
explicit stress tests; actual floor(N^.01) is one there. Independent
Vaughan coefficient vectors verify the new product partition,
small-divisor expansion, remaining prime-b covariance identity,
absence of removed core rows, and exact composite core cancellation.
No limiting estimate is inferred from the fixtures.

The run verifies 149 historical files unchanged against the frozen
checkpoint 13 manifest. The original analytic ledger, earlier
source bytes, old scripts and 007 audit are unchanged. New files are
results/delta_grouping_facets.json, delta_grouping_checks.json,
delta_grouping_reference.json and delta_grouping_reduction.json.
No new Lean/comparator replay or 007 kernel identification is claimed.

Admit (7), (11), (14), the exact interfaces (17)–(21), and the
reference enclosure (16), with their stated coefficient and transfer
hypotheses. The .011u estimate and the separate higher-degree task
remain open; no positive K or terminal prime comparison is credited.
