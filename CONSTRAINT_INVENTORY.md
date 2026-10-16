# Constraint inventory through checkpoint 18

All campaign exponents are relative to **N**, unless a tool explicitly uses x=N². Inequalities that need a power saving are strict and must eventually receive a fixed ε margin. Equality at a facet is not an analytic saving.

This inventory describes the exact combinatorial regions and the first admitted estimates. It is not an exhaustive catalog of analytic number theory.

## A. Arithmetic domain

Take b=1/4 and ϑ=97/100 initially. A descending prime chain p₁>⋯>pⱼ has pᵢ≈N^(tᵢ), product d, and

\[
\sigma=t_1+\cdots+t_j.
\]

| Condition | Inequality | Status |
|---|---|---|
| Base cutoff | tⱼ≥b | Exact cutoff, up to dyadic-box endpoints |
| Upper cutoff | t₁<ϑ | Exact cutoff |
| Ordered primes | t₁≥t₂≥⋯≥tⱼ | Necessary exponent inequalities; actual primes remain distinct |
| Product can divide an element of 𝒜 | σ≤2 | Limiting exponent domain; retain exact arithmetic boundary |
| Residual cofactor is nonunit and c-rough | σ+c≤2 | Necessary limiting inequality |
| Such a residual is forced to be prime | σ+2c>2 | Sufficient with a fixed exponent margin |
| Residual cofactor is 1 | d∈𝒜 | Separate terminal stratum; do not drop by a dimension argument |

The rough cutoff c is b in a base term Aⱼ and tⱼ in the frontier Rⱼ. The sign of both at depth j is (−1)^j in the corresponding expansion. A positive frontier may be dropped for a lower bound. A negative frontier needs an upper bound or further expansion.

The exact arithmetic sum, rather than σ≤2 alone, determines all boundary cases. In particular, σ+c=2 may represent a prime residual, and a term with residual 1 is not represented by assigning it an arbitrary prime exponent.

For b=1/4 the exact expansion has depth at most eight for sufficiently large N: a ninth extracted prime would force d≥N^(9/4)>max 𝒜.

## B. Admitted Type I information

For fixed d, the residual interval has length Y/d+O(1), where Y=N+1. At product exponent σ<1, use a sieve level

\[
D_d=N^{1-\sigma-\varepsilon}.
\]

| Purpose | Inequality or parameter | What is credited |
|---|---|---|
| Aggregate interval remainders | Total divisor level <N | O(N^(1−ε)) after fixed-depth dyadic splitting |
| Upper bound for S_d(N^c) | σ<1; use cutoff min(N^c,D_d) | Linear upper sieve main term plus admissible error |
| Positive lower sieve main term | σ+2c<1 | f((1−σ)/c)>0, with margin |
| Lower bound when σ+2c≥1 | No positive f supplied | Only nonnegativity |
| Subpower base B=exp(√log N) | Supplied fundamental-lemma/remainder estimates | Available alternative starting point; dimension then grows with N |

For a base-term chain d, unique ordering of its distinct prime factors gives bounded outer weights. Any further divisor multiplicities are fixed-order divisor bounds and require ε slack. A full adaptive design must explicitly retain these bounds after regrouping.

The implemented first calculation uses A₀−A₁ and drops the positive R₂. At b=1/4 it yields

\[
K_{\rm raw}=4\log((1-\vartheta)/\vartheta),
\qquad K_{\rm certified}=\max(0,K_{\rm raw})=0
\]

on the target range. No later branch is credited with mass in that calculation.

## C. Frozen tail constraints: keep the two problems distinct

The existing tail uses exponents (γ,β,μ,η), total denominator exponent Σ=γ+β, and phase exponent ξ=η+2−Σ. They describe a **cofactor upper sieve**, not an estimate for every rough-count frontier above.

The Robert–Sargos engine in that specific reduction has standalone exponent m₁ and full pass conditions

\[
m_1>4\eta+2-2\Sigma,\qquad
m_1<\Sigma-3\eta,\qquad
m_1>2\eta,\qquad
\eta<2-\Sigma,
\]

with slack for coefficient losses. On its interior tail range these reduce to the familiar window between 2η and Σ−3η. The reachable grouping intervals depend on the **proved** coefficient representation; a fractional exponent chosen by an optimizer does not itself establish a factorization of the sieve weights.

The balanced witness is μ=γ/2, η=Σ−1. Its upper window edge produces 4β+5γ≤6. The new program checks the corresponding rational boundary values. It does not rerun an exhaustive continuous optimization over γ or complete the source audit of the bilinear remainder representation.

Admitting the same source theorem to a new lower-count term requires a new reduction with its own frequency range, denominator product, coefficient slots, and required error. Reusing the tail's atoms without that reduction would be unsound.

## D. Candidate structured Dirichlet-polynomial family

The displayed balanced criterion in Li, arXiv:2308.04458v8, Lemma 4.1, uses exponents relative to **x**, an interval exponent λ, and a prime-factored residual polynomial. Its balance condition is

\[
|\alpha_1-\alpha_2|<2\lambda-1.
\]

In N-exponents tᵢ=2αᵢ, it becomes |t₁−t₂|<4λ−2. The formal limit λ=1/2 has no admissible point because its right side is zero and the inequality is strict.

This is a limited failure certificate for that unchanged condition. The candidate source theorem is not applied at λ=1/2, and other source criteria are not ruled out. Its factorization and prime-factored hypotheses must remain explicit in any future translation.

## E. Rejected general comparison

For the specific broad reference bℓ=(Y/x)1_[x,2x](ℓ), uniform o(Y) comparison of bilinear sums for arbitrary bounded coefficients is impossible. The proof in the campaign note uses coefficients m^(iτ), (k/x)^(iτ), with τ≈x/Y. This obstruction occurs for every fixed shorter-factor N-exponent μ∈(0,1).

Reject that interface before region optimization. It says nothing against an estimate for the actual structured coefficients, or against another precisely defined comparison sequence.

## F. Admission record required for the next stage

Each future analytic tool must supply all the following fields:

| Field | Required content |
|---|---|
| Arithmetic term | Exact signed sum, including all cutoff and ordering conditions |
| Source | Version, theorem/lemma number, and primary-source URL |
| Exponent units | x or N, with explicit conversion |
| Coefficients | Actual bounds, product structure, and any prime-factored restrictions |
| Comparison/main term | Fully specified, including normalization |
| Quantifiers | Uniformity in center, ranges, frequencies, and coefficient choices |
| Error | Enough saving to give o(u) after all blocks and transformations |
| Region | Derived inequalities with strictness and ε margins |
| Mass | Correctly signed integral or another rigorous bound |
| Proof status | Admitted, pending a reduction, or rejected with reason |

Numerical quadrature can guide the design. A claimed K>C requires enclosures in the direction appropriate to each sign and an error budget covering boundaries and omitted blocks.

## G. Selected structured frontier (checkpoint 2)

The positive terminal subregion of R₂ has

\[
\tfrac14\le t_2\le t_1\le\vartheta,\qquad
t_1+3t_2>2,\qquad t_1+2t_2<2.
\]

On compact interior regions the p₂-rough residual is prime. The exact candidate count explicitly keeps a prime residual and all markings. Its model mass is

\[
M_D=2\iint_D\frac{dt_1dt_2}{t_1t_2(2-t_1-t_2)}.
\]

Its centered long-reference asymptotic follows from quantitative PNT. The required short-interval comparison, with untwisted prime indicators as coefficients, is still unproved. See `STRUCTURED_FRONTIER_NOTE.md`, equations (11)–(13). No short lower-bound mass is admitted.

Each prime has N-exponent >(2−ϑ)/3 and <1. For ϑ=.97, the residual x-exponent for any nonempty group of whole primes is >103/600. The balanced candidate requires that exponent to be <Γ_g(λ)≤4λ−2; therefore it covers none of this region at λ=1/2 or .525, under every permutation. The derived necessary condition λ>1303/2400 is a statement about that facet, not a sufficient theorem or a universal short-interval barrier.

The certified reference mass satisfies 0.572657<M<0.572699. Omitting it exceeds the .547810725088 planning loss budget in an otherwise fully matched reference design. This conditional bookkeeping fact does not certify an upper bound for the true K of another design.

## H. Negative semiprime band (checkpoint 3)

For 4/5<κ<ϑ<1, the negative first frontier sum over N^κ≤p<N^ϑ consists of semiprimes with p extracted as the smaller prime. The global frozen tail theorem bounds it by C(κ)u. Restricting the positive slice estimates in that theorem's proof to the larger-prime band gives the sharper [C(κ)−C(ϑ)]u bound. This is a reduction from the frozen slice estimates, whose original independent source audit remains partial; it is not subtraction of global upper bounds.

Combined with the low Type I upper bound, the rational split κ=877/1000 improves the provisional raw lower coefficient at ϑ=.97 from −13.9043947593 to −10.1997915846. It remains negative. The signed ledger shows that even full R₂ reference recovery would not close the old Type I design.

The next sufficient aggregate input is an upper coefficient 3.49 for the negative frontier up to N^(19/20), for all sufficiently large even N, with o(u) error. This input is unproved. Conditional on it and the frozen tail theorem, the weak K>C route closes at .95. Its full statement and numerical margin are in `SIGNED_LEDGER_NOTE.md`.

The finite Holder/moment construction has threshold coefficient sum 2+2/[δₙ(δₙ−1)], where Σ1/δⱼ=1 and δ₁=2. Hence at the square-root endpoint it forces Σαⱼ>1. This excludes that unchanged family for every fixed finite tuple, including the nine five-factor and 87 six-factor displayed cells. It does not exclude all tools. See `results/moment_family_endpoint.json`.

## I. New well-factorable remainder inputs (checkpoint 4)

The complete reductions are in `NEGATIVE_FRONTIER_NOTE.md`, Sections 2–5. They use Robert–Sargos Theorem 1 and Lichtman arXiv:2109.02851v2, Definition 2.1 and Theorem 2.10, together with a direct sharp-interval transfer. All levels below carry a fixed positive loss.

| Outer family | Cofactor level β | Coefficient restriction and consequence |
|---|---|---|
| d≈N^γ, γ<1 | β<min(5/4−γ,2−2γ) | Bounded outer coefficients; well-factorable modulus weights; o(u) aggregate remainder |
| Actual primes p≈N^γ, 1/4≤γ≤1 | β<5/4−γ | Untwisted prime indicator with smooth partition; Vaughan decomposition for γ>3/4 |
| Root, d=1 | β<5/4 | Linear lower and upper coefficients (16/5)ℒ(5), (16/5)𝒰(5) |
| Ordered outer product pq, exponents v<t | β<5/4−t−v in the new triangle | Positive lower branch when t+3v<5/4 |

The full-level factorization is chosen before smaller actual modulus boxes. If actual β′≤β and Δ=β−β′, a factor capacity s gives an actual factor exponent in [max(0,s−Δ),s], rather than a freely selectable point. The allowed RS window has width at least 4ρ+4Δ, with ρ=5/4−γ−β>0, enough for this uncertainty. Fixed parameter losses also cover the smoothing frequency extension.

The exact e|P(z) support is retained. Its small-prime condition is completely multiplicative; the squarefree condition introduces a gcd expansion after e₁=q a, e₂=q b. The four RS terms acquire summable q powers −5/4, −7/4, −3/2 and −2. The elementary type-I term has power −2. Thus neither squarefreeness nor cross-factor coprimality is silently omitted.

Signed smoothing errors are controlled with positive boundary envelopes and the absolute values of the separate convolution coefficients. No arbitrary bounded cofactor comparison is used, and the higher level is not asserted for arbitrary unfactored sieve weights or arbitrary weights on primes.

## J. Smaller-prime tail, signed costs and remaining target

Sifting the prime cofactor against its smaller prime gives the additional bound

\[
C_{\rm small}(\vartheta)=\frac{16}{5}\log\frac{5-4\vartheta}{\vartheta}<C(\vartheta),
\qquad4/5<\vartheta<1.
\]

Restricted positive blocks also bound the negative semiprime band by [C_small(κ)−C_small(ϑ)]u. This separately supplies the weaker frozen inequality without completing the original paper's citation-chain audit.

At b=1/4, the new root lower coefficient exceeds 4.4837637 and its upper coefficient is below 4.499537. The exact whole-frontier cap is stronger than the new direct cofactor sum: at κ=.95 the latter costs about 8.17235u. The first positive triangle recovers G in [.1428644132,.1429534496], but this equals the gain already contained in the direct larger-cutoff upper sieve and must not be credited twice. It supplies no terminal prime lower comparison.

A sufficient new frontier target is ℛ_.95≤(3.73+o(1))u, yielding a conditional prime coefficient >.0061962 with C_small. If the frozen C is retained, the sufficient target is 3.58u. Both estimates are unproved; the certified K remains 0.

The explicit sequence (Y/H)(1+λ(m))1_B(m), on a long carrier around N², satisfies the o(u) divisor-mass axioms through total level N^(5/4) and the admitted one-sided mass consequences, while assigning zero weight to every prime. It violates the 3.73 frontier target. This excludes a prime proof using only those mass interfaces. It does not match the actual support, individual floor bounds or power-saving remainder error, and it does not rule out methods using stronger arithmetic information.

## K. Original source interfaces (checkpoint 5)

This section preserves the checkpoint 5 source status; the missing 1989 checks are supplied in Section L below.

`ORIGINAL_SOURCE_AUDIT.md` records the page-image audit of the uploaded originals. Iwaniec's *A new form of the error term in the linear sieve* (1980), Theorem 1, p. 309, supplies signed bilinear remainders for every prescribed split, with capacities greater than 1 and s≥2. Its coefficients depend explicitly on the capacities. The stronger fixed-weight quantifier needed to change splits between blocks is explicitly recorded in Fouvry–Iwaniec (1983), p. 199, (1.2)–(1.3), with well-factorable weights of order 2. This corroborates the modern formulation used in checkpoint 4. Constant capacities greater than 1 cover the exponent-zero limiting choice within fixed margins. The full-level/smaller-modulus distinction and combined squarefree support remain mandatory.

Iwaniec's *Rosser's sieve* (1980), Theorem 1, p. 172, instead has the ordinary absolute divisor remainder. It supports the existing Type I interface and supplies no additional higher level by itself.

The Fouvry–Iwaniec upload is *Primes in arithmetic progressions* (1983), not the 1989 *Exponential sums with monomials*. Its main theorem has well-factorable level x^(9/17−ε), a fixed nonzero coprime residue, and an x/(log x)^A error for every fixed A. Subtracting endpoints leaves an error too large for the campaign's u scale. Proposition 1 additionally requires a Siegel–Walfisz coefficient condition; Proposition 2 has a power saving but requires an interval-indicator coefficient. A new application must provide the arithmetic reduction and adequate error bound. No new short-interval mass is credited, and no universal exclusion of these candidate tools is asserted.

The original 1989 pipeline audit remains pending. All previous numerical enclosures and conditional sufficient targets are unchanged; K=0 and H(ϑ) remains unproved.

## L. FI1989 source audit and new arbitrary-outer range (checkpoint 6)

`FI_1989_AUDIT.md` verifies Lemma 9, Theorem 6 and Theorem 7 against the original page images. Lemma 9 includes the reciprocal weight a_m b_n/(mn). A raw-sum replacement needs rectangular partial-sum uniformity and proper signed boundary control; Fourier-weight monotonicity is not a valid justification. The existing sharp transfer supplies the needed details. Theorem 6 requires an additive character in h and separate denominator coefficients; controlled smooth twists and interval completion are allowed with a loss, but arbitrary joint frequency/denominator weights are not admitted by this source.

Its six exponent inequalities match the companion. The continuous balanced top-frequency calculation confirms that its groupings do not improve β=(6−5γ)/4 for the submitted γ≥1 decomposition. The reconstructed tail route retains full-level factorability, actual-factor uncertainty, combined squarefree support and signed smoothing, and verifies the original C(ϑ) formula with those addenda. The frozen manuscript and numerical records are unchanged.

For arbitrary bounded outer c_d at any fixed γ<1, the newly admitted cofactor level is β<5/4−γ. For γ>3/4 choose full factor exponent s=Σ−1+τ; actual exponents occupy [s−Δ,s] on retained product blocks. The complete FI caps cover that whole interval, including the smoothing frequency extension. In the gcd expansion its six relative q powers are −5/4, −11/8, −3/2, −11/8, −3/2 and −5/2; all are summable without assuming H≤B/q. This removes the earlier additional arbitrary-outer condition 2γ+β<2. Arbitrary bounded prime weights are included below exponent 1; the arbitrary-weight endpoint γ=1 remains unadmitted.

The root and actual-prime tail levels, positive small R₂ triangle, ledger enclosures and sufficient 3.73/3.58 frontier targets are unchanged. No new positive prime mass is credited. K=0, H(ϑ) and the terminal prime comparison remain unproved. The full tool inventory and full adaptive optimization remain incomplete.

## M. Regional negative improvement and centered target (checkpoint 7)

`FRONTIER_INVESTIGATION_NOTE.md` supplies the complete new reductions. The extended arbitrary-outer range differs from the old one only at σ>3/4. Positive lower-sieve mass still requires β>2c≥1/2, hence σ<3/4 under β<5/4−σ. No positive branch region is enlarged at the existing base cutoff.

The negative third frontier restricted to p₁p₂p₃≤N^(19/20) does improve. Its ordered three-prime reciprocal density is ρ₃(σ)=(1/3)∫_(1/4)^(σ−1/2) log(4(σ−v)−1)/[v(σ−v)] dv. The old and new upper costs are ∫4ρ₃/β, with β=2−2σ and 5/4−σ respectively, over 3/4≤σ≤19/20. Outward enclosures give old cost in [.1847951,.1888265], new cost in [.0960834,.0977512], and a direct reduction exceeding .0887117u. This is a bound on one negative piece; it cannot be subtracted from an unrelated whole-first-frontier cap. The complementary third-frontier products remain unestimated in this design.

Direct reciprocal applications of FI1989 Theorems 1–5 add no higher generic level. Theorem 2's first term is exactly critical at η=Σ−1. Theorem 3 has necessary Σ≤19/16 there; Theorem 4's fourth term requires Σ≤15/14 in its fixed-frequency application. Theorem 5 has a free fourth slot and an opposite-exponent ratio phase. Its printed α≠1 conflicts with a proof that requires α≠−1; α=−1 is not admitted. A reconstruction for a free-denominator Type I family at α=1 remains a separate candidate. The direct positive three-prime product phase has exponent 1 in every variable, and the literal Theorem 2 bound at H≈N is too large for o(u). These are scoped direct-mapping tests, not an exhaustive rejection of the paper's methods.

The long-carrier parity witness has exact limiting root coefficient 2ℒ(8), and R_.95 coefficient in [4.2914672098,4.2915489447]. It therefore continues to rule out closure using only the extracted one-sided mass interfaces, including the new regional upper estimate. It does not satisfy the actual short support, individual floor bounds or stronger power-saving remainder.

A sufficient actual-coefficient input is R_.95(J_N)−(Y/Y₁)R_.95(B_N)≤(.338+o(1))u, for every sufficiently large even N, with the centered ordinary comparator of checkpoint 2. The refined reference coefficient lies in [3.3915468895,3.3916379312]. This input would yield a conditional prime coefficient >.0065583 with the admitted root and smaller-prime tail. It is unproved and does not imply the full H main term. The focused recent primary-source check found adjacent almost-all or at-most-three-factor results whose stated quantifiers, intervals or coefficients do not supply this input. K remains 0.

## N. Ross geometry and actual-support parity checks (checkpoint 8)

`ROSS_GEOMETRY_AUDIT.md` maps both supplied Ross papers to the actual centered band. In center coordinates the residue is −N² mod d. At the left edge A=N²−N/2, odd-modulus offsets satisfy 16r_d≡1−(4N−1)², a translated negative-square class. Fixed-period QR and CRT distributions are exact, but their averages do not imply the required result for every even N. Individual divisor density remains Y/d with floor error less than one.

The odd full-depth reciprocal model differs from the square-shell model at shell index N by O(1/N); its gamma+log(2) correction transfers to the centered interval and contributes only o(u). The remaining signed floor sum is still the exact difference from the actual prime count.

For each fixed r, the exact first frontier is the prime-anchored weighted-wave sum with S=q+rp, p prime, N^(1/4)≤p<N^.95 and P^-(q)≥p. Its coefficient restriction depends jointly on p and q. The orientation counts the least prime once; neither all factor pairs nor sums over several r values may be credited as the same mass. Uniformly over these pairs, rp/q≤r*N^(-.1)/(1−1/(2N))→0. The asymptotic target lies in wave tails; complete-wave Liouville covariance samples do not estimate its selected arithmetic weights. Balancing the largest selected primes would require r of order N^.1 and new uniformity in r.

The exact actual-support Liouville identity is sum_m lambda(m)*1_[P^-(m)≥z]=sum_(d|P(z)) mu(d)^2*sum_(q:dq in J_N)lambda(q). At z=N it equals minus the prime count. At z=N^kappa with kappa>2/3 it equals rough semiprimes minus primes. The twist adds lambda(d)*sum_q lambda(q) to each divisor error, so it is not automatically an actual-support countermodel satisfying the campaign's error bounds. The older long-carrier mass witness keeps its original, narrower scope. A sufficiently strong estimate of the complete signed Mobius remainder, including the small-cofactor end, would detect primes by the exact identity; the twist does not exclude that route.

No new restricted-frontier estimate or positive prime mass is admitted. The sufficient centered excess target remains .338u, K=0 and H(ϑ) remains unproved. Source bytes, prior analytic bounds and numerical ledgers are preserved.

## O. Actual prime-product reduction (checkpoint 9)

`RESTRICTED_FRONTIER_NOTE.md` proves a uniform bound for rows divisible by a prime square p² with p≥z: E([A,B];z)≤4H/ceil(z)+(10/3)B^(1/3), H=B−A+1. Dyadic counting first by d and then by q in m=qd² supplies the bound. On the actual J_N at z=N^(1/4), this is O(N^(3/4))=o(u).

For every even N≥18, a root-rough row in J_N has Ω≤7. Eight factors with two distinct odd primes exceed the shell, while the remaining eighth-power case is an odd square outside it. This statement concerns the actual root-rough rows; it does not alter the conservative depth-eight templates for the older full combinatorial expansion. The long comparator can contain eight-factor rows. Each of their factors lies in [z,z(1+epsilon1)], epsilon1=Y1/(2N²), giving normalized mass O(N*epsilon1^7)=o(u). This subpower estimate is distinct from the actual-shell O(N^(3/4)) bound.

M_j is the ordered j-prime product count divided by j!, with p≥z and, for j=2, min(p,q)<N^.95. The last restriction is automatic for j≥3. A row with prime multiplicities e_p has coefficient 1/product(e_p!). The kernel Kcal=sum_(j=2)^7 M_j therefore equals R_.95 on squarefree actual rows and undercounts repeated-factor rows by at most the large-square error. On the long comparator there is an additional nonnegative eight-factor correction. In particular, ΔR≤ΔKcal+O(N^(3/4)) uniformly, and ΔR=ΔKcal+o(u). The nonnegative long correction is subtracted.

Long reference coefficients follow the factorial convolution recursion s*g_j(s)=int_(j−1)^(s−1)g_(j−1)(v)dv, with c_j=8g_j(8). The two-prime frontier coefficient is log(7)−log(21/19), the three-prime coefficient lies in [1.2191073676093,1.2191484689775], and the four-to-seven sum C_h lies in [.3266190082200,.3266565947410]. These are reference masses, not actual-shell bounds. The optional allocation Δ₂+Δ₃≤.011u and Kcal_higher(J)≤2C_h*u would suffice for the .338u target; both bounds are unproved. The old marked three-prime branch overlaps M₃ and cannot be credited independently.

Sharp centered Mellin inversion uses half-integer endpoints after rounding Y1 to the nearest odd length. This changes the normalized count by O(Y/Y1)=o(u). With T=x², truncated Perron has per-box error O_j(log(x)/x). The centered window kernel has a second-order Taylor cancellation, and its |t|≤exp((log x)^(1/3)) contribution per box is O_j(Y*exp(−3*(log x)^(1/3))). The O(log^7 x) aggregate remains o(u). The centered signed high-frequency integral is unestimated. Frequencies above x/Y and all boxes meeting either window remain retained.

The four printed cases of Li arXiv:2308.04458v8 Lemma 4.2 have necessary interval exponents 29/57, 67/133, 31/61 and 14/27, respectively. Each exceeds 1/2. The rational certificate is valid for every four-group partition, and the fixed gaps survive o(1) exponent perturbations. This excludes those four printed cases at the endpoint; it is not an exclusion of other estimates or refinements.

Liouville's sign on a j-factor row is exactly (−1)^j. Nonnegative per-pair wave reweighting with weights summing to one preserves both row mass and its sign. Seventeen exact finite centered experiments, including long eight-factor rows, and four independent small prime-tuple fixtures passed. Finite experiments do not prove a uniform bound. The historical analytic ledger and source bytes are unchanged; no new terminal comparison or positive prime mass is admitted, K=0, and H remains unproved.

## P. Uniform two/three-prime bilinear and Vaughan reductions (checkpoint 10)

`TWO_THREE_BILINEAR_NOTE.md` defines c_N(d) as the prime indicator z≤d<w plus one half of the ordered prime-pair count pr=d with p,r≥z and pr*max(p,r)≤N². The supports are disjoint, so 0≤c_N(d)≤1. Its support lies in [N^(1/4),N^(4/3)], and relevant cofactors lie between constant multiples of N^(2/3) and N^(7/4). The coefficient is fixed at the actual square center and remains explicitly prime-supported or two-prime-supported.

Largest-cofactor triprime orientation has an exact correction one half on pr² with p<r and one third on p³. Freezing its gate at the center costs O(N^(3/4))+O(Y*(H1/x)*log N)=o(u) after centered normalization. The proof includes every threshold pr² in the reference window, with a reciprocal-weight estimate; their number alone is insufficient for the weighted long comparison.

Proper prime powers satisfy P(t)≤5sqrt(t) and reciprocal tail sum_(q≥R)1/q≤25/sqrt(R). Thus replacing the prime cofactor by Lambda(q)/log(q) has error O(N^(7/8))=o(u), including prime powers with base below the root roughness cutoff. The complete centered two/three-prime target equals the resulting bilinear count up to these uniform errors.

Vaughan's exact identity with U=V=floor(N^.01) gives two free-integer Type I terms and B_N(W)=sum_d c_N(d)*sum_(m>U,b>V)beta_U(m)*Lambda(b)/log(mb)*1_W(dmb), beta_U(m)=sum_(a|m,a>U)mu(a). The small Lambda term vanishes on the cofactor support. These specific coefficients are retained; the Type II count has no free unit-coefficient integer variable.

The combined Type I integral density is G(v)=sum_d c_N(d)/d*[alpha_U−(gamma_U+alpha_U*lambda_V)/log(v/d)]. Its second derivative is O(x^(−2)*log(N)^4); normalized symmetric centering makes the complete main integral o(u). On d≤N^.95 the lattice errors are O(N^.97), uniformly. This includes every semiprime Type I term and the unbalanced triprime Type I terms in that outer range. Their triprime reference coefficient lies in [.5764489880,.5765294344]; approximately 79 percent of the joint reference lies in this Type I domain. The reference share is not an actual count bound or a Type II estimate.

The remaining exact reduction is Δ₂+Δ₃=ΔB_N+ΔR_I,high+o(u), where R_I,high is the Type I lattice-minus-integral error for N^.95<d≤N^(4/3). The optional sufficient estimate ΔB_N+ΔR_I,high≤(.011+o(1))u is unproved. The higher-degree factor-two cap is also unproved.

The direct FI1989 Theorem 2 additive mapping leaves a limiting error of scale N before logarithmic and divisor losses. For the balanced triprime reciprocal mapping, Theorem 6 at Sigma=4/3 and eta=1/3 requires simultaneously n0≥1/3 and n0≤1/6, independently of factor grouping. Li Lemma 4.1's printed necessary strict balance facet becomes abs(alpha1−alpha2)<0 at interval exponent 1/2. These are scoped direct-mapping and formal-facet exclusions; sparse norm, spacing, or square-centered refinements are not excluded.

Sixteen thousand exact log-vector Vaughan identities and eight centered fixtures passed. Five fixtures additionally used independent prime-pair and prime-power enumeration. Seven of the 17 old finite samples exceed the narrower .011u allocation, with maximum about .0451025u; this does not disprove a sufficiently-large-N estimate with an o(1) term. Historical source and ledger bytes are unchanged. The campaign's certified K remains zero and full H is open.

## Q. Short-only joint remainder and wider Type I region (checkpoint 11)

JOINT_REMAINDER_NOTE.md proves that (Y/H1)*R_I,all(B1)=O(N^(53/150)*(H1/x)^(-1))=o(u), retaining the small normalized reference multiplier. The classical quantitative PNT for Lambda and mu also gives (Y/H1)*B_N(B1)=o(u). The actual short Type II sum is not estimated by either statement.

The entire short Type I floor error is uniformly O(N^(1-c)) through d≤N^(9/8). The frozen triprime ordering condition is automatic there, since d*max(p,r)≤d²/z≤N². Smaller-prime-slot RS covers sigma≤11/10; for 11/10≤sigma≤9/8, FI6 covers alpha≤59/200 and RS covers alpha≥59/200. The small-variable product exponent runs through [0,1/50] and frequency extension is 1/10000. The minimum source margins are respectively 6/625, 49/10000 and 23/5000. Exact vertex enumeration certifies the complete continuous regions.

Free Type I weights can be frozen at the center with error O(N^(53/150)*log(N)^C)=o(u). The short Type II logarithmic denominator can likewise be frozen to log(N²/d), with error O(N^epsilon/log N)=o(u), by a tau_4 representation bound. Exact outer divisors d|N² have total o(u) contribution to Type II and Type I floor errors; the neighboring-product correlations remain unestimated.

The resulting target is Δ₂+Δ₃=B_N(J)+R_I,core(J)+o(u), where the Type I core is restricted to frozen two-prime products N^(9/8)<d≤N^(4/3). The remaining sufficient inequality B_N(J)+R_I,core(J)≤(.011+o(1))u is unproved. The original Type II coefficients beta_U and Lambda, U=V=floor(N^.01), are unchanged.

Bretèche-Dress-Tenenbaum's uniform mean-square theorem gives sum_(M<m≤2M)|beta_U(m)|²=O(M); the ratio tends to a positive L when U and M/U tend to infinity. This is a valid diagonal norm input and not a vanishing factor or a bound for the fixed-center nearby-product correlations. The exact nonnegative quadratic-form and divisor-floor identities were independently checked.

The proved Type I triprime reference subregion has coefficient in [.9789675932,.9791185891], leaving reference mass in [.2399887785,.2401808758]. Approximately 92.16 percent of the joint reference lies in the new Type I domain. This is neither an actual count cap nor an estimate of Type II. The newer Pliego monomial corollary's particular domain, power weights and exponent assumptions were checked without admitting a new terminal tool.

Thirty-two polytope vertices, nine exact energy fixtures and seven actual short-window signed formal decompositions passed. Some small fixtures force larger U,V to exercise the identity; asymptotic campaign parameters are unchanged. Historical source and ledger bytes remain unchanged, certified K=0 and H is open.

## R. Audit of 007 and translated auxiliary graphs (checkpoint 12)

OPENAI007_AUDIT.md checks the complete ordinary two-point manuscript, its critical proof arguments and selected actual Lean source. Its quantitative affine theorem fixes the forms before X increases; its general multiplicative theorem has no quantitative rate. Subtracting prefixes gives an N²-scale error, while reindexing the square-centered interval introduces moving intercepts.

The quantitative residue comparison is uniform over translated intervals of length at least exp(L^A/2), with primes at most exp(L) and fixed modulus l. At X=N² this permits an interval of N sites. The analytic dilation comparison instead costs eta*N² on a width-N seed window, and the MRT centering input averages starting points on a long initial interval. These analytic steps have not been localized.

A new consequence of the qualitative graph proof is derived: the specific centered divisor kernel satisfies a bound C*L0*B^(-1-c_star/2)*(M+D0*Q_B+ceil(tau*h*H)+1) on every translated interval of M positive integers. The bounded test sequences and admissible families may vary. The parameters h,tau,C0,T remain fixed. With B=(1/2)log(log M), the period and shift are M^o(1); the estimate then has size O(L0*M*B^(-1-c_star/2)). This auxiliary kernel uses its specified prime bands and cutoffs, with divisor labels at most a power of log M. It has not been identified with the actual product-window Vaughan kernel.

The actual beta_U is not multiplicative: for distinct primes p,q>U, beta_U(p)=beta_U(q)=beta_U(pq)=-1. It need not be one-bounded; beta_5(30)=2. The normalized Mangoldt prime detector also fails multiplicativity. The existing uniform beta mean-square bound is retained. An O(N/log(N)^c) estimate for the entire actual Mangoldt-weighted numerator would suffice after logarithmic division for any c>0; 007 supplies no such numerator estimate.

The exact cofactor overlap is now K(k,l)=max(0,min(2Q,floor(Jplus/k),floor(Jplus/l))-max(Q+1,V+1,ceil(Jminus/k),ceil(Jminus/l))+1), on Q<b≤2Q, b>V. It is the Gram kernel in the signed quadratic form with alpha_N(k)=sum_(d|k,k/d>U)gamma_N(d)*beta_U(k/d), gamma_N(d)=c_N(d)*log(N)/log(N²/d). Its actual weighted quadratic form and the high-outer Type I core remain unestimated.

Fifty-six source records and 78 unchanged historical files were hash-checked. Source-level matches cover the three exported statement types and nine defining bodies. Exact arithmetic verified 83,568 overlap pairs, 60 signed Gram identities, 21 singleton-center factors and the coefficient/prefix witnesses. No Lean comparator or transitive axiom audit was rerun. The challenge placeholders are not treated as failures of the actual solution modules. Historical numerical bounds, certified K=0 and the unproved status of H are unchanged.

## S. Actual cofactor estimates and signed product region (checkpoint 13)

COFACTOR_ESTIMATE_NOTE.md supersedes the unestimated-overlap and d=9/8 cutoff statuses above. Actual outer divisors have all prime factors greater than U; hence alpha_N(k)=beta_U(k)*sum_(d|k,d<k)gamma_N(d). The proper condition excludes m=1. The outer weight is at most 42, using at most seven large prime factors of contributing k and the actual prime/two-prime coefficients.

Every translated interval of H integers greater than 1 has beta first moment -H*alpha_U+O(U) and second moment H*q(U)+O(U²). On J these are o(u) and (L+o(1))*Y, L>0. The actual uniform Gram bound is E_Q≪(1+N/Q)*min(N+Q*U²,(1+Q/N)*(N²/Q+U²)). Its prime-b version costs log(2Q)^(-1) in the first alternative. The kernel is exactly diagonal for Q≥N. These estimates do not supply the terminal logarithmic saving. Proper prime powers in b contribute o(u) absolutely on any selected outer/b subset.

The full Type II becomes log(N)^(-1)*sum_J beta_U(n)*W_N(n)+o(u), with the explicit nonnegative prime-divisor weight (13) bounded by (36+o(1))*log N. A constant weight can be subtracted using the completed first moment. The covariance remains unestimated at the target scale.

RS/FI cover all 19/20≤sigma≤113/100, 1/4≤alpha≤sigma/2, delta≥0, sigma+delta≤1153/1000, with 34 rational vertices and minimum facet margin 3/5600. Below total exponent 11/10 use RS; above it split at alpha=(15*Sigma-13)/14+3*nu/2, nu=1/10000. The two nonautomatic ordering indicators p²r≤N² and pr²≤N² and the product cutoffs are retained with half-integer Mellin separation. Thus complete Type I through outer exponent 113/100 is o(u).

The signed Type II region db≤N^(49/50), or N^(19/20)<d≤N^(113/100) with db≤N^(1143/1000), is o(u) after beta expansion. The second case uses the same reciprocal source coverage; the first is elementary because including the small Möbius divisor yields total exponent at most 99/100. The cutoffs U=V=floor(N^.01) are unchanged.

The remaining weight depends on b after this region removal. Its boundedness preserves the uniform Gram inequalities, but the original b-independent alpha must not be inserted into the unchanged closed Gram expression. The remaining gate is B_remaining(J)+R_I,d>N^(113/100)(J)≤(.011+o(1))*u. The high-outer discrete Vaughan sum cancels every non-prime-power cofactor exactly, giving the alternative centered-prime-count form (27). No terminal comparison, positive K, higher-degree cap or proof of H is admitted.

Exact checks passed for 200,898 coefficient identities, 53,118 overlap pairs, 24 Gram forms and 1,827 high-outer rows, including 1,565 non-prime-power cancellations. Larger finite U fixtures are explicitly stress tests. All 140 unchanged historical files and two new primary PDFs were hash-checked; the analytic ledger is unchanged.


## T. Regrouping in the signed delta estimate (checkpoint 14)

The proofs and exact domains are in DELTA_GROUPING_NOTE.md; src/delta_grouping.py verifies 80 rational source vertices. U=V=floor(N^(1/100)) is unchanged. In selected RS branches the entire small Vaughan product joins the standalone prime, replacing A=a by A=a+delta. FI keeps A=a. This requires bounded divisor-order convolution coefficients and the previously admitted signed sharp transfer. Exact ordering/product indicators are separated before collapsing coefficients.

| Input | Uniform conclusion | Source margin or scope |
|---|---|---|
| Complete Type I | R_I,d≤N^(457/400)=o(u) | Minimum margin 1/3500 |
| Complete Type II product region | B_db≤N^(459/400)=o(u), all actual outer coefficients | Minimum margin 9/14000 |
| Additional Type I pair regions | Two exact monomial tests (13) in the note; union admitted | Minimum margin 1/10000 |
| Remaining core density | Reference coefficient in [.0884954626805,.0885320794086] | A long-reference mass, not an actual short upper bound |
| Selected reciprocal engines at top frequency | No source window for total denominator exponent ≥5/4 | RS width 5−4Σ−7ν; FI width (5−4Σ−3ν)/2; limited engine obstruction |

D_good is the admitted Type I domain; C is its complement in the actual gated outer support. The exact remaining reduction is Δ₂+Δ₃=B_(db>N^(459/400))+R_I,C+o(u). No C row is removed from Type II, because d>N^1.1425 and b>U imply db>N^1.1525. Jointly B_C+R_I,C=A_C−integral(G_C), so the remaining interface is B_(D_good,db>N^(459/400))+A_C−(M_C+o(1))u. Non-prime-power cofactors cancel exactly in the joint core. The covariance weight retains both the outer-domain and product restrictions.

The .011u joint bound remains unproved; reference-mass shrinkage does not credit that discrepancy budget. No positive K or terminal prime comparison is admitted, and the separate higher-degree cap remains open. Earlier source files and the analytic ledger are unchanged.


## U. Audit of 021 and conditional three-factor shell count (checkpoint 15)

OPENAI021_AUDIT.md audits the full 83-page source at commit adc7f1241b42e322a6451854ab7e4b4c146bf78a. Theorem 1.1 asserts h(k)<=C*k^2/(log log(3k))^2, arbitrary modulus prime sets and signed starts. Theorem 1.2 supplies a uniform survivor count c*Y*V0/B^2 for every assignment of one class at every prime <=z, Y=floor(z^2/log(z)^2). No fatal defect was identified in the critical proof chain checked; this is not an independent certification of all dependencies. Actual Lean exports and both target configurations were read; no comparator or transitive axiom replay was run. Challenge placeholders are not implementation failures.

The reference correction certificate is I>.2229793730375238, evaluated with exact fractions. Inverse witnesses use a list fixed before failing tuples; variance uses residue-pattern domination rather than independence of actual classes. Full-box mass is O(B^(-2)) independently of width. Stopped corrections are grouped, with actual coefficient >.39 and reference <=.33; the final prime deletion gains X/log X, giving the improved iterated-logarithm bound.

Conditional on Theorem 1.2, set z_N=(sqrt(N)*log(N))/4. A translated block of Y_N~N/4 sites fits in J_N. It has >=c*N*log log N/(log N)^2 z_N-rough survivors. Since z_N^4 exceeds the shell upper endpoint, all have Omega<=3, counting multiplicity. The guaranteed lower-bound scale is o(u); this does not say the actual count is o(u). The survivors need not be primes or squarefree. Liouville does not distinguish primes from triprimes.

The remaining TypeI rows have d>N^(457/400), so N/d<N^(-57/400). Remaining TypeII has db>N^(459/400), so N/(db)<N^(-59/400). These violate 021's growing included-node length >=w^(1/100). Its small-prime parameter w is logarithmic in N; the actual beta divisor cutoff U=N^(1/100) is also outside the automatic small-pattern transfer. This excludes the direct current mapping, not all possible adaptations. A new weighted stop before these lengths fall below one would have to preserve beta_U, the actual outer support and the ordering/product gates.

All 32 primary source records, 156 unchanged historical records, 4,710 arbitrary-class CRT rows, 637 signed-translation rows and 504 restricted-hyperbola decomposition cases pass exact checks. The latter include full residue multiplicities and negative translations and do not test the analytic Weil bound. The campaign's prior reference bounds and analytic ledger are unchanged. The .011u joint estimate, higher-degree cap, positive K and H remain unproved.

## V. Weighted first-prime stopping (checkpoint 16)

WEIGHTED_STOPPING_NOTE.md stops at the canonical first outer prime p. For single-prime outers p<N^(19/20); for pair outers pr with p≤r and pr²≤N², p≤N^(2/3). The full I_p={k:pk∈J} has real width N/p>N^(1/20). Every p>U and beta_U(pk)=beta_U(k) exactly. All pair, prime-continuation, D_good/core and db>N^(459/400) gates remain in the continuation weight, rather than restricting the interval before its moments are estimated.

| Input | Proved uniform conclusion | Limitation |
|---|---|---|
| Actual beta mean on full I_p | mean(beta)=−alpha_U+O(N^(−1/25)) | No conditional prime/avoidance mean asserted |
| Actual centered beta energy | (L+o(1))*H_p; relative floor error O(N^(−3/100)) | L>0, so this is not a vanishing norm |
| Aggregate centered beta energy | (L*log(19/5)+o(1))*N | Cauchy with bounded continuation still gives only O(N) |
| Bounded local mean removal | O(N*exp(−c*sqrt(log N))+N^(24/25))=o(u) | Does not estimate the covariance |
| Actual core prime count | beta_U(k)=−1 on P_core,p; 0≤P_core,p≤1 | Retains the positive core contribution |
| 021 complete-group comparison with positive weights | Weight ratio≤34/33 preserves the source sign; ratio≤101/100 leaves coefficient 67/10000 | Requires the same eligible group; signed beta or sharp selection is not covered |

Define Z_p=v_p−P_core,p with normalized logarithmic continuation weights and all original gates, and C_N=sum_p sum_Ip (beta−mean_Ip(beta))*(Z−mean_Ip(Z)). Then Δ₂+Δ₃=C_N−(M_core+o(1))*u, with the preserved core reference enclosure [.0884954626805,.0885320794086]. The remaining one-sided target is C_N≤(M_core+.011+o(1))*u. Neither this bound nor a sufficient N/log(N)^2 continuation-variance bound is proved.

Narrow-bin positive outer log weights meet the new flatness condition when every support and selection gate remains constant and the complete eligible source group is available. An exact two-row example shows that arbitrary sharp nonnegative selection can destroy the grouped sign; U-rough beta weights can also reverse it. These limit the weighted inference and do not refute 021 or the desired delta estimate.

Seven independently enumerated fixtures passed: 42,407 stopped sites, 53,719 original prime-b rows and 149 core prime rows. Actual and stress truncations are labeled; these are identity tests, not asymptotic covariance estimates. All 194 nonmutable historical records and the analytic ledger are unchanged. No lower-bound mass, positive K or proof of H is credited.


## W. Partial logarithmic saving with the actual stopped beta (checkpoint 17)

BETA_SUPPORT_ESTIMATE_NOTE.md proves a deterministic uniform support bound on every full first-prime stop using Shiu's nonnegative multiplicative-function theorem in Mangerel (2023), Lemma 3.2. The source's divisor-bounded formulation makes its constant uniform over the moving U,q,d families. Its almost-all results are not used.

| Input or deduction | Proved conclusion | Limitation |
|---|---|---|
| Pairing at a prime q dividing k | beta_U(k)=−sum_(d divides k,q not divides d,U/q<d≤U)mu(d) | beta itself is not multiplicative |
| Least prime q≤U^(1/4), nonzero beta | A squarefree boundary divisor d exists; Pminus(d)>q | Remaining m may share primes with d and may contain q |
| Uniform source length after k=qdm | Width margin at exponent 1/30 at least 7/2400 | Uses actual p<N^(19/20), qd≤N^(1/80) |
| Support sparsity | #{k∈I_p:beta_U(k)≠0}≪H_p/(log U)^δ, δ≈.086071332 | Nonnegative overcount discards the signed continuation |
| Actual beta L1 mean | sum_(I_p)|beta_U|≪H_p/(log U)^(δ/2) | Inherited second moment still has positive limiting density |
| Actual stopped covariance | |C_N|≪N/(log N)^(.043035666…) | Does not reach u=N/(2 log N); no .011u coefficient admitted |

The key envelope is g_(d,q)(m)=1_(Pminus(m)≥q)*t^(omega_U(m)−omega(gcd(m,dq))) with t=1/(2 log 2). The subtraction retains repeated and shared prime factors. Shiu is applied only to nonnegative multiplicative envelopes bounded by tau; no coprimality or small-prime independence is assumed. The rough stratum, high distinct-prime-count stratum and boundary-divisor stratum are bounded separately.

All actual ordering, D_good/C, prime-b, nonunit and db>N^(459/400) gates remain in the bounded continuation Z_p=v_p−P_core,p. The joint interface and the core reference enclosure are unchanged. The remaining target is C_N≤(M_core+.011+o(1))*u; a signed estimate on the boundary-divisor continuation/core configurations is still needed. Positive K, H and the separate higher-degree allocation remain open.

Exact checks passed for 599,990 large/short beta rows, 1,569,950 arbitrary-prime pairing rows, 52,327 boundary-divisor witness rows and 61,382 overlap exponent rows. Four rational source-length vertices have minimum margin 7/2400; the parameters are enclosed outward. All 199 nonmutable checkpoint 16 records and the frozen analytic ledger are unchanged. These fixtures verify identities and proof hypotheses; they do not prove the analytic density asymptotic experimentally.


## X. Signed core absorption and stronger actual-beta L1 control (checkpoint 18)

SIGNED_CORE_CONTINUATION_NOTE.md aggregates the actual stopped weights as V_N(n)=sum_p v_p(n/p) and P_N(n)=sum_p P_p(n/p). Then C_N=sum_J(beta_U(n)*V_N(n)+P_N(n))+o(u), with the inherited local mean-removal error. All original selection, ordering, prime-b, nonunit and db>N^(459/400) gates are unchanged.

| Deduction | Proved conclusion | Limitation |
|---|---|---|
| Core ordering and uniqueness | n=prℓ with p≤r≤ℓ; P_N(n)≤1 | Uses pr∈C, hence pr>N^(457/400) |
| Actual absorbing rows when r<ℓ | Single outers r and ℓ both occur; rℓ>D_B; their log ratios sum to at least 1−2/(N log N) | Repeated largest-prime cases are handled as a sparse error |
| Rough core upper absorption | sum_(Pminus(n)>U)(P_N(n)−V_N(n))≤O(N^(2/3)+1/log N)=o(u) | A one-sided upper bound; the rough contribution need not be o(u) absolutely |
| Signed remaining interface | C_N=F_N^+−G_N^−−R_N+o(u), F_N^+,G_N^−≥0, R_N≥−o(u) | The required comparison of these actual weighted sums remains unproved |
| Smooth-factor continuation identity | V_N(a*m)=V_N^*(m) for U-smooth a>1 and a*m∈J | V_N^* includes activated unit rows; the ordinary formula on m would omit them |
| Exact signed boundary kernel | Nonrough sum equals −sum_(q,d)mu(d)*K_N(q,d), retaining roughness and every prime-product gate | No uniform signed bound for K_N(q,d) is admitted |
| Stronger actual beta L1 bound | sum_(I_p)|beta_U|≪H_p/(log U)^η, η≈.0602478244 | Uses direct low-count boundary multiplicity and high-count Cauchy; does not supply the u-scale sign comparison |
| Stronger absolute covariance bound | |C_N|≪N/(log N)^η | 1−η≈.939752176 logarithmic power still separates this scale from u |

The fixed parameter rho is the unique root in (1,2) of 3−rho+rho*log(rho/4)=0; t=rho/2 and eta=(1−rho+rho*log rho)/2. This balances the increasing high-count L1 exponent with the decreasing low-count boundary exponent. The old support-sparsity bound with delta≈.086071332 is retained. No new selected-subset beta energy or multiplicativity of beta is assumed. The same uniform all-interval Shiu input is applied only to nonnegative divisor-bounded envelopes.

At a rough core site, the two actual single-prime continuation rows leave cofactor p>1 and pass the exact db gate with exponent margin 223/1200. All three primes lie below the single-prime cutoff with margin 37/400. There are O(N^(2/3)) repeated-largest exceptions because for each possible smallest factor p the r interval in n=p*r^2 has real width less than one. The repeated-small-prime case is included in the regular absorption.

The remaining target is F_N^+−G_N^−−R_N≤(M_core+.011+o(1))*u. The core reference enclosure, historical analytic ledger, certified K=0, and open status of H and the higher-degree allocation are unchanged. Source 007/021 comparisons are not automatically applied to the new signed kernel.

Seven fixtures passed on 141,107 shell sites: 111,967 smooth identities, 30,087 signed boundary rows, 538 regular core absorptions among 539 core sites, and both repeated-prime patterns. A stress fixture exercises 2,798 nonrough negative-beta sites. Another 73,143 signed even/odd boundary counts and 20,858 overlap exponents passed. Three rational core-domain vertices and outward root/exponent certificates passed. All 209 nonmutable historical records and the frozen mass ledger are unchanged. Finite checks verify identities and proof hypotheses, not the asymptotic terminal comparison.


## Y. Signed kernel estimation (checkpoint 19)

SIGNED_KERNEL_ESTIMATION_NOTE.md retains the exact checkpoint-18 continuation and activated-unit kernel. The deterministic uniform Shiu input now supplies bounds at scale u for the actual rough counterweight and the large least-prime block; it supplies no sharp signed terminal coefficient.

| Deduction | Proved uniform conclusion | Limitation |
|---|---|---|
| Actual rough counterweight | −o(u)≤R_N≪u | Constant unspecified; rough contribution is not declared absolutely o(u) |
| Individual activated-unit boundary kernels | K_J(q,d)≪N/(qd log q); the normalized reference has the same bound | Summing absolute envelopes does not preserve Möbius cancellation |
| Large least-prime signed block | |S_>T(J)|≪N log(U)/(log T)^2; T=U^epsilon gives O(epsilon^(-2)u) | No explicit .011 coefficient; q≤T remains unestimated at u scale |
| Exact sign above sqrt(U) | beta_U=omega_U−1; nonrough block nonnegative | All negative nonrough beta counterweight is supported at least prime ≤sqrt(U); discrepancy need not be nonnegative |
| Normalized exact long reference | a*(S_N(B1)−R_N(B1))=(M_core+o(1))*u | Uses inherited long PNT and long TypeII reduction; no short PNT inferred |
| Exact coefficient interface | −sum mu(d)*(K_J−aK_B1)−(R_J−aR_B1)≤(.011+o(1))*u is sufficient and equivalent up to inherited o(u) | Estimate is unproved; reference subtraction is retained |
| Active smooth-multiplier rigidity | Rough part>D_B>N, so at most one smooth multiplier can enter J | Invariance alone supplies no sign pairing inside J; not a counterexample to actual V_N |
| Boundary cofactor cells | Distinct qd≤U²<N have disjoint J/(qd) cells | No independence asserted; long reference cells need not be disjoint |

The global kernel interval Shiu margin at exponent 1/30 is at least 457/500. The reference freezing uses an averaged tau_4 bound with fixed B=4,C=1; a pointwise N^epsilon majorant would not suffice for its rho error. Proper-b powers, low-product long floors and normalized core powers have explicit negligible errors. No short core absorption is transferred to B1.

The inspected all-interval primitive Möbius and nilsequence results do not directly supply the changing weighted kernels or their interval lengths. This is a source-specific application audit, not a claim that no other methods exist. The earlier 007/021 application gaps remain unchanged. The overall exponent .0602478244, core reference enclosure, historical analytic ledger and certified K=0 are unchanged. H and the higher-degree cap remain open.

Six fixtures passed on 564,796 short/reference sites, independently enumerating 120,405 kernel sites. They exercised 28,095 unit rows, 64,731 positive and 7,436 negative active nonrough sites, both Möbius signs, 51,385 repeated-q and 21,088 shared-d sites. Another 119,340 beta-envelope checks include 103,054 high least-prime sign identities. Reference windows are artificial 3N+1 fixtures and stress cutoffs are explicitly labeled; these do not test asymptotic constants. All 214 nonmutable historical records and the frozen negative-frontier ledger are unchanged.


## Z. Small-prime cancellation (checkpoint 20)

SMALL_PRIME_CANCELLATION_NOTE.md retains the checkpoint-19 terminal discrepancy. It proves full-interval energy localization and substantial signed cancellation in an actual even-row subset of the original long reference. The short weighted block remains open.

| Deduction | Admitted conclusion | Scope / limitation |
|---|---|---|
| All fixed absolute moments above T | Sum_rough_T abs(beta_U)^j <<_j H*(log U)^(2^j-1)/(log T)^(2^j) | Fixed integer j; fixed T=U^epsilon gives O_j(epsilon^(-2^j)*H/log U) |
| Small-prime full-interval beta energy | (L+o(1))*H on Pminus<=U^epsilon | Uniform full stopped intervals and full shell only; no selected beta²V energy inferred |
| Actual small-prime reference signed sum | a*S_<=U^epsilon(B1)=O_epsilon(u) | Short counterpart remains unbounded at u scale by this argument |
| Exact even pairing | beta_U(c)=-sum_{d|c,d odd,U/2<d<=U} mu(d) | Repeated powers of 2 retained; odd reciprocal mean has inherited PNT decay |
| Both-sign even harmonic masses | Each >=c*log N/((log U)^delta*(log log U)^(3/2)) on N^.2<c<=N^.25 | Uses the newly admitted published GKM/Ford isolated-divisor lower-bound construction on initial intervals |
| Actual marked continuation W_N | 0<=W_N<=V_N, single-prime p in [N^.3,N^.35], even residual c in (N^.2,N^.25] | All original coefficients and gates retained; c need not be smooth or coprime to p |
| Actual opposing reference masses | Each sign >=c*N/((log U)^delta*(log log U)^(3/2)) | Larger than u; these are reference masses, not lower bounds for subtracted discrepancies |
| Actual reference signed cancellation | a*sum_B1 beta_U*W_N=o(u) | Long PNT at relative width rho=N^(-o(1)); not a short prime PNT |

The marked reference prime centers have exponents [7/5,3/2]. Actual short prime intervals have relative length exponents [2/7,1/3], so the long PNT used for the reference cannot be inserted into the short sum. Full-stop Shiu margin is 3/200; inherited beta floor-error margin is 3/100. The marked product gate has margin 241/400.

The two signs already have substantial mass at q=2, while the signed full small-q reference is O(u). Charging the two reference masses separately as O(u) errors is invalid. No lower bound for sum |K_J-a*K_B1| follows from those masses, and no barrier to other signed methods is claimed.

The next estimate remains E_small+E_large-E_rough<=(.011+o(1))*u. A concrete test subproblem is the actual even marked short prime sum (18), with its unchanged reference subtraction; the complementary continuation sectors and joint coefficient must still be handled. No positive prime mass is credited. The global eta exponent, core enclosure, historical ledger, K=0, H status and higher-degree cap are unchanged.

48,000 even identities, 479,980 fixed-moment envelopes and 4,099 actual marked rows passed. Both signs and 62 rows where the outer prime divides the residual are exercised. Artificial reference windows and enlarged residual ranges are labeled stress fixtures, not asymptotic tests. All 220 nonmutable checkpoint-19 records are preserved.


## AA. Marked-even completion (checkpoint 21)

MARKED_EVEN_COMPLETION_NOTE.md corrects the aggregate-order gap in checkpoints 19-20 without claiming a separate bound for their marked residual slice. Historical proof notes retain their original bytes.

| Deduction | Admitted conclusion | Scope / limitation |
|---|---|---|
| Completed original Vaughan sum | C_N(J)=Q_all(J)-Y*Pi_good+o(u), hence abs(C_N)=O(u) | Original nonnegative prime-cofactor marks are bounded by 3*rough_z; Shiu gives order only |
| Small least-prime short block and discrepancy | S_<=U^epsilon(J)=O_epsilon(u), E_<=U^epsilon=O_epsilon(u) | Completes the order-of-magnitude question; no sharp .011 coefficient |
| Fixed e-divisibility density | A_e, Gamma_e, L_e are negligible for squarefree fixed e>1 | Small Mangoldt bases dividing e are retained; finite coprime Euler-factor extension is proved |
| Fixed lattice source transfer | Full good TypeI and low-db TypeII remain negligible under e|n | Split independent finite gcd classes; preserve all gates; strict inherited margins survive fixed scaling |
| Full fixed masked continuation | Sum_(J,e|n) beta_U*V_N=o_e(u) and normalized original reference o_e(u) | e is fixed before N tends to infinity; includes complete even sector e=2 |
| Fixed least-prime union | S_<=Q(J), a*S_<=Q(B1), E_<=Q are o_Q(u) | Exact finite inclusion-exclusion; no explicit growing cutoff reaching U^epsilon |
| Complete marked outer prime band | T_mark+T_complement=o(u) on J and normalized B1 | All even residuals with original continuation gates; separate marked slice still open |
| Marked odd-divisor floor reduction | c=2*d*ell, d odd in (U/2,U], with both exact shell and residual endpoint gates | Denominator exponent [44/25,181/100]+o(1); direct audited RS/FI windows are empty beyond 5/4 |

The .0602478244 exponent remains the direct absolute-beta bound. It is no longer the best available bound for the completed signed covariance. Earlier current-index flags saying the short small-q aggregate was not estimated at u scale are superseded here. The large opposing reference masses remain valid and do not imply an absolute discrepancy lower bound.

The sharp remaining comparison is E_(Q<q<=U^epsilon)+E_(q>U^epsilon)-E_R<=(.011+o(1))*u for any fixed Q. The marked slice separately still needs signed control; completion only relates it to its complementary residual sectors. A non-effective slowly growing Q(N) follows by diagonalization, but an explicit quantitative growing-modulus range is not certified.

Exact checks passed for 105 density identities, 112,896 divisibility rows, 1,323 endpoint floors, 79,996 least-prime union rows, 138,004 actual prime-mark cap sites, 310,543 masked Vaughan rows, 2,029 original marked prime rows and 8,116 independent marked floor rows. Both signs and 42 outer-prime/residual overlap rows are exercised. Finite tests do not prove the analytic asymptotics or missing coefficient. All 226 nonmutable checkpoint-20 records and the negative-frontier ledger are unchanged. K=0, H and the higher-degree cap remain open.


## AB. Signed sieve coupling (checkpoint 22)

SIGNED_SIEVE_COUPLING_NOTE.md supersedes the diagonal-only growing-cutoff limitation recorded at checkpoint 21. The separate marked slice and sharp residual comparison remain open; earlier proof files are unchanged.

| Deduction | Admitted conclusion | Scope / limitation |
|---|---|---|
| Uniform coprime Mobius densities | Sum over squarefree e<=2N^delta0 of abs(A_e)+abs(Gamma_e)+abs(L_e) decays faster than every log power | Retain tau(e)*C_e/e; include small Mangoldt bases dividing e |
| Growing-mask reciprocal transfer | Some fixed delta0>0 has sum_e(abs(B_e(J))+a*abs(B_e(B1)))=o(u) | Strict raw source reserve survives kappa scaling; final numerical delta0 not selected |
| Long-reference logarithmic freezing | Sum masks pointwise, envelope tau(n)^2<=d_4(n), cost N*rho*(log N)^C=o(u) | Do not multiply slow rho decay by N^delta0 |
| Positive dimension-two sieve error | O(H*log(U)/log(T)^2*exp(-log(D)/log(T))) | Odd-prime beta sieve B=32; positive terminal products lie below D; deterministic Shiu on W/d |
| Exact signed sector coupling | S_<=T=B_2-sum_(e>1)lambda_e^+*(B_e-B_2e)+signed_positive_gap | Coefficient one; no ordered inequality after multiplying by signed beta |
| Growing subpower small-prime block | abs(S_<=T_N(J))+a*abs(S_<=T_N(B1))=o(u) whenever log(T_N)=o(log N), T_N->infinity | Explicit T_N=U^(1/log log N); no numerical coefficient charged |
| Fixed-power small-prime budget | C*epsilon^(-2)*exp(-100*delta0/epsilon)*u+o_epsilon(u) | Budget tends to zero as epsilon decreases, not fixed-epsilon o(u); numerical epsilon not evaluated |
| Coefficient-preserving remaining comparison | E_(T_N<q<=U)-E_R <= (.011+o(1))*u | This remains open, with exactly the original .011 coefficient |

The marked (18)/(20) and complementary residuals enter the complete even sector with their original logarithmic ratios and coefficient one. Their separate sizes are not bounded at u scale. Both signs and repeated prime factors remain permitted. No new short signed Mobius estimate or individual short prime PNT is admitted. The inherited full covariance O(u), direct absolute-beta eta=.0602478244 estimate, frozen mass ledger and K=0 are unchanged. The higher-degree allocation and H remain open.

Exact checks passed on 4,288 prime-divisibility patterns, 1,472 perturbed facet terms and 108,700 active original-continuation sites. The marked stress partition has 629 positive and 55 negative rows. All 232 nonmutable checkpoint-21 records and the negative-frontier ledger are unchanged. Finite samples establish neither the analytic theorem nor the remaining sharp coefficient.


## AC. Joint signed comparison (checkpoint 23)

JOINT_SIGNED_COMPARISON_NOTE.md retains the original .011 coefficient. The cutoff-free equivalent is Q_all(J)-a*Q_all(B1)<= (.011+o(1))*u, by checkpoint21 completion and checkpoint22 subpower sifting. This equivalence does not prove the sharp count.

The actual-shell prime-cofactor mark is unique and at most one; the earlier cap of three is valid but weaker. No cap-one assertion is made on the long reference. Paired positive trapezoid smoothing costs at most .003065u for kappa=1/1000. Its low Mellin frequencies, the normalized reference high-frequency tail, and the final short tail beyond N^(21/10) are o(u), by the admitted long PNT and elementary Mellin estimates. The remaining actual signed integral must be bounded by (.007935+o(1))*u; that estimate remains open.

For a method requiring a fixed least-prime power cutoff, a .001 budget leaves .010; the note gives an explicit epsilon recipe in the inherited constants delta0 and Cprime without inventing numerical values. All approximation costs must be retained.

Exact checks exercise 1,911,710 coefficient-one sector identities, 679,425 active original continuation rows, 95,003 actual-shell mark caps, 50,843 prime-padding rows and 95,175 smoothing checks. Stress U and one artificial long window are labeled. The finite checks do not prove the sharp coefficient. All 238 nonmutable checkpoint-22 records and the negative-frontier ledger are unchanged; K=0, H and the other open targets remain open.


## AD. Spectral coverage and an auxiliary exact identity (checkpoint24)

SPECTRAL_COVERAGE_NOTE.md proves additional uniform estimates while retaining the .011 target and .003065 smoothing charge. Exact product localization F_chi has coefficients Q_N({n})chi(n/x), with global mark cap3; it cannot use the sharper cap1 from the actual shell on the broader support. Expanding its square and bounding harmonic rows gives an absolute tail o(u) above T_star=N^(4/3)(log N)^2. Low frequencies and the normalized smooth-reference tail are negligible. The original integral equals the localized integral through T_star up to o(u); no assertion is made about individual old unlocalized high bands.

An auxiliary identity with U_aux=V_aux=floor(N^(1/1000)) retains every term. It does not discard a least-prime sector or change original U, D_good, V_N or the small/high/rough partition. Complete auxiliary Type I is negligible through N^(4609/4000), with additional pair wedges; low-product Type II is negligible through db<=N^(461/400). All 80 rational vertices have strictly positive source margins. The auxiliary core reference is [0.0606181981056243773390,0.0606520446991740030317]. It is not a short count cap; its associated auxiliary Type II contribution changes and remains open.

| Claim | Status / scope |
|---|---|
| Localized absolute tail above T_star | Uniform o(u), elementary proof; zero coefficient charge |
| Auxiliary TypeI complete range and two wedges | Uniform o(u), audited RS/FI restrictions retained |
| Auxiliary TypeII small-db product | Uniform o(u); larger db remains open on every outer family |
| Full centered prime-product region from TypeI coverage | Not inferred |
| Coupled auxiliary good TypeII plus positive core | Required <=((1+kappa)M_core+.007935+o(1))*u; unproved |
| Downward-rounded sufficient coefficient | .0686138, lower reference endpoint credited |
| Fixed least-prime threshold if needed | Original (23) budget xi; remaining spectral allowance .007935-xi |

The unavoidable band S>=5/4 for the standard two-engine top-frequency mapping has reference coefficient [.03558733741968899790,.03559402912923898414]. This quantifies a source-specific gap, not an obstruction to other methods or signed counterweights. Robert-Sargos Theorem3 needs an unweighted free standalone sum; Pliego2024 Corollary1.1 does not supply the current phase/coefficient/domain interface. Neither is admitted for the sharp estimate. Exact identities passed under three independent stress cutoffs, and 53,847 broader product sites passed the cap test. All 244 nonmutable checkpoint23 records are preserved. The .007935 and .011 coefficients, marked slice, higher-degree allocation and H remain open; K=0.


## AE. Short-scale centered localization (checkpoint25)

SHORT_SCALE_LOCALIZATION_NOTE.md retains the original .011 comparison and .003065 smoothing allowance. The actual product mark is unique and z-rough throughout |n-N^2|<=N+1 for even N>=2^16. A C2 local cutoff equals one on psi_Y and has area (1501/1000)*Y. Subtract the original long-PNT density G_N before forming its local Mellin transform Phi_N; the full signed integral equals I_kappa up to o(u). This does not approximate the short prime count by G_N.

An elementary weighted Selberg construction has exact quadratic main term 1/G(R), G(R)=sum_(r<=R)mu(r)^2/phi(r)~log R, R=floor(N^(1/4)/2), and lattice error O(R^2*log^2 R)=o(u). It supplies an actual local L1 envelope. The new absolute frequency tail beyond L*x/Y is at most (21147/L)*u eventually, uniformly L>=1. Taking L=log N gives o(u), shortening the upper frequency to (x/Y)*log N~N log N with zero nonvanishing allowance cost. The low local integral is o(u) absolutely. No individual old unlocalized or checkpoint24 bands are declared negligible.

| Claim | Status / exact scope |
|---|---|
| Narrow padding mark cap one | Proved for |n-x|<=Y, even N>=2^16 |
| Weighted Selberg upper envelope | Proved, actual marks bounded by the rough indicator |
| New centered integral through (x/Y)*log N | Equals original residual up to o(u) |
| Fixed multiplier L tail cost | 21147/L, retained in .007935-21147/L-xi |
| Explicit coupled upper coefficient | 5.000714, conservative and much too large |
| Required central .007935 and coupled .0686138 | Both remain unproved |

All 252 nonmutable checkpoint24 records and the frozen mass ledger are preserved. Exact checks cover 77,776 quadratic pairs, 771 independently enumerated lattice rows and 22,739 local mark sites; they do not prove the sharp coefficient. A rational Machin-series enclosure certifies the upward-rounded tail constant. No least-prime sector is discarded; original and auxiliary Vaughan cutoffs, higher-degree allocation and K=0 are unchanged.


## AF. Two free variables and a retained outer Type II term (checkpoint26)

TWO_FREE_PRIME_DECOMPOSITION_NOTE.md audits the deeper cofactor identity and proves a regional estimate after expanding the smaller outer prime detector too. The original least-prime cutoff, .011 allowance and .003065 smoothing charge are unchanged.

| Actual family / input | Completed result | Remaining scope |
|---|---|---|
| Cofactor-only depth-four identity | Exact coefficients 4,-6,4,-1 retained | One-variable reciprocal source gap persists for S>=5/4; no global obstruction inferred |
| Double Type I with two free integer slots | Main reference and uniform o(u) error on pr^2<=N^(3987/2000), p<=r | Complete good-region prime count still has Type II terms |
| Direct Robert–Sargos Lemma9 | Unit/log free slot admitted; gates handled by the inner subinterval maximum and Abel summation | Arbitrary prime-weighted free slot remains inadmissible |
| New outer Type II × cofactor Type I, b_p<=N^(1/800) | Whole signed sum o(u), zero nonvanishing budget | Larger actual Mangoldt factor retained |
| Earlier Type I and low-db Type II coverage | Preserved on the hybrid union with actual gates | Larger-db cofactor Type II retained |
| Hybrid pair core | Ordinary reference in [.00561763293475439,.00561785523729346] | No sharp short-count bound inferred |
| New coupled three-term comparison | Exact coefficient-one identity; coarse upper 4.945625 | Sufficient .0135582 coefficient remains unproved |

The first direct Type I facet has reserve 1/2000 and raw-term reserve 1/8000. The low-Mangoldt-factor outer Type II completion has first reserve 1/4000 and raw-term reserve 1/16000. Exact rational vertices certify continuous ranges; affine endpoint-order guards certify the hybrid geometry.

The new sufficient coefficient belongs to an expression containing an additional outer Type II term; comparing it with checkpoint24's .0686138 alone does not compare proved discrepancy bounds. The remaining analytic input is the signed joint estimate or the original .007935u integral. A later fixed least-prime power cutoff must charge xi from (23); a fixed complete-transform frequency multiplier L must charge 21147/L. The auxiliary Mangoldt-factor completion discards no least-prime sector and adds no such charge.

Checks passed for 6,645 depth-four identity rows, 22,100 tensor Vaughan rows, all strict regional facets and 476 affine endpoint-order guards. These fixtures do not prove the sharp coefficient. All 259 nonmutable checkpoint25 records and the frozen negative-frontier ledger are unchanged. K=0, H, the optional marked estimate and higher-degree allocation remain open; milestone7 is deferred.


## AG. One-sided coupled upper envelope and positive complement (checkpoint27)

COUPLED_ONE_SIDED_NOTE.md applies the already admitted full-level root upper sieve uniformly to the smoothed endpoints, then completes the actual three-term identity. It proves a coefficient without estimating individual signed TypeII terms.

| Claim / family | Completed result | Remaining input |
|---|---|---|
| Full checkpoint26 three-term expression | Upper coefficient 1.441618 | Required .0135582 remains unproved |
| Original centered marked contrast | Coarse upper 1.435994 | Required .007935 remains unproved |
| Centered z-rough count | Upper coefficient .007825257 | This is a different arithmetic count |
| Positive clipped complementary count | Exact short partition; normalized long excess-mark error o(u) | Centered lower comparison with deficit .0001u |
| Transfer after that lower comparison | Conditional .007925257 integral / .010990257 original coefficients | Missing lower estimate is not inferred |
| Direct final-cofactor linear lower sieve | Limiting prime s=5/4; balanced-semiprime s<=4/7; four-prime positive margin absent | Switching / joint degree comparison not excluded |

The positive short complement contains primes, unmarked balanced semiprimes with smaller factor >=N^(19/20), and rough integers of degree >=4, up to a nonnegative negligible repeated-three-prime term. Its ordinary reference coefficient is in [1.42812738782223954808,1.42816857732647018189]; it is not a proved short lower bound.

The concrete sufficient comparison uses its actual normalized original long count: Delta_D>=-(.0001+o(1))u. The certified rough coefficient leaves .000009743 of the original allowance after this deficit. Any later fixed least-prime power budget xi from checkpoint22 (23), or fixed-multiplier tail charge 21147/L, must remain in .003065+C_rough+eta+xi+21147/L. This continuation introduces no nonvanishing charge.

Outward trapezoid bounds refine the auxiliary root upper and Buchstab reference enclosures without changing old ledgers. Exact checks cover 402,157 original short-padding sites and the broad multiple-mark witness N=62,n=2431. Finite checks do not prove the sharp complement estimate. All 268 nonmutable checkpoint26 records are unchanged; H, positive K, optional marked and higher-degree tasks remain open.


Checkpoint27 clarification: the next action is the switched lower-weight audit in COUPLED_ONE_SIDED_NOTE.md Section8. A candidate must lie below the actual positive complement on the short padding; its normalized long-reference loss and one-sided short/long comparison error must total at most .0001u. The transfer criterion is proved, but no qualifying weight is constructed. The next deliverable is a coefficient/gate/source coverage table with these quantitative losses, or an explicit unsupported component.


## AH. One switched lower-weight feasibility audit (checkpoint28)

SWITCHED_MINORANT_AUDIT_NOTE.md defines an exact y-rough base plus a two-smallest-prime switched lower weight. Its fixed level sum is 1249/1000 and its box gate is 8PR^2<=N^(1249/1000). The auxiliary canonical p=r row has unit weight; the original Q_N half-diagonal weights remain unchanged.

| Requirement | Result |
|---|---|
| Pointwise lower weight | Proved by source-normalized singleton sieve kernels and unique two-smallest-prime selection |
| Switched WF remainder conditions | Pass: gamma<=1249/1500<1, gamma+beta=1.249<1.25, exact sifting support and full level retained |
| Actual y-rough base comparison | Still unproved; lower linear sieve has f(1249/950)=0 |
| Total reference/comparison budget .0001 | Fails already by reference loss >=1.56 |
| Omitting negative active blocks | Best remaining mean loses >=.32694384580670 of higher-degree reference |
| Perfect pricing inside the active gate | Still omits a four-prime box costing >=693/911600=.0007602018429... |

The failure is scoped to separate lower rough-cofactor minus upper prime-cofactor linear sieve pricing. Its normalized lower term is <=log(499/250)<1, while the upper term is at least one. Even one positive block in this family would require total level B>(3+e)/4=1.42957045711476..., a necessary pricing condition rather than a sufficient H estimate. Other switching, pooled degree estimates and coefficient families are not excluded.

The next decision is to discard this construction. A new candidate should account for the omitted four-prime box and audit the one-smallest-prime pool Pminus(m)>=p, Omega(m)>=3, kept together with the base. The exact short identity is verified; its coupled comparison and a qualifying minorant remain open.

Exact checks cover 451,078 original short-padding sites, both source branches, repeated factors, omitted-box witnesses, and the first-prime interface. The numerical tests do not instantiate the universal Iwaniec weights or prove a sharp short estimate. All 275 nonmutable checkpoint27 records are preserved. Original .003065/.007935/.011 coefficients and any later xi or 21147/L charges are retained; no rejected-candidate loss is added to the global allowance. K=0 and milestone7 remains deferred.


## AI. One-prime residual-degree feasibility audit (checkpoint29)

ONE_PRIME_DEGREE_POOL_AUDIT_NOTE.md tests a full one-smallest-prime lower weight with fixed level sum 1249/1000. It retains all physical outer primes p<= (3x/2)^(1/4), uses the primitive rough lower kernel with cutoff 2P, and subtracts exact prime and rough semiprime cofactors to retain Omega(m)>=3. The old four-prime box is geometrically included.

| Requirement / component | Result |
|---|---|
| Pointwise lower weight | Proved; repetitions and original canonical marks retained |
| Primitive rough WF remainder | Admitted: alpha in [1/4,1/2], beta=1.249-alpha; both RS and FI margins positive |
| Actual prime/semiprime exclusions and exact base | Centered comparisons remain unproved |
| Full candidate favorable reference loss | At least .94u |
| Best deletion / convex prime weighting | At least .18u loss, even at favorable 5/4 ceiling |
| Positive-part price clipping | Used only for reference optimization; no integer-weight transfer inferred |
| Least-prime band [.40,.43] | Covered, but primitive net reference price is negative |
| Coupled degree-pool band reference | In [.00980703333218,.01000715975262], not a short lower bound |

The scoped rejected family is one primitive lower rough sieve per prime followed by exact or upper-majorant low-degree exclusions and coefficients theta_p in [0,1] independent of the product integer. Other one-prime kernels and direct coupled estimates are not excluded. Finite source tolerance and upper exclusion majorants worsen the failure. The 5/4 source endpoint is not applied; it is only an upper ceiling for favorable pricing.

The next explicit input is a kernel for the joint pool Pminus(m)>=p, Omega(m)>=3 on N^.40<=p<=N^.43, or its actual centered lower comparison G_band(psi_Y)-a_N*G_band(psi_H1)>=-(eta_band+o(1))*u. Keep the remaining base and pool with eta_band+eta_rest<=.0001. This band estimate alone is insufficient for the full target; the comparison and qualifying kernel remain open.

Exact checks cover 451,078 original-padding sites, including 20 previously omitted box rows now included. Outward reference checks include a Buchstab partition cross-check and 25,600 cells for the band reference. All 283 nonmutable checkpoint28 records and the frozen mass ledger are preserved. Original .003065/.007935/.011 budgets and any later xi or 21147/L charges remain; no rejected-candidate loss is added to the global allowance. K=0; milestone7 remains deferred.


## AJ. Direct coupled-degree lower kernel and its comparison source (checkpoint30)

COUPLED_DEGREE_KERNEL_NOTE.md defines lambda_p(v)=Lambda(v)1_(Pminus(v)>=p), nu_p(m)=(9/2)*(lambda_p*lambda_p*lambda_p)(m)/log(m)^3, and the fixed lift 1-(1-nu)^5. The convolution proves its own roughness/degree support and 0<=nu<=1, including repeated bases. The band kernel is globally pointwise below the actual Pminus(m)>=p, Omega(m)>=3 pool.

| Requirement | Result |
|---|---|
| Pointwise lower weight and degree support | Proved directly; no separate low-degree subtraction |
| Four-prime seed in the band | >=27/32+o(1); lifted relative deficit <=3125/33554432+o(1) |
| Normalized reference loss | <=(.000001+o(1))u |
| Actual short deficit | <=(.000033+o(1))u, via admitted rough upper constant <.348 |
| Actual centered pool minus kernel | In [-(.000001+o(1))u,(.000033+o(1))u] |
| Required actual centered kernel lower comparison | Unproved; coarse lower coefficient -.010008 only |
| Actual detector expansion | Five moments, four complete Vaughan detectors, all 405 signed terms retained |
| Ordinary two-free RS reduction | Fails continuously even in all-Type-I: R+2L-2<=c+2d-2<=2-5a<=0 |

The rough upper count uses actual bounded prime outer coefficients, fixed full level N^(1.249)/(2P), sifting cutoff P, exact squarefree support and a fixed .001 reserve. The ratio s lies in [819/430,849/400]. The finite source tolerance is retained before limsup_N and epsilon->0; no N-dependent source tolerance is applied. This controls the defect, not the centered kernel lower bound.

The reference enclosure width is not dropped: the defect uses the upper reference endpoint, and the remaining estimate is centered against the actual original normalized long count. The forward lower transfer charges only the .000001 reference loss, since the short defect has a positive sign. The conditional final coefficient retains .003065+.007825257+.000001+eta_W+eta_rest+xi+21147/L, with eta_W+eta_rest<=.000099. No original signed sector is discarded; original .011 is unchanged.

The precise next analytic goal is the centered weighted four-factor comparison in the new note (20). A first separate source task is the all-four-Type-I lattice-minus-product-integral error with all four free variables, physical gates, h_i<=N^(.002) and logarithmic weights retained. The tested reduction does not prove it o(u); no exclusion of other multilinear or whole coupled methods is made. The exact base and remaining pool bands are retained in eta_rest.

Checks cover 3,108 formal convolution/cutoff rows, 451,078 actual-padding sites with literal prime-log values, all 20 old-box rows with positive weight, 72 formal four-slot Vaughan fixtures and 288 source corners. These do not prove the required sharp comparison. All 291 nonmutable checkpoint29 records and the frozen historical mass ledger are preserved. K=0; milestone7 remains deferred.

Checkpoint30 source addendum: Theorem3 applied separately at each external frequency with three retained free factors also fails at the required top height. Its first-two-error maximum is >=(5*S_free+C_free+2*chi)/8>=523/500>1. All 576 additional corners are checked, for 864 source corners across the two reductions. Joint frequency/product estimates and other four-variable lattice methods remain untested possibilities; no source is asserted to supply the required bound.


## AK. Four-factor normalization and the remaining short comparison (checkpoint31)

FOUR_FACTOR_NORMALIZATION_NOTE.md combines all four A_U=I1+I2 slots before integration. The exact physical-variable density is a_U(t)=m_U*(log(t)-s_U)-l_U, with all 1/d and 1/(db) Jacobians retained. Long quantitative Möbius PNT gives arbitrarily strong logarithmic bounds on m_U and l_U+1. Thus a_U(t)=1+O_A(log(N)^(-A)) on the actual physical band.

| Requirement | Result |
|---|---|
| Exact all-Type-I continuum with original gates | Proved |
| Centered continuous contribution | o(u), proved using exact paired areas and bounded J derivative <4 |
| Normalized original-long all-Type-I lattice error | o(u), proved; unscaled envelope N^(801/500)*log(N)^12, normalized exponent 301/500 and margin 199/500 |
| Normalized-long signed Type-II aggregate | o(u), proved collectively; separate absolute subterm estimates not asserted |
| Actual short all-Type-I lattice error | Still unproved at scale u |
| Actual short aggregate of Type-II terms | Still unproved with the required coefficient |
| Precise remaining band input | L(psi_Y)+B(psi_Y)>=-(eta_W+o(1))*u |
| New nonvanishing normalization charge | 0 |

The complete expansion has 80 all-Type-I signed subterms and 325 signed subterms with at least one Type II, totaling 405 across five moments. The short comparison must retain their signs and coupling. The unrestricted d4 short-interval result's primary publisher abstract requires length large compared with sqrt(X)*log(X); at X=x/D and length Y/D the ratio tends to zero already at D=1. Only its direct stated range is rejected; the unavailable full article and other four-variable methods are not excluded.

No original least-prime or frequency sector is discarded. Keep .003065+.007825257+.000001+eta_W+eta_rest+xi+21147/L<=.011 and eta_W+eta_rest<=.000099. The earlier .000001 kernel charge is unchanged. All 299 nonmutable checkpoint30 records are preserved. K=0, the .007935/.011 targets and the exact base/rest comparisons remain open, and milestone7 remains deferred.

Verification checks 720 scalar Vaughan rows, 128 four-slot signed tensors (including negative and positive Type-II aggregates), 28 one-slot continuum densities and seven continuum tensor collapses, plus 540 exact coarea geometry rows and the rational J derivative bound. These are identity checks, not a proof of the remaining short estimate.


## AL. Sharp short-window attempt after full recombination (checkpoint32)

SHARP_SHORT_WINDOW_TEST_NOTE.md retains L(psi_Y)+B(psi_Y)=P(psi_Y)-C(psi_Y), recombining all 80/325 signed Vaughan subterms before estimation. The actual required lower bound, eta_W+eta_rest<=.000099 and original .011 allowance are unchanged. No improved actual deficit coefficient is obtained.

The tested primary source is Matomaki–Pandey–Pliego–Teravainen–Wang, arXiv:2610.09567v1, Definition2.2 and Lemma2.3. Its generic large-value profile admits tau=1/2, while its mean-value Proposition3.2 requires tau<1/2 and a strict positivity margin. The prime-supported coefficients do not match the refined free-character/log coefficient clause; no prime mask is dropped to use it.

At the common source level upsilon=3/10 the exact profile is K(b)=min(tau,max(3*b/5,tau-2*b/5)). All fixed mixed integer moments are included. On the sorted actual-prime box a in [.40,.43], b in [.45,.47], c in [.505,.525], d=2-a-b-c in [.575,.645], every mixed moment length is <=199/400 or >=201/400, and total degree>=3 has length>=3/5. Thus the best available generic profile is at least 301/1000, above the required 3/10. The resulting .001 power gap in x is in an upper envelope; no actual critical state or negative short discrepancy is shown to occur. The failure persists at tau=999/2000<1/2.

Ordinary long PNT and the retained Phi5 floor give the exact weighted reference lower certificate 1599278967/4556220006400>.000351>.000099 for this box. It cannot simply be omitted under the current budget. This certificate is not a full reference enclosure and is not added as a new error allowance. A separate elementary calculation gives |psi_Y_hat(1/2+it)|>=.9 on [N/2,N] for sufficiently large N; its phase is kept, and this block is not an omitted tail.

| Input | Status |
|---|---|
| Exact 80/325 coupling | Preserved before testing |
| Current generic mixed-moment strict margin | Fails continuously on the retained box |
| Omitting that physical box | Costs more than the entire remaining budget |
| Actual large-value states, sizes or signs | Not determined |
| Sharp short-window lower comparison | Unproved; no improved coefficient |
| Prime-specific joint or phase-sensitive source | Not excluded; not supplied |

Verification checks 2,500 exact profile rows, 69 mixed-moment families through degree4 and 552 physical corner cases. The infinite higher-degree family is handled analytically. All 305 nonmutable checkpoint31 records, original reference enclosures and the frozen mass ledger are preserved. Retain .003065+.007825257+.000001+eta_W+eta_rest+xi+21147/L<=.011; no original sector is discarded. K=0 and milestone7 remains deferred.


## AM. Dyadic centered prime-pair variance (checkpoint 33)

The actual first-pair blocks retain p,r prime, p<r, p in [N^.40,N^.43], and pr³<=X_+. Their product is <=N^(143/150)(1+o(1)). The residual width h=Y/(PR) has exponent at least 7/150. Using the existing Selberg square with radius floor(h^.25)<r gives a uniform actual second-count upper O_j(h/log N). Therefore the centered block variance is O_j(N²/(PR log⁴N)), with local diagonal O_j(N/log³N)=o of that scale. The required uniform little-o of the full variance, equivalently an upper little-o for its complete centered off-diagonal expression, remains open. The three centering terms are retained.

An all-center norm with arbitrary fixed logarithmic savings does not automatically imply the sampled variance: the reciprocal sample centers are separated at scale h², and an explicit zero-long-mean Lipschitz function can concentrate at all sample centers while satisfying such all-center norms. This is a functional transfer counterexample only, not actual prime data. Audited source clauses have no admitted complete mapping to this prime sample. No global exclusion of other dispersion adaptations is claimed. The .000099 comparison/rest budget, .000001 reference charge and original .011/.007935 allowances remain unchanged. No actual deficit coefficient is improved.
