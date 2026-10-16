# A partial logarithmic saving for the stopped covariance

Checkpoint 17 — Michael M. Ross's H(ϑ) campaign — 8 October 2026

The next analytic step gives a uniform improvement of the actual stopped
covariance from O(N) to
\[
\boxed{\displaystyle
 |\mathcal C_N|\ll\frac{N}{(\log N)^{\delta/2}},\qquad
 \delta=1-\frac{1+\log\log2}{\log2}=0.086071332\ldots .}
\tag{1}
\]
Thus the exponent in (1) is 0.043035666… . The argument preserves the
actual power truncation, all prime ordering and product gates, and the
positive prime-cofactor core. It combines a divisor-pairing identity with
a uniform nonnegative multiplicative-function upper bound, then uses the
previously proved second moment of the actual β weight.

This is a partial analytic estimate. It does **not** prove the required
\(\mathcal C_N\le(M_C+.011+o(1))u\), where \(u=N/(2\log N)\).
The reference enclosure for M_C, the historical mass ledger, and K=0
are unchanged. H(ϑ) and the separate higher-degree allocation remain open.

## 1. Actual input and the new intermediate bound

Use the checkpoint 16 definitions without altering their coefficients:
\[
x=N^2,\quad J=[N^2-N/2,N^2+N/2]\cap\mathbb Z,\quad
U=\lfloor N^{1/100}\rfloor,\quad z=N^{1/4},
\]
\[
\mathcal P_N=\{p\text{ prime}:z\le p<N^{19/20}\},\quad
I_p=\{k:pk\in J\},\quad H_p=\#I_p=N/p+O(1).
\]
All asymptotic claims are for every sufficiently large even N, uniformly
in the actual p. For k>1 the coefficient is
\[
\beta_U(k)=\sum_{d\mid k,\ d>U}\mu(d)
=-\sum_{d\mid k,\ d\le U}\mu(d),\qquad \beta_U(1)=0.
\tag{2}
\]
It is neither multiplicative nor necessarily bounded by one.

Let v_p and P_p be exactly the continuation and complementary core
weights in WEIGHTED_STOPPING_NOTE.md, (16) and (18), and set Z_p=v_p−P_p.
In particular, retain the r≥p, pr²≤x, D_good/C, db>N^(459/400),
prime-b, and nonunit-cofactor tests in those definitions. The inherited
results are
\[
|Z_p(k)|\le37,\qquad
\sum_{k\in I_p}\beta_U(k)^2\ll H_p,
\qquad\sum_{p\in\mathcal P_N}H_p\ll N,
\tag{3}
\]
and, with the actual local means,
\[
\mathcal C_N=\sum_p\sum_{k\in I_p}
(\beta_U(k)-\bar\beta_p)(Z_p(k)-\bar Z_p)
=\sum_p\sum_{k\in I_p}\beta_U(k)Z_p(k)+o(u).
\tag{4}
\]
The second estimate in (3) follows from H_p q(U)+O(U²), q(U)→L>0,
and U²/H_p≪N^(−3/100). The centering error in (4) is
O(N exp(−c√log N)+N^(24/25))=o(u). These are prior analytic inputs,
not consequences of the finite checks in this checkpoint.

The new intermediate result is support sparseness on each full stop:
\[
\boxed{\displaystyle
 S_p:=\#\{k\in I_p:\beta_U(k)\ne0\}
 \ll \frac{H_p}{(\log U)^\delta}.}
\tag{5}
\]
The full-interval quantifier matters: no conditional prime pattern or
selected-subset moment estimate is being assumed.

## 2. Uniform analytic input and interval sizes

We use the deterministic, all-interval Shiu bound in the explicitly
uniform divisor-bounded form of Mangerel (2023), Lemma 3.2. Its relevant
content is the following. If f is multiplicative and
\(|f(n)|\le\tau(n)\) for n≤X, and
\(\sqrt X<Y\le X\), \(Y^\eta\le y\le Y\), then
\[
\sum_{Y-y<n\le Y}|f(n)|
\ll_\eta y\prod_{r\le X,\ r\ {\rm prime}}
\left(1+\frac{|f(r)|-1}{r}\right).
\tag{6}
\]
The constant is uniform over the entire family of functions under that
divisor bound. In our applications f is nonnegative, f(r)≤2, and (6)
is at most
\[
\ll_\eta y\exp\left(\sum_{r\le X}\frac{f(r)-1}{r}\right).
\tag{7}
\]
Use the usual uniform Mertens estimate
\(\sum_{r\le T}1/r=\log\log T+O(1)\), T≥2. All sums indexed by r in
this analytic section are over primes. We never apply (6) directly to β.

The newly scaled intervals have k=qdm, where q≤Q:=⌊U^(1/4)⌋ and d≤U.
Thus qd≤U^(5/4)≤N^(1/80). Write a=log_N p and s=log_N(qd). The m
interval has upper endpoint of order N^(2−a−s) and real width
N^(1−a−s). Uniformly on a≤19/20 and s≤1/80,
\[
1-a-s-\frac{2-a-s}{30}
=\frac{28-29(a+s)}{30}\ge\frac7{2400}>0.
\tag{8}
\]
Consequently the number of consecutive m sites is comparable to
H_p/(qd) and exceeds its upper endpoint to the power 1/30 for all
sufficiently large N. Integer rounding and the constants in the
endpoint comparison are absorbed by the fixed margin in (8).
Taking X=2Y at that upper endpoint meets √X<Y≤X. Also U is below
that endpoint with a fixed power margin: 2−a−s≥83/80>1/100.
Unscaled I_p satisfies the same conditions. Dyadic d intervals below
have length comparable to their endpoint and also qualify for (6).

Only this all-interval upper bound is admitted from the new source.
The almost-all results elsewhere in Mangerel's paper are not inputs at
the fixed center N². Neither a global divisor-count estimate subtracted
at two endpoints nor a moving-intercept correlation theorem is used.

## 3. Pairing at a small prime

For any prime q dividing k>1, pair squarefree divisors with and without q
in the short sum (2). This gives the exact identity
\[
\beta_U(k)=-\sum_{\substack{d\mid k,\ q\nmid d\\U/q<d\le U}}\mu(d).
\tag{9}
\]
In particular, if β_U(k)≠0 and q=P⁻(k)≤Q, at least one squarefree
divisor d satisfies
\[
U/q<d\le U,\qquad P^-(d)>q,\qquad k=qdm,\qquad P^-(m)\ge q.
\tag{10}
\]
The convention P⁻(1)=∞ applies. Neither m nor k has to be squarefree.
In particular gcd(d,m) can exceed one, and q can divide m. These cases
must be retained in the subsequent weights.

Put
\[
\lambda=\frac1{\log2},\quad t=\frac\lambda2,\quad
K=\lambda\log\log U,
\qquad 1<\lambda<2,\quad\tfrac12<t<1.
\tag{11}
\]
Write ω_U(k) for the number of **distinct** prime divisors of k not
exceeding U. Partition the support into three sets:

1. P⁻(k)>Q;
2. P⁻(k)≤Q and ω_U(k)>K;
3. P⁻(k)≤Q and ω_U(k)≤K.

The bounds below may overcount the second set by dropping its least-prime
test. All overcounts are nonnegative.

## 4. Rough numbers and the high prime-count set

The rough indicator \(\mathbf1_{P^-(k)>Q}\) is multiplicative and at most
one. Applying (6) and Mertens gives
\[
\#\{k\in I_p:P^-(k)>Q\}\ll H_p/\log Q\ll H_p/\log U.
\tag{12}
\]
For the second set use \(f(k)=\lambda^{\omega_U(k)}\).
This is nonnegative and multiplicative, and
\(f(k)\le2^{\omega(k)}\le\tau(k)\). Its prime value is λ for r≤U
and one otherwise. Hence
\[
\sum_{k\in I_p}\lambda^{\omega_U(k)}
\ll H_p(\log U)^{\lambda-1}.
\]
Markov's inequality gives
\[
\#\{k\in I_p:\omega_U(k)>K\}
\ll H_p(\log U)^{\lambda-1-\lambda\log\lambda}
=H_p(\log U)^{-\delta},
\tag{13}
\]
where δ=1−λ+λ log λ is the positive constant in (1).

## 5. The low prime-count set, including all overlaps

For squarefree d and q as in (10) define the multiplicative function
\[
g_{d,q}(m)=\mathbf1_{P^-(m)\ge q}
t^{\omega_U(m)-\omega(\gcd(m,dq))}.
\tag{14}
\]
The exponent is nonnegative because every prime of dq is at most U.
For any j≥1 its prime-power values are
\[
g_{d,q}(r^j)=
\begin{cases}
0,&r<q,\\
1,&r\mid dq,\\
t,&q<r\le U,\ r\nmid d,\\
1,&r>U.
\end{cases}
\tag{15}
\]
Thus 0≤g≤1 uniformly in the moving d,q,U. On the eligible m,
\[
t^{\omega_U(qdm)}=t^{1+\omega(d)}g_{d,q}(m).
\tag{16}
\]
The subtraction of ω(gcd(m,dq)) in (14) is what prevents double
counting shared prime factors. No coprimality or independence assumption
is made.

If ω_U(k)≤K then 1≤t^(−K)t^(ω_U(k)). The existence assertion (10)
therefore bounds the third support set by
\[
t^{-K}\sum_{q\le Q}\sum_{\substack{U/q<d\le U\\
\mu^2(d)=1,\ P^-(d)>q}}
t^{1+\omega(d)}\sum_{m:qdm\in I_p}g_{d,q}(m).
\tag{17}
\]
Apply (6) to the inner interval, justified uniformly by (8). The prime
sum in (7), up to an absolute additive constant, is
\[
-\sum_{r<q}\frac1r
+(t-1)\sum_{q\le r\le U}\frac1r
+(1-t)\sum_{r\mid dq}\frac1r.
\]
Set
\(E_t(d)=\exp((1-t)\sum_{r\mid d}1/r)\).
Absorbing the q contribution into the constant and using Mertens yields
\[
\sum_{m:qdm\in I_p}g_{d,q}(m)
\ll\frac{H_p}{qd}
\frac{(\log U)^{t-1}}{(\log q)^t}E_t(d).
\tag{18}
\]

It remains to bound the divisor sum
\[
A_q=\sum_{\substack{U/q<d\le U\\\mu^2(d)=1,\ P^-(d)>q}}
\frac{t^{\omega(d)}E_t(d)}d.
\]
Define
\(h_q(d)=\mu^2(d)\mathbf1_{P^-(d)>q}t^{\omega(d)}E_t(d)\).
This is multiplicative, with h_q(r)=0 for r≤q,
h_q(r)=t exp((1−t)/r) for r>q, and h_q(r^j)=0 for j≥2.
It is bounded by one: log t+(1−t)/r<0 for r≥2 and 0<t<1.

Cover (U/q,U] by O(log q) dyadic intervals D<d≤2D, allowing positive
overcounts at the two ends. Each D is at least U/(2q), so log D is
comparable to log U and q<D uniformly when q≤U^(1/4) and U is large.
The prime perturbation in h_q(r) is O(1/r), so its contribution to
the Euler sum is O(∑r 1/r²)=O(1), uniformly in q. Equations (6)–(7)
give
\[
\sum_{D<d\le2D}h_q(d)
\ll D\frac{(\log D)^{t-1}}{(\log q)^t}.
\]
Divide each such estimate by D and sum the O(log q) blocks. Therefore
\[
A_q\ll(\log U)^{t-1}(\log q)^{1-t}.
\tag{19}
\]
Combining (17)–(19), and absorbing the fixed factor t, bounds the third
set by
\[
\ll H_p t^{-K}(\log U)^{2t-2}
\sum_{q\le Q}\frac{(\log q)^{1-2t}}q.
\tag{20}
\]
The last prime sum is uniformly bounded. Indeed, the block
2^j≤q<2^(j+1) contributes O(j^(−2t)) by
π(T)≪T/log T, and 2t=λ>1. Finally
\[
2t-2-\lambda\log t
=\lambda-1-\lambda\log\lambda=-\delta,
\tag{21}
\]
because λ log 2=1. Equation (20) is consequently
O(H_p/(log U)^δ). Together with (12) and (13), this proves (5).

The value λ=1/log 2 balances the high-count and divisor bounds with
t=λ/2. It is a convenient rigorous choice; no optimality for the actual
covariance is asserted. The familiar divisor-density constant δ appears
through this calculation, rather than through an unproved short-interval
transfer of a global multiplication-table theorem.

## 6. Transfer to the actual covariance

Cauchy–Schwarz, restricted only by the support of β, now gives
\[
\sum_{k\in I_p}|\beta_U(k)|
\le\sqrt{S_p\sum_{k\in I_p}\beta_U(k)^2}
\ll\frac{H_p}{(\log U)^{\delta/2}}.
\tag{22}
\]
Use (3) and (4) with the actual Z_p:
\[
|\mathcal C_N|
\le37\sum_p\sum_{k\in I_p}|\beta_U(k)|+o(u)
\ll\frac{N}{(\log U)^{\delta/2}}+o(u)
\ll\frac{N}{(\log N)^{\delta/2}}.
\tag{23}
\]
Here log U=(1/100+o(1))log N, so the fixed truncation exponent only
changes the implied constant. This proves (1), including its uniformity
with all of the actual sharp selection gates.

More generally, the same conclusion holds for any uniformly bounded
continuation family on these full I_p; it needs no equidistribution of
those weights. The L² mass of β remains of order H_p. The new saving
comes from the sparseness of its support and gives a vanishing L¹ mean.

## 7. What it settles and what it leaves open

The inherited joint interface is still
\[
\Delta_2+\Delta_3=\mathcal C_N-(M_C+o(1))u,
\]
with
\[
M_C\in[0.088495462680506291767141069549718388565758372430595,
0.088532079408569630135767526784074925416683359058930].
\]
Equation (23) proves \(|\mathcal C_N|=o(N)\). It does not prove o(u):
its upper bound divided by u has order
\((\log N)^{1-\delta/2}\), which grows. The source bound has no
explicit numerical constant that could be credited against the .011u
allocation. No new prime lower-bound mass is booked.

The next analytic target is a one-sided estimate exploiting the **actual
signed continuation** on the boundary-divisor configurations (10),
including the core marks where β=−1. The nonnegative envelope in
(17) and the absolute value in (22) deliberately discard that sign.
Even an extra logarithmic saving would need its size checked: this route
still lacks a factor (log N)^(1−δ/2) to reach the u scale. A sharper
conditional estimate or a stronger signed method is needed; the present
proof does not supply one automatically.

## 8. Verification and sources

Run `python3 src/beta_support.py` from the campaign directory. It writes
only results/beta_support_checks.json and results/beta_support_estimate.json.
Checks include independent large-divisor, short-divisor and prime-paired
β formulas; witnesses at the least prime; the exact exponent identity
(16), including shared and repeated prime factors; rational interval-size
vertices; outward enclosures for δ and the two balancing exponents; and
finite support/Cauchy identities. They are identity and parameter checks,
not experimental proofs of the asymptotic support density or covariance.

All checks passed: 599,990 large/short β rows, 1,569,950 arbitrary-prime
pairing rows, 52,327 nonzero least-prime witness rows, and 61,382 exact
overlap rows. The latter include 28,025 rows with q dividing m and 8,206
rows with gcd(d,m)>1. The rational minimum margin is 7/2400, and the
outward enclosure for δ/2 is
[0.043035666027967103443786549388461338880295554765095,
0.043035666027967103443786549388461338880295554765230].

The frozen checkpoint 16 manifest is retained at
results/checkpoint16_preservation_manifest.json. All 199 nonmutable
historical records and the negative-frontier ledger must retain their
previous hashes. Source identities and redistribution information are
in sources/beta_support/SOURCE_MANIFEST.json and SOURCE_README.md.

The precise new primary input is:

- Alexander P. Mangerel, *Divisor-bounded multiplicative functions in short
  intervals*, Research in the Mathematical Sciences 10, 12 (2023),
  **Lemma 3.2, PDF page 13**.
  [Official article](https://doi.org/10.1007/s40687-023-00376-0).
  Its displayed constant depends only on the fixed divisor-bound
  parameters and the fixed interval exponent; that is the uniformity
  needed for the moving g and h families. The bundled PDF is unmodified,
  attributed to its author and licensed CC BY 4.0.
- P. Shiu, *A Brun–Titchmarsh theorem for multiplicative functions*,
  Journal für die reine und angewandte Mathematik 313 (1980), 161–170,
  **Theorem 1, printed p. 163; class conditions on p. 162**.
  [Original source](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0313/LOG_0015.pdf).
  The class conditions and theorem were read and visually checked.
  The original scan is consulted but not redistributed. For the present
  proof the explicitly uniform, unmodulated form (6) is the admitted
  formulation; no independent reconstruction of Shiu's entire proof is
  claimed.
- The campaign's previously admitted Bretèche–Dress–Tenenbaum mean-square
  input, quantitative Möbius mean and PNT remain the sources of (3)–(4).
  They are documented in COFACTOR_ESTIMATE_NOTE.md and
  WEIGHTED_STOPPING_NOTE.md; no stronger new moment estimate is assumed.

