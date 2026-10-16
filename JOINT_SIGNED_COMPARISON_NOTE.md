# Joint signed comparison: a budgeted spectral reduction

Checkpoint 23 — Michael M. Ross's H(ϑ) campaign — 10 October 2026

The joint comparison at coefficient .011 is **still unproved**. This
continuation restores checkpoint 22 and investigates that comparison,
rather than the optional separate marked estimate.

There are two new deductions. The original prime-cofactor count has
pointwise multiplicity at most one on the actual square shell, improving
the earlier cap of three. A paired positive smoothing then reduces a
sufficient sharp comparison to a **signed high-frequency integral of the
actual prime-supported coefficients**. Its low-frequency contribution,
its normalized long-reference high-frequency contribution, and its final
frequency tail are o(u), by the admitted long PNT and elementary Mellin
estimates.

With smoothing parameter κ=1/1000, the explicit coefficient ledger is

| Item | Coefficient of u |
|---|---:|
| Original permitted discrepancy | .011 |
| Conservative smoothing charge | .003065 |
| Remaining signed spectral allowance | .007935 |

These are deductions and a sufficient interface, not an estimate of the
remaining spectral integral. No short prime asymptotic or new large-value
theorem is admitted. K remains 0; H(ϑ), the higher-degree allocation and
the separate marked estimate remain open.

## 1. Complete the joint sum before estimating it

All definitions from checkpoints 21–22 remain unchanged:
\[
x=N^2,\quad J=[x-N/2,x+N/2]\cap\mathbb Z,\quad Y=N+1,\quad
u=N/(2\log N),\quad z=N^{1/4},\quad U=\lfloor N^{1/100}\rfloor,
\]
\[
H_1=2\lfloor xe^{-3(\log x)^{1/3}}/2\rfloor+1,\qquad
B_1=(x-H_1/2,x+H_1/2)\cap\mathbb Z,\qquad a=Y/H_1.
\]
N is even. The outer coefficient is exactly
\[
c_N(d)=\mathbf1_{d\ {\rm prime},\,z\le d<N^{19/20}}
+\frac12\sum_{pr=d\atop p,r\ge z\ {\rm prime}}
 \mathbf1_{pr\max(p,r)\le x}.
\]
D_good, its complementary core C, the db>N^(459/400) continuation
gate, the nonunit residual gate, V_N and P_N are frozen as before.
Define, for the complete actual outer support,
\[
Q_N(W)=\sum_d c_N(d)\sum_{q\ {\rm prime}}\mathbf1_W(dq),\qquad
\Pi_{\rm good}=\sum_{d\in D_{\rm good}}
 \frac{c_N(d)}{d\log(x/d)}. \tag{1}
\]

Checkpoint 21's completed identity on both windows gives
\[
\mathcal C_N(J)=Q_N(J)-Y\Pi_{\rm good}+o(u),\qquad
a\mathcal C_N(B_1)=aQ_N(B_1)-Y\Pi_{\rm good}+o(u).
\]
Its exact arithmetic identity is C_N(W)=S(W)−R(W). Thus, for any
least-prime cutoff T≤U,
\[
E_{T<q\le U}-E_R
 =Q_N(J)-aQ_N(B_1)-E_{\le T}+o(u). \tag{2}
\]
Here q on the left denotes the least prime factor; q in (1) denotes
the prime cofactor. These are different roles.

For the checkpoint-22 subpower cutoff T_N, E_≤T_N=o(u). Consequently
the user's original target is equivalent to
\[
\boxed{Q_N(J)-aQ_N(B_1)\le(.011+o(1))u.} \tag{3}
\]
All coefficients are one. No small-cutoff budget is spent in (3).

This equivalence follows from already completed identities. It does not
prove a new sharp prime-product count: checkpoints 9–10 already identified
the centered two- and three-prime count. Its value here is that the joint
high-block/rough comparison can be studied without separately estimating
either signed aggregate or the marked residual slice.

## 2. A sharper pointwise cap on the actual shell

**Proposition.** For all sufficiently large even N and every n∈J,
\[
\boxed{0\le Q_N(\{n\})\le
 \mathbf1_{P^-(n)\ge N^{1/4}}.} \tag{4}
\]
In particular there is at most one eligible prime-cofactor mark, with
weight one or one half.

A single-prime outer row has n=pq, with p<N^(.95). Since the lower
endpoint of J eventually exceeds N^(1.9), q>p and both factors cannot
be eligible single-prime outers. There is at most one such row, and it
is z-rough.

A two-prime outer row has n=prq, p≤r, and the original gate pr²≤x.
If q<r, then
\[
pr^2-n=pr(r-q)\ge pr.
\]
Also (pr)²=p(pr²)>pn≥2(x−N/2), so pr>N/2. But pr²≤x and
n≥x−N/2 require pr²−n≤N/2, a contradiction. Therefore
\[
p\le r\le q.
\]
The outer selects the two smallest factors. It is unique, including
repeated factors, and its canonical weight is one for p<r or one half
for p=r. All three factors are at least z.

The single-prime and two-prime cases concern integers of different
factor degrees. No integer can acquire a mark from both cases.
This proves (4).

The earlier cap of three was valid but unnecessary. Applying the same
deterministic Shiu estimate now needs only one rough indicator. Its
implicit constant still supplies no sharp .011 discrepancy coefficient.
No cap-one statement is asserted on the much wider reference window:
ordering thresholds there require the previously proved freezing error.

## 3. Keep the exact reference coefficient

The original long PNT, prime reciprocal asymptotics and ordering-error
bounds give
\[
aQ_N(B_1)=(M+o(1))u,\qquad
M\in[3.06493405810766331478,\ 3.06497515947581397662]. \tag{5}
\]
These endpoints abbreviate the unchanged outward enclosure in
results/two_three_reference_and_samples.json.

The semiprime contribution is log(19/3). The triprime contribution is
\[
2\int_{1/2}^{9/8}\frac{\log(4s-1)}{s(2-s)}\,ds+
2\int_{9/8}^{4/3}
 \frac{\log((2-s)/(2s-2))}{s(2-s)}\,ds.
\]
Thus (3) asks for a one-sided cap at the exact coefficient M+.011.
A reference coefficient is not an actual short-shell upper bound.
Replacing M by an enclosure endpoint in a proposed proof must retain
the resulting enclosure error.

## 4. Positive smoothing with a visible charge

For h>0 and fixed κ>0 define the trapezoid
\[
\psi_h(v)=
\begin{cases}
1,&|v-x|\le h/2,\\
(h/2+\kappa h-|v-x|)/(\kappa h),
  &h/2<|v-x|<h/2+\kappa h,\\
0,&|v-x|\ge h/2+\kappa h.
\end{cases} \tag{6}
\]
It has mass (1+κ)h and nonnegative values. Write
\[
A_h=\sum_n Q_N(\{n\})\psi_h(n),\qquad
I_\kappa=A_Y-aA_{H_1}. \tag{7}
\]
The coefficients c_N(d) and all their original gates remain frozen at x.
Because ψ_Y=1 on J and Q_N≥0,
\[
Q_N(J)-aQ_N(B_1)
 \le I_\kappa+a(A_{H_1}-Q_N(B_1)). \tag{8}
\]
The second term has the **original** long-reference count inside it.
Partial summation of the admitted PNT, with every outer coefficient
unchanged, gives
\[
a(A_{H_1}-Q_N(B_1))=(\kappa M+o(1))u. \tag{9}
\]
Its additional area is κH_1. The relative width remains
ρ=H_1/x=N^(-o(1)); the long PNT error after scaling is o(u).
This is the required price of smoothing the reference. It cannot be
discarded.

For κ=1/1000, the saved enclosure implies
\[
\kappa M<.003065=\frac{613}{200000}.
\]
Hence
\[
\boxed{I_\kappa\le(.007935+o(1))u,\quad \kappa=1/1000} \tag{10}
\]
is sufficient for the original .011 bound, because
613/200000+1587/200000=11/1000 exactly. Inequality (10) is stronger
than the unsmoothed target in the amount charged for the approximation;
it is not being asserted as an equivalent target.

## 5. An exact Mellin interface with the actual prime coefficients

Use a fixed C² function g supported on [1/2,19/10], equal to one on
[3/5,9/5], and between zero and one elsewhere. An explicit choice uses
H(t)=10t³−15t⁴+6t⁵ on the two transition intervals: g(v)=H(10v−5)
on [1/2,3/5], and g(v)=H(19−10v) on [9/5,19/10].
For all sufficiently large N, every prime cofactor counted in J, B_1
or either smoothed window lies in this plateau.

Define the finite Dirichlet polynomials
\[
\mathscr D_N(t)=\sum_d\frac{c_N(d)}{d^{1+it}},\qquad
\mathscr P_N(t)=\sum_{q\ {\rm prime}}
 \frac{g(\log q/\log N)}{q^{1+it}}. \tag{11}
\]
The padding changes no count inside the relevant windows. It is not a
replacement of prime indicators by arbitrary coefficients.
The inherited reciprocal asymptotics give
\[
|\mathscr D_N(t)|+|\mathscr P_N(t)|\ll1 \quad(t\in\mathbb R). \tag{12}
\]

Put l_h=x−h/2−κh, b_h=x−h/2, c_h=x+h/2 and r_h=x+h/2+κh.
Twice integrating (6) by parts gives
\[
\widehat\psi_h(s)=\int_0^\infty\psi_h(v)v^{s-1}\,dv
=\frac{l_h^{s+1}-b_h^{s+1}-c_h^{s+1}+r_h^{s+1}}
 {\kappa h\,s(s+1)}. \tag{13}
\]
Let
\[
K_N(t)=\widehat\psi_Y(1+it)-a\widehat\psi_{H_1}(1+it).
\]
Mellin inversion gives the absolutely convergent identity
\[
\boxed{I_\kappa=\frac1{2\pi}
 \int_{\mathbb R}\mathscr D_N(t)\mathscr P_N(t)K_N(t)\,dt.} \tag{14}
\]
Exact equality of the two normalized trapezoid areas gives K_N(0)=0.
The integral is real by conjugation symmetry; its integrand is signed.

Useful elementary bounds, for fixed κ, are
\[
|K_N(t)|\le2(1+\kappa)Y,\qquad
|\widehat\psi_h(1+it)|
 \ll\frac{x^2}{\kappa h(1+t^2)}. \tag{15}
\]
The latter bound follows directly from (13); all endpoints are
comparable to x.

## 6. The low frequencies and long-reference high frequencies are negligible

This is a new analytic deduction from the admitted long PNT.
It holds uniformly in all sufficiently large even N.

Set
\[
\mathscr L_N(t)=\int_0^\infty
 \frac{g(\log v/\log N)}{\log v}\,v^{-1-it}\,dv
=\int_{1/2}^{19/10}\frac{g(b)}b e^{-itb\log N}\,db.
\]
The quantitative PNT and partial summation supply some c_0>0 and fixed C
such that
\[
\mathscr P_N(t)-\mathscr L_N(t)
 \ll(1+|t|)(\log N)^C e^{-c_0\sqrt{\log N}}. \tag{16}
\]
Only primes at least N^(1/2) occur in this step. No short-interval
prime theorem is used. Choose
\[
T_0=\exp\{(c_0/4)\sqrt{\log N}\}. \tag{17}
\]
By (12), (15) and (16), replacing the prime polynomial by its PNT model in the part of (14)
with |t|≤T_0 costs
\[
O\!\left(YT_0^2(\log N)^C e^{-c_0\sqrt{\log N}}\right)=o(u).
\]

The C² padding, with piecewise integrable third derivative, allows three
integrations by parts:
\[
\mathscr L_N(t)\ll (|t|\log N)^{-3}\quad(|t|\ge1).
\]
Therefore the model integral outside |t|≤T_0 is o(u), using the
uniform first bound in (15).

The complete model integral has density
\[
G_N(v)=\sum_d\frac{c_N(d)}{d\log(v/d)}
\]
on all the relevant windows, since g=1 there. Throughout them,
\[
|G_N(v)-G_N(x)|\ll
 \frac{|v-x|}{x(\log N)^2}.
\]
The constant density cancels because the paired areas are equal.
The remaining model contrast is
O(Yρ/(\log N)²)=o(u). Combining these estimates proves
\[
\boxed{\frac1{2\pi}\int_{|t|\le T_0}
 \mathscr D_N(t)\mathscr P_N(t)K_N(t)\,dt=o(u).} \tag{18}
\]

The normalized long-reference part above T_0 is also negligible,
this time without replacing primes by a model. By (12) and (15),
\[
a\int_{|t|>T_0}|\mathscr D_N(t)\mathscr P_N(t)
 \widehat\psi_{H_1}(1+it)|\,dt
 \ll_\kappa\frac{Y\rho^{-2}}{T_0}=o(u). \tag{19}
\]
Here ρ^(-2)=exp(6(log x)^(1/3)+o(1)), whereas T_0 grows as
exp(c√log N). This comparison is why the inherited reference length
is sufficient. The reference is removed only after this estimate
and the explicit smoothing charge (9).

Finally (12) and (15) bound the short-window frequency tail beyond
\[
T_1=N^{21/10}
\]
by O_κ(x²/(YT_1))=O_κ(N^(9/10))=o(u).

Consequently define the real signed integral
\[
\mathfrak H_\kappa(N)=\frac1\pi\Re
 \int_{T_0}^{N^{21/10}}
 \mathscr D_N(t)\mathscr P_N(t)\widehat\psi_Y(1+it)\,dt.
\]
Equations (18)–(19) and the absolute final tail prove
\[
\boxed{I_\kappa=\mathfrak H_\kappa(N)+o(u).} \tag{20}
\]
A concrete sufficient remaining estimate is therefore
\[
\boxed{\mathfrak H_{1/1000}(N)
 \le\left(\frac{1587}{200000}+o(1)\right)u.} \tag{21}
\]
This **signed** integral bound is open. The center-dependent phase is
already in (13); it has not been averaged over N. Replacing the integral
by an absolute norm or importing an almost-all-interval estimate would
require its own coefficient and uniformity argument.

## 7. Explicit fixed-power budgeting if another method needs it

This section keeps the separate least-prime cutoff budget visible.
No fixed least-prime power cutoff is needed in Sections 4–6.

Write A=100δ_0 and retain the actual constant C′ of checkpoint 22, (23).
For a desired budget ξ>0, set
\[
s_\xi=\max\left(128,\ 
 2\log\max\left(1,\frac{C'}{\xi A^2}\right)\right),\qquad
\varepsilon=A/s_\xi. \tag{22}
\]
This is within the permitted small-power range. For s≥128,
s²≤e^(s/2), so
\[
C'\varepsilon^{-2}e^{-A/\varepsilon}
 =\frac{C'}{A^2}s_\xi^2e^{-s_\xi}\le\xi.
\]
Thus checkpoint 22, (23) gives
\[
|E_{\le U^\varepsilon}|\le(\xi+o_\varepsilon(1))u.
\]
The corresponding sufficient high-block comparison is
\[
E_{U^\varepsilon<q\le U}-E_R
 \le(.011-\xi+o(1))u. \tag{23}
\]
For ξ=.001, its coefficient is .010. This does not provide a numerical
ε: δ_0 and C′ have not been numerically certified. Formula (22) is an
explicit choice in those admitted constants, not an invented value.
If a further argument incurs both this loss and a smoothing loss, both
must be charged; their budgets cannot each be spent against the same .011.

## 8. Method audit and verification

The spectral reduction supplies a new interface and removes its low
frequencies. It does not establish a saving for the actual high-frequency
prime product. The published examples checked in this continuation do
not supply that missing theorem:

- Matomäki–Teräväinen, *Almost primes in almost all short intervals II*,
  Theorem 1.2, supplies E₃ existence in every interval of length
  √x(log x)^1.55. It is neither an upper count nor a result at length
  √x with the campaign's polynomial roughness restrictions.
  Source: https://arxiv.org/pdf/2207.05038
- Benatar, *A short-interval Hildebrand–Tenenbaum theorem*, Theorem 1.1,
  assumes length at least x^(7/12+ε), and counts distinct prime factors.
  It does not apply to this square-root shell or automatically to its
  restricted two/three-prime kernel.
  Source: https://arxiv.org/html/2408.16576v1

No broader claim excluding other methods is made.

Run python3 src/joint_signed_comparison.py. Its exact checks cover the
coefficient-one small/high/rough partition with the original continuation,
residual-beta invariance, repeated-prime rows, the unique short-shell
prime-cofactor mark, smooth prime padding, independent rational Mellin
moments, equal paired areas, rational coefficient accounting, and the
absolute-tail exponent. Stress U and an artificial long window are
explicitly labeled. Finite arithmetic checks do not prove (18) or (21);
(18) has the analytic proof above, while (21) remains unproved.

All 238 nonmutable checkpoint-22 records and the negative-frontier ledger
are preserved byte for byte. The previous manifest is saved separately.
Only current indices are updated.

| Claim | Status |
|---|---|
| Subpower joint target equals the original centered Q_N target | Deduction from checkpoints 21–22 |
| Actual-shell prime-cofactor mark cap one | Proved here |
| Positive paired smoothing and explicit .003065 charge | Proved here |
| Low Mellin frequencies and long-reference high tail | o(u), proved from admitted long PNT and elementary bounds |
| Final frequency tail beyond N^(21/10) | o(u), proved here |
| Signed intermediate-frequency cap .007935 | Open |
| Original .011 comparison, separate marked bound, higher-degree cap, H(ϑ) | Open; K=0 |

