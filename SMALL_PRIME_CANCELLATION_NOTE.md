# The small-prime block: energy and opposing continuation masses

Checkpoint 20 — Michael M. Ross's H(ϑ) campaign — 9 October 2026

Checkpoint 19 is genuine partial progress: the rough discrepancy and each
fixed large least-prime block have the target order O(u). It has not proved
the sharp joint estimate (3). This investigation identifies why the remaining
small-prime block needs signed control and proves a cancellation statement
for an actual subset of the continuation on the original long reference.

For every fixed 0<ε≤1, with T=U^ε, on a full stopped interval I_p,
\[
\boxed{\sum_{\substack{k\in I_p\\P^-(k)>T}}\beta_U(k)^2
       \ll\varepsilon^{-4}\frac{H_p}{\log U},\qquad
\sum_{\substack{k\in I_p\\P^-(k)\le T}}\beta_U(k)^2
       =(L+o(1))H_p.}
\tag{1}
\]
L>0 is the inherited actual-beta second-moment constant. These are
full-interval statements, uniform in the campaign's stopping primes;
they are not moments under the selected continuation weight.

There is also a concrete actual continuation subweight W_N≤V_N, supported
on even integers, for which the positive and negative reference masses obey
\[
\boxed{a\sum_{n\in B_1}\beta_U^+(n)W_N(n)\gg\frac{N}{D_U},\qquad
       a\sum_{n\in B_1}\beta_U^-(n)W_N(n)\gg\frac{N}{D_U},}
\tag{2}
\]
\[
\boxed{a\sum_{n\in B_1}\beta_U(n)W_N(n)=o(u),}
\tag{3}
\]
where β^+=max(β,0), β^-=max(−β,0), and
\[
D_U=(\log U)^\delta(\log\log U)^{3/2},\qquad
\delta=1-\frac{1+\log\log2}{\log2}=0.086071332\ldots.
\]
The lower bounds use the published isolated-divisor input described in
Section 3. Since N/D_U divided by u tends to infinity, both opposing
reference contributions are larger than the permitted remainder scale.
The construction keeps the original logarithmic coefficients and gates.

This is an actual long-reference cancellation result, not the missing
uniform short/reference discrepancy bound. The exponent η≈.0602478244,
core coefficient, analytic mass ledger and certified K=0 are unchanged.
H(ϑ), the .011u terminal comparison and the higher-degree cap remain open.

## 1. Frozen definitions and the precise unfinished estimate

Keep all checkpoint-19 definitions and weights:
\[
x=N^2,\quad J=[x-N/2,x+N/2]\cap\mathbb Z,\quad
Y=N+1,\quad u=N/(2\log N),\quad U=\lfloor N^{1/100}\rfloor,
\]
\[
D_B=N^{459/400},\quad z=N^{1/4},\quad w=N^{19/20},\quad
\beta_U(n)=-\sum_{\substack{d\mid n\\d\le U}}\mu(d)\quad(n>1),
\quad\beta_U(1)=0.
\]
V_N and P_N are the unchanged aggregated continuation and core weights;
0≤V_N≤36+o(1) near x. The normalized original reference is
\[
H_1=2\lfloor x\exp(-3(\log x)^{1/3})/2\rfloor+1,
\quad B_1=(x-H_1/2,x+H_1/2)\cap\mathbb Z,
\quad a=Y/H_1,\quad\rho=H_1/x.
\]
All cutoffs remain frozen at x. In particular, ρ^{-1}=N^{o(1)}.

Write S_≤T(W) for the actual nonrough sum β_U V_N restricted to
P^-(n)≤T, and S_{>T}(W) for T<P^-(n)≤U. Let
\[
E_\le=-\sum_{\substack{(q,d)\in\mathcal B_U\\q\le T}}
       \mu(d)(\mathcal K_J(q,d)-a\mathcal K_{B_1}(q,d)),
\]
and define E_> with q>T. Let E_R=R_J−aR_{B_1}. Then exactly
\[
E_\le=S_{\le T}(J)-aS_{\le T}(B_1),\qquad
\Delta_2+\Delta_3=E_\le+E_>-E_R+o(u).
\tag{4}
\]
The coefficient-exact remaining estimate is still
\[
\boxed{E_\le+E_>-E_R\le(.011+o(1))u.}
\tag{5}
\]
Checkpoint 19 proves E_>=O_ε(u), E_R=O(u), and
a(S_N(B_1)−R_N(B_1))=(M_C+o(1))u. It therefore also gives
\[
\boxed{aS_{\le T}(B_1)=O_\varepsilon(u).}
\tag{6}
\]
Thus the uncontrolled order-of-magnitude question can be located entirely
in S_≤T(J). A bound O(u) for it would close that scale question only;
the .011 coefficient would still require the joint comparison (5).

## 2. Higher absolute moments and localization of the beta energy

For every fixed positive integer j define
\[
f_{j,U,T}(n)=\mathbf1_{P^-(n)>T}\,2^{j\omega_U(n)}.
\]
At positive prime powers the values are 0 for p≤T, 2^j for T<p≤U,
and 1 for p>U. It is nonnegative and multiplicative, and
f_{j,U,T}≤τ_{2^j}. For n>1, |β_U(n)|≤2^{ω_U(n)}, so this majorizes
|β_U|^j on the selected rough set. It does not make β_U multiplicative.

Apply the inherited deterministic Shiu bound, Mangerel (2023), Lemma 3.2,
with the fixed divisor parameters B=2^j,C=1 and interval exponent 1/30.
The Euler exponent is
\[
-\sum_{p\le T}\frac1p+(2^j-1)\sum_{T<p\le U}\frac1p.
\]
Uniform Mertens estimates yield, for a full allowed window of H sites,
\[
\sum_{\substack{n\in W\\P^-(n)>T}}|\beta_U(n)|^j
\ll_j H\frac{(\log U)^{2^j-1}}{(\log T)^{2^j}}
\ll_j\varepsilon^{-2^j}\frac H{\log U}.
\tag{7}
\]
Constants are independent of the moving U,T and interval center; j is
fixed before N tends to infinity. The assertion is not uniform for j
growing with N. Eventual T≥2 suffices for every fixed ε>0.

For I_p={k:pk∈J}, put s=log_N p. Here 1/4≤s<19/20,
H_p=N/p+O(1), and the center is comparable to N^{2−s}. The minimum
Shiu power margin is
\[
\min_s\left(1-s-\frac{2-s}{30}\right)=\frac3{200}>0.
\]
The inherited exact full-interval energy gives
\[
\sum_{k\in I_p}\beta_U(k)^2=H_p q(U)+O(U^2),\qquad q(U)\longrightarrow L>0.
\]
Uniformly, U²/H_p≪N^{-3/100}. Subtract (7) with j=2 to get (1).
The same localization holds on the full shell J, with H=Y. No selected
β²V or β²v_p energy lower bound has been inferred.

The unweighted first moment on either full interval is −Hα_U+O(U)=o(H/log N).
Together with (7), j=1, it gives
\[
\left|\sum_{\substack{n\in W\\P^-(n)\le T}}\beta_U(n)\right|
\ll_\varepsilon H/\log U.
\tag{8}
\]
Thus the small-prime block has a small unweighted signed mean and a
nonvanishing full-interval mean square. Replacing the mean square by
O(H/log U) in a Cauchy estimate would be incorrect. Its covariance with
the actual V_N is precisely the additional information that is missing.

## 3. Even integers: signed mean versus absolute mass

For every even c>1, pairing squarefree divisors at the prime 2 gives
\[
\boxed{\beta_U(c)=-\sum_{\substack{d\mid c\\d\ {\rm odd}\\U/2<d\le U}}\mu(d).}
\tag{9}
\]
Repeated powers of 2 are allowed. Consequently, for t≥2,
\[
A_2(t):=\sum_{\substack{c\le t\\2\mid c}}\beta_U(c)
=-\sum_{\substack{U/2<d\le U\\d\ {\rm odd}}}
       \mu(d)\left\lfloor\frac{t}{2d}\right\rfloor
=-\frac t2 m_2(U)+O(U),
\tag{10}
\]
where m_2(U)=∑_{U/2<d≤U,d odd}μ(d)/d.

The admitted quantitative long Möbius PNT implies
m_2(U)=O(exp(−c_0√log U)). To check the odd restriction, let M_o(v)
be the summatory Möbius function on odd integers. The exact recursion
M_o(v)=M(v)+M_o(v/2) gives the same PNT decay after splitting the
dyadic iteration at v^{1/2}. Partial summation and the Euler factor
(1/ζ(s))/(1−2^{-s}), which vanishes at s=1, then give the required
odd reciprocal bound. Fixed powers of log U are absorbed by reducing c_0.

The additional source input is Granville–Koukoulopoulos–Maynard,
*Sieve weights and their smoothings*, Ann. Sci. Éc. Norm. Supér. 54 (2021),
1089–1177, DOI 10.24033/asens.2478. Their Section 1.1, equation (1.2)
and following paragraph, exhibit odd squarefree m with exactly one
divisor in (U/2,U], of density ≫1/D_U for t≥U^{1+ε_0}; the construction
uses Ford's isolated-divisor lower bound. For c=2m it gives
\[
\#\{c\le t:2\mid c,\ |\beta_U(c)|=1\}\gg_{\varepsilon_0}t/D_U.
\tag{11}
\]
This uses the lower-bound construction on even integers, rather than
assigning the source's total support lower bound to even integers without
justification. The published input is accepted here; this checkpoint does
not independently reprove Ford's counting argument. The source bounds
initial intervals [1,t], not every short interval near an arbitrary center.

Let β^± be as above. Since β is integer valued,
\[
\sum_{\substack{c\le t\\2\mid c}}|\beta_U(c)|\gg t/D_U,
\qquad
\sum_{\substack{c\le t\\2\mid c}}\beta_U^\pm(c)
=\frac12\left(\sum_{2\mid c\le t}|\beta_U(c)|\pm A_2(t)\right).
\]
For N^{9/40}≤t≤N^{1/4}, (10) is smaller than t/D_U uniformly, so
both signs have mass ≫t/D_U. Here U≤N^.01 and t≥U^{22.5},
well inside the source range with fixed ε_0=1.

Put A_0=N^{1/5}, A_1=N^{1/4}. The inherited full-beta energy and Cauchy
give ∑_{c≤A_0}|β_U(c)|≪A_0+U², which is negligible compared with
t/D_U for t≥N^{9/40}. Subtracting this initial portion and partially
summing gives
\[
h_U^\pm:=\sum_{\substack{A_0<c\le A_1\\2\mid c}}\frac{\beta_U^\pm(c)}c
\gg\frac{\log N}{D_U},\qquad h_U^++h_U^-\ll\log N.
\tag{12}
\]
Separately, partial summation of (10) gives
\[
h_U:=h_U^+-h_U^-
\ll(\log N)e^{-c_0\sqrt{\log U}}+U/A_0.
\tag{13}
\]
The signs need not be evenly distributed among the isolated-divisor
witnesses themselves. Their overall balance in (12) follows from the
signed mean on all even integers.

## 4. Transferring those masses to unchanged continuation rows

Take the actual single-prime outer subset
\[
\mathcal P_N^0=\{p\text{ prime}:N^{3/10}\le p\le N^{7/20}\},
\qquad\mathcal A_N=\{c\text{ even}:N^{1/5}<c\le N^{1/4}\}.
\]
Define the marked continuation subweight
\[
W_N(n)=\sum_{p\in\mathcal P_N^0}
 \sum_{\substack{b\text{ prime},\ c\in\mathcal A_N\\n=cpb}}
 \frac{\log b}{\log(x/p)}.
\tag{14}
\]
This is a subset of original rows, with no new coefficient assigned to
V_N. Near x, every marked row passes all actual conditions:

| Condition | Exponent check / reason |
|---|---|
| Single-prime outer z≤p<w | 3/10>1/4 and 7/20<19/20 |
| Outer in D_good | p≤N^{7/20}<N^{457/400} |
| Prime b>U | b≈N²/(cp), exponent at least 7/5 |
| Actual product pb>D_B | pb=n/c≳N^{7/4}; gap 241/400>0 |
| Original residual c>U and c>1 | c>N^{1/5}>N^{1/100} |
| Same beta coefficient | p,b>U imply β_U(cpb)=β_U(c), even if p divides c |
| Smallest prime | c is even, so every marked n has P^-(n)=2 |

The two-prime outer ordering gates and half-weights are not invoked: the
construction uses single-prime outers whose original coefficient is one.
The residual c need not be U-smooth; no coprimality between c,p,b is imposed.
Nothing is changed in the other sectors. Thus 0≤W_N(n)≤V_N(n).

For each c,p the b interval on B_1 has center comparable to
N²/(cp), lying between constant multiples of N^{7/5} and N^{3/2}.
Its relative length is ρ. The admitted quantitative long prime PNT gives
\[
\sum_{cpb\in B_1,\ b\text{ prime}}\log b
=\frac{H_1}{cp}+O\left(\frac{x}{cp}e^{-c_1\sqrt{\log N}}\right)
\tag{15}
\]
uniformly. Proper prime powers are removed in passing from Λ to θ; their
ordinary square-root bound is included in the displayed exponential error.

The prime-log numerator in (14) is essential: it produces the coefficient
1/(cp log(x/p)) exactly in the main term, with no new log(x/(cp)) factor.
Using (12) to sum the absolute PNT errors, define
\[
E_N=\sum_{p\in\mathcal P_N^0}\frac1{p\log(x/p)}
=\frac{\kappa+o(1)}{\log N},\qquad
\kappa=\int_{3/10}^{7/20}\frac{dt}{t(2-t)}
=\frac12\log\frac{119}{99}>0.
\tag{16}
\]
Then, for both signs and also their signed difference,
\[
a\sum_{n\in B_1}\beta_U^\pm(n)W_N(n)
=Y E_N h_U^\pm+o(u),
\tag{17}
\]
with total absolute error
O(Nρ^{-1} exp(−c_1√log N))=o(u), after absorbing fixed logarithms.
Equations (12) and (17) prove (2), and (13), (16), (17) prove (3).
For the signed main term, the two errors are bounded by
N exp(−c_2√log N)+N^{81/100}/log N=o(u).

The lower bound N/D_U is asymptotically larger than u by a factor
comparable to (log N)^{1−δ}/(log log N)^{3/2}, which tends to infinity.
Accordingly the actual positive and negative continuation totals on B_1
each have at least this normalized mass, already at q=2. The reference
small-prime signed total nevertheless has order O_ε(u), by (6).

## 5. What this resolves and what it does not

The long-reference cancellation has now been exhibited in a substantial
actual q=2 subweight, not only inferred for the aggregate. Its positive
and negative parts cannot each be charged as an O(u) reference error.
This rules out that particular separate unsigned accounting strategy.
It does not rule out an absolute estimate for the already-subtracted
kernels K_J−aK_B1: the reference masses alone do not lower-bound their
absolute discrepancy. Nor is it a counterexample to (5).

The short version of the marked subweight is explicitly
\[
\sum_{\substack{c\in\mathcal A_N\\p\in\mathcal P_N^0}}
 \frac{\beta_U(c)}{\log(x/p)}
 \sum_{b\text{ prime},\ cpb\in J}\log b.
\tag{18}
\]
Its prime intervals have width N/(cp), with exponent between 2/5 and
1/2 relative to N, at centers with exponents between 7/5 and 3/2.
Their relative length exponents are at most 1/3, far below the long PNT
used in (15). Applying (15) here, even before summing c,p, would be
invalid. An aggregate signed bound, retaining β_U(c), is required.
Solving (18) alone would still not cover the complementary actual rows.

The next analytic task remains (5). A useful concrete subproblem is to
estimate (18) together with its original reference subtraction, then
extend that estimate to the full small-q continuation while preserving
the joint coefficient and the rough discrepancy. No positive prime
mass has been credited for (1)–(3); no terminal coefficient is improved.

## 6. Verification and source scope

Run `python3 src/small_prime_cancellation.py` from the campaign directory.
The new checks verify even-divisor pairing and exact floor means, both
signs, the fixed-moment multiplicative envelopes, full-interval energy
partitions, independent marked-prime row enumeration, preservation of
actual weights, prime/log coefficients and rational source margins.
Finite wider windows are explicitly artificial identity fixtures; they
do not test the actual asymptotic B_1 PNT or the lower-bound constants.

The isolated-divisor lower bound is a newly admitted published source
input. Its location and application range are recorded separately in
results/small_prime_source_audit.json. Mangerel's deterministic bound,
the BDT beta energy, long PNT and prior analytic gates are inherited.
No almost-all interval theorem or smoothed replacement of β is used.
All 220 nonmutable checkpoint-19 records and the frozen historical
negative-frontier ledger are preserved unchanged.
