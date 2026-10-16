# H(ϑ) campaign — Fouvry–Iwaniec 1989, checkpoint 6

Michael M. Ross's square-root interval project. 5 October 2026.

The uploaded *Exponential sums with monomials*, J. Number Theory **33** (1989), 311–333, supplies the previously missing original. Lemma 9, Theorem 6 and Theorem 7 have now been checked against the page images. The Theorem 6 formula and its exponent caps in the companion inventory agree with the original. The continuous balanced-block obstruction also confirms that adjoining this bound does not improve the submitted tail level profile.

There is a further useful consequence for the campaign: **arbitrary bounded outer coefficients** at exponent γ<1 admit cofactor level β<5/4−γ, with fixed positive margins and well-factorable modulus weights. This removes the earlier extra condition 2γ+β<2 for that coefficient family. The proof below retains the full-level factorization, smaller actual moduli, combined squarefree support, and sharp interval error. At γ=1 the arbitrary-coefficient extension is not claimed; the earlier untwisted-prime endpoint remains a separate result.

The numerical ledger is unchanged. The root, actual-prime tail and first positive restoration already had their relevant levels. This extension therefore earns no additional positive prime mass in this checkpoint. K=0; H(ϑ), the terminal prime comparison and R_.95≤(3.73+o(1))u remain unproved.

## 1. Original statements and notation

The source has 23 individual PDF pages, with printed page 311 on PDF page 1. Relevant locations are:

| Statement | Printed pages | PDF pages |
|---|---|---|
| Definition of the special monomial sum | 324 | 14 |
| Theorem 6 | 325 | 15 |
| Divisor remainder and Lemma 9 | 330–331 | 20–21 |
| Theorem 7 and conditions (7.4)–(7.6) | 331 | 21 |
| Auxiliary conditions and corollary | 332 | 22 |

Text extraction was used for navigation; the equations and restrictions above were read on the rendered pages. The archived `sources/fi1989_monomials.pdf` is byte-identical to the upload. The script records its hash. This audit concerns the cited interfaces and their campaign applications, not all the paper's results or proofs.

Below N is always the campaign parameter, x=N², Y=N+1, and u=N/(2 log N). Source coefficient lengths are renamed A and B, and its normalized phase parameter is renamed X. This avoids confusing the source's N or x with the campaign's parameters.

## 2. Lemma 9: the exact transfer interface

For the source interval (x−y,x], printed p. 330 defines

\[
r_d=\lfloor x/d\rfloor-\lfloor(x-y)/d\rfloor-y/d,
\qquad
R(A,B)=\sum_{m<A}\sum_{n<B}a_mb_n r_{mn}.
\]

The associated exponential sum includes the reciprocal weight:

\[
S_t(H,A,B)=\sum_{1\le h\le H}\sum_{m<A}\sum_{n<B}
\frac{a_mb_n}{mn}\,e\!\left(\frac{ht}{mn}\right).
\]

Lemma 9 gives, for separately bounded coefficients and H=AB y^(−1)x^(3ε),

\[
|R(A,B)|\le
2\int_{x-2y}^{x+y}|S_t(H,A,B)|\,dt+O_\varepsilon(yx^{-\varepsilon}).
\]

This confirms the phase, height and power-saving normalization in the submitted pipeline. However, its three separate factors e₁,e₂,p are an extension of the source's two coefficient slots. Collapsing a product introduces a fixed divisor-order coefficient, which needs a small loss; it is not literally an application with both collapsed coefficients bounded by 1.

For the actual interval J, take the integer points of the real interval

\[
[N^2-N/2-1/2,\ N^2+N/2+1/2],
\]

whose length is exactly Y. This avoids an integer-endpoint ambiguity while preserving the zero-frequency term Y/d. A smooth cutoff at width δ=Yx^(−2ε) changes the factorized weighted count by at most

\[
O\bigl((\delta+1)x^\nu\bigr)=O(Yx^{-\varepsilon})
\]

for sufficiently small fixed ν relative to ε. To see this, a boundary integer has at most a fixed divisor function's number of representations as the product of the inner integer and the outer factors. The absolute values of all separated coefficients have the same divisor bound. Since Y≈x^(1/2), choose ε small enough that δ tends to infinity. Signed coefficients do not invalidate this absolute boundary estimate.

Poisson summation gives the zero frequency and the integral of the weighted exponential sum above. Reciprocal weights can be removed by partial summation on positive dyadic boxes, using uniform bounds for rectangular partial sums. The Fourier tail is negligible beyond a fixed multiple of (Q/Y)x^(3ε), where Q is the denominator product scale, by taking sufficiently many derivatives. These are the precise reasons the raw block target is a saving relative to Q, rather than relative to HQ.

The earlier pipeline proof's assertion that the Fourier weights are monotone is unnecessary and should be removed: Fourier transforms need not be monotone. The raw lemma should also state uniformity for rectangular partial sums, or uniformity over the bounded separated coefficient families, rather than only one full sum for one coefficient choice. The actual exponential engines have this uniformity, since a partial interval can be imposed in its separate coefficient slot. Use the integral form of Lemma 9, or the signed transfer already proved in `NEGATIVE_FRONTIER_NOTE.md`, Section 3. For complex coefficient families, handle both frequency signs, or use closure under conjugation; the source's initial remainder discussion uses real coefficients. The admitted estimates are uniform over the separated coefficient families and their conjugates, so this costs only a constant.

## 3. Theorem 6 and all six exponent terms

On pp. 324–325 the sum is

\[
S_{\chi\varphi\psi}(H,A,B)=
\sum_{h\sim H}\sum_{m\sim A}\sum_{n\sim B}
\chi(h)\varphi_m\psi_n
e\!\left(X\frac{h n^{-1}m^\alpha}{H B^{-1}A^\alpha}\right).
\]

The hypotheses are α≠0,1; H,A,B,X≥1; |φₘ|,|ψₙ|≤1; and **χ(h)=e(ζh), an additive character**. The bound is

\[
\begin{aligned}
|S|\ll_\alpha( HAB)^{1/2}\Big[&(H+B)^{1/2}
\big(X^{1/8}H^{-1/6}A^{1/12}B^{1/6}
+X^{1/8}H^{-1/8}B^{3/8}\\
&\qquad+B^{1/2}+B^{1/4}A^{1/8}\big)X^{1/8}
+A^{1/2}+X^{-1/4}A^{1/2}B\Big](\log(2HABX))^4.
\end{aligned}
\]

The companion's formula matches this statement. In the campaign α=−1 and X≈HN²/Q; hence α is admissible and X>1 in the relevant regions. The two denominator coefficient slots are separate. The theorem does not allow an arbitrary joint coefficient a(h,n). Interval completion in h is permitted: the source is uniform in the additive character, and Fourier completion of an interval has logarithmic cost. Smooth Mellin twists in h can instead be removed by partial summation with a small loss. This is enough for the specific separated weights in the sharp transfer; it is not arbitrary frequency-coefficient freedom.

Let Q≈N^Σ′, H≈N^η, A≈N^m₀, B≈N^n₀, m₀+n₀=Σ′, and ξ=η+2−Σ′. To bound S by N^(Σ′−c), the A^(1/2) term requires n₀>η. Then H+B≈B and the other five terms give the following **closed limiting caps**; actual estimates require strict margins.

| Term | Necessary limiting inequality |
|---|---|
| T1 | 7n₀≤8Σ′−7η−6 |
| T2 | 7n₀≤6Σ′−5η−4 |
| T3 | 8n₀≤5Σ′−5η−2 |
| T4 | 5n₀≤4Σ′−5η−2 |
| T5 | n₀≥η |
| T6 | 2n₀≤2−Σ′−η |

Write Cⱼ for each upper cap. For η≤Σ′−1 and Σ′≤4/3, C₂≤C₁,C₃,C₄. Thus the effective window is

\[
\eta\le n_0\le
\min\left(\frac{6\Sigma'-5\eta-4}{7},
\frac{2-\Sigma'-\eta}{2}\right).
\tag{1}
\]

This reproduces the companion's pruning. For a family with base a and added sieve factor exponent s, the correct existence condition is

\[
\max(a,\eta)\le\min(a+\beta',C_2,C_6).
\]

In particular, if the type-I base μ is below η, the chosen value is η, not μ. On the submitted facet region Σ′≤5/4, η≤Σ′−1, the condition η≤C₂,C₆ is automatic, so this clarification does not change its encoded optimum. Outside that region the pruned code contains relaxations and is not an unrestricted admission test. Full-level/smaller-modulus uncertainty must additionally be checked before using a chosen factor size.

### The submitted level cannot improve through Theorem 6

With μ=γ/2 and η=Σ−1, the possible B-slot exponents from splitting the sieve modulus have bases 0, γ/2, γ/2 and γ. The family with base 0 needs η≤β, which fails for γ>1. At γ=1, T6 for n₀≥η requires β≤1/4. Each middle family needs

\[
\gamma/2\le(3-2\Sigma)/2,
\quad\text{equivalently}\quad2\beta+3\gamma\le3,
\]

which fails for γ≥1 and β>0. The final family is still larger. Therefore Theorem 6 adds no admissible balanced top-frequency block beyond

\[
\beta=(6-5\gamma)/4,\qquad1\le\gamma<6/5.
\]

This is a continuous algebraic obstruction, not an extrapolation from the five numerical slices. Exchanging the two denominator slots is included: all subset/complement choices lie in those families. The result concerns this fixed decomposition and grouping toolkit, not all methods in the source or all possible prime decompositions.

## 4. Theorem 7: a restricted packaged bound

Printed p. 331 assumes 2≤y≤x^(1/2), and gives a power-saving dyadic bilinear remainder under

\[
A<yx^{-\varepsilon'},\qquad
B^6<Ay^7x^{-3-\varepsilon'},\qquad
A^2B^4<yx^{1-\varepsilon'},
\quad\varepsilon'=48\varepsilon.
\]

At y≈N and x≈N², its limiting exponents satisfy

\[
m_0<1,\qquad6n_0<m_0+1,\qquad2m_0+4n_0<3.
\]

Consequently both coefficient slots are below the interval scale; in fact the second has n₀<1/3. An undecomposed prime of exponent γ≥1 cannot occupy either slot. The submitted rejection of that direct application is confirmed.

For the literal campaign endpoints Y=N+1 is slightly larger than the square root of the upper endpoint. The packaged theorem's exact length hypothesis is therefore handled by splitting J into two adjacent subintervals of comparable length. This does not affect these exponent inequalities. The campaign's direct Poisson transfer does not require this packaged length restriction.

## 5. New remainder proposition: arbitrary bounded outer weights

**Proposition.** Fix 0≤γ<1 and β>0 with γ+β<5/4. Let c_d be arbitrary bounded coefficients on d≈N^γ, and let λ be a fixed well-factorable sequence of full level D=N^β with bounded or fixed divisor-order convolution factors. For the actual interval J, and with the exact e∣P(z) sifting support retained,

\[
\sum_{d\sim N^\gamma}c_d
\sum_{e\mid P(z)}\lambda(e)
\left(\sum_j1_J(dej)-\frac{Y}{de}\right)
=O(N^{1-c})
\tag{2}
\]

for some c>0 depending on the fixed exponent margins and divisor orders. The same estimate holds for the separated absolute-coefficient families required in the sharp transfer.

For γ≤3/4 this follows from checkpoint 4: γ+β<5/4 implies 2γ+β<2. For γ>3/4 the following Theorem 6 argument removes that second condition.

### Full-level factor choice and smaller actual moduli

Put Σ=γ+β, ρ=5/4−Σ>0. If Σ<1, the individual floor error and a divisor bound suffice. Suppose Σ≥1. Choose small fixed positive τ and ν, with

\[
\tau=\frac1{100}\min(1-\gamma,\rho,
\gamma-3/4+7\rho,1),\qquad\nu=\tau/10,
\]

or smaller values when absorbing additional fixed losses. Factor at the full capacities

\[
D_2=N^s,\qquad D_1=N^{\beta-s},\qquad
s=\Sigma-1+\tau.
\]

Both capacities exceed 1 for large N: s>0 and β−s=1−γ−τ>0. Put e₂ in the source B slot and collapse d e₁ into its A slot. The latter has a fixed divisor-order coefficient. Select this representation for a fixed outer and product block before estimating its frequencies and absolute boundary envelope.

For an actual modulus block e≈N^β′, let Δ=β−β′ and Σ′=γ+β′. The actual B-slot exponent lies in

\[
\max(0,s-\Delta)\le n_0\le s,
\]

up to harmless O(1/log N) box constants. Low blocks use the floor bound. On the remaining blocks the smoothing frequency range is η≤Σ′−1+ν, and Σ′≥1−ν. Hence

\[
n_0-\eta\ge\tau-\nu>0.
\]

The other caps hold throughout the whole actual factor interval, not at a freely selected factor size. Direct substitution gives

\[
\begin{aligned}
C_6-s&\ge2\rho+\Delta-\nu/2-\tau,\\
C_2-s&\ge\frac{8-6\Sigma-\Delta-5\nu-7\tau}{7}
\ge\frac{\gamma-3/4+7\rho-5\nu-7\tau}{7},\\
C_1-C_2&\ge-2\nu/7,\\
C_3-C_2&\ge1/32,\\
C_4-C_2&\ge(1-10\nu)/35.
\end{aligned}
\]

The chosen τ,ν make every required difference positive with fixed margins. This includes C₁ even after its possible −2ν/7 difference. Theorem 6 therefore gives a uniform saving relative to the denominator scale for the entire smoothing frequency range. At lower frequencies all inequalities improve. In particular, no truncated weight is being declared well-factorable at its smaller actual level.

### Exact squarefree support and the gcd expansion

First insert the completely multiplicative small-prime support into the separate factors. Then retain combined squarefreeness using

\[
\mu^2(e_1e_2)=\mu^2(e_1)\mu^2(e_2)
\sum_{q\mid e_1,\ q\mid e_2}\mu(q).
\]

Set e₁=qa, e₂=qb. The free lengths of both source denominator slots shrink by q; the original normalized phase size X stays the same. Apply the **full** Theorem 6 expression, rather than assuming H≤B/q in each gcd piece. Since H+B/q≤H+B, its six terms acquire at least the following relative powers:

| Term | Relative q power |
|---|---|
| T1 | −5/4 |
| T2 | −11/8 |
| T3 | −3/2 |
| T4 | −11/8 |
| T5 | −3/2 |
| T6 | −5/2 |

All are summable, including a sufficiently small fixed divisor loss. Thus the aggregate exponential saving holds with e∣P(z), even when the shortened B slot is smaller than H. The sharp transfer of checkpoint 4, Section 3, now applies to these separated families and their absolute boundary envelopes. It proves (2), including the signed smoothing discrepancy and frequency tail.

For a nonnegative outer family the well-factorable upper and lower sieve can therefore use

\[
B_{\rm arb,new}(\gamma)=5/4-\gamma,\qquad0\le\gamma<1,
\]

with a fixed loss. This includes arbitrary bounded weights supported on primes at any fixed exponent below 1. It does not include arbitrary unfactored modulus weights, arbitrary joint frequency/denominator coefficients, or the arbitrary-prime-weight endpoint γ=1.

## 6. Reconstructing the submitted tail route

The relevant original source statements are now all available. A valid independent reconstruction combines the submitted Vaughan coverage inequalities with the explicit fixed-weight formulation and the full-level/support/transfer details from the campaign.

Fix 1≤γ<6/5 and β<(6−5γ)/4 with fixed margins. Prime powers from Vaughan's Λ weighting cost O(N^(β+γ/2+ε)), whose limiting exponent is at most 3/4. After smooth separation, the original type-I and type-II ranges apply. For an actual product exponent β′≤β, set Σ′=γ+β′. The RS window at the largest retained formal frequency is

\[
[2\Sigma'-2,\ 3-2\Sigma'].
\]

The submitted coverage proof, applied at β′, covers each Vaughan exponent by the elementary free-variable estimate or an RS family with base μ or γ−μ. Its overlap inequalities have fixed slack from β<(6−5γ)/4 and γ<6/5. For instance the type-II lower-capacity gap is at least

\[
2-5\gamma/3-\beta>0.
\]

The decisive overlaps are 5−4Σ′ and 6−5γ−4β′. Both have fixed positive lower bounds in the admitted compact range. Thus a sufficiently small fixed perturbation gives strict margins in each selected branch.

To implement a selected RS family at the **full level**, use the factor-capacity selection from checkpoint 4. When its Vaughan base a is below the desired lower edge l, choose s=l−a+Δ plus a sufficiently small fixed perturbation; when a is safely inside the window, a constant factor capacity suffices. The available length condition l−a≤β′ follows from the coverage inequalities with their margins. The whole smaller-modulus uncertainty fits because

\[
(5-4\Sigma')-\Delta
\ge5-4\gamma-4\beta
>0.
\]

In fact writing β=(6−5γ)/4−ρ makes the last lower bound γ−1+4ρ. The representation is chosen for the fixed Vaughan and product block at its largest retained frequency. It works for all lower frequencies, and the fixed margins absorb the small smoothing extension. Combined squarefree support has the summable RS gcd powers already proved in checkpoint 4; elementary pieces have q^(−2). The signed sharp transfer then gives the required o(u) aggregate error.

Applying the upper sieve at z=D^(1/2) and summing the nonnegative larger-prime slices reconstructs the original tail constant:

\[
4\int_1^{2-\vartheta}\frac{d\gamma}{\gamma((6-5\gamma)/4)}
=\frac83\log\frac{2-\vartheta}{5\vartheta-4},
\qquad4/5<\vartheta<1.
\]

Every analytic estimate is established first with fixed losses; these may then tend to zero after taking the limiting upper bound. This verifies the relevant original tail source route **with the explicit addenda just described**. It is not an endorsement of the frozen paper's brief monotonicity or signed-smoothing wording without those details. Neither the original manuscript nor its historical numerical files have been edited.

## 7. Effect on the signed campaign

| Family or quantity | Before this checkpoint | After this checkpoint |
|---|---|---|
| Arbitrary bounded outer d≈N^γ, γ<1 | β<min(5/4−γ,2−2γ) | β<5/4−γ |
| Arbitrary bounded prime weights, fixed γ<1 | Only the arbitrary-outer RS region | Full new arbitrary-outer region |
| Untwisted prime endpoint γ=1 | Earlier Vaughan/RS calibration | Unchanged; arbitrary weights not extended to this endpoint |
| Root level and actual-prime cofactor levels | Already at the relevant 5/4 profile | Unchanged |
| First positive R₂ restoration | t+3v<5/4, v≥1/4 | Unchanged: this already has t+v<3/4 |
| Original tail source chain | 1989 statements missing | Relevant statements checked; reconstructed route supplied with explicit addenda |
| Sufficient upper target R_.95 | 3.73u with smaller-prime tail; 3.58u with frozen tail | Unchanged and unproved |
| Certified K and H(ϑ) | K=0, H unproved | Unchanged |

The new coefficient range is useful for future upper estimates on grouped negative branches. It does not turn a freely counted inner integer into a terminal prime, and it supplies no new terminal-prime comparison. The existing long-carrier parity witness still matches the extracted o(u) divisor-mass interface through total level N^(5/4); the witness was already uniform against fixed divisor-order coefficients. Thus the broader mass interface alone does not force a prime. This remains a statement about that interface, not a universal impossibility claim about stronger arithmetic data.

## 8. Reproduction and next work

Run `python3 src/fi1989_audit.py` from the campaign directory. The script verifies source and preserved-input identities, derives all six exponent inequalities using exact rational arithmetic, compares the resulting pruned atoms with the frozen code, checks the continuous balanced-block exclusions symbolically, and checks rational examples of the new full-factor interval. The continuous proofs are above; examples do not prove uniform applicability. It also records that the numerical ledger and conditional prime margins are unchanged.

The next substantive gate is still parity-sensitive information for the actual short interval and structured coefficients. The newly admitted arbitrary-outer range can be used in a redesigned signed upper estimate, but that design must earn and enclose a smaller frontier cost before claiming a positive K. Other theorems in the 1989 paper and other decompositions remain possible further inventory work; no exhaustive optimality claim is made.
