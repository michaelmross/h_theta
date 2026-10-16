# Audit of 007 for the H(ϑ) campaign

Michael M. Ross's square-root interval investigation. Checkpoint 12, 7 October 2026.

**Result.** 007 supplies useful divisor-graph methods, but it does not currently estimate the campaign's signed Vaughan remainder. This audit derives a translated-interval version of its qualitative graph bound and identifies the precise analytic and coefficient transfers still needed. The .011u estimate, the separate higher-degree cap, a positive prime coefficient K, and H(ϑ) remain unproved.

The source is OpenAI, *Ordinary two-point correlations of multiplicative functions*, 24 September 2026: the complete 87-page manuscript, its TeX build, and selected actual Lean implementation files, at repository commit **adc7f1241b42e322a6451854ab7e4b4c146bf78a**. The manuscript PDF has SHA-256 **ccb6f339a7505db7ab158dae4b739164ed8dda32be4012b0310198dd32f5c70a**. See the [primary manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf). Unchanged source bytes and a provenance manifest are included under sources/openai007.

This is a mathematical audit of the critical proof mechanisms and their applicability. No fatal defect was identified in the arguments checked below. That finding is narrower than an independent certification of every proof dependency. The Lean comparator and its transitive axiom check were **not** rerun; the selected Lean source files in this checkpoint are reading evidence, not a complete buildable formalization.

## 1. The actual estimate to be supplied

Keep checkpoint 11's definitions. For even N,

\[
x=N^2,\qquad J_N=[x-N/2,x+N/2]\cap\mathbb Z,\qquad
Y=N+1,\qquad u=\frac{N}{2\log N}.
\]

The geometric width is N; Y counts integer sites. Take
\[
U=V=\lfloor N^{1/100}\rfloor,\qquad
\beta_U(m)=\sum_{\substack{t\mid m\\t>U}}\mu(t)
          =-\sum_{\substack{t\mid m\\t\le U}}\mu(t)\quad(m>1).
\]

The bounded, frozen outer coefficient c_N(d) is the prime indicator on
N^(1/4)≤d<N^(19/20), plus one half of the ordered prime-pair indicator
d=pr with p,r≥N^(1/4) and pr max(p,r)≤N². Thus 0≤c_N≤1 and its
support lies between N^(1/4) and N^(4/3). The exact definition, including
prime powers and ordering errors, is preserved in TWO_THREE_BILINEAR_NOTE.md.

The remaining Type II term is
\[
B_N(J_N)=
\sum_d c_N(d)
\sum_{\substack{m>U\\b>V}}
\frac{\beta_U(m)\Lambda(b)}{\log(mb)}
\mathbf1_{J_N}(dmb).
\tag{1}
\]

Checkpoint 11 proved
\[
\Delta_2+\Delta_3=B_N(J_N)+R_{I,\mathrm{core}}(J_N)+o(u),
\tag{2}
\]
where the Type I core has outer support
N^(9/8)<d≤N^(4/3), consisting of the specified prime pairs. Its precise
signed reciprocal-floor form is equation (18) of JOINT_REMAINDER_NOTE.md.
All normalized long remainders and the Type I floor error through exponent
9/8 are already negligible. The current sufficient target is
\[
B_N(J_N)+R_{I,\mathrm{core}}(J_N)
\le(.011+o(1))u
\tag{3}
\]
for **every sufficiently large even N**. An almost-everywhere conclusion
or an estimate for a different coefficient family does not establish (3).

## 2. What the main results of 007 quantify

Theorem 1.1 has the order of quantifiers
\[
\exists c>0\ \forall\text{ fixed nonproportional affine forms }L_1,L_2\
\exists C_{L_1,L_2}\ \forall X\ge3:
\left|\sum_{n\le X}\lambda(L_1(n))\lambda(L_2(n))\right|
\le C_{L_1,L_2}\frac{X}{(\log X)^c}.
\tag{4}
\]
There is no asserted uniform bound on C for forms whose slopes or
intercepts grow with X. The manuscript also does not promise effective
constants.

Theorem 1.2 and Corollary 1.3 give ordinary correlation limits for fixed
one-bounded multiplicative functions, if one is uniformly nonpretentious
against every fixed Dirichlet character with twist height |t|≤N. They give
no rate for this general class. The functions, forms, and progression
parameters are fixed before the averaging variable increases.

Two separate attempts to obtain the required window estimate fail:

* Subtracting (4) at the endpoints near N² gives an error of order
  N²/(log N)^c, not an error measured by the window length N.
* Reindexing the window by n↦N²-N/2+n introduces intercepts depending on N.
  The fixed-form constants in (4) then provide no uniform estimate.

These are limitations of those deductions. They are not counterexamples
to 007 or proofs that its methods cannot be adapted.

There is a simple logical witness for the first limitation. Let
N_j=2^(2^j), j≥1, and let a(n) be one on the disjoint windows J_(N_j)
and zero elsewhere. The prefix sums satisfy
\[
0\le\sum_{n\le T}a(n)\le3\sqrt T
=o\!\left(\frac{T}{(\log T)^c}\right)
\]
for every fixed c>0. Yet the average on every selected window is one.
Indeed, the accumulated lengths through the jth window are at most
2N_j, and any T meeting that window has T≥N_j²/2. This sequence is
**not multiplicative**; it witnesses only that a prefix bound alone cannot
imply the requested localization.

## 3. Critical proof checks

The source was inspected through the analytic centering, graph traces,
arithmetic constraints, forest and cylinder enumeration, spectral
localization, and affine deductions. The following checks distinguish
algebraic validity from the stronger application we would need.

| Source location | Check and finding | Campaign consequence |
|---|---|---|
| §3, Lemma 3.1 | CRT marginals, bit encoding, nonnegative Fourier correction, and bounded independence fit the displayed budgets. The interval condition is exp(L^A/2), **not** exp(L^(A/2)). | Uniform translated residue tests are available for primes at most exp(L) and fixed modulus l. |
| §4, Lemmas 4.2–4.4 | The rough fourth moment and the fixed-frequency averaged MRT input pay for the frequency exceptional set. With log Z≥L^A/2 and A≥1000, the claimed L^(-.8) short-mean bound is consistent. | The analytic average remains over a long initial interval. |
| §§5–6 | One reciprocal is charged per distinct numerical prime before enlargements. Independent resampling retains separate abstract reciprocal factors. The real-rank lemma avoids any assumption of invertibility modulo every controlling prime. | Useful arithmetic machinery, but its independent harmonic prime variables are not automatically the campaign's divisor coefficients. |
| §7, Lemma 7.2 | The quotient-space incidence graph is a forest because the retained line directions are independent. Nonzero run increments prevent immediate reversals. Endpoints therefore decode each regular segment. The code universe is independent of the padding values. | The pattern bound can precede the padding summation without multiplying by a family for every padding choice. |
| §7, Lemma 7.3 | Backward induction bounds the padding sum in one common residue environment by K^m. Independence of successive sites is unnecessary. | This is a valid weighted-path summation device. |
| §8, Lemma 8.1 | The resolvent proof works for noncommuting self-adjoint edge matrices. Positivity along both signs of the real parameter controls the projected adjacency operator. | A general auxiliary transfer lemma is available once a suitable nonbacktracking moment has been proved. |
| §§10–12 | Raw bias capture and centering use multiplicativity after dilation. The general MRT input is used with its frequency supremum outside the integral. The limits fix B before the long variable tends to infinity. | These steps do not give a uniform rate for a changing β_U or a square-centered window. |
| §§13–15 | Primitive-path descent, rerooting, and private-coordinate extraction provide triangular constraints. Reverse elimination preserves the nonzero and invertibility conditions. Cylinder rank may jump; re-minimizing the predecessor still bounds the number of generators. | The conditional sieve preserves free center residues for signed averaging. |
| §16 | θ=β_Z²=1/4 cancels the good singleton's order-1/p contribution. Return normalizations are retained until that signed integral is taken. Factorials for repeated token types are retained in the exponential summation. | The cancellation depends on this specific divisor graph and normalization. |
| §17 | Singular-value moments handle complex edge coefficients. Exceptional blocks are periodic; Cauchy bounds their weighted mass without assuming independence. | This step can be localized, as proved in Section 5 below. |
| §§9 and 18 | The affine dilation identities and finite expansions at primes dividing fixed coefficients include nonunit residue classes. | The constants and finite expansions still depend on the fixed forms. |

The quoted short-interval results were checked against the actual corrected
[MRT manuscript, version 3](https://arxiv.org/abs/1503.05121v3), Theorems
1.3 and 1.7 and Lemma C.1. The bounded-independence specialization agrees
with [Braverman's Corollary 2](https://www.cs.toronto.edu/~mbraverm/Papers/FoolAC0v7.pdf).
The original versions of those inputs should not be substituted without
checking their hypotheses.

For clarity, the §8 transfer lemma says that if
\[
\mathscr B_{ij}=\mathbf1_{i\ne j}B_j,\quad
\|B_i\|\le a,\quad
\sum_i\|B_iv\|^2\le b^2\|v\|^2\quad(v=Pv),
\]
with self-adjoint B_i and orthogonal projection P, then
\[
\left\|P\left(\sum_iB_i\right)P\right\|
\le3\max\{a,b,\rho(\mathscr B)\}.
\tag{5}
\]
Its proof uses the resolvent of each B_i separately. In particular, P is
not inserted into every intermediate centered path: doing so would
require a new cancellation argument. Formula (5) does not by itself
estimate the spectral radius on its right.

## 4. Where the quantitative proof loses the short window

The decisive issue is already visible before the high-trace bound.
In §2.3, the pair (d,q) belongs to a logarithmic bin of width η and
T_j=X exp(jη). Full divisibility changes the variable n=qdm and gives
\[
\frac{u(q)}{qd}\,F\!\left(\frac{T_j}{qd}\right),\qquad
Xe^{-\eta}<\frac{T_j}{qd}\le X.
\]
For the prefix average F, boundedness gives
F(T_j/(qd))=F(X)+O(η+1/X). This is precisely why a common endpoint can
serve the whole bin.

Try the same comparison with a seed interval centered at x=N² and of
width H=N. If a divisor's ratio to its bin representative is e^δ,
0≤δ≤η, its rescaled seed interval has center e^(-δ)x. The endpoint
comparison now costs
\[
O\!\left(\frac{\eta x+1}{H}\right)
\]
after normalization by the window length, subject to the trivial
boundedness cap. The displayed endpoint argument needs
ηx=o(H), or η=o(1/N), for a vanishing window error.

The proof instead chooses
\[
L=(\log X)^{1/A},\quad
J=\left\lfloor\frac{\log L}{1200W}\right\rfloor,\quad
\eta=e^{-J}\asymp(\log X)^{-c},\quad
c=\frac1{1200WA}.
\tag{6}
\]
Thus ηN tends to infinity. The bin comparison cannot simply be reused on
J_N. Replacing its width by o(1/N) also changes the bin count and the
closing spectral factor K/η; the manuscript's logarithmic gain does not
pay for that refinement.

The second gap is §4's analytic centering input. MRT bounds an integral
over starting points from 0 to Z. Restricting this nonnegative integral
to an interval of length N near Z≈N² supplies its total bound, not a
bound proportional to N. It does not establish the every-center short
average used in a localized centering step.

The residue-comparison lemma is **not** this obstruction. At X=N²,
exp(L^A/2)=N, so J_N satisfies its length requirement for fixed l.
But that lemma handles bounded-depth residue events involving auxiliary
primes at most exp(L)=N^(o(1)). It does not supply the Liouville analytic
average, allow an unrestricted growing modulus, or identify those
auxiliary primes with the power-sized primes in c_N.

These observations locate the failure of an unchanged proof transfer.
Keeping divisor-dependent intervals exactly, introducing a different
binning argument, or proving a new local analytic input could change the
situation; none is supplied here.

## 5. A useful translated graph bound derived from 007

There is a positive transfer at the graph level. This section proves a
consequence of §§13–17; it is **not stated as a main theorem in 007**.
It does not use multiplicativity of the test sequences.

Use the parameters of Part II, which are reset independently of Part I:
ε=10^(-4), η=10^(-6), c_*=10^(-6), and its fixed A. Keep h, τ, C_0,
and T fixed. At auxiliary scale B, let the divisor family, cutoffs,
weights W, mean L_0, and signed kernel g_d satisfy §10. Write
\[
Q_B=\prod_{p\in\mathcal S}p,\qquad
B^{10}H\le D_0<2B^{10}H,
\]
where D_0 is a power of two, and put
\[
P_B=D_0Q_B,\qquad R_B=\lceil\tau hH\rceil.
\]
For sufficiently large B and every consecutive interval I of M positive
integers, every |a_d|≤1, and arbitrary one-bounded F,G,
\[
\left|\sum_{x\in I}\sum_{d\in\mathcal D}
 a_dF(x)G(x+hd)g_d(x,x+hd)\right|
\le C L_0 B^{-1-c_*/2}(M+P_B+R_B+1).
\tag{7}
\]
Here C and the threshold depend only on the fixed parameters, and
**not on the location of I, the test sequences, or the admissible family
and cutoffs**.

Proof. The elementary fact needed is that for any nonnegative
q-periodic sequence z and any translated interval of M integers,
\[
\sum_{n\in I}z(n)\le(M+q)\,\mathbb E_{n\bmod q}z(n).
\tag{8}
\]
Split I into full periods and one partial period; the latter has mass
at most a full period.

In §17 the block matrices have period Q_B in their block index, so
the exceptional-block event on sites has period P_B. The high-trace
estimate and its singular-value Markov bound give exactly the same
exceptional-block density as in that section. Deleted-vertex weights
have period Q_B; boundary-crossing and exceptional-block weights have
period P_B. Their full-period weighted means are the bounds proved
there. Apply (8) to each discarded class rather than taking a prefix
limit. For large B those means are bounded by a fixed multiple of
L_0 B^(-1-c_*/2); the exceptionally small classes are smaller still.
An endpoint incident to a deleted vertex lies in I+[0,R_B], accounting
for the R_B term.

On all remaining blocks the operator norm is at most
B^(-1-c_*/2). Test with the functions supported on I and I+[0,R_B],
respectively, and weighted by sqrt(W). Cauchy in the block index
and (8) for W give
\[
B^{-1-c_*/2}
\sqrt{L_0(M+Q_B)\,L_0(M+R_B+Q_B+1)}
\le L_0B^{-1-c_*/2}(M+R_B+Q_B+1).
\]
Support cutoffs handle the partially occupied first and last blocks.
Adding the three discarded classes proves (7). All comparisons use
positive full-period sums; no new independence of an interval location
and its residue coordinates is assumed.

There is also a legitimate slowly growing choice. Since
log Q_B≪exp(B), H≤exp(C_0B), and h is fixed, taking
\[
B=\tfrac12\log\log M
\]
gives P_B+R_B=M^(o(1))=o(M). Consequently (7) implies, uniformly over
translated intervals and changing bounded test sequences,
\[
\left|\sum_{x\in I}\sum_d a_dF(x)G(x+hd)g_d(x,x+hd)\right|
\ll L_0 M B^{-1-c_*/2}.
\tag{9}
\]
This conclusion retains the **specific centered divisor kernel** and
fixed h, C_0, τ, T. Its label range is at most exp(C_0B), a power of
log M. It does not give a correlation theorem for arbitrary multiplicative
functions in a moving window: the analytic bias-capture and centering
steps still have to be supplied. Nor does (9) permit h to grow without
rechecking the arithmetic arguments.

For our M≈N, this graph is a usable auxiliary input. Its labels and
prime bands do not coincide with the actual outer support of c_N,
whose smallest prime is N^(1/4). Introducing auxiliary small primes is
possible as a new method, but a kernel identity and error estimate are
needed first.

## 6. Coefficient and logarithmic-rate bookkeeping

The actual β_U cannot be substituted for a multiplicative factor in
Theorem 1.2. For distinct primes p,q>U,
\[
\beta_U(p)=\beta_U(q)=\beta_U(pq)=-1,
\]
whereas multiplicativity would require β_U(pq)=1. This witness uses
arguments strictly above U. Also β_5(30)=2, so one-boundedness is not
automatic. Checkpoint 11's uniform dyadic bound
\[
\sum_{M<m\le2M}|\beta_U(m)|^2\ll M
\]
is the appropriate norm input; it is not a multiplicativity assertion.

Likewise, Λ(n)/log n is one on primes and zero on a product of two
distinct primes, so it is not multiplicative. The frozen c_N is a
changing prime-supported coefficient, also not an eligible
multiplicative function. Part II's graph theorem allows arbitrary
bounded test sequences, but only after they have been placed on its
particular additive divisor graph. That is the missing representation
for (1).

The exponent in the printed quantitative construction satisfies
c=1/(1200WA)≤1/12,000,000 because W≥10 and A≥1000. This is a bound on
the exponent chosen by that construction, not a bound on the strongest
mathematically possible theorem. A direct unweighted error
N/(log N)^c with this c is larger than N/log N.

However, that observation alone does **not** reject a weighted route.
By checkpoint 11's logarithmic freezing, define
\[
\gamma_N(d)=c_N(d)\frac{\log N}{\log(N^2/d)},\qquad
0\le\gamma_N(d)\le3/2.
\]
Then
\[
B_N(J_N)=\frac1{\log N}
\sum_d\gamma_N(d)
\sum_{\substack{m>U\\b>V}}\beta_U(m)\Lambda(b)
\mathbf1_{J_N}(dmb)+o(u).
\tag{10}
\]
A bound O(N/(log N)^c) for the **entire actual numerator in (10)**
would therefore imply B_N=o(u) for every c>0. No such numerator bound
is asserted or derived by 007. In particular the Mangoldt factor's size
cannot be silently discarded when applying a one-bounded theorem.
The Type I core would still need its compatible signed estimate.

## 7. The exact nearby-product kernel to investigate next

Formula (10) identifies a concrete interface for an attempted graph
adaptation. Aggregate k=dm and set
\[
\alpha_N(k)=
\sum_{\substack{d\mid k\\k/d>U}}
\gamma_N(d)\beta_U(k/d).
\]
Only k≤(N²+N/2)/(V+1) can contribute, so the relevant vectors are finite.
On an integer dyadic b-block Q<b≤2Q, b>V, put
\[
v_b=\sum_k\alpha_N(k)\mathbf1_{J_N}(kb).
\]
Cauchy yields the exact quadratic form
\[
\left|\sum_{\substack{Q<b\le2Q\\b>V}}\Lambda(b)v_b\right|^2
\le
\left(\sum_{\substack{Q<b\le2Q\\b>V}}\Lambda(b)^2\right)
\sum_{k,l}\alpha_N(k)\overline{\alpha_N(l)}K_{N,Q}(k,l).
\tag{11}
\]
The overlap kernel has an elementary exact expression. With
a=N²-N/2 and z=N²+N/2,
\[
\begin{aligned}
L_{k,l}&=\max\{Q+1,V+1,\lceil a/k\rceil,\lceil a/l\rceil\},\\
U_{k,l}&=\min\{2Q,\lfloor z/k\rfloor,\lfloor z/l\rfloor\},\\
K_{N,Q}(k,l)&=\max(0,U_{k,l}-L_{k,l}+1).
\end{aligned}
\tag{12}
\]
This counts the integer b satisfying both product-window conditions.
Whenever an overlap occurs, |k-l|≤N/b. The diagonal k=l is present;
007's nonproportional affine theorem excludes analogous proportional
pairs and does not estimate this diagonal or the whole quadratic form.

The kernel in (12) is a positive Gram kernel of multiplication-shell
incidences. The kernel in (9) consists of centered divisibility factors
on edges x↦x+hd. They are not the same operator after a change of
notation. A useful adaptation must construct the centering and
identify the resulting errors, retain α_N's actual c_N and β_U factors,
and control the high-outer Type I floor remainder as well. A norm
estimate for unrelated bounded tests is insufficient.

This exact interface is the next research task. It makes the missing
kernel match reviewable rather than leaving “apply Chowla” as an
unspecified step. An estimate for the original joint signed sum in (3)
is also sufficient and can be weaker than separate absolute bounds.

## 8. What the formalization check establishes

The comparator configurations identify actual solution modules:

| Comparator | Solution module |
|---|---|
| OrdinaryTwoPointCorrelations | OAI.NumberTheory.TwoPointCorrelations.FinalMain |
| OrdinaryElliott | OAI.NumberTheory.OrdinaryCorrelations.Elliott.Main |

The first module forwards the three named statements to
OAI.NumberTheory.TwoPoint.Main. That main module instantiates the
conditional stages with the implemented prime-distribution,
Braverman, and MRT inputs. Its final exports have no extra analytic
hypotheses. The checked statement and distance definitions retain the
fixed-form quantifiers, ordinary positive-integer sums, and twist
height equal to the prime cutoff. The second comparator provides
another qualitative export.

The two comparator families use slightly different harmless
conventions at zero: the first bounds positive arguments, while the
second bounds all natural arguments. All correlation arguments are
positive. These definitions should not be conflated when examining
the source.

The occurrences of “sorry” in ComparatorChallenges are the expected
challenge placeholders. They are not evidence that the named solution
modules have missing proofs. Conversely, merely finding theorem
bodies in selected solution files does not certify their whole import
closure. The configurations permit only propext, Quot.sound, and
Classical.choice; this audit has not independently checked the exported
proofs against that permitted-axiom list. Nanoda is disabled in the
published configurations.

The pinned toolchain is Lean 4.34.1. No Lean or Lake executable was
available in this workspace, and no build or comparator success is
claimed. This checkpoint records the source scope without representing
the mathematical and application audit as a kernel replay.

## 9. Exact checks, reproduction, and admission

Run from the campaign directory:

    python3 src/openai007_audit.py

The script checks all bundled source hashes; compares the three final
Lean statement types with their challenge statements at the source
level; checks the exact singleton-center cancellation; supplies explicit
β_U and prime-detector nonmultiplicativity witnesses; and independently
enumerates integer cofactor overlaps to verify (12) and its quadratic
aggregation. It also checks the rational exponent bookkeeping and the
unchanged terminal status. These are finite identity and provenance
checks, not numerical evidence for (3), a substitute for the continuous
proof of (7), or a Lean proof check.

The new audit record is results/openai007_audit.json. The reproducible
checks are results/openai007_checks.json. The source manifest distinguishes
unchanged primary files from extracted text and repository inventories.
The preceding campaign notes, scripts, source files, and numerical
ledgers are preserved.

Admit (5), the random-prime rank lemma of §6, and (7)–(9) as **auxiliary**
tools with their displayed hypotheses. Do not admit a terminal prime
comparison from 007. The next gate remains (3); its higher-degree
companion is also open. No new positive K is credited, and the full
analytic inventory and mass optimization remain incomplete.
