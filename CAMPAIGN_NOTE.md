# A systematic campaign on H(ϑ): first checkpoint

Michael M. Ross's interval project — 4 October 2026.

This checkpoint launches the seven milestones in the supplied image. It establishes a reproducible baseline, a weaker sufficient objective, a complete exact Buchstab backbone, and a starter constraint inventory. It also gives a rigorous Type I calculation and a coefficient obstruction that the campaign must respect. It does **not** establish H(ϑ), a positive lower constant K, or the best result obtainable from all existing analytic tools.

## 1. Frozen benchmark and audit scope

Retain

\[
N=2n,\qquad x=N^2,\qquad
\mathcal A=[N^2-N/2,N^2+N/2]\cap\mathbb Z,
\qquad u=\frac{N}{2\log N}.
\]

The supplied Theorem A is the planning benchmark:

\[
T(\vartheta)\le(C(\vartheta)+o(1))u,
\qquad C(\vartheta)=\frac83\log\frac{2-\vartheta}{5\vartheta-4},
\qquad \frac45<\vartheta<1.
\]

The supplied files are copied unchanged under `baseline/`, with byte hashes. The original `fm_exact.py` was run to completion. Its five in-range levels are exactly

| γ | 1 | 21/20 | 11/10 | 23/20 | 6/5 |
|---|---:|---:|---:|---:|---:|
| β | 1/4 | 3/16 | 1/8 | 1/16 | 0 |

It reproduces the balanced witness μ=11/20, η=9/40 at γ=11/10, β=1/8, and the threshold

\[
\vartheta^{**}=0.939304820059\ldots.
\]

These computations certify the submitted linear-inequality model. They do not independently verify that every analytic reduction in the tail proof satisfies every hypothesis of its cited theorems. In particular:

- Robert–Sargos Theorem 1 was checked against the authors' full text; its four terms and coefficient slots match the displayed engine in the supplied paper.
- The linear inequalities, profile integral, and race constants have been checked. The companion's relaxed encodings remain subject to its stated sandwich argument and boundary conventions.
- A full independent audit of the Fouvry–Iwaniec pipeline and the exact Iwaniec remainder representation, including adaptive splitting of smaller modulus blocks, is still pending. Full text of those two primary sources was not successfully retrieved in this pass.
- The supplied program does not itself run a separate “remove FI/remove the extra exponent pair” experiment. Its advertised byproduct should not be treated as an additional reproduced computation.

Thus the prime consequence below is conditional on the frozen tail theorem as supplied until that source audit is complete. This checkpoint makes no modification to that paper.

## 2. The minimal sufficient objective

For ϑ>2/3, the rough elements of this interval are primes and semiprimes. With consistent strict cutoff conventions one has exactly

\[
\pi(\mathcal A)=S(\mathcal A,N^\vartheta)-T(\vartheta).
\]

Consequently, it is enough to prove, for one fixed ϑ∈(4/5,1),

\[
S(\mathcal A,N^\vartheta)\ge(K(\vartheta)-o(1))u,
\qquad K(\vartheta)>C(\vartheta).
\]

This would give a positive prime lower bound with constant K−C. Full H(ϑ) asks for the stronger constant

\[
m(\vartheta)=1+\log\frac{2-\vartheta}{\vartheta}.
\]

If a valid lower-bound construction yields K=m−ℒ, then its allowable loss is

\[
\mathcal L(\vartheta)<m(\vartheta)-C(\vartheta).
\]

The word “valid” matters: a model integral, an experimentally observed mass, or geometric coverage by an estimate whose coefficient assumptions fail cannot be credited as a proved K.

| ϑ | Buchstab value m | Required K > C | Allowable loss m−C | Hypothetical linear ceiling 2(m−1) |
|---:|---:|---:|---:|---:|
| 0.940 | 1.120144 | 1.106517 | 0.013627 | 0.240289 |
| 0.950 | 1.100083 | 0.897259 | 0.202824 | 0.200167 |
| 0.970 | 1.060018 | 0.512207 | 0.547811 | 0.120036 |
| 0.980 | 1.040005 | 0.333768 | 0.706237 | 0.080011 |
| 0.990 | 1.020001 | 0.163316 | 0.856684 | 0.040001 |
| 0.995 | 1.010000 | 0.080814 | 0.929186 | 0.020000 |

Use ϑ=97/100 as the first working target, while keeping ϑ variable in the code. This is a practical starting point, not a proved optimal choice. Moving ϑ toward 1 shrinks C, but moves the roughness cutoff toward the prime-detecting endpoint; the mass optimization must account for both effects.

### The weaker target still breaks the linear-sieve barrier

Put t(ϑ)=log((2−ϑ)/ϑ). At the actual unconditional Type I level D=N^(1−ε), the lower sieve function is zero. Even if one hypothetically had the usual linear-sieve remainder control at every level D=N^κ with κ<2, its lower main-term constant could be at most 2t(ϑ), by the calculation in the supplied paper.

For the whole benchmark range,

\[
C(\vartheta)>2t(\vartheta),\qquad 4/5<\vartheta<1.
\]

Indeed C−2t tends to zero as ϑ→1, and

\[
\frac{d}{d\vartheta}(C-2t)
=\frac{4\vartheta-16}
{\vartheta(2-\vartheta)(5\vartheta-4)}<0.
\]

This is a method-specific obstruction valid for every ϑ in the target range. Weakening H to K>C creates a real loss budget, but it does not turn the problem into an ordinary linear sieve.

## 3. Complete exact Buchstab backbone

For this section adopt the standard convention

\[
S_d(v)=\sum_{r\ge1}\mathbf1_{\mathcal A}(dr)
                \mathbf1\{P^-(r)\ge v\},\qquad P^-(1)=\infty.
\]

Thus primes **below** v are excluded. Changing the root from ≥N^ϑ to >N^ϑ can affect only multiples of a single boundary prime, at most O(N^(1−ϑ)+1)=o(u); it does not affect the target constant. The finite identities below keep their convention exactly and do not call that difference O(1).

Choose w=N^b, 0<b<ϑ, and z=N^ϑ. Define

\[
A_0=S_1(w),\qquad
A_j=\sum_{w\le p_j<\cdots<p_1<z} S_{p_1\cdots p_j}(w),
\]

and, for j≥1,

\[
R_j=\sum_{w\le p_j<\cdots<p_1<z} S_{p_1\cdots p_j}(p_j).
\]

Buchstab's identity gives S_1(z)=A_0−R_1 and R_j=A_j−R_(j+1). Therefore, for every truncation depth r≥0,

\[
\boxed{\displaystyle
S_1(z)=\sum_{j=0}^{r}(-1)^j A_j+(-1)^{r+1}R_{r+1}.}
\]

Every R_j is nonnegative. An odd truncation gives a lower bound; an even truncation gives an upper bound. A lower-bound algorithm may discard an uncovered **positive** contribution. It must estimate or expand an uncovered negative contribution.

For the starter choice b=1/4, a product of nine primes ≥w is ≥N^(9/4), exceeding the interval's upper endpoint for large N. Hence R_9=0 and the expansion through r=8 is exact. The generic ordered-prime regions through that depth are recorded in `region_inventory.json`. Prime powers are retained in the residual r, and r=1 is retained; neither is silently discarded.

This is a complete algebraic decomposition. Choosing which branches to expand, which factors to group, and where to use an analytic estimate is the subsequent Harman design problem, not something that follows merely from this identity.

The finite checker verifies the identity at every depth and the alternating bounds in 25 intervals, including square-centered intervals, prime powers, and the residual unit.

## 4. The first Type I calculation

At b=1/4, the lower linear sieve for A_0=S(𝒜,w), at level N^(1−ε), tends to the constant

\[
K_0=\frac{2e^{-\gamma_0}}{b}f(1/b)=4\log3.
\]

For a prime p=N^t, b≤t≤ϑ<1, the cofactor interval has length about N/p. Sieve it at level N^(1−t−ε). If this level is below w, reduce the upper sieve cutoff to that level. Since (1−t)/b≤3 over this range, the upper linear-sieve formula gives the asymptotic bound

\[
S_p(w)\le(2+o(1))\frac{N}{p(1-t)\log N}.
\]

Prime summation consequently bounds A_1/u by

\[
4\int_b^\vartheta\frac{dt}{t(1-t)}
=4\log\frac{3\vartheta}{1-\vartheta}.
\]

The remainders are admissible after dyadic subdivision: a prime block of exponent t has O(N^t) outer variables and level N^(1−t−ε), giving O(N^(1−ε)) before harmless logarithmic factors. All parameters stay a fixed distance from t=1 because ϑ is fixed.

Dropping the positive R_2 in the exact two-step identity therefore gives

\[
K_{\mathrm{raw}}=4\log3-4\log\frac{3\vartheta}{1-\vartheta}
=4\log\frac{1-\vartheta}{\vartheta}<0.
\]

Combining this with nonnegativity leaves only K=0. This proves the failure of this particular one-step Type I design. It does not prove the failure of every possible adaptive decomposition.

## 5. A necessary correction to the Type II interface

The supplied paper describes a schematic bilinear expression with general bounded coefficients and an unspecified “expected” term. Before optimizing any region, that expected term and the coefficient class must be fixed.

A natural-looking formulation would compare the short interval with a broad reference:

\[
a_\ell=\mathbf1_{\mathcal A}(\ell),\qquad
b_\ell=\frac{Y}{x}\mathbf1_{[x,2x]}(\ell),\qquad Y=N+1,
\]

and ask for

\[
\sum_{m\sim M}\sum_{k\sim K}\alpha_m\beta_k(a_{mk}-b_{mk})=o(Y)
\]

uniformly for all |α_m|,|β_k|≤1. That formulation is false, including ranges with M well below N. This is a statement about this specified comparator; it is not a refutation of every possible Type II formulation or of H(ϑ).

### Proposition: a short-interval resonance

Fix 0<μ<1, take M=⌊N^μ⌋, K≈x/(2M), and restrict m to [5M/4,7M/4] and k to (K,2K]. Let

\[
\tau=\frac{x}{10Y},\qquad
\alpha_m=m^{i\tau}\mathbf1_{[5M/4,7M/4]}(m),\qquad
\beta_k=(k/x)^{i\tau}.
\]

Then the short-interval bilinear sum has real part ≫Y, while the broad-reference sum is O(1). Hence their discrepancy is ≫Y.

**Proof.** For an interior m, every k with mk∈𝒜 lies in the chosen k range for large N. The number of these pairs is

\[
\sum_{5M/4\le m\le7M/4}\left(\frac{Y}{m}+O(1)\right)
=Y\log(7/5)+O(M+Y/M)\asymp Y.
\]

On the short interval,

\[
\alpha_m\beta_k=\exp\bigl(i\tau\log(mk/x)\bigr),
\qquad |\tau\log(mk/x)|\le1/10
\]

for large N. The real part is therefore positive and bounded below by a fixed proportion of the pair count.

For the broad sum, fix m. The remaining k range is an interval inside (K,2K], and the phase τlog k has monotone derivative τ/k. Here τ/k≈M/Y→0, so the first-derivative/Kuzmin–Landau bound yields O(K/τ), uniformly in the truncated interval. Summing absolutely over O(M) values of m and multiplying by Y/x gives

\[
O\left(\frac{Y}{x}\frac{MK}{\tau}\right)
=O(Y/\tau)=O(Y^2/x)=O(1).
\]

The discrepancy is thus ≫Y. ∎

The finite demonstration in the code gives discrepancies around 0.34Y as N grows from 200 to 2000; the proof, rather than those examples, establishes the obstruction.

This rules out importing a general prime-producing sieve framework with a broad uniform comparator unchanged into the interval problem. Ford–Maynard's framework explicitly assumes its Type I/II inputs; it does not provide those interval estimates. A short-interval campaign should instead specify the structured prime-factor coefficients actually produced by its decomposition, or another suitable comparison with all hypotheses proved. In particular, oscillatory twists cannot be included in a purported “prime-factored” coefficient class without checking that they preserve the required bounds.

## 6. First literature check and a limited endpoint certificate

The tool registry distinguishes the frozen tail engine, valid Type I bounds, candidate structured Dirichlet-polynomial inputs, and statements not yet applicable to the lower-bound problem.

As one concrete candidate, the displayed balanced criterion in Runbo Li's arXiv:2308.04458v8, Lemma 4.1, requires

\[
|\alpha_1-\alpha_2|<2\lambda-1,
\]

where the interval length is x^λ and the α's are exponents relative to x. At the formal endpoint λ=1/2, this would require a nonnegative number to be strictly negative. The source theorem is not being applied outside its stated setting: this is a certificate that **retaining this particular inequality unchanged cannot reach the endpoint**. It does not exclude different criteria, other grouping patterns, or refinements of the underlying mean-value argument.

The short-interval presentation also illustrates why “prime-factored” and “decomposable” polynomial classes must be recorded, rather than replaced by arbitrary coefficients. Its claimed improved prime-gap result is not assumed as an independently certified theorem here.

Pliego's 2024 monomial-sum result was also inspected. Its displayed corollary has a special weight, a non-box domain, and phase/sign restrictions; it is not a drop-in replacement for the arbitrary-coefficient reciprocal-phase engine. It remains a separate applicability investigation.

No complete inventory of existing analytic tools or global minimal obstruction certificate has yet been obtained. It is too early to decide that new mathematical machinery is necessary.

## 7. Milestone status and the next gate

| Supplied milestone | Checkpoint status |
|---|---|
| 1. Freeze C(ϑ) | Files frozen; arithmetic reproduced; independent source audit partial |
| 2. Set K>C | Complete, with an explicit loss budget and linear-sieve obstruction |
| 3. Complete Buchstab/Harman decomposition | Exact algebraic backbone complete; adaptive analytic design pending |
| 4. Explicit Type I/II inventory | Starter domains and Type I conditions written; estimate-specific Type II cells pending |
| 5. Encode available tools and optimize mass | Initial Type I calculation complete; full registry and optimizer pending |
| 6. Minimal obstruction if unsuccessful | Two limited obstructions proved; neither is a universal certificate |
| 7. Existing refinement or new theorem? | Deferred until the estimate-specific mass calculation exists |

The next task is concrete: select a signed Buchstab frontier, retain the exact structured coefficient class, and formulate an interval estimate for it with a specified main term, uniformity, and error o(u) after all blocks are summed. Translate the valid estimate into strict exponent inequalities, then measure the positive mass it rescues. For the working target ϑ=0.97 the final certified mass must exceed 0.512207285u.

A successful future calculation must report the grouped variables, cutoff, source theorem, coefficient restrictions, error budget, sign, and mass integral for every admitted region. An unsuccessful calculation must identify the uncovered cells that prevent that inequality, with its toolkit stated. Numerical integrals will require reliable upper/lower enclosures before they become a certificate.

## Primary sources consulted

1. O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, J. reine angew. Math. 591 (2006), 1–20, Theorem 1. [Authors' PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf).
2. K. Ford and J. Maynard, *On the theory of prime producing sieves*, arXiv:2407.14368. [arXiv record](https://arxiv.org/abs/2407.14368); [HTML](https://arxiv.org/html/2407.14368v1). Consulted for the exact input interface, not for a proved interval estimate.
3. R. Li, *The number of primes in short intervals and numerical calculations for Harman's sieve*, arXiv:2308.04458v8, §§2–4, especially Lemma 4.1. [Versioned HTML](https://arxiv.org/html/2308.04458v8). Candidate structured sieve machinery; endpoint extension not assumed.
4. J. Pliego, *Estimates for a three-dimensional exponential sum with monomials*, J. Théor. Nombres Bordeaux 36 (2024), 725–766, Corollary 1.1. [Publisher PDF](https://www.numdam.org/item/10.5802/jtnb.1294.pdf).
5. H. Iwaniec, *A new form of the error term in the linear sieve*, Acta Arith. 37 (1980), 307–320. [Publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/37/0/102638/a-new-form-of-the-error-term-in-the-linear-sieve). Metadata checked; full-text audit pending.
6. E. Fouvry and H. Iwaniec, *Exponential sums with monomials*, J. Number Theory 33 (1989), 311–333. [Publisher record](https://www.sciencedirect.com/science/article/pii/0022314X8990067X). Full-text audit pending.

The supplied paper, companion constraint inventory, exact script, and milestone image are the authoritative project baseline for this checkpoint.
