# Ross geometry papers in the H(ϑ) campaign — checkpoint 8

Michael M. Ross's investigation. 6 October 2026.

Both supplied papers are now incorporated, including their original ZIPs, unchanged TeX and figures. They supply exact offset, factor-wave and parity identities, and a global model correction that transfers to the campaign's centered interval. None supplies the uniform restricted-frontier estimate needed to close the current signed argument. The certified lower coefficient remains **K=0**, and **H(ϑ) remains unproved**.

The principal new bridge is an exact expression for the negative first frontier in the papers' wave coordinates. It identifies the required prime and rough-cofactor weights, their asymptotic position in wave tails, and the centered comparison to be estimated. The second bridge is a Liouville checksum on the actual short interval, with a necessary qualification about the twisted divisor errors.

## 1. Sources, parameters and admission decisions

The audit uses the supplied source bytes, rather than searching for another revision:

| Supplied paper | Preserved source | Relevant source labels |
|---|---|---|
| Multiplication Geometry in Square Shells: Finite Coverage, Truncated Legendre Sums, and the Parity Barrier | sources/ross_square_shells/main.tex | lem:A-Sn; prop:A-Delta; eq:good-tautology; eq:twisted-divisor; eq:twist-exact; sec:reciprocal; sec:typeII |
| Factor Rays and the Self-Conjugate Parabola: Deterministic Coverage Geometry in Square Intervals | sources/ross_factor_rays/main.tex | prop:waves; eq:weighted-wave; eq:wave-liouville; prop:single-class; prop:medium-prime; rem:rigidity; sec:wave-comp |

The full supplied TeX texts were read. Source hashes and independent finite checks are recorded in results/ross_geometry_audit.json. The ZIPs contain TeX and figures, but not the large-scan programs or the complete-wave FFT program/CSV referenced in the papers. Their large computations have not been reproduced here.

| Quantity | Paper convention | Campaign convention |
|---|---|---|
| Shell variable | Square-shell paper: n, with x=n² | N even, x=N² |
| Centered band | Factor-ray paper: J_n=[4n²−n,4n²+n] | N=2n gives J_N=[N²−N/2,N²+N/2] exactly |
| Window size | Square-shell Y counts odd positions | Y=N+1 counts all integer positions; Y_o counts odd positions |
| Interval exponent | The paper's provisional θ has Y=x^θ | Our interval has exponent 1/2 in x |
| Roughness exponent | Separate from the interval exponent | b=1/4, κ=19/20 in N; the corresponding x-exponents are 1/8 and 19/40 |
| H | The square-shell H(n) is an actual prime count | H(ϑ) is the campaign's proposed asymptotic hypothesis |

Thus the paper's 4/9 benchmark is not a value of the campaign parameter ϑ.
The paper's collision depths count all relevant odd trial-division primes. The campaign's depth at most eight counts extracted primes at least N^(1/4); these are different decompositions.

| Input | Admission here |
|---|---|
| Coverage, radical, Bonferroni and shifted-majorant identities | Exact bookkeeping; no extra prime mass |
| Product-truncated reciprocal model and its first correction | Global analytic model; centered transfer proved below |
| Quadratic entry offsets | Exact, with a translation at our left edge |
| Composite/weighted waves | Exact, after retaining least-prime orientation and roughness |
| Liouville checksum | Exact on our actual interval; the twist's additional errors remain explicit |
| Complete-wave covariance samples | Finite evidence; no restricted-frontier comparison |
| KRW/Vaaler exponent ledger | Provisional in the supplied paper; no new theorem admitted |
| Generic Type I–II discussion | A useful diagnostic; it is not a proved reduction for our coefficient family |

The existing admitted sieve estimates and all checkpoint 7 numerical enclosures are unchanged.

## 2. The correct quadratic offsets in the centered interval

Write

$$
A=N^2-\frac N2,\qquad B=N^2+\frac N2,\qquad J_N=[A,B]\cap\mathbb Z.
$$

In center coordinates t=m−N², divisibility by d means

$$
t\equiv-N^2\pmod d.
\tag{1}
$$

This is the negative-square class in the factor-ray paper. In left-edge coordinates j=m−A, however, the entry offset is r_d≡−A, represented in [0,d−1]. For every odd d,

$$
16r_d\equiv1-(4N-1)^2\pmod d,
\tag{2}
$$

because 16A=(4N−1)²−1. At an odd prime p this gives the translated set

$$
r_p\in16^{-1}-\{v^2:v\in\mathbb F_p\}.
\tag{3}
$$

The left edge is not a square, so directly copying the unshifted negative-QR entry formula would be incorrect. Multiplication by the square 16^{-1} leaves the square-value set unchanged.

As even N runs through a complete period 2p, N mod p and 4N−1 mod p each run through every class once. The center offset 0 has one preimage and each nonzero negative-square value has two. At the left edge, 16^{-1} has one preimage and each other admissible value has two. CRT gives the product of these multiplicities for any fixed odd squarefree modulus.

In particular, any admissible vector on a fixed finite prime set is realized by some even N modulo twice its product. The one-parameter description alone does not prevent coordinate choices at a fixed set of primes. Its potentially useful restriction is the relation between the size of N and the growing prime set needed at that N. Averaging through a full CRT period does not give a pointwise result at every center.

For a fixed center displacement t, the exact number of solutions N mod p to p|(N²+t) is

$$
1+\chi_p(-t),
\tag{4}
$$

with χ_p(0)=0. This identifies a concrete character structure for a future center-averaged investigation. It does not replace the campaign's all-even-N quantifier.

For each fixed N the divisor count remains

$$
A_d(J_N)=
\begin{cases}
1+\lfloor(N-r_d)/d\rfloor,&r_d\le N,\\
0,&r_d>N.
\end{cases}
\tag{5}
$$

Consequently |A_d(J_N)−Y/d|<1. The QR restriction constrains the phase of this error; it does not multiply the local density Y/d by a factor of one-half.

Two further geometric consequences have a small scale. The sole square in J_N is the even row N², so the odd candidate rows contain no fixed point of divisor conjugation. Also,

$$
N^2-a^2=(N-a)(N+a),\qquad
1\le a\le\sqrt{N/2},
\tag{6}
$$

gives deterministic composite rows in the lower half. There are only O(√N)=o(u) such rows, where u=N/(2 log N). These particular rows cannot change a leading coefficient measured in units of u. Absence of odd squares does not determine the parity of Ω(m).

## 3. Transfer of the full-depth model and its correction

Let P_N^o be the product of the odd primes at most N. Every odd composite in J_N has a prime factor at most N, since √B<N+1. Put

$$
T_N(B)=\sum_{\substack{d\le B\\d\mid P_N^o}}\frac{\mu(d)}d,
\qquad
\Pi_N=\#\{p\text{ prime}:p\in J_N\}.
$$

With Y_o the number of odd positions and A_d^o their divisor count, full inclusion–exclusion gives

$$
\Pi_N=Y_oT_N(B)+
\sum_{\substack{d\le B\\d\mid P_N^o}}
\mu(d)\left(A_d^o(J_N)-\frac{Y_o}{d}\right).
\tag{7}
$$

This is the exact centered counterpart of eq:good-tautology. The last sum contains the unknown prime count through this equality; the identity alone does not estimate it.

The square-shell paper's reciprocal model at shell index N has upper cutoff (N+1)². The two models differ only in the O(N) integers between B and (N+1)². Each reciprocal term has absolute value at most 1/B, hence

$$
\left|T_N(B)-S_N^{\rm shell}\right|=O(N^{-1}).
\tag{8}
$$

Their logarithmic cutoffs also differ by O(N^{-1}). The supplied paper's global expansion, with β₁=γ+log 2 and γ here Euler's constant, therefore transfers:

$$
T_N(B)=\frac2{\log B}
\left(1+\frac{\gamma+\log2}{\log B}
+O((\log B)^{-2})\right)+O(N^{-1}).
\tag{9}
$$

Since Y_o=Y/2+O(1), this yields

$$
Y_oT_N(B)
=u\left(1+\frac{\gamma+\log2}{2\log N}
+O((\log N)^{-2})\right)+O(1).
\tag{10}
$$

This is a global-model bridge to our actual interval shape. Its first correction is O(u/log N)=o(u). It cannot supply a fixed leading improvement to the 0.338u frontier-excess target. A bound on the signed remainder in (7) would be a new local arithmetic input.

The paper itself distinguishes the model correction from shell-prime fluctuations and the finite-depth sawtooth tail in prop:A-Delta. Its q=1 localization formula explicitly contains the shell prime count. Neither a cumulative signed shell average nor the large finite certificate scans supplies the campaign's pointwise centered comparison.

## 4. Exact wave coordinates for the actual negative frontier

Retain the campaign's definition

$$
\mathcal R_\kappa(W)
=\sum_{\substack{p\ {\rm prime}\\N^{1/4}\le p<N^\kappa}}
\ \sum_{\substack{q:\ pq\in W\\P^-(q)\ge p}}1.
\tag{11}
$$

The relevant windows lie near N², so for large N the cofactor is nonunit and q≥p. Every row counted here is marked exactly once by its least prime p. Prime powers are retained.

For each fixed integer wave weight r≥1 define

$$
F_r(W;N)=
\sum_S\ \sum_{\substack{p\ {\rm prime}\\N^{1/4}\le p<N^\kappa}}
\mathbf1_{\{q=S-rp\ge p\}}\,
\mathbf1_{\{P^-(q)\ge p\}}\,
\mathbf1_W(pq).
\tag{12}
$$

Then, by the unique assignment S=q+rp,

$$
F_r(W;N)=\mathcal R_\kappa(W).
\tag{13}
$$

The geometric identity is exactly the paper's weighted-wave discriminant:

$$
S^2-4rpq=(q-rp)^2.
\tag{14}
$$

Three coefficient and counting restrictions matter:

1. The p coordinate is an actual prime, not an unrestricted divisor.
2. The cofactor condition P^-(q)≥p depends on p; it is retained as a joint restriction.
3. Only the least-prime orientation is counted. Summing every factor pair, its conjugate, or several r values would change the multiplicity.

The paper's ordinary unweighted row statistic ⌊(τ(m)−1)/2⌋ is consequently a different count. On J_10000 its total over all integer rows is 88,009, whereas the actual first frontier is 1,686.

### Which part of a wave is relevant?

On J_N, put ρ=rp/q=rp²/m. Since p<N^κ,

$$
0<\rho\le
\frac{rN^{2\kappa-2}}{1-1/(2N)}.
\tag{15}
$$

For every fixed κ<1 and fixed r, ρ→0 uniformly over the selected pairs. Thus

$$
\frac{|q-rp|}{q+rp}\longrightarrow1,\qquad
\frac{S^2/(4r)}{pq}=\frac{(1+\rho)^2}{4\rho}\longrightarrow\infty.
\tag{16}
$$

The campaign's pairs asymptotically lie in wave tails, far below their crests. A balanced crest requires q≈rp, hence r≈N²/p². At p near N^.95 this means r of order N^.1; at p≈N^γ it means r of order N^(2−2γ). A study with a changing r would need estimates uniform in that range.

This limiting distinction can develop slowly. For r=8 and N=10,000 some selected pairs still have rp/q>1; the finite checks record the actual ratios. No claim that all finite samples already resemble the asymptotic tails is needed.

The paper's complete-wave λ and λ_odd covariance averages have unrestricted factor coordinates and point-count weighting across whole waves. They do not estimate (12), its prime restriction, its roughness condition, or its centered window comparison. Cancellation of a complete-wave sum does not in itself bound a selected subset.

### The concrete wave estimate that would advance the campaign

Fix κ=19/20 and let B_N be the existing ordinary centered comparator of length

$$
Y_1=N^2\exp\!\left(-3(\log(N^2))^{1/3}\right).
$$

For any one fixed r, the sufficient checkpoint 7 target becomes

$$
F_r(J_N;N)-\frac{Y}{Y_1}F_r(B_N;N)
\le (0.338+o(1))u
\tag{17}
$$

for every sufficiently large even N. All windows, prime cutoffs and cofactor weights in (12) remain part of this target. Equation (17) is exactly the old frontier comparison in new coordinates, rather than an extra assumption or a stronger arbitrary-coefficient demand.

An estimate of this restricted tail sum would give the previously recorded conditional prime coefficient >0.0065583. No such estimate is proved in the supplied papers or here. Even its proof would supply a positive prime coefficient, not the full H(ϑ) asymptotic.

The factor-ray paper's sparse post-parabola range (√A,N+1] does not resolve (17). Its only possible prime is N+1, hitting N²−1. The frontier's extracted prime is below N^κ<N, while its cofactor is asymptotically above N. Counting the sparse near-N range therefore does not estimate these selected pairs.

## 5. An actual-interval Liouville checksum, with the error qualification

For z≤N define P(z)=∏_{p<z}p and

$$
\Phi_z(m)=\sum_{\substack{d\mid m\\d\mid P(z)}}\mu(d)
=\mathbf1_{\{P^-(m)\ge z\}}.
$$

Complete multiplicativity gives the exact identity

$$
L_z(J_N):=\sum_{m\in J_N}\lambda(m)\Phi_z(m)
=\sum_{d\mid P(z)}\mu(d)^2
\sum_{q:\ dq\in J_N}\lambda(q).
\tag{18}
$$

This formula uses the actual interval. For z>2 all surviving rows are odd, so one may equivalently perform the divisor sum on odd rows with odd d.

At z=N, every surviving row is prime, because N is even and all possible composite least primes are <N. Thus

$$
L_N(J_N)=-\Pi_N.
\tag{19}
$$

For each fixed 2/3<κ<1 and sufficiently large N, the N^κ-rough rows have at most two prime factors. If T_κ counts their semiprimes, with repetitions allowed, then

$$
S_1(N^\kappa)=\Pi_N+T_\kappa,\qquad
L_{N^\kappa}(J_N)=T_\kappa-\Pi_N,
$$

and therefore

$$
\Pi_N=\frac{S_1(N^\kappa)-L_{N^\kappa}(J_N)}2.
\tag{20}
$$

This is a parity-sensitive diagnostic. It does not claim cancellation of L_z; indeed the negative prime contribution is precisely part of it.

The nonnegative twist a_m^+=(1+λ(m))1_J(m) has no prime mass, but its divisor sums satisfy

$$
A_d^+(J_N)-\frac Yd
=\left(A_d(J_N)-\frac Yd\right)
+\lambda(d)\sum_{q:\ dq\in J_N}\lambda(q).
\tag{21}
$$

There is an analogous formula with Y_o and odd rows. The extra sum need not be small. For N=40, the odd-row d=1 untwisted remainder is 0, while the twisted remainder is −8. Thus this actual-support twist does not automatically preserve the individual floor bound, the o(u) remainder axioms, or the stronger power-saving error.

The papers' claim that the twist preserves “one-weight structure” is correct at the level of the algebraic form (21). It must not be read as verifying those quantitative hypotheses. The exact full detector still cancels, since its added term is −Π_N by (19). This is an excellent check that a proposed reduction has retained the complementary-factor correction; it is not a new actual-support countermodel to all the campaign's admitted estimates.

There is a further scope qualification. If the complete signed remainder in (7), including the large-divisor/small-cofactor end, were o(u), then (10) would immediately prove Π_N∼u. More modest one-sided control could already prove a positive prime coefficient. Thus the twist does not refute a sufficiently strong full-range signed estimate merely because its notation has a Möbius weight on one variable. The obstruction concerns the quantitative interfaces actually retained, and the unestimated complementary correction. A universal assertion that every such “one-weight” form is incapable of detecting primes would go beyond this exact stress test.

Checkpoint 7's long-carrier witness remains a separate, proved limitation of the extracted mass interface, with its recorded support and error limitations unchanged.

As a concrete check, at N=10,000:

$$
S_1(N^{.95})=600,\quad T_{.95}=52,\quad
L_{N^{.95}}=-496,\quad \Pi_N=548.
$$

The full checksum is −548. Its signed divisor ranges d≤N, N<d≤N^(5/4), and d>N^(5/4) contribute −72, −65, and −411 respectively. This is one finite observation of where the correction is stored, not a uniform distribution law.

## 6. What is established and what to investigate next

The original-source calibration is retained: the reciprocal KRW/Vaaler calculation is expressly provisional in the supplied square-shell paper. At our window exponent 1/2 its displayed generic inequality would read δ<7/12 in x, or divisor exponent <7/6 in N. Without the complete reduction, Fourier truncation, coefficients and endpoint treatment, this is an exponent diagnostic and adds no admitted region.

The factor-ray paper's offset-blind limitation has also been checked against the primary [Ford–Green–Konyagin–Maynard–Tao paper](https://ford126.web.illinois.edu/wwwpapers/primegaps2.pdf), §1.1, (1.1)–(1.2). Its covering length is j(P(y))−1 and grows faster than every fixed multiple of y. This supports the stated failure for arbitrary entry offsets. It does not establish a covering at the actual square-generated offsets, or prove that their QR restrictions are insufficient.

The useful next investigation is now specified:

- Work with the prime-anchored sum (12), retaining the p-dependent roughness and center.
- Seek a bound for its short-minus-long restricted tail sum (17); if wave weights vary to approach crests, state and prove the required uniformity in r.
- Use (18)–(21) to check every new divisor or wave reduction for an omitted Liouville correction.
- If pursuing the QR phase directly, distinguish estimates averaged over centers from the all-even-N bound required here.

This does not require arbitrary-coefficient Type II as a logically necessary input. A bound for this actual coefficient family, or another signed arithmetic comparison that closes the ledger, could suffice.

## 7. Reproduction and preserved results

Run:

    python3 src/ross_geometry_audit.py

The standard-library script independently factors nine actual bands at N=20,40,80,120,200,400,1000,2000,10000. All cutoffs use exact integer powers. It checks the first-frontier identity against prime/cofactor enumeration, the wave representations at r=1,2,8, translated QR multiplicities and CRT, exact floor counts, the square and difference-of-squares rows, the actual-support Liouville sums, and the twist correction. For the first four bands it also checks (7) with exact rational model and remainder sums, plus the cutoff bound (8).

| N | Primes | Base rough rows | R_.95 | N^.95-rough rows | Rough semiprimes |
|---:|---:|---:|---:|---:|---:|
| 40 | 7 | 20 | 12 | 8 | 1 |
| 400 | 31 | 133 | 100 | 33 | 2 |
| 1,000 | 71 | 266 | 189 | 77 | 6 |
| 2,000 | 131 | 534 | 379 | 155 | 24 |
| 10,000 | 548 | 2,286 | 1,686 | 600 | 52 |

These are finite identity checks, not asymptotic estimates. Their general algebraic justifications are given above.

Checkpoint 1–7 notes, supplied originals, prior scripts and numerical results are preserved byte-for-byte. New files are this note, the two source archives and their contents, the exact-check script, and results/ross_geometry_audit.json. Current indexes identify checkpoint 8. The 0.338u target, admitted root/tail estimates, regional third-frontier improvement, certified K=0 and unproved H status are unchanged.
