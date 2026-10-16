# Estimating the signed boundary kernels

Checkpoint 19 — Michael M. Ross's H(ϑ) campaign — 8 October 2026

The complete signed estimate remains open. This investigation proves three
additional bounds and an exact discrepancy formulation:

\[
\boxed{-o(u)\le R_N\ll u,\qquad
\mathcal K_N(q,d)\ll\frac{N}{qd\log q}.}
\tag{1}
\]
For every fixed \(0<\varepsilon\le1\), the nonrough signed block whose
least prime exceeds \(U^\varepsilon\) also has a uniform bound
\[
\boxed{|S_{>U^\varepsilon}(J)|\ll\varepsilon^{-2}u.}
\tag{2}
\]
The implied constants are independent of N; the inherited Shiu input does
not supply the explicit coefficient needed for .011u. Neither (1) nor (2)
settles the small least-prime block or the terminal comparison.
The identity β_U=ω_U−1 above the least-prime cutoff √U also shows
that every negative nonrough counterweight lies in the smaller-prime block.

Retaining the actual long reference reduces the required estimate to
\[
\boxed{-\sum_{q,d}\mu(d)
 \bigl(\mathcal K_J(q,d)-a\mathcal K_{B_1}(q,d)\bigr)
 -\bigl(R_J-aR_{B_1}\bigr)\le(.011+o(1))u.}
\tag{3}
\]
Its main coefficient has been accounted for by the reference, rather than
discarded or reallocated. The old core enclosure, exponent
\(\eta\approx0.0602478244\), and analytic mass ledger are unchanged.
K=0, H(ϑ), and the higher-degree allocation remain open.

## 1. Fixed weights and the signed sums

Keep the checkpoint 18 definitions, including every ordering, outer
support, D_good/C, prime-b, db>D_B, half-weight, and nonunit-cofactor
condition. Thus
\[
x=N^2,\quad J=[x-N/2,x+N/2]\cap\mathbb Z,\quad
U=\lfloor N^{1/100}\rfloor,\quad D_B=N^{459/400},\quad
u=N/(2\log N).
\]
Write V_N(n) and P_N(n) for the actual aggregated continuation and core
weights in SIGNED_CORE_CONTINUATION_NOTE.md. The auxiliary V_N^*(m)
includes its essential activated unit rows; it does not change V_N.

For any finite window W near x, with all coefficients frozen at the same
x, define
\[
S_N(W)=\sum_{\substack{n\in W\\P^-(n)\le U}}\beta_U(n)V_N(n),\qquad
R_N(W)=\sum_{\substack{n\in W\\P^-(n)>U}}(V_N(n)-P_N(n)),
\]
\[
\mathscr C_N(W)=\sum_{n\in W}(\beta_U(n)V_N(n)+P_N(n))
              =S_N(W)-R_N(W).
\tag{4}
\]
The last equality is exact: β_U=−1 on rough integers and P_N vanishes
on nonrough integers. On J the inherited covariance differs from
\(\mathscr C_N(J)\) by o(u), and S_N(J)=F_N⁺−G_N⁻.

For the actual boundary family
\[
\mathcal B_U=\{(q,d):q\le U\text{ prime},\ U/q<d\le U,
\mu^2(d)=1,\ P^-(d)>q\},
\]
let
\[
\mathcal K_W(q,d)=\sum_{\substack{qdm\in W\\P^-(m)\ge q}}V_N^*(m).
\tag{5}
\]
The same elementary prime pairing as checkpoint 18 proves, for each W,
\[
S_N(W)=-\sum_{(q,d)\in\mathcal B_U}\mu(d)\mathcal K_W(q,d).
\tag{6}
\]
No coprimality is inserted: q may divide m and d may share primes with m.
Every boundary multiplier qd is U-smooth and greater than U, so the
original residual cofactor is greater than U even if its auxiliary
cofactor becomes one. Formula (6) remains valid on the reference window;
it does not require the short-window core-ordering argument.

## 2. The rough counterweight has the target order of magnitude

Use Mangerel (2023), Lemma 3.2, the already admitted deterministic
all-interval Shiu bound. For a nonnegative multiplicative f with
f(n)≤τ(n), it gives on the present intervals
\[
\sum_{n\in W}f(n)\ll |W|
 \exp\left(\sum_{p\le X}\frac{f(p)-1}{p}\right),
\tag{7}
\]
with X comparable to the upper endpoint. Fix its interval parameter
at 1/30, divisor parameters B=2, C=1. The full shell has length
N+1 and center comparable to N², so it qualifies with a fixed power
margin. These are uniform family constants, not changing with U.

Apply (7) to \(f(n)=\mathbf1_{P^-(n)>U}\). Mertens' estimate gives
\[
Q_U(J):=\#\{n\in J:P^-(n)>U\}\ll\frac{N}{\log U}
\ll\frac{N}{\log N}.
\tag{8}
\]
Since V_N≤36+o(1), and P_N≥0,
\[
R_N(J)\le(36+o(1))Q_U(J)\ll u.
\]
Checkpoint 18 proved the opposite one-sided bound
\(R_N(J)\ge-O(N^{2/3}+1/\log N)=-o(u)\). Together these prove (1)'s
rough-counterweight assertion, and in particular |R_N(J)|=O(u).

This closes its *scale* bound, not its coefficient. It also shows that
an upper estimate as large as N/(log N)^η for the positive boundary
envelope cannot be paid for by an arbitrarily large rough reserve:
the actual R_N itself is only O(u). Signed cancellation in S_N(J), or
a compatible direct comparison, is still needed.

## 3. Uniform individual kernel bounds

For (q,d)∈𝔅_U, qd≤U²≤N^(1/50). The m interval in (5) has real
width N/(qd), and center comparable to N²/(qd). Its site count is
comparable to that width uniformly. If s=log_N(qd), then
\[
1-s-\frac{2-s}{30}\ge\frac{457}{500}>0,
\qquad 0\le s\le1/50.
\tag{9}
\]
Thus the same Shiu source is valid on every one of these moving
intervals; U is below their centers with a fixed power margin.

Because qd>U is U-smooth, the exact activated-unit identity gives
\(V_N^*(m)=V_N(qdm)\le36+o(1)\) for contributing sites. Apply (7)
to the multiplicative indicator \(\mathbf1_{P^-(m)\ge q}\). Its Euler
product excludes the primes *less* than q and is O(1/log q), including
q=2. Hence, uniformly over the complete actual family,
\[
\mathcal K_J(q,d)\ll\frac{N}{qd\log q}.
\tag{10}
\]
This is a nonnegative bound. Summing its absolute values against μ(d)
does not establish the signed coefficient in (3).

## 4. A uniform signed bound when the least prime is large

Let 2≤T≤U, and restrict the nonrough sum to T<P⁻(n)≤U:
\[
S_{>T}(W)=\sum_{\substack{n\in W\\T<P^-(n)\le U}}
                       \beta_U(n)V_N(n)
=-\sum_{\substack{(q,d)\in\mathcal B_U\\q>T}}\mu(d)\mathcal K_W(q,d).
\tag{11}
\]
The actual β weight satisfies |β_U(n)|≤2^(ω_U(n)) for n>1, where
ω_U counts distinct prime divisors at most U. Define the multiplicative
majorant
\[
f_{U,T}(n)=\mathbf1_{P^-(n)>T}\,2^{\omega_U(n)}.
\tag{12}
\]
At every positive prime power its values are 0 for p≤T, 2 for T<p≤U,
and 1 for p>U. Therefore f_{U,T}(n)≤τ(n), with the same fixed divisor
bound used above. It majorizes |β_U| on the selected set, without
asserting multiplicativity of β_U.

The Euler exponent in (7) is
\[
-\sum_{p\le T}\frac1p+\sum_{T<p\le U}\frac1p
=\sum_{p\le U}\frac1p-2\sum_{p\le T}\frac1p.
\]
Uniform Mertens estimates consequently give
\[
\sum_{n\in W}f_{U,T}(n)
\ll |W|\frac{\log U}{(\log T)^2}.
\tag{13}
\]
All implied constants here are independent of T,U,N once the window
condition holds. Multiplying by V_N≤36+o(1) proves
\[
\boxed{|S_{>T}(J)|\ll N\frac{\log U}{(\log T)^2}.}
\tag{14}
\]
For T=U^ε, T≥2 eventually for every fixed ε>0, and (14) becomes (2).
This solves a uniform *order-of-magnitude* subproblem in the signed
kernel family. It does not give an explicit .011 coefficient, and it
does not bound the complementary q≤U^ε sum at scale u.

At T=√U there is also an exact sign identity. If P⁻(n)>√U, every
nonzero squarefree divisor at most U is either 1 or one prime. Thus
\[
\boxed{\beta_U(n)=\omega_U(n)-1.}
\tag{14a}
\]
On the nonrough selected set ω_U≥1, so S_>√U(W)≥0. Equivalently,
every boundary d with q>√U is prime, and μ(d)=−1. There is no
Möbius cancellation within that actual positive block. All nonrough
negative β counterweight G_N⁻ is supported on P⁻(n)≤√U. This sign
statement concerns each actual window sum; its short-minus-reference
discrepancy need not be nonnegative.

## 5. Retaining the reference gives the coefficient-exact interface

Keep the original reference, rather than choosing a new averaging scale:
\[
H_1=2\left\lfloor x\exp(-3(\log x)^{1/3})/2\right\rfloor+1,
\quad B_1=(x-H_1/2,x+H_1/2)\cap\mathbb Z,
\]
\[
Y=N+1,\quad a=Y/H_1,\quad \rho=H_1/x.
\tag{15}
\]
Its cardinality is H_1. All outer and inner gates, U and logarithmic
denominators remain frozen at x. The following normalized reference
main term is proved using the inherited long-reference reduction:
\[
\boxed{a\mathscr C_N(B_1)=(M_C+o(1))u.}
\tag{16}
\]
Here are the error checks needed to transfer that result to the exact
prime-b, product-gated continuation used in (4).

1. **The full long Type II term.** JOINT_REMAINDER_NOTE.md, (3)–(7),
   proves aB_Dgood(B_1)=o(u), uniformly for fixed outer subsets. This
   uses the quantitative long PNT for Λ and μ, the normalized Type I
   floor error, and the unchanged density centering. No short PNT is
   inferred from it.
2. **Long logarithmic freezing.** Near x, the relative error replacing
   log(mb) by log(x/d) is O(ρ/log N). Before taking signs, the full
   Type II sum is majorized by \(\sum_{n\in B_1}\tau_4(n)\): use
   c_N(d)≤1, |β_U(m)|≤τ(m), Λ(b)/log(mb)≤1, and the convolution
   1*1*τ=τ_4. Applying Lemma 3.2 with the fixed parameters B=4,C=1
   gives O(H_1(log N)³). The normalized freezing error is therefore
   O(Nρ(log N)²)=o(u). A pointwise N^ε bound would not suffice for
   this particular error; the averaged divisor bound is used.
3. **Proper powers in the b slot.** The collapsed coefficient is
   O_ε(N^ε). Counting k with kb∈B_1, the proper-power reciprocal
   sum O(U^(−1/2)), and the global proper-power count
   O(N^(1−1/200)) give, after multiplication by a,
   \[
   O_\epsilon\bigl(N^{1+\epsilon}U^{-1/2}
           +N^{-1/200+\epsilon}\rho^{-1}\bigr)=o(u).
   \]
   For example ε=1/1000 gives leading exponent 249/250. This is an
   absolute estimate, so D_good and other selections are retained.
4. **The removed low-product region.** For db≤D_B the residual interval
   has center at least a constant times N^(341/400), well above U.
   Its first moment is −(H_1/(db))α_U+O(U), with
   α_U=O(exp(−c√log N)). Summing the floor errors over d,b costs
   O_ε(U N^(459/400+ε)). After normalization the error is
   O_ε(N^(63/400+ε)ρ^(−1))=o(u); the α_U main term is o(u) as well.
   Thus aB_Dgood,db≤D_B(B_1)=o(u) by a long-interval argument.
5. **The core reference.** The quantitative long PNT in each prime
   cofactor interval gives
   \[
   a\sum_{n\in B_1}P_N(n)
   =Y\sum_{d\in C}\frac{c_N(d)}{d\log(x/d)}+o(u)
   =(M_C+o(1))u.
   \]
   If transferring from the earlier Mangoldt/log count, the normalized
   proper-cofactor-power contribution is
   O(N^(2/3)ρ^(−1)(log N)^C)=o(u): enlarge d to all integers ≤N^(4/3)
   and count proper powers up to 2x/d. The fixed gates defining C
   remain exactly those used in its original reference integral.

These steps establish a∑_(B1)β_U V_N=o(u), while the core contributes
(M_C+o(1))u. This proves (16).

No short core absorption is assumed on B_1. A long reference can
contain different prime-factor orderings. The exact identity (4) still
holds, and P_N(n)≤3 there: a prime-cofactor mark requires a triprime and
there are at most three pair choices, with the canonical half weights.
Also V_N≤36+o(1) near x. Shiu consequently gives
\[
|aR_N(B_1)|\ll u,\qquad
|R_N(J)-aR_N(B_1)|\ll u.
\tag{17}
\]
The reference analogues of (10) and (14) are
\[
a\mathcal K_{B_1}(q,d)\ll\frac{N}{qd\log q},\qquad
|aS_{>T}(B_1)|\ll N\frac{\log U}{(\log T)^2}.
\tag{18}
\]
The reference intervals have ample length for the same fixed Shiu
parameter, since ρ=N^(−o(1)).

Define the *signed* discrepancies
\[
\mathcal E_N(q,d)=\mathcal K_J(q,d)-a\mathcal K_{B_1}(q,d),\qquad
\mathcal E_R=R_N(J)-aR_N(B_1).
\tag{19}
\]
They are not nonnegative kernels. Equations (10) and (18) give
|E_N(q,d)|≪N/(qd log q) individually. Equations (4), (6) and (16) give
\[
\mathcal C_N-(M_C+o(1))u
=-\sum_{(q,d)\in\mathcal B_U}\mu(d)\mathcal E_N(q,d)
 -\mathcal E_R+o(u).
\tag{20}
\]
This proves the advertised coefficient-exact interface (3). The enclosure
for M_C is unchanged:
\[
[0.088495462680506291767141069549718388565758372430595,
 0.088532079408569630135767526784074925416683359058930].
\]

For a fixed ε, split (20) at T=U^ε. The q>T discrepancy and E_R are
each O_ε(u) by (14), (17), (18). The q≤T discrepancy is not yet
estimated at scale u. Even an O(u) bound for that last block would
still need the actual joint coefficient .011, rather than unspecified
constants for three separate absolute estimates.

## 6. Why small-prime invariance is not already cancellation

There is an exact geometric obstruction to a tempting pairing argument.
If V_N(n)>0, an actual row has h=db>D_B, and every prime in d and b
exceeds U. Hence the entire U-rough part m_>U(n) is divisible by h:
\[
m_{>U}(n)\ge h>D_B>N.
\tag{21}
\]
For a fixed such rough part m, two distinct integer smooth multipliers
a₁,a₂ give products whose distance is at least m>N. They cannot both
lie in the diameter-N shell J. In particular, smooth multiplication
invariance does not furnish a positive/negative β pairing *inside the
actual shell while keeping the large-prime part fixed*.

More formally, on the set of shell sites with rough part greater than
D_B, the map n↦m_>U(n) is injective. Any prescribed bounded selection
of those sites can be extended to an auxiliary weight depending only
on m_>U(n), hence invariant under U-smooth multiplication. This says
that invariance alone does not constrain the signs of the selected
shell values. Such an auxiliary weight is not the campaign's V_N and
is not a counterexample to (3); the actual prime-divisor coefficients
must supply the missing regularity or signed comparison.

The same issue is visible in the boundary kernels. Each multiplier
a=qd in 𝔅_U is squarefree and uniquely determines q=P⁻(a), d=a/q;
U<a≤U²<N. For distinct a<b in this range, their closed real cofactor
cells are disjoint because
\[
\frac{x-N/2}{a}-\frac{x+N/2}{b}
=\frac{(b-a)N^2-(a+b)N/2}{ab}>0.
\tag{22}
\]
Once a contributing m with V_N^*(m)>0 is fixed, the d interval has
width N/(qm)<N/(qD_B)<1. Thus a usual unweighted long Möbius sum in
d does not occur after fixing the other variables. Distinct d sample
different cofactor cells, so an elementary Mertens bound cannot be
inserted without controlling the variation or arithmetic correlations
of their weights. Disjointness does not assert statistical independence.

## 7. Primary-source transfer checks

The new admitted upper bounds use the same source as checkpoints
17–18: Alexander P. Mangerel, *Divisor-bounded multiplicative functions
in short intervals* (2023), Lemma 3.2
([official article](https://doi.org/10.1007/s40687-023-00376-0)). Its
constants are explicitly uniform in the divisor-bounded family. It
estimates absolute values and supplies no signed μ-weighted kernel
discrepancy by itself. The new τ₄ reference majorant uses the same
lemma with fixed B=4,C=1.

Two possible signed transfers were checked against their primary texts:

| Primary result inspected | What prevents a direct deduction here |
|---|---|
| Matomäki–Teräväinen, *On the Möbius function in all short intervals*, Theorem 1.1 ([official text](https://ems.press/content/serial-article-files/32826)) | The theorem needs length at least X^θ with fixed θ>.55, and sums the actual μ. Kernel m intervals have width exponent at most 1/2 relative to their centers; first-prime stopped intervals have exponent at most 3/7. β_U and the changing V_N^* are also different weights. A long d-range version does not eliminate its uncontrolled kernel selection. |
| Matomäki–Shao–Tao–Teräväinen, *Higher uniformity of arithmetic functions in short intervals I*, Theorem 1.1 ([primary text, v4](https://arxiv.org/html/2204.03754v4)) | Its μ/Λ tests are controlled nilsequences with displayed interval and complexity hypotheses. No such representation of this selected prime-divisor kernel has been supplied; the μ/Λ interval thresholds in that theorem exceed the present kernel exponent. |

These are checks of those particular results, not an exclusion of all
possible methods. The already audited 007 and 021 tools retain their
original application gaps; neither is newly admitted as a terminal
signed estimate. No almost-all result is substituted at the fixed center
N², and no new signed-cancellation theorem is assumed.

## 8. Verification and the next analytic step

Run `python3 src/signed_kernel_estimation.py` from the campaign directory.
It verifies the exact kernel identity by independently enumerating the
boundary family and integer cofactors, compares both least-prime blocks
with the original outer weights, and checks the joint reference
discrepancy with exact coefficients of log b/log(x/d). It also checks
activated unit rows, both Möbius signs, repeated/shared small primes,
the rough-part injection, disjoint cofactor cells, the actual β
majorant, and rational source-length/error exponents.

The finite reference windows are explicitly artificial 3N+1 windows for
testing the algebra. They do not test the asymptotic reference main term
or the .011u estimate. Actual and stress U values remain separately
labeled. The proof of the analytic bounds is above; finite checks cannot
certify their asymptotic constants.

All six fixtures passed on 564,796 short/reference sites, independently
enumerating 120,405 rough kernel-cofactor sites. They exercised 28,095
activated unit rows, 64,731 positive and 7,436 negative active nonrough
sites, both Möbius signs, 51,385 repeated-q and 21,088 shared-d sites.
Another 119,340 actual-β envelope checks passed, including 103,054 exact
high least-prime sign identities and 46,994 nonrough sign checks.

The unresolved concrete estimate is (3), with the q≤U^ε discrepancy
the remaining block not even bounded at u scale by this argument, and
the joint sharp coefficient still unresolved across the blocks. A
successful next step must estimate the actual signed discrepancies or
compare them with E_R; a nonnegative divisor envelope with an unspecified
constant is insufficient.

All 214 nonmutable checkpoint-18 records and the negative-frontier ledger
are preserved. The frozen previous manifest is
results/checkpoint18_preservation_manifest.json. This checkpoint adds
the stated partial analytic bounds and exact reference/error interface;
it credits no new prime lower-bound mass.
