# The centered two- and three-prime estimate: bilinear reduction

Checkpoint 10 — Michael M. Ross's H(ϑ) campaign — 6 October 2026

The estimate \(\Delta_2+\Delta_3\le(0.011+o(1))u\) has not been proved. This investigation proves a uniform reduction to explicit Vaughan Type II sums and a high-outer Type I floor-error sum. The complete semiprime Type I contribution, and the triprime Type I contribution with two-prime outer product at most \(N^{0.95}\), are uniformly negligible after centering. Prime-power contamination and the freezing of the triprime ordering condition are also uniformly \(o(u)\).

These are arithmetic reductions with the actual coefficients. They admit no new terminal prime comparison, no positive certified \(K\), and no proof of \(H(\vartheta)\).

## 1. The target and the exact windows

Use \(x=N^2\), \(N\) even, \(Y=N+1\), \(u=N/(2\log N)\), \(z=N^{1/4}\), and \(w=N^{19/20}\). The actual interval is
\[
J=[N^2-N/2,N^2+N/2]\cap\mathbb Z.
\]
The original reference length is \(Y_1=x\exp(-3(\log x)^{1/3})\). Put
\[
H_1=2\lfloor Y_1/2\rfloor+1,\qquad
B_1=(x-H_1/2,x+H_1/2)\cap\mathbb Z,\qquad a=Y/H_1.
\]
Both real windows have half-integer endpoints. Write \(\Delta F=F(J)-aF(B_1)\). The original normalization and endpoints differ by \(o(u)\), as proved in checkpoint 9. All subsequent identities use these exact rounded windows; \(a\le1\) for all sufficiently large \(N\).

The factorial prime-product definitions of \(M_2,M_3\) remain those in RESTRICTED_FRONTIER_NOTE. The working sufficient allocation is
\[
\Delta M_2+\Delta M_3\le(0.011+o(1))u. \tag{1}
\]
It would suffice together with the separate, still-unproved bound
\[
\sum_{j=4}^{7}M_j(J)\le(2C_{\ge4}+o(1))u.
\]
Equation (1) is an optional allocation of the total \(0.338u\) budget, not a necessary consequence of the full target.

## 2. An exact orientation and a frozen outer coefficient

For sufficiently large \(N\), both windows have lower endpoint greater than \(w^2\). Hence
\[
M_2(W)=\sum_{\substack{z\le p<w\\p\ {\rm prime}}}
       \sum_{q\ {\rm prime}}{\bf1}_W(pq). \tag{2}
\]
The cofactor is greater than \(p\); no square row occurs.

For triprimes introduce the largest-cofactor orientation
\[
T_3(W)=\frac12
 \sum_{\substack{p,r\ge z\\p,r\ {\rm prime}}}
 \sum_{\substack{q\ {\rm prime}\\q\ge\max(p,r)}}{\bf1}_W(prq).
\]
Its exact diagonal correction is
\[
T_3(W)-M_3(W)
=\frac12\sum_{\substack{z\le p<r\\p,r\ {\rm prime}}}{\bf1}_W(pr^2)
 +\frac13\sum_{\substack{p\ge z\\p\ {\rm prime}}}{\bf1}_W(p^3). \tag{3}
\]
For example, \(p r^2\), \(p<r\), has coefficient one in \(T_3\) and one half in \(M_3\); \(p^3\) has coefficients one half and one sixth. The repeated-large-prime bound from checkpoint 9 makes the centered correction in (3) \(O(N^{3/4})\).

Freeze the ordering at the square center:
\[
c_{3,N}(d)=\frac12
 \sum_{\substack{p,r\ge z\ {\rm prime}\\pr=d}}
 {\bf1}_{\,pr\max(p,r)\le x}.
\]
For distinct prime factors its value is one when the condition holds; for \(d=p^2\) it is one half. Define
\[
c_N(d)={\bf1}_{\,d\ {\rm prime},\,z\le d<w}+c_{3,N}(d).
\tag{4}
\]
The two supports are disjoint, so
\[
0\le c_N(d)\le1,\qquad z\le d\le x^{2/3}
\]
on its support, for all sufficiently large \(N\). This coefficient is explicitly prime-supported or two-prime-supported and depends on \(N\). It is not being replaced by an arbitrary coefficient family in the terminal estimate.

Let
\[
C_N(W)=\sum_d c_N(d)\sum_{q\ {\rm prime}}{\bf1}_W(dq). \tag{5}
\]
The cofactor in (5) lies between constant multiples of \(N^{2/3}\) and \(N^{7/4}\). We next control the freezing error uniformly.

### The freezing error

Write \(p\le r\), \(d=pr\), and \(v_0=pr^2\). The actual and frozen ordering differ on a window only if \(v_0\) lies between its endpoints. For windows in \([x/2,2x]\), such a pair satisfies
\[
(x/2)^{1/3}\le r\le (2x/z)^{1/2},\qquad d\gg N^{9/8}.
\]
On the short window, there are at most \(Y/d+1=O(1)\) possible integer cofactors per pair. The number of thresholds \(pr^2\) in \(J\) is at most the number of rows with a square divisor \(r^2\), \(r\ge(x/2)^{1/3}\). Checkpoint 9's dyadic square-divisor bound therefore gives a short freezing error \(O(N^{2/3})\).

For the reference window, enlarge both primes to integers. The reciprocal weight of its thresholds is bounded by
\[
\begin{aligned}
\sum_{pr^2\in B_1}\frac1{pr}
&\ll \frac1x\sum_{r\le(2x/z)^{1/2}}
 r\left(\frac{H_1}{r^2}+1\right)\\
&\ll \frac{H_1}{x}\log N+\frac1z.
\end{aligned}
\]
The normalized count of thresholds themselves is
\[
a\,O(H_1x^{-1/3}+x^{1/3})
=O(Yx^{-1/3}+ax^{1/3}).
\]
Thus the normalized long freezing error is
\[
O\!\left(Y\frac{H_1}{x}\log N+N^{3/4}+N^{1/3}+aN^{2/3}\right).
\]
This is \(o(u)\). Combining this calculation with (2)–(3),
\[
\Delta M_2+\Delta M_3
=\Delta C_N+
O(N^{3/4})+
O\!\left(Y\frac{H_1}{x}\log N\right). \tag{6}
\]
No boundary threshold has been dropped without this estimate. The frozen support also keeps all the triprime degrees of freedom that the actual ordering allows up to this error.

## 3. Prime detection with a uniform prime-power error

Define
\[
A_N(W)=\sum_d c_N(d)
 \sum_{q\ge2}\frac{\Lambda(q)}{\log q}{\bf1}_W(dq). \tag{7}
\]
The weight is one on a prime and \(1/k\) on \(q=\ell^k\), \(k\ge2\). It is nonnegative and at most one.

Let \(P(t)\) count proper prime powers up to \(t\). Enlarging prime bases to integer bases gives
\[
P(t)\le \sqrt t+(\log_2t)t^{1/3}\le5\sqrt t,\qquad t\ge2.
\]
The last inequality follows by maximizing \((\log_2t)/t^{1/6}\), whose maximum is \(6/(e\log2)<4\). Dyadic summation then gives
\[
\sum_{\substack{q\ge R\\q\ {\rm proper\ prime\ power}}}\frac1q
\le25R^{-1/2}.
\]
For any relevant integer window of cardinality \(H\), with cofactor range \([R,S]\), the bounded outer coefficient yields
\[
0\le A_N(W)-C_N(W)
\le25H/\sqrt R+5\sqrt S. \tag{8}
\]
Here \(R\gg N^{2/3}\), \(S\ll N^{7/4}\). On the short window, and after normalization on the long window, (8) is \(O(N^{7/8})=o(u)\). This argument includes prime powers whose prime base is below \(z\); no roughness assumption on that base is hidden.

Consequently,
\[
\boxed{\quad
\Delta M_2+\Delta M_3
=\Delta A_N+
O(N^{7/8})+
O\!\left(Y\frac{H_1}{x}\log N\right).
\quad} \tag{9}
\]
This is a uniform reduction for every sufficiently large even \(N\).

## 4. The actual Vaughan coefficients

Choose
\[
U=V=\lfloor N^{1/100}\rfloor,\qquad
\beta_U(m)=\sum_{\substack{a\mid m\\a>U}}\mu(a).
\]
For \(m>1\), equivalently \(\beta_U(m)=-\sum_{a\mid m,a\le U}\mu(a)\). In particular \(|\beta_U(m)|\le\tau(m)\).

Use the exact convolution identity
\[
\Lambda
=\mu_{\le U}*\log
 -\mu_{\le U}*{\bf1}*\Lambda_{\le V}
 +\mu_{>U}*{\bf1}*\Lambda_{>V}
 +\Lambda_{\le V}. \tag{10}
\]
One primary presentation is [Helfgott, *The ternary Goldbach problem*, slide 65](https://www.mpim-bonn.mpg.de/webfm_send/210). The identity is used here algebraically; its Goldbach exponential-sum conclusions are not imported.

Every cofactor in (7) is greater than \(V\) for sufficiently large \(N\), so the last term vanishes exactly. Equations (7) and (10) give
\[
A_N(W)=I_1(W)+I_2(W)+B_N(W), \tag{11}
\]
where
\[
I_1(W)=
\sum_d c_N(d)\sum_{a\le U}\mu(a)
\sum_{da\ell\in W}\frac{\log\ell}{\log(a\ell)},
\]
\[
I_2(W)=-
\sum_d c_N(d)\sum_{\substack{a\le U\\b\le V}}\mu(a)\Lambda(b)
\sum_{dab\ell\in W}\frac1{\log(ab\ell)},
\]
and the remaining Type II count is
\[
B_N(W)=
\sum_d c_N(d)
\sum_{\substack{m>U\\b>V}}
\frac{\beta_U(m)\Lambda(b)}{\log(mb)}
{\bf1}_W(dmb). \tag{12}
\]
The two Type I terms have a free integer \(\ell\). The Type II term has the specific truncated-Möbius divisor coefficient \(\beta_U\) and a Mangoldt coefficient. It has no free integer coefficient that would justify using a divisor-floor remainder theorem directly.

## 5. Uniform centering of the Type I main terms

Put
\[
\alpha_U=\sum_{a\le U}\frac{\mu(a)}a,\quad
\gamma_U=\sum_{a\le U}\frac{\mu(a)\log a}a,\quad
\lambda_V=\sum_{b\le V}\frac{\Lambda(b)}b,\quad
T=\gamma_U+\alpha_U\lambda_V.
\]
Replacing the free lattice sums by integrals gives the combined density
\[
G(v)=\sum_d\frac{c_N(d)}d
 \left(\alpha_U-\frac{T}{\log(v/d)}\right). \tag{13}
\]
For example, changing variables \(v=da\ell\) in \(I_1\) gives
\[
\frac1{da}\frac{\log(v/(da))}{\log(v/d)}
=\frac1{da}\left(1-\frac{\log a}{\log(v/d)}\right).
\]
The coefficient in (4) is frozen at \(x\) while differentiating with respect to \(v\); it is not differentiated as a moving cutoff.

Absolute harmonic bounds give \(|T|\ll(\log N)^3\), \(\sum_dc_N(d)/d\ll\log N\), and \(\log(v/d)\gg\log N\) throughout \([x/2,2x]\). Hence, conservatively,
\[
|G''(v)|\ll x^{-2}(\log N)^4.
\]
The symmetric windows have zero first moment about \(x\), and their normalized lengths match. Taylor's formula therefore proves
\[
\int_{x-Y/2}^{x+Y/2}G(v)\,dv
 -a\int_{x-H_1/2}^{x+H_1/2}G(v)\,dv
\ll Y(H_1/x)^2(\log N)^4=o(u). \tag{14}
\]
This holds for the complete outer support and for any fixed subset of it. No cancellation estimate for \(\mu\) or quantitative PNT is needed for (14).

## 6. A proved saving for every semiprime Type I term

For each \(d,a\), the weight \(\log\ell/\log(a\ell)\) is between zero and one and has bounded total variation on the relevant interval. Its lattice-minus-integral error is \(O(1)\). For each \(d,a,b\), the weight \(1/\log(ab\ell)\) is \(O(1/\log N)\) with bounded variation. Its weighted error is \(O(\Lambda(b)/\log N)\).

Restrict the outer coefficients to \(d\le w=N^{19/20}\). Summing these errors gives
\[
O(wU)+O\!\left(wU\sum_{b\le V}\Lambda(b)/\log N\right)
=O(wUV)=O(N^{97/100}), \tag{15}
\]
using only \(\Lambda(b)\le\log V\). The normalized reference error has the same bound because \(a\le1\). Combining (14)–(15), the entire centered Type I contribution on this outer range is \(o(u)\), uniformly.

Every semiprime outer prime is less than \(w\), so this covers its complete Type I contribution. It also covers the triprime rows whose two smaller-prime product is at most \(w\), whose largest prime is at least a constant multiple of \(N^{1.05}\).

The reference coefficient of that triprime subregion is
\[
c_{3,\mathrm{low}}
=2\int_{1/2}^{19/20}
\frac{\log(4\sigma-1)}{\sigma(2-\sigma)}\,d\sigma
\in[0.5764489880,\ 0.5765294344]. \tag{16}
\]
It follows by integrating the two outer prime exponents at fixed sum \(\sigma\). Together with the semiprime reference coefficient, this is approximately 79 percent of the joint two/three-prime reference mass. This percentage describes where the Type I proof applies; it is not a bound on the Type II term or on the actual short count.

## 7. The remaining estimate, with every coefficient specified

Let \(I_{1,\mathrm{high}},I_{2,\mathrm{high}},G_{\mathrm{high}}\) restrict (11) and (13) to \(d>w\). Define the high-outer floor error
\[
R_{I,\mathrm{high}}(W)
=I_{1,\mathrm{high}}(W)+I_{2,\mathrm{high}}(W)
 -\int_{W_{\mathbb R}}G_{\mathrm{high}}(v)\,dv,
\]
where \(W_{\mathbb R}\) is the corresponding real window.

These outer coefficients are only two-prime products, with
\[
N^{0.95}<d\le N^{4/3}.
\]
The trivial full-support lattice bound is too large; centering (14) estimates the main integral but does not estimate this floor-error sum.

Equations (9), (11), and (14)–(15) prove the central reduction:
\[
\boxed{\quad
\Delta M_2+\Delta M_3
=\Delta B_N+\Delta R_{I,\mathrm{high}}+o(u).
\quad} \tag{17}
\]
Thus the sufficient uniform estimate is now
\[
\Delta B_N+\Delta R_{I,\mathrm{high}}
\le(0.011+o(1))u \tag{18}
\]
for every sufficiently large even \(N\). The terms may be estimated jointly; separate small absolute bounds are stronger than necessary.

## 8. What the checked source estimates supply

The original Fouvry–Iwaniec source remains sources/fi1989_monomials.pdf. Theorem 2 on printed p. 314 was inspected again on the page image: its published bound uses coefficients bounded by one and contains the first term \((XM_1M_2M_3M_4)^{1/2}\), rather than a sparsity-sensitive norm in that statement.

In the direct additive Fourier mapping of (12), the four variables are frequency \(h\), outer product \(d\), \(m\), and \(b\). At significant short-window frequencies \(H\asymp N\), the product scale is \(DMB\asymp N^2\) and phase size \(X\asymp H\). That first term has scale \(HN\); multiplying by the Fourier coefficient scale \(N^{-1}\) gives \(N\), before the printed logarithm and divisor-order losses. This supplies no \(o(u)\) estimate. This test does not exclude a refinement using the actual sparse support, the norm of \(\beta_U\), or a different spacing argument.

For a balanced triprime Type I example, the two outer primes have exponent \(2/3\), giving denominator exponent \(\Sigma=4/3\) and top reciprocal frequency exponent \(\eta=\Sigma-1=1/3\). The previously verified Theorem 6 facets would require a denominator slot with exponent
\[
n_0\ge1/3,\qquad
n_0\le(3-2\Sigma)/2=1/6.
\]
They are incompatible under every factor grouping, even granting the necessary separation and completion. This is a rejection of that direct generic mapping, not of a square-centered refinement or all the source's methods.

For the printed large-values alternative, [Li, arXiv:2308.04458v8, Lemma 4.1](https://arxiv.org/html/2308.04458v8) has the necessary facet \(|\alpha_1-\alpha_2|<2\theta-1\). Its formal region is empty at \(\theta=1/2\); the theorem has not been extended to that endpoint. The earlier four-factor certificate is preserved in checkpoint 9.

The missing input in (18) is therefore substantive arithmetic cancellation. It cannot be inferred from the source tools already admitted, the completed Type I main-term centering, or the long reference masses.

## 9. Exact checks and the limits of the finite allocation

The script checks Vaughan's identity by comparing exact integer coefficients of \(\log p\), for every \(1\le n\le4000\) and four pairs \((U,V)\): 16,000 identities without floating-point comparison.

Eight actual centered fixtures at \(N=20,40,80,120,200,5000,10000,18000\) verify the factorial diagonal correction, frozen ordering, prime-power correction, and centered transfer using rational weights. The first five additionally compare segmented integer factorization against independent prime-pair and prime-power enumeration. Prime powers have the exact rational weight \(1/k\). The 20,000-cell reference enclosure in (16) uses outward interval arithmetic.

The previous 17 exact centered experiments were also reexamined for the narrower optional allocation (1). Seven have finite excess greater than \(0.011u\). The maximum is about \(0.0451025u\) at \(N=18000\). In particular, the prior observation that all complete frontier excesses were below \(0.338u\) did not establish this separate allocation. These finite failures do not disprove (1), whose quantifier permits an unspecified sufficiently-large threshold and an \(o(1)\) term.

Reproduce the new work from the project directory:

    python3 src/two_three_frontier.py

It writes the bilinear reduction, exact Vaughan/bilinear fixtures, reference/sample audit, and scoped analytic certificates in results/two_three_*.json. The historical ledger and prior source bytes remain unchanged.

The next arithmetic calculation should address (18): a centered sparse-coefficient Type II estimate with \(\beta_U\), together with the reciprocal floor-error family for the larger prime-pair outer products, or a joint bound for their signed sum. The coefficient freeze and Type I proof above supply a complete starting formulation. The \(0.011u\) estimate, the higher-degree cap, positive \(K\), and full \(H(\vartheta)\) remain open.
