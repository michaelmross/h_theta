# The joint remainder: removing the comparator and widening Type I

Checkpoint 11 — Michael M. Ross's H(ϑ) campaign — 6 October 2026

The requested uniform bound
\[
\Delta_2+\Delta_3\le(0.011+o(1))u
\]
has not been completed. This investigation proves three further inputs: all normalized long-reference remainders are negligible; the complete Type I floor error is uniformly negligible through outer product \(N^{9/8}\); and the actual truncated-Möbius Type II coefficient has uniform dyadic mean square \(O(M)\).

The resulting remaining target contains only the actual short window:
\[
\boxed{\Delta_2+\Delta_3=B_N(J)+R_{I,\mathrm{core}}(J)+o(u).} \tag{1}
\]
The Type I core is supported only on two-prime products
\[
N^{9/8}<d\le N^{4/3}.
\]
Neither this core nor the Type II term has the needed joint uniform bound. No terminal comparison, positive certified \(K\), or proof of \(H(\vartheta)\) is admitted.

## 1. Fixed notation and the exact coefficients

Retain all the definitions of TWO_THREE_BILINEAR_NOTE:
\[
x=N^2,\quad Y=N+1,\quad u=N/(2\log N),\quad
z=N^{1/4},\quad w=N^{19/20},
\]
with \(N\) even. The integer short interval is
\[
J=[x-N/2,x+N/2]\cap\mathbb Z.
\]
Its real window is \(J_{\mathbb R}=(x-Y/2,x+Y/2)\). Put
\[
H_1=2\lfloor x e^{-3(\log x)^{1/3}}/2\rfloor+1,\quad
B_1=(x-H_1/2,x+H_1/2)\cap\mathbb Z,\quad
a=Y/H_1,\quad \rho=H_1/x.
\]
All cutoffs and coefficients are fixed at \(x\) throughout each comparison.

The bounded outer coefficient is
\[
c_N(d)={\bf1}_{\,d\ {\rm prime},\,z\le d<w}
 +\frac12\sum_{\substack{p,r\ge z\ {\rm prime}\\pr=d}}
 {\bf1}_{\,pr\max(p,r)\le x}.
\]
It satisfies \(0\le c_N(d)\le1\), with support in
\([N^{1/4},N^{4/3}]\). The actual cofactor range is between constant multiples of \(N^{2/3}\) and \(N^{7/4}\).

Use the unchanged truncations and coefficient
\[
U=V=\lfloor N^{1/100}\rfloor,\qquad
\beta_U(m)=\sum_{\substack{t\mid m\\t>U}}\mu(t).
\]
Thus the remaining Type II count is exactly
\[
B_N(W)=\sum_d c_N(d)
 \sum_{\substack{m>U\\b>V}}
 \frac{\beta_U(m)\Lambda(b)}{\log(mb)}{\bf1}_W(dmb). \tag{2}
\]
No arbitrary outer weights or cofactor prime indicators are substituted for these coefficients.

Let \(I_1,I_2,G\) be the Type I sums and density in checkpoint 10, so
\[
A_N(W)=I_1(W)+I_2(W)+B_N(W),\qquad
A_N(W)=\sum_d c_N(d)\sum_q\frac{\Lambda(q)}{\log q}{\bf1}_W(dq).
\]
For any fixed outer subset \(\mathcal D\), write
\[
R_{I,\mathcal D}(W)=I_{1,\mathcal D}(W)+I_{2,\mathcal D}(W)
 -\int_{W_{\mathbb R}}G_{\mathcal D}(v)\,dv.
\]
These are signed lattice-minus-integral errors. The short Type I counts themselves have a main term and are not being declared negligible.

## 2. The normalized long-reference Type I floor error is negligible everywhere

The weighted lattice error for one \(d,t\) Type I row is \(O(1)\). For a \(d,t,b\) row it is \(O(\Lambda(b)/\log N)\). These bounds were proved in checkpoint 10 using bounded variation of the free-integer weights.

They apply on the long interval as well. Enlarging the outer support to all integers at most \(N^{4/3}\), and using \(U,V\le N^{1/100}\), gives
\[
|R_{I,\mathrm{all}}(B_1)|\ll N^{4/3+1/50}.
\]
Consequently,
\[
a|R_{I,\mathrm{all}}(B_1)|
\ll N^{53/150}\rho^{-1}=o(u). \tag{3}
\]
Indeed \(\rho^{-1}=\exp(3(\log x)^{1/3}+o(1))=N^{o(1)}\), while \(53/150<1\). The same bound holds for every fixed subset of the outer support, including the eventual core.

This uses the actual value of \(a\), rather than the less precise inequality \(a\le1\). No exponential-sum estimate is needed for (3).

## 3. The normalized long-reference Type II term also vanishes

Define the ordinary cofactor-prime density
\[
P_N(v)=\sum_d\frac{c_N(d)}{d\log(v/d)}.
\]
The classical quantitative prime number theorem supplies
\[
\sum_{k\le t}\Lambda(k)=t+O(t e^{-c\sqrt{\log t}}),\qquad
\sum_{k\le t}\mu(k)=O(t e^{-c\sqrt{\log t}}).
\]
One primary exposition is [Tao, 254A Notes 2, Corollary 39 and Exercise 41](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/). Only these long-interval consequences are used.

Partial summation on each cofactor interval, whose endpoints are comparable with \(x/d\), and \(\sum_dc_N(d)/d\ll\log N\), give
\[
a\left|A_N(B_1)-\int_{B_{1,\mathbb R}}P_N(v)\,dv\right|
\ll N\rho^{-1}e^{-c_1\sqrt{\log N}}(\log N)^C=o(u). \tag{4}
\]
The endpoint PNT error is divided by the relative reference length \(\rho\). This is harmless because \((\log N)^{1/2}\) grows faster than \((\log N)^{1/3}\). The argument would not yield this estimate for the actual short window.

For clarity, retain the checkpoint 10 density constants
\[
\alpha_U=\sum_{t\le U}\frac{\mu(t)}t,\quad
\gamma_U=\sum_{t\le U}\frac{\mu(t)\log t}t,\quad
\lambda_V=\sum_{b\le V}\frac{\Lambda(b)}b,\quad
T=\gamma_U+\alpha_U\lambda_V.
\]
Quantitative Möbius partial summation gives, after reducing \(c_2>0\) to absorb fixed logarithms,
\[
\alpha_U=O(e^{-c_2\sqrt{\log N}}),\qquad
\gamma_U=-1+O(e^{-c_2\sqrt{\log N}}),\qquad
T=-1+O(e^{-c_2\sqrt{\log N}}). \tag{5}
\]
The limiting values follow from \(1/\zeta(s)=(s-1)+O((s-1)^2)\); the quantitative Möbius bound makes both weighted tails convergent. A harmonic bound for \(\lambda_V\) suffices.

Since
\[
G(v)=\sum_d\frac{c_N(d)}d
\left(\alpha_U-\frac{T}{\log(v/d)}\right),
\]
(5) implies \(|G(v)-P_N(v)|\ll e^{-c_3\sqrt{\log N}}\log N\) on \([x/2,2x]\). Thus
\[
a\left|\int_{B_{1,\mathbb R}}(G-P_N)(v)\,dv\right|=o(u). \tag{6}
\]
Combining (3), (4), (6), and the exact Vaughan decomposition proves
\[
\boxed{a B_N(B_1)=o(u).} \tag{7}
\]
These arguments are uniform over the actual frozen outer coefficient and its fixed subsets. They supply neither a short prime number theorem nor cancellation in \(B_N(J)\).

## 4. Complete Type I control through outer product \(N^{9/8}\)

The elementary argument already controls \(d\le N^{19/20}\). By itself it extends to any fixed exponent below \(1-2/100=0.98\). The following reciprocal-sum argument goes farther.

On the triprime outer range \(d=pr\le N^{9/8}\), the frozen ordering gate is automatic:
\[
d\max(p,r)\le d^2/z\le N^{9/4-1/4}=x. \tag{8}
\]
Hence the outer coefficient here is simply one half of the ordered prime-pair convolution with \(p,r\ge z\) and the product cutoff. There is no hidden ordering-boundary error in this range.

On a dyadic prime-pair block, let
\[
\sigma=\log_N(PR),\qquad
\alpha=\log_N\min(P,R),\qquad
\tfrac14\le\alpha\le\sigma/2,
\]
up to \(O(1/\log N)\) dyadic constants. Let \(\delta\in[0,1/50]\) be the exponent of the small Vaughan product: \(t\) in \(I_1\), or \(tb\) in \(I_2\). The denominator exponent is
\[
\Sigma=\sigma+\delta.
\]
Collapse the other prime and the small variables into the other denominator slot. Their coefficients have fixed divisor order; prime indicators remain in the separate prime slots.

Use the sharp transfer of NEGATIVE_FRONTIER_NOTE, Section 3. A fixed frequency extension
\[
\nu=1/10000,\qquad
\eta\le\max(0,\Sigma-1)+\nu
\]
includes its smoothing and completion ranges, after choosing their losses small enough. The source phase size is \(X\asymp Hx/Q\), and the standalone reciprocal exponent is \(-1\).

The admitted [Robert–Sargos Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), applied with the smaller prime as standalone variable, requires positive margins in
\[
\begin{aligned}
\alpha&>4\eta+2-2\Sigma,&
\alpha&<\Sigma-3\eta,\\
\alpha&>2\eta,&
\eta&<2-\Sigma.
\end{aligned} \tag{9}
\]
The original FI1989 Theorem 6 instead requires
\[
\begin{aligned}
\alpha&<(8\Sigma-7\eta-6)/7,&
\alpha&<(6\Sigma-5\eta-4)/7,\\
\alpha&<(5\Sigma-5\eta-2)/8,&
\alpha&<(4\Sigma-5\eta-2)/5,\\
\alpha&>\eta,&
\alpha&<(2-\Sigma-\eta)/2.
\end{aligned} \tag{10}
\]
These are the six original facets already audited in FI_1989_AUDIT. FI retains its additive-character frequency restriction; interval completion and smooth partial summation are those verified there.

The following three continuous regions cover every triprime block with \(19/20\le\sigma\le9/8\):

| Outer-product range | Smaller-prime range | Engine | Minimum facet margin |
|---|---|---|---|
| \(19/20\le\sigma\le11/10\) | \(1/4\le\alpha\le\sigma/2\) | RS | \(6/625\) |
| \(11/10\le\sigma\le9/8\) | \(1/4\le\alpha\le59/200\) | FI6 | \(49/10000\) |
| \(11/10\le\sigma\le9/8\) | \(59/200\le\alpha\le\sigma/2\) | RS | \(23/5000\) |

For example, at the upper end of the third region the strongest RS lower edge is \(2\Sigma-2+4\nu\le0.2904\), below \(\alpha\ge0.295\). In the second region the smallest first FI cap is \(0.2999\), above \(\alpha\le0.295\). These gaps overlap rather than leaving a boundary box uncontrolled.

The script verifies every vertex of the three rational polytopes, splitting the RS region at \(\Sigma=1\). All margins are affine on each piece, so this certifies the entire continuous regions rather than sampled parameters. Lower frequencies improve the margins. Dyadic constants, fixed divisor losses, and logarithmic blocks are absorbed by their strict positive gaps.

The sharp product cutoff \(pr\le N^{9/8}\) can be separated by truncated Mellin inversion, using a half-integer product threshold. The resulting prime-slot twists are bounded, and the arbitrarily small truncation error is absorbed in the power saving. Smooth weights depending on \(pr\), including \(1/\log(x/(pr))\), admit the same separation.

The free-variable weights can be frozen at the square center before this transfer. Their variation over \(J_{\mathbb R}\), after including \(\Lambda(b)\) in \(I_2\), is \(O(Y/(x\log N))\). For a denominator \(k\), the resulting lattice/integral error is bounded by this variation times \(O(Y/k+1)\). Summing over the full support costs at most
\[
O(N^{53/150}(\log N)^C)=o(u).
\]
After freezing, the remaining errors are ordinary \(r_k(J)\) with separated smooth coefficient weights; the fixed short-window transfer applies directly. The same source estimates apply to the absolute-coefficient boundary envelopes required for signed smoothing. No estimate for arbitrarily shorter partial intervals is assumed.

The denominator raw-sum savings therefore transfer to the weighted lattice errors. Combining with the elementary low range,
\[
\boxed{R_{I,\,d\le N^{9/8}}(J)=O(N^{1-c_4})=o(u)} \tag{11}
\]
for some fixed \(c_4>0\). Every semiprime outer prime lies in this range. With the centered integral estimate from checkpoint 10, all centered Type I terms on this enlarged range are also \(o(u)\).

## 5. The precise remaining short-window inequality

Define
\[
R_{I,\mathrm{core}}(W)=
I_{1,\,d>N^{9/8}}(W)+I_{2,\,d>N^{9/8}}(W)
-\int_{W_{\mathbb R}}G_{\,d>N^{9/8}}(v)\,dv. \tag{12}
\]
Only two-prime outer products occur here. Its full coefficient still includes the frozen gate \(pr\max(p,r)\le x\).

Checkpoint 10 proved
\(\Delta_2+\Delta_3=\Delta A_N+o(u)\) with uniform ordering and prime-power errors, and proved that \(\Delta\int G=o(u)\). Equations (3), (7), and (11) now give (1).

Thus the remaining sufficient estimate is exactly
\[
\boxed{B_N(J)+R_{I,\mathrm{core}}(J)
\le(0.011+o(1))u} \tag{13}
\]
for every sufficiently large even \(N\). It is still unproved. An upper bound for the signed sum suffices; small separate absolute bounds would be stronger.

The triprime reference coefficient belonging to the proved Type I range is
\[
2\int_{1/2}^{9/8}
\frac{\log(4s-1)}{s(2-s)}\,ds
\in[0.9789675932,\ 0.9791185891]. \tag{14}
\]
The remaining triprime reference coefficient lies in
\([0.2399887785,\ 0.2401808758]\). Including semiprimes, the enlarged Type I domain represents between \(92.1636\) and \(92.1699\) percent of the joint reference mass.

These are reference enclosures only. They do not bound the actual short count or supply an estimate for Type II. In particular the remaining reference mass \(0.2401u\) cannot be replaced by the \(0.011u\) discrepancy allocation.

## 6. The actual Type II coefficient has bounded mean square

For \(m>1\),
\[
\beta_U(m)=-\sum_{\substack{t\mid m\\t\le U}}\mu(t).
\]
[Bretèche–Dress–Tenenbaum (2020), (1.5) and Theorem 1.1](https://tenenb.perso.math.cnrs.fr/PPP/Sxz.pdf) imply
\[
\sum_{M<m\le2M}|\beta_U(m)|^2\ll M \tag{15}
\]
uniformly. If \(U\to\infty\) and \(M/U\to\infty\), this sum is
\((L+o(1))M\), with \(L>0\). Thus the coefficient's mean square stays positive on every fixed dyadic exponent range \(\log_N M>1/100\). This supplies a useful Cauchy input; it supplies no vanishing norm factor by itself.

There is also an elementary exact quadratic form:
\[
Q(U)=\sum_{s,t\le U}\frac{\mu(s)\mu(t)}{[s,t]}
=\sum_{r\le U}\varphi(r)
 \left(\sum_{\substack{t\le U\\r\mid t}}\frac{\mu(t)}t\right)^2.
\]
For integer \(M\ge1\),
\[
\sum_{M<m\le2M}|\beta_U(m)|^2
=\sum_{s,t\le U}\mu(s)\mu(t)
\left(\left\lfloor\frac{2M}{[s,t]}\right\rfloor
-\left\lfloor\frac{M}{[s,t]}\right\rfloor\right)
=MQ(U)+O(U^2). \tag{16}
\]
The nonnegative diagonalization follows from
\((s,t)=\sum_{r\mid(s,t)}\varphi(r)\).

The signs cannot be simplified globally: for \(U=3\), \(\beta_U(6)=1\), whereas \(\beta_U(\ell)=-1\) on primes \(\ell>U\).

For a cofactor \(q\) with \(P^-(q)>U=V\), Vaughan's first Type I weight is one and its second is zero. The Type II cofactor weight is then exactly
\[
\frac{\Lambda(q)}{\log q}-1.
\]
It vanishes on primes and is negative on rough composites. Cofactors with smaller divisors can contribute with the other sign; the full sum cannot be bounded by simply dropping the negative part.

## 7. What the coefficient norm leaves to estimate

There is one more useful separation on the actual short interval. Since \(dq\in J\),
\[
\frac1{\log q}=\frac1{\log(x/d)}
+O\!\left(\frac{Y}{x(\log N)^2}\right).
\]
The absolute representation count satisfies
\(\sum_{dmb=n}|\beta_U(m)|\Lambda(b)\le\tau_4(n)\log n\).
Consequently, for any fixed sufficiently small \(\varepsilon>0\),
\[
B_N(J)=\sum_d\frac{c_N(d)}{\log(x/d)}
\sum_{\substack{m>U\\b>V}}\beta_U(m)\Lambda(b){\bf1}_J(dmb)
+O(N^\varepsilon/\log N). \tag{17}
\]
This is an \(o(u)\) error. It puts the logarithmic coefficient entirely in the fixed outer slot.

Similarly, define
\[
r_k(J)=\left\lfloor\frac{x+Y/2}{k}\right\rfloor
-\left\lfloor\frac{x-Y/2}{k}\right\rfloor-\frac Yk.
\]
The free-weight freezing proved above yields the explicit core form
\[
\begin{aligned}
R_{I,\mathrm{core}}(J)
={}&\sum_{d>N^{9/8}}c_N(d)\sum_{t\le U}\mu(t)
\left(1-\frac{\log t}{\log(x/d)}\right)r_{dt}(J)\\
&-\sum_{d>N^{9/8}}\frac{c_N(d)}{\log(x/d)}
\sum_{\substack{t\le U\\b\le V}}\mu(t)\Lambda(b)r_{dtb}(J)
+o(u). \tag{18}
\end{aligned}
\]
Thus the two still-unestimated contributions can be studied with fixed logarithmic weights and the exact square-centered floor errors.

On a dyadic \(b\)-range, write
\[
V_b=\sum_d\sum_{m>U}
\frac{c_N(d)\beta_U(m)}{\log(mb)}{\bf1}_J(dmb),
\]
where \(d\) ranges over the full outer support.

Cauchy's inequality gives
\[
\left|\sum_{b\sim B,\ b>V}\Lambda(b)V_b\right|^2
\le\left(\sum_{b\sim B}\Lambda(b)^2\right)
 \left(\sum_{b\sim B}|V_b|^2\right). \tag{19}
\]
The second factor contains signed correlations of
\[
c_N(d_1)c_N(d_2)\beta_U(m_1)\beta_U(m_2)
\]
over pairs satisfying both \(d_1m_1b,d_2m_2b\in J\). Hence
\[
|d_1m_1-d_2m_2|\le Y/b.
\]
The diagonal norm (15) does not by itself estimate these nearby-product correlations at the fixed center \(N^2\). A successful refinement must retain the actual prime-supported coefficient and this localization, or estimate the signed joint sum in (13) by another method.

Exact outer divisors of the center can be removed cheaply. There are at most \(\tau(N^2)=N^{o(1)}\) such \(d\), and each \(d\ge z\). Their entire Type II contribution is
\[
O\!\left(\sum_{\substack{d\mid N^2\\d\ge z}}
(Y/d+1)N^\varepsilon\right)=O(N^{3/4+2\varepsilon})=o(u).
\]
Their Type I floor contribution is \(O(UV\,\tau(N^2))=o(u)\), by bounded variation or (18). Thus exact divisibility of an outer product into \(N^2\) is not itself a main-term obstruction. Nearby products remain unestimated.

The direct FI1989 additive mapping and the balanced reciprocal obstruction from checkpoint 10 remain scoped tests. At the balanced triprime endpoint \(\sigma=4/3\), its original incompatible FI6 facets persist; the new coverage below \(9/8\) does not reach that point.

The newer [Pliego monomial paper, Corollary 1.1](https://www.numdam.org/item/10.5802/jtnb.1294.pdf) was also checked. It imposes ordered positive exponents, specified power weights, and a nonrectangular domain. No transfer to the present prime/Möbius coefficient family is supplied there. This is a check of that corollary, not an exhaustive exclusion of newer exponential-sum techniques.

## 8. Exact checks and reproduction

The new script verifies:

- All 32 vertices across the three continuous source-applicability regions, including the \(\Sigma=1\) split, with rational arithmetic.
- Nine exact Möbius energy fixtures, checking both the floor expansion and nonnegative quadratic-form diagonalization.
- Seven actual short-window signed decompositions, including independent evaluation of the Type II divisor sum and the Type I terms as exact coefficients of \(\log p/\log q\).
- The new reference region with 20,000 outward interval cells.

Several small fixtures deliberately use \(U,V>1\) to exercise nontrivial signed coefficients; these are identity checks, not assertions that the asymptotic campaign truncations have those values at small \(N\). The campaign's actual truncations are unchanged.

Run from the project directory:

    python3 src/joint_remainder.py

The script writes results/joint_remainder_*.json. Earlier notes, source bytes, numerical ledgers, and checkpoint 10's exact Vaughan checks are preserved.

The \(0.011u\) bound and the separate higher-degree cap remain unproved. The remaining input is an arithmetic estimate for (13), not further information about the interval or coefficients. This checkpoint narrows that estimate and supplies stronger uniform inputs; it does not complete it.
