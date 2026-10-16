# Spectral coverage and an auxiliary prime identity

Checkpoint 24 — Michael M. Ross's H(ϑ) campaign — 11 October 2026

**The sharp .007935u spectral estimate and original .011u comparison
remain open.** This continuation proves two additional estimates and
records their scope in a coverage table.

* After an exact localization of the product, its absolute spectral tail
  above N^(4/3)(log N)^2 is o(u). This replaces the earlier upper limit
  N^(21/10) in an equivalent signed integral without spending a coefficient.
* An auxiliary exact Vaughan identity extends complete Type I control
  from outer exponent 1.1425 to 1.15225 and the negligible low-product
  Type II range from 1.1475 to 1.1525. Two additional Type I wedges leave
  an auxiliary pair-core reference coefficient in
  [0.06061819810, 0.06065204470], versus the original frozen core's
  [0.08849546268, 0.08853207941].

The new core coefficient is a long-reference density, not an upper bound
for its short prime count. Its associated Type II coefficient changes
with the auxiliary identity. Neither coefficient improvement proves
the joint sharp comparison. All original arithmetic gates, reference
windows, historical files and the certified K=0 are retained.

## 1. Frozen target and coefficient ledger

Use the notation and original c_N(d), Q_N, Y, H_1, a and ψ_h of
JOINT_SIGNED_COMPARISON_NOTE.md:

\[
x=N^2,\quad Y=N+1,\quad u=\frac{N}{2\log N},\quad
\kappa=\frac1{1000},\quad a=Y/H_1,\quad \rho=H_1/x=N^{-o(1)}.
\]

The original c_N(d) is the single-prime row z≤d<N^(.95), plus the
half-weighted ordered pair with p,r≥z=N^(1/4) and
pr max(p,r)≤x. Thus 0≤c_N≤1 and d≤N^(4/3). The count is
Q_N(W)=Σ_d c_N(d)Σ_(q prime)1_W(dq). Its smoothed contrast is
I_κ=Q_N(ψ_Y)−aQ_N(ψ_(H_1)). Checkpoint 23 proves

\[
Q_N(J)-aQ_N(B_1)\le I_\kappa+
   (.003065+o(1))u,
\qquad
I_\kappa=\mathfrak H_\kappa(N)+o(u).
\tag{1}
\]

Here 𝔥_κ is the specified original integral from T_0 to N^(21/10).
The coefficient .003065 is an outward smoothing allowance, using the
original full reference mass. It is unchanged in this continuation.

| Budget item | Coefficient of u |
|---|---:|
| Original comparison | .011 |
| Previously charged smoothing | .003065 |
| Remaining signed integral | .007935 |
| New localization and auxiliary exact identity | 0 |
| Fixed least-prime power cutoff, if subsequently used | ξ from checkpoint 22, (23) |

With a fixed least-prime cutoff budget ξ, the last signed allowance is
.007935−ξ. The auxiliary identity below discards no least-prime sector
and therefore does not incur ξ. The original subpower T_N in (2) of
checkpoint 23 and original U=N^(.01) are unchanged.

## 2. Exact product localization

Choose 0≤χ≤1, supported on [1/2,3/2], equal to one on [3/4,5/4],
with two continuous derivatives and piecewise integrable third derivative.
For example use H(s)=10s³−15s⁴+6s⁵ and

\[
\chi(v)=
\begin{cases}
H(4v-2),&1/2\le v\le3/4,\\
1,&3/4\le v\le5/4,\\
H(6-4v),&5/4\le v\le3/2,\\
0,&\text{otherwise}.
\end{cases}
\]

Since ρ→0, χ(n/x)=1 on both smoothed windows for all sufficiently
large N. Define the finite polynomial with the **actual prime marks**

\[
F_N(t)=\sum_n\frac{Q_N(\{n\})\chi(n/x)}{n^{1+it}}.
\tag{2}
\]

No prime coefficient is replaced by an arbitrary sequence. This is the
original product coefficient localized to n≈x. Mellin inversion gives
the exact identity

\[
I_\kappa=\frac1{2\pi}\int_{\mathbb R}F_N(t)
 \bigl(\widehat\psi_Y(1+it)-a\widehat\psi_{H_1}(1+it)\bigr)\,dt.
\tag{3}
\]

The integral is absolutely convergent. The center phase is retained:
writing F_N(t)=x^(-it)Σ_n Q_N({n})χ(n/x)n^(-1)(n/x)^(-it)
makes its cancellation with the x^(it) factor in ψ̂ explicit.

There is a global elementary cap

\[
0\le Q_N(\{n\})\le3. \tag{4}
\]

The single-prime row has factor degree two and at most two distinct
prime cofactors; the pair row has factor degree three and at most three.
Those degrees are disjoint, and each c_N≤1. The sharper cap one on J
is not used on this broader padding support. In fact at N=62,
n=11·13·17=2431 has three admissible pair marks and lies in [x/2,3x/2].

## 3. A uniform absolute tail at a shorter cutoff

Write a_n=Q_N({n})χ(n/x)/n. From (4) and the support,

\[
\sum_n|a_n|^2\le72/x \qquad(x\ge2). \tag{5}
\]

For T>0, expand the square of F_N on [T,2T]. Its diagonal contributes
TΣ|a_n|². For n≠m in the support,

\[
\left|\int_T^{2T}(n/m)^{-it}\,dt\right|
 \le\frac2{|\log(n/m)|}\le\frac{3x}{|n-m|}.
\]

Use 2|a_na_m|≤|a_n|²+|a_m|² and the harmonic row bound
Σ_(m≠n)1/|n−m|≤2(1+log(2x)). This proves, without an external
mean-value theorem,

\[
\int_T^{2T}|F_N(t)|^2\,dt
 \le\bigl(T+6x(1+\log(2x))\bigr)\sum_n|a_n|^2
 \le72T/x+2160\log N \qquad(N\ge2).
\tag{6}
\]

The trapezoid formula in checkpoint 23, (13), and its endpoints≤3x/2
give

\[
|\widehat\psi_Y(1+it)|\le\frac{9x^2}{\kappa Yt^2}
\quad(t\ne0). \tag{7}
\]

Cauchy on each dyadic frequency band and (6) imply

\[
\int_T^{2T}|F_N(t)|\,dt
 \le9T/N+47\sqrt{T\log N}.
\]

Apply (7) and sum these bounds on [2^jT,2^(j+1)T]. Since
Σ_j2^(-j)=2 and Σ_j2^(-3j/2)<2, and π>3, one obtains the explicit
positive-frequency tail estimate

\[
\boxed{\frac1\pi\int_T^\infty
 |F_N(t)\widehat\psi_Y(1+it)|\,dt
 \le\frac{282}{\kappa}\frac{N^3\sqrt{\log N}}{T^{3/2}}
     +\frac{54}{\kappa}\frac{N^2}{T}.}
\tag{8}
\]

Conjugation gives the corresponding normalized two-sided estimate.
Take

\[
T_*=N^{4/3}(\log N)^2.
\]

Then (8) is

\[
O_\kappa\left(\frac{N}{(\log N)^{5/2}}
       +\frac{N^{2/3}}{(\log N)^2}\right)=o(u).
\tag{9}
\]

This is a bound for the **localized polynomial (2)**. It does not assert
that individual bands of the old, unlocalized product above T_* are
negligible. The exact identity (3) is required for the transfer.

## 4. Low frequencies and the new coverage table

The required low-frequency argument also survives localization. Its
long-PNT model is

\[
F_N^0(t)=\int_0^\infty\chi(v/x)G_N(v)v^{-1-it}\,dv,
\qquad G_N(v)=\sum_d\frac{c_N(d)}{d\log(v/d)}.
\]

On χ's support, every relevant prime cofactor is between constant
multiples of N^(2/3) and N^(7/4), and the old prime padding g is one
there. Quantitative long PNT and partial summation, now with χ(dq/x),
give a common c_0>0 and fixed C such that

\[
F_N(t)-F_N^0(t)
 \ll(1+|t|)(\log N)^C e^{-c_0\sqrt{\log N}}.
\tag{10}
\]

Here Σ_dc_N(d)/d=O(1), as already established. Choose the common
T_0=exp((c_0/4)√log N) for this and the old PNT estimate. The cost of
replacing F_N in (3) on |t|≤T_0 is o(u).

In logarithmic coordinates v=xw, χ(w)G_N(xw) has three integrable
derivatives, each O(1/log N). Three integrations by parts show
F_N^0(t)≪(log N)^(-1)(1+|t|)^(-3). Thus its high-frequency integral
against the paired kernel is o(u). The full model contrast is the same
one as before, because χ=1 on both windows. Its constant density
cancels by equal paired areas, and the remaining error is
O(Yρ/(log N)²)=o(u). Hence the low part of (3) is o(u).

Also |F_N(t)|=O(1) by (4), so the old elementary estimate proves

\[
a\int_{|t|>T_0}|F_N(t)\widehat\psi_{H_1}(1+it)|\,dt
 \ll_\kappa Y\rho^{-2}/T_0=o(u).
\]

Combining this with (9) proves the new sufficient interface

\[
\boxed{\mathfrak H_\kappa(N)
 =\frac1\pi\Re\int_{T_0}^{T_*}
   F_N(t)\widehat\psi_Y(1+it)\,dt+o(u).}
\tag{11}
\]

All estimates are uniform in sufficiently large even N. No averaging
over centers, short prime theorem, or coefficient allowance is used.

| Frequency piece | Estimate | Status / reason |
|---|---|---|
| Localized paired integral, \(\lvert t\rvert\le T_0\) | o(u) | Long PNT, model decay, equal areas |
| Normalized smooth reference, \(\lvert t\rvert>T_0\) | o(u) absolutely | Kernel decay and ρ^(-2)/T_0→0 |
| Localized short polynomial, \(\lvert t\rvert>T_*\) | o(u) absolutely | Proved in (5)–(9) |
| Localized signed short integral, T_0<t≤T_* | Required upper coefficient .007935 | Open |

Near t≈x/Y≈N, (6) with the kernel bound |ψ̂_Y|≤(1+κ)Y still gives
only O(N^(3/2)√log N) for an absolute band integral. It therefore
does not supply the missing coefficient. The shortening in (11) removes
a proven tail; cancellation in the central range remains necessary.

## 5. A finer auxiliary Vaughan identity

Apply checkpoint 10's exact convolution identity to the original
Mangoldt cofactor with the new **auxiliary identity parameters**

\[
U_{\rm aux}=V_{\rm aux}=\lfloor N^\tau\rfloor,
\qquad\tau=1/1000.
\]

The original c_N, least-prime sectors and original continuation in (2)
are not redefined. Keeping all terms makes this an exact identity for
the same original prime count. Proper full-cofactor powers cost
O(N^(7/8))=o(u), as in checkpoint 10; the proof works on every window
of length comparable to N and therefore on ψ_Y by layer averaging.

Denote the resulting Type I and II terms by I_(1,τ), I_(2,τ), B_τ,
and the associated Type I density by G_τ. Their small-product exponents
are δ≤ρ_I=2τ for Type I and δ≤ρ_B=τ in the small-db Type II expansion.
The long Möbius/PNT centering and normalized long-reference removal
remain valid for this fixed positive τ.

In particular, the actual remaining coefficient is defined by

\[
B_{\tau,\mathcal D,db>Z}(\psi)=
 \sum_{d\in\mathcal D}c_N(d)
 \sum_{\substack{m>U_{\rm aux},\ b>V_{\rm aux}\\db>Z}}
 \frac{\beta_{U_{\rm aux}}(m)\Lambda(b)}{\log(mb)}\psi(dmb),
\qquad
\beta_{U_{\rm aux}}(m)=-\sum_{t\mid m,\ t\le U_{\rm aux}}\mu(t).
\]

This auxiliary β is used only inside the complete exact decomposition;
the original β_U in the joint high-block/rough comparison is retained.

On a reciprocal block let S be the denominator exponent before the
small variables and A the standalone exponent. Keep ν=1/10000 and
η≤max(0,S+δ−1)+ν. The audited RS and FI6 facets are those in
DELTA_GROUPING_NOTE.md, (1). Use the same split

\[
s_\rho(S)=\frac{15S-13}{14}+\frac\rho2+\frac{3\nu}2.
\]

FI uses A=a; RS on the upper branch uses A=a+δ. The rational
continuous certificates, checking every facet and the S+δ=1 split,
are in results/spectral_coverage_facets.json.

| Auxiliary piece | Covered region | Minimum facet reserve |
|---|---|---:|
| Type I, RS | .95≤S≤1.10, a≥1/4 | 57/1250 |
| Type I, FI/augmented RS | 1.10≤S≤4609/4000, a≥1/4 | 13/56000 |
| Small-db Type II, FI/augmented RS | .98≤S≤461/400, a≥S−.95 | 1/2000 |
| Each additional pair Type I wedge below | Actual pair gate and wedge inequalities | 1/10000 |

The elementary low range is unchanged. The original separation of
ordering gates, half-integer product thresholds, bounded-convolution
coefficients, logarithmic weights and signed boundary envelopes applies
with smaller small products. Source reserves absorb the fixed logarithmic
and arbitrarily small divisor losses. FI retains its audited additive
frequency restriction; no arbitrary joint frequency coefficient is added.

Consequently, for some fixed c>0,

\[
R_{I,\tau,d\le N^{4609/4000}}(\psi_Y)=O(N^{1-c})=o(u),
\qquad B_{\tau,db\le N^{461/400}}(\psi_Y)=o(u).
\tag{12}
\]

For the second assertion expand β_aux(m)=−Σ_(t|m,t≤U_aux)μ(t),
with free m=tℓ, exactly as in checkpoint 14. The product condition
ensures m≫N^(.8475)>U_aux. A single-prime outer selects the smaller
prime of d,b; a pair outer selects its smaller prime. Both satisfy
a≥S−.95. The integral main term vanishes by the quantitative long
Möbius estimate. Proper b powers, on every selected subset, have the
absolute bound from checkpoint 13:

\[
O_\epsilon\bigl(N^\epsilon
 (NU_{\rm aux}^{-1/2}+N^{7/8}U_{\rm aux}^{-1/2})\bigr).
\]

Choosing ε=τ/4 makes the first exponent 3999/4000<1 and the second
3499/4000<1, so both are o(u). The source estimates for ψ_Y follow
by its layer representation as the average of centered sharp windows
with widths between Y and (1+2κ)Y. The previous transfers are uniform
over these comparable widths; all gates remain frozen at x.

For pair d=pr with p≤r, the two additional covered wedges are

\[
\begin{array}{ll}
\mathcal A_\tau:&pr^2\le N^{3991/2000},\quad
                 p^3r^2\le N^{7489/2500},\\
\mathcal B_\tau:&pr^2\le N^{799/400},\quad
                 p^3r^2\le N^{1871/625}.
\end{array} \tag{13}
\]

These correspond respectively to A=a and A=a+δ in RS. The exact
vertex certificates give reserve 1/10000 throughout. The original
pair diagonal retains its half weight; its short floor contribution
is o(u) by the previous diagonal bound with the smaller small products.

## 6. Factor coverage and the remaining coupled estimate

Let 𝒢_τ be the auxiliary union of d≤N^(4609/4000) and the supported
pair wedges (13), and 𝒞_τ its complement in the actual outer support.
These are auxiliary sets, distinct from the frozen original D_good,C.
The exact identity gives

\[
\boxed{I_\kappa=
 B_{\tau,\mathcal G_\tau,\,db>N^{461/400}}(\psi_Y)
 +Q_{\mathcal C_\tau}(\psi_Y)
 -(1+\kappa)M_{\mathcal C_\tau}u+o(u).}
\tag{14}
\]

To verify (14), remove the proved good Type I remainder and small-db
Type II. On the core, retain all three discrete terms together:
I_(1,τ,C)+I_(2,τ,C)+B_(τ,C)=A_(Λ,C), exactly. Full-cofactor prime
powers are o(u). The condition d>N^(4609/4000) and b>V_aux excludes
core small-db rows eventually because
461/400<4609/4000+1/1000. The normalized long Type II and floor
errors are o(u) by the old long-reference proof. The remaining core
density integral is (1+κ)M_C u+o(u).

| Actual factor region | Type I remainder | Type II | Full centered prime count |
|---|---|---|---|
| All single-prime outers, z≤d<N^(.95) | o(u) | db≤N^(1.1525) removed; larger db open | Open |
| Pair outers in 𝒢_τ | o(u) | db≤N^(1.1525) removed; larger db open | Open |
| Pair outers in 𝒞_τ | Uncontrolled separately | Retained jointly with Type I | Open |

Thus Type I coverage is not a certificate that whole prime-product
regions have negligible discrepancy. The single-prime Type II family
still occurs in the first term of (14).

The outward reference integration uses canonical logarithmic coordinates
S=log_N(pr), a=log_N p. On the core S>4609/4000>9/8,
2S−2≤a≤S/2, with density 2/[a(S−a)(2−S)]. Removing the two
wedges gives the exact affine pieces saved in
results/spectral_coverage_reference.json. Its 12,000-bin interval
Riemann enclosures prove

\[
M_{\mathcal C_\tau}\in
[0.0606181981056243773390,\ 0.0606520446991740030317].
\tag{15}
\]

The original core coefficient is unchanged in its own files. The new
reference reduction is between .0278434u and .0279139u; it is not
earned prime mass or an error allowance. In particular, a concrete
sufficient new analytic task, with coefficients exactly one, is

\[
\boxed{B_{\tau,\mathcal G_\tau,\,db>N^{461/400}}(\psi_Y)
 +Q_{\mathcal C_\tau}(\psi_Y)
 \le(.0686138+o(1))u.} \tag{16}
\]

This decimal is rounded **down** from
(1+κ)·0.060618198105624377339043095546585986442385831820644
+ .007935 = .06861381630373000171638… . Using the certified lower
reference endpoint makes (16) sufficient without spending an unrecorded
enclosure error. Inequality (16) is unproved; the available completed
estimates give order O(u) without its coefficient.

## 7. Quantifying one persisting source gap

Checkpoint 14 already proved that the standard top-frequency reciprocal
mapping of RS1 and FI6 has no standalone slot when Σ≥5/4. Its necessary
slot widths are respectively 5−4Σ−7ν and (5−4Σ−3ν)/2. Shrinking an
auxiliary cutoff cannot remove this gap. This is a restriction of these
two mappings, not an impossibility result for other phases or joint sums.

The corresponding actual outer band 5/4≤S≤4/3 has reference mass

\[
M_{\ge5/4}=2\int_{5/4}^{4/3}
 \frac{\log((2-S)/(2S-2))}{S(2-S)}\,dS
 \in[.03558733741968899790,\ .03559402912923898414].
\tag{17}
\]

For a strategy that separately makes every other factor region o(u),
an isolated upper bound Q_band(ψ_Y)≤C⁺u would need
C⁺−(1+κ)M_band≤.007935. Its ratio C⁺/M_band must therefore be
about 1.224 or smaller. A factor-two upper estimate on this band
would not close that particular strategy. Other regions could instead
supply signed counterweights; (17) does not preclude such coupling.

Two stronger-looking published interfaces were checked without admitting
them for the missing estimate:

* Robert–Sargos (2006), Theorem 3 uses an unweighted free standalone
  integer sum. The current standalone prime/convolution coefficient is
  not such a sum. Theorem 1 remains the admitted weighted interface.
* Pliego (2024), Corollary 1.1 of *Estimates for a three-dimensional
  exponential sum with monomials* has particular power weights and a
  special domain D_T. Its strict 0<a<c<b phase requirements fail for
  the conjugate reciprocal exponents (−1,1,1), and its conclusion is not
  an arbitrary-coefficient dyadic bound. The paper itself records the
  domain-transfer limitation after the corollary.

Primary sources:
[Robert–Sargos (2006)](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)
and [Pliego (2024)](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1294.pdf).
The original FI6 source and audit are retained locally. No broader
exclusion of existing methods is asserted. A finer prime identity with
multiple free variables still needs a valid estimate for each resulting
phase and coefficient family before it can enter the coverage table.

## 8. Verification and next lemma

Run `python3 src/spectral_coverage.py` from the campaign directory.
It checks all 80 rational facet vertices, complete exact identities under
three independent stress cutoffs, the global cap on broader product
windows, the explicit three-mark witness, rational tail exponents, the
unchanged coefficient ledger and outward reference enclosures. The
analytic proofs are (5)–(12); finite checks do not prove (16).

The next required lemma is either the signed localized integral bound
in (11) at coefficient .007935, or the equivalent-up-to-o(u) coupled
estimate (14) at its exact reference coefficient. The downward-rounded
version (16) is a concrete sufficient formulation. It must retain the
actual B_τ coefficients and all gates; the separate marked task is not
used here. The original .011 comparison, H(ϑ), higher-degree allocation
and positive K remain open.
