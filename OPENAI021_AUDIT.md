# Audit of 021 for the H(ϑ) campaign

Michael M. Ross's square-shell investigation. Checkpoint 15, 8 October 2026.

**Result.** The critical proof chain of 021 has now been audited. No fatal error was identified in the arguments checked. Its quantitative covering theorem has a useful square-shell consequence: conditional on that theorem, every sufficiently large shell contains at least a constant times N log log N/(log N)^2 integers with at most three prime factors, counted with multiplicity. This does not supply the campaign's prime lower bound or its remaining signed delta estimate.

The source is OpenAI, *A quadratic bound for Jacobsthal's function*, 25 September 2026: the complete 83-page manuscript, its TeX build, and selected actual Lean implementation and comparator files. The pinned repository commit is **adc7f1241b42e322a6451854ab7e4b4c146bf78a**. The PDF has SHA-256 **f80267eebc82a9b8905057b45b35ef8734485b2b0b7b809a3051c06240cf0b1e**. See the [primary manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) and [formalization scope](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/021.md). Original source bytes and URLs are recorded in sources/openai021/manifest.json.

This is an audit of the mathematical mechanisms, quantifiers, arithmetic margins, and applicability. It is narrower than an independent certification of every analytic dependency. The Lean comparator and its transitive axiom check were **not rerun**. The square-shell assertion below is explicitly recorded as a consequence of 021, rather than as a separately established replacement for the campaign's existing prime estimates.

## 1. The full manuscript is stronger than the catalog statement

For a positive modulus q, let j(q) be the least positive length such that every interval of that length contains an integer coprime to q. Put

\[
h(k)=\sup_{q\ge1,\ \omega(q)\le k}j(q).
\]

Theorem 1.1, page 2, asserts that one absolute C>0 satisfies

\[
h(k)\le C\frac{k^2}{(\log\log(3k))^2}\qquad(k\ge1).
\tag{1}
\]

The modulus, its prime factors, and the interval's signed starting point are arbitrary. Prime powers do not affect coprimality. The paper supplies neither an explicit final C nor an effective threshold usable for a finite shell computation. Its Siegel–Walfisz input permits ineffective constants.

The more useful intermediate result is Theorem 1.2, page 4. For sufficiently large z, set

\[
L=\log z,\quad Y=\left\lfloor z^2/L^2\right\rfloor,\quad
w=L/(\log L)^2,\quad B=L/\log w,\quad
V_0=\prod_{p\le w}(1-1/p).
\]

For **every** choice of one forbidden class a_p modulo each prime p≤z,

\[
\#\{1\le j\le Y:j\not\equiv a_p\pmod p\text{ for every }p\le z\}
\ge c\,YV_0/B^2
\asymp Y\log w/L^2
\tag{2}
\]

with an absolute positive lower constant. Classes may depend on z and on the interval. In particular, for a block beginning at any integer A, choosing a_p=1−A modulo p makes the count in (2) exactly the count of integers A+j−1 with no prime divisor at most z. There is no fixed-translation restriction here.

## 2. What was checked in the proof

The positive reference calculation alone does not prove (2) for arbitrary residue classes. The comparison with the actual counts is the substantive additional task. The audit traced both parts through the following chain.

| Stage | Main checks and implication |
|---|---|
| Exact decreasing-prime tree, §3 | Partition by the smallest newly forbidden prime. Alternating lower/upper signs and upper-node omissions give a valid lower expansion. All retained progressions have coordinate length at least w^(1/100). Stops form a prefix-free family of even nodes. |
| Delay functions and renewal process, §4 | Derivative weights are positive and integrate to probability kernels. The change of measure telescopes exactly. Regeneration has exponential moments, positive nonarithmetic decrements, and the stated invariant densities. The compact renewal limit and band bounds retain the dependence between a state and its elapsed decrement. |
| Transfer from harmonic paths to primes, §5 | Harmonic prime errors are uniform at both endpoints. High-ratio histories have negligible original weight. Coupling is supplemented by discrete marginal bounds, so inverse derivative weights in the tail are not controlled by total variation alone. |
| Positive reference margin, §6 | The root benchmark has a negative boundary term. The signed correction integral more than compensates for it. Both the coarse positive margin and the sharper rational certificate were independently checked. The local reference estimate is uniform on each fixed stopping window. |
| Regular independent boxes, §7 | A discrepant compact endpoint has a recent witnessing edge. Singleton bins give the needed independence. The total enlarged box mass is O(B^(−2)), independent of bin width; errors are summed with this mass, not with the growing number of boxes. |
| Inverse and variance alternatives, §§8–9 | Fixed whole-box rational candidates are chosen before failing tuples are selected. Polynomial height, curve-point bounds, and the isolated-prime range are compatible. Both variance branches preserve residue restrictions and give a small-effective-height alternative. |
| Stops and final error budget, §§10–11 | The comparison at stops is an average over complete owner families. Missing prime choices are paid for with an absolute upper sieve. Hard endpoints are covered by marked visits and independent search bins. Parameters are fixed in the stated order before z tends to infinity. |

Several details matter for the uniform conclusion:

* The invariant raw densities are π_e(s)=φ_e(s) for s≥2 and π_o(s)=(1−s^(−2))φ_o(s) for s≥1. The cycle log-decrement mean is M_g/β, with 0<M_g≤4e^γ. This produces the B^(−2) weight scale.
* In the inverse argument, the isolated prime has size R=z^α with α≤1/100. The nonlinear-curve contribution is negligible because its controlling factor is R^4 S_q^(−1/3) times subpower losses, hence z^((13α−2)/3+o(1)). The exponent is negative throughout the stated range.
* Small-prime residue patterns in the variance argument are compared with a dominating measure. The proof does not assume that the actual prescribed classes are random or independent.
* Appendix A keeps multiplicities when an interval is longer than a modulus. The explicit modular-hyperbola error is uniform in prime-power moduli and translated rectangles, and gives R^(3/5+o(1)) in the large-modulus variance range. The gcd factor in the complete Kloosterman bound is retained.
* Lemma 10.4 is uniform over arbitrary subsets of restricted primes. Its lower coefficient e^(−γ)(.94−o(1)) follows from the geometric-product comparison and a uniformly bounded expected logarithmic excess.
* The stopped-family count gains a coefficient greater than .39, whereas the reference coefficient is at most .33. Choosing the permitted missing-prime fraction sufficiently small leaves at least .34. This proves a **grouped** nonnegative correction; it is not a pointwise inequality at each stopped node.

The exact comparison identity has the form

\[
L_{\rm stop}-YV_0P_e(r_0,B)
=\sum_{\rm expanded\ d}(-1)^{\omega(d)}(N_d-\mu_d)
+\sum_{\rm stopped\ d}\bigl(S_d-\mu_dP_e(r_d,b_d)\bigr),
\quad \mu_d=YV_0/d.
\tag{3}
\]

The proof bounds the first sum's absolute cost and proves the second sum nonnegative after its owner-family grouping. The choice order K, error tolerance, regularity constants, inverse-list bounds, variance cutoff, owner tolerance, stopping window, bin width, and finally z avoids using a small-width limit to justify constants already chosen from that limit. These were the principal sign and uniformity risks examined.

### Exact reference and stopping margins

Proposition 6.3 obtains

\[
\frac{B^2P_e(r_0,B)}{e^\gamma}
\longrightarrow-\frac1{100}+\frac{2I}{M_g}>.02.
\]

The coarse calculation is

\[
I>\frac83-1-.66-.52-.34=.146666\ldots>.14,
\quad
-\frac1{100}+\frac{.28}{4(1.95)}=.0258974358\ldots>.02.
\]

The script also proves the stated rational upper bounds on log 2, γ and e^(.66). It reproduces Remark 6.4's stronger lower certificate

\[
I>.2229793730375238\ldots>.222979373.
\]

The displayed decimals are summaries of exact fractions. An alternating-series bound gives f(2.18)<.296515<.30 with the same coarse e^γ bound. The stopped-family coefficient before rounding is

\[
\frac{.94\cdot.95}{2.19+.02}=.4040723981\ldots>.39.
\]

These checks validate the arithmetic margins; they do not replace the renewal limit or the inverse and variance arguments.

## 3. The final deduction of the improved Jacobsthal bound

Pages 72–74 use more than a crude union bound over remaining divisor primes. Write ℓ=log k and M=log log k, and choose

\[
z=A_0k\ell/M,
\quad Y\sim A_0^2k^2/M^2,
\quad X=Y/z\sim A_0k/(\ell M),
\quad \log w\sim M.
\]

Equation (2) leaves at least c_0Y log w/(log z)^2 candidates. For each modulus prime q>z, its progression contains at most 1+X points. The paper encloses those points in a progression segment of coordinate length comparable to X, and applies an upper sieve by primes at most X^θ. Since these primes are below z and q is invertible modulo them, the surviving points divisible by q number at most

\[
C_1(1+X/\log X).
\tag{4}
\]

This extra logarithm is essential. For at most k remaining divisor primes,

\[
\frac{k(1+X/\log X)}{Y\log w/(\log z)^2}
\longrightarrow\frac1{A_0}.
\]

Fixing A_0 sufficiently large leaves a candidate coprime to the whole modulus. The finitely many remaining k are covered by the elementary bound h(k)≤(k+1)2^k+1 and an enlarged absolute C. The enclosing-progression argument also covers q>Y and arbitrary signed translations. The final deduction is consistent with the stronger form (1).

## 4. A quantitative three-factor consequence for the square shells

Keep the campaign's even N, square center x=N^2, and interval

\[
J_N=[N^2-N/2,N^2+N/2]\cap\mathbb Z,
\qquad u=N/(2\log N).
\]

Set a **new auxiliary cutoff**

\[
z_N=\frac14\sqrt N\log N,
\quad L_N=\log z_N,
\quad Y_N=\left\lfloor z_N^2/L_N^2\right\rfloor.
\tag{5}
\]

This does not change the existing campaign cutoff N^(1/4) or its coefficients. For T=log N≥8,

\[
L_N=T/2+\log(T/4),\qquad T/2\le L_N\le5T/8.
\]

The last upper bound follows from log(T/4)≤T/8, whose difference has nonnegative derivative for T≥8 and is positive at T=8. Consequently, once rounding is allowed for,

\[
N/8\le Y_N\le N/4,\qquad Y_N\sim N/4.
\tag{6}
\]

Choose a block of Y_N consecutive integers inside J_N and prescribe its translated divisibility classes as in §1. Theorem 1.2 gives at least

\[
c\,Y_NV_0/B^2
\asymp \frac{N\log\log N}{(\log N)^2}
\tag{7}
\]

integers with least prime factor greater than z_N. Here log w∼log log N and L_N∼(log N)/2.

Four such prime factors, **including repeated factors**, would have product greater than z_N^4. But

\[
z_N^4=\frac{N^2(\log N)^4}{256}
\ge16N^2>N^2+N/2\quad(T\ge8).
\]

Each counted integer is positive, greater than one, and therefore has Ω(n)≤3. We obtain the following precise conditional consequence of 021:

\[
\#\{n\in J_N:P^-(n)>z_N,\ 1\le\Omega(n)\le3\}
\gg \frac{N\log\log N}{(\log N)^2}
\quad\text{for every sufficiently large even }N.
\tag{8}
\]

The constant and the sufficiently-large threshold are unspecified. Equation (8) counts primes, semiprimes and triprimes together, with Ω counting multiplicity. It is not a claim of squarefree support, and no novelty claim is made for the general almost-prime problem.

## 5. Why this does not yet close H(ϑ) or the delta estimate

The guaranteed scale in (8), divided by u, is a constant times

\[
2\log\log N/\log N\longrightarrow0.
\]

This says that the **provided lower-bound scale** is o(u), not that the actual survivor count is o(u). The assertion also leaves all of its survivors free to be composite. If Q_j counts its survivors with Ω=j, then Q_1+Q_2+Q_3 is controlled from below, while Q_1 alone is not. Even a Liouville balance would only separate Q_2 from Q_1+Q_3: primes and triprimes have the same Liouville sign. A quantitative triprime comparison is still required to isolate primes.

For comparison, applying (1) to the product of primes at most the prime-detecting cutoff near N gives

\[
j\!\left(\prod_{p\le N}p\right)
\ll\frac{N^2}{(\log N)^2(\log\log N)^2}.
\]

That upper bound is much longer than J_N. It supplies no prime in this shell through that application.

There is also a concrete failure of the direct node-estimate mapping to the **remaining** campaign rows. Checkpoint 14 already covers Type I through d≤N^(457/400); its remaining gated core C has d>N^(457/400). The progression-coordinate length is then

\[
N/d<N^{-57/400}\longrightarrow0.
\]

The remaining Type II product range has db>N^(459/400), so its coordinate length satisfies

\[
N/(db)<N^{-59/400}\longrightarrow0.
\tag{9}
\]

These lengths fail 021's included-node condition J_d≥w^(1/100), as well as the growing-length hypotheses in its variance estimates. Applying those estimates verbatim to the unresolved floor rows is therefore invalid. This is an exclusion of that direct mapping, not a proof that the method cannot be redesigned.

The coefficient cutoff is a separate issue. At the auxiliary shell scale, 021 has w of order log N/(log log N)^2. The campaign instead retains U=V=floor(N^(1/100)) and its actual truncated divisor weight β_U. Those power-sized divisor parameters are not covered automatically by 021's small-prime patterns and fixed-logarithmic-power progression moduli. Replacing U by w would change the campaign's coefficient rather than estimate it.

The unchanged campaign interface is

\[
\Delta_2+\Delta_3
=B_{D_{\rm good},\,db>N^{459/400}}(J_N)
+A_C(J_N)-(M_C+o(1))u,
\tag{10}
\]

with

\[
M_C\in[.08849546268050629,.08853207940856963].
\]

Equation (2) does not bound (10)'s actual weighted β_U covariance or its gated prime-cofactor count. In particular, it does not prove the optional upper allowance (.011+o(1))u. No positive prime coefficient K is credited; the separate higher-degree cap and H(ϑ) remain open.

## 6. Formalization evidence and reproducible checks

The actual solution module lean/OAI/NumberTheory/Jacobsthal/Main.lean imports both QuadraticBound and IteratedLogBound. The exported improved theorem is OAI.Erdos970.Erdos970Final.erdos_970_iterated_log. It obtains the uniform source-root survivor lower bound and passes it to the improved terminal-budget deduction. The comparator target quantifies over all positive moduli with at most k distinct prime factors and all signed integer starts. Both configurations permit only propext, Quot.sound and Classical.choice.

The two ComparatorChallenges files contain intended target placeholders using `sorry`; they are not the actual proof implementations. The selected actual implementation files have no `sorry` or newly declared `axiom` in their bodies. This source scan is **not** a transitive axiom check. Neither Lean nor Lake is installed in the current environment, and no kernel/comparator replay was performed. Fourteen Lean source/documentation records are included as reading evidence, not as a complete buildable checkout.

The exact-check script is src/openai021_audit.py. Run it from the campaign directory:

```bash
python3 src/openai021_audit.py
```

It verifies the rational reference and stopping margins; 4,710 arbitrary-class CRT rows; 637 signed-translation rows; and 504 restricted modular-hyperbola decomposition cases. Of the latter, 360 retain intervals longer than a modulus and all 504 exercise negative translations. These cases check the exact arithmetic decomposition and multiplicities, not the analytic Weil estimate. The shell inequalities in (6)–(9) are recorded alongside the consequence and its limitations.

All **32 primary-source records** and **156 unchanged historical checkpoint-14 records** pass size and SHA-256 verification. The original analytic ledger, numerical reference enclosures and source certificates are preserved. PDF pages 4, 34, 65 and 72–74 were rendered and inspected against the extracted text and TeX.

## 7. What to investigate next

The critical manuscript audit is complete at the stated scope; independent Lean replay is a separate pending verification. The next mathematical transfer is to place any new stops **before** the progression lengths in (9) fall below one, retain the campaign's actual β_U and prime-pair ordering weights, and determine whether grouped corrections can control the residual expression (10). A weighted analogue of the stopped-family comparison would be a substantive new lemma; the unweighted covering estimate is not that lemma.

For the auxiliary three-factor route, the first required additional estimate is a uniform comparison of the actual Q_3 contribution in J_N. Such a comparison must come with a sufficiently strong survivor lower bound to produce a positive multiple of u. Merely subtracting a triprime bound from (7)'s smaller guaranteed scale cannot supply that multiple. The square-shell geometry and factor-ray identities may organize these prime/triprime rows, but an actual arithmetic estimate remains necessary.
