# Estimating the actual cofactor overlap

Michael M. Ross's H(ϑ) campaign. Checkpoint 13, 7 October 2026.

**Result.** The overlap quadratic form has an explicit uniform upper bound with the actual coefficients. It falls short of the required logarithmic saving. Two further cancellation estimates do hold: the complete Type I range extends from outer exponent 9/8 to **113/100**, and a specified product region of Type II is uniformly negligible. Proper prime powers in the Type II Mangoldt slot are negligible as well. The remaining Type II term is a precise weighted truncated-Möbius covariance on the square-centered interval.

The uniform .011u estimate, separate higher-degree cap, positive prime coefficient K, and H(ϑ) remain unproved. No global impossibility claim about other arithmetic methods is made.

## 1. The actual coefficients simplify before Cauchy

Retain all campaign cutoffs:
\[
x=N^2,\quad J=[x-N/2,x+N/2]\cap\mathbb Z,\quad
Y=N+1,\quad u=\frac{N}{2\log N},\quad
z=N^{1/4},\quad U=V=\lfloor N^{1/100}\rfloor.
\]
N is even and sufficiently large. The frozen coefficient is
\[
c_N(d)=\mathbf1_{d\text{ prime},\ z\le d<N^{19/20}}
+\frac12\sum_{\substack{p,r\ge z\text{ prime}\\pr=d}}
\mathbf1_{pr\max(p,r)\le x}.
\]
Every prime factor of a supported d exceeds U. Put
\[
\gamma_N(d)=c_N(d)\frac{\log N}{\log(x/d)},\qquad
0\le\gamma_N(d)\le\frac32c_N(d).
\]
Checkpoint 11's logarithmic freezing gives
\[
B_N(J)=\frac1{\log N}
\sum_{b>U}\Lambda(b)\sum_k\alpha_N(k)\mathbf1_J(kb)+o(u),
\quad
\alpha_N(k)=\sum_{\substack{d\mid k\\k/d>U}}
\gamma_N(d)\beta_U(k/d).
\tag{1}
\]
For m>1,
\[
\beta_U(m)=\sum_{\substack{t\mid m\\t>U}}\mu(t)
=-\sum_{\substack{t\mid m\\t\le U}}\mu(t).
\]
For supported d|k, a divisor t≤U divides k if and only if it divides k/d. Thus β_U(k/d)=β_U(k) whenever k/d>1. If 1<k/d≤U, both values are zero. The case k/d=1 must be excluded: β_U(1)=0, while the negative truncated sum at 1 is −1. We obtain the exact identity
\[
\boxed{\alpha_N(k)=\beta_U(k)S_N(k),\qquad
S_N(k)=\sum_{\substack{d\mid k\\d<k}}\gamma_N(d).}
\tag{2}
\]

Contributing k satisfy k≤(x+N/2)/(U+1)<x. They have at most seven prime factors ≥z, counted with multiplicity. With r such factors, the possible prime outer weights sum to at most r, and the two-prime weights sum to at most r(r−1)/2. The actual square weight is only one half and obeys the same bound. The ordering and prime cutoffs can only decrease the sum. Hence
\[
\boxed{0\le S_N(k)\le\tfrac32(7+21)=42.}
\tag{3}
\]
This removes an additional unrestricted divisor-order loss. It does not say that β_U is bounded or multiplicative.

## 2. Uniform local moments of β_U

Define
\[
q(U)=\sum_{s,t\le U}\frac{\mu(s)\mu(t)}{[s,t]},\qquad
\alpha_U=\sum_{t\le U}\frac{\mu(t)}t.
\]
For every interval I of H consecutive integers greater than 1, expansion and counting multiples give
\[
\sum_{n\in I}\beta_U(n)=-H\alpha_U+O(U),\qquad
\sum_{n\in I}\beta_U(n)^2=Hq(U)+O(U^2).
\tag{4}
\]
The absolute floor errors are at most U and U². The interval's location does not enter. Also
\[
q(U)=\sum_{r\le U}\varphi(r)
\left(\sum_{\substack{t\le U\\r\mid t}}\frac{\mu(t)}t\right)^2\ge0.
\]
[Bretèche–Dress–Tenenbaum (2020), (1.2)](https://tenenb.perso.math.cnrs.fr/PPP/Sxz.pdf) supplies q(U)→L>0, hence q(U)≪1. The previously admitted long-interval Möbius estimate gives α_U=O(exp(−c√log N)), absorbing fixed logarithms. Since U²=o(Y), (4) proves, uniformly on the actual J,
\[
\boxed{\sum_{n\in J}\beta_U(n)=o(u),\qquad
\sum_{n\in J}\beta_U(n)^2=(L+o(1))Y.}
\tag{5}
\]
The first moment cancels, but the second moment stays positive. A vanishing unweighted β norm is unavailable. This statement does not lower-bound a weighted overlap energy.

## 3. Uniform bounds for the actual overlap quadratic form

For an integer Q≥U, write
\[
v_b=\sum_k\beta_U(k)S_N(k)\mathbf1_J(kb),\qquad
E_Q=\sum_{Q<b\le2Q}|v_b|^2.
\]
The exact Gram representation is
\[
E_Q=\sum_{k,l}\alpha_N(k)\overline{\alpha_N(l)}K_{N,Q}(k,l).
\]
With a=x−N/2 and f=x+N/2,
\[
K_{N,Q}(k,l)=\max\!\left(0,
\min\{2Q,\lfloor f/k\rfloor,\lfloor f/l\rfloor\}
-\max\{Q+1,U+1,\lceil a/k\rceil,\lceil a/l\rceil\}+1\right).
\tag{6}
\]
This retains the integer endpoints and every diagonal term.

Put h_Q=1+N/Q. For fixed b, the possible k form an interval of at most h_Q sites. By Cauchy, (3), and (4),
\[
|v_b|^2\le42^2h_Q\sum_{a/b\le k\le f/b}\beta_U(k)^2
\ll h_Q(h_Q+U^2).
\]
Summing over b proves the first bound below. Alternatively, interchange k and b after Cauchy: the enclosing k interval has length O(N²/Q), and each k has at most O(1+Q/N) incident b. Apply (4) to that interval. The result is
\[
\boxed{E_Q\ll(1+N/Q)
\min\!\left\{N+QU^2,\ (1+Q/N)(N^2/Q+U^2)\right\}.}
\tag{7}
\]
Constants are independent of N, Q and the small-divisor residue classes at the center. The actual sparse support, rather than arbitrary unrestricted α, supplies (3).

In particular,
\[
E_Q\ll N^2/Q\quad(U\le Q\le N/U^2),\qquad
E_Q\ll N\quad(Q\ge N\text{ in the contributing range}).
\tag{8}
\]
Indeed contributing b≤O(N^{7/4}/U), so QU²/N≤O(N^{3/4}U)=o(N). If Q≥N, then b>N and the window's width N/b is less than one. Distinct k,l cannot overlap: the kernel is exactly diagonal. That simplification does not estimate away the diagonal energy.

For prime b only, E_Q^(p)=Σ_{Q<p≤2Q,p>U}|v_p|². The fixed-b bound and the Chebyshev prime-count upper bound yield
\[
E_Q^{(p)}\ll\frac{(1+N/Q)(N+QU^2)}{\log(2Q)}.
\tag{9}
\]
In the lower range of (8), this is O(N²/(Q log(2Q))). Since Σ_{Q<p≤2Q}(log p)²≪Q log(2Q), Cauchy bounds a single normalized Type II block by O(N/log N)=O(u). Its constant is not .011, there are many blocks, and there is no vanishing factor. To obtain an o(u) absolute bound for one block from this argument would require, for example,
\[
E_Q^{(p)}=o\!\left(\frac{N^2}{Q\log(2Q)}\right).
\tag{10}
\]
The present estimates do not prove this. It is a limitation of this norm argument, not a necessary condition for the one-sided joint campaign target.

## 4. Proper prime powers in b are negligible

This is a new removal in the Mangoldt slot b, distinct from the earlier removal of proper prime powers in the full cofactor mb. By (2)–(3), β_U(k)≪_εN^ε, and the number of k incident to b, the proper-b contribution is at most
\[
\frac{O_\varepsilon(N^\varepsilon)}{\log N}
\sum_{\substack{U<b\le S\\b\text{ proper prime power}}}
\Lambda(b)(N/b+1),\qquad S\ll N^{7/4}/U.
\]
Checkpoint 10's elementary bounds give Σ_{b>U, proper power}1/b≪U^(−1/2) and #{b≤S:proper power}≪√S. Using Λ(b)≤log S≪log N proves
\[
\boxed{B_{\mathrm{proper}\ b}(J)
=O_\varepsilon\!\left(N^\varepsilon(NU^{-1/2}+\sqrt S)\right)=o(u).}
\tag{11}
\]
For example ε=1/1000 gives a leading bound O(N^{249/250}); the freezing error is also o(u). This absolute argument applies to every selected subset of (d,b).

## 5. The signed Type II estimate is a specific covariance

For a prime b=p>U, β_U(n/p)=β_U(n). Equations (1), (2), and (11) therefore give
\[
\boxed{B_N(J)=\frac1{\log N}\sum_{n\in J}
\beta_U(n)\mathcal W_N(n)+o(u),}
\tag{12}
\]
where the actual nonnegative weight is
\[
\mathcal W_N(n)=\sum_{\substack{p\mid n\\p>U\text{ prime}}}\log p
\sum_{\substack{d\mid n/p\\d<n/p}}\gamma_N(d).
\tag{13}
\]
The m>U condition is preserved: 1<m≤U gives common β value zero; m=1 is excluded by the proper-divisor condition.

For sufficiently large N, n∈J has at most eight prime factors ≥z. Thus Σ_{d|n}c_N(d)≤8+28=36. The sum of log p over distinct prime divisors of n/d is at most log(n/d), so
\[
0\le\mathcal W_N(n)
\le\sum_{d\mid n}\gamma_N(d)\log(n/d)
\le(36+o(1))\log N.
\tag{14}
\]
The last step uses n=x+O(N) and frozen γ: log(n/d)/log(x/d)=1+O(1/(N log N)). With (5), this proves the uniform full bound B_N(J)=O(N), without an N^ε divisor loss. It remains too large for the target scale u.

Any constant \(\bar{\mathcal W}_N=O(\log N)\), including the mean of the weights on J, can be subtracted by (5):
\[
B_N(J)=\frac1{\log N}\sum_{n\in J}
\beta_U(n)(\mathcal W_N(n)-\bar{\mathcal W}_N)+o(u).
\tag{15}
\]
Unweighted Möbius centering is complete. The open input is its covariance with the prime-divisor weight (13). Cauchy in n gives
\[
|B_N(J)|\le\frac{\sqrt{(L+o(1))Y}}{\log N}
\left(\sum_{n\in J}|\mathcal W_N(n)-\bar{\mathcal W}_N|^2\right)^{1/2}
+o(u).
\]
This route would need weight variance o(N) to prove o(u); no such bound is established. The joint one-sided estimate may instead use cancellation with the Type I core.

## 6. Optimized source coverage widens Type I

On an ordered prime-pair block put
\[
\sigma=\log_N(PR),\quad \alpha=\log_N\min(P,R),\quad
\Sigma=\sigma+\delta,
\]
where δ is the exponent of the remaining denominator product. Set ν=1/10000 and η≤max(0,Σ−1)+ν. With the smaller prime as the standalone reciprocal variable, the four RS margins are
\[
\alpha-(4\eta+2-2\Sigma),\quad
\Sigma-3\eta-\alpha,\quad \alpha-2\eta,\quad 2-\Sigma-\eta.
\tag{16}
\]
The six original FI6 margins are
\[
\begin{gathered}
(8\Sigma-7\eta-6)/7-\alpha,\quad
(6\Sigma-5\eta-4)/7-\alpha,\\
(5\Sigma-5\eta-2)/8-\alpha,\quad
(4\Sigma-5\eta-2)/5-\alpha,\\
\alpha-\eta,\quad (2-\Sigma-\eta)/2-\alpha.
\end{gathered}
\tag{17}
\]
These are the admitted phase and short-window transfer conventions of checkpoints 6 and 11; their source hypotheses are unchanged.

Consider the continuous polytope
\[
19/20\le\sigma\le113/100,\quad
1/4\le\alpha\le\sigma/2,\quad
\delta\ge0,\quad \Sigma\le1153/1000.
\tag{18}
\]
Use RS when Σ≤11/10. Above that, split at
\[
s(\Sigma)=\frac{15\Sigma-13}{14}+\frac{3\nu}{2}:
\quad\alpha\le s(\Sigma)\text{ uses FI6},\quad
\alpha\ge s(\Sigma)\text{ uses RS}.
\]
This is the midpoint between the RS lower edge 2Σ−2+4ν and the relevant FI upper edge (Σ+1)/7−ν. Splitting the low RS region at Σ=1 makes all margins affine. Exact rational evaluation at every vertex gives:

| Region | Engine | Vertex records | Minimum facet margin |
|---|---|---:|---:|
| Σ≤11/10 | RS | 14 | 31/625 |
| Σ≥11/10, α≤s(Σ) | FI6 | 10 | 3/5600 |
| Σ≥11/10, α≥s(Σ) | RS | 10 | 3/5600 |

These regions cover (18), including the shared boundaries, with fixed positive slack. Before choosing the rational cutoff the overlap condition is 13Σ<15−35ν; Σ≤1.153 is strictly inside it. This is a ceiling for this selected two-engine coverage, not for all arithmetic methods.

Above σ=9/8, the ordering gate is no longer automatic and must be separated. Retain it exactly as
\[
pr\max(p,r)\le x
\iff p^2r<x+\tfrac12\ \text{and}\ pr^2<x+\tfrac12.
\]
Use truncated Mellin inversion for both indicators and the outer-product cutoff, with half-integer thresholds for integer monomials. On bounded dyadic boxes a polynomially large truncation height makes every pointwise error an arbitrarily small power of N: the half-integer distance prevents an arbitrarily close threshold. Each integral has O(log N) coefficient mass. Its twists in p,r have bounded magnitude after taking a real part O(1/log N). Arbitrary complex bounded source coefficients accommodate those twists, and the collapsed other denominator slot retains fixed divisor order. The extra integrals cost fixed logarithms, absorbed by the positive margins.

For Type I, δ≤1/100 in the first term and δ≤1/50 in the second. With σ≤113/100, Σ≤1.15<1.153. Smooth logarithmic weights and signed boundary envelopes use the same separation and short-window transfer as checkpoint 11. Their freezing error and main-density centering were already uniform over the full support; low outer products retain the elementary proof. Consequently
\[
\boxed{R_{I,\,d\le N^{113/100}}(J)=O(N^{1-c})=o(u)}
\tag{19}
\]
for some fixed c>0, including the newly nonautomatic gate. This does not reach balanced d≈N^{4/3}.

The [primary RS Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf) allows the arbitrary bounded complex coefficients used here. Original FI1989 statements, frequency restrictions, and signed transfer remain as audited in FI_1989_AUDIT.md and JOINT_REMAINDER_NOTE.md, with the original PDF unchanged. No individual short cofactor prime-number theorem is assumed.

## 7. A signed Type II product region is negligible

Define the actual (d,b) index region
\[
\mathcal R_N=\{db\le N^{49/50}\}
\cup\{N^{19/20}<d\le N^{113/100},\ db\le N^{1143/1000}\}.
\tag{20}
\]
The second set has only two-prime outer coefficients. Let B_R be the actual Type II sum restricted to this region, retaining m>U and b>U.

Here db≤N^{1.143}, so m≫N^{.857}>U. Expand β_U(m) as its negative small-divisor sum, and put m=tℓ. The frozen numerator becomes
\[
-\sum_{(d,b)\in\mathcal R_N}\gamma_N(d)\Lambda(b)
\sum_{t\le U}\mu(t)\sum_{dtb\ell\in J}1.
\tag{21}
\]
Its integral part is −Yα_UΣ_Rγ_N(d)Λ(b)/(db). Absolute harmonic bounds make the final sum O((log N)^3), so the previously admitted α_U bound makes this main term o(u), even before external division by log N.

On the first set in (20), bound each floor error by one. There are O(N^{49/50}log N) integer pairs (d,b); t costs N^{1/100} and Λ(b) a logarithm. The error is O(N^{99/100}(log N)^C)=o(u).

On the second set, use the smaller outer prime as standalone variable and collapse the other prime with t,b into the other denominator slot. Its exponent satisfies
\[
\Sigma=\log_N(dtb)\le1143/1000+1/100=1153/1000.
\]
Thus every block lies in (18). Λ(b)/log N is bounded, and the collapsed coefficient has fixed divisor order. Mellin separation handles db's cutoff and the two ordering indicators as in Section 6. The raw floor-error power saving, including its signed smoothing envelopes, applies; fixed logarithms are absorbed. After division by log N in (1),
\[
\boxed{B_R(J)=o(u)}
\tag{22}
\]
uniformly for all sufficiently large even N. This uses the signed β expansion and reciprocal estimates, not a smaller positive Gram norm.

For illustration, the triprime portion includes b≤N^{.018} at d≤N^{9/8}, and b≤N^{.013} at d≤N^{1.13}, for d>N^{.95}. Smaller d blocks permit larger b under (20). Those examples are not replacements for the defining product conditions, and the estimate does not cover all b or all outer products.

## 8. The remaining joint inequality, retaining its changed weight

Let B_rem restrict B_N to (d,b)∉R_N. Let R_I,new be checkpoint 11's signed floor-error expression now restricted to d>N^{113/100}. Then
\[
\boxed{\Delta_2+\Delta_3=B_{\mathrm{rem}}(J)+R_{I,\mathrm{new}}(J)+o(u).}
\tag{23}
\]
The actual gated Type I core is N^{1.13}<d≤N^{4/3}. The remaining sufficient target is
\[
B_{\mathrm{rem}}(J)+R_{I,\mathrm{new}}(J)\le(.011+o(1))u.
\tag{24}
\]
It remains unproved.

The region removal makes the proper-divisor weight depend on b:
\[
S_{\mathrm{rem}}(k,b)=\sum_{\substack{d\mid k\\d<k}}\gamma_N(d)
\mathbf1_{(d,b)\notin\mathcal R_N}.
\]
Keeping a single b-independent α in the old Gram formula after removal would be incorrect. However 0≤S_rem≤42, so (7), (9), and the exact diagonal geometry still hold for the remaining rows by the same proofs.

The actual remaining covariance weight is
\[
\mathcal W_{\mathrm{rem}}(n)=
\sum_{\substack{p\mid n\\p>U\text{ prime}}}\log p
\sum_{\substack{d\mid n/p\\d<n/p}}\gamma_N(d)
\mathbf1_{(d,p)\notin\mathcal R_N}.
\tag{25}
\]
Prime-power removal is absolute on subsets, so (12) and (15) hold with this weight and B_rem. In numerator units the concrete remaining target is
\[
\sum_{n\in J}\beta_U(n)
(\mathcal W_{\mathrm{rem}}(n)-\bar{\mathcal W}_{\mathrm{rem}})
+(\log N)R_{I,\mathrm{new}}(J)
\le(.0055+o(1))N.
\tag{26}
\]
The bar can be the average of the nonnegative weights on J; its removal costs o(u).

Another exact formulation preserves the joint sign. No row with d>N^{1.13} is removed in (20). Vaughan's identity therefore gives
\[
B_{d>N^{1.13}}(J)+R_{I,\mathrm{new}}(J)
=A_{d>N^{1.13}}(J)-\int_{J_{\mathbb R}}G_{d>N^{1.13}}(v)\,dv.
\tag{27}
\]
Every non-prime-power cofactor cancels exactly between the three discrete Vaughan terms. In particular composite cofactors with small factors should not be charged separately by positive absolute bounds. Proper prime-power contamination in A is already o(u). Either (26), or the low-outer remaining covariance combined with the actual centered prime count in (27), is a sufficient next interface.

The present proof does not bound the covariance in (26), nor the balanced triprime count/floor core in (27). The positive β second moment, diagonal overlap, and O(u) estimates on selected blocks explain why the straightforward norm estimates fall short. They do not exclude a refined signed dispersion estimate.

## 9. Verification and admission

Run from the campaign directory:

    python3 src/cofactor_estimation.py

The script verifies the frozen checkpoint 12 and source hashes; the multiplicity constant (3); (2) as coefficients of independent outer weights; exact local moments (4); actual overlap/Gram identities and diagonal geometry; and joint high-outer composite cancellation as exact coefficients of log(prime). It certifies all **34 rational vertices** of the continuous source region, including the Σ=1 split. These checks verify identities and source applicability, not the unknown terminal estimate.

Six fixtures passed: N=100,200,1000,2000,10000,10000 with U=1,3,3,5,1,8 respectively. The U>1 fixtures are labeled stress tests: actual floor(N^{1/100}) at these finite N is still one, and the campaign truncation is unchanged. The run checked **200,898 coefficient identities, 53,118 overlap pairs, 24 Gram forms, and 1,827 joint core rows**, including 1,565 non-prime-power rows with exact cancellation. These are finite identity checks, not evidence for (24).

Finite diagnostics retain the actual c_N and frozen γ_N with outward interval logarithms. Rational proxy weights are used separately for independent exact Gram checks; their purpose and scope are labeled in the results. No new Lean replay is claimed, and 007's centered graph has not been identified with (25).

New files are results/cofactor_estimation.json, results/cofactor_facets.json, and results/cofactor_checks.json. Primary BDT and RS PDFs have unchanged byte hashes in sources/cofactor_estimation/SOURCE_MANIFEST.json. Earlier notes, scripts, source bytes, the 007 audit, and numerical ledgers are preserved.

Admit the coefficient identities, local moments, uniform Gram bounds, prime-power removal, covariance reformulation, enlarged Type I estimate (19), and product-region cancellation (22), with their stated hypotheses. No terminal prime comparison is admitted. The .011u bound, higher-degree companion, full inventory and mass optimization remain incomplete; no positive K is credited.
