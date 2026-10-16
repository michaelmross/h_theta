# H(ϑ) campaign — frontier investigation, checkpoint 7

Michael M. Ross's square-root interval project. 6 October 2026.

The broader coefficient range from checkpoint 6 **reduces the cost of a negative Buchstab branch**. For the third frontier restricted to outer product at most $N^{19/20}$, the new upper coefficient is enclosed in $[0.0960834,0.0977512]$, compared with $[0.1847951,0.1888265]$ using the earlier arbitrary-outer level. The directly enclosed reduction exceeds $0.0887117u$.

This is a regional improvement. It does not improve the already smaller whole-first-frontier cap, prove the aggregate target, or supply terminal prime mass. The extension creates no positive lower-sieve region at the existing base cutoff. An accounting identity also shows why recovering a parent estimate through these child bounds must not be credited again.

Direct applications of the remaining 1989 bounds do not supply the missing comparison. An internal statement/proof discrepancy in Theorem 5 requires particular care. A focused check of adjacent recent literature likewise found no applicable stated every-center comparison.

A sufficient arithmetic input is now a one-sided **centered excess bound of $0.338u$** for the actual first frontier. It would give a prime lower coefficient exceeding $0.0065583$ using the admitted root and smaller-prime tail. That input remains unproved; it would establish a positive prime lower bound, not the full $H(\vartheta)$ main term. No further interval or coefficient information is needed from the user. The missing item is an estimate for the interval and coefficients already specified.

## 1. Setup and the sign restriction

Retain

$$
x=N^2,\quad N=2n,\quad
J_N=[N^2-N/2,N^2+N/2]\cap\mathbb Z,\quad
Y=N+1,\quad u=\frac{N}{2\log N},\quad b=\frac14.
$$

Write $S_d(N^c)=\sum_r1_{J_N}(dr)1_{P^-(r)\ge N^c}$, with $P^-(1)=\infty$. The actual first frontier is

$$
R_\kappa(J_N)=\sum_{N^{1/4}\le p<N^\kappa}S_p(p),
\qquad S_1(N^\kappa)=S_1(N^{1/4})-R_\kappa(J_N).
\tag{1}
$$

For a fixed outer-product exponent $\sigma<1$, checkpoint 6 admits arbitrary bounded outer coefficients with cofactor level

$$
\beta<\frac54-\sigma,
\tag{2}
$$

with fixed margins, full-level well-factorable weights and exact sifting support. The arbitrary-coefficient endpoint $\sigma=1$ remains unadmitted. The earlier level was

$$
\beta<\min\left(\frac54-\sigma,2-2\sigma\right).
\tag{3}
$$

The extension differs only for $\sigma>3/4$. Positive lower-sieve mass with residual cutoff $N^c$ requires $\beta>2c$. Every branch at the existing base cutoff has $c\ge1/4$, so

$$
\beta>2c\ge\frac12,\quad \beta<\frac54-\sigma
\quad\Longrightarrow\quad \sigma<\frac34.
\tag{4}
$$

The extension therefore supplies no new positive lower-sieve region at any depth of this expansion. It can improve negative-branch upper estimates. A different base cutoff or a new arithmetic comparison is outside this conclusion.

## 2. A negative-branch improvement

The third Buchstab identity has signs

$$
S_1(z)=A_0-A_1+A_2-R_3,\qquad
R_3=\sum_{w\le p_3<p_2<p_1<z}S_{p_1p_2p_3}(p_3),
\tag{5}
$$

where $w=N^{1/4}$ and $z=N^\kappa$. Consider the exact subterm

$$
R_{3,\le .95}=
\sum_{\substack{w\le p_3<p_2<p_1<z\\p_1p_2p_3\le N^{19/20}}}
S_{p_1p_2p_3}(p_3).
\tag{6}
$$

Take $\kappa=19/20$ or $97/100$. Its upper prime cutoff is inactive in the limiting exponent region: every outer prime exponent is at most $19/20-2b=9/20$. The three distinct primes have a unique ordered representation, so their product has a bounded outer coefficient.

For $\sigma=\log_N(p_1p_2p_3)\in[3/4,19/20]$, choose $\beta=5/4-\sigma-\varepsilon$ and a slightly smaller sifting cutoff $z'=N^{\beta/2-\varepsilon'}$. Since $z'<p_3$,

$$
S_{p_1p_2p_3}(p_3)\le S_{p_1p_2p_3}(z').
$$

The upper linear sieve with $s=\log D/\log z'$ just above 2 has aggregate upper main term

$$
\frac{2Y}{d\beta\log N}
=\frac{4+o(1)}{d\beta}u.
\tag{7}
$$

This is an aggregate remainder estimate, not a pointwise small-error assertion for each $d$. Freeze $\sigma,\beta,z'$ on finitely many exponent boxes; apply checkpoint 6's proposition to the bounded product coefficients; retain full-level factorability and combined squarefree support. Sum the boxes, then let the mesh and fixed level losses tend to zero after $N\to\infty$. The maximum exponent $19/20<1$ leaves a fixed outer margin. The lower endpoint $3/4$ is covered by the earlier range with fixed slack. The common cutoff $z'$ is below every outer prime, so no small-prime sieve factor overlaps the outer factors.

The reciprocal density of three ordered primes of total exponent $\sigma$ is

$$
\rho_3(\sigma)=\frac13
\int_{1/4}^{\sigma-1/2}
\frac{\log(4(\sigma-v)-1)}{v(\sigma-v)}\,dv.
\tag{8}
$$

The unordered simplex has symmetry factor $1/3!$; integrating the other two prime exponents gives $2\log((\sigma-v-b)/b)/(\sigma-v)$. Equal-prime diagonals have vanishing reciprocal main-term mass. They are absent from the strict outer chain; repeated prime factors in the residual are still retained.

PNT partial summation in the outer variables gives upper coefficients

$$
B_{\rm old}=\int_{3/4}^{19/20}\frac{4\rho_3(\sigma)}{2-2\sigma}\,d\sigma,
\qquad
B_{\rm new}=\int_{3/4}^{19/20}\frac{4\rho_3(\sigma)}{5/4-\sigma}\,d\sigma.
\tag{9}
$$

The directly enclosed positive difference uses

$$
\frac1{2-2\sigma}-\frac1{5/4-\sigma}
=\frac{\sigma-3/4}{(2-2\sigma)(5/4-\sigma)}.
\tag{10}
$$

With 384 interval cells per coordinate:

| Quantity | Lower endpoint | Upper endpoint |
|---|---:|---:|
| $B_{\rm old}$ | 0.18479512859 | 0.18882643909 |
| $B_{\rm new}$ | 0.09608342456 | 0.09775111895 |
| $B_{\rm old}-B_{\rm new}$ | 0.08871170403 | 0.09107532015 |

Displayed endpoints are rounded outward. Thus $R_{3,\le .95}\le(B_{\rm new}+o(1))u$, with a negative-branch upper-cost reduction exceeding $0.0887117u$.

This reduction cannot be subtracted from an unrelated whole-first-frontier cap. Products above $N^{19/20}$ and the remaining terms in (5) still need their own bounds. No full adaptive ledger is closed.

There is a further accounting check. Take a parent product of two primes with $1/2\le\sigma_2<3/4$, so its base lower-sieve main term is positive. Put $\beta=5/4-\sigma_2\in(1/2,3/4]$ and raise its rough cutoff from $b$ to $c$. Wherever the full child range is covered and $b\le c<\beta$, the child level is $\beta-t$. The relevant parent lower and child upper functions are then in their explicit ranges. Their difference is

$$
\frac4\beta\log\frac{\beta-b}{b}
-\int_b^c\frac4{t(\beta-t)}\,dt
=\frac4\beta\log\frac{\beta-c}{c}.
\tag{10a}
$$

When $c<\beta/2$, this is the lower coefficient already available by sifting the parent directly at $c$. When $c\ge\beta/2$, it supplies no positive coefficient. A regional negative-cost improvement can therefore recover an existing direct parent estimate and must not be credited again as independent positive restoration.

## 3. Remaining direct Fouvry–Iwaniec bounds

Theorems 1–5 were read on the source page images, complementing checkpoint 6's Theorems 6–7 and Lemma 9. Source lengths are renamed below; $X$ is the source phase size. Logarithmic factors are omitted only from the displayed power expressions.

| Statement | Printed page | Coefficient restriction or bound |
|---|---:|---|
| Theorem 1 | 313 | Separate coefficients; $X^{-1/2}(X+M)^{1/2}(X+B)^{1/2}\|\phi\|_2\|\psi\|_2$ |
| Theorem 2 | 314 | Arbitrary joint coefficient on each variable pair; first term $(XM_1M_2M_3M_4)^{1/2}$ |
| Theorem 3 | 315 | Separate $\phi_m$ and joint $\psi_{m_1m_2}$; standalone phase exponent $\alpha\ne0,1$ |
| Theorem 4 | 317 | Separate coefficients; both phase exponents differ from 0 and 1 |
| Theorem 5 | 323–324 | Joint $\phi_{m_1m_2}$, separate $\psi_{m_3}$, **unit coefficient on $m_4$**, ratio phase $(m_3/m_4)^\alpha$ |

Theorem 3's exact power terms are

$$
X^{1/4}M^{1/2}(M_1M_2)^{3/4}
+M^{7/10}M_1M_2
+M(M_1M_2)^{3/4}
+X^{-1/4}M^{11/10}M_1M_2.
\tag{11}
$$

Theorem 4's exact terms are

$$
X^{1/8}(M_1M_2)^{3/4}
+M_1^{4/5}M_2
+M_1M_2^{17/20}
+X^{-1/8}(M_1M_2)^{21/20}.
\tag{12}
$$

Its powers $4/5$ and $21/20$ must not be inferred from OCR.

### Reciprocal remainder tests

For the existing reduction, the denominator product has scale $N^\Sigma$, the frequency length is $H=N^\eta$, and

$$
X\asymp HN^2/N^\Sigma,\qquad \xi=\eta+2-\Sigma.
\tag{13}
$$

The raw block must save relative to $N^\Sigma$, not $HN^\Sigma$. Its highest necessary unsmoothed frequency has exponent $\eta=\Sigma-1$. Sharp transfer adds a small positive extension; equality there cannot supply the saving.

**Theorem 1.** With $h$ in one slot and the collapsed denominator in the other, bounded coefficients give exponent $\max(\eta+1,\Sigma+\eta/2)$, at least $\Sigma$ at the highest frequency. Fixing $h$, applying the bound to denominator groups, and summing absolutely has exponent at least $3\Sigma/2-1/2>\Sigma$ there for $\Sigma>1$. These are generic mappings; no new prime-specific spacing or norm estimate is asserted.

**Theorem 2.** Including $h$ gives length product $HN^\Sigma$. Its first term has exponent

$$
\frac{\xi+\eta+\Sigma}{2}=\eta+1=\Sigma
\tag{14}
$$

at the highest frequency, independent of denominator grouping. Fixing $h$ and summing absolutely instead gives $1+3\eta/2>\Sigma$ there for $\Sigma>1$. The printed logarithm and coefficient losses do not improve these inequalities.

**Theorem 3.** Put a denominator group of exponent $a$ in its standalone slot, and $h$ plus the other denominator group in the joint pair. The four necessary closed caps are

$$
a\ge4\eta+2-2\Sigma,\quad
a\ge\frac{10}{3}\eta,\quad
a\le\Sigma-3\eta,\quad
a\le5-\frac{15}{2}\eta-\frac52\Sigma.
\tag{15}
$$

The second and third imply $19\eta\le3\Sigma$, hence $\Sigma\le19/16$ at $\eta=\Sigma-1$. These caps are stricter than the corresponding Robert–Sargos window. Fixing $h$ gives the still smaller necessary cap $\Sigma\le22/19$. These direct applications cannot raise total level $5/4$.

**Theorem 4.** The frequency cannot occupy either slot because its phase exponent is 1. For fixed $h$, with denominator groups in the slots, the first term requires $9\eta+2\le3\Sigma$, hence $\Sigma\le7/6$ at the highest frequency. The fourth term gives the stronger necessary cap $\Sigma\le15/14$. Neither is a sufficient region for applying all terms.

**Theorem 5 discrepancy.** Page 324 prints $\alpha\ne1$, but its proof applies Lemma 7 with $-\alpha$, requiring $\alpha\ne-1$, and defines $\beta=\alpha/(\alpha+1)$. The proof therefore does not justify the reciprocal value $\alpha=-1$ apparently allowed by the printed statement. An excluded-value sign discrepancy is an inference from the proof, not a verified external erratum. No application at $\alpha=-1$ is admitted.

Even formally granting the printed bound there would not help the generic remainder. The only direct ratio mapping with free $h$ is $m_4=h$, $m_3$ a denominator group of exponent $a$. Its first term $X^{1/2}(M_1M_2)^{3/4}M_3$ exceeds the target exponent by $(a+2-\Sigma)/4>0$ at the highest frequency for $\Sigma<2$.

A mapping with a free denominator factor instead uses $\alpha=1$, excluded by the printed statement. A reconstruction from the proof could be investigated for that Type I family. It is not a direct comparison for three weighted primes or for a balanced Type II block, which has no free denominator slot.

For the submitted larger-prime profile, a balanced Type II witness beyond the claimed frontier has $\Sigma>(6-\gamma)/4>6/5$, $1\le\gamma<6/5$. Theorem 3's $19/16<6/5$, Theorem 4's caps, Theorem 2's equality, and Theorem 5's free-slot restriction do not fill the gap left by checkpoint 6's Theorem 6. This extends the obstruction for **these direct mappings of the printed bounds**. Other decompositions, prime-specific spacing arguments and reconstructed special cases are not excluded.

### The marked three-prime comparison

The positive terminal box has actual untwisted prime-indicator coefficients. Additive Fourier inversion with period $T\asymp x=N^2$ has significant short-interval frequencies $H\asymp T/Y\asymp N$. Their Fourier coefficients have scale $Y/T\asymp N^{-1}$; a centered long comparator is negligible at this height for a fixed smooth weight.

Theorem 2 allows all four phase exponents to equal 1. With variables $h,p_1,p_2,p_3$, its length product is $HN^2$, and $X\asymp H$. Its first term is

$$
\sqrt{XHN^2}\asymp HN\asymp N^2.
\tag{16}
$$

Multiplication by $Y/T$ leaves order $N$, with a positive logarithmic factor in the printed bound. The desired error is $o(u)=o(N/\log N)$; the uniform box interface requires further logarithmic saving before summing boxes. The literal theorem does not prove that comparison. This neither shows that actual prime sums attain the bound nor excludes a sharper prime-specific evaluation of its spacing proposition.

Theorems 3 and 4 exclude the unreworked product-phase exponent 1. Theorem 5 requires an opposite-exponent pair and a free fourth variable, which this phase does not provide. The reciprocal Theorem 6 has a different phase. No terminal prime comparison is added.

## 4. A sharper mass-only witness

Checkpoint 4 constructed

$$
a_m^*=\frac YH(1+\lambda(m))1_B(m),\qquad
B=[N^2-H/2,N^2+H/2]\cap\mathbb Z,\quad
H=\frac{N^2}{(\log(N^2))^{10}},
\tag{17}
$$

where $\lambda(m)=(-1)^{\Omega(m)}$. It satisfies the extracted $o(u)$ divisor axioms through level $N^{5/4}$ and their one-sided mass consequences, while giving every prime weight zero. It does not have the actual support $J_N$, the individual integer floor bound, or the stronger power-saving remainder error.

Its root mass can be evaluated. Write $\mathcal L,\mathcal U$ for the normalized sieve functions:

$$
\begin{split}
&\mathcal U(s)=1\ (1\le s\le3),\quad
\mathcal L(s)=0\ (1\le s\le2),\quad
\mathcal L(s)=\log(s-1)\ (2\le s\le4),\\
&\mathcal U'(s)=\frac{\mathcal L(s-1)}{s-1},\qquad
\mathcal L'(s)=\frac{\mathcal U(s-1)}{s-1}
\quad\text{beyond the explicit ranges}.
\end{split}
\tag{18}
$$

These also give the leading long-carrier coefficients, normalized by $H/\log x$, for odd and even $\Omega$, respectively. To verify this, count integers with exactly $j$ prime factors by symmetric prime-product partial summation. The coefficient $C_1(s)$ is 1 for $s>1$; $C_j(s)=0$ for $s\le j$, $j\ge2$. Differentiating the lower-cutoff boundary of the prime-product integral gives

$$
C_j'(s)=\frac{C_{j-1}(s-1)}{s-1}.
$$

Even and odd sums give (18), including semiprime coefficient $\log(s-1)$. Uniqueness follows on successive intervals of length one. Only finitely many $j$ contribute at $s=8$.

This partial summation applies on (17): the last prime is at least $N^{1/4}$, and its interval has relative length comparable to $(\log x)^{-10}$. Zero-free-region PNT endpoint errors are negligible relative to this main term. Fixed interior regions can be used first, then boundary strips removed in the limiting integrals.

Repeated prime factors contribute at most

$$
O\left(H\sum_{p\ge N^{1/4}}p^{-2}+\pi(O(N))\right)
=O(HN^{-1/4}+N)=o(H/\log N).
$$

The degenerate eighth-factor exponent boundary has zero limiting volume. The exact sequence and its Buchstab identities still retain every prime power. Thus

$$
S_1^*(N^{1/4})=(2\mathcal L(8)+o(1))u.
\tag{19}
$$

Also $\mathcal L(s)+\mathcal U(s)=s\omega(s)$, by the same initial data and delay equation. At $\kappa=19/20>2/3$, only even-$\Omega$ semiprimes survive the high rough cutoff, giving

$$
R_{.95}^*/u=2\mathcal L(8)-2\log(21/19)+o(1).
\tag{20}
$$

The enclosed limiting coefficient is

$$
4.2914672098
<2\mathcal L(8)-2\log(21/19)
<4.2915489447.
\tag{21}
$$

This sharpens the earlier witness lower coefficient $4.2835968$. Its excess above $3.73$ exceeds $0.5614672$, and its centered excess over the ordinary reference is at least $0.8998292$. It also respects the new regional negative bound because that bound follows from the same divisor-mass axioms.

An adaptive optimization using only these extracted one-sided mass inequalities therefore cannot force the frontier target or a positive prime coefficient. This is an interface limitation. Estimates retaining actual short support, stronger errors or arithmetic correlations are not excluded.

## 5. The concrete arithmetic target

Use checkpoint 2's ordinary centered comparator

$$
Y_1=x\exp[-3(\log x)^{1/3}],\qquad
\mathcal B_N=[x-Y_1/2,x+Y_1/2]\cap\mathbb Z.
$$

Define $R_\kappa(I)$ by (1), replacing $J_N$ with $I$ and retaining cutoffs based on $N$. Its ordinary reference coefficient is

$$
r_{\rm ref}=8\omega(8)-\left(1+\log(21/19)\right).
\tag{22}
$$

The new $\mathcal L(8)+\mathcal U(8)$ enclosure, intersected with the independently preserved Buchstab enclosure, gives

$$
3.3915468895<r_{\rm ref}<3.3916379312.
\tag{23}
$$

Prime-product partial summation on the long comparator proves $(Y/Y_1)R_{.95}(\mathcal B_N)=(r_{\rm ref}+o(1))u$. A sufficient new estimate is therefore

$$
\boxed{
R_{.95}(J_N)-\frac{Y}{Y_1}R_{.95}(\mathcal B_N)
\le\left(\frac{169}{500}+o(1)\right)u
}
\tag{24}
$$

for **every sufficiently large even $N$**. It concerns a fixed arithmetic frontier with actual prime indicators and rough cofactors. It requires neither arbitrary bounded coefficients nor full asymptotic transfer of every terminal box. An almost-all-center estimate does not meet its quantifier.

If (24) were proved, then

$$
R_{.95}(J_N)\le(3.729637932+o(1))u<(3.73+o(1))u.
$$

The admitted root lower coefficient $L_0=(16/5)\mathcal L(5)$ and smaller-prime semiprime tail $C_{\rm small}(.95)$ would give

$$
\#\{p\in J_N:p\text{ prime}\}
\ge\left(L_0-r_{\rm ref}-0.338-C_{\rm small}(.95)+o(1)\right)u
>(0.0065583+o(1))u.
\tag{25}
$$

For a fixed positive finite-$N$ coefficient one may choose any smaller constant, with sufficiently large $N$. The saved enclosure of the conditional limiting margin is $[0.0065583130197,0.0066783497276]$.

This is a conditional implication. Neither (24), (25), nor the full main term $m(\vartheta)=1+\log((2-\vartheta)/\vartheta)$ is proved here.

## 6. Focused primary-literature check

The following adjacent statements were checked against their quantifiers. This was not an exhaustive literature review.

| Primary source | Relevant result | Campaign admission |
|---|---|---|
| [Teräväinen, arXiv:1510.06005v2](https://arxiv.org/html/1510.06005v2), Theorem 1 | Exactly three distinct prime factors in almost all very short intervals | No every-center comparison or selected balanced-factor region |
| [Matomäki–Teräväinen, arXiv:2207.05038v2](https://arxiv.org/abs/2207.05038v2) | Exactly two prime factors in almost all intervals of logarithmic length | No uniform arithmetic frontier bound |
| [Gafni–Tao, arXiv:2508.06463v1](https://arxiv.org/html/2508.06463v1), Theorem 1.1 and Lemmas 2.1, 3.1 | Almost-all prime gaps; averaged rough-count moments with $H=\lfloor\log^\alpha X\rfloor$, $z=\exp(\log^\beta X)$, $0<\beta<\alpha<1$ | Different roughness/length regime and averaged centers; no deterministic square-center conclusion |
| [Campbell, arXiv:2603.10356v2](https://arxiv.org/html/2603.10356v2), Theorem 1.1 | At most three prime factors between every pair of consecutive squares | Its square-started interval has length about $2\sqrt x$; $J_N$ is centered with length about $\sqrt x$. At-most-three-factor existence gives no marked balanced-product density |

These stated results are not admitted to the missing comparison. Their proofs may motivate further coefficient-specific arguments, but existence or almost-all statements cannot be substituted for (24). No claim is made that the proofs have been exhausted.

## 7. Reproduction and status

Run **python3 src/frontier_investigation.py** from the campaign directory. It uses Python's standard library, 20,000 cells per unit in (18) and 384 cells per coordinate in (9). Every operation is outward rounded with the inherited 50-digit interval type. The moving inner domain in (8) is mapped to a unit interval before enclosure. The positive difference (10) is enclosed directly.

Independent Buchstab and preserved root enclosures are checked for overlap. Exact rational exponent calculations reproduce the source caps. Their continuous arguments are supplied above; they are not inferred from a finite parameter sweep.

| File | Content |
|---|---|
| results/third_frontier_upper.json | Regional old/new negative costs and direct reduction |
| results/frontier_investigation.json | Extended delay enclosures, sharper parity witness, reference and conditional centered target |
| results/fi_remaining_bounds.json | Source-page evidence, exact exponent translations, coefficient restrictions and scoped rejections |

The four uploaded originals, historical notes, supplied baseline and all previous numerical result files are preserved. Current indexes and the state record are updated to checkpoint 7. The stronger $H(\vartheta)$ statement, a positive certified $K$ and the aggregate frontier target remain unproved. The usable progress is the regional negative-cost reduction, its accounting limitation, the sharper mass-interface certificate, and the arithmetic inequality (24).
