# H(ϑ) campaign — checkpoint 4

Michael M. Ross · 5 October 2026

There is further progress with the existing ingredients. The main addition is a well-factorable remainder argument for small extracted products and, after Vaughan decomposition, for the **smaller** prime in a semiprime. It strengthens the root sieve, recovers a small positive Buchstab branch, and gives a smaller tail constant. It does not prove H(ϑ), or a positive lower coefficient K for S₁(N^ϑ).

The new analytic reductions are written below. Their inputs are the published Robert–Sargos theorem and a primary-source formulation of Iwaniec's well-factorable sieve. The original sources and the earlier notes remain frozen. The original paper's particular Fouvry–Iwaniec citation chain is still only partially audited; the argument here supplies a separate route to the tail estimate. The numerical program verifies the algebra and encloses the integrals; it does not prove the analytic estimates by sampling.

## 1. The outcome and the remaining gap

Keep N=2n, x=N², J=[N²−N/2,N²+N/2]∩ℤ, Y=N+1 and u=N/(2 log N). Use S_d(c)=∑_r 1_J(dr)1_{P⁻(r)≥N^c}, with P⁻(1)=∞. An exponent in an argument of S in this note is relative to N. Set b=1/4 and

\[
\mathcal R_\kappa=\sum_{N^b\le p<N^\kappa}S_p(\log_N p).
\]

Equivalently, the cutoff in each summand is the prime p itself. The exact identity is S₁(κ)=S₁(b)−ℛ_κ.

The derived root bounds are

\[
(L_0-o(1))u\le S_1(b)\le(U_0+o(1))u,
\quad L_0=\frac{16}{5}\mathcal L(5),\quad U_0=\frac{16}{5}\mathcal U(5),
\tag{1}
\]

where 𝒰(s)=sF(s)/(2e^{γ₀}) and ℒ(s)=sf(s)/(2e^{γ₀}). Conservative outward enclosures are

\[
4.4837637679<L_0<4.4837927631,
\qquad4.4994503253<U_0<4.4995361297.
\tag{2}
\]

This increases the earlier root lower coefficient 4 log 3≈4.3944491547 by more than .0893146. The original level-one upper coefficient is 4𝒰(4)≈4.5888827. The earlier conversational estimate of 4.54 for that cap was too low.

The separate smaller-prime tail calculation gives, for fixed 4/5<ϑ<1,

\[
T(\vartheta)\le(C_{\rm small}(\vartheta)+o(1))u,
\qquad C_{\rm small}(\vartheta)=\frac{16}{5}\log\frac{5-4\vartheta}{\vartheta}.
\tag{3}
\]

| ϑ | Frozen C(ϑ) | Derived C_small(ϑ) | m(ϑ)−C_small(ϑ), a planning budget |
|---:|---:|---:|---:|
| .950 | .897259298 | .747567524 | .352515935 |
| .970 | .512207285 | .460121257 | .599896753 |
| .990 | .163316334 | .157667357 | .862333310 |

The exact interval records, including the unrounded frozen constants, are in `results/negative_frontier_ledger.json`. The frozen benchmark is retained; equation (3) is an additional bound rather than an edit to the baseline.

At κ=.95, the following would suffice:

\[
\boxed{\quad\mathcal R_{.95}(N)\le(3.73+o(1))u\quad}
\tag{4}
\]

for every sufficiently large even N. Equations (1), (3) and (4) would give a prime lower coefficient greater than .0061962. The critical upper coefficient is enclosed in [3.7361962441,3.7362252393]. The reference value of ℛ_.95 is approximately 3.39159, so (4) permits an excess of about .3384u above that reference; the critical threshold permits about .3446u.

If the **frozen** tail benchmark C is kept as the race to beat, the strengthened root instead permits the sufficient upper target 3.58u: L₀−3.58−C(.95)>.00650. The original 3.49u target remains sufficient. Distinguish these two routes: 3.73 would close K>C_small; 3.58 would close K>C with the frozen C.

Neither new frontier target is proved. The available whole-frontier cap is ℛ_.95≤S₁(b)≤(4.499537+o(1))u. The root lower minus this cap is still negative, so the certified rough lower coefficient is **K=0**.

## 2. Source interface and the smaller-modulus issue

Lichtman, *A modification of the linear sieve, and the count of twin primes*, arXiv:2109.02851v2, Definition 2.1 and Theorem 2.10, gives the form needed here. A sequence λ of level D is well-factorable when every D=D₁D₂ admits λ=α*β, with each factor bounded by 1 and supported up to Dᵢ. Its upper and lower sieve remainders are finite sums of such sequences, with the usual F and f main terms and a controllably small fixed error. We use this theorem's sieve formulation, not its application to primes in arithmetic progressions.

Robert–Sargos, *Three-dimensional exponential sums with monomials*, Theorem 1, supplies the engine for phase h z'/(νw), with arbitrary bounded a(h,ν) and b(w). Products of a fixed number of variables can be collapsed with divisor-bounded coefficients. The four exponent conditions for a saving over a denominator block of exponent Σ′ are

\[
m_1>4\eta+2-2\Sigma',\quad
m_1<\Sigma'-3\eta,\quad
m_1>2\eta,\quad
\eta<2-\Sigma'.
\tag{5}
\]

Every analytic application below uses fixed positive margins; equalities in the calculation are limiting facets only.

The source requires the standalone monomial exponent α to satisfy α(α−1)≠0 and the other two exponents to be nonzero. Our standalone exponent is −1, and the other exponents are 1 and −1, so these requirements hold. Its phase parameter is X≈HN²/Q>1, where H is the frequency scale and Q the original denominator scale.

**Retain the sifting restriction.** The sieve theorem sums only over e|P(z). A generic well-factorable sequence need not preserve factorability after multiplication by this squarefree indicator. Let h_z(e)=1_{P⁺(e)<z}; this function is completely multiplicative, so multiplying both convolution factors by h_z preserves their product. The remaining squarefree condition satisfies

\[
\mu^2(e_1e_2)=\mu^2(e_1)\mu^2(e_2)
\sum_{q\mid e_1,\,q\mid e_2}\mu(q).
\]

For each q set e₁=q a and e₂=q b. The separate coefficients remain bounded; the free joint and standalone lengths each decrease by q, while the original phase parameter X is unchanged because the denominator contains q². In the four Robert–Sargos terms, summing the q-piece relative to the original bound produces respectively the factors

\[
q^{-5/4},\qquad q^{-7/4},\qquad q^{-3/2},\qquad q^{-2}.
\]

Their sums converge, including a sufficiently small fixed divisor loss. In the elementary type-I estimate the free Vaughan variable does not change and the number of outer modulus pairs decreases by q², again a summable factor. These observations apply also to the absolute-coefficient boundary envelopes below. Thus all new remainder statements hold with the exact e|P(z) restriction; this restriction has not been silently discarded. The same device covers a restricted set of sifting primes by replacing h_z with the corresponding completely multiplicative support indicator.

It is essential to retain the **full** sieve level. Write D=N^β, but suppose a modulus product block e≈E has actual exponent β′≤β. Put Δ=β−β′. If the chosen full-level factorization has D₂=N^s and D₁=N^{β−s}, every contributing dyadic box has actual second-factor exponent v satisfying

\[
\max(0,s-\Delta)+O(1/\log N)\le v\le s+O(1/\log N).
\tag{6}
\]

The lower bound follows from e=e₁e₂≈E and e₁≤D₁. It does not follow by declaring the truncated sequence λ(e)1_{e≈E} well-factorable at the smaller level E.

To put a fixed Vaughan group of exponent a together with e₂ in the standalone slot, let [l,U] be the allowed window from (5). In the closed geometry, use s=0 when a∈[l,U]. When a<l, choose

\[
s=l-a+\Delta.
\tag{7}
\]

Then the entire actual standalone range lies in [l,l+Δ], provided l−a≤β′ and U−l≥Δ. Small fixed perturbations of s give the strict margins. Modulus partitions are imposed before selecting the exact convolution representation of the fixed λ; their smooth product cutoffs are separated by Mellin inversion. Dyadic boxes intersecting that product block differ in exponent by O(1/log N), which the margins absorb. The representation may depend on a fixed outer/Vaughan block because each block is a linear functional of the same λ. It is not chosen separately for individual integers.

Choose the representation at the largest retained frequency: the RS windows widen and the elementary condition improves at all smaller frequencies. One representation therefore works for the full frequency sum and for its boundary envelopes. It is not replaced by a different absolute-coefficient envelope at each frequency.

This proves the smaller-modulus bookkeeping needed by the new reductions. The program encloses the full range in (6), rather than checking a freely chosen actual factor size.

## 3. From an exponential block to the sharp interval remainder

Here is the direct transfer argument used below, so the new bounds do not depend on fetching the original Fouvry–Iwaniec pipeline lemma.

Write r_k=∑_j1_J(kj)−Y/k. On a product block k≈Q, suppose the relevant factorized coefficient family, and the same family with its separate coefficients replaced by their absolute values, satisfy

\[
\left|\sum_{h\sim H}\sum_{\text{outer variables}}
 c(\text{outer variables}) e\!\left(\frac{hz'}k\right)\right|
\ll QN^{-c_0}
\tag{8}
\]

uniformly for z′ within O(Y) of x and all frequencies up to (Q/Y)N^{2σ}, for some fixed c₀>0 and sufficiently small σ>0. Fixed divisor losses and smooth dyadic weights are included in the saving.

View the integer interval J as the integer points of [N²−N/2−1/2,N²+N/2+1/2], whose real length is Y. Convolve its indicator with a nonnegative smooth kernel at width δ=YN^{-σ}. Poisson summation in j gives zero frequency Y/k and nonzero frequencies

\[
\frac1k\int_{\text{real interval}}
 e\!\left(-\frac{hz'}k\right) dz'
 \widehat\rho(\delta h/k).
\tag{9}
\]

The prefactor on the product box is O(Y/Q). Separate the smooth multiplier by Mellin inversion in δh/k, and separate smooth product cutoffs in the same way. A smooth logarithmic cutoff below all occurring arguments makes that inversion absolutely integrable; its cost is a fixed logarithmic or N^ε loss. Bounded complex twists preserve the available coefficient slots. Equation (8), integrated over z′, therefore bounds each retained frequency block by YN^{-c₁}. Beyond Q/δ times an additional small power of N, rapid decay of the kernel makes the tail negligible, choosing a sufficiently large fixed number of derivatives.

For signed coefficients, convolution alone does not sandwich the weighted count. Its discrepancy from the sharp indicator is supported in the two boundary strips of width O(δ). Majorize those strips with nonnegative smooth envelopes. For each exact factorization λ=α*β, bound this error using |α|,|β|, and absolute values of the other separated coefficients. The zero frequency costs O(δN^ε log^C N), and the nonzero frequencies obey (8) for those absolute coefficients. In Vaughan type-I pieces the free inner weight remains smooth under this replacement; type-II weights remain bounded. Thus the strip error is also O(YN^{-c₂}).

Blocks with Q≤N^{1−ε} can instead use |r_k|≤1 and a divisor bound. Frequencies for the remaining boxes exceed their formal top exponent Σ′−1 by only O(σ); take σ small relative to all the fixed margins in the applications below. The finite number of sieve components and the logarithmic number of partitions are harmless. Consequently the weighted sharp remainder is O(N^{1−c})=o(u).

This argument explicitly controls the signed smoothing error and the high-frequency tail. The zero-frequency main term retains Y=N+1. No comparison against an arbitrary bounded cofactor sequence is asserted.

## 4. General bounded outer coefficients

Let c_d be bounded coefficients on d≈N^γ with fixed 0≤γ<1, and let λ be well-factorable of level N^β. The preceding transfer gives

\[
\sum_d c_d\sum_e\lambda(e)r_{de}=O(N^{1-c})
\tag{10}
\]

whenever

\[
\gamma+\beta<\frac54,\qquad 2\gamma+\beta<2.
\tag{11}
\]

To verify this, place e₂ alone in the standalone slot and d e₁ in the joint slot. For an actual product block Σ′=γ+β′>1 and η≤Σ′−1, the limiting window is [2η,Σ′−3η]. At its worst frequency it is [2Σ′−2,3−2Σ′]. Condition 2γ+β<2 gives 2Σ′−2<β′, so the sieve factor can reach its lower edge. Writing ρ=5/4−γ−β>0, the width at that frequency is

\[
5-4\Sigma'=4\rho+4\Delta>\Delta.
\]

Use (7) with a=0. Every actual box allowed by its full-level factorization passes (5). Near Σ′=1, use the full lower edge max(2η,4η+2−2Σ′); the strict margins allow the small frequency extension required by smoothing. Lower product blocks use the floor bound. Collapsing d e₁ gives a bounded-divisor joint coefficient. This proves (10).

For a nonnegative outer family, applying the well-factorable upper and lower sieve is now valid. Its effective cofactor level is

\[
B_{\rm arb}(\gamma)=\min(5/4-\gamma,\,2-2\gamma),
\tag{12}
\]

with a small fixed loss. This is a weighted bilinear remainder statement; it does not raise the level for arbitrary unfactored sieve weights.

At γ=0 it supplies the root sieve at level N^{5/4−ε}, giving (1) as ε tends to zero after N tends to infinity. It also applies to the outer product of two ordered primes: encode their unique marking as a coefficient of d=pq, retaining repeated primes in the cofactor.

## 5. The actual prime coefficient permits a better level

For a family indexed by **untwisted primes** p≈N^γ, with a smooth dyadic partition, the cofactor level can be

\[
B_{\rm prime}(\gamma)=5/4-\gamma,
\qquad1/4\le\gamma\le1,
\tag{13}
\]

again with a fixed loss. This is not a statement for arbitrary bounded weights b_p on the primes.

For γ≤3/4, (12) already proves (13). For γ>3/4, use Vaughan's convolution identity with U=V=P^{1/3}. For completeness, with μ_U and Λ_V denoting the truncated functions,

\[
\Lambda=\mu_U*\log-\mu_U*1*\Lambda_V
+\Lambda_V+(\mu-\mu_U)*1*(\Lambda-\Lambda_V).
\tag{14}
\]

This follows from μ*1=δ₁ and log=1*Λ. On a block near P, the separate Λ_V term vanishes. The first two terms have a smooth free variable and outer Vaughan exponent 0≤μ≤2γ/3; in the last term both factors exceed P^{1/3}, and choosing the shorter gives γ/3≤μ≤γ/2. The coefficients have fixed divisor growth, absorbed with a smaller power margin. The smooth prime partition and removal of log p are separated by Mellin inversion, or retained as a smooth weight in the free variable.

Prime powers introduced by Λ have remainder contribution O(N^{β+γ/2+ε}). At β≤5/4−γ and γ≥3/4 this exponent is at most 7/8+ε, so the correction is o(u).

For type I, summing over the smooth k variable gives

\[
\sum_{k\sim K}e(hz'/(ck))\ll\Lambda_1^{1/2}K^{1/2}+\Lambda_1^{-1},
\]

where |f′|≈Λ₁ and f′ is monotone. The second derivative test handles Λ₁ bounded away from zero, with its second term absorbed into the first; the first derivative estimate handles small Λ₁. The exponent condition is

\[
3\eta+2\mu\le\beta'+3\gamma-2.
\tag{15}
\]

The Λ₁⁻¹ term contributes O(N^(2Σ′−2)) to the raw block and is smaller than N^Σ′ with a fixed margin, since Σ′<5/4. Thus (15), made strict, suffices for the elementary option.

Otherwise use the standalone group m_v e₂ or k e₂ in (5). Write β=5/4−γ−ρ and β′=β−Δ. At the top limiting frequency η=Σ′−1, the five coverage checks have the following nonnegative margins:

| Coverage check | Exact margin at the worst frequency |
|---|---|
| μ≤γ/2 fits below the RS upper edge | (1−γ)/2+2ρ+2Δ |
| γ/3+β′ reaches the RS lower edge | 1/12+(2/3)(1−γ)+ρ+Δ |
| Elementary range overlaps the first RS range | 2ρ+2Δ |
| The two RS ranges overlap | 1−γ+4ρ+4Δ |
| Last RS range reaches μ=2γ/3 | Same margin as the second row |

All margins improve for smaller η. These are algebraic identities, not a finite-box inference. The continuous standalone windows used in these checks are implemented by the full-level construction (6)–(7): their width is at least 4ρ+4Δ, enough to cover the possible Δ uncertainty in the actual sieve factor. Small perturbations preserve the strict saving, including the frequency extension for smoothing. The transfer in Section 3 proves the prime-family remainder bound at (13).

At γ=1, |A|−X for the prime cofactor family is also controlled by this argument, using the well-factorable unit weight. For γ<1 the direct floor calibration suffices. Thus the sieve main term may consistently use X=Y∑_p g(p/P)/p.

The interval checks can also be read without the table. For Σ′>1 and η≤Σ′−1, put l=2η, U=Σ′−3η, and E=(β′+3γ−2−3η)/2. The elementary type-I range is μ≤E. The two RS ranges in μ are [l−β′,U] and [γ−U,Σ′−2η]. At the top frequency E=1/2−β′>0. The third table row is E−(l−β′), the fourth is U−(γ−U), and the final row is (Σ′−2η)−2γ/3. They establish continuous coverage, with overlaps of fixed width when ρ>0. The type-II interval [γ/3,γ/2] lies in the first RS range by the first two rows. This covers the continuum; the rational examples in the program only check consistency.

## 6. Reverse the tail sieve to the smaller prime

For ϑ>2/3, every composite counted by S₁(ϑ) is a semiprime. For sufficiently large even N, its smaller prime q is ≤N and its larger prime is >N. Indeed, two factors ≤N−1 have product at most (N−1)²<min J, while a square near N² would require its prime base to be N; N is even. The slight endpoint difference between q>N^ϑ and q≥N^ϑ contributes at most O(N^(1−ϑ)+1)=o(u). Consequently S₁(ϑ) is the prime count plus this tail, up to a harmless convention at that cutoff.

On a nonnegative smooth block q≈N^a, ϑ≤a≤1, apply Section 5 with cofactor level β=5/4−a−ε and cutoff z=N^(β/2). The prime cofactor is larger than N and survives this sifting. Mertens' product and F(2)=e^{γ₀} give the block upper bound

\[
\frac{2Y}{\beta\log N}\sum_q\frac{g(q/N^a)}q+o(u).
\]

The error in each block has a power saving, uniform on the compact a range with fixed ε. Harmonic prime partial summation gives the limiting measure da/a. First sum a fixed fine exponent partition, then let its mesh and ε tend to zero after N tends to infinity. Smooth partitions can be enlarged at the final cutoff; their excess harmonic mass tends to zero. This yields

\[
\frac{T(\vartheta)}u\le
\int_\vartheta^1\frac4{a(5/4-a)}\,da+o(1)
=\frac{16}{5}\log\frac{5-4\vartheta}{\vartheta}+o(1),
\]

which proves (3) by the new reduction. The same positive block argument, restricted to κ≤a<ϑ, gives

\[
\sum_{N^\kappa\le q<N^\vartheta}S_q(\log_N q)
\le[C_{\rm small}(\kappa)-C_{\rm small}(\vartheta)+o(1)]u
\]

for fixed 4/5<κ<ϑ<1. This is an estimate of restricted blocks, not subtraction of global upper bounds.

The new constant is strictly smaller than the frozen one. The difference of their integral kernels is

\[
\frac{16}{(2-a)(5a-4)}-\frac{16}{a(5-4a)}
=\frac{16(a-1)(a-8)}{a(5-4a)(2-a)(5a-4)}>0
\]

for 4/5<a<1. Thus the frozen inequality also follows as a weaker consequence of this separate argument, while its original citation chain remains a separate, partially audited object. If full H(ϑ) were available, the equation m(ϑ)=C_small(ϑ) would move its conditional prime threshold to

\[
0.9195428694313932<\vartheta_*<0.9195428694313990.
\]

This is a conditional race threshold. It supplies no proof of H(ϑ).

## 7. Cost the negative frontier and the first signed restoration

Let β(t)=5/4−t, with a fixed loss in applications. The prime-family upper sieve gives the direct negative cost

\[
U_{\rm dir}(\kappa)=
\int_{1/4}^{5/16}\frac{4\mathcal U(\beta(t)/t)}{t\beta(t)}\,dt
+\frac{16}{5}\log\frac{3\kappa}{5/4-\kappa},\qquad\kappa>5/16.
\tag{16}
\]

For the first range sift to p itself. For the remaining range sift to the smaller of p and N^(β/2), so 2≤s≤3 and 𝒰(s)=1. The cutoff only decreases, giving a valid upper bound for the p-rough term. Harmonic partial summation supplies dt/t as in the tail calculation. Outward enclosures give

| κ | U_dir(κ) | Root lower minus U_dir(κ) |
|---:|---:|---:|
| .95 | [8.1723347213, 8.1723706735] | [−3.6886069055, −3.6885419583] |
| .97 | [8.4597809882, 8.4598169403] | [−3.9760531724, −3.9759882251] |

These costs are much smaller than the earlier one-step estimates, but the whole-frontier cap U₀ is stronger still. Combining the root lower with that cap leaves a gap of about −.015715u. Nonnegativity is the best rough lower bound obtained here.

The next Buchstab expansion is exact:

\[
\mathcal R_1=A_1-\mathcal R_2,\quad
A_1=\sum_{N^b\le p<N^\kappa}S_p(b),\quad
\mathcal R_2=\sum_{N^b\le q<p<N^\kappa}S_{pq}(\log_Nq).
\]

The positive second frontier can now be lower-sieved on the small triangle

\[
\tfrac14\le v<t,\qquad t+3v<\tfrac54,
\]

where v and t are the q and p exponents. Its outer product exponent is t+v≤3/4, so Section 4 applies at level β=5/4−t−v with a fixed loss. The lower sieve is positive when β/v>2 and is in its explicit logarithmic range here. It yields

\[
\mathcal R_2\ge(G-o(1))u,\qquad
G=\int_{1/4}^{5/16}\int_v^{5/4-3v}
\frac{4\log((5/4-t-2v)/v)}{tv(5/4-t-v)}\,dt\,dv.
\tag{17}
\]

Strict subtriangles are used first; their integral tends to (17). The finite arithmetic sum retains q<p and all repeated prime factors in the residual. The diagonal has zero integral mass but is not used to alter the arithmetic identity.

The numerical enclosure is

\[
0.14286441329549<G<0.14295344956727.
\]

This is a recovered lower contribution to a positive rough branch. It includes composite residuals and is not a short-interval prime lower estimate. The checkpoint-2 terminal prime region requires t+3v>2 and is wholly outside this new positive triangle.

There is an important accounting check: **do not add G on top of the direct frontier bound (16).** With the same levels, lowering A₁ at cutoff b and restoring (17) produces exactly the improvement already present when directly sifting the negative term at its larger cutoff. In normalized form,

\[
\frac{d}{dc}\left[\frac4\beta\mathcal U(\beta/c)\right]
=-\frac4{c(\beta-c)}\mathcal L((\beta-c)/c).
\]

Integrating this identity in c and then interchanging the ordered integrals equates G with the excess of the A₁ upper cost over the direct ℛ₁ upper cost. The program independently encloses both expressions and checks that the enclosures intersect. This prevents a false double credit of a positive branch.

## 8. A parity witness for the mass interface

Improving the mass bounds alone does not resolve the remaining target. The following explicit weighted sequence illustrates the limitation of that interface; it is not the actual indicator of J.

Set H=N²/(log(N²))^10 and B=[N²−H/2,N²+H/2]∩ℤ. With λ(m)=(-1)^Ω(m), take

\[
a_m^*=\frac YH(1+\lambda(m))1_B(m).
\tag{18}
\]

This sequence is nonnegative and gives weight zero to every prime. Its divisor sums have main term Y/d. Quantitative Liouville cancellation, following from the zero-free-region prime number theorem, gives for every fixed A, uniformly for d≤N^(5/4),

\[
r_d^*=O(Y/H)+O\left(\frac Yd(\log(N^2))^{10-A}\right).
\]

The two cofactor endpoints are ≥a constant times N^(3/4), so the logarithms in this estimate are comparable. Summing against any fixed divisor order τ_C(d) costs

\[
O(N^{1/4}\log^{10+C}N)
+O(Y\log^{10-A+C}N)=o(u)
\]

by taking A sufficiently large. The sequence therefore satisfies the asymptotic divisor axioms through the total level N^(5/4), and hence the one-sided sieve mass consequences used here. Weighted Buchstab identities remain exact. It does **not** satisfy the original individual integer floor bound, the stronger power-saving error, or the actual short support of J. The claim concerns the extracted o(u) mass interface.

For fixed ϑ>2/3, only semiprimes survive both the rough cutoff and the even-Ω factor in (18). Standard prime partial summation on the long carrier gives

\[
S_1^*(\vartheta)=(2t(\vartheta)+o(1))u,
\qquad t(\vartheta)=\log\frac{2-\vartheta}{\vartheta}.
\]

This model also respects the new tail bound: C_small(ϑ)>2t(ϑ), since their difference vanishes at 1 and

\[
\frac{d}{d\vartheta}[C_{\rm small}(\vartheta)-2t(\vartheta)]
=-\frac{12}{\vartheta(5-4\vartheta)(2-\vartheta)}<0.
\]

The same derivative proves compatibility with every restricted band C_small(κ)−C_small(ϑ). The weaker frozen bounds are compatible as well. The root lower sieve on this model implies

\[
\mathcal R^*_{.95}\ge(L_0-2t(.95)-o(1))u
>(4.2835968-o(1))u,
\]

so the model violates the desired 3.73 frontier target while satisfying the admitted asymptotic mass inequalities. Even an elaborate signed optimization built only from those inequalities cannot force a prime lower bound. This is a failure certificate for the interface, not a universal obstruction to methods that exploit the actual interval or stronger arithmetic correlations.

Tao's linear-sieve lecture constructs the corresponding Liouville examples and explicitly asks for the 1+λ variant. Equation (18), the level check, and compatibility with the campaign's tail constants are the application here.

The next estimate must use additional arithmetic information. A concrete sufficient version is equation (4), uniformly over all large even N with o(u) error. A positive lower comparison for the selected terminal prime term remains another possible ingredient, but its reference mass alone neither proves (4) nor closes the current signed design. The prime-free witness explains why retaining the actual coefficient structure is essential.

## 9. Proof status, reproduction and sources

| Item | Status at this checkpoint |
|---|---|
| Exact signed identities and whole-frontier cap | Proved arithmetic statements; finite checks included |
| Full-level factor choice for smaller modulus blocks | Derived continuously in Section 2 |
| Squarefree sifting support | Retained through the summable gcd expansion in Section 2 |
| Sharp-interval remainder transfer | Derived with smoothing, signed boundary envelopes and frequency tail in Section 3 |
| General outer and untwisted-prime remainder levels | Derived from the published RS theorem in Sections 4–5 |
| Strengthened root, smaller-prime tail and small positive R₂ triangle | Consequences of those reductions and the well-factorable sieve |
| Numerical constants | Outward interval enclosures; no reliance on floating quadrature tolerances |
| Upper frontier targets 3.73 and 3.58 | Unproved sufficient inputs |
| H(ϑ), positive K, and a prime in every J | Not proved |
| Complete adaptive branch optimization | Not completed; a mass-only interface has the explicit limitation above |

Run `python3 src/negative_frontier.py` from the campaign directory. The program uses only the standard library and reads the preceding signed reference ledger. Its default run uses 20,000 cells per unit for the normalized sieve delay equations, 20,000 interval cells per one-dimensional integral, and 384 cells per triangle coordinate. It checks 24,000 prime/Vaughan coverage examples and 1,314 general-outer examples using exact rationals, plus 15 finite arithmetic instances. These examples check the implementation, while the continuous inequalities and analytic proofs are in this note.

The sieve grid starts from exact constants and outward logarithms, then advances causally using the delay equations. The triangle is mapped to a rectangle with nonnegative gap 5/4−4v, avoiding interval evaluation of a logarithm below its admissible domain. Its two-dimensional enclosure is checked against the independent one-dimensional difference formula. The threshold is bracketed by rational bisection; target margins use the lower root endpoint and upper tail endpoint. The baseline manifest is checked before calculations.

The four new result files are `negative_frontier_coverage.json`, `negative_frontier_arithmetic.json`, `negative_frontier_ledger.json`, and `negative_frontier_parity_witness.json`. The archive contains the complete campaign, preserving the original sources and the three earlier research notes.

Primary sources used for the new reductions:

1. O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, J. reine angew. Math. 591 (2006), 1–20, equation (1.1) and Theorem 1. [Author-hosted full text](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf).
2. J. D. Lichtman, *A modification of the linear sieve, and the count of twin primes*, arXiv:2109.02851v2 (14 February 2024), Definition 2.1 and Theorem 2.10. [Full text](https://arxiv.org/pdf/2109.02851v2). The theorem restates the well-factorable sieve of Iwaniec; the argument here does not use Lichtman's prime-progression applications.
3. K. Matomäki and X. Shao, *Vinogradov's three primes theorem with almost twin primes*, arXiv:1512.03213v2 (6 January 2017), Lemma A.1. [Full text](https://arxiv.org/pdf/1512.03213v2). This additionally states the linear sieve for nonnegative weighted sequences with main parameter X, as used for the cofactor families and (18).
4. T. Tao, *254A, Supplement 5: The linear sieve and Chen's theorem* (29 January 2015), the Liouville parity examples and Exercise 7. [Author's lecture](https://terrytao.wordpress.com/2015/01/29/254a-supplement-5-the-linear-sieve-and-chens-theorem-optional/).

The original Iwaniec (1980) and Fouvry–Iwaniec (1989) full texts were not successfully retrieved. Their original citation chain is still marked partial in the registry. The new reduction is explicit about what it proves from the verified modern sieve formulation and Robert–Sargos, so the remaining frontier target is not being hidden inside a source citation.
