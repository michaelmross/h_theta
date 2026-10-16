# An alternate route: centered dispersion of two prime pairs

H(ϑ) campaign — supplement to checkpoint 32 — 13 October 2026

**This note does not prove the sharp short-window inequality.** It proves
a conditional reduction, its uniform pairing margin, and the harmlessness
of the diagonal. The new centered off-diagonal estimate below is open.
No actual deficit coefficient or campaign allowance is improved.

The proposed method estimates a variance of the actual prime-pair count
after subtracting its continuous reference. It does not first bound the
absolute values of the four separate prime Dirichlet polynomials. It
therefore uses information not supplied by checkpoint 32's generic
large-value audit.

## 1. The actual target and the retained weight

Keep x=N², Y=N+1, ℓ=log N, u=N/(2ℓ), κ=.001, the original smoothing
ψ_Y, and the fifth-degree kernel W_N. Write

\[
c_j=(-1)^{j+1}\binom5j,\qquad
\Phi_5(v)=\sum_{j=1}^5c_jv^j=1-(1-v)^5.
\]

After the already justified denominator freezing and removal of repeated
prime rows, sort the four primes as p<r<s<t. The exact comparison weight
on such a row is

\[
\sum_{j=1}^5c_j27^j
\frac{(\log r\log s\log t)^j}{(\log(x/p))^{3j}},
\qquad N^{.40}\le p\le N^{.43}.
\tag{1}
\]

Sorting removes the original factor 1/6, because the residual three
distinct primes have six ordered representations. All five moments
remain. Only the already proved o(u) repeated-row error is used.

Checkpoint 31 gives

\[
\Delta W_N=\mathcal P_N(\psi_Y)-\mathcal C_N(\psi_Y)+o(u).
\tag{2}
\]

The current sharp input is a lower comparison with coefficient η_W and
η_W+η_rest≤.000099. Proving an o(u) comparison for W_N would settle
its part of that input, but would still leave any outstanding comparison
for the other complement terms.

## 2. A uniform margin from the two smallest primes

Let X_+=x+(.5+κ)Y, the upper end of the smoothing support. On every
sorted row contributing to the short count,

\[
pr^3\le prst\le X_+.
\]

Consequently, with m=pr,

\[
m\le X_+^{1/3}p^{2/3}
 \le N^{143/150}(1+O(N^{-1})).
\tag{3}
\]

The exponent is exact:
(2+2·.43)/3=143/150. Thus m is separated from N by the fixed exponent
7/150. This holds on the whole retained band, including checkpoint 32's
box Q; no exceptional physical box is deleted.

Use the index set

\[
\mathcal I_N=\{(p,r):p,r\text{ prime},\ N^{.40}\le p\le N^{.43},
                 \ p<r,\ pr^3\le X_+\}.
\]

For j=1,…,5 define the nonnegative first-pair coefficient

\[
\alpha_j(p,r)=
 \left(\frac{\ell}{\log(x/p)}\right)^{3j}
 \left(\frac{\log r}{\ell}\right)^j.
\tag{4}
\]

It is uniformly bounded for each fixed j. The total coefficient mass
satisfies

\[
A_j:=\sum_{\mathcal I_N}\alpha_j(p,r)
 \ll_j\frac{N^{143/150}}{\ell^2}.
\tag{5}
\]

Indeed r≤(X_+/p)^{1/3}, and the ordinary prime upper bound gives

\[
\begin{aligned}
\#\mathcal I_N
 &\ll\frac{N^{2/3}}{\ell}
       \sum_{p\le N^{.43}}p^{-1/3}\\
 &\ll\frac{N^{2/3}N^{(2/3)\cdot.43}}{\ell^2}.
\end{aligned}
\]

The logarithmic estimates are long-interval estimates; no prime theorem
on an individual short interval is invoked here.

## 3. The centered second-pair count

For a prime threshold r, define

\[
\beta_{j,r}(n)=
 \sum_{\substack{r<s<t\text{ prime}\\st=n}}
 \left(\frac{\log s}{\ell}\right)^j
 \left(\frac{\log t}{\ell}\right)^j.
\tag{6}
\]

The second pair retains its actual prime masks and its dependence on r.
It is not an unrestricted divisor coefficient. Its continuous reference
density is

\[
f_{j,r}(v)=
\begin{cases}
\displaystyle\frac{1}{2\ell^{2j}}
 \int_r^{v/r}(\log z)^{j-1}(\log(v/z))^{j-1}\frac{dz}{z},
 &v\ge r^2,\\[6pt]
0,&v<r^2.
\end{cases}
\tag{7}
\]

The factor 1/2 sorts the two continuous residual factors. Formula (7)
is exactly the pushforward of the weighted measures dz/log z and
dw/log w under v=zw, on z,w≥r. No conjectural local prime density is
asserted by defining this reference.

For (p,r)∈I_N and m=pr put

\[
\begin{aligned}
T_{j,r}(m)&=\sum_n\beta_{j,r}(n)\psi_Y(mn),\\
R_{j,r}(m)&=\int_0^\infty f_{j,r}(v)\psi_Y(mv)\,dv,\\
E_j&=\sum_{\mathcal I_N}\alpha_j(p,r)
                 \big(T_{j,r}(pr)-R_{j,r}(pr)\big),\\
D_j&=\sum_{\mathcal I_N}\alpha_j(p,r)
                 \big|T_{j,r}(pr)-R_{j,r}(pr)\big|^2.
\end{aligned}
\tag{8}
\]

These are finite sums on the physical support. The short window for
the second product is centered at x/(pr) and has length comparable
to Y/(pr). Its location is tied to the first prime pair.

Replacing just the first two prime sums in Σα_jR_{j,r} by their
continuous prime measures costs o(u). This uses ordinary long PNT,
after the second pair has already been integrated. To check the scale,
write

\[
R_{j,r}(pr)=\frac1{pr}\int\psi_Y(w)f_{j,r}(w/(pr))\,dw.
\tag{9}
\]

On the contributing support f_{j,r}≪_j1/ℓ; its derivative in log v
and its variation under the moving lower endpoint r are O_j(1/ℓ).
The moving endpoint v=r² has zero integral length, so introduces no
jump in f. Partial summation against the ordinary exponential PNT
remainder in p and r therefore gives
O_j(N exp(-c√ℓ)ℓ^C)=o(u). The restrictions r>p and pr³≤X_+ are
handled by the same endpoint variation; the latter is also the natural
zero boundary of the integrated second-pair count.

The resulting continuous four-factor integral is the one with all
four densities equal to 1 in checkpoint 31. Its difference from
the actual all-Type-I continuous density C_N is already o(u).
Consequently

\[
\boxed{\Delta W_N=\sum_{j=1}^5c_j27^jE_j+o(u).}
\tag{10}
\]

Equation (10) is a reduction, not a sharp estimate.

## 4. A sufficient dispersion lemma with a fixed power margin

Cauchy–Schwarz and (5) give

\[
|E_j|\le(A_jD_j)^{1/2}.
\tag{11}
\]

**Conditional lemma.** Suppose that, uniformly for every sufficiently
large N, all five actual centered variances in (8) satisfy

\[
\boxed{D_j\ll_j N^{26/25},\qquad j=1,\ldots,5.}
\tag{12}
\]

Then

\[
|E_j|\ll_j\frac{N^{299/300}}{\ell}=o(u),
\qquad \Delta W_N=o(u).
\tag{13}
\]

The exponent calculation is

\[
\frac12\left(\frac{143}{150}+\frac{26}{25}\right)
 =\frac{299}{300}<1.
\]

The finite constants c_j27^j do not consume a leading coefficient
when there is a fixed power saving. More generally, D_j≪N^{1+ε}
with any fixed ε<7/150 suffices. Fixed logarithmic factors in that
bound can also be absorbed into its power margin.

This global variance criterion is sufficient, not necessary. If its
global weighting proves inefficient, a weaker criterion can be used
separately on dyadic p,r rectangles. With p≍P, r≍R and M=PR, the
coefficient mass is O_j(M/ℓ²). A uniform estimate

\[
D_{j;P,R}=o\!\left(\frac{N^2}{M\ell^4}\right)
\tag{14}
\]

would give E_{j;P,R}=o(N/ℓ³). There are O(ℓ²) such rectangles,
so a uniform little-o factor in (14) would again give E_j=o(u).
The individual thresholds r in (6)–(8) must remain in these local
variances; grouping by m does not remove those thresholds.

## 5. The diagonal is already below the required scale

Expand D_j exactly. Its diagonal term is

\[
D_j^{\rm diag}=
 \sum_{\mathcal I_N}\alpha_j(p,r)
 \sum_n\beta_{j,r}(n)^2\psi_Y(prn)^2.
\tag{15}
\]

On the physical support a second product n=st has one sorted prime
representation. Its weight is bounded for fixed j. Each n·pr has
one sorted four-prime representation, with least prime p in the band.
Since 0≤ψ_Y≤1, the admitted upper estimate for the rough band in
checkpoint 30 implies

\[
\boxed{D_j^{\rm diag}\ll_j u.}
\tag{16}
\]

This is an actual diagonal bound, with an unspecified constant. That
constant is adequate for (12), since u=o(N^{26/25}); it is not an
improved campaign deficit coefficient.

Define the remaining exact centered expression by

\[
\begin{aligned}
D_j^{\rm off}=
\sum_{\mathcal I_N}\alpha_j(p,r)\Bigg[&
 \sum_{n\ne k}\beta_{j,r}(n)\beta_{j,r}(k)
                      \psi_Y(prn)\psi_Y(prk)\\
 &-2R_{j,r}(pr)T_{j,r}(pr)+R_{j,r}(pr)^2\Bigg].
\end{aligned}
\tag{17}
\]

Then D_j=D_j^{diag}+D_j^{off}. The concrete missing input is the
one-sided estimate

\[
\boxed{D_j^{\rm off}\le C_jN^{26/25}\quad(j=1,\ldots,5),}
\tag{18}
\]

uniformly in N. An upper bound suffices; an absolute-value bound is
not required. The three terms inside the bracket must remain centered
together. In particular, separating their absolute values would discard
the cancellation of the mean square.

For terms in (17), the two second products satisfy
|n-k|≪Y/(pr). Their prime factorizations, their common lower threshold
r, and the curved centers x/(pr) remain part of the estimate.
This is the prime-specific correlation problem to which a dispersion
or phase-preserving argument would have to apply.

A basic count alone does not supply (12). Since β is bounded and its
support inside each window has O(Y/(pr)) integer positions, one only
gets, by summing prime reciprocal squares,

\[
D_j\ll_j N^2\sum_{p\ge N^{.4}\atop p\text{ prime}}p^{-2}
                       \sum_{r\ge p\atop r\text{ prime}}r^{-2}
 \ll_j\frac{N^{6/5}}{\ell^2}.
\tag{19}
\]

This is an upper envelope, not an asserted variance size. The fixed
gap between 6/5 and 26/25 is not repaired by additional fixed powers
of log N. Thus (18) is a substantive additional analytic input.

## 6. What the checked sources do and do not provide

The publisher text of
[Correlations of almost primes](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/correlations-of-almost-primes/08F8E4E4C36F68ED6DDA373CCAF7A221)
was checked at Lemma 2.4 and §7.5, Lemma 7.12. Its Parseval reduction
averages over interval centers; its twisted fourth-moment factor has
free integer coefficients 1 or log n, times a character. Neither
clause is an estimate for (17) with its actual prime-pair sampling.
This is an applicability check, not an exclusion of a new adaptation.

The more generous mixed-moment audit in checkpoint 32 is unchanged.
No published result checked in this supplement has been verified to
prove (18). The diagonal proof and the exponent margin do not imply
the off-diagonal bound.

## 7. Coverage and the unchanged coefficient ledger

| Item | Result |
|---|---|
| Entire least-prime band [.40,.43] | Retained |
| Five Φ₅ moments and all prime masks | Retained |
| Uniform two-smallest-prime pairing margin | Proved: 7/150 |
| Continuous first-pair reference replacement | o(u), ordinary long PNT |
| Diagonal dispersion | O(u), admitted rough upper bound |
| Conditional implication from (12) | Proved: error O(N^(299/300)/log N) |
| Actual centered off-diagonal bound (18) | Open |
| Actual sharp comparison for W_N | Open |
| Other complement terms η_rest | Unchanged |

The sufficient original coefficient remains

\[
.003065+.007825257+.000001+\eta_W+\eta_{\rm rest}
              +\xi+21147/L\le .011,
\qquad \eta_W+\eta_{\rm rest}\le .000099.
\tag{20}
\]

The spectral allowance remains .007935 after dropping the smoothing
charge .003065. No original least-prime power sector or frequency
sector is discarded. No sharp coefficient is credited until the new
analytic input is proved. Checkpoint 32 remains the latest completed
campaign archive; this note records an alternate route and its precise
remaining test.
