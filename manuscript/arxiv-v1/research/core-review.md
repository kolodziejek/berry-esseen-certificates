# Independent review of the combined analytic core

Date: 27 October 2026. Review branch: `manuscript/review-core-20261027`.
The reviewed files were read from the coordinator's separate `manuscript-v1`
worktree. This branch does not edit them. Their SHA-256 values at the
diagnostic checkpoint are in `runs/manuscript-20261027/core01/receipt.json`.
The coordinator subsequently added explanatory cross-references and row
identifiers to section 06, and resolved the two minor wording points below.
The mathematics reviewed below is unchanged; the final file hashes are in
`runs/manuscript-20261027/core01/reviewed-source-hashes.json`.

**Conclusion:** no blocking mathematical error was found in the statements
and proofs of the four reviewed sections at their stated scope. The core
supports the conditional manuscript, not a complete sharp Berry--Esseen
proof. Three small wording/integration recommendations are recorded below.
The continuum arguments were independently rederived; finite diagnostics
are supporting checks, not their proof.

| Component | Mathematical status from this review | Execution status |
|---|---|---|
| Fixed-index attainment, atom-safe contact and compact support | Locally rederived and checked for every stated index; no third-moment uniform-integrability assumption | No numerical test can establish the compactness argument |
| One-step Gaussian smoothing and least contrary index | Locally rederived; the least-index consequence remains conditional on the finite base and independent exclusion | Exact entry reserves checked; no certificate run |
| Sign split, physical defect and simultaneous weighted resource | Locally rederived under the explicit common-law and gap hypotheses | Exact checks on eight rational unit-variance laws |
| Count/master identities and conditional local witnesses | Locally rederived, retaining raw threshold, phase and event conventions | 288 exact count/collision cases |
| Whole-count coupling, discrete curvature and crossing moments | Locally rederived under the stated gap, phase, bounded-noise and legal-count assumptions | 96 full-coupling cases and 3,024 discrete-curvature cases |
| Convex score charge and joint residual | Locally rederived implication from the acquired resource and envelope | The existing 92-row arithmetic scan was not rerun in this review |
| Fourier acquisition, marked-crossing linear term, full local cover and BASE41 | Supplied/pending dependencies outside this review; not discharged by the preceding items | No inherited/native program or full certificate executed |

## Findings and recommended wording

1. **Resolved minor wording, section 03, variance-remainder paragraph near lines 116--124.**
   After displaying $G_w^{(4)}(H)=w^{-2}\phi'''(H/\sqrt w)$, “its absolute
   value is at most” can grammatically refer to the derivative. The displayed
   bound with factor $1/8$ is the bound for the **integrated variance
   remainder**, and is correct for that object. Replace the phrase by “the
   variance remainder therefore has absolute value at most.” No constant or
   theorem changes. The final read confirms that this correction is present.
2. **Resolved minor wording, section 06, definition of $d_{\rm new}$ near lines 66--70.**
   Explicitly display $nD\le N d_{\rm new}$. The following proof uses this
   scaling correctly, but “This is a bound on $nD$” after defining the scalar
   $d_{\rm new}$ can be read as the incorrect inequality $nD\le d_{\rm new}$.
   The final read confirms the explicit weighted inequality is now present.
3. **Resolved integration wording, Fourier appendix scope remark.** The separate argument at
   `ms:uniform-bridge` now exists. The remark should say that this appendix
   retains its original floor 47 and that the parameterized floor-42 bridge
   is provided separately, conditional on the complete analytic inputs and
   finite predicates. It should no longer imply that no bridge argument has
   been written. The final read confirms this wording and the explicit
   cross-reference are present. This review did not independently verify
   the entire new bridge or accept its numerical premises.

None is a counterexample to a reviewed lemma. No source or certificate
removal is justified merely by this review.

## Independent derivations

### Attainment and contact: section 02, lines 17--179

A positive maximizing sequence bounds the third moments by
$\rho_j\le\sqrt n/\eta$. The inequalities
$E[X_j^2;|X_j|>A]\le M/A$ and
$E[|X_j|;|X_j|>A]\le M/A^2$ give uniform integrability of the **first two**
moments. They give no uniform integrability of $|X_j|^3$, and the proof does
not assert it. Thus the weak limit has mean zero and variance one, while
only $\rho(P)\le\lim\rho_j=b$ is initially known.

The positive discrepancy is at least $\eta/\sqrt n$. Chebyshev bounds the
negative-threshold CDF, and the Gaussian tail bounds the positive-threshold
discrepancy, by $n/H_j^2$. Hence thresholds have a bounded subsequence.
For its limit $H$, the closed-set inequality first gives a bound at
$H+\epsilon$; right continuity then gives the bound at $H$ itself. This
retains any atom at the limiting threshold. The extremal inequalities
force $\rho(P)=b$ only at the end. The reflection identity uses a strict
event followed by increasing closed thresholds, so it equates suprema
without incorrectly asserting equality of closed events at an atom.

For contamination, retain the raw event $S_n\le H$ while standardizing the
perturbed marginal. The CDF factor is a finite polynomial in the
contamination weight; its derivative is
$n(F_{n-1}(H-y)-F_n(H))$. The moment derivative is
$|y|^3-\rho-3y\beta$, where $\beta=E[X|X|]$, not $EX^3$.
Differentiating the normal argument gives
$-\sqrt n\,y-H(y^2-1)/(2\sqrt n)$. Substituting these derivatives into the
quotient gives exactly $G'(0+)=I(y)$, with the displayed factor $\rho I(y)$
on the right side of the contact formula.

The function $F_{n-1}(H-y)$ is upper semicontinuous; at an atom its value
is the larger closed-event value. Since $I\le0$ and $\int I\,dP=0$, a
strictly negative value at any closed support point would contradict
positive mass in a neighborhood. This proves contact on the closed
support, including accumulation points. Its cubic term is $-C|y|^3$ with
$C>0$; all other terms have degree at most two or are bounded. Therefore
both distant rays lack contact points. Compact support is obtained before
any fourth moment is invoked. Rearranging gives exactly the stated CDF
majorant, including the linear coefficient $3C\beta/\sqrt n$ and constant
$C\rho/(2\sqrt n)$.

### Smoothing and least contrary index: section 03, lines 9--200

Conditioning the last summand bounds the difference from $EG_{n-1}(H-X)$
by the preceding **global** constant for the same marginal. Third-order
Taylor remainder in the spatial variable integrates only $|X|^3$.
For variance, $\partial_vG_v=G_v''/2$ and
$\partial_v^2G_v=G_v^{(4)}/4$, so the integral Taylor remainder is
$\frac14\int_0^1(1-t)G_{v+t}^{(4)}\,dt$.
The factor $\int_0^1(1-t)dt=1/2$ explains the $1/(8v^2)$ bound. The
Gaussian transform gives $\|\phi'''\|\le2/\pi$, yielding exactly the
recurrence printed in the manuscript. Both signs and all raw thresholds
are controlled uniformly. Remote atoms cause no hidden fourth-moment
requirement.

At $n\ge42$, putting $s=\sqrt{n/(n-1)}$ gives
$n(s-1)=[n/(n-1)]/(s+1)$, so the entry expression and
$3003/10250$ follow from $s<81/80$, $\sqrt{n-1}>6$ and $C_E<41/100$.
The strict reserves printed in the manuscript are exact.
Choosing the least index with $C_n\ge C_E$, rather than $C_n>C_E$, is
necessary for the strict conclusion at all subsequent indices. At the
first possible index 42 the two preceding indices are 41 and 40, both
covered by BASE41. Attainment remains available when $C_n=C_E$.
The reasoning does not itself prove BASE41 or a local exclusion theorem.

### Physical defect and joint plane: section 05, lines 11--252

The sign split gives $m^2=(1-\theta)pq$, $\ell=m/(pq)$,
$s=pq\theta/(1-\theta)$ and $X=\ell(Y-p)$. These identities distinguish
physical displacement from count displacement by a factor $\ell$.
Expanding each conditional third moment verifies all three displayed
identities for $\rho,\gamma,\beta$, with one common pair of conditional
cubic moments. An atom at zero belongs to the nonpositive class and causes
no sign error in these expansions.

For the gap functional, signwise Tonelli gives
$\int\tau=1$, $2\int|t|\tau=\rho$. If zero is in the support, the
one-sided gap estimate gives $J\le\rho$ and hence
$D\ge(\sqrt{10}-1)\rho$. Otherwise write the central gap as $(-A,B)$.
The sharper outer estimate is
$J_o^+\le T_+-2BR_+$ and
$J_o^-\le T_--2AR_-$, not merely $J_o\le T_++T_-$.
Expanding the central square and using
$\sqrt{\sigma+1}\sqrt{\sigma-1}=3$ reproduces the exact defect
decomposition. Every remainder is nonnegative. The auxiliary bounds
$AB\le1$, $m\le1/2$, $m\ge1/(2\rho)$ and $J\le\rho+2m$ have the stated
directions.

The stronger outer estimate yields

$$
D\ge(\sigma-1)EX_+^3+(\sigma+1)EX_-^3
       -6mAB+6BR_++6AR_-.
$$

Conditional cubic expansion gives
$EX_+^3\ge m\bar B^2+3B\theta_+$ and the corresponding negative term.
After substituting $R_+=\theta_++m\Delta_B$ and
$R_-=\theta_-+m\Delta_A$, the noise coefficients are exactly
$3(\sigma+1)B$ and $3(\sigma+3)A$. The deterministic remainder splits
into the displayed squared probability cost and
$6m[(A+B)(\Delta_A+\Delta_B)+\Delta_A\Delta_B]$.
Thus these costs are simultaneous; the argument does not spend the same
defect twice.

Multiplication by $n$, followed by
$m\ell=1-\theta$ and
$n\theta=(1-\theta)\lambda/(pq)$, gives the weighted joint-plane proof.
The replacements $n\ge N$, $1-\theta\ge1-\Theta$ and $pq\le v_*$
all act on nonnegative terms, including $b\ge0$. The cases $r<0$ and
$r=0$ are handled before division. An unweighted bound $D\le d_D$ would
not suffice for the claimed plane when $n>N$; the text correctly assumes
$nD\le Nd_D$.

### Count identities and curvature: section 05, lines 253--466

Conditioning the full sign vector produces independent residuals with
their actual conditional marginal laws. Summing by its number of positive
labels proves the mixture identity. Subtracting the binomial CDF gives
strict outgoing events and closed incoming events exactly as printed.
The threshold conversions are consistent:

$$
x=np+H/\ell=k+u,\qquad \delta=k-np=H/\ell-u,
\qquad H/\sqrt n=(\delta+u)/\sqrt{n(v+s)}.
$$

Direct subtraction then gives the master identity. In particular the
repair is $C(\rho_B-\rho)$, with the actual own score $C$, not $C_B$.
The nearest witness uses a positive deficit before replacing the count
mass by a lower bound; the whole-count witness uses $B<0$ and the valid
bound $I/n\le\max(0,I)/N$. No sign is silently assumed for $I$.

For the coupled cutoff, all legal increments are at least $c=1-d>1/2$;
the constant extension has increments one. Conditional on the coupled
residuals, the selector's closed event is precisely $J\le K$. This proves
the whole-count identity without replacing the actual marginal by a
relaxation. Centering forces admissible one-sided support bounds to have
$a_0,a_1\ge0$, hence $c\le1$ as needed later.

Double summation of the binomial differences gives weights $r-i+1$ on the
positive side and $h-1-i$ on the negative side. The hypothesis $\chi<2$
leaves only the first positive difference; on the negative side
$(\chi+i)_+\le\chi_++i$ produces exactly the second and third binomial
coefficients.

The first crossing bound follows from
$(cr-u)^2-r(c-u)^2=(r-1)(rc^2-u^2)\ge0$.
For the second, the derivative numerator is
$j(2u-c)+u$, nonpositive when $j\ge1$ and $u\le c/3$; replacing a
larger $u$ by $c/3$ decreases the crossing threshold. For the third,
the derivative numerator is $2cj-(3j^2-1)/2<0$ for $j\ge2$ and $c\le1$.
Its value at $j=2$ gives the denominator $(2c-1/2)^3$.
All divisors are positive because $c>1/2$ and $|u|\le1/2$.
Independence and centering yield
$EW_k^4\le A_U^2t+3t^2$, and Cauchy--Schwarz yields the stated cubic
moment bound. Bounded conditional noise is explicitly required before
this fourth-moment step.

The remaining linear term $\pi_k ER$ is not controlled by these curvature
bounds. The text correctly keeps its marked-crossing derivation separate.
Legal/interior count ranges, a positive own-variance multiplier and
normalizers such as $\sqrt n\,m_B\le1$ remain independent gates.

### Score charge: section 06

For each fixed corner, sign and nonnegative $h=|H|$, replacing the convex
slope by its chord gives an expression affine in $C$. Its supremum is
convex even though the displayed quotient need not look affine. Positive
endpoint $Q$ ensures positivity throughout. The maximizing value is
$A+\max(0,F_+,F_-)^2/(4Q)$; retaining the zero is essential.

On $[c,\chi]$ discard the nonnegative charge and use the larger formal
interval $[C_0,\chi]$. On $[\chi,C_1]$ the charge is at least
$N(C-\chi)$, so convexity bounds the charged expression by its endpoints.
Equality $C=c$ is included without inventing a positive charge. This
argument proves the two-interval lemma conditional on the same-law
resource and original moment-corner envelope.

The tightened residual and joint intercepts are the weighted-plane
construction already reviewed above. Replacing a positive intercept by a
smaller unrelated marginal bound would be invalid; the section instead
recomputes both from one residual. The CENTRAL uncertainty in the high
endpoint must be retained when enclosing chord weights, with lower $Q$
and lower endpoint in the subtracted score charge. The described outward
directions are correct. The actual 92 input rows, their rounding contracts,
the six printed ceilings and the workload count are not freshly verified
by this core review; their separate exact reports remain necessary.

## Reproducible diagnostics and limits

`check_core_review.py` is a new standard-library exact-rational diagnostic,
not an import or wrapper of inherited code. Run it from the review tree:

```sh
python3 manuscript/arxiv-v1/research/check_core_review.py
```

Run `core01` returned 0 in 0.807 seconds. It checked eight explicit centered
unit-variance laws, including symmetric and skew Bernoulli, two nearby
four-point mixtures, a three-point law with an atom at zero, a wider
four-point mixture, and tiny atoms at either distant sign. All moment
identities and the physical inequalities were evaluated exactly in
rationals and the ordered field generated by $\sqrt{10}$.
It checked 288 count identities at closed half-step and atom thresholds,
96 full independent-coupling/crossing cases in admissible gap regimes,
and 3,024 discrete-curvature cases with count extensions past both ends.
A negative control detects replacement of the strict outgoing event by
a closed one at a Bernoulli count collision.

These tests are finite adversarial diagnostics. They do not prove the
general statements, compactness, domination of an improper integral,
uniform Fourier remainders, complete domain coverage, or correctness of
an external theorem. No Gaussian floating-point value is used by this
diagnostic. No native program, archived checker, finite-base proof object,
LOW/HIGH campaign or external service was executed. No root manuscript
file was edited and no merge or publication was performed.
