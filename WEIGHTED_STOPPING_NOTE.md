# First-prime stopping for the remaining delta estimate

Checkpoint 16 — Michael M. Ross's H(ϑ) campaign — 8 October 2026

Stopping at the canonical first outer prime gives intervals on which the
**actual** truncated Möbius weight has uniformly controlled mean and second
moment. This avoids the short coordinate lengths that blocked the direct
021 mapping. The remaining Type II sum and prime-cofactor core then become
one explicitly defined, locally centered covariance, with every actual
support and selection gate retained.

The one-sided covariance estimate needed for the .011u allocation is
**not proved**. This is a proved arithmetic localization and moment
estimate, together with a restricted positive-weight extension of 021's
stopped comparison. It credits no new lower-bound mass: K=0 and H(ϑ)
remain open. The higher-degree allocation remains a separate open task.

## 1. The input being continued

Keep the even-N square shell and the campaign's actual truncation:
\[
x=N^2,\quad J=[x-N/2,x+N/2]\cap\mathbb Z,\quad
u=\frac{N}{2\log N},\quad z=N^{1/4},\quad
U=\lfloor N^{1/100}\rfloor.
\]
For m>1,
\[
\beta_U(m)=\sum_{\substack{t\mid m\\t>U}}\mu(t)
=-\sum_{\substack{t\mid m\\t\le U}}\mu(t),\qquad \beta_U(1)=0.
\tag{1}
\]
In particular β_U(m)=0 for 1<m≤U. If every prime factor of a exceeds U
and m>1, then β_U(am)=β_U(m). This assertion also permits repeated
large prime factors; it does not assert that β_U is multiplicative.

The frozen outer coefficient is
\[
c_N(d)=\mathbf1_{d\ {\rm prime},\ z\le d<N^{19/20}}
+\frac12\sum_{\substack{pr=d\\p,r\ge z\ {\rm prime}}}
\mathbf1_{pr\max(p,r)\le x},\qquad
\gamma_N(d)=c_N(d)\frac{\log N}{\log(x/d)}.
\tag{2}
\]
For canonical pairs p≤r write e_{p,r}=1 when p<r and e_{p,p}=1/2.
All pair sums below retain pr²≤x.

Let D_good be the supported outer products satisfying d≤N^(457/400),
or one of the two additional pair tests:
\[
\begin{array}{ll}
pr^2\le N^{3919/2000},&p^3r^2\le N^{7399/2500},\\
pr^2\le N^{3959/2000},&p^3r^2\le N^{7349/2500}.
\end{array}
\tag{3}
\]
Let C be its complement within the actual outer support, and put
D_B=N^(459/400). Checkpoint 14 proved
\[
\Delta_2+\Delta_3
=B_{D_{\rm good},\,db>D_B}(J)+A_C(J)-(M_C+o(1))u.
\tag{4}
\]
The preserved enclosure is
\[
0.088495462680506291767141069549718388565758372430595
\le M_C\le
0.088532079408569630135767526784074925416683359058930.
\tag{5}
\]
A_C uses the Mangoldt/log prime-power weight. Proper prime-power
cofactors in A_C and proper prime powers in the Type II b slot have
already been bounded by o(u), uniformly on selected subsets. After
the previously proved freezing of the logarithmic denominator,
the prime-b version of the first term in (4) is
\[
\sum_{d\in D_{\rm good}}\frac{c_N(d)}{\log(x/d)}
\sum_{\substack{b>U\ {\rm prime}\\db>D_B}}\log b
\sum_{\substack{m>U\\dmb\in J}}\beta_U(m)+o(u).
\tag{6}
\]
These o(u) errors are inherited from checkpoints 10–14, rather than
deduced from the finite tests accompanying this note.

## 2. A stop before the coordinate interval collapses

For a single-prime outer product stop at p=d. For a canonical pair
outer product d=pr, p≤r, stop at p. Its ordering gate gives p³≤pr²≤x,
so p≤N^(2/3). Consequently every actual outer row has a stop in
\[
\mathcal P_N=\{p\ {\rm prime}:z\le p<N^{19/20}\}.
\]
Define the **full** stopped interval
\[
I_p=\{k\ge1:pk\in J\},\qquad H_p=\#I_p.
\]
Its real width and site count satisfy
\[
N/p>N^{1/20},\qquad H_p=N/p+O(1).
\tag{7}
\]
In particular H_p≥N^(1/20)/2 for all sufficiently large N, uniformly
in p. Also p>U and every k∈I_p is greater than 1. Thus
\[
\beta_U(pk)=\beta_U(k)
\tag{8}
\]
exactly throughout each stopped interval.

This is an exact one-layer regrouping. It does not claim to construct
021's even-node Buchstab stopping tree or to inherit that tree's lower
comparison. The later pair and continuation conditions are carried as
weights on I_p; their conditional distribution has not been estimated.

## 3. Uniform local moments with the actual power cutoff

Put
\[
\alpha_U=\sum_{t\le U}\frac{\mu(t)}t,\qquad
q(U)=\sum_{s,t\le U}\frac{\mu(s)\mu(t)}{[s,t]}.
\]
On any interval of H consecutive integers greater than 1, counting
multiples of t differs from H/t by less than 1. Expanding (1) and its
square therefore gives, with explicit absolute errors,
\[
\sum_{k\in I_p}\beta_U(k)=-H_p\alpha_U+E_{1,p},
\quad |E_{1,p}|\le U,
\]
\[
\sum_{k\in I_p}\beta_U(k)^2=H_pq(U)+E_{2,p},
\quad |E_{2,p}|\le U^2.
\tag{9}
\]
These bounds are uniform in the center of I_p. No small-prime pattern
equidistribution theorem or fixed-translation hypothesis is used.

With \(\bar\beta_p=H_p^{-1}\sum_{I_p}\beta_U\), equations (7)–(9) imply
\[
\bar\beta_p=-\alpha_U+O(N^{-1/25}).
\tag{10}
\]
The exact centered energy is
\[
\begin{split}
\sum_{I_p}|\beta_U-\bar\beta_p|^2
={}&H_p(q(U)-\alpha_U^2)\\
&+E_{2,p}+2\alpha_UE_{1,p}-E_{1,p}^2/H_p.
\end{split}
\tag{11}
\]
Since |α_U|≤U and H_p≥1, the error on the second line is at most 4U².
Its error relative to H_p is uniformly O(N^(-3/100)).

The previously admitted long Möbius estimate gives
α_U=O(exp(−c√log N)). The BDT input already used in
COFACTOR_ESTIMATE_NOTE.md gives q(U)→L>0. Hence, uniformly on every
stopped interval,
\[
\sum_{I_p}|\beta_U-\bar\beta_p|^2=(L+o(1))H_p.
\tag{12}
\]
The power cutoff U causes no moment-length mismatch at these first-prime
stops: U²/H_p≪N^(-3/100). This statement concerns the **full** I_p,
not an interval subsequently restricted by prime-divisor or avoidance
conditions.

The prime reciprocal estimate, already available from the admitted
quantitative PNT, gives
\[
\sum_{p\in\mathcal P_N}H_p
=N\sum_{z\le p<N^{19/20}}\frac1p+O(N^{19/20})
=(\log(19/5)+o(1))N.
\tag{13}
\]
Summing the error in (11) costs O(U²N^(19/20))=O(N^(97/100))=o(N).
Thus the aggregate centered beta energy is
\[
\mathcal E_N:=\sum_p\sum_{I_p}|\beta_U-\bar\beta_p|^2
=(L\log(19/5)+o(1))N.
\tag{14}
\]
For any numbers a_p bounded by an absolute constant, (9) and (13) give
the useful uniform centering bound
\[
\left|\sum_pa_p\sum_{I_p}\beta_U\right|
\ll N e^{-c\sqrt{\log N}}+N^{24/25}=o(u).
\tag{15}
\]

## 4. Carrying the actual continuation through the stop

Define nonnegative, dimensionless continuation weights on I_p:
\[
v_p^{(1)}(k)=\frac1{\log(x/p)}
\sum_{\substack{b\mid k\\b>U\ {\rm prime}\\pb>D_B\\k/b>1}}\log b,
\]
\[
v_p^{(2)}(k)=
\sum_{\substack{r\mid k\\r\ge p\ {\rm prime}\\pr^2\le x\\pr\in D_{\rm good}}}
\frac{e_{p,r}}{\log(x/(pr))}
\sum_{\substack{b\mid k/r\\b>U\ {\rm prime}\\prb>D_B\\k/(rb)>1}}\log b,
\quad v_p=v_p^{(1)}+v_p^{(2)}.
\tag{16}
\]
All single-prime outer products are in D_good. The r≥p condition
also enforces r≥z, so no outer support has been enlarged. The db gate
remains **inside** each continuation weight.

Removing the large primes p, r and b from β is valid when the remaining
m>1. Extending m>U to m>1 adds only zero rows, since β_U(m)=0 for
1<m≤U. The unit cofactor is explicitly excluded. Consequently (6) is
\[
B_{D_{\rm good},\,db>D_B}(J)
=\sum_p\sum_{k\in I_p}\beta_U(k)v_p(k)+o(u).
\tag{17}
\]

For the complementary core define the marked prime count
\[
P_p(k)=\sum_{\substack{r\mid k\\r\ge p\ {\rm prime}\\pr^2\le x\\pr\in C}}
e_{p,r}\mathbf1_{k/r\ {\rm prime}}.
\tag{18}
\]
Every supported pair has pr≤N^(4/3), so its cofactor in J is
≫N^(2/3)>U. On the support of (18), k=rℓ with r and ℓ both prime and
greater than U. Therefore β_U(k)=−1, including repeated-prime cases,
and
\[
A_C(J)=\sum_p\sum_{I_p}P_p(k)+o(u)
=-\sum_p\sum_{I_p}\beta_U(k)P_p(k)+o(u).
\tag{19}
\]

There is at most one eligible r at a given core site. Indeed, if r>ℓ,
then pr²−prℓ=pr(r−ℓ)≥pr>N^(457/400)>N, whereas pr²≤x and
prℓ∈J require pr²−prℓ≤N/2. This is impossible. Thus only the smaller
of the two prime factors of k can be r. It follows that 0≤P_p(k)≤1.

Let
\[
Z_p(k)=v_p(k)-P_p(k).
\tag{20}
\]
Combining (17) and (19) gives the single joint identity
\[
B_{D_{\rm good},\,db>D_B}(J)+A_C(J)
=\sum_p\sum_{I_p}\beta_U(k)Z_p(k)+o(u).
\tag{21}
\]
The cancellation on composite core rows from checkpoint 14 has not
been replaced by a separate positive charge.

The old actual-weight bound gives
\(\sum_{p\mid n}v_p(n/p)\le(36+o(1))\) on n∈J. To see its applicability,
each canonical outer product occurs once in this sum, and the inner
prime-divisor logarithms sum to at most log(n/d). The total outer
coefficient is at most 36, and log(n/d)/log(x/d)=1+o(1) uniformly on
support. Hence 0≤v_p≤36+o(1), −1≤Z_p≤36+o(1), and the actual mean
\(\bar Z_p=H_p^{-1}\sum_{I_p}Z_p\) is bounded by an absolute constant.

## 5. What is now proved, and the estimate still needed

Define the covariance with actual local means:
\[
\mathcal C_N=\sum_{p\in\mathcal P_N}\sum_{k\in I_p}
(\beta_U(k)-\bar\beta_p)(Z_p(k)-\bar Z_p).
\tag{22}
\]
Exact local centering gives
\[
\sum_p\sum_{I_p}\beta_U Z_p
=\mathcal C_N+\sum_p\bar Z_p\sum_{I_p}\beta_U.
\]
Equation (15) makes the last term o(u), even though each \(\bar Z_p\)
depends on N and p. Thus (4) and (21) imply
\[
\boxed{\Delta_2+\Delta_3=\mathcal C_N-(M_C+o(1))u.}
\tag{23}
\]
The exact remaining one-sided requirement is
\[
\boxed{\mathcal C_N\le(M_C+.011+o(1))u.}
\tag{24}
\]
The reference subtraction M_C is essential. The positive core prime
count is part of this covariance; mean-zero β on the full I_p does
not make its covariance with the selected continuation small.

For comparison, let
\[\mathcal V_N=\sum_p\sum_{I_p}|Z_p-\bar Z_p|^2.\]
The available Cauchy bound is
\[
|\mathcal C_N|\le\sqrt{\mathcal E_N\mathcal V_N}.
\tag{25}
\]
Boundedness of Z alone gives \(\mathcal V_N=O(N)\), and therefore only
O(N), losing the logarithm needed at scale u. An **optional sufficient**
variance input would be
\[
\mathcal V_N\le
\left(\frac{(M_C+.011)^2}{4L\log(19/5)}+o(1)\right)
\frac{N}{(\log N)^2}.
\tag{26}
\]
This strong absolute-value route is neither proved nor necessary for
the one-sided target. The uniform local beta moments are now settled;
the conditional covariance with (16)–(18) remains the analytic task.

## 6. A positive-weight extension of the 021 comparison

The proof of 021 Proposition 10.5, audited in checkpoint 15, supplies
on each **complete eligible owner group** a nonnegative actual count
S_i and a positive reference scale T_i with
\[
\sum_i S_i\ge .34\sum_iT_i,\qquad R_i\le .33T_i.
\tag{27}
\]
Here T_i denotes J_iV_all(P), not the auxiliary survivor count denoted
T_p in the source. The source's .34 lower bound even uses the full
bin's scale before restricting to the owner group; (27) is its weaker
consequence on that group. Its uniformity and complete-group
hypotheses remain required.

For positive weights with a_min≤a_i≤a_max and
a_max/a_min≤1+ε, positivity of S_i and the individual reference cap give
\[
\sum_i a_i(S_i-R_i)
\ge a_{\min}(.01-.33\varepsilon)\sum_iT_i.
\tag{28}
\]
Thus the source sign survives a weight ratio at most 34/33. For
ε=1/100 the retained coefficient is exactly 67/10000.

In a bin p∈[R,(1+ξ)R], fixing the other outer factors q′ and keeping
c_N(pq′) constant gives a_p=c_N(pq′)log N/log(x/(pq′)). Since actual
outer support has pq′≤N^(4/3),
\[
\frac{a_{\max}}{a_{\min}}
\le1+\frac{3\log(1+\xi)}{2\log N}.
\tag{29}
\]
For fixed ξ this eventually meets (28). This resolves the **outer
logarithmic weight** issue wherever a full eligible source group has
constant support and gates. It does not show that the delta continuation
defines such a group. A bin intersecting an ordering, D_good or db
boundary cannot be discarded using its reference mass alone. Complex
Mellin weights do not meet the positive-weight hypotheses either.

There are two exact cautions about extending (28):

1. A sharp nonnegative selection need not preserve the grouped sign.
   Take S=(0,17/25), R=(33/100,33/100), T=(1,1). These satisfy (27),
   and the unweighted correction is 1/50. Weights (1,0) give −33/100.
   This is a counterexample to an unrestricted weighted inference,
   **not a counterexample to 021**.
2. The actual β_U can be negative throughout a group. For U=5 and
   k=77, both tag primes p=13,17 give β_U(pk)=−1. More generally it
   equals −1 on every U-rough integer greater than 1. Multiplying a
   positive grouped correction by this weight reverses its sign.
   This blocks automatic transfer of 021's lower comparison; it does
   not disprove the campaign's one-sided upper estimate.

## 7. Verification and the next analytic task

Run `python3 src/weighted_stopping.py` from the campaign directory.
The checks independently enumerate the original outer products and
the first-prime continuation, preserving canonical half weights,
all ordering and product gates, m>U and the zero extension to m>1.
They compare exact coefficients of the formal symbols
X_(d,b)=log(b)/log(x/d), and also check the core prime identity, local
moments and exact local centering. No floating logarithms are used.

Actual campaign truncations and larger stress truncations are labeled
separately. Finite fixtures test these identities, not (24). Historical
checkpoint-15 records and the frozen analytic ledger are verified by
size and SHA-256 before the new result files are written.

All seven fixtures passed: 42,407 stopped sites, 53,719 original prime-b
rows and 149 core prime-cofactor rows. The stress fixtures exercise
negative, zero and positive beta values and the zero extension in (17).
All 194 nonmutable checkpoint-15 records verified unchanged.

The next analytic step is to estimate (22) with the actual continuation
weights, or to construct a signed comparison whose boundary is exactly
(21) and which proves (24). Any use of 021 must supply the missing
complete-group and signed-weight argument. Applying the local moment
formula after a prime or avoidance restriction would require a new
conditional estimate; equations (9)–(15) alone do not supply it.

The prior core enclosure, .011u allocation, analytic ledger, higher-degree
task and certified K are unchanged.
