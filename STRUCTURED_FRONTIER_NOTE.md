# H(ϑ) campaign — checkpoint 2

Michael M. Ross · 5 October 2026 · working target ϑ=97/100

The next input is now specified: a **positive, marked three-prime subterm of R₂**, with its actual coefficients, a centered long reference, and an explicit short-interval comparison to prove. Its long-reference mass is approximately **0.572678u**. An outward interval calculation certifies that this mass exceeds the working loss allowance. The previously inspected balanced Dirichlet-polynomial criterion covers none of this region at square-root length, regardless of which original prime is used as the residual factor.

These are a combinatorial reduction, a reference-mass calculation and a criterion-specific obstruction. **No short-interval transfer for this term, positive K, or H(ϑ) is proved.** The tail formula remains the submitted planning benchmark; its independent source audit is still partial. Checkpoint 1 is preserved in `CAMPAIGN_NOTE.md`.

## 1. A positive frontier with honest coefficients

Retain

\[
x=N^2,\quad N=2n,\quad Y=N+1,\quad
J_N=[x-N/2,x+N/2]\cap\mathbb Z,\quad
u=\frac{N}{2\log N},\quad w=N^{1/4},\quad z=N^{\vartheta}.
\]

Our cutoff convention is

\[
S_d(v)=\sum_r1_{J_N}(dr)1_{P^-(r)\ge v},\qquad P^-(1)=\infty.
\]

Two Buchstab steps give the exact identity

\[
S_1(z)=A_0-A_1+R_2,\qquad
R_2=\sum_{w\le p_2<p_1<z}S_{p_1p_2}(p_2).
\]

Thus a nonnegative subterm of R₂ can be retained in a lower bound. Write

\[
t_i=\log_N p_i\ (i=1,2),\qquad t_3=2-t_1-t_2.
\]

The selected limiting region is

\[
\mathcal P_\vartheta=\left\{
\tfrac14\le t_2\le t_1\le\vartheta,
\quad t_1+3t_2>2,
\quad t_1+2t_2<2
\right\}.
\tag{1}
\]

On any fixed compact interior region with these inequalities separated from equality, the residual r has

\[
p_2<r<p_2^2.
\]

If it is p₂-rough, it must therefore be prime. Indeed a composite p₂-rough r is at least p₂². The unit residual is excluded here because p₁p₂≤N^(2ϑ)<min J_N for all sufficiently large N. Prime powers in other branches remain part of the campaign.

For a fixed polygon D inside (1), define the exact marked count, for any interval I,

\[
Q_D(I)=\sum_{\substack{p_2<p_1\ \mathrm{prime}\\
w\le p_2,\ p_1<z\\
(\log_Np_1,\log_Np_2)\in D}}
\ \sum_{\substack{q\ \mathrm{prime}\\q\ge p_2}}
1_I(p_1p_2q).
\tag{2}
\]

It is a positive subterm even at a finite boundary, since the prime condition is imposed explicitly. The assertion that this is the *entire rough cofactor* on D uses a fixed margin and sufficiently large N; the limiting facets alone are not a finite-N primality test.

The marks matter. For example 385=5·7·11 appears in the terminal R₂ term with both (p₁,p₂,q)=(7,5,11) and (11,5,7), if the cutoffs permit them. Formula (2) retains both. There is no factorial divisor in its mass integral.

A concrete first test is the rectangle

\[
\frac{39}{50}\le t_1\le\frac{81}{100},\qquad
\frac{57}{100}\le t_2\le\frac{59}{100}.
\tag{3}
\]

Here 3/5≤t₃≤13/20, t₁+3t₂≥2.49 and t₁+2t₂≤1.99. The three primes satisfy p₂<q<p₁ for large N, so this particular box has a unique mark. It provides a small interior test before the whole region is considered.

The coefficients in a product box are simply

\[
a_j(m)=1_{m\ \mathrm{prime}}1_{P_j<m\le2P_j},\qquad j=1,2,3.
\tag{4}
\]

One may regroup the first two primes into

\[
\alpha_m=\sum_{\substack{p_1p_2=m\\p_i\in(P_i,2P_i]}}1,
\qquad\beta_q=1_{q\ \mathrm{prime}}1_{P_3<q\le2P_3}.
\]

These are fixed arithmetic coefficients of bounded multiplicity. They carry no free Mellin twists and no arbitrary bounded sequence. The comparator obstruction in checkpoint 1 does not rule out this class.

## 2. The reference mass can already be proved

Set L=log x and

\[
Y_1=x\exp[-3L^{1/3}],\qquad
\mathcal B_N=[x-Y_1/2,x+Y_1/2]\cap\mathbb Z.
\tag{5}
\]

For fixed D with a margin, the prime number theorem with an error of the form O(v·polylog(v)·exp(−c√log v)) gives

\[
Q_D(\mathcal B_N)=\frac{Y_1}{2\log N}
\left(M_D+o_D(1)\right),\qquad
M_D=2\iint_D\frac{dt_1dt_2}{t_1t_2(2-t_1-t_2)}.
\tag{6}
\]

This use of the prime number theorem is unconditional. For each pair p₁,p₂ the q-interval is centered at v=x/(p₁p₂), has length v·exp(−3L^(1/3)), and v≥N^c for a fixed c>0. The PNT error at its two endpoints is smaller than this main term by any logarithmic factor. This remains uniform away from the exponent facets. Partial summation in the two outer prime variables then gives

\[
\sum_{p_1,p_2}\frac{1}{p_1p_2\log(x/(p_1p_2))}
=\frac{1+o(1)}{\log N}
\iint_D\frac{dt_1dt_2}{t_1t_2(2-t_1-t_2)}.
\]

For the full polygon, first use fixed interior polygons and then let their margins tend to zero. The integrand is bounded on its closure for this fixed ϑ; boundary strips have vanishing long-reference mass. This limiting reference calculation does not assert anything about the short count.

For ϑ∈(4/5,1), the lower cutoff 1/4 is inactive in this particular region. Put t=t₂ and

\[
a(t)=\max(t,2-3t),\qquad b(t)=\min(\vartheta,2-2t).
\]

Then

\[
M_{\mathcal P_\vartheta}=
\int_{(2-\vartheta)/3}^{2/3}
\frac{2}{t(2-t)}
\log\left(\frac{b(t)(2-t-a(t))}{a(t)(2-t-b(t))}\right)dt.
\tag{7}
\]

There are three smooth pieces, separated at 1/2 and (2−ϑ)/2. This removes a moving-domain ambiguity from numerical integration.

The reproducible interval enclosures are in `results/structured_frontier_mass.json`. They use interval Riemann sums, 50-digit Decimal arithmetic with outward rounding at every operation, and neighboring representable values around each correctly rounded logarithm. They do not treat a quadrature package's error estimate as a proof. The script independently checks the arithmetic against exact rational values and five logarithms against rational atanh-series enclosures.

At the working target, exploratory quadrature gives

\[
M_{\mathcal P_{.97}}\simeq0.572678019235,\qquad
M_{\mathrm{box}\ (3)}\simeq0.004165006340.
\tag{8}
\]

Only the outward enclosures, not all the digits in (8), are certified. A conservative consequence of the saved certificate is

\[
0.572657<M_{\mathcal P_{.97}}<0.572699,
\qquad 0.0041649649<M_{\mathrm{box}\ (3)}<0.0041650478.
\tag{9}
\]

The benchmark constants are

\[
m=1+\log\frac{2-\vartheta}{\vartheta},\qquad
C=\frac83\log\frac{2-\vartheta}{5\vartheta-4}.
\]

At ϑ=.97, m−C≈0.547810725088. The enclosures certify

\[
M_{\mathcal P_{.97}}-(m-C)>0.024846.
\tag{10}
\]

This comparison has a specific meaning: **in a design that recovers the full reference mass on every other signed piece, dropping all of this positive marked region costs more than the final allowable model loss.** Such a design would leave approximately m−M=0.487339990491, below C≈0.512207284638.

It is not an unconditional ceiling for K, a failure certificate for every adaptive decomposition, or a claim that the marked triple products themselves are z-rough. They are restoration terms in an alternating identity. In particular, adding this mass to checkpoint 1's very negative one-step Type I result would still not give a useful lower bound.

## 3. The missing short-interval estimate

The sharp comparison to investigate is

\[
Q_D(J_N)-\frac{Y}{Y_1}Q_D(\mathcal B_N)
=o_D\left(\frac{Y}{\log N}\right)
\tag{11}
\]

for **every sufficiently large even N**, for each fixed polygon D contained in the interior with a fixed margin. An almost-all statement about interval centers does not supply this quantifier. A lower comparison would suffice on this positive branch.

For admission through independent prime boxes, use the stronger, explicit interface: for each fixed margin δ>0 and A>4, prove a uniform comparison error O_(δ,A)(Y L^(−A)) for the untwisted coefficients (4), for all boxes whose products can meet J_N and whose exponents remain within that margin. There are at most O(L³) boxes. Summing this error is then o(Y/L). Boxes that cross exponent facets can be omitted in this positive branch, and their long-reference mass tends to zero as the mesh and fixed margins are removed. This interface is a proposed input, **not an admitted theorem**.

A smooth formulation avoids pretending that a cutoff and its Mellin truncation have no cost. Fix ρ∈C_c^∞((−1/2,1/2)), 0≤ρ≤1, let c_ρ=∫ρ, and put

\[
W_h(v)=\rho((v-x)/h),\qquad
\widehat W_h(s)=\int_0^\infty W_h(v)v^{s-1}dv,
\]

\[
P_j(s)=\sum_{P_j<p\le2P_j}p^{-s},\qquad
F_{\mathbf P}(s)=P_1(s)P_2(s)P_3(s),\qquad
\Delta\widehat W(s)=\widehat W_Y(s)-\frac{Y}{Y_1}\widehat W_{Y_1}(s).
\]

Mellin inversion gives the exact centered discrepancy

\[
\sum_{p_j\in(P_j,2P_j]}
\left(W_Y(p_1p_2p_3)-\frac{Y}{Y_1}W_{Y_1}(p_1p_2p_3)\right)
=\frac{1}{2\pi}\int_{\mathbb R}
F_{\mathbf P}(\tfrac12+it)\Delta\widehat W(\tfrac12+it)dt.
\tag{12}
\]

The integral is absolutely convergent for this fixed smooth weight, since F is a finite Dirichlet polynomial and the Mellin transform decreases faster than any fixed power of |t|. The center x is part of the kernel; it must not be removed from the estimate.

Let T₀=exp(L^(1/3)). When P₁P₂P₃ is within fixed factors of x, elementary estimates give

\[
|F_{\mathbf P}(\tfrac12+it)|\ll\sqrt x,
\qquad
|\Delta\widehat W(\tfrac12+it)|
\ll_\rho\frac{Y}{\sqrt x}\frac{Y_1}{x}(1+|t|).
\]

The first bound follows by summing p^(−1/2) trivially in each box. The second follows by comparing the two scaled integrands and differentiating v^(−1/2+it). Their constants depend only on the fixed product factors and ρ. Hence the contribution of |t|≤T₀ is

\[
\ll_\rho Y\frac{Y_1}{x}T_0^2
=Y\exp(-L^{1/3})
=o(YL^{-A})
\]

for every fixed A. This part of the reduction is proved.

The remaining required estimate is now explicit:

\[
\left|\frac1{2\pi}\int_{|t|>T_0}
P_1(\tfrac12+it)P_2(\tfrac12+it)P_3(\tfrac12+it)
\Delta\widehat W(\tfrac12+it)dt\right|
\ll_{\delta,\rho,A}YL^{-A}.
\tag{13}
\]

It is required uniformly in the actual prime boxes above and in even N, for each fixed ρ and fixed margin δ. No arbitrary coefficient sequence or free frequency shift is included. Equation (13) retains oscillatory cancellation. Replacing it by an absolute mean-value bound is a stronger proposal that would need its own justification and tail control. We do not assert that a finite-height bound alone proves (13).

Because W_Y≤1_(J_N) on integers, (13) yields a lower bound with mass c_ρM_D. Taking fixed smooth minorants with c_ρ→1, followed by interior polygons approaching the full region, would recover its full positive mass. This states exactly how a successful input would be used and where uniformity is needed.

## 4. What the checked published criteria actually say

The source audit used the primary Baker–Harman–Pintz paper and Li's versioned exposition. The balanced criterion has two relevant facets, in x-exponents α:

\[
|\alpha_1-\alpha_2|<2\lambda-1,\qquad
\alpha_R<\Gamma_g(\lambda),\quad
\Gamma_g(\lambda)\le4\lambda-2.
\tag{14}
\]

It retains a source-specific prime-factored hypothesis on the residual polynomial. We do not use that hypothesis as a substitute for the exponent inequalities. The published interval ranges also do not authorize an endpoint extension to λ=1/2.

There is a stronger geometric exclusion here than the zero balance width alone. Every original prime factor in (1) has N-exponent strictly above (2−ϑ)/3. Indeed t₁≤ϑ and t₁+3t₂>2 imply t₂>(2−ϑ)/3; t₁≥t₂ and t₃>t₂ give the other two. At ϑ=.97 this is 103/300. Thus any nonempty residual group of whole original primes has

\[
\alpha_R>\frac{103}{600}.
\]

Consequently (14) would require

\[
\lambda>\frac{2+103/600}{4}
=\frac{1303}{2400}\simeq0.542916667.
\tag{15}
\]

This is a necessary consequence of one displayed cap, not a sufficient interval theorem at that exponent. It excludes the region for λ=1/2 and also for λ=.525, where the cap is only 1/10. For the actual length Y=N+1, λ_N=log(Y)/log(x)=1/2+o(1), so the cap is o(1); the exclusion survives the length correction. Permuting the three primes does not change their positive lower exponent bound. Grouping whole primes does not reduce it.

At the center of the concrete box (3), the x-exponents are

\[
(\alpha_{p_1},\alpha_{p_2},\alpha_q)
=(159/400,29/100,5/16).
\]

The three possible residual choices give the following exact necessary thresholds from just the two facets:

| Paired factors | Residual exponent | Pair difference | Necessary λ lower threshold |
|---|---:|---:|---:|
| p₁,p₂ | 5/16 | 43/400 | 37/64 = .578125 |
| p₁,q | 29/100 | 17/200 | 229/400 = .5725 |
| p₂,q | 159/400 | 9/400 | 959/1600 = .599375 |

The actual inequalities are strict. These are necessary thresholds only, and may lie outside a source theorem's stated range. All six permutations are recorded with exact rational arithmetic in `results/structured_frontier_obstruction.json`.

Li's Lemma 4.2 is a different, four-variable product criterion with every factor of positive exponent. It cannot be directly instantiated with three original primes and a unit fourth factor. Also every original prime here is strictly below N: t₁<1; for t₂≤1/2, t₃<2t₂≤1, while for t₂>1/2, t₃≤2−2t₂<1. No original prime fills its required α₁≥1−λ=1/2 slot at the endpoint. Grouping two primes fills a longer slot but leaves too few nonunit factors for this direct four-factor application. A valid further arithmetic decomposition or a different criterion would have to be supplied. This does not exclude every use of the general large-values machinery.

This geometry also explains the elementary gap. Every pair has limiting N-exponent 2−tᵢ>1, so fixing any two primes puts its divisor outside the admitted total-level <N floor-count estimate. Fixing p₁ and applying the plain lower linear sieve to the remaining p₂-rough cofactor does not help: t₁+2t₂>2−t₂>4/3, whereas a positive lower sieve term at the available interval level requires t₁+2t₂<1. These statements concern the specified elementary inputs, not every regrouping or sieve refinement.

The geometry is also encoded as nine exact nonnegative combinations of rational facets, rather than as a grid test. For example, with g₁=t₁−t₂≥0 and g₂=t₁+3t₂−2>0,

\[
t_1+t_2-1=(g_1+g_2)/2>0.
\]

The certificate verifies each linear identity and that at least one strictly positive input has a positive coefficient. This supplies the factor and pair bounds used above.

Existence of an almost-prime in a short interval, an almost-all interval theorem, or the reciprocal-phase upper-tail estimate likewise does not supply the particular marked count and pointwise comparison (11). None is admitted to this lower-mass calculation without that reduction.

## 5. Verification, status and the next gate

The new standard-library program is `src/structured_frontier.py`. It verifies the frozen source hashes, checks 15 exact forced-prime counts, retains repeated primes, checks the two-mark witness, encloses both reference integrals and the planning loss budget, and verifies nine rational facet identities and six permutations. Those checks certify these arithmetic and numerical statements. They do not test the analytic asymptotic (11) on a finite sample.

The coefficient class and its comparator are now specified. The reference mass and the failure of the checked balanced criterion are established. **The high-frequency estimate (13) is the next analytic proof gate.** The first test can be the interior box (3); its successful treatment would establish a valid input, although its approximately .004165u mass alone would not close the campaign. The next research task is to derive (13), or a sufficient one-sided version, using a theorem whose hypotheses cover this concrete prime convolution. If that fails, record the exact missing frequency or exponent saving before changing the decomposition.

The campaign state remains: K=0 from nonnegativity, no positive Type II mass admitted, full adaptive mass optimization pending, H(ϑ) open. The original tail source audit remains a separate outstanding task.

## Sources

1. R. C. Baker, G. Harman and J. Pintz, *The difference between consecutive primes, II*, Proc. London Math. Soc. 83 (2001), 532–562, especially Lemmas 6 and 9 and §5. [Primary paper](https://www.cs.umd.edu/~gasarch/BLOGPAPERS/BakerHarmanPintz.pdf). Its Perron/mean-value organization motivates (12); the centered smooth reduction above is stated and proved directly rather than invoking its theorem outside its interval range.
2. R. Li, *The number of primes in short intervals and numerical calculations for Harman's sieve*, arXiv:2308.04458v8, Lemmas 4.1–4.2. [Versioned primary text](https://arxiv.org/html/2308.04458v8). Source of the compact criterion checked in (14) and the direct four-factor applicability test.
3. A. Fiori, H. Kadiri and J. Swidinsky, *Sharper bounds for the error term in the Prime Number Theorem*, arXiv:2206.12557v2. [Primary record and abstract](https://arxiv.org/abs/2206.12557v2). Supplies more than the PNT error strength needed for (6).
4. Python documentation, `decimal.Decimal.ln`. [Official specification](https://docs.python.org/3/library/decimal.html#decimal.Decimal.ln). States correct rounding to ROUND_HALF_EVEN; the script adds an outward representable neighbor on each side.

The source files supplied by the user remain the frozen project baseline. The selected term, long-reference proof, centered smooth reduction, mass enclosures and residual-cap exclusion are calculations made in this checkpoint.
