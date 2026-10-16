# Completing the even sector and bounding the signed aggregate

Checkpoint 21 — Michael M. Ross's H(ϑ) campaign — 9 October 2026

The concrete marked even-cofactor problem from checkpoint 20 is still open.
Completing its surrounding Vaughan sum does, however, give two uniform
deductions with the original coefficients:

\[
\boxed{|\mathcal C_N(J)|\ll u,\qquad
S_{\le U^\varepsilon}(J)-aS_{\le U^\varepsilon}(B_1)
=O_\varepsilon(u)} \tag{1}
\]
for fixed 0<ε≤1, and
\[
\boxed{\sum_{\substack{n\in J\\2\mid n}}\beta_U(n)V_N(n)=o(u),\qquad
a\sum_{\substack{n\in B_1\\2\mid n}}\beta_U(n)V_N(n)=o(u).} \tag{2}
\]
Every fixed least-prime sector has the same negligible signed bound.
These are signed completion results. They do not bound the marked
residual slice separately, either by O(u) or by o(u).

**Correction of scope.** Checkpoints 19–20 left the short small-prime
aggregate unbounded at u scale by their direct kernel argument. Completing
the earlier Vaughan identity supplies (1). The statement that no u-scale
bound was available for that aggregate was too strong. The exponent
η≈0.0602478244 remains a valid direct absolute-beta estimate; it is no
longer the strongest bound for the completed signed covariance.
Historical proof files are preserved, and current indices record this
correction explicitly.

The coefficient-exact .011u comparison, higher-degree allocation, positive
certified K and H(ϑ) remain unproved. No new prime lower-bound mass is
credited.

## 1. Keep the actual weights and both windows

Use the unchanged definitions
\[
x=N^2,\quad J=[x-N/2,x+N/2]\cap\mathbb Z,\quad Y=N+1,
\quad u=\frac{N}{2\log N},\quad z=N^{1/4},\quad
U=\lfloor N^{1/100}\rfloor,
\]
\[
c_N(d)=\mathbf1_{d\ {\rm prime},\ z\le d<N^{19/20}}
+\frac12\sum_{pr=d\atop p,r\ge z\ {\rm prime}}
\mathbf1_{pr\max(p,r)\le x},\qquad
\beta_U(m)=-\sum_{t\mid m,\ t\le U}\mu(t)\quad(m>1).
\]
Set β_U(1)=0. In a canonical pair p≤r the outer weight is one for
p<r and one half for p=r; the ordering gate is pr²≤x.

D_good, its complementary core C, and D_B=N^(459/400) are exactly those
in DELTA_GROUPING_NOTE.md, equations (13)–(14). The actual continuation is
\[
V_N(n)=\sum_{d\in D_{\rm good},\ d\mid n}
\frac{c_N(d)}{\log(x/d)}
\sum_{\substack{b\mid n/d,\ b>U\ {\rm prime}\\
db>D_B,\ n/(db)>1}}\log b. \tag{3}
\]
The core prime marks are
\[
P_N(n)=\sum_{d\in C}c_N(d)\mathbf1_{n/d\ {\rm prime}}.
\]
Define the exact arithmetic aggregate
\[
\mathcal C_N(W)=\sum_{n\in W}(\beta_U(n)V_N(n)+P_N(n)). \tag{4}
\]
It agrees with the locally centered covariance of checkpoint 16 up to
o(u) on J. Keep
\[
H_1=2\lfloor x e^{-3(\log x)^{1/3}}/2\rfloor+1,\quad
B_1=(x-H_1/2,x+H_1/2)\cap\mathbb Z,\quad a=Y/H_1.
\]
Thus a=N^(-1+o(1)); all gates are frozen at x.

Write S(W) for (3) weighted by β_U on P⁻(n)≤U, and
R(W)=Σ_{P⁻(n)>U}(V_N(n)−P_N(n)). The exact rough beta value is −1,
and all core marks are rough. Hence
\[
\mathcal C_N(W)=S(W)-R(W). \tag{5}
\]
The inherited comparison is
\[
\Delta_2+\Delta_3=\mathcal C_N(J)-(M_C+o(1))u,
\quad a\mathcal C_N(B_1)=(M_C+o(1))u. \tag{6}
\]
The full saved enclosure for M_C is unchanged, approximately
[0.08849546268,0.08853207941].

## 2. Completion gives a uniform O(u) bound for the aggregate

For an actual outer subset D put
\[
Q_D(W)=\sum_{d\in D}c_N(d)\sum_{q\ {\rm prime}}\mathbf1_W(dq),
\qquad \Pi_D=\sum_{d\in D}\frac{c_N(d)}{d\log(x/d)}.
\]
The exact Vaughan identity from checkpoint 10, complete Type I control on
D_good, negligible db≤D_B Type II region, selected proper-power errors
and logarithmic freezing from checkpoints 10–14 give
\[
\sum_{n\in J}\beta_U(n)V_N(n)
=Q_{D_{\rm good}}(J)-Y\Pi_{D_{\rm good}}+o(u). \tag{7}
\]
Here the combined Type I density is
\[
G_D(v)=\sum_{d\in D}\frac{c_N(d)}d
\left[\alpha_U-
\frac{\gamma_U+\alpha_U\lambda_U}{\log(v/d)}\right],
\]
with α_U=Σ_{t≤U}µ(t)/t, γ_U=Σ_{t≤U}µ(t)log(t)/t,
λ_U=Σ_{b≤U}Λ(b)/b. The inherited long Möbius estimate gives
α_U exponentially small in √log N and γ_U=−1 plus such an error;
λ_U≪log U. Its integral over the half-integer window with Y sites is
YΠ_D+o(u). This is the uncentered Type I main term, which must be kept
when completing the identity.

Adding the core prime marks to (7) yields
\[
\mathcal C_N(J)=Q_{\rm all}(J)-Y\Pi_{D_{\rm good}}+o(u). \tag{8}
\]
Both terms on the right are O(u). To verify this without any short prime
asymptotic, every cofactor q is ≫N^(2/3)>z and every outer prime is at
least z. A prime-cofactor row therefore has two or three prime factors,
counted with multiplicity, and at most three canonical eligible outer
marks. Consequently, pointwise on J,
\[
0\le Q_{\rm all}(\{n\})\le3\mathbf1_{P^-(n)\ge z}. \tag{9}
\]
Apply the deterministic Shiu bound, in
[Mangerel (2023), Lemma 3.2](https://link.springer.com/article/10.1007/s40687-023-00376-0),
to the multiplicative indicator on the right. It is bounded by one;
with fixed interval exponent 1/30 the length Y≈N is admissible at center
≈N². Its Euler product is O(1/log z). Thus Q_all(J)≪N/log z≪u.
The theorem supplies an order bound, with no sharp numerical constant.

For the other term, all pair primes are ≤N^(7/8), since p≥z and
pr²≤N² when p≤r. The inherited prime reciprocal asymptotics give
\[
\sum_d\frac{c_N(d)}d
\le\sum_{z\le p<N^{19/20}}\frac1p
+\frac12\left(\sum_{z\le p\le N^{7/8}}\frac1p\right)^2=O(1).
\]
Also d≤N^(4/3), so log(x/d)≥(2/3)log N and YΠ_good=O(u).
Equation (8) proves the first assertion in (1).

The already proved rough bound R(J)=O(u), together with (5), gives
S(J)=O(u). Subtract the large least-prime block
S_{>U^ε}(J)=O_ε(u), which was bounded in checkpoint 19. This proves
S_{≤U^ε}(J)=O_ε(u). Its normalized reference is O_ε(u) by checkpoint 20,
so its discrepancy is O_ε(u) as claimed in (1).

This does not upgrade Σ|β_U|V_N to O(u), and gives no .011 coefficient.
The large opposing reference masses in checkpoint 20 remain compatible
with all these signed statements.

## 3. Complete continuation on each fixed divisibility mask is negligible

Fix a squarefree integer e>1 before N tends to infinity. Eventually all
outer d and every retained prime b>U are coprime to e. Multiply the exact
Vaughan identity by the mask 1_{e|n}; no outer or continuation gate changes.

### The exact masked Type I density

For the I₁ lattice, e|dtℓ is equivalent to ℓ being a multiple of
h=e/(e,t). For I₂ use h=e/(e,tb). In each case put ℓ=hj and retain
the original logarithmic weight. The density of multiples supplies
(e,t)/e or (e,tb)/e. In particular no log h is added to the main term:
the original log ℓ becomes log(v/(dt)) after changing variables.

Define
\[
A_e(U)=\sum_{t\le U}\frac{\mu(t)}t\frac{(e,t)}e,
\quad \Gamma_e(U)=\sum_{t\le U}\frac{\mu(t)\log t}t\frac{(e,t)}e,
\]
\[
L_e(U)=\sum_{b\le U}\frac{\Lambda(b)}b
\sum_{t\le U}\frac{\mu(t)}t\frac{(e,tb)}e.
\]
The combined density is exactly
\[
G_{D,e}(v)=\sum_{d\in D}\frac{c_N(d)}d
\left[A_e(U)-\frac{\Gamma_e(U)+L_e(U)}{\log(v/d)}\right]. \tag{10}
\]
For e=1 this is the original density. For e>1 all three scalar
coefficients are negligible; the ordinary prime main term vanishes.

To prove this, set
\[
\alpha_e^0(y)=\sum_{t\le y,\ (t,e)=1}\frac{\mu(t)}t,
\qquad \gamma_e^0(y)=\sum_{t\le y,\ (t,e)=1}\frac{\mu(t)\log t}t.
\]
The finite Euler-factor extension of the inherited long Möbius PNT is
\[
\alpha_e^0(y)=O_e(e^{-c_e\sqrt{\log y}}),\qquad
\gamma_e^0(y)=-C_e+O_e(e^{-c_e\sqrt{\log y}}),
\quad C_e=\prod_{p\mid e}(1-1/p)^{-1}. \tag{11}
\]
For completeness, convolve µ with the indicator of integers supported
on the fixed primes dividing e. Its Dirichlet series is
ζ(s)^(-1)∏_{p|e}(1−p^(-s))^(-1). In the harmonic sums split the smooth
convolution variable at √y. Below √y use the original quantitative
Möbius estimate; above it, the convergent fixed Euler product at s=1/2
bounds the reciprocal tail by O_e(y^(-1/4)). The extra log in γ has
the same bound with fixed logarithmic losses. Its limiting constant is
−C_e. This derives (11) from the previously admitted input, without a
new short-interval theorem.

Factor a squarefree t as a·s with a|e and (s,e)=1. Exact identities are
\[
A_e(U)=\frac1e\sum_{a\mid e}\mu(a)\alpha_e^0(U/a),
\]
\[
\Gamma_e(U)=\frac1e\sum_{a\mid e}\mu(a)
\big[\gamma_e^0(U/a)+\log a\,\alpha_e^0(U/a)\big]. \tag{12}
\]
Since Σ_{a|e}µ(a)=0, the limiting constants in Γ_e cancel exactly.
Both A_e and Γ_e have the decay in (11).

The small Mangoldt variable must also be treated when its prime base
divides e. If b=r^k and r∤e, its inner sum in L_e is A_e; if r|e,
it is A_{e/r}. Thus the exact identity is
\[
L_e(U)=A_e(U)\sum_{r^k\le U,\ r\nmid e}\frac{\log r}{r^k}
+\sum_{r\mid e}A_{e/r}(U)\sum_{r^k\le U}\frac{\log r}{r^k}. \tag{13}
\]
A_1=α_U has the same small bound. Therefore
L_e(U)=O_e((log U)e^(-c_e√log U)), and integrating (10) gives o_e(u).

### Transfer of the fixed-modulus floor estimates

The required floor estimates are new deductions from the admitted
Type I and low-product proofs, rather than an assertion that arbitrary
congruence masks are automatically covered. There are only finitely many
values h|e. Split t and b by their gcd classes with e, giving independent
bounded coefficients in the two slots, then use ℓ=hj. Original outer
ordering, D_good membership and db gates remain in place.

For each fixed h the phase and interval center become x/h and length Y/h;
all exponent scales change by O_e(1/log N). The source inequalities have
strict margins: the smallest Type I margin is at least 1/10000 and the
low-product Type II margin is 9/14000. They therefore retain positive
margins for sufficiently large N. The same RS/FI coefficient separation,
signed sharp transfer, logarithmic weights and absolute boundary envelopes
apply. Elementary branches retain a floor error of at most one per row.
Summing the finitely many gcd classes gives
\[
I_{1,D_{\rm good},e}(J)+I_{2,D_{\rm good},e}(J)=o_e(u). \tag{14}
\]
On the long reference one can use elementary floor bounds even for the
whole outer support: after normalization the cost is
a·O(N^(4/3)U²(log N)^C)=N^(53/150+o(1))=o(u).
The density integral is also o_e(u).

### Removing the low product and proper-power terms under the mask

The masked Mangoldt/cofactor term A_{D_good,e} is negligible. A prime
cofactor exceeds every prime dividing fixed e, so it cannot satisfy the
mask. If e has at least two distinct prime factors, no Mangoldt cofactor
can satisfy it at all. If e=q is prime, only q^k remains; with q^k≫N^(2/3),
enlarging the outer support to integers gives O_e(N^(1/3)+log N)=o(u).
The normalized long-reference bound is the same. The inherited absolute
proper-power subset estimate would also suffice.

Vaughan completion and (14) now give B_{D_good,e}(J)=o_e(u). To pass
to (3), the low-product subtraction must still be justified under the
mask. After the already proved absolute proper-b-power removal, b>U
is prime and coprime to e. On db≤D_B, m≫N^(.8525)>U. Expand β_U(m)
into its small divisors and count ℓ on the lattice h=e/(e,t). The
integral is
\[
-\frac{Y A_e(U)}{\log N}
\sum_{db\le D_B}\frac{\gamma_N(d)\Lambda(b)}{db}=o_e(u),
\quad \gamma_N(d)=c_N(d)\frac{\log N}{\log(x/d)}.
\]
The finite-modulus version of the same low-product floor proof gives
o_e(u). Its normalized reference floor cost is at most
a·N^(459/400+1/100)(log N)^C=o(u).
All selected absolute power and logarithmic-freezing errors remain o(u).

Removing large primes from β and extending m>U to m>1 adds only zero
rows for 1<m≤U. Consequently the final conclusion is
\[
\boxed{\sum_{n\in J,\ e\mid n}\beta_U(n)V_N(n)=o_e(u),\qquad
a\sum_{n\in B_1,\ e\mid n}\beta_U(n)V_N(n)=o_e(u).} \tag{15}
\]
This proves (2) with e=2. Uniformity is in all sufficiently large even N
for each fixed e; an explicit N-dependent range of e is not supplied.

## 4. Remove all bounded least-prime sectors

For fixed Q≥2 let P(Q)=∏_{q≤Q prime}q. Exact inclusion-exclusion gives
\[
\mathbf1_{P^-(n)\le Q}
=-\sum_{e\mid P(Q),\ e>1}\mu(e)\mathbf1_{e\mid n}.
\]
The finite sum of (15) therefore proves
\[
\boxed{S_{\le Q}(J)=o_Q(u),\qquad
aS_{\le Q}(B_1)=o_Q(u),\qquad E_{\le Q}=o_Q(u).} \tag{16}
\]
Taking differences also handles each individual fixed least prime.
It follows that the remaining sharp comparison can be written, for any
fixed Q, as
\[
E_{Q<q\le U^\varepsilon}+E_{>U^\varepsilon}-E_R
\le(.011+o(1))u. \tag{17}
\]
Every block here is now bounded at u scale, but their signed coefficient
is not controlled at .011.

A diagonal argument allows some sufficiently slowly growing Q(N)→∞ in
(16): choose increasing thresholds so the finitely many sums through Q=j
have normalized size below 1/j. This gives no explicit growth rate and
does not reach Q=U^ε. No quantitative growing-modulus source extension is
claimed. An explicit slowly growing cutoff is a further audit task.

## 5. What completion says about the concrete marked slice

Keep exactly the checkpoint-20 subweight
\[
\mathcal P_N^0=\{p\ {\rm prime}:N^{3/10}\le p\le N^{7/20}\},
\quad\mathcal A_N=\{c\ {\rm even}:N^{1/5}<c\le N^{1/4}\},
\]
\[
T_{\rm mark}(W)=\sum_{p\in\mathcal P_N^0,\ c\in\mathcal A_N}
\frac{\beta_U(c)}{\log(x/p)}
\sum_{b\ {\rm prime},\ cpb\in W}\log b. \tag{18}
\]
The residual need not be smooth or coprime to p. All original gates
hold here automatically for sufficiently large N, as checked in
checkpoint 20. Its normalized original reference remains o(u).

Restrict the outer coefficient in the fixed-mask proof to p∈P_N^0.
This is an admissible partial prime box; its complete Type I floor cost
is already bounded elementarily by N^(7/20)U²=N^(37/100). Keep the
low-product argument and every continuation gate. Define T_comp with
the same prime p range and gates but every even residual c>1 outside A_N.
Then (15) gives the precise completion relation
\[
T_{\rm mark}(J)+T_{\rm comp}(J)=o(u),\qquad
a(T_{\rm mark}(B_1)+T_{\rm comp}(B_1))=o(u). \tag{19}
\]
Thus the two discrepancies are negatives of one another up to o(u).
Equation (19) does not estimate either separately: the weights are signed,
so W_N≤V_N supplies no monotonicity for their sums. The direct absolute
estimate O(N/(log N)^η) is still available for the marked short sum,
but no separate O(u) marked bound has been established here.

The exact even-divisor pairing also supplies a fully gated floor form:
\[
T_{\rm mark}(J)=-\sum_{U/2<d\le U,\ d\ {\rm odd}}\mu(d)
\sum_{p\in\mathcal P_N^0}\frac1{\log(x/p)}
\sum_{b\ {\rm prime}}\log b
\sum_{\substack{N^{1/5}<2d\ell\le N^{1/4}\\2dpb\ell\in J}}1. \tag{20}
\]
For fixed d,p,b the inner count is the nonnegative part of
\[
\min\!\left(\left\lfloor\frac{N^{1/4}}{2d}\right\rfloor,
\left\lfloor\frac{x+N/2}{2dpb}\right\rfloor\right)
-\max\!\left(\left\lfloor\frac{N^{1/5}}{2d}\right\rfloor+1,
\left\lceil\frac{x-N/2}{2dpb}\right\rceil\right)+1. \tag{21}
\]
Repeated small factors are allowed; there is no added coprimality test.
The ℓ interval has width N/(2dpb)≪1. Since d≈U and
pb≈N²/c, the paired denominator has exponent
\[
\log_N(2dpb)\in[44/25,181/100]+o(1). \tag{22}
\]
Both previously audited direct reciprocal engines have empty
top-frequency windows when this exponent is at least 5/4. The lower
edge in (22) exceeds that threshold by 51/100. This rules out that
specific direct mapping, rather than all bilinear methods.
Long Möbius cancellation cannot be inserted into the spiky floor kernel
without a signed kernel estimate. Likewise the prime b intervals still
have relative length exponents [2/7,1/3]; the long-reference PNT does
not justify an individual asymptotic there.

The concrete next task remains a separate signed estimate for (18)/(20),
or a method that controls its coupling with the complementary residual
sectors while retaining the coefficient in (17).

## 6. Reproducibility and claim boundaries

Run `python3 src/marked_even_completion.py`. The new checks passed:

| Exact check | Count |
|---|---:|
| Masked density identities, including small prime-power bases dividing e | 105 |
| Divisibility lattice rows | 112,896 |
| Sharp endpoint floor counts | 1,323 |
| Fixed least-prime inclusion-exclusion rows | 79,996 |
| Actual prime-cofactor cap sites | 138,004 |
| Masked actual outer/cofactor Vaughan rows | 310,543 |
| Independent marked prime rows in the floor regrouping | 2,029 |
| Marked endpoint floor rows | 8,116 |

The marked floor fixture has 357 positive and 114 negative beta rows,
and 42 rows in which the outer prime divides the residual. The full
continuation fixtures independently check residual-beta invariance and
the marked/complementary partition, with both signs and repeated primes.
Stress truncations, enlarged residual cuts and the artificial wider
reference are explicitly labeled. Finite checks certify neither the
asymptotic source estimates nor the marked or .011 bound.

All 226 nonmutable checkpoint-20 records and the frozen negative-frontier
ledger are unchanged. Only four current indices are updated; this note,
its checks, result, source-scope audit and preservation snapshot are new.

| Conclusion | Status |
|---|---|
| Completed signed covariance O(u) and small-q discrepancy O_ε(u) | Proved from admitted inputs and completion |
| Complete even continuation and every fixed small-prime union o(u) | Proved by masked density and fixed-modulus transfer |
| Marked even residual slice separately O(u) or o(u) | Open |
| Explicit growing cutoff reaching U^ε | Open |
| Joint .011 coefficient, higher-degree cap, positive K and H(ϑ) | Open; K=0 |
