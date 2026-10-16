# A short-scale localization lemma for the remaining signed integral

Checkpoint 25 — Michael M. Ross's H(ϑ) campaign — 11 October 2026

**The requested .007935u estimate is not proved.** The two alternatives
at the end of checkpoint 24 estimate the same residual. Examining the
coupled arithmetic alternative yields a further spectral localization:
subtract the established long-reference density *before* restricting
the product to a window of width comparable with N.

For this new, centered localized transform, an absolute tail above
T=(x/Y) log N is o(u). More generally T=L_N x/Y suffices for any
L_N→∞. This replaces checkpoint 24's N^(4/3)(log N)^2 upper limit
in a new equivalent-up-to-o(u) signed integral. No nonvanishing part
of the .007935 allowance is spent. The new transform is essential;
this does not estimate individual bands of either earlier transform.

The proof also supplies a conservative explicit upper coefficient
5.000714 for the coupled expression in checkpoint 24, (14). It is
far above the sufficient .0686138 coefficient. It is not a sharp
estimate or positive lower-bound mass.

## 1. Keep the original comparison and reference

All definitions, arithmetic gates, least-prime sectors, auxiliary
Vaughan cutoffs and outer sets of checkpoints 23–24 are retained:

\[
x=N^2,\qquad Y=N+1,\qquad u=\frac{N}{2\log N},\qquad
z=N^{1/4},\qquad \kappa=1/1000.
\]

N is even. In particular,

\[
c_N(d)=\mathbf1_{d\ {\rm prime},\ z\le d<N^{19/20}}
 +\frac12\sum_{pr=d\atop p,r\ge z\ {\rm prime}}
       \mathbf1_{pr\max(p,r)\le x},
\quad
Q_N(W)=\sum_d c_N(d)\sum_{q\ {\rm prime}}\mathbf1_W(dq).
\]

Here and below “prime” in these formulas denotes the original prime
indicator. There is no enlargement to arbitrary coefficient sequences.
Write q_N(n)=Q_N({n}). The smoothed residual is

\[
I_\kappa=Q_N(\psi_Y)-aQ_N(\psi_{H_1}),\qquad a=Y/H_1.
\]

The earlier proof gives

\[
Q_N(J)-aQ_N(B_1)\le I_\kappa+(.003065+o(1))u,
\qquad I_\kappa=\mathfrak H_\kappa(N)+o(u). \tag{1}
\]

The remaining sufficient coefficient is .007935. The ordinary
long-PNT density is

\[
G_N(v)=\sum_d\frac{c_N(d)}{d\log(v/d)}. \tag{2}
\]

It is used only on windows near x, where v/d≫N^(2/3). The admitted
reference calculation, including the frozen ordering gates, states

\[
YG_N(x)=(M+o(1))u,
\quad
M\in[3.0649340581076633147812768096087415241136662002238,
      3.0649751594758139766181825312222805801782319361390]. \tag{3}
\]

The underlying M is the fixed integral from checkpoint 23; the endpoints
are certified enclosures, not short-count bounds. Also Σ_d c_N(d)/d=O(1),
so G_N'(v)=O(1/(x(log N)^2)) uniformly on the reference and short windows.

## 2. Extend the unique-mark bound to the short padding

**Lemma 1.** For every even N≥2^16 and integer |n−x|≤Y,

\[
0\le q_N(n)\le\mathbf1_{P^-(n)\ge z}. \tag{4}
\]

For the single-prime outer family n=pq, two eligible outers would give
n<N^(19/10). But x−Y>x/2≥N^(19/10) for this range of N. Thus there
is at most one row; its prime cofactor exceeds p and z.

For the pair family choose its canonical p≤r and suppose q<r. Then
the original gate gives

\[
Y\ge x-n\ge pr^2-n=pr(r-q)\ge pr,
\qquad (pr)^2=p(pr^2)>pn\ge z(x-Y).
\]

Since z≥16, x−Y>x/2 and Y≤2N, one has
z(x−Y)>8N^2>Y^2. This contradicts pr≤Y. Hence q≥r, so the
outer pair is the two smallest prime factors and is unique. Its
canonical weight is one for p<r and one half for p=r. Repeated
factors are allowed. These rows have degree three and are disjoint
from the degree-two family. Every factor in a counted row is ≥z.

The broader product support in checkpoint 24 still has cap three.
The cap in (4) relies on the much narrower, specified padding.

## 3. A weighted Selberg bound with an explicit leading coefficient

This elementary upper bound quantifies the local L1 envelope needed
for the tail. It does not supply the sharp signed coefficient.

For nonnegative, compactly supported w of bounded variation, supported
on |v−x|≤Y, let A(w)=∫w(v)dv and V(w) be its total variation.
Take R=floor(z/2), and set

\[
\mathcal G(R)=\sum_{r\le R}\frac{\mu^2(r)}{\varphi(r)}.
\]

There are real Selberg weights λ_d, supported on squarefree d≤R,
with λ_1=1, such that

\[
\sum_{d,e\le R}\frac{\lambda_d\lambda_e}{[d,e]}
 =\frac1{\mathcal G(R)},\qquad |\lambda_d|\le\frac d{\varphi(d)}
 \le\tau(d). \tag{5}
\]

For completeness define y_r=μ(r)/(φ(r)𝒢(R)) on r≤R, zero elsewhere,
and λ_d=dΣ_(r:d|r)μ(r/d)y_r. Möbius inversion gives
Σ_(d:r|d)λ_d/d=y_r. The identity
(d,e)=Σ_(r|d,r|e)φ(r) proves (5), while λ_1=Σ_rμ(r)y_r=1.
For squarefree d the explicit formula is

\[
\lambda_d=\frac{\mu(d)d}{\varphi(d)\mathcal G(R)}
 \sum_{m\le R/d\atop(m,d)=1}\frac{\mu^2(m)}{\varphi(m)}.
\]

It proves the coefficient bound; nonsquarefree d have λ_d=0.

On a z-rough n, Σ_(d|n)λ_d=1 because R<z. Consequently (4) and
the nonnegative square give

\[
\sum_n q_N(n)w(n)
 \le\frac{A(w)}{\mathcal G(R)}
       +V(w)R^2(1+\log R)^2. \tag{6}
\]

Indeed Σ_k w(ℓk)=A(w)/ℓ+O(V(w)), with absolute error ≤V(w).
Expand the square and use Σ_(d≤R)|λ_d|≤Σ_(d≤R)τ(d)
≤R(1+log R). All weights and all lattice rows remain actual.

The normalization 𝒢(R)∼log R has an elementary proof. The Dirichlet
coefficients g(n)=μ²(n)/φ(n) satisfy g=(1/n)*h under Dirichlet
convolution, with multiplicative h given by

\[
h(p)=\frac1{p(p-1)},\quad h(p^2)=-\frac1{p(p-1)},\quad
h(p^j)=0\quad(j\ge3).
\]

Its absolute coefficient sum converges, and Σ_n h(n)=1. Thus
𝒢(R)=Σ_(d≤R)h(d)H_floor(R/d), and dominated convergence after
division by log R proves the assertion. Since log R∼(log N)/4 and
R²(log R)²=O(N^(1/2)(log N)²)=o(u), (6) implies

\[
\sum_n q_N(n)w(n)\le
 \left(\frac{8A(w)}Y+o(1)\right)u \tag{7}
\]

for the fixed-shape weights used below, each with V(w)=2. This is
a coarse rough-number bound, rather than a prime-density asymptotic.

## 4. Localize after subtracting the reference density

Put α=1/2+κ=501/1000. With H(s)=10s³−15s⁴+6s⁵ define

\[
\chi_N(v)=
\begin{cases}
1,&|v-x|\le\alpha Y,\\
H\left(\dfrac{Y-|v-x|}{(1-\alpha)Y}\right),
   &\alpha Y<|v-x|<Y,\\
0,&|v-x|\ge Y.
\end{cases} \tag{8}
\]

It is nonnegative, C², has total variation two, and equals one on
the support of ψ_Y. Its area is (1+α)Y: ∫_0^1H(s)ds=1/2.
Define the actual local mass and its deterministic density model by

\[
A_\chi=\sum_n q_N(n)\chi_N(n),\qquad
D_\chi=\int\chi_N(v)G_N(v)\,dv.
\]

By (3), (7) and the derivative bound,

\[
A_\chi\le(8(1+\alpha)+o(1))u=(12.008+o(1))u,
\qquad D_\chi=((1+\alpha)M+o(1))u. \tag{9}
\]

The centered local Mellin transform is

\[
\boxed{\Phi_N(t)=
 \sum_n\frac{q_N(n)\chi_N(n)}{n^{1+it}}
 -\int\chi_N(v)G_N(v)v^{-1-it}\,dv.} \tag{10}
\]

No short prime approximation is asserted in subtracting the integral.
The exact Mellin inversion identity is

\[
\frac1{2\pi}\int_\mathbb R\Phi_N(t)
       \widehat\psi_Y(1+it)\,dt
 =Q_N(\psi_Y)-\int\psi_Y(v)G_N(v)\,dv. \tag{11}
\]

Both integrals are absolutely convergent. The established long PNT
gives aQ_N(ψ_H1)=a∫ψ_H1 G_N+o(u). Equal normalized areas and
the derivative bound imply

\[
a\int\psi_{H_1}G_N-\int\psi_YG_N
 =O\left(\frac{Y(H_1+Y)}{x(\log N)^2}\right)=o(u).
\]

Therefore

\[
\boxed{I_\kappa=
 \frac1{2\pi}\int_\mathbb R\Phi_N(t)
             \widehat\psi_Y(1+it)\,dt+o(u).} \tag{12}
\]

The original reference is removed through this proved comparison.
It is not included in the short support of χ_N.

## 5. Uniform tail and the shortened signed interface

Positivity of the two local masses gives, for every real t,

\[
|\Phi_N(t)|\le\frac{A_\chi+D_\chi}{x-Y}. \tag{13}
\]

The exact trapezoid formula from checkpoint 23 and endpoints of
modulus at most x+αY give

\[
|\widehat\psi_Y(1+it)|
 \le\frac{4(x+\alpha Y)^2}{\kappa Yt^2}\quad(t\ne0). \tag{14}
\]

Hence for any T>0,

\[
\boxed{\frac1\pi\int_T^\infty
 |\Phi_N(t)\widehat\psi_Y(1+it)|\,dt
 \le\frac{4(x+\alpha Y)^2}{\pi\kappa YT(x-Y)}
           (A_\chi+D_\chi).} \tag{15}
\]

Take T_L=Lx/Y. Equations (9) and (15) yield the asymptotic coefficient

\[
C_{\rm tail}=\frac{4(1+\alpha)(8+M)}{\pi\kappa}
 \le21146.634266<21147. \tag{16}
\]

The inequality is certified using the full outward upper endpoint
in (3) and a rational Machin-series lower bound for π. The strict
rounding reserve and the fact that the factor
(x+αY)²/[x(x−Y)] tends to one show that, for all sufficiently large
N, **uniformly for every L≥1**,

\[
\boxed{\frac1\pi\int_{Lx/Y}^\infty
 |\Phi_N(t)\widehat\psi_Y(1+it)|\,dt
 \le\frac{21147}{L}u.} \tag{17}
\]

For the inherited T_0=exp(c_0√log N/4), (9), (13) and
|ψ̂_Y|≤(1+κ)Y also give

\[
\frac1\pi\int_0^{T_0}
 |\Phi_N(t)\widehat\psi_Y(1+it)|\,dt
 =O(T_0/\log N)=o(u). \tag{18}
\]

This low-part argument is an absolute estimate for a short-support
transform. It does not invoke PNT on a short interval.

Conjugation, (1), (12), (17) and (18) prove the promised lemma:

**Lemma 2 (short-scale centered spectral localization).** For any
L_N→∞,

\[
\boxed{\mathfrak H_\kappa(N)=
 \frac1\pi\Re\int_{T_0}^{L_Nx/Y}
   \Phi_N(t)\widehat\psi_Y(1+it)\,dt+o(u).} \tag{19}
\]

In particular L_N=log N gives upper limit (x/Y)log N∼N log N.
The estimates hold uniformly over all sufficiently large even N.
There is no averaging over centers, and the phase x=N² is unchanged.
The transforms D_N P_N, F_N of checkpoint 24, and Φ_N here differ.
Only their *completed signed integrals with the reference retained
as above* are identified up to o(u); individual old high bands are
not declared negligible.

## 6. Preserve both kinds of coefficient budget

Let H_L be the integral in (19) with fixed L≥1. The direction needed
for an upper bound is

\[
I_\kappa\le H_L+\left(\frac{21147}{L}+o(1)\right)u. \tag{20}
\]

Thus the sufficient central coefficient and the original allowance are

| Choice | Central signed allowance | Tail charge | Smoothing charge |
|---|---:|---:|---:|
| L_N=log N | .007935 | o(1) | .003065 |
| Fixed L | .007935−21147/L | 21147/L | .003065 |
| Fixed L, plus least-prime budget ξ | .007935−21147/L−ξ | 21147/L | .003065 |

The ξ term is the separate fixed-power least-prime budget from
checkpoint 22, (23); this proof uses no such discarded sector.
For example fixed L=100,000,000 charges .00021147 and leaves
.00772353 for the central integral. These three coefficients sum
to .011 exactly. The growing-L statement is asymptotic; it does
not make a finite numerical promise at a particular N.

## 7. What can presently be bounded in the coupled alternative

Apply (7) directly to ψ_Y, whose area is (1+κ)Y and variation two.
Together with the established smoothed reference this proves

\[
I_\kappa\le((1+\kappa)(8-M)+o(1))u
 \le(4.940002+o(1))u. \tag{21}
\]

For the actual coupled expression S_τ from checkpoint 24, (14),

\[
S_\tau=B_{\tau,\mathcal G_\tau,db>N^{461/400}}(\psi_Y)
           +Q_{\mathcal C_\tau}(\psi_Y)
 =I_\kappa+(1+\kappa)M_{\mathcal C_\tau}u+o(u).
\]

Keeping that exact coupling and using the lower full-reference and
upper core-reference enclosure endpoints gives

\[
\boxed{S_\tau\le(5.000714+o(1))u.} \tag{22}
\]

The unrounded coefficient is at most 5.00071370457810219894… .
This supplies an explicit uniform upper coefficient, but is much
larger than the required .0686138. No individual sign or small
norm for the actual B_τ term is inferred from (22).

The remaining central requirement is still

\[
\frac1\pi\Re\int_{T_0}^{(x/Y)\log N}
 \Phi_N(t)\widehat\psi_Y(1+it)\,dt
 \le(.007935+o(1))u. \tag{23}
\]

Neither the Selberg bound nor the absolute tail proves (23). Its
content is the sharp short count minus its established density,
now resolved at the natural frequency scale x/Y≈N. The alternative
sharp coupled estimate remains open as well.

## 8. Verification and preservation

Run `python3 src/short_scale_localization.py`. It checks the exact
Selberg quadratic minimizers, their coefficient bounds, independently
enumerated lattice errors for the local polynomial taper, the local
mark cap and repeated-factor rows, the cutoff/budget arithmetic,
Machin π enclosures and all decimal rounding directions. The proofs
of the uniform estimates are above; finite checks do not prove (23).

All 252 nonmutable records in checkpoint 24's manifest and the
historical negative-frontier ledger are preserved byte for byte.
The earlier SPECTRAL_COVERAGE_NOTE.md and its code/results remain
unchanged. New artifacts are additive; only the current indices
and the current manifest are updated.

The original .011 comparison, .007935 sharp coefficient, optional
marked estimate, higher-degree allocation, positive K and H(ϑ)
remain open. The certified lower constant is still K=0.
