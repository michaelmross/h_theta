# H(ϑ) campaign — checkpoint 3

Michael M. Ross · 5 October 2026

The priority has changed. Checkpoint 2 specified a strong three-prime comparison, but recovering that positive term alone would not close the current lower bound. The signed ledger shows that the much larger problem in the current design is the excess in the first negative upper bound. This checkpoint adds a valid way to reuse the frozen tail estimates on that negative branch, derives its optimal intermediate cutoff, and states an aggregate inequality with an allowed loss that would suffice.

**No positive K or H(ϑ) is proved.** The new upper-branch reduction is proved as an implication from the submitted tail estimates. Their independent source audit is still partial; the resulting numerical improvement is conditional on those frozen estimates. The new aggregate inequality is an unproved research target.

## The signed ledger identifies the deficit

Use N=2n, x=N², Y=N+1, u=N/(2 log N), w=N^(1/4), and the same exact cutoff convention as before. The two-step identity is

\[
S_1(N^{\vartheta})=A_0-A_1+R_2,
\quad A_0=S_1(w),\quad
A_1=\sum_{w\le p<N^{\vartheta}}S_p(w).
\]

On the centered long reference from checkpoint 2, the normalized masses are

\[
a_0=8\omega(8),\qquad
a_1=8\int_{1/4}^{\vartheta}\frac{\omega(8-4t)}t\,dt,
\qquad r_2=m(\vartheta)-a_0+a_1.
\tag{1}
\]

Here ω is Buchstab's function: ω(v)=1/v on [1,2], and

\[
v\omega(v)=1+\int_1^{v-1}\omega(s)\,ds\qquad(v\ge2).
\]

The quantitative PNT used in checkpoint 2 gives the long rough-count density. Repeated prime factors have vanishing long-reference mass; this observation is not used to erase any unverified short-interval terms. For A₁, fixing p=N^t leaves a w-rough cofactor at N^(2−t). Integrating its density against the outer prime harmonic measure gives (1). The residual 1 in A₁ is excluded because p<N^ϑ<x. The R₂ mass then follows from the exact signed identity, rather than a new multidimensional quadrature.

At ϑ=.97, the following are conservative outward bounds from `signed_mass_ledger.json`:

| Term | Sign | Long-reference coefficient | Currently available short bound |
|---|---:|---:|---:|
| A₀ | + | 4.491591 < a₀ < 4.491761 | Lower: 4 log 3 ≈ 4.394449 |
| A₁ | − | 6.089782 < a₁ < 6.090254 | Upper: ≈ 18.298844 |
| R₂, all cofactors | + | 2.658040 < r₂ < 2.658680 | Lower: 0 |
| Terminal prime part of R₂ | + | .572657 < M < .572699 | Lower: 0 |
| Remaining part of R₂ | + | 2.085341 < M < 2.086023 | Lower: 0 |

The root loses less than .097311u against its reference. The A₁ upper estimate has an excess between 12.208590u and 12.209062u. Even **assuming** a complete reference transfer for all of R₂ would leave the present Type I calculation below −11.2457u. Thus the earlier .572678u positive region is not the immediate bottleneck of this design.

The enclosures use 20,000 cells per unit in Buchstab's delay equation. Each cell uses only previously enclosed cells at arguments shifted by 1; numerator and denominator bounds are rounded outward. This is a causal interval proof, not an ODE solver's claimed tolerance. Closed-form values at 2, 5/2 and 3 provide independent checks. The model masses are not admitted as short-interval estimates.

## The tail can bound a negative frontier

Use the one-step identity directly:

\[
S_1(N^{\vartheta})=A_0-R_1,
\qquad R_1=\sum_{w\le p<N^{\vartheta}}S_p(p).
\]

For 4/5<κ<ϑ split it exactly into

\[
R_{1,\mathrm{low}}=\sum_{w\le p<N^\kappa}S_p(p),
\qquad
R_{1,\mathrm{high}}=\sum_{N^\kappa\le p<N^\vartheta}S_p(p).
\tag{2}
\]

Every cofactor counted in the high branch is prime for all sufficiently large N. It is p-rough and below p² because 3κ>2; it cannot be 1. Since p<N^ϑ<N and the product lies near N², the other prime exceeds N. Each semiprime has its smaller prime p extracted exactly once. Therefore the high branch is a subset of the frozen semiprime tail T(κ), and the global theorem alone gives

\[
R_{1,\mathrm{high}}\le(C(\kappa)+o(1))u.
\tag{3}
\]

The submitted proof supplies more than a global bound: its positive slice estimate is integrated over the larger-prime exponent. For the high branch in (2), that larger prime lies between N^(2−ϑ)(1−O(1/N)) and N^(2−κ)(1+O(1/N)). Restrict the same positive slice estimates to this band. With a=2−log_N(q), their integral gives

\[
R_{1,\mathrm{high}}
\le\left(\int_\kappa^\vartheta
\frac{16\,da}{(2-a)(5a-4)}+o(1)\right)u
=\left(C(\kappa)-C(\vartheta)+o(1)\right)u.
\tag{4}
\]

This follows from the per-slice proposition and level profile in the frozen paper. It does **not** follow by subtracting two global upper bounds. Endpoint block enlargement has vanishing normalized cost for fixed κ>4/5. The same outstanding source issues in the original slice proof remain outstanding here; this reduction introduces no additional three-prime transfer hypothesis.

For the low branch, S_p(p)≤S_p(w), so the admitted cofactor Type I upper sieve gives

\[
R_{1,\mathrm{low}}\le
\left(4\log\frac{3\kappa}{1-\kappa}+o(1)\right)u.
\tag{5}
\]

Combining (4), (5), and the root lower bound yields the new conditional bound

\[
K_{\mathrm{raw}}(\kappa;\vartheta)
=4\log\frac{1-\kappa}{\kappa}-C(\kappa)+C(\vartheta).
\tag{6}
\]

Its best interior split is

\[
\kappa_*=5-\sqrt{17}\simeq .8768943744,
\]

provided κ*<ϑ. Indeed the derivative of the negative cost is

\[
\frac4{\kappa(1-\kappa)}-
\frac{16}{(2-\kappa)(5\kappa-4)},
\]

whose numerator vanishes exactly when κ²−10κ+8=0; its sign changes from negative to positive at κ*. The rational split κ=877/1000 avoids relying on rounded optimization output. At ϑ=.97 it gives

| Calculation | Raw lower coefficient |
|---|---:|
| Previous Type I design | −13.9043947593 |
| Global tail reuse, equation (3) | −10.7119988692 |
| Restricted slice reuse, equation (4) | −10.1997915846 |

The restricted slice reduction gains **3.7046031748u** over the previous raw calculation. All three raw constants remain negative; after nonnegativity, the certified K is still zero. This is an improvement of a specified bound, not a positive-count theorem.

## A concrete sufficient aggregate upper bound

Take κ₀=19/20=.95 and define the negative frontier

\[
\mathcal R_{.95}(N)=
\sum_{N^{1/4}\le p<N^{19/20}}S_p(p).
\]

The next useful input can be an aggregate, one-sided inequality:

\[
\boxed{\quad
\mathcal R_{.95}(N)\le(3.49+o(1))u
\quad\text{for every sufficiently large even }N.
\quad}
\tag{7}
\]

This permits a loss relative to the reference upper value on this frontier. It retains the exact rough cofactor, the prime cutoff and the pointwise quantifier. It requires an upper bound on the aggregate negative term, with an o(u) error. It applies to a different frontier from checkpoint 2; recovery of that selected three-prime term alone does not imply (7).

If (7) holds, the existing root bound gives

\[
S_1(N^{.95})\ge(4\log3-3.49-o(1))u
\simeq(0.904449155-o(1))u.
\]

The frozen tail constant is C(.95)≈.897259298. Thus this input would prove a positive prime lower coefficient

\[
4\log3-3.49-C(.95)>0.00718.
\tag{8}
\]

It would close the weak K>C route at .95. With the regional estimate (4), it would also give a lower coefficient greater than .51939 at the original target .97, above C(.97)≈.512207285.

The critical upper threshold in (7) is 4 log 3−C(.95)≈3.497189857. The long-reference value of its left side is a₀−m(.95), enclosed between 3.391508 and 3.391677. Therefore an additional loss of .1u relative to that value is also sufficient, with a rigorously enclosed positive margin greater than .00551u. Neither version of (7) is currently proved. The present Type I plus regional-tail upper estimate is still about 14.2092u, so the gap is substantial and explicitly measured.

The next decomposition should therefore refine the **negative** frontier in (7), recording the upper mass on each signed branch and using the semiprime slice bound where it applies. A full three-prime asymptotic is a possible future tool, but it is no longer treated as a prerequisite before doing this signed optimization.

## A family-wide endpoint obstruction

The source audit now covers the Hölder/moment construction in Li's proof after Lemma 4.5, including the nine displayed five-factor cells and the 87 six-factor cells. Write λ for the interval exponent, d=1−λ, and let the finite moment orders satisfy δ₁=2 and Σ_j 1/δ_j=1. The thresholds of that construction have coefficient sum

\[
1+\sum_{2\le j<n}\frac2{\delta_j}+
\frac2{\delta_n-1}
=2+\frac2{\delta_n(\delta_n-1)}.
\]

At λ=1/2 their sum forces

\[
\sum_j\alpha_j\ge
1+\frac1{\delta_n(\delta_n-1)}>1,
\]

contradicting the product-length condition Σα_j=1. This proves the formal endpoint collapse for **every fixed finite moment tuple in that construction**, without checking only a sample of the 96 displayed cells. The necessary interval exponent is at least

\[
\lambda\ge\frac12+
\frac1{2(\delta_n(\delta_n-1)+1)}.
\]

All four separate cases of Li's Lemma 4.2 also have exact sum or complementary-facet contradictions at λ=1/2. Their necessary lower thresholds are respectively 29/57, 67/133, 31/61 and 14/27. The rational certificates are in `moment_family_endpoint.json`.

This is a statement about the unchanged finite moment construction and those four displayed cases. It does not apply a source theorem outside its interval range, exclude other large-values arguments, or prove that new mathematics is unavoidable. Allowing moment orders to grow with N would need uniform estimates beyond the fixed-parameter source statement.

## Reproduction and proof status

Run `python3 src/signed_mass.py` after the earlier scripts. It writes the interval ledger and exact moment certificates. The earlier frozen files and checkpoint notes are preserved. The new script uses the standard-library outward arithmetic from checkpoint 2 and checks Buchstab's known low-argument formula as well as the exact moment identities.

The proved additions are the reference ledger, the reduction of the negative high branch to the frozen tail/slice statements, the optimum split of this particular bound, and the finite-moment endpoint contradiction. The tail source audit remains partial. Inequality (7), positive K and H(ϑ) remain open.

Sources: the supplied `baseline/one-hypothesis.tex`, especially the swap lemma, slice proposition, tail integral and assembly; [Li, arXiv:2308.04458v8, Lemmas 4.2–4.5 and the proof following 4.5](https://arxiv.org/html/2308.04458v8); and the quantitative PNT source and Decimal arithmetic specification listed in checkpoint 2. The ledger, restricted-band reduction and algebraic endpoint certificates are calculations made here.
