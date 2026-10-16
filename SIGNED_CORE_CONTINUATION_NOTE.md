# Signed core absorption and the next continuation estimate

Checkpoint 18 — Michael M. Ross's H(ϑ) campaign — 8 October 2026

Two further analytic deductions are proved. First, the positive core
prime count is covered, up to o(u), by negative single-prime continuation
on the same rough triprimes. This gives the exact signed interface
\[
\boxed{\mathcal C_N=F_N^+-G_N^--R_N+o(u),\qquad
F_N^+,G_N^-\ge0,\quad R_N\ge-o(u).}
\tag{1}
\]
All weights and gates in these quantities are the actual campaign weights.
Second, a direct treatment of the boundary stratum improves the available
absolute covariance bound to
\[
\boxed{|\mathcal C_N|\ll N/(\log N)^\eta,
\qquad \eta=0.06024782442318413\ldots .}
\tag{2}
\]
This replaces checkpoint 17's exponent 0.043035666… . The stronger
exponent comes from treating the low prime-count stratum directly in L¹,
then balancing it against the high-count Cauchy bound. The core absorption
is a separate signed deduction, useful for the one-sided target.

Neither (1) nor (2) proves the .011u allocation. The original target is
still a signed comparison at u=N/(2 log N), with its preserved reference
subtraction. H(ϑ), a positive lower-bound constant K, and the separate
higher-degree allocation remain open.

## 1. Actual global weights

Keep x=N², J=[x−N/2,x+N/2]∩ℤ for even N,
U=⌊N^(1/100)⌋, z=N^(1/4), and u=N/(2 log N). Retain the exact
outer coefficient c_N(d), D_good, complementary core C, and
D_B=N^(459/400) from WEIGHTED_STOPPING_NOTE.md. The continuation v_p
and core mark P_p are exactly its (16) and (18); no gate is changed.

Aggregate them on the original integer n:
\[
V_N(n)=\sum_{\substack{p\in\mathcal P_N\\p\mid n}}v_p(n/p),
\qquad
P_N(n)=\sum_{\substack{p\in\mathcal P_N\\p\mid n}}P_p(n/p).
\tag{3}
\]
The set 𝒫_N consists of primes z≤p<N^(19/20). The scalar P_N(n) in
(3) denotes the total core weight. We have V_N≥0 and V_N≤36+o(1)
on J. Each stop prime is greater than U, and n/p>1, so
β_U(n/p)=β_U(n) exactly. Also β_U(n)=−1 wherever P_N(n)>0.
Checkpoint 16's local mean removal therefore gives
\[
\mathcal C_N
=\sum_{n\in J}\bigl(\beta_U(n)V_N(n)+P_N(n)\bigr)+o(u).
\tag{4}
\]
The proper-prime-power and logarithmic-freezing errors are the previously
proved o(u) errors. The pointwise arguments below concern the actual
frozen prime-b continuation and prime-cofactor core in (3).

If P⁻(n)>U, then β_U(n)=−1. If P⁻(n)≤U, then P_N(n)=0, since every
core integer is a product of three primes greater than U. Consequently
(4) already separates the nonrough signed continuation from the rough
block P_N−V_N.

## 2. Ordering the core and retaining the product gate

A core mark has n=prℓ with p≤r, all three factors prime, pr∈C,
and pr²≤x. Its weight is e_(p,r)=1 when p<r and 1/2 when p=r.
Because the complete Type I region is included in D_good,
\[
pr>N^{457/400}>N.
\tag{5}
\]
If r>ℓ, then pr²−n=pr(r−ℓ)≥pr>N. But pr²≤x and n≥x−N/2
would imply pr²−n≤N/2. Hence
\[
p\le r\le\ell.
\tag{6}
\]
Thus a core mark must select the two smallest prime factors, counting
multiplicity. There is only one possible marked pair at a given n,
including repeated-prime cases; in particular 0≤P_N(n)≤1.

From (5) and n≤x+N/2,
\[
\ell\le(N^2+N/2)/N^{457/400}
\ll N^{343/400}<N^{19/20}
\tag{7}
\]
eventually, with exponent margin 37/400. Ordering gives the same upper
cutoff for p and r. All three primes are at least z, because r≥z and
ℓ≥r. They are therefore eligible actual single-prime outers, all of
which lie in D_good.

The two larger prime factors have product
\[
r\ell\ge n^{2/3}\gg N^{4/3}>D_B,
\tag{8}
\]
with exponent margin 4/3−459/400=223/1200. This verifies the **actual
db>D_B gate** for the absorbing rows, rather than restoring the removed
low-product region.

## 3. The rough core is absorbed up to o(u)

First suppose r<ℓ. These give two distinct single-prime stops. At the
stop r the continuation contains b=ℓ, and at the stop ℓ it contains
b=r. Both leave the prime cofactor p>1; b>U and (8) verify all the
other tests. These actual rows contribute at least
\[
V_N(pr\ell)\ge
\frac{\log\ell}{\log(x/r)}+
\frac{\log r}{\log(x/\ell)}.
\tag{9}
\]
Put A=log p, B=log r, C′=log ℓ, and ε=log(x/n). Since A≤B≤C′,
\[
\frac{C'}{A+C'}+\frac{B}{A+B}-1
=\frac{C'-A}{2(A+C')}+\frac{B-A}{2(A+B)}\ge0.
\tag{10}
\]
The denominators in (9) are A+C′+ε and A+B+ε. A negative ε only
increases the ratios. Its positive part is at most 1/N for N≥2, and
A+B> (457/400)log N. Comparing the two ratios with (10) gives
\[
V_N(pr\ell)\ge1-\frac2{N\log N}.
\tag{11}
\]
Because P_N≤1, this covers the core mark. The repeated-small-prime
case p=r<ℓ is included: the two stops r and ℓ are distinct, both
rows exist, and the marked core weight is only 1/2.

The remaining cases have r=ℓ, including a cube. They are sparse enough
to allow a uniform absolute error. For n=pr²∈J with p≤r,
p³≤x+N/2, so p<2N^(2/3). For a fixed integer p≥2 the interval for r
has real width
\[
\sqrt{\frac{x+N/2}{p}}-\sqrt{\frac{x-N/2}{p}}
=\frac{N}{\sqrt p\,(\sqrt{x+N/2}+\sqrt{x-N/2})}
\le\frac1{\sqrt{3p}}<1.
\tag{12}
\]
It contains at most one integer r. Counting all such p, even without
requiring primality, gives O(N^(2/3)) exceptional sites. On each,
P_N−V_N≤P_N≤1. For rough sites with no core mark, P_N−V_N≤0.
Summing (11) on the remaining at most N+1 sites proves
\[
\boxed{\displaystyle
\sum_{\substack{n\in J\\P^-(n)>U}}(P_N(n)-V_N(n))
\le O\!\left(N^{2/3}+\frac1{\log N}\right)=o(u).}
\tag{13}
\]
This is a one-sided bound. The rough block can make a substantial
negative contribution; it has not been asserted to equal o(u).

## 4. The signed interface that remains

Define the actual nonnegative sums
\[
F_N^+=\sum_{\substack{n\in J\\\beta_U(n)>0}}\beta_U(n)V_N(n),
\]
\[
G_N^-=\sum_{\substack{n\in J\\P^-(n)\le U,\ \beta_U(n)<0}}
(-\beta_U(n))V_N(n),
\qquad
R_N=\sum_{\substack{n\in J\\P^-(n)>U}}(V_N(n)-P_N(n)).
\tag{14}
\]
Positive β automatically implies P⁻(n)≤U. Equations (4) and (14)
give the signed identity (1), with R_N≥−o(u) from (13). In particular,
\[
\mathcal C_N\le F_N^++o(u).
\tag{15}
\]
The positive core count no longer needs a separate upper estimate for
this inference: its domination is by actual negative continuation on
the same integers. The stronger terminal comparison still needs the
negative counterweights in (14), or a sufficiently sharp bound on F_N⁺.

The inherited discrepancy identity is unchanged:
\[
\Delta_2+\Delta_3=\mathcal C_N-(M_C+o(1))u,
\]
where
\[
M_C\in[0.088495462680506291767141069549718388565758372430595,
0.088532079408569630135767526784074925416683359058930].
\]
The exact remaining sufficient target is therefore
\[
\boxed{F_N^+-G_N^--R_N\le(M_C+.011+o(1))u.}
\tag{16}
\]
Reference subtraction remains essential. No mass is added to the
historical lower-bound ledger by (13).

## 5. An exact signed boundary kernel and its unit rows

There is a useful exact separation of small primes from the continuation.
Define the auxiliary weight
\[
V_N^*(m)=\sum_{\substack{d\in D_{\rm good}\\d\mid m}}
\frac{c_N(d)}{\log(x/d)}
\sum_{\substack{b\mid m/d\\b>U\ {\rm prime}\\db>D_B}}\log b.
\tag{17}
\]
The supported d retain the frozen prime/two-prime coefficients, canonical
half weights, ordering gates and pr²≤x. The db gate remains inside
the inner sum. The auxiliary weight includes the rows with m/(db)=1.
They must be present in (17).

Indeed, if a>1 has all its prime factors at most U, all the primes in d
and b are greater than U. Divisibility by d and b is unchanged when
passing from m to am. The remaining cofactor in am is
a·m/(db)>1, even when m/(db)=1. Thus, whenever am∈J,
\[
\boxed{V_N(am)=V_N^*(m).}
\tag{18}
\]
This is an identity for the actual V_N; it introduces an auxiliary
weight without modifying its original nonunit-cofactor condition. A
naive substitution of the ordinary continuation formula on m would
omit valid rows.

For a nonrough n, let q=P⁻(n)≤U. The exact prime pairing gives
\[
\beta_U(n)=-\sum_{\substack{d\mid n,\ q\nmid d\\U/q<d\le U}}\mu(d).
\tag{19}
\]
Every nonzero summand has squarefree d with P⁻(d)>q and d≤U.
Writing n=qdm, the factor qd is U-smooth and greater than U. Equation
(18) therefore applies, including to every row whose cofactor becomes
one after this division. It yields the exact signed representation
\[
\boxed{\displaystyle
\sum_{\substack{n\in J\\P^-(n)\le U}}\beta_U(n)V_N(n)
=-\sum_{q\le U\ {\rm prime}}
\sum_{\substack{U/q<d\le U\\\mu^2(d)=1,\ P^-(d)>q}}
\mu(d)\,\mathcal K_N(q,d),}
\tag{20}
\]
where
\[
\mathcal K_N(q,d)=
\sum_{\substack{qdm\in J\\P^-(m)\ge q}}V_N^*(m).
\tag{21}
\]
The convention P⁻(1)=∞ applies. Repeated q factors in m and
gcd(d,m)>1 are allowed. No coprimality or independence is assumed.
For every eligible term, qd>U ensures that the original residual
cofactor is even greater than U, as in the unextended Vaughan row.

Equivalently, if a_U(n) is the entire small-prime part of n and
m_>U=n/a_U(n), the nonrough continuation factors exactly as
\[
\beta_U(n)V_N(n)=\beta_U(a_U(n))V_N^*(m_{>U}).
\tag{22}
\]
The short-interval membership still couples those two factors. This
factorization supplies no automatic mean-value estimate for (20).

A concrete stress example checks the necessity of the unit activation.
Take N=96, U=3, n=9174=2·3·11·139∈[9168,9264]. The small factor is
6, q=2, the boundary divisor is d=3, and β_3(n)=1. In the remaining
m=1529=11·139, the ordinary continuation excludes the row with outer
11 and b=139 because its cofactor is one. In n the cofactor is 6>U,
so that row is valid. V_N(n)=V_N^*(1529), whereas the ordinary continuation
formula on 1529 is zero under the same frozen coefficients. That formula
is evaluated with N fixed; the auxiliary integer is outside J. This is
an exact stress-cutoff example;
it does not alter the campaign's asymptotic U=⌊N^.01⌋.

## 6. Improving the L¹ exponent without assuming new cancellation

The support bound of checkpoint 17 remains valid with
δ=1−(1+log log 2)/log 2≈.086071332. A stronger L¹ inference is
available because the low-count boundary estimate was already a sum
over all possible boundary divisors, rather than merely their union.

Let ρ be the unique root in (1,2) of
\[
3-\rho+\rho\log(\rho/4)=0,
\quad \rho=1.52961427840864012\ldots ,
\]
and put
\[
t=\rho/2,\quad K=\rho\log\log U,\quad Q=\lfloor U^{1/4}\rfloor,
\qquad
\eta=\frac{1-\rho+\rho\log\rho}{2}
=2-\rho+\rho\log(\rho/2).
\tag{23}
\]
The derivative of the root equation's left side is log(ρ/4)<0 on
(1,2); its values at the ends have opposite signs. Thus the parameter
is well defined, fixed independently of N, and 1/2<t<1.

Work on a full stopped interval I_p of H=H_p sites and let ω_U(k)
count distinct prime divisors at most U. Use its inherited second
moment ∑β_U²≪H. Partition into the Q-rough set, the set with
ω_U(k)>K, and the remaining low-count set with P⁻(k)≤Q.

For the Q-rough set, the uniform Shiu bound gives a count ≪H/log U.
Cauchy against the full second moment costs at most
\[
\sum_{\substack{k\in I_p\\P^-(k)>Q}}|\beta_U(k)|
\ll H/(\log U)^{1/2}.
\tag{24}
\]
For the high-count set, the nonnegative multiplicative function
ρ^(ω_U(k)) is bounded by τ(k). The same uniform source theorem and
Mertens give
\[
\#\{k\in I_p:\omega_U(k)>K\}
\ll H(\log U)^{\rho-1-\rho\log\rho}
=H(\log U)^{-2\eta}.
\]
Again applying Cauchy only with the full-interval energy gives
\[
\sum_{\substack{k\in I_p\\\omega_U(k)>K}}|\beta_U(k)|
\ll H/(\log U)^\eta.
\tag{25}
\]
No selected-subset β moment is assumed in either step.

For the low-count set, pair at q=P⁻(k)≤Q and define the boundary
multiplicity
\[
D_q(k)=\sum_{\substack{d\mid k,\ q\nmid d\\U/q<d\le U}}\mu^2(d).
\]
Equation (19) gives |β_U(k)|≤D_q(k), not just the existence of one
divisor. Since ω_U(k)≤K and t<1,
\[
|\beta_U(k)|\le t^{-K}t^{\omega_U(k)}D_q(k).
\tag{26}
\]
The sum of the right side is exactly the same nonnegative boundary
envelope bounded in checkpoint 17, with its t replaced by ρ/2.
For completeness, the overlap-corrected multiplicative function is
\[
g_{d,q}(m)=\mathbf1_{P^-(m)\ge q}
t^{\omega_U(m)-\omega(\gcd(m,dq))},
\quad t^{\omega_U(qdm)}=t^{1+\omega(d)}g_{d,q}(m).
\tag{27}
\]
It is bounded by one. The scaled interval qdm∈I_p has real width
comparable to H/(qd), with qd≤U^(5/4)≤N^(1/80). The fixed Shiu
interval exponent 1/30 is still allowed with minimum power margin
7/2400. Its constant is uniform over the moving q,d,U families.

The uniform upper bound and dyadic divisor calculation give
\[
\sum_{m:qdm\in I_p}g_{d,q}(m)
\ll\frac H{qd}\frac{(\log U)^{t-1}}{(\log q)^t}E_t(d),
\quad E_t(d)=\exp\left((1-t)\sum_{r\mid d}\frac1r\right),
\]
\[
\sum_{\substack{U/q<d\le U\\\mu^2(d)=1,\ P^-(d)>q}}
\frac{t^{\omega(d)}E_t(d)}d
\ll(\log U)^{t-1}(\log q)^{1-t}.
\tag{28}
\]
Both proofs are unchanged from BETA_SUPPORT_ESTIMATE_NOTE.md, (18)–(19):
the divisor envelope has prime value t exp((1−t)/r)<1, and the
perturbation contributes only O(∑r r^(−2)). Summing (26) using (27)–(28)
therefore bounds the low-count L¹ sum by
\[
\ll Ht^{-K}(\log U)^{2t-2}
\sum_{q\le Q\ {\rm prime}}\frac{(\log q)^{1-2t}}q
\ll H(\log U)^{-\eta}.
\tag{29}
\]
The prime series converges because 2t=ρ>1. Its exponent is
2t−2−ρ log t=−[2−ρ+ρ log(ρ/2)]=−η by (23).
Since η<1/2, (24), (25) and (29) prove the stronger uniform bound
\[
\boxed{\sum_{k\in I_p}|\beta_U(k)|\ll H_p/(\log U)^\eta.}
\tag{30}
\]
Use the actual bound |Z_p|≤37, ∑p H_p≪N, the previously proved
local centering error o(u), and log U=(1/100+o(1))log N. This proves
the absolute covariance estimate (2). The same bound controls F_N⁺
by the nonnegative actual v_p, but its exponent is still less than one.

The balancing in (23) is optimal for these two specific envelopes:
the high-count exponent (1−ρ+ρ log ρ)/2 increases on (1,2), and
the low-count exponent 2−ρ+ρ log(ρ/2) decreases there. This is a
scoped optimization of this argument; it is not an optimality claim
for the actual continuation or a barrier to stronger analytic methods.

## 7. Remaining analytic task and verification

The remaining one-sided estimate is (16). The rough core has a proved
upper absorption, and the nonrough block has the exact signed kernel
(20)–(21). What is still missing is a uniform signed estimate for the
μ(d)-weighted kernels, or a comparison of F_N⁺−G_N⁻ against the
actual rough counterweight R_N with the required coefficient.

The bound (2) is o(N), but its upper scale divided by u grows as
(log N)^(1−η), with 1−η≈.939752176. It supplies neither an explicit
.011u coefficient nor a new prime lower-bound mass. Bounds for the
absolute boundary envelope alone do not control that remaining signed
comparison. The reference enclosure and historical analytic ledger
are unchanged; K=0 and H(ϑ) remains unproved.

Run `python3 src/signed_core_continuation.py` from the campaign directory.
It writes only results/signed_core_continuation_checks.json and
results/signed_core_continuation_estimate.json. It checks original-outer
weights and the global signed decomposition with exact coefficients of
X_(d,b)=log b/log(x/d), smooth multiplication with activated unit rows,
the signed boundary kernel, core ordering and both actual absorbing
rows, repeated-small and repeated-largest cases, outward frozen-log
inequalities, rational domain facets, and the certified parameter root.
Finite fixtures include actual and stress truncations, explicitly
labeled; they do not test the asymptotic terminal u-scale comparison.

All seven fixtures passed on 141,107 shell sites. They checked 111,967
smooth-factor identities, 30,087 signed boundary-divisor rows, and 538
regular core absorptions among 539 marked core sites. Both repeated
patterns were exercised, with one repeated-largest exception. The
negative nonrough counterweight was exercised at 2,798 sites. Another
73,143 exact even/odd boundary count identities and 20,858 overlap
exponents passed. Three rational core-domain vertices and the outward
parameter root certificate also passed. The enclosed new exponent is
[0.060247824423184131569041622857316763681703683368180,
0.060247824423184131569041622857316763681703726864980].

The frozen checkpoint 17 manifest is retained at
results/checkpoint17_preservation_manifest.json. All 209 nonmutable
historical records and the negative-frontier ledger must retain their
previous hashes. The strengthened beta support/L¹ arguments use the
same primary analytic input as checkpoint 17: Alexander P. Mangerel,
*Divisor-bounded multiplicative functions in short intervals* (2023),
Lemma 3.2, its explicitly uniform all-interval form of Shiu's bound.
[Official article](https://doi.org/10.1007/s40687-023-00376-0).
The inherited actual-beta energy and first moment inputs are documented
in WEIGHTED_STOPPING_NOTE.md. No almost-all input, multiplicativity of
β, conditional prime-pattern independence, or new Möbius correlation
theorem is assumed.
