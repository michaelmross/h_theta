# H(ϑ) campaign — original-source audit, checkpoint 5

Michael M. Ross's square-root interval project. 5 October 2026.

The uploaded originals verify the bilinear remainder statement used in the campaign and supply an early explicit formulation with fixed well-factorable weights. They also identify a citation distinction that matters for choosing different factorizations on different blocks. The numerical ledger is unchanged: the certified prime lower coefficient is still K=0, H(ϑ) remains unproved, and the sufficient frontier targets 3.73u and 3.58u remain research targets.

The Fouvry–Iwaniec attachment is their **1983 progression paper**, rather than the **1989 monomial-sum paper** cited in the submitted tail proof. The latter's Lemma 9 and Theorem 6 are still awaiting primary-text verification. Thus this checkpoint closes the relevant original sieve-statement checks, not the entire original tail citation chain.

## 1. Source identification and audit scope

| Archived file | Original article | Printed pages | Relevant locations checked on page images |
|---|---|---|---|
| `sources/aa37127.pdf` | H. Iwaniec, *A new form of the error term in the linear sieve*, Acta Arith. **37** (1980) | 307–320 | Conditions (1)–(2), p. 308; Theorem 1, p. 309; factor-partition Lemma 1 and surrounding discussion, pp. 312–313 |
| `sources/aa36210.pdf` | H. Iwaniec, *Rosser's sieve*, Acta Arith. **36** (1980) | 171–202 | Theorem 1 and its absolute remainder, p. 172 |
| `sources/aa4226.pdf` | E. Fouvry and H. Iwaniec, *Primes in arithmetic progressions*, Acta Arith. **42** (1983) | 197–218 | Well-factorability, main theorem, and sieve remainder (1.2)–(1.3), p. 199; Proposition 1 and (A1)–(A2), p. 203; Proposition 2 and (A3), p. 213; block-dependent factor choice, p. 216 |

These PDFs contain scanned two-page spreads. Printed page numbers are the references above. For example, Iwaniec p. 309 is PDF page 2, right half; Fouvry–Iwaniec p. 199 is also PDF page 2, right half. OCR was used to navigate; the mathematical statements listed above were checked against the images. This is an audit of the campaign's relevant source interfaces, not a claim to have independently reproved every argument in all three articles.

The archived PDFs are byte-identical copies of the supplied files. Their hashes and the locations audited are recorded in `results/original_source_audit.json`. The original campaign paper, code, milestone image, previous four notes, and numerical results are preserved.

## 2. Iwaniec's bilinear remainder: what Theorem 1 says

Use M and M′ for the source's two factor capacities, to avoid confusing its letter N with the campaign parameter. On printed p. 309 the hypotheses include

\[
0<\varepsilon<1/3,\qquad M>1,\quad M'>1,\quad
D=MM',\qquad 2\le z\le D^{1/2},\quad
s=\frac{\log D}{\log z}\ge2.
\]

The upper and lower bounds have the form

\[
S(\mathcal A,z)\le XV(z)[F(s)+E]+R^+,
\qquad
S(\mathcal A,z)\ge XV(z)[f(s)-E]-R^-.
\]

For fixed ε and the fixed dimension-one sieve constants, the stated error is ε plus a quantity tending to zero with D. The remainders are finite sums of signed bilinear forms:

\[
R^\nu=
\sum_{\ell<\exp(8\varepsilon^{-3})}
\sum_{\substack{m<M\\m\mid P(z)}}
\sum_{\substack{n<M'\\n\mid P(z)}}
a^\nu_{m,\ell}(M,M',\varepsilon)
b^\nu_{n,\ell}(M,M',\varepsilon)
r(\mathcal A,mn),
\qquad |a|,|b|\le1.
\]

The theorem also says that the inequalities remain valid when the additional condition mn∣P(z) is imposed. This point matters: m∣P(z) and n∣P(z) separately allow a common prime, whereas mn∣P(z) excludes it. The campaign keeps the combined squarefree support.

This statement supplies **signed remainders**, not a bound by the sum of the absolute values of individual divisor errors. Estimating each signed bilinear form in absolute value is legitimate; replacing it at the outset by the unrestricted absolute divisor sum discards the cancellation the theorem is designed to retain.

### Density and sifting range in the campaign

For the interval/cofactor counts the divisor density is g(d)=1/d, corresponding to the source convention ω(pᵅ)=1. Condition (1), printed p. 308, is the dimension-one Mertens product condition. Condition (2) concerns prime powers of exponent at least two; here

\[
\sum_{p\ge w}\sum_{\alpha\ge2}\frac1{p^\alpha}
=\sum_{p\ge w}\frac1{p(p-1)}
\le\frac1{\lceil w\rceil-1}.
\]

The inequality follows by enlarging to all integers and telescoping, and is stronger than the required O(1/log(3w)) bound. Fixed sieve constants therefore suffice. These density checks do not estimate the campaign's aggregate interval remainders; that is the separate analytic task in checkpoint 4.

The relevant sieve parameters lie in the source's s≥2 range. The limiting root parameter is s=5, the tail upper sieve uses s=2, and the positive restoration uses s>2. Boundary values of the derived exponent regions are only limiting parameters: every actual power-saving application must retain fixed positive slack.

For fixed ε the source error is not o(1). To approach the displayed limiting sieve constants, first establish the estimates for fixed parameters, then make the sieve tolerance and level loss small enough for the desired strict numerical margin. At κ=.95 the margin associated with the hypothetical 3.73u bound allows this. No endpoint power saving is being inferred from the limiting constants.

### Factor capacities near exponent zero

The source requires both factor capacities to exceed 1. A factor of campaign exponent zero may have a fixed capacity such as 2, with the complementary capacity D/2. Its exponent differs from zero by O(1/log N), which is covered by a fixed interior margin. No application needs to assert that Theorem 1 literally permits capacity 1.

Lemma 1 on p. 312 partitions the admissible prime-box products into factors under prescribed capacities. The subsequent construction includes auxiliary parameter enlargement and reparametrization. These support retaining fixed losses in applications. A statement that the support products can be partitioned is weaker than a convolution identity for their coefficients; support factorization alone does not justify well-factorability of arbitrary weights.

## 3. Fixed weights and adaptive factorizations

Theorem 1 on p. 309 explicitly writes its coefficients as functions of M, M′ and ε. Its bare statement therefore gives

\[
\text{for every prescribed split, there exist suitable bilinear coefficients}.
\]

That statement alone does not establish the stronger quantifier order needed for changing splits after decomposing a single remainder:

\[
\text{there exist fixed sieve weights which admit a representation for every split}.
\]

The latter formulation is explicitly recorded in Fouvry–Iwaniec (1983), printed p. 199. They define a **fixed** arithmetic function λ of level D to be well-factorable when, for every D=D₁D₂, it has a convolution representation λ=μ∗ν with factors of the corresponding levels and fixed finite divisor orders. On the same page, formulas (1.2)–(1.3) give upper and lower linear-sieve remainders as a finite sum

\[
R^\pm(\mathcal A,D)
=\sum_{j<J_\varepsilon}\sum_{d\mid P(z)}
\lambda_j^\pm(d)\,r(\mathcal A,d),
\]

where λⱼ± are well-factorable of level D and order 2; the attribution is to Iwaniec's 1980 paper. Printed p. 216 further illustrates choosing the factor capacities according to a previously fixed bilinear block, using the well-factorability of the fixed λ.

Checkpoint 4 already used a modern explicit formulation: Lichtman, arXiv:2109.02851v2, Definition 2.1 and Theorem 2.10. The original 1983 statement now corroborates this interface. The original order-two formulation can also be used with fixed divisor losses absorbed by the strict power margins. It should not be silently relabeled as an order-one assertion from the 1983 text.

### Citation correction for the submitted slice proof

In `baseline/one-hypothesis.tex`, the paragraph following the slice proposition says that the weights are fixed once for all and that Iwaniec's theorem supplies every factorization simultaneously. The fixed-weight conclusion is supported by the explicit well-factorable formulation; the bare statement of Theorem 1 on p. 309 does not state those quantifiers. A suitable replacement paragraph is:

> Use the fixed well-factorable sieve remainder formulation recorded in Fouvry–Iwaniec (1983), p. 199, (1.2)–(1.3), attributed there to Iwaniec (1980); equivalently use the explicit modern formulation. For each fixed sieve tolerance, the remainder is a finite sum of linear functionals of fixed well-factorable weights of full level D. Decompose each functional into its outer, identity, product-size and frequency blocks. On a fixed block choose a convolution representation appropriate to its largest retained frequency. Its factors have bounded or fixed-divisor-order coefficients, and the latter losses are absorbed by the strict analytic margins. The same representation is used for all lower frequencies and for the absolute boundary envelope of that block. Summing these bounds controls the original fixed remainder.

This is a proposed citation and formulation amendment, not an edit to the frozen paper. It does not complete the still-pending original monomial-sum reduction.

### Smaller moduli and exact support remain separate obligations

Well-factorability is at the **full level D=Nᵝ**. It does not assert that the restriction of λ to an actual modulus box e≈Nᵝ′ is well-factorable at that smaller size. If Δ=β−β′ and the selected second factor has capacity Nˢ, its actual exponent lies in

\[
\max(0,s-\Delta)\le s'\le s.
\]

The capacity choice must control that whole interval. The earlier smaller-modulus proof and frequency margins remain necessary.

Similarly, the full support e∣P(z) is retained by the completely multiplicative prime cutoff and the identity

\[
\mu^2(e_1e_2)=\mu^2(e_1)\mu^2(e_2)
\sum_{q\mid e_1,\ q\mid e_2}\mu(q).
\]

After writing e₁=qa and e₂=qb, checkpoint 4 obtains the summable relative q powers −5/4, −7/4, −3/2 and −2 in the Robert–Sargos terms. The source audit confirms that this combined support cannot simply be omitted. It does not replace that derivation with a claim of unrestricted coefficient freedom.

## 4. What Rosser's sieve adds

Theorem 1 in *Rosser's sieve*, printed p. 172, gives one-sided main terms with a remainder bounded by

\[
\sum_{\substack{d\le y\\d\mid P(z)}}|R(\mathcal A,d)|.
\]

This is the ordinary absolute-remainder interface. For the campaign's individual interval errors bounded by 1, it gives the familiar Type I use of total divisor level below N with fixed loss. It supplies no automatic extension to level N^(5/4), no terminal prime comparison, and no replacement for the signed bilinear remainder theorem. The two Iwaniec papers serve different interfaces and should be cited accordingly.

## 5. The 1983 progression theorem: precise scope

The main theorem on printed p. 199 concerns a fixed nonzero integer a, a fixed finite-order well-factorable weight λ of level

\[
Q=x^{9/17-\varepsilon},
\]

and gives, for each fixed A>0,

\[
\sum_{(q,a)=1}\lambda(q)
\left(\pi(x;q,a)-\frac{\operatorname{li}(x)}{\varphi(q)}\right)
\ll_{a,\varepsilon,A,\kappa}\frac{x}{(\log x)^A}.
\]

At x=N² the modulus exponent is 18/17−2ε relative to N. This conversion is a source parameter conversion, not an admitted campaign sieve level.

Subtracting two endpoint estimates of this strength yields an error bounded only on the x scale. For the campaign normalization u≈√x/log x,

\[
\frac{x/(\log x)^A}{u}
\asymp\frac{\sqrt{x}}{(\log x)^{A-1}}\longrightarrow\infty
\quad\text{for each fixed }A.
\]

Thus this theorem alone does not give the required o(u) short-interval error. Its implied constants depend on the fixed residue a; the condition (q,a)=1 also differs from the zero-residue divisibility counts in the cofactor remainders. A valid application needs an explicit transformation with all resulting conditions verified.

The paper contains more specialized bilinear propositions; their hypotheses must also be retained:

| Result | Source conditions, using its variables | Coefficient requirement |
|---|---|---|
| Proposition 1, p. 203 | MN≤x; xᵋ<N≤x^(1/3); Q≤x^(−ε)N; R≤min(x^(1/2−ε)N^(−3/4), x^(5/8−ε)N^(−11/8)) | (A1): fixed divisor-order bounds; (A2): a uniform Siegel–Walfisz condition for the n-sequence |
| Proposition 2, p. 213 | MN≤x; x^(1/4)<N≤x; Q≤x^(−ε)N; R≤(x/N)^(1/3) | (A1) and (A3): the n-sequence is the indicator of an interval contained in (N,2N] |

Their bilinear form concerns mn≡a mod qr with (qr,a)=1 and a 1/φ(qr) main term. Proposition 1 yields logarithmic saving on the x scale; Proposition 2 yields x^(1−η) for some η(ε)>0 under its more restrictive interval-sequence hypothesis. The latter is a potential ingredient for a future reduction. It is not rejected simply because the main theorem has logarithmic error. However, the campaign's terminal prime or rough-cofactor indicators are not (A3), and no reduction matching these coefficient, residue, length and error conditions has been supplied here.

The modular-inverse exponential sums appearing in this progression argument are also not automatically interchangeable with the ordinary reciprocal-monomial phase in the campaign. Neither the progression theorem nor its auxiliary bounds have been credited as a new H(ϑ) input.

## 6. Updated admission and proof status

| Item | Status after reading the originals |
|---|---|
| Iwaniec's prescribed-split bilinear remainder and s≥2 range | Verified against the 1980 original |
| Fixed well-factorable weights permitting blockwise split choices | Explicitly corroborated by the 1983 original; modern formulation already used in checkpoint 4 |
| Density 1/d and prime-power condition | Checked for the campaign's nonnegative sifted sequences |
| Ordinary absolute Type I remainder | Verified against *Rosser's sieve* |
| Checkpoint 4 sharp transfer, smaller-modulus coverage, gcd expansion and higher cofactor levels | Earlier derived inputs; their proofs remain in `NEGATIVE_FRONTIER_NOTE.md` |
| Submitted 1989 Lemma 9/Theorem 6 pipeline and extra grouping inventory | Primary-text audit still pending; the uploaded 1983 article is a different paper |
| New use of the 1983 progression estimates in the actual short interval | Pending an explicit reduction; no mass admitted |
| Terminal prime comparison or R_.95≤(3.73+o(1))u | Unproved |
| H(ϑ), a positive K, or a universal impossibility theorem | None proved |

The limiting root enclosure remains

\[
4.48376376795409<L_0<4.48379276301814,
\qquad
4.49945032531085<U_0<4.49953612965391.
\]

The independently derived smaller-prime tail remains

\[
C_{\rm small}(\vartheta)=\frac{16}{5}\log\frac{5-4\vartheta}{\vartheta}.
\]

At κ=.95 an upper bound R_.95≤(3.73+o(1))u would give a prime coefficient exceeding .0061962 after the smaller-prime tail subtraction. With the frozen tail benchmark, the sufficient target is 3.58u. These are unchanged conditional implications. The available whole-frontier cap still fails to give a positive lower bound. The original parity witness remains a limitation of the extracted mass interface, not an impossibility theorem about the actual interval or stronger arithmetic estimates.

## 7. Reproduction and next proof gate

Run `python3 src/source_audit.py` from the campaign directory. It checks the archived original hashes, frozen baseline hashes, unchanged numerical ledger hash, rational parameter conversions and stated conditional ledger margins; it writes the audit metadata and restores the campaign state to checkpoint 5. It does not verify printed theorem statements by computation or prove the analytic reductions. The page-image reading is the evidence for those statements.

The next source check is the actual 1989 *Exponential sums with monomials*. The next arithmetic proof gate remains an estimate for the actual structured short-interval sequence that improves the negative frontier or establishes a usable terminal prime comparison. The 1983 article adds a well-factorability citation and candidate tools with explicit constraints; it supplies neither missing estimate without further work.
