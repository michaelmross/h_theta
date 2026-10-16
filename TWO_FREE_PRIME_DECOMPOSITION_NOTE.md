# Two free variables in the prime-product comparison

Checkpoint 26 — Michael M. Ross's H(ϑ) campaign — 11 October 2026

**The sharp .007935u integral bound and original .011u comparison remain
unproved.** This continuation audits the finer prime decomposition
proposed after checkpoint 25 and proves a new regional estimate.

Expanding only the cofactor does not repair the balanced source gap
for the audited one-variable reciprocal transfer. Expanding the smaller
outer prime as well produces two free integer variables. The direct
fractional-part consequence of Robert–Sargos Theorem 3 then controls
all four Type I × Type I components on

\[
p,r\ge N^{1/4},\qquad p\le r,\qquad
pr^2\le N^{3987/2000}=N^{1.9935}.
\]

This includes balanced outer exponents .65,.65. Keeping checkpoint 24's
coverage on the complement leaves a hybrid pair-core reference near
.00561774, instead of that checkpoint's .06064. A new outer Type II
term must be retained in the comparison. Its small Mangoldt-factor
part is also o(u); its larger part is not sharply estimated.

The smaller reference core is not earned prime mass. The new joint
sufficient coefficient .0135582 belongs to a different coupled expression,
including the new outer Type II term. It is not a proof of that bound.

## 1. Original target and exact prime identities

Keep x=N², Y=N+1, u=N/(2 log N), z=N^(1/4), κ=1/1000, the original
c_N, J, B_1, H_1, a=Y/H_1 and every original arithmetic gate.
The auxiliary U=V=floor(N^τ), τ=1/1000, is the same exact-identity
parameter as in checkpoint 24. It does not replace the original
least-prime cutoff floor(N^.01).

Write

\[
I_\kappa=Q_N(\psi_Y)-aQ_N(\psi_{H_1}).
\]

Checkpoint 25 retains the completed identities and budgets

\[
Q_N(J)-aQ_N(B_1)\le I_\kappa+(.003065+o(1))u,
\qquad I_\kappa=\mathfrak H_\kappa(N)+o(u).
\tag{1}
\]

Here q is the whole cofactor before prime expansion; the least prime
called q in the original comparison has a different role.

The remaining signed allowance is .007935. The short centered transform
Φ_N and its N log N tail statement remain as proved in checkpoint 25.
No individual frequency band of an expanded prime identity is assigned
the tail estimate for the complete actual-prime transform.

### 1.1 The finer cofactor identity and its audited limitation

Let μ_Z(n)=μ(n)1_(n≤Z), let 1 denote the constant arithmetic function,
and let log denote n↦log n. The depth-four identity is

\[
\Lambda=\sum_{j=1}^4(-1)^{j-1}\binom4j
  \mu_Z^{*j}*1^{*(j-1)}*\log
\quad\text{on }n<(Z+1)^4. \tag{2}
\]

It follows directly from P=μ_Z*1: δ−P has support n>Z, so
(δ−P)^{*4} vanishes below (Z+1)^4. Use Λ*1=log and expand
δ−(δ−P)^{*4}. All four coefficients 4,−6,4,−1 remain.
Taking Z=floor(X_N^(1/4)), X_N=floor(2N^(7/4)), covers every
cofactor in both original smoothed windows eventually. This is an
exact expansion, not a discarded least-prime sector.

The general identity is described by Heath-Brown in
[*Sieve identities and gaps between primes*, Lemma 1](https://www.numdam.org/item/AST_1982__94__61_0.pdf).
The algebra above independently fixes the truncation and endpoint
conventions needed here.

Suppose only the cofactor is expanded, an unrestricted cofactor
variable of exponent ℓ is eliminated, and another unrestricted cofactor
variable of exponent A is used as the standalone slot. If the actual
outer product has exponent S, then

\[
\Sigma=2-\ell,\qquad A+\ell\le2-S.
\tag{3}
\]

The necessary first facet of the direct unweighted reciprocal bound is
A>2Σ−2. Therefore

\[
A-(2\Sigma-2)\le\ell-S\le2-2S.
\tag{4}
\]

For S≥5/4 this is at most −1/2, irrespective of the depth of the
cofactor identity. The weighted RS1/FI6 windows also remain empty at
their standard top-frequency mapping in this band, as certified earlier.
Thus this cofactor-only elimination cannot use these particular source
interfaces to dispose of every balanced cell.

This excludes neither expanding an outer prime nor a different joint
phase or multidimensional transfer. It is not a global obstruction.

The frequency scales must also be distinguished. Eliminating a free
variable of length L≈x/Q gives reciprocal phase hx/Q, with the critical
integer frequencies h≈Q/Y. Its phase size is then hx/Q≈x/Y≈N.
The shorter Mellin cutoff in checkpoint 25 consequently retains this
critical range; it does not remove the balanced reciprocal blocks.

### 1.2 Expand the smaller outer prime with the complete auxiliary identity

The useful continuation uses the complete two-term Type I plus Type II
Vaughan identity already admitted, on **both** the smaller outer factor
and the cofactor. For k>U define

\[
\begin{aligned}
\mathcal A_U(k)
 &=\sum_{t\mid k,\ t\le U}\mu(t)
       \frac{\log(k/t)}{\log k}
   -\sum_{tb\mid k,\ t,b\le U}
       \frac{\mu(t)\Lambda(b)}{\log k},\\
\mathcal B_U(k)
 &=\sum_{mb=k,\ m>U,\ b>U}
       \frac{\beta_U(m)\Lambda(b)}{\log k},
\qquad
\beta_U(m)=-\sum_{t\mid m,\ t\le U}\mu(t).
\end{aligned} \tag{5}
\]

Exactly,

\[
\frac{\Lambda(k)}{\log k}=\mathcal A_U(k)+\mathcal B_U(k).
\tag{6}
\]

The small Mangoldt term is absent on both physical factors p≥z and
q≈x/(pr)≫N^(2/3). The identity applies to integers in the expanded
slots, including composites and prime powers; their exact cancellations
must be kept. It does not retain a prime-indicator mask on a variable
subsequently described as free.

The Type I products are p=h_pf and q=h_qℓ, where each small product
h_p,h_q is either t≤U or tb≤U². The f and ℓ coefficients are
unit coefficients or logarithmic weights. Thus they are free integer
variables with controlled variation, rather than arbitrary prime coefficients.

## 2. Proper powers, diagonal weights and logarithms

Replacing a prime indicator by Λ(k)/log k introduces proper prime powers.
They cost o(u) absolutely on the short window and its normalized original
reference, even with the fixed divisor-order envelopes of (5).

For the newly expanded smaller p≤r, the original gate implies p≤N^(2/3).
If p=b^j≥z with j≥2, then n is a multiple of b^j. Summing N/b^j+1
over the possible bases gives

\[
O_\epsilon\bigl(N^\epsilon
  (N^{7/8}+N^{1/3})(\log N)^C\bigr)=o(u)
\tag{7}
\]

for sufficiently small fixed ε. For j=2 the reciprocal tail starts at
b≥N^(1/8); j≥3 gives a smaller main exponent. On the long reference,
replace N by H_1 in the multiple count and then normalize: the main
bound is O_ε(N^(7/8+ε)(log N)^C), and the floor part is
O_ε(N^(−2/3+ε)ρ^(−1)(log N)^C), ρ=H_1/x=N^(−o(1)).
The inherited proper-cofactor-power bound is likewise o(u).

Canonical p<r rows have weight one and p=r rows weight one half.
The diagonal has absolute envelope
O_ε(N^ε(N/z+N^(2/3))(log N)^C)=o(u), including the small-variable
convolutions. Its weight is retained in the exact identities and fixtures;
its continuous reference measure is zero.

For the oscillatory error, log ℓ and log q may be frozen at their values
at v=x with an o(u) error. On the short window their variation is O(1/N);
on the long window it is O(ρ). The complete absolute expansions are
bounded by a fixed divisor function. The inherited deterministic Shiu
bound gives O(H(log N)^C) on either window, so the normalized long
freezing error is O(Nρ(log N)^C)=o(u). Do not multiply a slowly decaying
error by an uncontrolled count of tuples.

Weights such as log f/log(h_pf) and 1/log(x/(h_pf r)) remain smooth
weights of bounded total variation on a free-f dyadic box. No oscillatory
Mellin twist or arbitrary coefficient is introduced into the free slot.

## 3. A valid two-free-variable reciprocal estimate

The primary input is the direct fractional-part Lemma 9 following
[Robert–Sargos (2006), Theorem 3, printed pp.14 and 17](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf).
Its inner integer sum is unweighted and has a maximum over subintervals.
For a free slot F, other slot W, and phase size X, its bound is

\[
(FW)^{1+\epsilon}
\left\{\left(\frac{X}{F^2W}\right)^{1/4}
+F^{-1/2}+X^{-1}\right\}.
\tag{8}
\]

Here the reciprocal exponents are −1,−1, satisfying its nonzero
and nonunit-standalone-exponent hypotheses.

In the count, eliminate ℓ from p=h_pf and q=h_qℓ, and retain f as
the free standalone variable. Put

\[
S=\log_N(pr),\quad a=\log_N p,\quad
\alpha=\log_N h_p,\quad \beta=\log_N h_q,
\quad
\Sigma=S+\beta,\quad A=a-\alpha.
\tag{9}
\]

The other slot is W=rh_ph_q. Thus FW≈N^Σ and X≈x/(FW)=N^(2−Σ).
Subtracting the free-ℓ lattice integral at the two short-window endpoints,
(8) gives the three error exponents

\[
\frac{\Sigma+1}{2}-\frac A4,\qquad
\Sigma-\frac A2,\qquad 2\Sigma-2.
\tag{10}
\]

Strict power savings relative to N follow from

\[
A>2\Sigma-2,\qquad \Sigma<3/2. \tag{11}
\]

### 3.1 Retain gates and coefficient restrictions

For a fixed r,h_p,h_q, the physical inequalities p≥z, p≤r and
pr²≤N^g, g=3987/2000, restrict f to an interval:

\[
z/h_p\le f\le
\min\{r/h_p,\ N^g/(h_p r^2)\}.
\tag{12}
\]

Additional dyadic cuts are intervals as well. They are handled by the
source's inner subinterval maximum, followed by Abel summation for the
slowly varying logarithmic weights.

When W is collapsed, different factorizations r h_p h_q can have
different intervals. Take the source's subinterval maximum before
collapsing them. The number of factorizations and the small-variable
coefficients have fixed divisor order; they add an arbitrarily small
power, absorbable by the strict source reserve. This never replaces
the free-f coefficient by an arbitrary sequence.

For ψ_Y average the corresponding sharp centered windows, whose
widths range from Y to (1+2κ)Y. The endpoint phases remain comparable
with x, and every gate stays frozen at x. The source bound is uniform
over these endpoints and partial boxes. Integer cutoffs can be represented
by half-integer thresholds without changing their predicates.

### 3.2 Continuous source certificate

The new two-free-variable region is

\[
\mathcal G_2=\{p,r\ge z,\ p\le r,\ pr^2\le N^{3987/2000}\}.
\tag{13}
\]

The Type I small products satisfy 0≤α,β≤2τ=.002. Since
2S−a≤g, (11)'s first margin obeys

\[
A-2\Sigma+2
=2-2S+a-\alpha-2\beta
\ge .0065-.002-.004=.0005.
\tag{14}
\]

Also S≤2g/3=1.329 and Σ≤1.331, so
3−2Σ≥.338. The free slot is at least N^(.248).
All 12 vertices of the four-dimensional polytope are checked exactly;
the minimum first margin is 1/2000, and the minimum raw-term power
reserve in (10) is 1/8000. Fixed logarithms and a sufficiently small
divisor loss leave some c>0.

At physical p,r exponents .65,.65 and worst small products .002,.002,
the new free slot has A=.648, Σ=1.302, with first margin .044.
This was not an admissible free slot while the outer p was a prime
coefficient. The new identity changes the coefficient family, which
is why the earlier scoped source rejection does not apply to it.

**Lemma 1.** All four Type I × Type I lattice-minus-integral errors
on (13) are O(N^(1−c))=o(u), for some fixed c>0, uniformly in even N.

On the normalized long reference elementary floor bounds suffice:
there are at most N^(1.331+ε) coefficient rows, giving
O(N^(.331+ε)ρ^(−1)(log N)^C)=o(u) after scaling.

## 4. Complete the Type I × Type I main term

Let

\[
\alpha_U=\sum_{t\le U}\frac{\mu(t)}t,\qquad
\gamma_U=\sum_{t\le U}\frac{\mu(t)\log t}t,\qquad
\mathcal L_U=\sum_{b\le U}\frac{\Lambda(b)}b.
\]

The admitted long Möbius estimates give α_U=O(e^(−c√log N)(log N)^C),
γ_U=−1+O(e^(−c√log N)(log N)^C), and ℒ_U=O(log N).
The complete Type I density for a physical factor v is

\[
g_U(v)=\alpha_U-
\frac{\gamma_U+\alpha_U\mathcal L_U}{\log v}
=\frac1{\log v}
+O(e^{-c\sqrt{\log N}}(\log N)^C).
\tag{15}
\]

After the free-ℓ integral, replace the free-f lattice sum by its
integral. Its harmonic weight has variation O(1/F), F≥z/U².
Summing the small products and harmonic r rows costs at most

\[
O\bigl(NU^2/z\,(\log N)^C\bigr)
=O(N^{.752}(\log N)^C)=o(u).
\tag{16}
\]

The p-change of variable is p=h_pf; the physical p endpoints in
(12) are independent of the small-product representation.
Summing the two p Type I components and the two q Type I components
therefore gives the density

\[
\sum_{r\ {\rm prime}}\frac1r
\int_{z\le p\le r,\ pr^2\le N^g}
 g_U(p)g_U(v/(pr))\,\frac{dp}{p}.
\tag{17}
\]

Insert (15), then apply the inherited long prime reciprocal estimate
to r≥z. This is the ordinary reference density on G_2. Its variation
over the original windows is O(|v−x|/(x(log N)²)).

Write \(\mathcal A_{\mathrm I,\mathrm I,\mathcal G_2}(\psi)\) for
the actual sum with \(\mathcal A_U(p)\mathcal A_U(q)\), r prime and
the canonical weight. Lemma 1, (15)–(17) prove

\[
\boxed{
\mathcal A_{\mathrm I,\mathrm I,\mathcal G_2}(\psi_Y)
 =((1+\kappa)M_{\mathcal G_2}+o(1))u,\qquad
a\mathcal A_{\mathrm I,\mathrm I,\mathcal G_2}(\psi_{H_1})
 =((1+\kappa)M_{\mathcal G_2}+o(1))u.}
\tag{18}
\]

This is a statement about the complete double Type I term, including
its main term. It does not estimate the entire actual prime count
on G_2.

## 5. Retain and partially estimate the new outer Type II term

Pointwise expand

\[
(\mathcal A_U(p)+\mathcal B_U(p))
(\mathcal A_U(q)+\mathcal B_U(q)).
\]

The two q-TypeII products recombine exactly:

\[
\mathcal A_U(p)\mathcal B_U(q)
+\mathcal B_U(p)\mathcal B_U(q)
=\frac{\Lambda(p)}{\log p}\mathcal B_U(q).
\tag{19}
\]

After the absolute proper-p-power removal (7), this is the original
cofactor Type II term with its actual prime outer coefficient, restricted
to G_2. The additional term is

\[
\mathcal O_p(\psi)=
\sum_{r\ {\rm prime},\ p\ge z,\ p\le r,\ pr^2\le N^g}
\theta(p,r)\mathcal B_U(p)
\sum_q\mathcal A_U(q)\psi(prq),
\tag{20}
\]

where p,q are integers, θ=1 for p<r and θ=1/2 for p=r. It contains
the actual β_U(p/b_p), Mangoldt and cofactor Type I weights. It is
not an arbitrary sequence or the optional marked estimate.

### 5.1 A summable low-Mangoldt-factor completion

Let Z_p=N^(1/800), and split (20) by the actual Mangoldt factor
b_p in \(\mathcal B_U(p)\). On U<b_p≤Z_p,
m=p/b_p≫N^(.24875)>U, so expand β_U(m)=−Σ_(t|m,t≤U)μ(t)
with m=tf. Now p=t b_p f is free in f; the other free variable
is again the cofactor Type I variable ℓ.

Here α≤τ+1/800=9/4000=.00225 and β≤.002. The same direct
source criterion gives margin

\[
A-2\Sigma+2\ge .0065-.00225-.004=.00025.
\tag{21}
\]

All 12 vertices of this second polytope are also checked; its minimum
raw-term reserve is 1/16000. Use the direct Lemma 9 bound, rather than
inserting the more conservative Y/Q frequency envelope.

In the double lattice integral the p scalar is
−α_U Σ_(U<b_p≤Z_p)Λ(b_p)/b_p, divided by log p. It is exponentially
small, and the q scalar is (15). The p free-integer replacement
costs O(NUZ_p/z (log N)^C)=O(N^(.75225)(log N)^C)=o(u).
Consequently

\[
\boxed{\mathcal O_{p,\ b_p\le N^{1/800}}(\psi_Y)=o(u),\qquad
a\mathcal O_{p,\ b_p\le N^{1/800}}(\psi_{H_1})=o(u).}
\tag{22}
\]

This is a whole signed-term estimate, not just a lattice remainder.
The b_p cutoff is a Mangoldt factor inside an exact identity; it is
not a discarded least-prime sector. The larger-b_p part remains.

### 5.2 Normalize the remaining reference by completion

The original long-PNT comparison on G_2, (18), (19), and the previously
proved normalized long cofactor Type II estimate imply
a O_p(ψ_H1)=o(u). This is a deduction from the complete identity,
not a separate short-interval estimate for the outer β coefficients.
Subtract (22) to obtain the same result for its larger-b_p part.

## 6. Preserve the earlier coverage and form the new joint target

Let G_τ be the auxiliary good outer set from checkpoint 24, unchanged.
Form the new auxiliary union

\[
\mathcal G_h=\mathcal G_\tau\cup\mathcal G_2,\qquad
\mathcal C_h=(\text{actual outer support})\setminus\mathcal G_h.
\tag{23}
\]

Use the double identity on G_2 and the old cofactor identity on
G_τ\G_2. The older estimates remain applicable after the additional
monomial cutoff pr²>N^g, separated before collapsing weighted
coefficients as in checkpoint 24. No source frequency restriction
or earlier gate is changed.

The old complete low-db Type II estimate also holds on G_h with the
actual prime outer coefficients. Its finite new monomial predicates
are separated before the old RS1/FI6 grouping. It removes db≤N^(461/400)
as a whole signed sum. Every core row has d>N^(4609/4000); with b>U
it is outside that low-db range.

Combining (18)–(23) with the original reference gives

\[
\boxed{
I_\kappa=
\mathcal B_{q,\mathcal G_h,\ db>N^{461/400}}(\psi_Y)
+\mathcal O_{p,\mathcal G_2,\ b_p>N^{1/800}}(\psi_Y)
+Q_{\mathcal C_h}(\psi_Y)
-(1+\kappa)M_{\mathcal C_h}u+o(u).}
\tag{24}
\]

All three remaining coefficients are one. The cofactor term uses
the actual original c_N restricted to the new auxiliary union.
The new outer term occurs only on G_2. The positive core is the
original prime-supported count on C_h. Their coupling must be retained.

## 7. Outward reference enclosure for the hybrid core

Use S=log_N(pr), a=log_N p≤log_N r, with ordinary reference density
2/[a(S−a)(2−S)]. Put

\[
L=2S-2,\quad L_B=L+.0025,\quad L_A=L+.0045,\quad
U_B=3-2S-.0064,\quad U_A=3-2S-.0044,
\quad R_2=2S-3987/2000.
\]

Intersecting the old core with the complement of (13) gives these
reference intervals (endpoint conventions have zero reference measure):

| S range | Remaining a intervals |
|---|---|
| [4609/4000, 49891/40000] | [L,L_B] |
| [49891/40000, 49911/40000] | [L,L_B], [U_B,L_A], [U_A,R_2] |
| [49911/40000, 1329/1000] | [L,R_2] |
| [1329/1000, 4/3] | [L,S/2] |

For affine endpoints ℓ≤r with width w=r−ℓ, the exact inner integral is

\[
\frac2{S(2-S)}
\left\{\log(1+w/\ell)+\log(1+w/(S-r))\right\}.
\tag{25}
\]

The two positive logarithms avoid interval dependency loss from taking
a logarithm of a ratio close to one. Outward integration with 12,000
cells per inner-interval piece encloses

\[
\boxed{
M_{\mathcal C_h}\in
[.0056176329347543997289726759920036568828,\
 .0056178552372934597068724043781138837216].}
\tag{26}
\]

The full complement of G_2 alone has reference in
[.01044016094630,.01044120695153]. Keeping the older coverage produces
the smaller hybrid core in (26). Neither number caps its short count.

Using the certified lower endpoint, the exact reference credit in (24)
leads to the concrete sufficient condition

\[
\boxed{
\mathcal B_{q,\mathcal G_h,\mathrm{large}}(\psi_Y)
+\mathcal O_{p,\mathcal G_2,\mathrm{large}\ b_p}(\psi_Y)
+Q_{\mathcal C_h}(\psi_Y)
\le(.0135582+o(1))u.}
\tag{27}
\]

The decimal is rounded down from
(1+κ)·.0056176329347543997289726759920036568828+.007935
=.01355825056768915412870… . Thus no enclosure error is spent without
being recorded. Inequality (27) is unproved. It contains an additional
outer Type II term absent from checkpoint 24's .0686138 formulation.
Comparing those right-hand sides alone is not a comparison of proved
discrepancy bounds.

The explicit Selberg envelope from checkpoint 25 also gives a coarse
upper coefficient 4.945625 for the whole three-term expression in (27),
using the full-reference lower and hybrid-core upper endpoints. This is
far above .0135582; it does not bound the new outer term separately.

## 8. Coverage and coefficient ledger

| Actual family or component | Completed estimate | What remains |
|---|---|---|
| Cofactor-only depth-four identity | Exact, all four terms retained | Audited balanced source gap persists |
| Double Type I on G_2 | Main (18), error o(u) | Full good prime count still includes Type II terms |
| Old cofactor Type I on G_τ\G_2 | Original main, error o(u) | Its larger-db cofactor Type II |
| Cofactor Type II on G_h, db≤N^(461/400) | o(u) | Larger db, actual coefficients retained |
| Outer Type II × cofactor Type I, b_p≤N^(1/800) | o(u) | Larger b_p in (24) |
| Hybrid core actual prime count | Reference enclosure only | Joint sharp short bound |

The original .003065 smoothing and .007935 signed allowance still sum
to .011. The exact identities, proper-power removals and completed
regional errors add zero nonvanishing coefficient cost. A subsequently
used fixed least-prime power cutoff must still charge ξ from checkpoint
22, (23). A fixed multiplier L for the complete original centered
transform must also charge 21147/L from checkpoint 25; the remaining
allowance is then .007935−ξ−21147/L. The new Mangoldt-factor cutoff
in (22) spends no such budget because its full selected term is proved
o(u).

The next analytic input is a one-sided estimate for the coupled
three-term expression (24), or the original centered integral with its
unchanged coefficient. Independent absolute charges for these new
signed terms are not justified by the reference mass calculation.

## 9. Verification and preservation

Run python3 src/two_free_prime_decomposition.py.
Its exact checks cover the depth-four convolution identity, tensor
Vaughan products in independent logarithmic-prime coefficients, the
coefficient-one recombination, composite cancellation, proper-power
and diagonal rows, independent outer-Mangoldt-factor partitions,
continuous rational source facets, the independently formed union-complement
geometry with affine endpoint-order guards, and outward reference arithmetic.
Finite fixtures do not prove (27); the regional analytic proofs are
(7)–(22).

All 259 nonmutable checkpoint 25 records and the frozen historical
mass ledger are preserved byte for byte. The older good sets, notes,
source bytes and reference enclosures remain unchanged. The new
sets are auxiliary to a new complete identity for the same target.
K remains zero; H(ϑ), the original sharp comparison, the optional
marked estimate and higher-degree allocation remain open.
