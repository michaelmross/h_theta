# Testing the recombined sharp short-window comparison

Checkpoint 32 — Michael M. Ross's H(ϑ) campaign — 13 October 2026

**The sharp short-window inequality is not proved. No improved actual
deficit coefficient is obtained in this checkpoint.**

The attempt recombines the complete Vaughan expansion before estimation,
then tests current generic large-value bounds on the actual four-prime
coefficient family. The test fails even after allowing every fixed mixed
integer moment of the four prime polynomials. A retained physical box
has weighted reference at least (.000351+o(1))u, so omitting this box
would exceed the entire remaining .000099 comparison budget.

This is a scoped obstruction to that absolute mean-value method. It is
not a lower bound for the actual frequency error, a counterexample to
the requested inequality, or an exclusion of prime-specific joint or
phase-sensitive estimates. In particular, the source bounds do not
show that the problematic large-value states occur.

## 1. The actual coupled target is retained

Keep checkpoint 31's x=N², Y=N+1, u=N/(2 log N), the original H₁,
κ=1/1000, the actual fifth-degree kernel W_N, and its physical gates.
The exact definitions give

\[
\mathcal L_N(\psi_Y)+\mathcal B_N(\psi_Y)
 =\mathcal P_N(\psi_Y)-\mathcal C_N(\psi_Y).
\tag{1}
\]

Thus recombining the 80 all-Type-I and 325 with-Type-II subterms
returns the full four-detector count. This retains their cancellations
on composite slots. It is not a separate estimate of their absolute
values. Checkpoint 31's normalization proves

\[
\Delta\mathcal W_N
 =\mathcal P_N(\psi_Y)-\mathcal C_N(\psi_Y)+o(u).
\tag{2}
\]

The requested analytic input remains

\[
\boxed{\mathcal P_N(\psi_Y)-\mathcal C_N(\psi_Y)
 \ge-(\eta_W+o(1))u,\qquad
 \eta_W+\eta_{\rm rest}\le .000099.}
\tag{3}
\]

The actual prime-product representation, obtained after the already
proved proper-power padding and denominator freezing, has weight

\[
\frac16\sum_{j=1}^5c_j27^j
 \frac{\prod_{i=2}^4(\log p_i)^j}
      {(\log(x/p_1))^{3j}},
\quad
c_j=(-1)^{j+1}\binom5j,
\tag{4}
\]

on ordered four-prime tuples with p₁ in [N^.40,N^.43] and p₂,p₃,p₄≥p₁.
The common kernel is Φ₅(v)=1−(1−v)⁵, as in checkpoint 30.
All five logarithmic moments remain; no original prime sector is dropped.

In a dyadic physical box, each moment in (4) separates into four prime
Dirichlet polynomials with coefficients bounded by constants depending
only on j. For example, with ℓ=log N, the first-slot coefficient is
(ℓ/log(x/p₁))^(3j), and the other three are (log p_i/ℓ)^j.
The factors ℓ^(3j) cancel. These coefficients are prime-supported;
they are not unit coefficients on free integer intervals.

## 2. The modern source and its precise scope

The primary source checked is [Matomäki–Pandey–Pliego–Teräväinen–Wang,
arXiv:2610.09567v1](https://arxiv.org/html/2610.09567v1), Definition 2.2,
Lemma 2.3(i),(ii), and Proposition 3.2. Its generic coefficient class is
divisor bounded. Its large-value bound applies for T=X^τ with 0<τ≤1,
including the critical τ=1/2. The mean-value proposition itself has
τ<1/2 and requires a strict positivity margin.

For the source's level parameter, here written υ to distinguish it from
the arithmetic kernel ν_p, the generic exponent is

\[
\begin{aligned}
K_0(b,\upsilon;\tau)=\min\{&\tau+b(6\upsilon-2),\\
 &\max(\tau+b(4\upsilon-8/5),\tau/2+b(4\upsilon-1)),\\
 &\tau+b(2\upsilon-1)\},\\
K(b,\upsilon;\tau)&=\min\{\tau,\max(2b\upsilon,K_0(b,\upsilon;\tau))\}.
\end{aligned}
\tag{5}
\]

The refined free-coefficient clause requires coefficients of the form
1_I(n)χ(n)log^r n, with I an integer interval, χ a suitable character,
and r=0 or 1. The recombined prime indicators do not meet that clause.
Dropping their prime masks to use it would change the actual count.
No such replacement is admitted here.

## 3. A test that includes all fixed mixed integer moments

Use X=x, not N. A physical prime length N^a has source exponent β=a/2.
If the four primitive source lengths have exponents β_i with sum 1,
the simultaneous level υ=3/10 means

\[
|A_i(1/2+it)|\asymp x^{\beta_i/5}.
\tag{6}
\]

Their product has amplitude x^(1/5). For an absolute mean-value bound
at height T≍√x, the corresponding level set needs exponent at most
3/10, with further saving, to give an error on scale √x/log x.

Allow every fixed vector k=(k₁,k₂,k₃,k₄) of nonnegative integers,
not all zero. The mixed polynomial ∏A_i^k_i has length exponent
b=Σk_iβ_i and level υ=3/10. Its coefficients remain of fixed divisor
order. Splitting its product support into finitely many dyadic ranges
has no power cost, exactly as in the source's proof for powers.
The generic bound therefore supplies a level-set exponent K(b,3/10;τ).
Taking all such mixed products is more generous than testing only
powers of individual slots or one fixed grouping.

At this particular level the formula simplifies exactly:

\[
\boxed{K(b,3/10;\tau)
 =\min\{\tau,\max(3b/5,\tau-2b/5)\}.}
\tag{7}
\]

Indeed the third term τ−2b/5 in K₀ is no larger than its first term,
and no larger than the maximum in its second term. At τ=1/2, the
smallest possible value over unrestricted b>0 is 3/10, attained only
at b=1/2. An available mixed-product length that misses 1/2 gives a
strictly worse exponent. Logarithmic sparsity gains do not repair a
fixed positive power gap in this test.

For an interior illustration take the N-exponent quartet

\[
(a_1,a_2,a_3,a_4)=(.415,.460,.515,.610),
\quad
\boldsymbol\beta=(83/400,23/100,103/400,61/200).
\tag{8}
\]

All fixed mixed integer moments have best source exponent
61/200=.305, attained by the product of the middle two slots,
whose length exponent is 39/80. The product-amplitude exponent 1/5
then gives a source upper-envelope exponent 101/200=.505,
rather than the required 1/2. These are exponents of the available
bounds, not exponents asserted for the actual integral.

## 4. Continuous failure on a retained physical box

Consider squarefree n=prst with its prime factors sorted p<r<s<t and
N-exponents

\[
a\in[.40,.43],\qquad b\in[.45,.47],\qquad
c\in[.505,.525],\qquad d=2-a-b-c\in[.575,.645].
\tag{9}
\]

Call this physical box Q. Its ranges are disjoint and sorted; all
original band and residual rough-degree conditions are satisfied.
In the actual windows log_N n=2+o(1), so the limiting equalities in
(9) have uniform o(1) perturbations. The strict margins below persist.

The source exponents are a/2,b/2,c/2,d/2. Every single-slot length is
below 1/2. For a mixed moment of total degree two, the possibilities
on Q satisfy the following separation from 1/2:

| Pair, including repetitions | N-exponent sum range relative to 1 |
|---|---|
| p+p, p+r, p+s, r+r, r+s | ≤.995 |
| p+t, r+t, s+s, s+t, t+t | ≥1.005 |

For instance r+s≤.995 and p+t=2−b−c≥1.005. All mixed moments of
total degree at least three have source length exponent at least
3·(.40/2)=3/5. Consequently, for every nonzero integer vector k,
its source length either lies below 199/400, lies above 201/400,
or is in the still larger degree-at-least-three range.

Using (7), the full mixed-moment family therefore has

\[
\boxed{\inf_{\boldsymbol k\ne0}
 K(\boldsymbol k\cdot\boldsymbol\beta,3/10;1/2)
 \ge\frac{301}{1000}>\frac3{10}
 \quad\text{throughout Q}.}
\tag{10}
\]

Below 1/2 the profile is at least 1/2−(2/5)(199/400)=301/1000.
Above 1/2 it is at least (3/5)(201/400)=603/2000;
total degree at least three gives at least 9/25 until the trivial cap
1/2 is reached. These inequalities prove the continuous statement;
finite corner checks are supplementary.

This is not just a failure to satisfy the endpoint hypothesis of the
source's Proposition 3.2. At the admitted height exponent τ=999/2000,
the corresponding minimum is still at least 601/2000>.3. Thus the
same level already fails to supply its positivity margin below 1/2.
This failure persists even granting its other pointwise hypotheses
and all required completions at no power cost. No successful full
invocation of that proposition for the weighted family is asserted.

## 5. This box cannot be omitted within the budget

Let W_Q be the actual checkpoint-30 kernel restricted to the sorted
four-prime rows in Q. It is nonnegative and lies below W_N. Ordinary
long PNT and the same coarea argument as checkpoint 31 give

\[
a_N\mathcal W_Q(\psi_{H_1})=(M_{Q,W}+o(1))u,
\tag{11}
\]

where

\[
M_{Q,W}=2(1+\kappa)
 \int_{.40}^{.43}\int_{.45}^{.47}\int_{.505}^{.525}
 \frac{\Phi_5(27bcd/(2-a)^3)}{abcd}\,dc\,db\,da,
\quad d=2-a-b-c.
\tag{12}
\]

There is no factor 1/6 in (12): one sorted representation is selected,
and the six ordered residual-prime representations in P_N have that
same symmetric kernel. The box has no repeated-prime rows because
its four prime ranges are disjoint. The additional box gates have
bounded variation in each physical slot, so checkpoint 31's normalized
long PNT error remains o(u) here. No short prime asymptotic is used.

Checkpoint 30 proves the uniform seed bound ν≥27/32+o(1), hence the
kernel weight is at least 1−ε₅+o(1), where ε₅=(5/32)⁵. The box volume
is .03·.02·.02. Its denominator is at most .43·.47·.525·.645.
It follows that

\[
\begin{aligned}
M_{Q,W}
 &\ge2(1+.001)(1-\epsilon_5)
       \frac{.03\cdot.02\cdot.02}{.43\cdot.47\cdot.525\cdot.645}\\
 &=\frac{1599278967}{4556220006400}
  >.000351>.000099.
\end{aligned}
\tag{13}
\]

The displayed rational constant is a proved lower bound, not a
numerical enclosure of the entire box reference.

If a proposed lower weight simply deletes Q and relies on nonnegativity
for its short contribution, its reference loss must be at least (13).
Even allocating the entire present .000099 comparison/rest budget
to that omission would fail. No such loss is added to the campaign's
allowance. This argument says nothing about the actual sign of ΔW_Q.

## 6. The missing information is now explicit

The original smoothing does not suppress the critical height by a
power of x. With sinc(z)=sin(z)/z and sinc(0)=1, its exact rectangular
convolution representation gives, uniformly for N/2≤t≤N,

\[
\begin{aligned}
\widehat\psi_Y(1/2+it)
={}&x^{-1/2+it}(1+\kappa)Y
 \operatorname{sinc}\!\left(\frac{(1+\kappa)tY}{2x}\right)
 \operatorname{sinc}\!\left(\frac{\kappa tY}{2x}\right)
 +O(N^{-1}).
\end{aligned}
\tag{13a}
\]

To justify the error, write v=x+h on the support |h|≤(.5+κ)Y
and use log(1+h/x)=h/x+O((h/x)²). The combined amplitude and phase
error is O(1/N); the scaled trapezoid area is O(1). Its Fourier
transform is the product in (13a), since ψ_Y is the convolution of
rectangles of lengths (1+κ)Y and κY, divided by κY. For large N,
the two sinc arguments have absolute values at most .51 and .001.
The inequality sinc(z)≥1−z²/6 on these ranges proves

\[
\boxed{|\widehat\psi_Y(1/2+it)|\ge .9
 \quad(N/2\le t\le N,\ N\text{ sufficiently large}).}
\tag{13b}
\]

The phase x^(it) is retained. This is a multiplier bound, not a lower
bound on any centered integral. This frequency block remains inside
the original required short-frequency range; it is not an omitted tail.

At the common level (6), the source's generic moment envelopes allow
a level-set exponent at least .301 on Q. Their associated absolute
contribution envelope therefore has exponent at least .501, before
fixed logarithms and completions. This fixed power loss prevents this
route from producing any fixed u-scale coefficient, including .000099.
It is not an actual lower bound on an error or on a level-set size.

One sufficient additional input for this particular absolute method
would be a prime-specific joint bound of the shape

\[
\#\{t\in\mathcal U:
 x^{\beta_i/5}\le|A_i(1/2+it)|<2x^{\beta_i/5}
 \ (i=1,2,3,4)\}
 \ll_A\frac{x^{3/10}}{(\log x)^A},
\tag{14}
\]

for every fixed A, uniformly in the relevant actual prime polynomials,
physical boxes and 1-separated U⊂[c√x,C√x]. The product amplitude
on this state is O(x^(1/5)), so (14) would control its absolute mean
with arbitrary logarithmic saving. This would handle this identified
state, not automatically all other levels, boxes, or η_rest.

Alternatively, a one-sided phase-sensitive estimate for the actual
centered short product integral could avoid that absolute level-set
requirement. No such estimate or (14) is proved here. In particular,
the fact that each prime polynomial has a long mean does not bound
this simultaneous short-frequency state.

| Required item | Status after this attempt |
|---|---|
| Full 80/325 arithmetic coupling | Retained exactly before estimation |
| Generic large-value source coefficients and powers | Checked |
| All fixed mixed integer moments | Included in the negative source test |
| Critical source positivity margin on Q | Fails continuously |
| Deleting Q within .000099 | Fails by its actual long-reference lower bound |
| Actual critical level-set sizes or signs | Not determined |
| Sharp short-window lower comparison (3) | Unproved; no improved actual coefficient |
| Prime-specific joint or phase-sensitive method | Not excluded; additional input required for this route |

The next actual analytic task remains (3). A concrete unresolved test
is the genuine short comparison on Q, keeping all its prime factors
and the actual Φ₅ weight, or an estimate controlling its contribution
in the whole coupled sum. Another continuous normalization or another
unrestricted O(u) envelope would not settle this missing coefficient.

## 7. Preserved coefficient ledger and verification

The unchanged sufficient original coefficient is

\[
.003065+.007825257+.000001+\eta_W+\eta_{\rm rest}
                   +\xi+21147/L\le .011,
\quad\eta_W+\eta_{\rm rest}\le .000099.
\tag{15}
\]

The spectral allowance remains .007935 after omitting the smoothing
charge .003065. The conditional kernel charge .000001 remains inside
the original .0001 complement budget. No fixed original least-prime
power or frequency sector is discarded. Any later deletion requires
its original ξ or 21147/L charge. The .000351 box certificate is not
a permitted new error charge. All historical mass ledgers and
reference enclosures are unchanged; K=0, H(ϑ) and the sharp targets
remain open, and milestone 7 remains deferred.

Run `python3 src/sharp_short_window_test.py`. Exact rational checks
verify the source-profile simplification, all mixed moments through
degree four, the continuous length-gap certificate and reference
lower bound. The infinite higher-degree family is handled by the
analytic lower length 3/5 in Section 4. These checks do not verify
that problematic frequency states occur, or prove (3). All 305
nonmutable checkpoint-31 records are preserved byte for byte.
