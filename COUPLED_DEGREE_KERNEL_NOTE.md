# A direct lower weight for the coupled degree pool

Checkpoint 30 — Michael M. Ross's H(ϑ) campaign — 12 October 2026

**A new weight passes the pointwise and reference tests. Its required
centered lower comparison remains unproved.**

The weight uses a threefold von Mangoldt convolution to enforce the
roughness and residual degree conditions together. A fixed fifth-degree
polynomial makes it close to the four-prime indicator in the test band.
There is no separate subtraction of prime or semiprime cofactors.

The proved reference loss is at most (.000001+o(1))u. An admitted rough
upper sieve also bounds its short-count deficit by (.000033+o(1))u.
These are bounds for the difference between the actual pool and the
new weight; they do not assert that either count has its long mean on
the short window.

The remaining comparison is explicit: bound the actual centered weight
below by −η_W u, keeping η_W+η_rest≤.000099. The usual Robert–Sargos
mapping that eliminates one free factor and retains one other free
factor fails throughout this band, even in the all-Type-I term. A
comparison using more of the multilinear structure remains open.

The original .007935/.011 targets remain open, K=0, and milestone 7
remains deferred.

## 1. Actual target and unchanged notation

Keep x=N², Y=N+1, u=N/(2 log N), even N, z=N^(1/4), y=N^(19/20),
κ=1/1000, the original H_1, a_N=Y/H_1 and ρ=H_1/x=N^(-o(1)).
The original prime-product marks and their half-weighted diagonal are
unchanged. Write

\[
d_N(n)=\mathbf1_{P^-(n)\ge z}(1-\min\{1,q_N(n)\}).
\]

This continuation concerns the actual test pool in checkpoint 29, (21):

\[
G_N(n)=\sum_{N^{2/5}\le p\le N^{43/100}\atop p\ {\rm prime},\ p\mid n}
 \mathbf1_{P^-(n/p)\ge p,\ \Omega(n/p)\ge3},
\qquad \mathcal G_N(\psi)=\sum_nG_N(n)\psi(n).
\tag{1}
\]

Its positive rows select the smallest prime exactly once and have degree
at least four. Thus 0≤G_N≤d_N. Let

\[
\Delta\mathcal G_N=\mathcal G_N(\psi_Y)
 -a_N\mathcal G_N(\psi_{H_1}).
\tag{2}
\]

The original full positive complement also contains the exact y-rough
base and the degree pool outside this band, up to the inherited
nonnegative repeated-three-prime correction. They are retained in the
remaining comparison; no original signed least-prime sector is dropped.

The preserved ordinary long reference of (1), denoted M_G, satisfies

\[
a_N\mathcal G_N(\psi_{H_1})=(M_G+o(1))u,
\quad
M_G\in[.0098070333321849229383,\ .0100071597526122167744].
\tag{3}
\]

This interval is used through its upper endpoint for loss bounds.
The centered comparison continues to use the actual normalized long
count, so its enclosure width is not discarded as an o(u) error.

## 2. A convolution with automatic rough degree support

For a prime p set λ_p(1)=0 and

\[
\lambda_p(v)=\Lambda(v)\mathbf1_{P^-(v)\ge p}\quad(v>1),
\qquad C_{3,p}=\lambda_p*\lambda_p*\lambda_p,
\tag{4}
\]

where * is Dirichlet convolution. This is the convolution of three
von Mangoldt functions with a prime-base cutoff, not μ*log³.
For m>1 define

\[
\nu_p(m)=\frac9{2}\frac{C_{3,p}(m)}{(\log m)^3},
\qquad \nu_p(1)=0.
\tag{5}
\]

**Lemma 1.** For every p and m,

\[
0\le\nu_p(m)\le1,\qquad
\nu_p(m)>0\Longrightarrow P^-(m)\ge p,\ \Omega(m)\ge3.
\tag{6}
\]

Proof. Each convolution factor is a prime power with base at least p.
Three factors therefore give the stated support. If m has a prime
below p, the convolution is zero; if it has more than three distinct
prime factors, it is also zero.

Suppose first m has three distinct prime bases r,s,t, with positive
exponents A,B,C. The only possible assignment places one base in each
factor, giving C_3=6 log r log s log t. Since
log m=A log r+B log s+C log t≥log r+log s+log t, AM–GM gives ν≤1.

If m=r^A s^B with two bases, write L=log m, x=log r/L and y=log s/L.
Counting positive exponent compositions gives

\[
C_3=3\log r\log s\{(A-1)\log r+(B-1)\log s\},
\quad
\nu=\frac{27}{2}xy(1-x-y)\le\frac12.
\]

The last bound follows from AM–GM for x,y,1−x−y, which are nonnegative.
It also includes the zero degree-two case.

For m=r^A, the number of ordered positive compositions of A into three
parts is binomial(A−1,2), or zero for A<3. For A≥3,

\[
\nu=\frac94\frac{(A-1)(A-2)}{A^3}
\le\frac9{4A}\le\frac34.
\]

This covers all cases, including repetitions. □

## 3. Fixed polynomial correction and pointwise lower weight

For a fixed positive integer k let Φ_k(v)=1−(1−v)^k. Choose k=5:

\[
\Phi_5(v)=5v-10v^2+10v^3-5v^4+v^5.
\]

By Lemma 1, 0≤Φ_5(ν_p(m))≤1, and it vanishes whenever the joint
rough-degree condition fails. Define

\[
w_N(n)=\sum_{N^{2/5}\le p\le N^{43/100}\atop p\ {\rm prime},\ p\mid n}
 \Phi_5(\nu_p(n/p)),\qquad
\mathcal W_N(\psi)=\sum_nw_N(n)\psi(n).
\tag{7}
\]

A nonzero row has p equal to the smallest prime of n. There is only
one such prime divisor in the outer sum, even when it repeats. Hence

\[
\boxed{0\le w_N(n)\le G_N(n)\le d_N(n).}
\tag{8}
\]

This is a global arithmetic inequality. The polynomial is applied to
a convolution whose range was proved; no factorability or comparison
property is inferred merely from nonlinear clipping.

On a squarefree four-prime row n=prst, with p the smallest prime,

\[
\nu_p(rst)=\frac{27\log r\log s\log t}{(\log(rst))^3}.
\tag{9}
\]

At product x, let α=log_N p∈[2/5,43/100] and b,c,d be the other
exponents. They satisfy b,c,d≥α and b+c+d=2−α. Concavity of
log b+log c+log d shows that its minimum on this simplex occurs at a
vertex. Thus bcd≥α²(2−3α). The function

\[
\frac{27\alpha^2(2-3\alpha)}{(2-\alpha)^3}
\]

is increasing on this band: its logarithmic derivative has numerator
8(1−2α)>0 over a positive denominator. Therefore

\[
\nu\ge\frac{27}{32},\qquad
1-\Phi_5(\nu)\le\left(\frac5{32}\right)^5
=\frac{3125}{33554432}=:\epsilon_5.
\tag{10}
\]

For n in either original window, log_N n=2+o(1); the same compact
geometry gives (10) with an o(1) perturbation. The perturbation is
uniform and contributes o(u) after the count bounds below. The lift
order is fixed; no growing polynomial degree is used.

## 4. Exceptional rows and an admitted upper bound

The uniform estimates in this section justify applying (10) to the
dominant actual rows, rather than assuming squarefreeness.

A repeated prime base b≥N^(2/5) in a contributing near-x integer obeys
b²≤(x+O(H_1))/N^(2/5), so b≪N^(4/5). Summing multiples of b² gives
on the short padding

\[
O(N^{3/5}+N^{4/5})=o(u).
\]

On the normalized long window the analogous envelope is
O(N^(3/5)+N^(−1/5)ρ^(-1))=o(u). Kernel weights are bounded by one,
so this absolute envelope applies to their deficits.

There cannot be six prime factors in this band near x. A possible
degree-five row has all its prime factors in a relative O(ρ) interval
about N^(2/5). The inherited ordinary long PNT bounds its normalized
mass by O(Nρ^4/(log N)^5)=o(u). On the short padding that real interval
has width O(N^(−3/5))<1, so a degree-five row repeats a prime and is
already in the preceding envelope. Thus squarefree four-prime rows
give the full main of the deficit on both windows.

For the short bound retain the actual rough count

\[
\mathcal R_N(\psi_Y)=
\sum_{N^{2/5}\le p\le N^{43/100}\atop p\ {\rm prime}}
 \sum_{P^-(m)\ge p}\psi_Y(pm).
\tag{11}
\]

It contains the actual degree pool. In each fixed p-box [P,2P), use
the ordinary upper sieve with sifting cutoff P and full level
D_P=N^(1249/1000)/(2P). Since P≤p, the sieve majorizes (11).
The actual bounded outer coefficient is the prime indicator, not a
free prime slot. With B=1249/1000 its limiting exponents satisfy

\[
\gamma=\alpha\in[.40,.43],\quad
\beta=B-\alpha,\quad
\gamma+\beta=B<5/4,\quad 2\gamma+\beta<2.
\]

The inherited WF transfer is admitted, with full level, exact squarefree
sifting support and fixed reserve 1/1000. The smallest older RS margin
is .321. The ratio s=β/α lies in [819/430,849/400]⊂(1,3).

The primary sieve formulation is
[Lichtman, arXiv:2109.02851v2, Theorem 2.10 and (2.5)](https://arxiv.org/html/2109.02851v2).
Its upper branch has sF(s)=2e^(γ_0) here. Retain its Cε term while
using the fixed-margin remainder, take the limsup in even N, then
ε→0. This is the same fixed-parameter limiting argument as checkpoint
27; it is not an application with an N-dependent source tolerance.

Prime reciprocal partial summation gives

\[
\mathcal R_N(\psi_Y)\le(U_B+o(1))u,
\quad U_B=(1+\kappa)\frac4B
\log\frac{b(B-a)}{a(B-b)},\quad a=.40,\ b=.43.
\tag{12}
\]

Outward arithmetic certifies
U_B∈[.3471707279485729919135,.3471707279485729919136], hence U_B<.348.
This upper estimate controls the defect; it does not give a lower
comparison for the degree pool.

## 5. Proved reference loss and short deficit

Put \(\mathcal E_N=\mathcal G_N-\mathcal W_N\), a nonnegative count.
Equations (3), (10) and the exceptional-row envelopes give

\[
0\le a_N\mathcal E_N(\psi_{H_1})
\le(\epsilon_5M_G+o(1))u
\le(.000001+o(1))u.
\tag{13}
\]

The certified product upper endpoint is
.0000009319893785391204780251<.000001. It bounds the defect from above;
it is not an asserted lower coefficient for the actual loss.

Similarly, the admitted actual upper estimate (12) proves

\[
0\le\mathcal E_N(\psi_Y)
\le(\epsilon_5U_B+o(1))u
\le(.000033+o(1))u,
\tag{14}
\]

with product upper endpoint .0000323327936184194862762032.

| Fixed lift order k | Reference-defect envelope | Short-defect envelope |
|---|---:|---:|
| 3 | <.000038175u | <.001324352u |
| 4 | <.000005965u | <.000206930u |
| 5 | <.000000932u | <.000032333u |

The fifth degree is the first to pass .0001u using this uniform
short-defect envelope. This is not a claim that lower degrees cannot
pass a sharper average estimate. Degree three already passes the
reference test; degree five supplies the stronger two-window control.

Writing ΔW=W(ψ_Y)−a_NW(ψ_H1), the exact difference is
ΔG−ΔW=E(ψ_Y)−a_NE(ψ_H1). Therefore the new uniform comparison is

\[
\boxed{-(.000001+o(1))u
\le\Delta\mathcal G_N-\Delta\mathcal W_N
\le(.000033+o(1))u.}
\tag{15}
\]

This compares the two actual centered counts; it does not determine
the sign or size of ΔW itself.

Nonnegativity gives the coarse actual bound
ΔW≥−(.010008+o(1))u, using (3). It does not meet the required .000099
combined comparison/rest allowance.

In the required one-sided direction, if

\[
\Delta\mathcal W_N\ge-(\eta_W+o(1))u,
\tag{16}
\]

then ΔG≥−(η_W+.000001+o(1))u. Only the normalized reference loss is
charged in this forward lower transfer: the short defect has a positive
sign. Its .000033 bound is retained in (15), not charged a second time.

## 6. The actual coefficient family in the centered comparison

The pointwise polynomial construction does not make a prime-supported
sequence a WF divisibility weight. The source must be tested on the
actual four-factor product sum.

Up to the negligible repeated rows, (9) gives the ordered-prime
representation with a factor 1/6. Freeze log(n/p) at log(x/p) only in
this comparison representation. The per-row change is
O(|log(n/x)|/log N); there are at most a fixed number of ordered prime
representations per integer. The short and normalized long errors are
o(u) by the trivial window count. No slowly decaying ρ is multiplied
by an N^ε bound in this freezing step.

Let c_j=(-1)^(j+1) binomial(5,j). Define

\[
\begin{aligned}
T_j(\psi)=\sum_{N^{.40}\le v_1\le N^{.43}\atop
                         v_2,v_3,v_4\ge v_1}
 &\frac{\Lambda(v_1)}{\log v_1}
 \frac{\prod_{i=2}^4\Lambda(v_i)(\log v_i)^{j-1}}
      {(\log(x/v_1))^{3j}}\,
 \psi(v_1v_2v_3v_4).
\end{aligned}
\tag{17}
\]

All v_i in (17) are integer variables. Replacing the actual prime
detectors by Λ(v)/log v adds proper prime powers. Each added power
value lies between N^(.40) and O(N^(.80)) on the physical support.
Their reciprocal sum is O(N^(−.20)(log N)^C), and their number is
O(N^(.40)(log N)^C). Summing their multiples, with the fixed divisor
order of the four-factor representation, gives O(N^(.80+ε))=o(u) on
the short window for sufficiently small fixed ε. The normalized long
bound is likewise o(u). This padding is applied to the complete count,
before expanding its detectors; no prime mask remains on an expanded
free variable.

Thus on both windows, in their respective normalizations,

\[
\mathcal W_N(\psi)=\frac16\sum_{j=1}^5c_j27^jT_j(\psi)+o(u).
\tag{18}
\]

Use the complete auxiliary Vaughan identity at U=floor(N^(1/1000)):

\[
\begin{aligned}
I_1(v)&=\sum_{d\mid v,\ d\le U}\mu(d)\log(v/d),\\
I_2(v)&=-\sum_{db\mid v,\ d,b\le U}\mu(d)\Lambda(b),\\
II(v)&=\sum_{mb=v,\ m>U,\ b>U}\beta_U(m)\Lambda(b),
\quad \beta_U(m)=-\sum_{d\mid m,\ d\le U}\mu(d),\\
\Lambda(v)&=I_1(v)+I_2(v)+II(v)\quad(v>U).
\end{aligned}
\tag{19}
\]

Every physical variable is ≥N^(.40)>U. Expand all four detectors in
(17), keeping its exact gates and smooth logarithmic weights. There
are 81 signed terms per logarithmic moment and five moments: 405 terms
in all. Equivalently there are 16 grouped Type-I/Type-II patterns per
moment. Their cancellations on composite integer slots are essential.

The requested lower comparison is now the actual coupled estimate

\[
\frac16\sum_{j=1}^5c_j27^j
\sum_{\boldsymbol\sigma\in\{I_1,I_2,II\}^4}
\{T_{j,\boldsymbol\sigma}(\psi_Y)
 -a_NT_{j,\boldsymbol\sigma}(\psi_{H_1})\}
\ge-(\eta_W+o(1))u.
\tag{20}
\]

No Type-II term, or all-Type-I lattice error, is removed from (20).
The formal expansion proves the identity, not the lower estimate.

## 7. Continuous source obstruction for the usual two-free reduction

The tested source is the direct fractional-part Lemma 9 following
[Robert–Sargos (2006), Theorem 3, printed pages 14 and 17](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf).
The source's standalone integer sum is unweighted, with an interval
maximum; smooth logarithms are handled by Abel summation. With free
standalone exponent A, denominator-product exponent Σ, and phase size
N^(2−Σ), its error exponents are

\[
\frac{\Sigma+1}{2}-\frac A4,\qquad
\Sigma-\frac A2,\qquad 2\Sigma-2.
\tag{21}
\]

The first two require A>2Σ−2 for a strict saving relative to N.

Even take all four detector terms to be Type I. Their small products
have exponents h_i∈[0,.002]. Sort the physical factor exponents as
a≤b≤c≤d, with a∈[.40,.43] and a+b+c+d=2. Eliminate one original
free factor with physical exponent L and small-product exponent h_e;
retain a different original factor with exponent R and small-product
h_s as the source's free standalone variable. Then

\[
\Sigma=2-L+h_e,\quad A=R-h_s,\quad
A-2\Sigma+2=R+2L-2-h_s-2h_e.
\tag{22}
\]

For every choice of the distinct slots,

\[
R+2L-2\le c+2d-2
=2-2a-2b-c\le2-5a\le0.
\tag{23}
\]

Hence the first two exponents in (21) are at least one. The endpoint
a=b=c=.40,d=.80 gives only equality even with h_e=h_s=0. Small Type-I
products can only worsen the first margin. The mapping supplies no
strict power-saving region anywhere in the limiting band.

| Physical quartet vertex | Best optimistic first margin |
|---|---:|
| (.40,.40,.40,.80) | 0 |
| (.40,.40,.60,.60) | −.20 |
| (.40,8/15,8/15,8/15) | −.40 |
| (.43,.43,.43,.71) | −.15 |
| (.43,.43,.57,.57) | −.29 |
| (.43,157/300,157/300,157/300) | −.43 |

All six vertices, all 12 ordered elimination/standalone choices, and
all four small-product corners are checked: 288 rational rows. The
continuous inequality (23), not finite sampling, proves the failure.

Collapsing two free factors into a product does not give a unit-weight
standalone integer variable: its factorization coefficient and gates
remain. A method exploiting those two variables together would be a
different mapping. This audit does not exclude such a method, a
three-free-variable estimate, or a direct estimate for the whole signed
comparison (20).

There is a second checked mapping: apply Theorem 3 separately at each
external Fourier frequency, using the three remaining free factors as
its parameter C and two inner variables M,N. At the required top
height Q/Y, the phase has N-exponent χ=1, or larger with a fixed
frequency reserve. Put S_f=M_f+N_f+C_f for their free-length exponents.
The first two source terms have error exponents

\[
E_1=\frac{3S_f+\chi-N_f}{4},\qquad
E_2=\frac{3S_f+\chi-M_f}{4}.
\tag{23a}
\]

With small-product exponents at most .002, S_f≥3a−.006 and
C_f≥a−.002. Since min(M_f,N_f)≤(S_f−C_f)/2,

\[
\max(E_1,E_2)\ge\frac{5S_f+C_f+2\chi}{8}
\ge\frac{16a-.032+2}{8}\ge\frac{523}{500}>1.
\tag{23b}
\]

Thus this separate-per-frequency three-free use of Theorem 3 also
fails to supply a saving, even before summing the small-product rows.
All 576 parameter/elimination/small-product cases are checked. This
does not rule out estimating frequency and the product variables
jointly, or another four-variable lattice method.

## 8. What is proved, what is needed next, and the coefficient ledger

| Requirement | Result |
|---|---|
| Joint roughness and degree support | Exact, including repeated prime powers |
| Pointwise lower weight for the actual band pool | Proved |
| Normalized reference loss | ≤(.000001+o(1))u; passes the budget |
| Actual short deficit | ≤(.000033+o(1))u, using an admitted upper sieve |
| Comparison between the two centered actual counts | (15), with both coefficients retained |
| Required actual centered lower bound for W | Unproved; (16)/(20) is the remaining input; coarse lower coefficient −.010008 is proved |
| Standard one-free-after-elimination RS mapping | Fails continuously, including all-Type-I |
| Per-frequency three-free Theorem 3 mapping | Fails continuously; first-two-error maximum ≥523/500 |
| Qualifying source-complete weight for the entire complement | Not supplied |

The next analytic input is precisely (20), with

\[
\eta_W+\eta_{\rm rest}\le .000099,
\tag{24}
\]

where η_rest controls the exact base and all other degree-pool bands.
The kernel loss .000001 is charged inside the original .0001
complement budget. A band estimate alone is insufficient for the full
original comparison.

A concrete first separate source task is the all-four-Type-I lattice
remainder in (20), comparing its four free integer sum with the same
continuous product integral, with h_i≤N^(.002), the actual physical
gates and smooth logarithmic weights retained. The two-free bound
does not prove this remainder o(u). A source using the additional free
variables, or a whole coupled comparison that controls it with the
other signed patterns, is required. A separate-per-frequency use of
Theorem 3 is insufficient by (23b). No successful source is asserted here.

The sufficient original spectral budget is still

\[
.007825257+.000001+\eta_W+\eta_{\rm rest}
 +\xi+21147/L\le .007935.
\tag{25}
\]

The final original coefficient includes the smoothing charge .003065
and every term in (25). Any ξ from discarding an original fixed-power
least-prime sector must be retained using checkpoint 22, (23); a fixed
complete-transform multiplier retains 21147/L. This construction
discards neither sector. Its conditional kernel charge .000001 remains
explicit; the original .011 allowance is unchanged.

## 9. Verification and preserved status

Run `python3 src/coupled_degree_kernel.py`.

The exact convolution checks cover 3,108 formal factor/cutoff rows,
including repeated bases and the polynomial identity. They are exact
algebra checks, with positive rational substitutions for formal log
variables. The actual arithmetic checks evaluate the new kernel's
literal prime logarithms outward on 451,078 original-padding sites.
They retain the original cutoffs and canonical half-diagonal marks,
and give positive kernel weight to all 20 old-box rows found there.

Seventy-two four-slot formal Vaughan fixtures, 70 with composite
slots, verify recombination of all 81 signed terms. The five common
logarithmic moment weights give the retained 405-term interface.
The second RS mapping has 576 additional exact cases, for 864 source
corners in total. Outward coefficient arithmetic verifies both defect charges and the
admitted upper-band constant. These fixtures do not prove (16) or (20).

All 291 nonmutable checkpoint-29 records, the old reference enclosures,
and the frozen historical mass ledger are unchanged. H(ϑ), the sharp
.007935/.011 comparison, the exact base/rest comparisons and the
optional marked estimate remain open. K=0; milestone 7 remains deferred.
