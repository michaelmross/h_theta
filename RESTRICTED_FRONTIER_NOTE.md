# Restricted frontier: prime products on the actual square shell

Checkpoint 9 investigation — 6 October 2026

The restricted wave count admits a pointwise reduction to factorially weighted products of two through seven actual primes. Repeated large prime factors cost \(O(N^{3/4})=o(u)\) on the actual shell. The long comparator has an additional nonnegative eight-factor boundary correction. This reduction and the finite checks are complete. The uniform centered prime-product estimate remains unproved, so \(H(\vartheta)\) remains open and the certified campaign value is \(K=0\).

## 1. Target and notation

Let \(N\) be even, \(x=N^2\), and
\[
J=[N^2-N/2,N^2+N/2]\cap\mathbb Z,\qquad
Y=N+1,\qquad u=\frac{N}{2\log N}.
\]
Set \(z=N^{1/4}\), \(w=N^{0.95}\), and
\[
Y_1=x\exp\{-3(\log x)^{1/3}\},\qquad
B=[x-Y_1/2,x+Y_1/2]\cap\mathbb Z.
\]
Write
\[
R(W)=\#\{m\in W:z\le P^-(m)<w\}.
\]
This is the least-prime-oriented frontier in ROSS_GEOMETRY_AUDIT, equivalently \(\sum_{z\le p<w}S_p(p)\). Its unresolved one-sided target is
\[
R(J)-\frac{Y}{Y_1}R(B)\le(0.338+o(1))u. \tag{1}
\]
The previously admitted ledger makes (1) sufficient for its conditional positive prime coefficient. That implication is not a proof of (1), of the full campaign hypothesis, or of a positive certified \(K\).

For \(j\ge3\), define
\[
M_j(W)=\frac1{j!}\sum_{\substack{p_1,\ldots,p_j\ge z\\p_i\ {\rm prime}}}
 {\bf1}_W(p_1\cdots p_j).
\]
For \(j=2\), retain the frontier cutoff:
\[
M_2(W)=\frac12
 \sum_{\substack{p,q\ge z\ {\rm prime}\\\min(p,q)<w}}{\bf1}_W(pq),
\qquad
\mathcal K(W)=\sum_{j=2}^{7}M_j(W). \tag{2}
\]
The symbol \(\mathcal K\) is this counting kernel, not the campaign's certified constant \(K\).

On either window, the minimum-prime restriction is automatic for \(j\ge3\): three primes at least \(w\) already have product \(N^{2.85}>2x\), for sufficiently large \(N\). Thus the kernel uses ordinary prime indicators with independent cutoffs; no nested cofactor roughness condition remains.

## 2. A uniform repeated-prime bound

For any positive integer interval \(W=[A,B_0]\cap\mathbb Z\), \(H=B_0-A+1\), and \(z\ge1\), let \(E(W;z)\) count integers divisible by \(p^2\) for some prime \(p\ge z\). Then
\[
E(W;z)\le\frac{4H}{\lceil z\rceil}+\frac{10}{3}B_0^{1/3}. \tag{3}
\]

Proof. Enlarge the prime square divisors to all integers \(d\ge\lceil z\rceil\), and split them into dyadic blocks \(D\le d<2D\). Counting multiples of each \(d^2\) gives at most
\[
H/D+D
\]
pairs \(m=qd^2\) in a block. Counting \(q\le B_0/D^2\) first gives at most
\[
\sum_{q\le B_0/D^2}
 \left(\frac{B_0-A}{(\sqrt{B_0}+\sqrt A)\sqrt q}+1\right)
 \le 2H/D+B_0/D^2.
\]
Consequently each block contributes at most
\[
2H/D+\min(D,B_0/D^2).
\]
The first term sums to at most \(4H/\lceil z\rceil\). Blocks below \(B_0^{1/3}\) contribute at most \(2B_0^{1/3}\), and the remaining geometric series contributes at most \((4/3)B_0^{1/3}\). This proves (3).

Applied to \(J\), (3) is \(O(N^{3/4})\), uniformly in every even \(N\), and
\[
O(N^{3/4})/u=O(N^{-1/4}\log N)\longrightarrow0.
\]
Applied to \(B\) and multiplied by \(Y/Y_1\), the repeated-prime correction is also \(O(N^{3/4})\). This is a bound on the actual arithmetic support, stronger than the extracted mass axioms alone.

## 3. Seven factors on the actual shell; eight on the comparator

For every even \(N\ge18\), a \(z\)-rough integer in \(J\) satisfies
\[
\Omega(m)\le7. \tag{4}
\]
Indeed, nine factors give \(m\ge z^9=N^{9/4}>N^2+N/2\). Eight factors with at least two distinct odd primes give
\[
m\ge z^7(z+2)=N^2+2N^{7/4}>N^2+N/2.
\]
The remaining case is \(m=p^8\), an odd square. The only square in \(J\) is the even square \(N^2\), so that case is impossible. Here \(\Omega\) counts factors with multiplicity.

A row \(m=\prod_p p^{e_p}\) with \(\Omega(m)=j\) has coefficient
\[
\frac1{\prod_p e_p!}
\]
in \(M_j\). This equals one for squarefree rows and lies in \((0,1]\) otherwise. Equations (3)–(4) therefore give
\[
R(J)=\mathcal K(J)+E_J,\qquad 0\le E_J=O(N^{3/4}). \tag{5}
\]

The long comparator need not satisfy (4). Put \(\epsilon_1=Y_1/(2x)\). Eight rough factors in \(B\) force every prime factor into
\[
[z,z(1+\epsilon_1)].
\]
The number of such rows is at most \((z\epsilon_1+1)^8\). Since \(z\epsilon_1\to\infty\), their normalized contribution is
\[
\frac{Y}{Y_1}O(x\epsilon_1^8)=O(N\epsilon_1^7)=o(u).
\]
This is a subpower estimate; it is not being claimed to be \(O(N^{3/4})\). For sufficiently large \(N\), nine rough factors exceed the upper endpoint of \(B\). Together with the repeated-prime estimate,
\[
R(B)=\mathcal K(B)+E_B,\qquad E_B\ge0,\qquad
\frac{Y}{Y_1}E_B=o(u). \tag{6}
\]

The useful one-sided identity is especially clean:
\[
R(J)-\frac{Y}{Y_1}R(B)
\le
\mathcal K(J)-\frac{Y}{Y_1}\mathcal K(B)+O(N^{3/4}). \tag{7}
\]
The comparator correction is subtracted and nonnegative. An asymptotic equality with error \(o(u)\) follows from (5)–(6). Thus proving (1) reduces to the same centered estimate for the explicit kernel (2).

## 4. Reference masses and the remaining budget

The long-window prime-product calculation gives
\[
\frac{Y}{Y_1}M_j(B)=(c_j+o(1))u.
\]
For the unrestricted product components, define factorial convolutions
\[
g_j(s)=\frac1{j!}
 \int_{\substack{t_i\ge1\\t_1+\cdots+t_j=s}}
 \frac{dt_1\cdots dt_{j-1}}{t_1\cdots t_j}.
\]
Then \(g_1(s)=1/s\) for \(s\ge1\), \(g_j(s)=0\) for \(s<j\), and
\[
s g_j(s)=\int_{j-1}^{s-1}g_{j-1}(v)\,dv,\qquad c_j=8g_j(8).
\]
The factorial normalization is essential. In particular \(g_2(s)=\log(s-1)/s\).

The semiprime frontier coefficient is exactly
\[
c_2=\log7-\log(21/19)=1.8458266904983307686\ldots.
\]
The following displayed intervals are widened outward from the 20,000-cell interval calculation:

| Component | Reference coefficient \(c_j\) |
| --- | --- |
| Two primes, with frontier cutoff | \(1.8458266904983307686\ldots\) |
| Three primes | \([1.2191073676093,\ 1.2191484689775]\) |
| Four primes | \([0.2993157331037,\ 0.2993465713008]\) |
| Five primes | \([0.0267063438926,\ 0.0267127637637]\) |
| Six primes | \([0.0005960323611,\ 0.0005963594200]\) |
| Seven primes | \([0.0000008988625,\ 0.0000009002567]\) |

In particular,
\[
C_{\ge4}:=\sum_{j=4}^{7}c_j
\in[0.3266190082200,\ 0.3266565947410]. \tag{8}
\]
The independently computed total overlaps the frozen ordinary-root and frontier enclosures. Those earlier ledger values have not been replaced.

Write \(\Delta_j=M_j(J)-(Y/Y_1)M_j(B)\). The actual remaining target is
\[
\Delta_2+\Delta_3+\sum_{j=4}^{7}\Delta_j
 \le(0.338+o(1))u. \tag{9}
\]
Two- and three-prime products account for over 90 percent of the reference frontier. A possible sufficient allocation would be
\[
\Delta_2+\Delta_3\le(0.011+o(1))u,\qquad
\sum_{j=4}^{7}M_j(J)\le(2C_{\ge4}+o(1))u. \tag{10}
\]
It would give an upper excess below \(0.337656595u\). Both estimates are unproved. In particular, (8) is a reference mass, not an upper bound on the actual short shell. The existing marked three-prime subterm overlaps \(M_3\), so it cannot be credited independently.

## 5. What survives of the wave geometry and parity checksum

On these components, Liouville's function has the exact sign
\[
\lambda(p_1\cdots p_j)=(-1)^j.
\]
The signed frontier therefore has kernel
\[
M_2+\sum_{j=3}^{7}(-1)^jM_j,
\]
with the same small actual repeated-prime error. This retains the useful checksum from ROSS_GEOMETRY_AUDIT.

A change of wave parameter \(r\), including a nonnegative weighted average of \(r\)'s whose per-pair weights sum to one, leaves each represented product and its Liouville sign unchanged. It cannot algebraically introduce parity cancellation. This does not exclude a new analytic estimate using moving waves.

More concretely, if the selected least prime is \(p>N^{2/3+\delta}\), the rough cofactor must itself be prime, for all sufficiently large \(N\). All those selected rows have Liouville sign \(+1\). Cancellation on a complete wave does not by itself control this density-restricted subset.

The earlier long-support parity witness remains scoped to the extracted mass-only interface. Its excess decomposes here as
\[
c_2-c_3+c_4-c_5+c_6-c_7
 \in[0.8998763229655,\ 0.8999550108545],
\]
compatible with the previous witness. It is not a counterexample on \(J\) and does not satisfy every stronger arithmetic or error hypothesis. Nor does this argument deny the force of a complete signed Möbius remainder estimate.

## 6. A sharp centered Mellin formulation

The remaining task can be specified without arbitrary cofactor coefficients or an unspecified short interval.

Round \(Y_1\) to the odd integer
\[
H_1=2\lfloor Y_1/2\rfloor+1.
\]
The corresponding endpoints \(x\pm H_1/2\) are half-integers, as are \(x\pm Y/2\). Replacing the comparator and the normalization by this rounded window changes the centered kernel count by \(O(Y/Y_1)=o(u)\), since its row coefficients lie in \([0,1]\).

For \(h=Y,H_1\), put
\[
\widehat W_h(s)=
 \frac{(x+h/2)^s-(x-h/2)^s}{s},\qquad
D(s)=\widehat W_Y(s)-\frac{Y}{H_1}\widehat W_{H_1}(s).
\]
Using primes only up to \(2x\), the global Dirichlet polynomial is
\[
F(s)=\frac{P_z(s)^2-P_w(s)^2}{2!}
     +\sum_{j=3}^{7}\frac{P_z(s)^j}{j!},
\qquad P_a(s)=\sum_{a\le p\le2x}p^{-s}. \tag{11}
\]
For estimates, expand (11) into dyadic prime boxes whose product ranges meet either window. Include every such box, including boundary boxes. All other boxes have zero contribution to the exact window counts. There are \(O(\log^7x)\) retained boxes in total. For each fixed degree \(j\), its polynomial satisfies
\[
|F_{\rm box}(1/2+it)|\ll_j\sqrt x,
\]
because the product support is comparable with \(x\) and each integer's ordered factorization multiplicity is bounded by \(j!\).

Truncated Perron at \(T=x^2\) represents a box difference by
\[
\frac1{2\pi}\int_{-T}^{T}
 F_{\rm box}(1/2+it)D(1/2+it)\,dt
 +O_j(\log x/x). \tag{12}
\]
The error follows by summing \(O_j(x/(T|m-v|))\) at each half-integer endpoint \(v\); \(|m-v|\ge1/2\) and the reciprocal distances have a harmonic sum. Summed over the boxes, this error is \(o(u)\).

Centering gives a second-order cancellation. Indeed,
\[
\frac{\widehat W_h(s)}h
 =\int_{-1/2}^{1/2}(x+ha)^{s-1}\,da,
\]
so the term linear in \(h\) integrates to zero. Taylor's formula yields
\[
|D(1/2+it)|
 \ll \frac{Y}{\sqrt x}(1+|t|)^2(H_1/x)^2.
\]
With \(T_0=\exp\{(\log x)^{1/3}\}\), the integral for \(|t|\le T_0\) is therefore
\[
O_j\!\left(Y(H_1/x)^2T_0^3\right)
 =O_j\!\left(Y e^{-3(\log x)^{1/3}}\right).
\]
Even after the box count, this is \(o(u)\).

Consequently the unresolved estimate is the centered high-frequency integral in (12), summed over the actual prime boxes, for
\[
T_0<|t|\le x^2.
\]
An upper bound \((0.338+o(1))u\) is enough. The stronger per-box estimate \(O(Y\log^{-A}x)\), \(A>8\), would imply \(o(u)\), but is not necessary. The relevant sign is the centered window difference, not an inserted Liouville sign. Frequencies above the natural sharp-window scale \(x/Y\) have not been discarded. The centering phase, boundary boxes, and actual prime coefficients must remain in the next argument.

## 7. A scoped obstruction to one published four-factor criterion

The primary source is [Li, *The number of primes in short intervals and numerical calculations for Harman's sieve*, Lemma 4.2](https://arxiv.org/html/2308.04458v8). Use \(\eta\) for its interval exponent, to distinguish it from the campaign's roughness parameter.

Our calculation from the four printed cases gives the following necessary inequalities for any four grouped exponents with sum one:

| Printed case | Necessary total lower bound | Necessary \(\eta\) |
| --- | --- | --- |
| 1 | \(1\ge(57/28)(1-\eta)\) | \(\eta\ge29/57\) |
| 2 | \(1\ge(133/66)(1-\eta)\) | \(\eta\ge67/133\) |
| 3 | \(1\ge(61/30)(1-\eta)\) | \(\eta\ge31/61\) |
| 4 | \(1\ge(27/13)(1-\eta)\) | \(\eta\ge14/27\) |

For case 3, the last two restrictions imply \(\alpha_3+\alpha_4\ge7(1-\eta)/10\); add the bounds for the first two groups. The other rows follow by addition.

At \(\eta=1/2\), these require respectively \(1\ge57/56,\ 133/132,\ 61/60,\ 27/26\). Every case is empty, regardless of grouping. The fixed gaps survive the \(o(1)\) perturbations in a dyadic setup. This is a certificate for those four printed cases only; it excludes neither other estimates nor a square-centered refinement.

## 8. Exact finite checks

The new script factors both the actual and rounded reference windows, counts each degree, and tracks the factorial kernel with exact rational weights. Prime cutoffs are tested by integer powers: \(p^4\ge N\) and \(p^{20}<N^{19}\). Comparator lengths and normalized excesses use outward interval arithmetic.

Seventeen sampled even values were checked:
\[
5000,\ 10000,\ 11000,\ 12000,\ 13000,\ 14000,\ 14640,\ 15000,\ 
16000,\ 17000,\ 18000,\ 19000,\ 20000,\ 28560,\ 50000,\ 83520,\ 100000.
\]
All the exact centered identities
\[
\Delta R=\Delta\mathcal K+E_J-(Y/H_1)E_B
\]
passed. Each band also passed its Liouville-signed kernel/correction identity. Independent small fixtures at \(N=20,40,80,120\) compared direct prime-tuple enumeration with integer factorization and checked the large-square bound by direct enumeration.

| \(N\) | \(H_1\) | \(R(J)\) | \(R(B_{H_1})\) | Centered excess divided by \(u\), approximately |
| --- | ---: | ---: | ---: | ---: |
| 5,000 | 11,107 | 822 | 1,817 | 0.013232 |
| 14,640 | 69,717 | 2,511 | 11,956 | 0.000218 |
| 18,000 | 99,525 | 2,759 | 15,036 | 0.042950 |
| 28,560 | 221,099 | 4,405 | 34,005 | 0.008853 |
| 83,520 | 1,433,487 | 11,968 | 205,482 | -0.001153 |
| 100,000 | 1,965,103 | 13,310 | 260,855 | 0.008174 |

The maximum sampled excess has interval upper endpoint below \(0.042950401210810687\), at \(N=18{,}000\), below \(0.338\). Reference eight-factor rows occur at \(N=14{,}640,\ 28{,}560,\ 83{,}520\), containing \(11^8,\ 13^8,\ 17^8\), respectively. They provide a concrete check that the long correction cannot simply be omitted. These samples do not establish any uniform asymptotic estimate.

## 9. Reproduction and the next proof task

Run from the project directory:

    python3 src/restricted_frontier.py

The script writes:

- results/restricted_frontier_reduction.json
- results/frontier_prime_product_mass.json
- results/frontier_four_factor_certificate.json
- results/frontier_centered_experiments.json

The default reference computation uses 20,000 cells. To regenerate the reduction, masses, and four-factor certificate while retaining the previously computed experiments:

    python3 src/restricted_frontier.py --skip-experiments

The next task is a uniform estimate for \(\Delta_2+\Delta_3\), with a genuine bound for the higher-degree remainder, or a joint estimate for the complete kernel. Equation (10) gives one concrete sufficient allocation, not a required decomposition.

Start with the exact semiprime expression. With integer endpoints \(L=N^2-N/2\), \(U=N^2+N/2\), for sufficiently large even \(N\),
\[
M_2(J)=\sum_{\substack{z\le p<w\\p\ {\rm prime}}}
\left[\pi(U/p)-\pi((L-1)/p)\right]. \tag{13}
\]
Here \(\pi(t)\) counts primes at most the real number \(t\). Because \(p<w<\sqrt L\), the cofactor is always greater than \(p\), so (13) counts each row once and has no repeated-prime correction.

Form the analogous long-window expression, subtract it with the exact normalization, and split the actual \(p\)-ranges into dyadic blocks. The target is a prime-weighted average of short prime intervals, retaining the square-centered congruence \(m-N^2\equiv-N^2\pmod p\). A pointwise prime-count estimate in each cofactor interval would be unnecessarily strong. A proposed averaged estimate must supply the fixed-center quantifier, actual prime coefficients, normalization, and adequate aggregate error. Introduce the three-prime polynomial on the same centered comparison; a small joint excess can use cancellation between its window discrepancy and the semiprime discrepancy without requiring equally strong separate bounds.

Moving-wave geometry is useful if it supplies such an arithmetic estimate while preserving the actual prime coefficients and boundary contributions. A regrouping identity, reference-volume calculation, or larger finite sample alone cannot discharge (9).

No new terminal estimate is admitted in this checkpoint. The previously frozen numerical ledger, source texts, and earlier hypothesis distinctions remain in force.
