# Feasibility audit of a two-smallest-prime switched lower weight

Checkpoint 28 — Michael M. Ross's H(ϑ) campaign — 12 October 2026

**Decision: reject this candidate.** Its pointwise lower-weight construction
is valid, and the switched sieve remainders fit the admitted source
conditions. Its reference loss is at least (1.56+o(1))u, against the
.0001u acceptance budget. This remains a rejection after giving the
unswitched prime-and-balanced-semiprime part its full reference mass.

There is also an independent coverage failure: an omitted four-prime
box has smoothed long-reference coefficient at least
693/911600=.0007602018429… . This exceeds the entire budget even if the
active switched region were estimated perfectly.

The audit does not reject switching in general. It rejects the
two-smallest-prime construction that subtracts a separate upper
prime-cofactor sieve from a lower rough-cofactor sieve at the admitted
5/4 level. No sharp original comparison, H(ϑ) or positive K is proved.

## 1. Target and one explicit candidate

Keep x=N², Y=N+1, u=N/(2 log N), z=N^(1/4), even N, κ=1/1000,
the original H_1, a=Y/H_1 and ρ=H_1/x=N^(-o(1)). Keep the original
prime-product marks

\[
c_N(d)=\mathbf1_{d\ {\rm prime},\ z\le d<N^{19/20}}
 +\frac12\sum_{pr=d\atop p,r\ge z\ {\rm prime}}
 \mathbf1_{pr\max(p,r)\le x},
\qquad
q_N(n)=\sum_{dq=n,\ q\ {\rm prime}}c_N(d).
\tag{1}
\]

Use the positive complement from checkpoint 27,

\[
d_N(n)=\mathbf1_{P^-(n)\ge z}
 (1-\min\{1,q_N(n)\}),\qquad
\mathcal D_N(\psi)=\sum_n d_N(n)\psi(n).
\tag{2}
\]

The accepted transfer would require a lower weight w_N≤d_N on the
short padding, a normalized long-reference loss at most η_loss u,
and a one-sided comparison error at most η_err u, with
η_loss+η_err≤.0001. The reference test is a necessary part of this
specified sufficient route.

Set

\[
y=N^{19/20},\qquad \delta=1/1000,\qquad
\Lambda_*=5/4-\delta=1249/1000.
\tag{3}
\]

Here Λ_* is an exponent-level parameter, not the von Mangoldt function.
The y cutoff is the original boundary between marked and unmarked
semiprimes. It does not replace the original small least-prime cutoff.

Partition p,r into disjoint dyadic intervals [P,2P), [R,2R),
with P=2^jz, R=2^kz and j≤k. Retain p≤r. For each box define

\[
D_{P,R}=\frac{N^{\Lambda_*}}{4PR},\qquad R^+=2R.
\]

A box is active exactly when

\[
D_{P,R}\ge R^+,\quad\text{equivalently}\quad
8PR^2\le N^{\Lambda_*}.
\tag{4}
\]

The cutoff is fixed once for the entire box. It is not selected
separately for individual product integers.

Let ℓ_(D,Z) and u_(D,Z) be the source-normalized lower and upper sieve
weights in Section 2. Define the candidate, on x/2≤n≤3x/2, by

\[
w_N(n)=\mathbf1_{P^-(n)\ge y}
 +\sum_{\text{active }(P,R)}
  \sum_{p\in[P,2P),\,r\in[R,2R)\atop
       p,r\ {\rm prime},\ p\le r,\ pr\mid n}
 \left\{\ell_{D_{P,R},R^+}(n/(pr))
       -u_{D_{P,R},D_{P,R}}(n/(pr))\right\}.
\tag{5}
\]

Set w_N=0 outside this broad interval. The exact base indicator is
retained; its short comparison is not assumed. This deliberately
gives the candidate full credit for the base when testing reference
loss.

The auxiliary p=r row in (5) has weight one: it selects the first two
prime factors as a multiset once. The original half-weighted diagonal
in (1) remains unchanged.

## 2. Pointwise weight validity, with source tolerance retained

The primary sieve input is
[Lichtman, arXiv:2109.02851v2, Theorem 2.10, (2.4)–(2.5), and (5.17)](https://arxiv.org/html/2109.02851v2).
Its remainder weights are finite sums of well-factorable sequences,
fixed independently of the integer set being sifted.

For g(e)=1/e put V(Z)=∏_(p<Z)(1−1/p), s=log D/log Z and

\[
R^\pm_{D,Z}(m)=
 \sum_{e\mid P(Z)}\widetilde\lambda^\pm(e)
 \left(\mathbf1_{e\mid m}-\frac1e\right).
\]

Choose a fixed small ε>0 and a sufficiently large source constant
C≥0 bounding the O(ε) terms. The source inequalities applied to the
singleton set {m} give the normalized kernels

\[
\begin{aligned}
\ell_{D,Z}(m)&=V(Z)\{f(s)-C\varepsilon\}-R^-_{D,Z}(m),\\
u_{D,Z}(m)&=V(Z)\{F(s)+C\varepsilon\}+R^+_{D,Z}(m),
\end{aligned}
\tag{6}
\]

and the pointwise inequalities

\[
\ell_{D,Z}(m)\le\mathbf1_{P^-(m)\ge Z}
\le u_{D,Z}(m).
\tag{7}
\]

This singleton normalization is the present derivation; it does not
silently assume that an unmodified conventional sieve polynomial
has the same pointwise and factorability properties. The sign of each
remainder in (6) follows the stated source formulation.

All finite-tolerance corrections in (6) lower ℓ or raise u. Their
reference effect therefore worsens this candidate. No ε=0 source
application or N-dependent tolerance is used.

On an active box, pr²≤8PR²≤N^Λ_*≪x. For n≈x, m=n/(pr) is larger
than r, R^+ and D_(P,R); in fact

\[
m/D_{P,R}\ge\tfrac12N^{2-\Lambda_*},
\qquad m/R^+\ge\tfrac12N^{2-\Lambda_*}
\]

on x/2≤n≤3x/2. Since R^+≥r, (7) yields

\[
\ell_{D,R^+}(m)-u_{D,D}(m)
\le
\mathbf1_{P^-(m)\ge r}-\mathbf1_{m\ {\rm prime}}.
\tag{8}
\]

The right side is nonnegative here. It counts composite r-rough
cofactors. Summing over p≤r counts at most one pair: the two smallest
prime factors of n. A surviving row has Ω(n)≥4 and P^-(n)≥z.
This positive pool is disjoint from P^-(n)≥y, since y³≫x.
Every integer in either pool is unmarked by (1).

Thus (5) obeys

\[
\boxed{w_N(n)\le d_N(n)\quad(x/2\le n\le3x/2).}
\tag{9}
\]

This includes the original short padding and long reference.
Repeated factors and original canonical mark weights are retained.

## 3. Actual source conditions for the switched terms

Write a_1=log_N p, a_2=log_N r,
γ=a_1+a_2 and β=Λ_*−γ. Dyadic endpoint constants perturb these
exponents by O(1/log N); the fixed source reserve absorbs them.

The limiting active domain is the triangle

\[
a_1\ge1/4,\qquad a_2\ge a_1,\qquad
a_1+2a_2\le\Lambda_*.
\tag{10}
\]

Its vertices are

\[
(1/4,1/4),\quad(1/4,999/2000),\quad
(1249/3000,1249/3000).
\]

Consequently

\[
\gamma\le1249/1500<1,\qquad
\beta\ge1249/3000>0,\qquad
\gamma+\beta=\Lambda_*<5/4.
\tag{11}
\]

For each fixed box the outer coefficient of d=pr is bounded by one,
including p=r: prime factorization gives a unique ordered p≤r.
The fixed box gates are incorporated before using this coefficient.
Both sieve remainders in (6) have the same full level D_(P,R);
their exact squarefree sifting supports are retained.

The already proved WF_FI_ARBITRARY_OUTER proposition in
FI_1989_AUDIT.md, Section 5, therefore applies to both switched
remainders. For γ≤3/4 the earlier RS route also has
2γ+β≤1.999<2. For the FI part choose τ=10^(-5), ν=10^(-6);
the inherited capacity inequalities have positive rational margins.
All three active vertices and both source branches are checked.

| Candidate term | Actual coefficient family | Source result |
|---|---|---|
| Lower r-rough cofactor remainder | Bounded prime-pair outer coefficient; finite full-level WF sieve components | Admitted power saving |
| Upper prime-cofactor remainder | Same outer coefficient; upper sieve majorant with cutoff D | Admitted power saving |
| Exact base P^-(n)≥y | Actual prime-and-balanced-semiprime pool | Its one-sided comparison remains unproved |
| Base replaced by a WF lower weight | γ=0, level N^Λ_*, s=1249/950<2 | Remainder admitted, but f(s)=0 and reference worsens |

A prime mask has not been called a free unit-weight slot. The switched
inner sums are actual sieve polynomials over integer cofactors.
The inherited fixed-WF transfer controls their errors. It does not
automatically estimate the exact base indicator.

The reference-loss test below already rejects (5), so there is no
reason to pursue a new proof of the base comparison for this candidate.

## 4. Why every active block has a negative reference contribution

Let \(\mathcal L(s)=sf(s)/(2e^{\gamma_0})\).
For 1≤s≤2 it is zero; for 2≤s≤4 it is log(s−1).
The upper prime sieve at s=1 has F(1)=2e^(γ_0).

Ignoring only the unfavorable Cε corrections for the purpose of
giving the candidate its most favorable mean, Mertens and (6) give
the cofactor density

\[
\frac{2}{\beta\log N}
 \left\{\mathcal L(\beta/a_2)-1\right\}.
\tag{12}
\]

Throughout (10),

\[
1\le\beta/a_2\le4\Lambda_*-2=749/250=2.996.
\]

It follows that

\[
\mathcal L(\beta/a_2)
\le\log(499/250)=.69114517788927\ldots<1.
\tag{13}
\]

Thus every active switched block has negative leading reference
mean. The prime upper cost exceeds the lower rough contribution.
This is an algebraic source-function failure throughout the continuous
domain, independent of finite numerical examples.

Even sending the fixed level reserve δ to zero would leave
\(\mathcal L(3)=\log2<1\).
For this same separately priced construction, obtaining even one
positive leading cofactor block would require a stronger total
divisor level B satisfying

\[
4B-2>1+e,\qquad
B>\frac{3+e}{4}=1.42957045711476\ldots .
\tag{14}
\]

This is a necessary condition for positive cofactor pricing in this
specific family. It is not a sufficient condition for the .0001
reference budget or for H(ϑ).

## 5. Certified long-reference loss

The exact base retains the ordinary normalized reference

\[
c_{\rm base}=(1+\kappa)\left\{1+\log(21/19)\right\}.
\tag{15}
\]

This follows from Buchstab's function at log x/log y=40/19∈(2,3).
It credits both primes and the unmarked balanced semiprimes in full.
No short asymptotic for that base is used.

The magnitude of the negative switched mean before the (1+κ)
factor is

\[
B_{\rm sw}=4\int_{1/4}^{\Lambda_*/3}
 \int_{a_1}^{(\Lambda_*-a_1)/2}
 \frac{1-\mathcal L((\Lambda_*-a_1-a_2)/a_2)}
 {a_1a_2(\Lambda_*-a_1-a_2)}
 \,da_2\,da_1.
\tag{16}
\]

For the normalized long window, the centered divisibility remainders
in (6) have zero continuous main. Elementary floor errors after
multiplication by a are
O(N^(Λ_*−1)ρ^(-1)(log N)^C)=o(u).
Prime reciprocal partial summation in the two outer variables gives
(16). Factor-two dyadic sifting endpoints change exponents by
O(1/log N) and hence add o(u) to this long reference.

Outward two-dimensional integration with 240 cells per coordinate
certifies

\[
B_{\rm sw}\in
[1.23568132923165579755,\ 1.26405733218138403015].
\]

The most favorable candidate mean is
c_base−(1+κ)B_sw, enclosed in
[−.16413784749802589515,−.13573346854534793432].
The fixed positive-tolerance corrections only make it smaller.

The original positive complementary reference is unchanged:

\[
c_{\mathcal D}\in
[1.42812738782223954808,\ 1.42816857732647018189].
\]

Therefore the most favorable reference loss is enclosed in

\[
c_{\mathcal D}-c_{\rm base}+(1+\kappa)B_{\rm sw}
\in[1.56386085636758748240,\ 1.59230642482449607704].
\tag{17}
\]

For every fixed-tolerance implementation of (5), this proves

\[
\boxed{
a\{\mathcal D_N(\psi_{H_1})-\mathcal W_N(\psi_{H_1})\}
\ge(1.56+o(1))u.}
\tag{18}
\]

The displayed enclosure describes the favorable small-tolerance
coefficient limit, not an upper bound on the loss of every finite
implementation. Its lower endpoint is used for rejection.

Deleting all negative active blocks cannot repair the budget.
That leaves at most the base mean and loses at least
(.32694384580670+o(1))u of higher-degree reference.
If the exact base is also replaced by its admitted WF lower sieve,
the whole reference loss is at least (2.66+o(1))u. That variant would
remove the unsupported exact-base comparison, but would worsen
the fatal reference loss.

## 6. Independent omitted-box certificate

Consider distinct sorted four-prime factors with independent
N-exponents

\[
a_1\in[.40,.43],\qquad
a_2\in[.45,.48],\qquad
a_3\in[.50,.53].
\tag{19}
\]

At product x=N², a_4=2−a_1−a_2−a_3 lies in [.56,.65],
with a fixed ordering margin over a_3.
These integers are rough, have degree four and carry no original mark.
Their positive complement is one.

Every prime pair selected from such an integer satisfies
log_N(pr²)≥a_1+2a_2≥1.30>Λ_*.
Consequently no active box in (5) contributes.
The base also vanishes because its smallest prime is <y.
The candidate weight is exactly zero on this box.

The ordinary canonical four-prime reference density is

\[
\frac{2\,da_1\,da_2\,da_3}
 {a_1a_2a_3(2-a_1-a_2-a_3)}.
\]

Bounding each denominator by its maximum over the box gives the
exact smoothed lower reference coefficient

\[
(1+\kappa)
 \frac{2(.03)^3}{(.43)(.48)(.53)(.65)}
=\frac{693}{911600}
=.000760201842913558\ldots>.0001.
\tag{20}
\]

The usual long PNT applies because all four prime scales have fixed
positive exponents and the original relative width ρ exceeds the
inherited PNT error. The reference in (20) is a normalized long count,
not a short count.

Since (9) also holds on the long window, this omitted positive mass
cannot be canceled by overcounting elsewhere. It rules out the
active-domain construction even if its active components were
perfectly priced and perfectly compared. The box still lies outside
a_1+2a_2≤5/4 when δ tends to zero.

## 7. Feasibility decision and the next interface

| Requirement from checkpoint 27 | Audit outcome |
|---|---|
| Pointwise lower weight | Passed, using the exact source-normalized kernels |
| Switched source conditions | Passed with fixed rational margins |
| Exact-base one-sided comparison | Still unproved |
| Reference loss plus comparison charge ≤.0001 | Failed already by reference loss >1.56 |
| Recovery by active-block deletion or tolerance refinement | Failed |
| Recovery by perfect estimates confined to the active gate | Failed: omitted box alone costs >.000760 |

**Reject the separately priced two-smallest-prime candidate.**
Sharpening its remainder estimates or its numerical quadrature will
not repair the reference-loss failure.

The next candidate should change the residual grouping and account for
the omitted four-prime box. One concrete starting interface extracts
only the smallest prime, keeping the residual degree pool intact:

\[
\mathcal D_N(\psi_Y)
=S_N(\psi_Y;y)+
 \sum_{p\ge z,\ p\ {\rm prime}}
 \sum_{m\atop P^-(m)\ge p,\ \Omega(m)\ge3}
 \psi_Y(pm)+o(u).
\tag{21}
\]

The higher-degree term counts each rough integer of degree at least
four exactly once. The o(u) accounts for the nonnegative repeated
three-prime correction described in checkpoint 27.
A contributing p automatically satisfies p≤(x+Y)^(1/4)=N^(.5+o(1)).
This interface includes the omitted box, unlike (4).

Equation (21) is an exact arithmetic starting point up to the stated
negligible correction. It is not an admitted short comparison:
the joint condition P^-(m)≥p, Ω(m)≥3 needs a new lower-weight
construction or a direct coupled estimate. The prime-and-balanced
base and this higher-degree pool must retain their combined budget.
No successful replacement candidate is asserted here.

The next manageable test is therefore a source-and-reference audit of
a weight for the **one-prime residual degree pool in (21)**.
It must preserve its degree condition, include the omitted box, and
fit the same total .0001 reference-loss/comparison budget. If it does
not, record the specific additional estimate it requires.

## 8. Original coefficient ledger and verification

The original smoothing charge .003065 and signed allowance .007935
remain unchanged. This rejected candidate supplies no new sharp bound.
For any future accepted candidate the sufficient budget remains

\[
.007825257+\eta_{\rm loss}+\eta_{\rm err}
+\xi+21147/L\le .007935.
\tag{22}
\]

The final original coefficient retains all terms:
.003065+.007825257+η_loss+η_err+ξ+21147/L.
Here ξ is the checkpoint-22 (23) charge if a fixed least-prime sector
is subsequently discarded; 21147/L is the checkpoint-25 charge for a
fixed complete-transform tail multiplier. Neither is introduced by
this audit. The omissions of the present lower weight are included
in its failed reference-loss test, not hidden in an o(u) assertion.

Run python3 src/switched_minorant_audit.py.
The exact checks cover the active rational triangle, both inherited
source branches, the sign of every leading cofactor mean, and
451,078 short-padding sites with the original mark cutoffs and gates.
They retain repeated-prime rows and verify the first-prime interface.

The finite fixtures test the switching pool and its pointwise
relation to the original marks. They do not numerically instantiate
Iwaniec's universal weights; the weight inequalities are proved from
the primary source. The outward reference certificate integrates a
positive loss function after mapping the active triangle to a rectangle.
The omitted-box mass uses exact rational endpoint bounds.

All 275 nonmutable checkpoint-27 records and the frozen historical
mass ledger are unchanged. The original .007935/.011 comparison,
H(ϑ), the optional marked estimate and a qualifying positive
complement construction remain open. K=0; milestone 7 remains deferred.

