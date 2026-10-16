# One-prime residual degree pool: source and reference audit

Checkpoint 29 — Michael M. Ross's H(ϑ) campaign — 12 October 2026

**Decision: reject the primitive lower-sieve construction below.**
Extracting only the smallest prime removes checkpoint 28's geometric
exclusion. It does not make a single rough-cofactor lower sieve accurate
enough after the prime and semiprime cofactors are removed.

Give those two removals their exact counts and credit the exact unmarked
base in full. The full candidate still loses at least (.94+o(1))u of
normalized reference. Even the best deletion of unfavorable outer-prime
blocks loses at least (.18+o(1))u, including when the admitted level is
replaced by its more favorable limiting pricing ceiling 5/4. The allowed
total reference-loss/comparison budget is .0001u.

The rejection applies to one primitive rough linear-sieve lower weight
followed by separate exact or upper-majorant low-degree exclusions. It
does not exclude other one-prime weights or a direct coupled estimate of
the degree pool. No sharp .007935/.011 comparison, H(ϑ), or positive K is
proved.

## 1. Preserve the actual positive complement and its degree condition

Keep x=N², Y=N+1, u=N/(2 log N), z=N^(1/4), y=N^(19/20), even N,
κ=1/1000, the original H_1, a_N=Y/H_1, and ρ=H_1/x=N^(-o(1)).
The original prime-product mark is unchanged:

\[
c_N(d)=\mathbf1_{d\ {\rm prime},\ z\le d<y}
 +\frac12\sum_{pr=d\atop p,r\ge z\ {\rm prime}}
 \mathbf1_{pr\max(p,r)\le x},
\qquad q_N(n)=\sum_{dq=n,\ q\ {\rm prime}}c_N(d).
\tag{1}
\]

The auxiliary degree decomposition does not alter its half-weighted
diagonal. Let

\[
d_N(n)=\mathbf1_{P^-(n)\ge z}(1-\min\{1,q_N(n)\}),
\qquad \mathcal D_N(\psi)=\sum_n d_N(n)\psi(n).
\tag{2}
\]

Checkpoint 28, (21), gives the short arithmetic interface

\[
\mathcal D_N(\psi_Y)=S_N(\psi_Y;y)+\mathcal G_N(\psi_Y)+o(u),
\qquad
\mathcal G_N(\psi)=\sum_{p\ge z,\ p\ {\rm prime}}
 \sum_{m\atop P^-(m)\ge p,\ \Omega(m)\ge3}\psi(pm).
\tag{3}
\]

The sum selects the smallest prime once, even with repeated factors.
It counts exactly the rough integers of degree at least four. The
nonnegative repeated-three-prime correction is the inherited o(u).
The degree condition in (3) is essential: removing it would also count
marked semiprimes and marked three-prime integers.

For the candidate use the broad support x/2≤n≤3x/2 and put
\(A_N=(3x/2)^{1/4}\). Every contribution to the degree pool on this
support has p≤A_N. Define, for these p and m=n/p,

\[
\begin{aligned}
R_p(m)&=\mathbf1_{P^-(m)\ge p},\\
E_{1,p}(m)&=\mathbf1_{m\ {\rm prime}},\\
E_{2,p}(m)&=\mathbf1_{P^-(m)\ge p,\ \Omega(m)=2}.
\end{aligned}
\]

Here m>p, uniformly for large N. Consequently the exact identity is

\[
R_p(m)-E_{1,p}(m)-E_{2,p}(m)
=\mathbf1_{P^-(m)\ge p,\ \Omega(m)\ge3}=:G_p(m).
\tag{4}
\]

E_2 counts the canonical unordered semiprime once, including a square.
All repeated factors are retained in (4).

## 2. One explicit lower weight and its pointwise proof

Fix B=1249/1000. Partition the outer primes into disjoint dyadic boxes
[P,2P), P=2^jz. For each box take

\[
D_P=\frac{N^B}{2P},\qquad Z_P=2P.
\tag{5}
\]

There is no two-prime active gate. All z≤p≤A_N are included. For large
N, D_P≥Z_P throughout this physical domain; in limiting exponents
α=log_N p∈[1/4,1/2], its sieve ratio is (B−α)/α≥1.498.

Use the fixed source-normalized lower kernel from checkpoint 28:

\[
\ell_{D,Z}(m)=V(Z)\{f(s)-C\varepsilon\}
 -\sum_{e\mid P(Z)}\widetilde\lambda^-(e)
       \left(\mathbf1_{e\mid m}-\frac1e\right),
\quad s=\frac{\log D}{\log Z},
\quad V(Z)=\prod_{r<Z\atop r\ {\rm prime}}(1-1/r).
\tag{6}
\]

The primary input is
[Lichtman, arXiv:2109.02851v2, Theorem 2.10, (2.4)–(2.5), and (5.17)](https://arxiv.org/html/2109.02851v2).
Apply its fixed weights to singleton sets with g(e)=1/e, as derived in
checkpoint 28. Choose a fixed small ε>0 and a sufficiently large C≥0
for the source O(ε) term. This gives

\[
\ell_{D_P,Z_P}(m)\le R_p(m),
\tag{7}
\]

because Z_P≥p. The weights are fixed independently of the integer set.
No source application at ε=0 is used; every finite correction lowers
the candidate and worsens its reference loss.

For any fixed outer coefficients 0≤θ_p≤1, independent of n, define

\[
w_{N,\theta}(n)=\mathbf1_{P^-(n)\ge y}
 +\sum_{z\le p\le A_N,\ p\ {\rm prime},\ p\mid n}
 \theta_p\left\{\ell_{D_P,Z_P}(n/p)
             -E_{1,p}(n/p)-E_{2,p}(n/p)\right\}
\tag{8}
\]

on the broad support, and set it to zero outside. The explicit full
candidate has θ_p=1. The other θ_p cover deletions and convex weighting
of prime blocks.

By (4) and (7), each bracket is ≤G_p(m), and G_p≥0. Multiplication by
θ_p∈[0,1] preserves that upper bound. Summing G_p selects one smallest
prime and counts every rough degree≥4 integer once. The y-rough base
has degree at most two on this support, since y³≫x. The base and higher
degree pool are disjoint and carry no original mark. Therefore

\[
\boxed{w_{N,\theta}(n)\le d_N(n).}
\tag{9}
\]

This holds throughout the broad support, hence on both the short padding
and the original long reference. It is a pointwise construction, not a
proved short-versus-long comparison.

The exact exclusions in (8) make this an optimistic benchmark for the
separately priced family. Replacing either by a pointwise upper majorant
can only decrease the weight and its long mean.

## 3. Source coverage: what is admitted and what remains unproved

The primitive rough-sieve component has γ=α, β=B−α. Its limiting source
domain has two endpoints:

| α | β | s=β/α | 2−2γ−β |
|---|---|---|---|
| 1/4 | 999/1000 | 999/250 | 501/1000 |
| 1/2 | 749/1000 | 749/500 | 251/1000 |

Thus γ<1, β>0, γ+β=B<5/4, with fixed reserve 1/1000. The older RS
route also has 2γ+β<2 throughout. Box endpoint constants and p≤A_N
perturb exponents only by O(1/log N).

The prime indicator and θ_p form the actual bounded outer coefficient.
They are not declared a free prime slot. The inner remainder is a finite
sum of fixed full-level WF components; its exact squarefree sifting
support is retained. FI_1989_AUDIT.md, Section 5, and the inherited signed
transfer therefore admit the rough-sieve remainder. Its scalar term has
only O(N^(1/2+o(1))) divisibility floor error, which is o(u).

| Actual term | Source status |
|---|---|
| Primitive rough-cofactor lower sieve, including θ_p | Admitted power-saving comparison |
| Exact prime exclusion E_1 | Required centered upper comparison remains unproved |
| Exact semiprime exclusion E_2 | Required centered upper comparison remains unproved |
| Exact y-rough base | Required centered lower comparison remains unproved |
| Coupled degree pool G | No comparison is inferred from the rough remainder |

E_1 and E_2 impose actual prime conditions on the integer cofactor. The
WF divisibility theorem does not automatically estimate these masks.
A joint estimate could control their coupling instead of estimating them
separately. The reference test below fails even if all three missing
comparisons were perfect, so they are not pursued for this candidate.

## 4. Price the reference with exact low-degree exclusions

All references use the original long width ρ. After fixing the outer
prime, the cofactor has size N^(2−α) and the same relative long width.
The inherited ordinary PNT is valid uniformly on these fixed positive
prime scales. It is not a short-interval PNT assertion.

Put

\[
\mathcal L(s)=\frac{sf(s)}{2e^{\gamma_0}},\qquad
\mathcal L(s)=0\ (1\le s\le2),\qquad
\mathcal L(s)=\log(s-1)\ (2\le s\le4).
\tag{10}
\]

The most favorable primitive lower-sieve density, before division by
log N, is 2L((B−α)/α)/(B−α). Prime cofactors have density 1/(2−α).
For the canonical semiprime cofactor r≤q, r≥p, partial summation gives

\[
\int_\alpha^{(2-\alpha)/2}\frac{dt}{t(2-\alpha-t)}
=\frac1{2-\alpha}\log\frac{2-2\alpha}{\alpha}.
\]

Hence the favorable net cofactor price is

\[
h_B(\alpha)=
\frac{2\mathcal L((B-\alpha)/\alpha)}{B-\alpha}
 -\frac{1+\log((2-2\alpha)/\alpha)}{2-\alpha}.
\tag{11}
\]

The factor from the outer prime and the normalization Y/u is
2dα/α. The exact base is credited with its full smoothed reference

\[
c_{\rm base}=(1+\kappa)\{1+\log(21/19)\}.
\tag{12}
\]

The candidate's best finite-tolerance mean is bounded above by

\[
c_{\rm base}+(1+\kappa)J_B,
\qquad J_B=2\int_{1/4}^{1/2}\frac{h_B(\alpha)}\alpha\,d\alpha.
\tag{13}
\]

The centered sieve remainders have zero long main. Their normalized
elementary floor envelope is
O(N^(B−1)ρ^(-1)(log N)^C)=o(u). The factor-two sifting endpoint changes
exponents by O(1/log N), giving o(u) in these reference formulas.
Finite Cε corrections only reduce (13).

For clarity, the ordinary long degree partition also has negligible
corrections. Repeated factors have normalized envelope
O(N/z+ρ^(-1))=o(u), as in checkpoint 27, (17). A squarefree three-prime
row failing the smallest-pair gate must have its second prime in a
relative O(ρ) band about sqrt(x/p), and its third in the same relative
band. Ordinary long PNT bounds their total by O(ρ²x/(log N)²);
normalization gives O(Nρ/(log N)²)=o(u). Thus subtracting the base from
the preserved positive complement reference leaves exactly the ordinary
higher-degree reference, up to o(u).

Outward interval integration with 12,000 cells per one-dimensional
integral gives:

| Unscaled component | Certified enclosure |
|---|---|
| Primitive rough lower mean | [1.29687482914878, 1.29715649151644] |
| Exact prime exclusion | log(7/3) = .84729786038720… |
| Exact semiprime exclusion | [1.07182765175302, 1.07198683535809] |

For θ_p=1 the favorable full candidate mean is in
[.47815126555243,.47859255237113]. The preserved smoothed complement
reference is in [1.42812738782223954808,1.42816857732647018189]. Its
favorable loss is therefore in

\[
[.94953483545111,\ .95001731177404].
\tag{14}
\]

In particular every fixed-tolerance full candidate (8) satisfies

\[
a_N\{\mathcal D_N(\psi_{H_1})-\mathcal W_{N,1}(\psi_{H_1})\}
\ge(.94+o(1))u.
\tag{15}
\]

The enclosures describe favorable tolerance-free pricing bounds. They
are not upper bounds on every finite implementation's loss.

## 5. The best prime-block deletion still fails

For any 0≤θ_p≤1, its reference contribution is at most the positive
part of (11). This permits optimal deletion of every unfavorable block:

\[
J_B^+=2\int_{1/4}^{1/2}\frac{\max\{0,h_B(\alpha)\}}\alpha\,d\alpha.
\tag{16}
\]

The positive part is taken only in the reference price. It is not a
claim that clipping the integer weight preserves the source transfer.
Uniform long PNT for the exact counterweights and bounded θ_p makes the
price ceiling valid even for arbitrary individual prime coefficients.

For B=1.249 the certificate gives

\[
J_B^+\in[.14326005054826,.14338664277698],
\]

and the corresponding favorable loss is in
[.18341381638694,.18358172471212].

Allow the strictly more favorable pricing ceiling B_0=5/4. On [2,4],
f(s)/(2e^(γ_0))=log(s−1)/s is increasing: its derivative's numerator
is s/(s−1)−log(s−1)≥4/3−log3>0. On [1,2] it is zero. Consequently
every admitted smaller level has a primitive lower mean bounded by
the B_0 price. This is an optimistic numerical ceiling, not a source
application at γ+β=5/4.

At this ceiling,

\[
J_{B_0}^+\in[.14375657898941,.14388360653739],
\]

and the best possible loss in this family is bounded below by the lower
endpoint of

\[
[.18291635566278,\ .18308469974253].
\tag{17}
\]

Thus the whole family, including lower admitted levels, block deletions,
convex prime weighting, finite source tolerances, and upper majorants
in place of the exact exclusions, satisfies

\[
\boxed{\eta_{\rm loss}\ge .18,\qquad
        \eta_{\rm loss}+\eta_{\rm err}>.0001.}
\tag{18}
\]

This rejects the specified minorant-transfer route with a nonnegative
comparison-error allowance. A positive short-window excess large enough
to compensate for this loss would itself be an additional analytic
input. Refining numerical quadrature or improving a vanishing WF
remainder cannot supply it.

## 6. The old omitted box is covered but its least-prime band is unpriced

The checkpoint-28 four-prime box has
α_1∈[.40,.43], α_2∈[.45,.48], α_3∈[.50,.53], and
α_4=2−α_1−α_2−α_3∈[.56,.65]. The full one-prime pool contains it;
there is no 8PR² gate in (8).

Nevertheless h_(5/4)(α)<0 throughout [3/8,1/2]. Indeed on this band,

\[
\frac{2\mathcal L((5/4-\alpha)/\alpha)}{5/4-\alpha}
\le\frac{2\log(4/3)}{3/4},\qquad
\frac{1+\log((2-2\alpha)/\alpha)}{2-\alpha}
\ge\frac{1+\log2}{13/8}.
\tag{19}
\]

The right-side difference is at least .27478453329367. These inequalities
also cover smaller levels by the monotonicity used above.

Since θ_p≥0, the candidate's entire normalized contribution from this
least-prime band is nonpositive. The true degree pool is positive there.
Pointwise (9) prevents its deficit from being canceled by overcounting
other prime blocks. In particular the old box alone still forces the
independent reference deficit

\[
\frac{693}{911600}=.000760201842913558\ldots>.0001.
\tag{20}
\]

Unlike checkpoint 28, this is not a claim that the full candidate is
zero on each integer in the box. It is a reference-pricing obstruction
for its whole least-prime band. Deleting that band makes its candidate
weight zero there; retaining it gives nonpositive net reference credit.

## 7. A concrete coupled test block and the missing estimate

The audit identifies a specific next object, rather than another use of
the rejected primitive lower sieve. Keep the degree condition together:

\[
\mathcal G_{[.40,.43]}(\psi)=
\sum_{N^{.40}\le p\le N^{.43},\ p\ {\rm prime}}
 \sum_{m\atop P^-(m)\ge p,\ \Omega(m)\ge3}\psi(pm).
\tag{21}
\]

Its ordinary long main consists of four-prime integers. For α>.40
the remaining cofactor has degree at most three at product x; the
degree-five boundary and repeated factors are o(u). With
q=(2−α)/α∈[157/43,4], Buchstab's equation gives

\[
q\omega(q)-1-\log(q-1)
=\int_1^{q-2}\frac{\log v}{v+1}\,dv.
\]

Consequently the exact leading smoothed reference is

\[
M_{[.40,.43]}=(1+\kappa)\,
2\int_{.40}^{.43}\int_1^{2/\alpha-3}
 \frac{\log v}{\alpha(2-\alpha)(v+1)}\,dv\,d\alpha,
\tag{22}
\]

certified by 25,600 outward cells to lie in

\[
[.00980703333218,\ .01000715975262].
\tag{23}
\]

For the possible degree-five long boundary, every prime lies in a
relative O(ρ) interval about N^(.40). Ordinary PNT and the resulting
five-prime tuple envelope, after normalization, give
O(Nρ^4/(log N)^5)=o(u). This justifies the four-prime main in (22).
No positive short mass is credited by (23).

A useful new kernel must target G_p itself, or a direct argument must
prove a one-sided centered estimate such as

\[
\mathcal G_{[.40,.43]}(\psi_Y)
 -a_N\mathcal G_{[.40,.43]}(\psi_{H_1})
\ge-(\eta_{\rm band}+o(1))u.
\tag{24}
\]

The remainder of the degree pool and the exact base must be controlled
with a combined charge η_rest, retaining η_band+η_rest≤.0001.
A successful band estimate alone would not complete the original target.
Equation (24) is unproved. The admitted rough-WF estimate in Section 3
does not supply it because it discards the joint degree information.

This is the next explicit analytic test: **a lower weight for the
coupled pool (21), or its actual centered lower comparison (24)**.
It includes the known four-prime box and has the certified reference
(23). The present audit supplies no successful replacement kernel.

## 8. Frozen coefficient ledger and verification

The sufficient original budget remains

\[
.007825257+\eta_{\rm loss}+\eta_{\rm err}
 +\xi+21147/L\le .007935,
\tag{25}
\]

and its final original coefficient remains
.003065+.007825257+η_loss+η_err+ξ+21147/L≤.011.
Here ξ is the checkpoint-22 (23) charge if a fixed least-prime sector
is later discarded, and 21147/L is the checkpoint-25 fixed-transform
tail charge. Neither is introduced by this audit. The fixed outer-prime
band in (21) does not discard any original signed least-prime sector.
The rejected reference losses are not added to the global allowance.

Run `python3 src/one_prime_degree_pool_audit.py`.
The exact checks retain the original cutoffs, original canonical mark
weights, repetitions, and physical one-prime gates. They cover 451,078
short-padding sites, including 20 formerly omitted four-prime-box rows
now included in the degree pool. They test the arithmetic upper envelope
used in the pointwise proof, not literal numerical Iwaniec weight values.

Outward interval arithmetic certifies (14), (17), (19), and (23). An
independent Buchstab check verifies consistency of
8ω(8)−4ω(4) with the prime, semiprime, and higher-degree reference
partition. The 5/4 endpoint is used only for favorable pricing.
All 283 nonmutable checkpoint-28 records and the frozen historical
mass ledger are unchanged.

The original .007935/.011 comparison, the positive complement sharp
lower comparison, H(ϑ), the optional marked estimate, and a qualifying
degree-pool lower weight remain open. K=0; milestone 7 remains deferred.
