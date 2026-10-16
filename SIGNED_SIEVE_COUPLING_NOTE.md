# Signed sifting of the coupled small-prime sectors

Checkpoint 22 — Michael M. Ross's H(ϑ) campaign — 9 October 2026

The coupling alternative in checkpoint 21 can now be controlled while
preserving the original coefficient. The separate marked estimate (18)/(20)
is still open. The new result estimates the surrounding small-prime sectors
as one signed sum, retaining every original outer and continuation weight.

Let S_≤T(W) be the β_U V_N sum on P⁻(n)≤T, and let
E_≤T=S_≤T(J)−aS_≤T(B₁), with the actual shell and frozen reference below.
For every growing subpower cutoff,
\[
T_N\longrightarrow\infty,\qquad \log T_N=o(\log N),
\]
the admitted inputs and the argument here prove
\[
\boxed{|S_{\le T_N}(J)|+a|S_{\le T_N}(B_1)|=o(u),
\qquad E_{\le T_N}=o(u).} \tag{1}
\]
For example, take T_N=U^(1/log log N). Consequently the remaining
comparison in checkpoint 21, (17), is equivalent to
\[
\boxed{E_{T_N<q\le U}-E_R\le(.011+o(1))u.} \tag{2}
\]
No part of .011 is consumed in this reduction. Here q denotes the least
prime factor, E_R=R_N(J)−aR_N(B₁), and the high block stops at U.
All coefficients in (2) remain one. The inequality in (2) is **not proved**.

There is also a useful fixed-power version:
\[
\boxed{\lim_{\varepsilon\downarrow0}\limsup_{N\to\infty,\ N\ {\rm even}}
\frac{|S_{\le U^\varepsilon}(J)|+
a|S_{\le U^\varepsilon}(B_1)|}{u}=0.} \tag{3}
\]
Thus a sufficiently small fixed ε can spend any prescribed positive budget
ξu; the complementary comparison at coefficient .011−ξ would suffice.
Neither o(u) for each fixed ε>0 nor a numerical ε achieving a .001 budget
is claimed. The fixed positive mask exponent below is established by the
strict source margins, but its final numerical value is not selected here.

The full signed covariance remains O(u). The direct absolute-beta exponent
η≈.0602478244, the frozen mass ledger, K=0 and the status of H(ϑ) are unchanged.
The sharp residual comparison, higher-degree allocation and H(ϑ) remain open.

## 1. Keep the original continuation and reference

Use the definitions of MARKED_EVEN_COMPLETION_NOTE.md without alteration:
\[
x=N^2,\quad J=[x-N/2,x+N/2]\cap\mathbb Z,\quad Y=N+1,
\quad u=N/(2\log N),\quad U=\lfloor N^{1/100}\rfloor,
\]
\[
H_1=2\lfloor x e^{-3(\log x)^{1/3}}/2\rfloor+1,
\quad B_1=(x-H_1/2,x+H_1/2)\cap\mathbb Z,\quad a=Y/H_1.
\]
All gates and outer weights are frozen at x. In particular,
\[
\beta_U(m)=-\sum_{t\mid m,\ t\le U}\mu(t)\quad(m>1),\quad\beta_U(1)=0,
\]
\[
V_N(n)=\sum_{d\in D_{\rm good},\ d\mid n}
\frac{c_N(d)}{\log(x/d)}
\sum_{\substack{b\mid n/d,\ b>U\ {\rm prime}\\
db>N^{459/400},\ n/(db)>1}}\log b. \tag{4}
\]
The exact c_N, D_good and pair-ordering gates are those in checkpoint 21;
there is no enlargement to arbitrary bounded continuation coefficients.
We use the inherited bound 0≤V_N≤36+o(1) throughout both windows.

Write
\[
B_e(W)=\sum_{n\in W,\ e\mid n}\beta_U(n)V_N(n). \tag{5}
\]
Checkpoint 21 proved B_e(J)=o_e(u) and aB_e(B₁)=o_e(u) for each fixed
squarefree e>1. The first new step is a uniform extension which can be
summed over a small power range.

## 2. A summable growing-mask completion estimate

**Lemma.** There is a fixed δ₀>0, less than 1/100, for which
\[
\boxed{\sum_{\substack{1<e\le2N^{\delta_0}\\\mu^2(e)=1}}
\big(|B_e(J)|+a|B_e(B_1)|\big)=o(u).} \tag{6}
\]
The outer weight remains the actual c_N on D_good. The same proof works
for the original marked outer prime band with its full continuation.
This lemma is a deduction from the admitted completion and source estimates,
not an invocation of a short-interval Möbius theorem.

### 2.1 Uniform scalar densities, summed with their 1/e factor

For squarefree e define
\[
A_e=\sum_{t\le U}\frac{\mu(t)}t\frac{(e,t)}e,\quad
\Gamma_e=\sum_{t\le U}\frac{\mu(t)\log t}t\frac{(e,t)}e,
\]
\[
L_e=\sum_{b\le U}\frac{\Lambda(b)}b
\sum_{t\le U}\frac{\mu(t)}t\frac{(e,tb)}e. \tag{7}
\]
The exact masked Type I density is
\[
G_e(v)=\sum_{d\in D_{\rm good}}\frac{c_N(d)}d
\left[A_e-\frac{\Gamma_e+L_e}{\log(v/d)}\right]. \tag{8}
\]
In the logarithmic lattice integral there is no extra log e or log h:
the original variable has logarithm log(v/(dt)).

Set C_e=∏_{p|e}(1−1/p)^(−1), and write α_e⁰(y), γ_e⁰(y) for the
coprime harmonic Möbius sums in checkpoint 21, (11). Their Euler convolution
is over integers h whose prime factors divide e. Split it at √y. For
h≤√y the inherited quantitative Möbius PNT applies at y/h≥√y; the
sum of reciprocal weights is at most C_e. The logarithmic version adds
only powers of log N. The remaining tail is bounded by a power of y^(−1)
times
\[
J_e=\prod_{p\mid e}(1-p^{-1/2})^{-1}.
\]
Uniformly for e≤2N^δ with any fixed δ<1/100,
J_e=N^{o(1)} and C_e≪log log(3e). For example,
log J_e≪ω(e)≪log(3e)/log log(3e); this already suffices for the
power-decaying tail. Since y≥U/e≥N^(1/100−δ+o(1)), there is c_δ>0
with uniform bounds
\[
|\alpha_e^0(y)|+|\gamma_e^0(y)+C_e|
\ll C_e(\log N)^C e^{-c_\delta\sqrt{\log N}}. \tag{9}
\]
The tail can be absorbed into (9) for large N; the estimates are not
multiplied by N^δ when summing the main scalar errors.

The exact identities from checkpoint 21 are
\[
A_e=\frac1e\sum_{r\mid e}\mu(r)\alpha_e^0(U/r),
\quad\Gamma_e=\frac1e\sum_{r\mid e}\mu(r)
\big[\gamma_e^0(U/r)+\log r\,\alpha_e^0(U/r)\big]. \tag{10}
\]
For e>1 the constant −C_e cancels because Σ_{r|e}µ(r)=0. Thus
|A_e|+|Γ_e|≪τ(e)C_e e^(−1)(log N)^C exp(−c_δ√log N).
The required sum has only logarithmic cost:
\[
\sum_{\substack{e\le2N^\delta\\\mu^2(e)=1}}\frac{\tau(e)C_e}{e}
\le\prod_{p\le2N^\delta}\left(1+\frac2{p-1}\right)
\ll(\log N)^2. \tag{11}
\]
The small Mangoldt variable also retains bases dividing e. Precisely,
\[
L_e=A_e\sum_{p^k\le U,\ p\nmid e}\frac{\log p}{p^k}
+\sum_{p\mid e}A_{e/p}\sum_{p^k\le U}\frac{\log p}{p^k}. \tag{12}
\]
Here A₁=α_U is exponentially small. Summing the second term first in
e=p f and then in p costs at most
Σ_{p≤2N^δ}log p/(p−1)≪log N times Σ_f|A_f|.
Equations (9)–(12) therefore give
\[
\sum_{\substack{1<e\le2N^\delta\\\mu^2(e)=1}}
(|A_e|+|\Gamma_e|+|L_e|)
\ll(\log N)^C e^{-c_\delta\sqrt{\log N}}. \tag{13}
\]
Since Σ_d c_N(d)/d=O(1) and log(v/d)≫log N, their density integrals
on J and normalized B₁ are o(u). The low-db subtraction has the scalar
A_e and the same summable bound.

### 2.2 Perturb the source inequalities, rather than assuming mask uniformity

Every outer prime exceeds N^(1/4), and e≤2N^δ<U eventually. Hence the
outer d is coprime to e; the retained prime b>U is also coprime to e.
For Type I split t and the small Mangoldt b by their gcd classes with e.
There are at most τ(e)²≤e² independent pairs of classes. On each, put
ℓ=h j, where h=e/(e,t) or e/(e,tb). The coefficients in the separated
slots remain bounded or of the same fixed divisor order. No joint frequency
coefficient is introduced, and every original ordering and db gate remains.

Let κ=log_N h, Σ be the original coefficient-product exponent, A the
standalone slot exponent, and H=N^η the frequency scale. The transformed
center is x/h, length Y/h and phase size exponent
\[
\xi=\eta+2-\kappa-\Sigma,\qquad
\eta\le\max(0,\Sigma-1+\kappa)+\nu,\quad\nu=1/10000. \tag{14}
\]
Direct substitution in the original raw bounds gives these perturbed
strict facets (FI's A is its reciprocal B slot):

| RS | FI1989 Theorem 6 |
|---|---|
| A>4η+2−κ−2Σ | A<(8Σ−7η−6+3κ)/7 |
| A<Σ−3η | A<(6Σ−5η−4+2κ)/7 |
| A>2η | A<(5Σ−5η−2+κ)/8 |
| η<2−κ−Σ | A<(4Σ−5η−2+κ)/5 |
| | A>η |
| | A<(2−κ−Σ−η)/2 |

These use [Robert–Sargos (2006), Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)
and the original FI formula already audited in FI_1989_AUDIT.md.
They are derived substitutions; neither source states the campaign mask lemma.
FI's additive-character frequency restriction and its admitted interval
completion are retained.

The frozen rational certificates in results/delta_grouping_facets.json
cover 80 vertices, with minimum condition margin τ=1/10000. Increasing
κ from zero increases the top η by at most κ. Each displayed condition
margin decreases by at most 4κ. Thus for 0≤κ≤τ/16 the whole continuous
regions retain margin at least 3τ/4, including the branch where Σ crosses
1−κ. This Lipschitz bound handles that new branch without a sampled
frequency argument. The exact script verifies the enclosing affine slabs.

The raw term savings are the condition margins times
(1/4,1/4,1/2,1/2) for RS and
(7/12,7/8,1,5/8,1/2,1/2) for FI. Hence there is a uniform positive
power reserve before the arbitrarily small coefficient, smoothing and Mellin
losses. The same reasoning covers the inherited low-db Type II regions.
The elementary rows below the transfer threshold also retain their savings
after a sufficiently small δ is chosen: their denominator-row counts do
not increase under a fixed gcd restriction.

Choose the sharp-transfer losses strictly below this reserve. There are
then fixed c_*>0 and C<∞ such that an e-mask's summed floor errors are
\[
\ll e^C N^{1-c_*}(\log N)^C,\qquad 1<e\le2N^\delta. \tag{15}
\]
To justify the polynomial dependence in (15), the only e-dependent
operations are at most e² gcd classes, h≤e in the rescaled window and
phase, and polynomial bounds for the corresponding smooth cutoffs.
The source constants are uniform in bounded coefficient restrictions and
real phase size; the original product gates are separated by the same
Mellin procedure. A boundary representation remains bounded by a fixed
divisor function. All these losses are polynomial, not unspecified O_e
constants. Select the losses and their fixed power reserve first, then take
\[
0<\delta_0<\min\!\left(\tau/32,\ 1/100,\ c_*/(2(C+1))\right). \tag{16}
\]
For e≤2N^δ₀ the phase condition eventually has κ≤τ/16. Summing (15)
over e now gives O(N^(1−c_*/2)(log N)^C)=o(u). This is a fixed positive
power range, although an optimized or numerical δ₀ is not supplied.

On B₁ elementary floor bounds suffice. With the gcd-class cost included,
normalizing the Type I rows costs at most
a·N^(4/3+1/50) N^(Cδ₀)(log N)^C=o(u), after reducing δ₀ if necessary.
The corresponding low-db cost is at most
a·N^(459/400+1/100) N^(Cδ₀)(log N)^C=o(u).

### 2.3 Sum masks before freezing the long-reference logarithms

The inherited absolute proper-power errors have fixed positive power
savings, both for the full cofactor and for the large Mangoldt b slot.
The number of selected squarefree masks dividing any n is at most τ(n).
Multiplying their absolute envelope by this divisor factor adds an
arbitrarily small power loss, which can be absorbed into those fixed savings.
The masked ordinary prime cofactor term vanishes: a prime cofactor is
≫N^(2/3), whereas e≤2N^δ₀ and is coprime to the outer. Only the inherited
proper-power error remains.

A separate precaution is needed for logarithmic freezing on B₁. Multiplying
an o(u) freezing error by the number N^δ₀ of masks would be invalid, since
the reference relative width is only
ρ=H₁/x=exp(−3(log x)^(1/3))+O(1/x). Instead sum masks pointwise first.
The complete absolute continuation is bounded by Cτ(n), and the mask
count supplies one further τ(n). Since τ(n)²≤d₄(n), the deterministic
Shiu bound gives a total envelope O(H₁(log N)^C). Its normalized
freezing cost is O(Nρ(log N)^C)=o(u). On J the relative width is O(1/N),
and the same bound gives a logarithmic-size error. The short free-variable
Type I variation errors have the inherited fixed power savings and can
absorb the small aggregate mask loss as in (15). On B₁ integrate the
masked Type I density with its original varying denominator; its sum is
already negligible by (13). Only the lattice remainder needs elementary
partial summation. Thus no slowly decaying Type I reference error is
multiplied by N^δ₀ either.

Finally apply the exact masked Vaughan completion, the summable densities
(13), all good Type I errors, low-db removal and the selected absolute
errors just treated. Their sum proves (6). No short prime asymptotic is used.

## 3. Positive sieve errors control an approximation to a signed sum

Put D=N^δ₀. Let T→∞ with T≤N^(δ₀/64), and set z_T=T+1/2, so
the odd primes p<z_T are exactly the odd primes p≤T. Write
\[
\chi_T(n)=\mathbf1_{(n,\prod_{3\le p\le T}p)=1},\qquad
s=\frac{\log D}{\log z_T}.
\]
Use the dimension-two beta sieve on **odd primes only**, with fixed sieve
parameter B=32, predicates
\[
p_1\cdots p_{r-1}p_r^{B+1}\le D,\qquad
z_T>p_1>\cdots>p_r\ge3,
\]
and coefficients λ_e^±∈{−1,0,1}. This parameter satisfies the sufficient
fundamental-lemma condition: 2e log(32/31)(32/31)²<1/e. Both λ₁=1;
coefficients are supported on squarefree odd e≤D.

The exact combinatorial identities and the fundamental lemma are given in
[Tao (2015), Proposition 14 and Lemma 17](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/).
For ν^±(n)=Σ_{e|n}λ_e^± they give nonnegative terminal expansions of
ν⁺−χ_T and χ_T−ν⁻. Each terminal is an odd product
d=p₁⋯p_r and imposes d|n with no odd prime below p_r dividing n.
For the model
\[
g(p)=2/p\ (p\ge3),\qquad
V_2(v)=\prod_{3\le p<v}(1-2/p)\asymp(\log v)^{-2},
\]
the sum of the upper and lower positive model terminal errors is
\[
\sum_r\sum_{d\in\mathcal E_r}g(d)V_2(p_r)
\ll V_2(z_T)e^{-s}. \tag{17}
\]
The omission of 2 is essential: g(2)=1 would invalidate the strict
g(p)<1 input. The complete even continuation has already been treated
by (6), and is not charged through this sieve majorant.

The terminal products, as well as the coefficients, lie below D. For
r≥3 use the last satisfied predicate of the same parity at r−2:
d≤D p_(r−2)^(2−B)≤D. For r=1,2 use z_T²≤D. This support fact
allows the short-interval upper bound below uniformly at every terminal.

### 3.1 The actual-beta majorant and the short-shell upper bound

Let f_U(n)=2^(ω_{≤U}(n)), a nonnegative multiplicative function with
f_U(p^k)=2 for p≤U, and 1 otherwise. Then |β_U(n)|≤f_U(n)≤d₂(n).
If a terminal d has r distinct primes and n=d m, repeated primes are
allowed and
\[
f_U(n)\le2^r f_U(m). \tag{18}
\]
For odd n satisfying the terminal avoidance condition, m has no prime
below q=p_r, including 2. Apply the deterministic Shiu upper bound to
f_U(m)1_{P⁻(m)≥q} on the scaled window W/d. Its center is ≍N²/d;
its length is ≍H/d, where H=Y or H₁. With a fixed interval exponent
1/30 the hypothesis holds uniformly for d≤D: the shorter window has
length exponent 1−δ₀, exceeding (2−δ₀)/30. Rounding the real endpoints
costs only a bounded enlargement of this polynomial-length window.

[Mangerel (2023), Lemma 3.2](https://link.springer.com/article/10.1007/s40687-023-00376-0)
states the needed deterministic form for divisor-bounded multiplicative
functions; it is not an almost-all-interval result. Its Euler product here is
\[
\prod_{p<q}(1-1/p)\prod_{q\le p\le U}(1+1/p)
\ll\frac{\log U}{(\log q)^2}.
\]
Thus, uniformly over all terminals and either original window,
\[
\sum_{\substack{n\in W,\ n\ {\rm odd}\\d\mid n,
\ p\nmid n\ (3\le p<q)}}f_U(n)
\ll H\,\frac{2^r}{d}\frac{\log U}{(\log q)^2}. \tag{19}
\]
Using V_N≤36+o(1), (17), V₂(q)≍1/log²q and (19) now gives
\[
\sum_{n\in W,\ n\ {\rm odd}}
|\beta_U(n)|V_N(n)(\nu^+(n)-\nu^-(n))
\ll H\frac{\log U}{(\log z_T)^2}e^{-s}. \tag{20}
\]
This is the only use of absolute values at the new sieve step. It charges
the positive approximation error, not an entire marked or least-prime sector.
The constant in (20) is independent of T and s in the stated range.

### 3.2 Keep the signed identity and the coefficient one

Set w(n)=β_U(n)V_N(n). On odd n the true small-prime indicator is
1−χ_T(n). Direct expansion, with λ₁⁺=1, gives the exact identity
\[
\boxed{S_{\le T}(W)=B_2(W)
-\sum_{e>1}\lambda_e^+\big(B_e(W)-B_{2e}(W)\big)
+\sum_{n\in W,\ n\ {\rm odd}}w(n)(\nu^+(n)-\chi_T(n)).} \tag{21}
\]
Every mask in (21) lies at most 2D. The first two terms have total
absolute size o(u) on J and normalized B₁ by (6), uniformly in the
chosen bounded coefficients. The last term is bounded using the positive
gap in (20). In particular, we never multiply a sieve inequality by a
signed w and infer an ordered inequality for its sum.

Combining both windows, with aH₁=Y≈N, proves the uniform estimate
\[
\boxed{\frac{|S_{\le T}(J)|+a|S_{\le T}(B_1)|}{u}
\le C\left(\frac{\log N}{\log(T+1/2)}\right)^2
\exp\!\left(-\frac{\delta_0\log N}{\log(T+1/2)}\right)+o(1).} \tag{22}
\]
The o(1) is independent of T in this range; it is the summed mask error.
No numerical value of C is needed to take the limits below.

For T_N→∞ with log T_N=o(log N), the ratio r_N=log N/log(T_N+1/2)
tends to infinity and T_N≤N^(δ₀/64) eventually. Since r_N²e^(−δ₀r_N)→0,
(22) proves (1). For the explicit T_N=U^(1/log log N), the displayed
error is
\[
O\big((\log\log N)^2(\log N)^{-100\delta_0+o(1)}\big)u+o(u).
\]
For sufficiently small fixed ε>0 and T=U^ε, (22) instead gives
\[
|S_{\le U^\varepsilon}(J)|+a|S_{\le U^\varepsilon}(B_1)|
\le\big(C'\varepsilon^{-2}e^{-100\delta_0/\varepsilon}+o_\varepsilon(1)\big)u,
\tag{23}
\]
which proves (3). A fixed ε leaves a fixed, possibly very small coefficient;
letting N tend to infinity alone does not remove it.

## 4. What this controls in (18)/(20), and what is still missing

Keep exactly the checkpoint-21 marked p band and even residual cut, and
write T_comp for its even residual complement with the same continuation
gates. Let T_even,other comprise the even rows from the other eligible
outers. Row by row, with the original logarithmic ratios,
\[
B_2(W)=T_{\rm mark}(W)+T_{\rm comp}(W)+T_{\rm even,other}(W). \tag{24}
\]
The marked outer-band completion already proves T_mark+T_comp=o(u).
Equation (21) and the new small-prime estimate control the entire coupled
union in (24) together with the remaining odd small-prime sectors. There
is no factor greater than one on T_mark, T_comp or the rough counterweight.
The large opposing marked reference masses are not charged separately.

In the original range c<p automatically. Removing the even residual cut
restores the Vaughan convolution; keeping that cut still breaks it.
The exact odd-divisor spiky floor kernel in checkpoint 21, (20), is
therefore **not** separately estimated by this argument. No separate O(u)
or o(u) bound is supplied for T_mark(J), and no individual short prime
asymptotic or signed Möbius kernel theorem is inserted there.

For any fixed Q, E_≤Q=o(u), while E_≤T_N=o(u) by (1). Subtracting
these from checkpoint 21, (17), proves precisely the equivalence (2).
This is coefficient-preserving control of the surrounding sectors, and
an explicit growing cutoff superseding the earlier diagonal-only cutoff.
For a fixed power one may instead choose ξ>0 and a sufficiently small
fixed ε from (23); then proving
E_(U^ε<q≤U)−E_R≤(.011−ξ+o(1))u suffices. A numerical ε requires
evaluating C and a usable δ₀; this checkpoint does not invent either.

The next concrete task is the **joint signed comparison**
E_(T_N<q≤U)−E_R in (2), with its original .011 coefficient.
For methods needing a fixed power threshold, use (23) with an explicit
error budget and keep that budget in the final coefficient. The completed
order estimates make both aggregate terms O(u), but give no sharp
coefficient. A separate marked estimate remains an optional stronger task.

## 5. Verification and preservation

Run `python3 src/signed_sieve_coupling.py`. It checks the exact beta-sieve
upper and lower terminal identities, their dimension-two Euler models,
coefficient and terminal level support, repeated-prime majorants, and
the continuous source-facet perturbations. Its original-continuation
fixtures verify (21) and (24) as rational coefficients of each positive
log b/log(x/d) basis term, including both marked signs and repeated b.
The finite fixtures use explicitly labeled stress U, an enlarged residual
cut and an artificial wider reference; they are not asymptotic samples.
Finite checks do not prove (6), (22), a separate marked estimate or (2).

All 232 nonmutable checkpoint-21 records and the negative-frontier ledger
are preserved byte for byte. Only the four current indices change. This
note, its checking code, result, source-scope audit and preservation snapshot
are new. The complete archive preserves every earlier checkpoint source
and proof file; no previous claim is silently rewritten.

| Claim | Status |
|---|---|
| Summable completion on a fixed positive power mask range | Proved from uniform densities and perturbed strict source bounds |
| Coupled signed small-prime discrepancy at every growing subpower cutoff | o(u), with original gates and reference |
| Explicit cutoff U^(1/log log N) | o(u), no .011 coefficient consumed |
| Fixed U^ε small block as ε↓0 | Arbitrarily small coefficient budget; no fixed-ε o(u) claim |
| Marked residual (18)/(20) separately at u scale | Open |
| Joint high-block/rough comparison at coefficient .011 | Open |
| Higher-degree allocation, K>0 and H(ϑ) | Open; K remains 0 |
