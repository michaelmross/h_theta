# Testing centered variance on individual dyadic blocks

Checkpoint 33 — Michael M. Ross's H(ϑ) campaign — 14 October 2026

**The required little-o variance estimate remains unproved.** This
checkpoint proves its O-scale analogue, with the correct power and four
logarithms, uniformly over all active first-pair blocks. Its diagonal
is negligible at that scale. The checked correlation and dispersion
sources do not directly supply the remaining saving on the actual
prime-pair sample. No actual sharp deficit coefficient is improved.

The accompanying PAIR_DISPERSION_ROUTE_NOTE.md retains the preceding
conditional reduction. Its global N^(26/25) hypothesis is not assumed.
The present test uses its weaker block criterion (14).

## 1. Exact blocks, coefficients, and target

Keep x=N², Y=N+1, ℓ=log N, κ=.001, u=N/(2ℓ), and the original ψ_Y.
Its support is |w−x|≤(.5+κ)Y and 0≤ψ_Y≤1. Set X_+=x+(.5+κ)Y.
Let

\[
\mathcal I_{P,R}=\{(p,r):p,r\text{ prime},\ P\le p<2P,\ R\le r<2R,
\ N^{.40}\le p\le N^{.43},\ p<r,\ pr^3\le X_+\}.
\tag{1}
\]

Dyadic ranges are half-open and clipped at the actual band endpoints.
For an active block put M=PR, h=Y/M, B=x/M, and define

\[
\mathcal V_{P,R}=\frac{N^2}{M\ell^4}.
\tag{2}
\]

For j=1,…,5 retain the actual nonnegative weights

\[
\begin{aligned}
\alpha_j(p,r)&=\left(\frac{\ell}{\log(x/p)}\right)^{3j}
                   \left(\frac{\log r}{\ell}\right)^j,\\
\beta_{j,r}(n)&=\sum_{r<s<t\text{ prime}\atop st=n}
                   \left(\frac{\log s\log t}{\ell^2}\right)^j,\\
f_{j,r}(v)&=\frac{\mathbf1_{v\ge r^2}}{2\ell^{2j}}
          \int_r^{v/r}(\log z)^{j-1}(\log(v/z))^{j-1}\frac{dz}{z}.
\end{aligned}
\tag{3}
\]

The integral is taken only when v≥r²; the density is zero otherwise.
The threshold r in β and f remains individual to each first pair.
Define the actual second count and its continuous reference by

\[
T_{j,r}(m)=\sum_n\beta_{j,r}(n)\psi_Y(mn),\qquad
\mathcal R_{j,r}(m)=\int f_{j,r}(v)\psi_Y(mv)\,dv.
\tag{4}
\]

The tested variance and discrepancy are

\[
\begin{aligned}
D_{j;P,R}&=\sum_{\mathcal I_{P,R}}\alpha_j(p,r)
              |T_{j,r}(pr)-\mathcal R_{j,r}(pr)|^2,\\
E_{j;P,R}&=\sum_{\mathcal I_{P,R}}\alpha_j(p,r)
              (T_{j,r}(pr)-\mathcal R_{j,r}(pr)).
\end{aligned}
\tag{5}
\]

No masks, five-moment terms, or physical sectors are deleted. The
requested input is

\[
\boxed{D_{j;P,R}=o(\mathcal V_{P,R})}
\tag{6}
\]

uniformly over all active blocks and j=1,…,5. The reference itself
need not be bounded below on blocks near the zero-volume boundary;
(2), rather than a relative bound using that reference, is the target.

## 2. Uniform geometry and the first-pair mass

As proved in the preceding note,

\[
pr\le X_+^{1/3}p^{2/3}\le N^{143/150}(1+O(N^{-1})).
\]

Since M≤pr<4M on a block and p,r≥N^.40, every active block has

\[
N^{4/5}/4\le M\le N^{143/150}(1+O(N^{-1})),\qquad
N^{7/150}(1+o(1))\le h\ll N^{1/5}.
\tag{7}
\]

In particular log h≥(7/150)ℓ+O(1). Long prime upper bounds give

\[
A_{j;P,R}:=\sum_{\mathcal I_{P,R}}\alpha_j(p,r)
 \ll_j\frac{M}{\ell^2}.
\tag{8}
\]

All coefficients in (3) are bounded for fixed j on their contributing
support. Also f_{j,r}≪_j1/ℓ: the logarithmic integrand has size
O_j(ℓ^(2j−2)) and its log z interval has length O(ℓ). Thus

\[
0\le\mathcal R_{j,r}(pr)\ll_j h/\ell.
\tag{9}
\]

If M=N^σ at limiting power scale, the residual product is at scale
B=N^(2−σ), its window has width h=N^(1−σ), and

\[
\frac{\log h}{\log B}=\frac{1-\sigma}{2-\sigma}
 \in[7/157,1/6]+o(1).
\tag{10}
\]

The first-pair parameter σ lies in [4/5,143/150]. Formula (10) helps
match a short-interval source to the correct residual scale.

## 3. An elementary uniform bound for the second-pair count

For each (p,r), the support of ψ_Y(pr·) lies in a real interval of
length at most (1+2κ)h. Every integer counted by β_{j,r} is r-rough.
Choose the auxiliary Selberg radius

\[
Z=\lfloor h^{1/4}\rfloor.
\]

Uniformly on active blocks, Z≤O(N^(1/20))<r for large N. This radius
is only an upper-bound device; it does not discard any original
least-prime sector or change the campaign's fixed-power budget.

Use checkpoint 25's explicit Selberg weights, supported on squarefree
d≤Z, with

\[
\lambda_1=1,\quad |\lambda_d|\le d/\varphi(d)\le\tau(d),\quad
\sum_{d,e\le Z}\frac{\lambda_d\lambda_e}{[d,e]}=\frac1{G(Z)},
\quad G(Z)=\sum_{d\le Z}\frac{\mu^2(d)}{\varphi(d)}.
\tag{11}
\]

On an r-rough integer their divisor sum is 1. For any interval J
of length L≤(1+2κ)h, counting multiples exactly gives

\[
\begin{aligned}
\#\{n\in J:P^-(n)\ge r\}
 &\le\sum_{n\in J}\left(\sum_{d\mid n}\lambda_d\right)^2\\
 &\le\frac{L}{G(Z)}+O\!\left(Z^2(1+\log Z)^2\right).
\end{aligned}
\tag{12}
\]

The implied constant is independent of J's location. Here
G(Z)≫log Z; for this lower bound it is already enough to use
G(Z)≥Σ_(d≤Z)μ²(d)/d=(1/ζ(2))log Z+O(1), obtained by expanding
μ²(d)=Σ_(a²|d)μ(a). The exact minimizer and the stronger elementary
normalization were proved in checkpoint 25.

Since Z²≪h^(1/2), the error in (12) is o(h/log h), uniformly by (7).
With bounded β weights and at most one sorted representation n=st,

\[
\boxed{T_{j,r}(pr)\ll_j h/\log h\ll_j h/\ell.}
\tag{13}
\]

This is an upper bound, not a local semiprime asymptotic. In particular,
its leading constant has not been matched to the reference density.

## 4. The proved block variance and the remaining saving

Equations (8), (9), and (13) imply, for the full centered square,

\[
\boxed{D_{j;P,R}\ll_j\frac{M}{\ell^2}\frac{h^2}{\ell^2}
 \ll_j\frac{N^2}{M\ell^4}=\mathcal V_{P,R}.}
\tag{14}
\]

This proves the correct O-scale bound on every active block. The
argument bounds |T−R| by T+R; it therefore does not establish a saving
from centering. It must not be read as the required little-o in (6).

The diagonal in the exact expansion satisfies the stronger local bound

\[
\begin{aligned}
D^{\rm diag}_{j;P,R}
 &=\sum_{\mathcal I_{P,R}}\alpha_j(p,r)
            \sum_n\beta_{j,r}(n)^2\psi_Y(prn)^2\\
 &\ll_j\sum_{\mathcal I_{P,R}}\alpha_j(p,r)T_{j,r}(pr)
 \ll_j N/\ell^3=o(\mathcal V_{P,R}).
\end{aligned}
\tag{15}
\]

Indeed its ratio to (2) is O_j((M/N)ℓ)≪N^(-7/150)ℓ→0 uniformly.
The remaining expression is exactly

\[
\begin{aligned}
D^{\rm off}_{j;P,R}=\sum_{\mathcal I_{P,R}}\alpha_j(p,r)\Bigg[&
 \sum_{n\ne k}\beta_{j,r}(n)\beta_{j,r}(k)
                       \psi_Y(prn)\psi_Y(prk)\\
 &-2\mathcal R_{j,r}(pr)T_{j,r}(pr)
                       +\mathcal R_{j,r}(pr)^2\Bigg].
\end{aligned}
\tag{16}
\]

It suffices to prove D^off≤ε_N V_(P,R) for one ε_N→0 independent of
the active block. An absolute bound on this signed expression is not
necessary. All three terms in (16) must retain their centering.

Cauchy–Schwarz now supplies only

\[
|E_{j;P,R}|\ll_j N/\ell^3.
\tag{17}
\]

There are O(ℓ²) first-pair blocks, so (17) gives O(u) for their sum,
with no sharp coefficient. A uniform little-o in (6) would give o(u)
after summing the blocks and the five fixed coefficients c_j27^j.

## 5. Why an average over all centers does not close this test

This section proves a failure of a proposed norm transfer, not a
counterexample to the actual prime variance.

Distinct sorted first pairs have distinct integer products m∈[M,4M].
Their residual centers z_m=x/m are separated by

\[
|z_m-z_{m'}|\ge\frac{x}{16M^2}\asymp h^2.
\tag{18}
\]

Since h→∞, windows or neighborhoods of radius h around these centers
are disjoint for large N. The samples occupy a sparse subset of a
residual interval of length comparable to B.

Consider a fixed interior exponent block, for example

\[
P\asymp N^{83/200},\qquad R\asymp N^{23/50},\qquad
M\asymp N^{7/8}.
\tag{19}
\]

Its index set has K_N≍M/ℓ² pairs by ordinary long PNT; the inequalities
p<r, pr³<X_+ and the positive residual-volume condition are strict.
The α_j weights are bounded below by a positive constant for each
fixed j on this block. In particular a+3b=359/200<2.

Let b(t)=(1−|t|)_+, with ∫b=1 and ∫b²=2/3. Take an interval J of
length L≍B containing all centers and their h-neighborhoods. Define
a function on J by

\[
g_N(v)=-\frac{ch}{\ell}\sum_m b\!\left(\frac{v-z_m}{h}\right)+\gamma_N,
\qquad \gamma_N=\frac{cK_Nh^2}{\ell L},\quad c>0\text{ fixed}.
\tag{20}
\]

The model offset makes the long mean zero. The neighborhoods are
disjoint. Therefore

\[
\begin{aligned}
\int_Jg_N(v)\,dv&=0,\\
\int_J|g_N(v)|^2\,dv
 &=\frac{c^2h^2}{\ell^2}
       \left(\frac23K_Nh-\frac{K_N^2h^2}{L}\right)
 \ll\frac{K_Nh^3}{\ell^2}.
\end{aligned}
\tag{21}
\]

The function is Lipschitz with constant O(c/ℓ). Since K_Nh/L≪M/(Nℓ²)
tends to zero, at every sample center its value is
g_N(z_m)=−(c+o(1))h/ℓ. Its weighted sampled square consequently has
size comparable to

\[
K_Nh^2/\ell^2\asymp\mathcal V_{P,R}.
\tag{22}
\]

Nevertheless, for every fixed A>0,

\[
\frac{\int_J|g_N(v)|^2\,dv}{B h^2/\ell^{2+A}}
 \ll\frac{M}{N}\ell^{A-2}\longrightarrow0.
\tag{23}
\]

Thus even arbitrary fixed logarithmic savings in an all-centers
mean-square norm, together with an exactly zero long mean and this
Lipschitz control, do not imply the desired sampled little-o bound.
Smoothing the tent gives the same conclusion if desired. No actual
prime coefficients or prime-pair counts are asserted to realize (20).
Additional nonconcentration or arithmetic information about the sampled
error is required for that transfer.

## 6. Source coverage and scope of the negative audit

The following primary texts were read at the listed clauses. None is
admitted as a proof of (6) or (16).

| Primary source and clause | Checked scope | Gap for the present application |
|---|---|---|
| [Natalie Evans, Correlations of almost primes](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/correlations-of-almost-primes/08F8E4E4C36F68ED6DDA373CCAF7A221), Theorems 1.1, 1.3; Lemma 2.4 | Shift averages and correlation counts over long integer intervals; the restricted theorem uses a subpower smaller prime; the Parseval lemma integrates over centers | Actual β has both prime factors ≥r≥N^.40. General E₂ counts cannot be substituted for that restriction. An all-centers norm needs a sampled transfer, which (23) shows is not automatic |
| [Matomäki–Teräväinen, Almost primes in almost all short intervals II](https://arxiv.org/pdf/2207.05038), Theorems 1.1, 2.1 | Almost-all center estimates with a polylogarithmic first prime and a sieve minorant; its variance integrates over the center | Neither the coefficient family nor the averaging measure is the actual β and prime-pair sample here |
| [Adam Harper, Simple Barban–Davenport–Halberstam type asymptotics for general sequences](https://arxiv.org/pdf/2412.19644), variance definition and Theorem 1 | Variance over moduli and residue classes for long progression sums, with explicit distribution and sparsity conditions | No reduction to the curved short-window sample is supplied; those conditions have not been verified to give (16) |
| [Sary Drappeau, Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method](https://arxiv.org/pdf/1504.05549), Theorem 2.1 | Kloosterman phase and two smooth summation variables, with scale derivative bounds | The actual prime masks are not smooth coefficients. The original product window has relative width ≍1/N, so its derivatives do not satisfy those scale bounds directly. Completion or arithmetic decomposition would require a separately verified mapping |

For the last row, on a smoothing ramp the log derivative in a physical
factor v_i has size ≍x/(κY)≍N/κ. A smooth weight varying at the scale
of v_i would have bounded log derivative. This rejects the direct use
of the original window as that source's smooth weight. It does not
exclude a valid decomposition and completion leading to a different
source application.

This is a scoped audit of these clauses and the attempted all-centers
transfer. It is not an assertion that every existing dispersion theorem
fails, that the variance is actually large, or that the sharp inequality
is false.

## 7. Outcome, remaining input, and coefficient ledger

| Required item | Status |
|---|---|
| O(N²/(PR log⁴N)) on all active dyadic blocks | Proved, uniform, unspecified constant |
| Local diagonal bound O(N/log³N) | Proved; uniformly negligible at the target scale |
| All-centers mean-square to this sample without another input | Norm implication fails by (20)–(23) |
| Uniform centered off-diagonal little-o | Unproved |
| Actual sharp deficit coefficient | No improvement |
| Prime masks, thresholds, five moments, physical sectors | Retained |

The remaining analytic input is still (16) with a uniform little-o
upper bound, or a direct one-sided estimate of the original coupled
short comparison. This checkpoint has not produced a theorem closing
that input. Another O-scale envelope alone will not provide its coefficient.

The original sufficient ledger remains

\[
.003065+.007825257+.000001+\eta_W+\eta_{\rm rest}
               +\xi+21147/L\le .011,
\qquad \eta_W+\eta_{\rm rest}\le .000099.
\tag{24}
\]

The spectral allowance remains .007935. No sector is removed, and the
Selberg radius in Section 3 adds no deletion charge. All earlier
reference enclosures and actual deficit coefficients are unchanged.
H(ϑ), the .011/.007935 targets and milestone 7 remain open; certified
K=0. All 311 nonmutable checkpoint-32 records are preserved byte for byte.

Run `python3 src/dyadic_variance_test.py`. Exact checks verify the
continuous exponent margins, the interval Selberg algebra, and a finite
zero-mean sampled-norm construction. The uniform proofs are above;
finite checks do not verify the actual prime variance or its little-o bound.
