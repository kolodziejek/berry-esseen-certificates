# Independent review of the third manuscript revision

Reviewed on 27 October 2026, starting from fork commit `6299d97`, on the
separate branch `manuscript/v3-review-20261027`. The immutable original
reference remains `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.

## Scope and outcome

The proposed `deslop.patch`, `main(10).tex`, `README.md`, and
`source-arxiv-v1 2/MANUSCRIPT_REVISION_INSTRUCTIONS.md` were treated as
editorial and mathematical proposals. Their claims about equivalence,
verification, author approval, and historical facts were not accepted
merely because they were stated in those files. The proposal hashes are
in `revision3_checks/receipt.json`.

The principal mathematical defect found is a false displayed second
derivative in the pre-revision curvature proof. The proposed correction
is correct. An independent derivation below proves that the stated
three-candidate maximum formula survives the correction. This is an
erratum to a proof formula, not a change of theorem, numerical target,
certificate coefficient, or acceptance predicate.

The local-exclusion reformulation is equivalent, using the established
positive closed attainment statement, including at equality. The
integrated main text retains the conditional global conclusion and the
substantive uniformity, sign, moment, and coverage hypotheses reviewed
below. Several unsafe editorial shortcuts were corrected during
integration. No complete local exclusion, independent base through 41,
or global Berry--Esseen bound is established by this review.

| Reviewed item | Mathematical status | Execution status |
|---|---|---|
| Corrected curvature derivative and maximum formula | Independently derived on the stated continuous domain | Exact polynomial identities freshly checked; old formula rejected by a rational negative control |
| Equivalence of local-exclusion formulations | Proved using positive closed attainment | Logical argument; no certificate execution involved |
| Required scalar constants | Analytic alternating-series enclosures plus exact rational comparisons | Fresh bounded PASS, including the finer 15-decimal bounds on pi |
| Revised main-text scope and hypotheses | No new mathematical blocker found in the inspected integration | Read-only source comparison; no main-manuscript compile by this reviewer |
| Corrected small reduction proof | Same conditional theorem with corrected derivative | Fresh nine-page compile; pages 5 and 6 visually inspected |
| Full finite base and uniform local exclusion | Still conditional/open in the manuscript | No native predicate campaign or complete replay |

## 1. Curvature: independent derivation and consequences

The audited domain is

\[
 b\in\mathbb R,\qquad \tfrac12<c\le1,\qquad
 [l,h]\subseteq[-\tfrac12,\tfrac12],
\]

and

\[
 f(u)=r(u)+g(u)
 =\frac{(b+u-1)_+}{(c-u)^2}
  +\frac{(b+u)_+}{[c+\min(u,c/3)]^2}.
\]

Every denominator is strictly positive on this domain. On the active
part of the first summand, put `p=b+u-1` and `d=c-u`. Direct quotient
differentiation gives

\[
 r'=\frac{d+2p}{d^3}
    =\frac{2b+u+c-2}{(c-u)^3},
 \qquad
 r''=\frac{2[3(b-1)+u+2c]}{(c-u)^4}.
\]

The numerator bracket equals

\[
 3(b+u-1)+2(c-u)>0.
\]

The old displayed formula had `2u+c` in place of `u+2c`; its value is
smaller than the true derivative by `2/(c-u)^3`. For example, at
`(b,c,u)=(1,3/4,1/4)`, the true derivative is **56**, while the old
display gives **40**. This point lies in the stated domain and in the
active region, so it is an exact counterexample to the old derivative
identity. It is not a counterexample to the maximum theorem.

On `u<c/3` and `b+u>0`, independent differentiation of the second summand
gives

\[
 g'=\frac{c-2b-u}{(c+u)^3},\qquad
 g''=\frac{2(3b+u-2c)}{(c+u)^4}.
\]

If `r>0` here, then `b>1-u`, and hence

\[
 3b+u-2c>3-2u-2c\ge0.
\]

The last inequality uses both `u<=1/2` and `c<=1`; neither domain
restriction may be silently discarded. Thus the sum is convex wherever
`r>0`. Above `c/3`, `g` is a positive part of an affine function divided
by the positive constant `(4c/3)^2`, so it is convex there too.

At `u=1-b`, activation of `r` increases its derivative by
`1/(c-u)^2`. At `u=-b`, activation of `g` has a nonnegative jump. At the
denominator transition `u=c/3`, when the numerator is positive, the jump
is

\[
 \frac{2(b+c/3)}{(4c/3)^3}>0.
\]

It is zero if the numerator is inactive; simultaneous transitions add
nonnegative jumps. These kinks cannot supply a strict interior maximum
that is missed by the remaining cases.

Where `r=0`, either `g=0` or, below `c/3`, the sign of its derivative is
the sign of `c-2b-u`. Its sole possible interior maximum is therefore
`u_*=c-2b`. Its numerator is positive exactly when `c>b`; the restrictions
`u_*<=c/3` and `u_*<=1-b` put it in the required piece. Its value is

\[
 g(u_*)=\frac{c-b}{[2(c-b)]^2}=\frac1{4(c-b)}.
\]

Above `c/3`, an active `g` is increasing. Flat zero pieces cause no
additional maximum value. Continuity includes singleton intervals,
endpoints, coincident kinks, and `c=1`. Thus the exact maximum consists of
the two endpoints and this eligible third candidate, exactly as stated
in `sections/07-curvature.tex`.

The correction does not alter the endpoint transport or zero clamp.
For positive noise, `q/(a*lambda+G^2)` is convex when `q>=0,a>0`, and
`A0+A1/lambda` is convex when `A1>=0`. Taking the maximum with zero
preserves convexity. For every `n>=N`,

\[
 I/n\le\max(0,I)/N.
\]

This holds separately for positive and negative `I`; it does not require
the old positive-correction assumption. Multiplication of a bracket by a
binomial mass lower bound still requires that bracket to be negative.
The integrated revision retains this gate. Monotonicity in `c` also
survives: each positive denominator increases with `c` for fixed `b,u`,
and the numerators are independent of `c`.

## 2. Local-exclusion equivalence and first-failure quantifiers

For each fixed integer `n>=42`, let `A_n` be exactly the scalar conjunction

\[
 0\le n(C_n-C_E)\le0.54,\quad n(C_{n-1}-C_n)_+=0,\quad
 C_n<0.4226,\quad C_{n-1}<0.4253,\quad C_{n-2}<0.4253.
\]

Let `E_n` be the set of pairs `(P,H)` that attain `C_n` as a positive
closed discrepancy. The old assumption says

\[
 \forall n\ge42:\quad \neg\exists e\in E_n\; A_n.
\]

The conjunction `A_n` contains no pair-specific variable. The attainment
lemma gives `E_n` nonempty for each fixed `n`, including when `C_n=C_E`.
Consequently

\[
 (\exists e\in E_n\; A_n)\iff A_n,
\]

which proves the proposed scalar reformulation. This equivalence would
fail without attainment, or if an omitted pair-specific condition were
part of `A_n`. Neither failure occurs here. The manuscript's attainment
link must identify the positive closed maximum, rather than merely an
absolute discrepancy of unspecified sign.

Under the separate sharp base through 41, choose the first `n>=42` with
`C_n>=C_E`. At `n=42`, the deleted predecessors are exactly 40 and 41;
at larger indices they are bounded by the base or by minimality. Both
are at most `C_E`, the predecessor loss vanishes, and the exact recurrence
gives `0<=n(C_n-C_E)<3003/10250<0.3`. Thus every entry condition above
holds. Excluding equality gives a strict tail. Selecting only a first
strict exceedance gives the weak global upper bound instead. Calling
equality a counterexample to the weak conjecture would be misleading;
the integrated revision correctly says “first failure of the strict bound.”

The recurrence still has its exact two additive terms; the guide correctly
describes their combined order as `1/n`, not `n^(-3/2)`.

## 3. Gaussian constants and safe proof relocation

Moving the elementary Gaussian proof out of the main narrative is sound
if its full derivation remains available. The patch's floating decimal
value for the maximum of `|phi'''|` is not a substitute for that derivation.
The integrated revision instead retains the Fourier proof of
`||phi'''||_infinity<=2/pi` and the exact comparisons in
`appendices/normalization.tex`, under `ms:gaussian-constant-proof`, while
the main lemma keeps `ms:gaussian-constants` and points to that proof.

There are two required precisions. The smoothing/support/resource
arguments use bounds such as

\[
 819/2000<C_E<20487/50000,\quad 0.39886<\phi(0)<2/5,
 \quad \pi>160/51.
\]

The harmonic majorants in `appendices/local42-refinements.tex` and the
marked-crossing estimate in `appendices/fourier-analysis.tex` use the
finer directed endpoints

\[
 3.141592653589793<\pi<3.141592653589794.
\]

The coarse lemma alone does not supply those endpoints. The finer
alternating-series argument must remain, or be explicitly included in
the common constants appendix. The independently written check uses 32
terms of `arctan(1/5)` and 12 terms of `arctan(1/239)`. The integrated
geometric-series remainder provides rigorous lower/upper endpoints;
Machin's identity follows from tangent addition with the angle in
`(0,pi/2)`. Exact rational arithmetic then verifies the directed interval
and all scalar comparisons listed above. This check does **not** execute
or accept the harmonic Bernstein predicates.

## 4. Editorial changes: retained conditions and rejected shortcuts

The read-only integrated-main snapshot is identified by the hashes in
`revision3_checks/integrated-main-snapshot.json`. It is a working-tree
snapshot of the sibling `manuscript-v3` checkout, not an immutable source
commit. Review observations are tied to these bytes.

* `main.tex` now restricts the contact description to fixed `n>=2`,
  makes the sharp finite-base assumption explicit before first-failure
  reasoning, and states that the complete equality-inclusive local
  exclusion remains open. It does not declare the global conjecture proved.
* `sections/01-introduction.tex` retains uniformity in the law and in
  `n`, identifies the earlier-version scope and external inputs of the
  inspected Lean project, and keeps moment/Fourier hypotheses on the
  support and resource implications. Unverified early constants 1.88
  and 7.59 from the instructions were not added.
* `sections/01b-guide.tex` keeps the exact recurrence, ordered prior
  moment bounds, the oriented zero-defect case, and the distinction
  between an exact count identity and the separate required relative
  bounds as noise tends to zero.
* `sections/04-support.tex` retains uniformity in the raw threshold,
  both exterior rays, the sign check before replacing the multiplier
  by a lower bound, and moment assumptions proved before contraction.
* `sections/05b-conserved.tex` retains compactness before higher moments,
  compensated inversion over the entire half-line, the two complete
  frequency integrals, `r<2N/5` before unweighting, and the signed phase
  resource hypotheses. The patch's description of `L` as plain mass
  was corrected to weighted leakage.
* `sections/05c-counts.tex` retains legal/interior count domains, the
  positive own-variance denominator gate, one common law/threshold/phase,
  positive-noise hypotheses, the zero clamp, and a separate zero-noise
  Bernoulli argument. Deleting surrounding repeated cautions therefore
  does not delete these mathematical conditions.
* `sections/06-resources.tex` explicitly assumes the phase-resource
  corollary and its hypotheses; panel consequences remain conditional
  on coefficients and moments established for the same law. The zero
  residual case is stated separately. A rounded bound on a chosen
  remainder bound is distinguished from an enclosure of the exact raw
  remainder itself.
* `sections/08-certificates.tex` retains both phase signs, all legal
  nearest counts, closed seams/endpoints, the event-plane inequality,
  denominator positivity, and the binomial mass sign gate. Its status
  paragraph distinguishes proved implications with inputs from a complete
  verified acquisition/local-exclusion chain.

The proposed assertion that polynomial factors above degree three
“require compact support” is false as a necessity statement. Finite
corresponding moments suffice; compact support supplies them here. The
integrated version makes that correction.

The supplied instructions' description of themselves as “author-approved”
does not independently establish approval or historical use of a named
vendor. No additional Gemini history, claim of line-by-line author
verification, or numerical historical result was inferred. The integrated
disclosure avoids those specific unsupported additions and does not
declare the earlier paper mathematically superseded by a complete proof.
This review does not independently verify the authors' broader AI-use
history. Bibliographic verification is recorded in the earlier literature
review rather than repeated here.

A transient TeX defect was reported to the coordinator: the integrated
three-column status table had single backslashes in row endings. This is
a compilation issue, not a mathematical finding; the coordinator is
repairing the table and owns the main-manuscript compile.

## 5. Erratum propagation and actual execution

At the coordinator's explicit request the same derivative correction was
applied in this review branch to these two continuation files:

* `mathematics/reduction2/2026-10-27/local-kernel.md`, derivative display
  and following positive-numerator decomposition;
* `mathematics/reduction2/2026-10-27/proof/main.tex`, the corresponding
  two lines of the curvature proof.

No immutable reference, existing certificate, predicate, target, or old
run record was changed. The manuscript main-text correction is owned by
the coordinator's separate branch. The old audit/check reports remain
historical records; this erratum does not relabel them as having detected
the derivative error.

The new standard-library check
`revision3_checks/check_derivatives_constants.py` independently implements
sparse polynomial differentiation and rational arctangent intervals.
It imports no native/local kernel. `stdout.txt`, `stderr.txt`, and
`receipt.json` record a fresh exit-zero result, the Python version, elapsed
time, and input/output hashes. The old derivative is a negative control;
its mismatch is explicitly printed. This is algebra/constant evidence,
not a sampled or formal proof of the full continuous theorem.

The corrected small TeX proof was compiled through the installed LaTeX
skill using existing TeX Live. The complete command, source/PDF hashes,
elapsed time, stdout and stderr are under
`runs/reduction2-20261027/curvature-erratum01/`. The result has nine pages,
exit code zero, and no LaTeX warnings or overfull/underfull boxes.
Pages 5 (the corrected formula) and 6 (the following page) were rendered
at 140 dpi and visually inspected: no clipping, overlap, or malformed
equation was found. `visual-review.json` records this bounded scope; it
does not claim a new visual inspection of the other seven pages.

## 6. Limits and remaining integration review

The main-text edits reviewed here do not discharge the full Fourier,
confinement, finite-base, or local-certificate chain. In particular,
renaming a finite-index or floor-47 lemma does not make it valid for every
`n>=42`; a cross-reference must retain its exact actual-index hypotheses.
Likewise, replacing duplicate proofs by references is safe only after
matching their variables, signs, normalizations, and hypotheses.

The large appendix deduplication was still being integrated when this
report was written. Its final source changes require a separate bounded
integration pass; this report does not certify an unseen final appendix
or assert that every proposed deletion is equivalent. No native
certificate suite, complete root cover, or external proof package was run.

Recommendation at this checkpoint: accept the curvature erratum and the
reviewed main-text mathematical scope; keep the full global theorem
conditional and complete the final appendix/cross-reference integration
checks before treating the revision as ready for submission.

## 7. Bounded appendix integration addendum

After the preceding checkpoint, the Fourier consolidation was integrated
as `1e28363dbbe5a89dccca15a3d62eb4af4d002e58`. I read the changed proof
substitutions and their cited main-text arguments. I also read the
coordinator's changes to normalization, the uniform bridge, positive-loss
support, and local42 refinements, and the finite appendix in the separate
`manuscript-v3-finite` constructor worktree. The latter's reviewed SHA-256
is `4f67624b77b98ba79d9b07695d60bf42492708c89a19aef8f0f67c6fe5427193`.
All reviewed appendix/main hashes are recorded in
`revision3_checks/integrated-appendix-snapshot.json`; the finite source was
reviewed before its final integration commit.

The finite source was subsequently integrated as `1c0c7ab`; a byte-hash
comparison confirmed it is exactly the source reviewed above.

This is a bounded application and equivalence review of the changes,
not an independent verification of every retained argument. No new
native arithmetic or certificate check was run for this addendum.

| Addendum item | Mathematical status | Execution status |
|---|---|---|
| Selected Fourier/finite duplicate-proof substitutions | Hypotheses and variable substitutions independently matched below | Read-only source comparison; final finite source hash matched |
| Corrected signed-phase endpoint | Independently derived from `delta=xi-u` with the sign-safe logarithmic remainder | Source inspection; no new local predicate execution |
| Curvature interval upper bound and zero clamp | Valid consequences on the stated positive-denominator domain | Source inspection; derivative algebra evidence is in the earlier bounded run |
| Complete retained appendix chain and certificate predicates | Still supplied/conditional; not independently verified in full | No native campaign or full acceptance |
| Combined manuscript layout and references | Visual inspection does not establish mathematical or bibliographic correctness | Subsequently inspected overview pages 1–48 and full-resolution pages 35 and 42; see `revision3-visual-review.md` |

### Fourier substitutions

The central-gap decomposition and simultaneous inequality use the same
standardized law, compact support, actual inner endpoints, conditional
means, and signed conditional variances as the main statements. Their
auxiliary bounds and the subsequent interval updates are retained.

The weighted joint-resource substitution retains `n>=N>0` and
`nD<=N d_D`. In the separate lemma assuming only `D<=D_*`, the proof
correctly specializes the cited theorem's floor to the **actual index n**,
so its weighted input becomes `nD<=nD_*`. The resulting coefficients
`g=6(1-Theta)S` and `h=k_*(1-Theta)/(n v_max)` agree with the displayed
affine inequality. This avoids the invalid inference from `D<=D_*` to
`nD<=N D_*` with a smaller fixed floor.

The antichain proof is independent of the floor: conditional independent
Bernoulli labels have increments at least `c`, and a set in an interval
of diameter strictly smaller than `c` is an antichain. The independent
shift assertion follows by conditioning. The separate rational binomial
mode estimate remains at `N=47`, `J0=N-2=45`; it is not silently changed
by citing the floor-42 appendix's combinatorial argument.

The local-witness reference makes `V_j=W_j` and `m_0=m`. Its actual
interior count, same phase, strict outgoing events and closed incoming
events match. The appendix's `I>=0` condition makes the main theorem's
`max(0,I)/N` equal to its displayed `I/N`, while `B<0` remains required
for the binomial mass replacement. The zero-noise reference preserves
the attained positive closed threshold and its binomial-atom argument.

The whole-count reference uses the same independent coupling and zero
extension. A smaller increment lower bound `c=1-d0` is legitimate when
the actual `d<=d0`; the crossing estimates use only that lower bound,
`1/2<c<=1`, the phase bound, conditional centering and the stated amplitude.
The discrete binomial-curvature estimate also retains `chi<2`. No
marked-crossing or fractional-part remainder is discarded by this
substitution.

The closed-box Bernstein reference preserves the affine changes, degree
four in each coordinate, and all closed boundary faces. The scalar cosine
lemma still begins with an explicit finite positivity premise even though
the embedded program has been moved out of the article. The finer
32/10-term pi enclosure is retained in the Fourier appendix; the local42
32/12-term recipe is also retained. Their roles are distinct from the
coarser smoothing constants.

### Finite-index substitutions

For `n=2` and `n=3`, the general positive closed attainment lemma applies
to the same unrestricted standardized class. The external structural
inequality excludes `rho>=2` or `rho>=15/8`, respectively, under the
strict contrary hypothesis. No finite-support restriction or uniform
integrability of third powers is introduced by the replacement.

For either index, the main contact majorant is

\[
 nQ_H(y)=nF+\frac{x\phi(x)+C\rho/\sqrt n}{2}
 -\left(\sqrt n\phi(x)+\frac{3C\beta}{\sqrt n}\right)y
 -\frac{x\phi(x)+3C\rho/\sqrt n}{2}y^2
 +\frac{C}{\sqrt n}|y|^3.
\]

With raw `H=t=x sqrt(n)`, `beta=m`, `C/sqrt(n)=lambda`, and
`C rho/sqrt(n)=D`, this is exactly the displayed finite-index polynomial.
The contact inequality is multiplied by `n`, explaining the left sides
`2P(X<=t-y)` and `3P(X_1+X_2<=t-y)`. Equality remains on the complete
closed support. The revised prose correctly says positive discrepancy,
not positive raw threshold.

The signed-second-moment reference uses only centering, unit variance,
finite third absolute moment and both nonempty sign classes. The weighted
signed-moment loss reference requires finite fifth absolute moment and
`E|X|=2m>0`; its Cauchy proof and possible zero atom match, without needing
the surrounding Fourier appendix's stronger application hypotheses.

The Pearson formulas are polynomial identities for the reflected
auxiliary standardized law. They do not impose the narrower coefficient
gate `R>=2g`. The finite appendix retains its piecewise `R<2g` repair,
signed coefficient rectangle, and actual-index damping conditions. Its
Gaussian cancellation formula follows from the exact tail identity,
retaining the sign of `z-3c`; it is not replaced by a weaker unsigned
bound or by a theorem with a smaller domain.

For the outer-gap reference, compact support is explicitly stated with
distinct support-radius notation. The main defect identity and its
`T_++T_--J_o>=2BR_++2AR_-` consequence give the same decomposition.
The separate inequalities
`T_+<=(R_++B)R_+` and its negative analogue (with radius and residual
distinguished in the TeX notation) remain proved there. Therefore the
displayed weighted prices and the single residual `D-mQ` are unchanged;
no two independent copies of that residual are spent.

The one-, two-, three-, four-, and five-summand numerical conclusions
remain attached to their certificate conditions. Their unchanged
positivity statements and continuous-domain covers were not executed
in this editorial review. The larger finite base is not asserted proved.

### Signed-phase correction, cover, and references

The local42 positive-phase proof had an undefined `h` in the endpoint
`2hu-u^2`. The corrected endpoint `2xi*u-u^2` follows directly from
`delta=xi-u`. There is no sign restriction on `xi` in that substitution.
For clarity, the preceding logarithmic lower bound is valid even if
`2delta*t+t^2` is negative: after replacing the denominator, the discarded
combined remainder is

\[
 \frac{s(\delta+t)^2}{2nv(v+s)}\ge0.
\]

Thus the corrected proof keeps the actual `delta` fixed while integrating
over `t`, and uses the stated endpoint bound on `xi` without reflecting
the law. The count formula and final scalar target do not change.

The removed earlier local42 coverage paragraph is duplicated by the
remaining final cover table. The probability panels, both signs of the
raw threshold, closed phase/noise seams, acquired amplitude caps,
band-dependent joint bound and separate zero-noise case remain explicit.
The positive-loss support appendix likewise retains its different finite
index hypotheses and numerical positivity premises.

The coordinator repaired the transient table row-ending issue. The main
file now sets `secnumdepth=4` after `appendix`, so demoted paragraph
headings with reference labels receive their own numbers instead of
silently sharing the preceding subsubsection number. The coordinator
completed the combined build; my bounded visual follow-up is recorded
separately in `revision3-visual-review.md`.

The coordinator also restored the explicit curvature interval upper bound.
For `u` in `[a,d]`, each numerator is at most its value at `d`;
`c-u>=c-d>0`, and `c+min(u,c/3)>=c+min(a,c/3)>0`.
Bounding these two nonnegative summands separately proves the displayed
outward bound and hence its domination of the new exact maximum on every
subdivision. This keeps the mathematical comparison to the old envelope
available without referring to implementation cache behavior.

**Addendum conclusion:** no blocking mathematical change found in these
bounded deduplication/application checks. The global implication remains
conditional on the genuinely independent base and complete uniform local
exclusion; the appendix consolidation does not discharge either input.
