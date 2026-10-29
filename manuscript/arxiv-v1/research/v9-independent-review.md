# Independent review of the v9 analytic composition

## Scope and status

The inventory baseline is fork commit `924e6160bee44ed3a50eba35f7dbb8dcd5b9a9c7`.
This review concerns the selected manuscript dependency graph, the transport of
old formulas to a fixed-target witness, and the scope of the new confinement
statements. It does not rerun a certificate campaign, accept BASE41, or prove a
complete local comparison. The original reference baseline remains
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.

The reviewer contributed some earlier structural and scalar lemmas. Those
contributions are not being represented as newly independent verification here.
The independent task is to audit the new composition and other authors' new
transcriptions against explicit source hypotheses. Formula checks below are
algebraic source derivations; execution status is **not run in this review**
unless a later subsection explicitly records a new command.

## Retained analytical dependencies

Locations in this table refer to the inventory baseline. Removing a source
from the selected compilation does not delete that source, invalidate its
properly scoped statement, or discharge its old numerical obligations.

| Source and precise scope | Selected v9 disposition | Reason and retained obligation |
|---|---|---|
| `sections/02-extremizers.tex`, old normalized-ratio extremizer/contact | Replace in the selected route by the full fixed-target extremizer/contact proof | The fixed-target objective is `a=sqrt(n)(F-Phi)-c rho`; the coefficient in its contact polynomial is the fixed `c`. An attained ratio maximum and its multiplier cannot silently be relabelled. Atom-safe closed-threshold attainment and compact support before higher moments remain necessary. |
| `sections/05b-conserved.tex`, old score-dependent conserved identity | Replace by `mathematics/fixed-target-v8/2026-10-28/conservation-proof.tex` | The fixed-target identity contains `(n+H^2)a`; its off-contact residual is `n^(3/2)(B-H xi)`. The Lebesgue support contribution in `B` must not be omitted. Full contact equality, not an arbitrary moment box, makes both residuals zero. |
| `appendices/fourier-analysis.tex:1-340`, labels `ms:fourier:kernel` and `kernel-1` through `kernel-24` | Retain as the closed-half-line smoothing appendix used by ROOT4 | The original-law ROOT4 bridge invokes this exact one-sided kernel. Its atom convention, cardinal boundary and normalization are not supplied by the compensated quadratic-hinge inversion formula. |
| `appendices/fourier-analysis.tex:354-726`, anchor/cosine/profile/modulus/rectangle machinery | Inactive for the selected fixed-target Fourier route | `mathematics/fixed-target-v7/2026-10-27/fourier-closure.tex` supplies a different complete elementary LOW/HIGH proof. It does not cite these lemmas. This is removal of an unused route, not proof that its numerical comparisons are unnecessary in every historical branch. |
| `appendices/fourier-analysis.tex:727-1471`, old LOW/HIGH families | Replace in selected route by the complete new Fourier appendix | The new proof must include compensated inversion, the entire sixth-order LOW triple, all six HIGH terms, the comparator tail, optional-term gates and index monotonicity. Its moment and actual-event inputs remain separate hypotheses supplied by the new entry proof. |
| `appendices/fourier-analysis.tex:1472-3042`, old resource atlas, score-phase enclosures and propagation | Inactive after full new fixed-target entry and resource proofs are included | The old atlas uses actual-score intervals and old row acquisitions. New entry must prove its own common-law moments, positive/localizing-matrix constraints, actual-event acquisition, signed coefficients, raw-to-resource conversion, ordered refinements and complete closed covers. A new table is not a substitution rule for the old score variable. |
| `appendices/fourier-analysis.tex:3043-3468`, literal floor-47 confinement | Replace by the explicitly rederived floor-42 fixed-target confinement | Old hypotheses include floor 47, strip .55, `p<q`, score coefficients and its own strict budget. New strip .6, floor 42 and fixed `c` require changed derivatives, deleted-index concentration constants and endpoint conventions. The old statement cannot be cited unchanged. |
| `appendices/fourier-analysis.tex:3470-4081`, exact counts, normalizations, tails, marked crossing and harmonic gain | Retain as a conditional count toolbox, with fixed-target score transport | The count identities and pathwise estimates do not require an extremal ratio. Their probability, phase, interior-count and positivity domains remain explicit; in particular the later one-sided normalization recipe assumes `p<1/2`. The scalar harmonic Bernstein conditions and a complete local cover remain unaccepted premises unless separately discharged. |
| `appendices/normalization.tex` | Retain | Its Gaussian constants are used by new support/Fourier calculations; the enlarged Stirling segment proof is used by the conditional count refinements. An enlarged segment crossing one half does not itself extend every later probability bound to `p>1/2`. |
| `appendices/local42-refinements.tex:1-438`, generic joint-budget, mass, signed Gaussian and cubic repair lemmas | Retain after explicit fixed-target adaptation | The signed cubic repair needs both a lower and upper positive multiplier: a negative cubic lower bound uses the upper multiplier. The actual count `k` must remain fixed while integrating the Gaussian derivative. |
| `appendices/local42-refinements.tex:440-494`, old score range, 45+47 rows and comparison schedule | Retire from selected route or label historical | The old `.4<=C<=.4226`, probability range `[.29,.474]`, row amplitudes and exclusions are not the new fixed-target acquisition. Their existence in a source file does not establish those bounds for the new witness. |
| `appendices/uniform-bridge.tex` | Inactive for the selected new entry | This is the old finite-LOCAL42-to-uniform-support bridge. It is not needed by a newly proved direct support/entry chain, but its removal must not be described as acceptance of LOCAL42 or its finite predicates. |
| `appendices/finite-support.tex`, `appendices/finite-analysis.tex` | Inactive in the selected account of the new approach, preserved as old finite-base candidates | No selected tail statement may claim BASE41 from their omission. ROOT4 is only one independently scoped candidate in the still-open finite base; it does not replace all of their finite-n dependencies. |
| `mathematics/fixed-target-v8/2026-10-28/root4-bridge.tex` | Retain as a separately conditional original-law finite-base bridge | The one common tagged measure, exact contact/zero-atom budgets, full fourth-power remainder, original-law quadrature and threshold interpolation are genuine analytic inputs. Whole-domain producer validity, qualified finite arithmetic and global owner localization remain separate. |

## Exact count transport

For one common law and one actual threshold let

`a = sqrt(n)(P(S_n<=H)-Phi(H/sqrt(n))) - c rho`,

`a_B = sqrt(n)(F_B(k)-Phi(delta/sqrt(nv))) - c rho_B`.

Direct subtraction gives

`a-a_B = sqrt(n) pi_k (Q/pi_k-f(u)) + R_c`,

where

`R_c = sqrt(n)[Phi(delta/sqrt(nv))-Phi(delta/sqrt(n(v+s)))] + c(rho_B-rho)`.

Thus the two local witnesses can conclude `a-a_B < -epsilon lambda`.
They must not retain the old left side `rho_B(C-C_B)` after changing the
definition of the right side. For the one-sided cubic repair at old Fourier
lines 3648-3675, the hypothesis `Q_*>0` ensures `rho-rho_B>=0` and a lower
bound for fixed `c` licenses the same favorable subtraction. For the more
general signed repair in `local42-refinements.tex:380-438`, define the positive
multiplier using fixed `c`, retain both its endpoints, and use the upper one
when `Q_*<0`.

The marked crossing, common-sum tail, fractional-part gain and discrete
curvature arguments do not contain the score coefficient. Their inputs
remain the same actual two conditional laws. In particular the strict
outgoing event and closed incoming event must survive the transcription.
The retained count recipe is not a proved cover for the new acquired domain:
the old Stirling/mass/ratio recipe has `p` below one half, an interior `k`,
positive denominators, and a checked lower variance factor. The new strip
result for probabilities up to .53 does not automatically satisfy them.

## New Fourier edge: explicit inputs, not an atlas alias

The complete proof in `fourier-closure.tex` derives its own symmetrization,
Taylor expansion on the complex joining segment, Jensen actual-event bound,
nonzero and zero Fourier cells, rational Gaussian tail and all-index floor
comparison. It does not need the old anchor/profile/modulus atlas. The
following obligations must be visible before applying it:

1. Actual bounded support and common valid bounds for the fourth and sixth
   moments, cubic coefficient and fifth-order Taylor coefficient.
2. A genuine event of two independent copies, with positive probability
   lower bound, positive distance lower bound and a conditional squared
   distance upper bound. An optimizer of a moment relaxation is not that
   event.
3. Every positive decay and index-monotonicity gate, including the separate
   gates for optional HIGH improvements. A failed optional gate permits the
   simpler complete bound, not omission of the corresponding integral.
4. One complete LOW triple; minima may select whole valid HIGH bounds.
5. The compensated inversion lemma for a finite signed measure of mass and
   first moment zero and finite absolute second moment. Its identity is
   valid at atoms and for every `H`; no fixed-law asymptotic limit is used.

The new signed transport must order its operations: prove actual support
before higher moments; obtain a raw bound before licensing the density/phase
price; derive a resource bound for the same witness; then intersect subsequent
boxes only with already proved necessary conditions. The six-piece HIGH
event may use an actual-gap bound only after that gap has been acquired.

## Integrated-source review

### Count transport: corrected transcription defect

An intermediate v9 transcription renamed the count-increment lower bound
`c=1-d` to `zeta`, to distinguish it from the fixed target `c=CE`, but left
`cr`, `cj`, `ci` and `cR` in several crossing calculations. It also changed
the separate variance coefficient `c_v` to undefined `zeta_v`. This would
have been a mathematical error: the target `CE<1/2` does not satisfy the
increment hypothesis. The reviewer reported the exact sites; the coordinator
corrected them. A subsequent read of `sections/05c-counts.tex:184-212` and
`appendices/count-comparison.tex:422-600` confirmed the corrections, including
the marked forward event, two tail distances and variance denominators.
The remaining `C` occurrences only name the actual ratio or its Bernoulli
comparison. `local42-refinements.tex` now uses fixed `c` in both branches of
its signed repair and does not import the old 45+47-row cover.

### New moments and signed resources

The full draft `sections/06-fixed-resources.tex` in the separate confinement
worktree was read, including every formula. The following were re-derived
from its premises rather than inferred from an earlier success log:

- The two outer-gap integral bounds and the endpoint expansion yield one
  nonnegative budget `D>=B0+E0+integral k+ dmu+ + integral k- dmu-`.
  The two measures are defined from the same physical conditional noise.
  There is no independent choice of moment maxima.
- The initial product bound follows from `J<=rho+2mAB`, `gamma<=rho`,
  `rho>=1` and `m<=1/2`. The theta and displacement updates use a refreshed
  binary lower charge only after a previously proved theta decrease.
- The beta interval uses the correct orientation also when `p>1/2`.
  The rho update maximizes the two affine branches before and after the
  turnover `r/(kL)`, with the positive-part slope allowing either sign.
- In the weighted joint inequality the input is `nD<=N D_I`. After
  subtracting `n B0>=N b_I`, the displacement term has an additional
  factor `n>=N`, while `n theta=(1-theta)lambda/(pq)`. These give the
  two displayed intercepts. One does not obtain this conclusion by
  multiplying an arbitrary unweighted bound by `N`.
- The previous raw ceiling licenses the density floor in the new raw
  polynomial. Only its newly proved raw ceiling licenses the new phase
  price. From `exp(-w)M>=c rho-T/n>0` one obtains
  `R_c-U>=H^2(c rho-T/n)/2`. The direction and order are correct.
- For each actual sign of `H`, the signed linear envelope is convex in
  the fixed target endpoint parameter. The remaining terms are affine;
  endpoint maximization is valid even if the constant moment term or
  signed slope is negative. The positive quadratic gate is separate.
- Closed-region filtering retains every intersecting moment cell. A
  concave quadratic is maximized at its clipped vertex; whole valid
  ceilings can be intersected. An empty list is an exclusion only
  relative to the complete ancestor cover.

No blocker was found in these analytic implications. The eight-round
30-panel numerical claims and the 682-cell phase export remain linked to
their stated finite conditions. This review did not replay those checks.

### New confinement: index, sign and atom checks

The full draft `sections/07-fixed-confinement.tex` was read through the
central-panel theorem. Its low-noise heat lemma is proved independently of
the resource-strip input: it uses fixed-target contact, nonnegative excess,
and the true predecessor bound. The later resource-strip acquisition may
therefore cite it without a circular assumption about its conclusion.
The heat expansion explicitly covers `u>sqrt(3)` and proves the Gaussian
derivative bounds it uses. The negative quintic proof correctly uses
concavity of `P'`, not the false stronger assertion `P''(left)<0`.
The held-moment derivatives used along each physical ray are distinguished
from derivatives of the boundary family. The abstract probability interval
is `[.4,.6]`; the acquired application is only `[.4,.53]`.

For the high-noise argument, the following checks were made directly:

- The derivative of the fixed-target contact majorant has coefficient
  `c`, and the excess changes only its constant. For negative physical
  `t`, using an upper coefficient multiplying `t` gives a lower slope,
  as required. The positive-side completion and the negative-part
  correction in the sharper lower-ray bound have the correct signs.
- The central-gap defect expansion, its two endpoint displacement costs,
  the noise term and leakage are charged to one shared resource simplex.
  `kappa<phi(0)/6` gives its displayed direction. `R_*<0` excludes;
  resource equality is retained.
- Conditional label increments are at least `1-d`. Only intervals of
  strictly smaller diameter are bounded by an antichain probability.
  Both deleted indices satisfy `j>=n-2>=40`; the factor checks are the
  new floor-42 inequalities, not reused floor-47 constants.
- In the lower-ray construction, the right endpoint of `I` is at most
  `-tau-zeta`, hence its physical coordinate is at most
  `-E(l+tau+zeta)`, exactly the domain of the sharper slope. `I+` starts
  strictly beyond `a0+1-.6-2d0`, lies inside the half-open central gap,
  and both widths are below the actual increment. Contact is needed at
  the putative support endpoint only; the other endpoint uses the global
  majorant in the correct direction.
- In the upper-ray construction, `d0+2tau<1/2` places `I+` strictly before
  the putative contacting point. The atom at the inner support endpoint
  is included; the atom at the upper contacting point is excluded.
  The stated half-open survival differences implement these conventions.
- The signed deletion identity keeps the centered noise term, producing
  `epsilon/2`. The pair event is strict `Delta>tau`; equality is in the
  good event. The two deleted convolutions are not interchanged.
- The simplex vertex bounds and the tangent upper bound for
  `x/(N tau+x)` are valid simultaneously. The inverse-index replacement
  uses nonnegative quantities and its separate sign gate. Taking a
  minimum of complete error bounds is safe.

No blocker was found in this scoped derivation. The complete high-noise
claim remains conditional on its 128 closed-box cover and strict finite
gates, and is restricted to `[.41,.42]`. The low-noise theorem supplies the
16 first-band boxes without changing the recorded failed sufficient
estimates. Neither result supplies the final count comparison or the
remaining high-noise panels.

### Fixed-target core and selected entry

The complete foundation drafts `sections/02-fixed-target.tex` (336 lines)
and `sections/04-fixed-entry.tex` (910 lines at the read) were checked,
together with the complete selected Fourier proof. No blocking mathematical
defect was found in this bounded source review. Particular checks were:

- The common third-moment ceiling preserves the first two moments under
  weak convergence, but is not misused as uniform integrability of third
  moments. Maximality and the negative third-moment penalty force equality
  in the lower semicontinuity step. The threshold inequality is the closed
  moving-threshold inequality. Full closed-support contact is obtained by
  upper semicontinuity, before compact support licenses higher moments.
- Contamination holds the raw sum event fixed while standardizing the
  perturbed marginal. Its normal and cubic derivatives have the stated
  factors. Reflection uses the left limit, hence dominates rather than
  falsely equates an error at an atom. Equality `C_n=c` supplies attained
  excess zero using the bounded-rho approximating sequence.
- The two evaluations of the zero-bias integral have the residual signs
  `B-H xi`; the nonzero support integral in `B` is retained. The first-
  moment identity and hinge identity yield `(n+H^2)a`, not `na`.
  Specialization to `c=CE` is explicitly required for the positive defect
  resource.
- The first moment radius uses the stated affine Shevtsova bound, not a
  different affine inequality with a larger numerical consequence. The
  support contact comparison uses the true predecessor and discards
  `-na<=0`; no ratio-optimality premise or own-score ceiling is imported.
- Before an actual gap exists, the universal event
  `{(X-X')^2>=9/25}` follows from `E(X-X')^2=2` and
  `E(X-X')^4=2M4+6`. Its probability and conditional-square bounds have
  the correct directions. Thus no prospective gap is used in the first
  Fourier pass.
- The coarse negative-gap charge follows by extending its nonnegative
  integral and applying Tonelli. The integral divided by the squared
  terminal magnitude is exactly the displayed Gamma expression, and
  `E X_-^3=(rho-gamma)/2` produces its factor `3/2`.
- The strict second-pass test excludes zero from the closed support and
  therefore acquires the actual central gap. The stronger gap-distance
  formula follows by adding the two valid lower bounds for
  `m(A^2+B^2)` and `2mAB`, then dividing by the upper first-moment bound.
- Localizing-matrix and Cauchy inequalities retain one common `m` and
  sign moments. Zero denominators drop a nonnegative correction unless
  the original positive-semidefinite inequality gives a genuine
  contradiction. The three fifth-moment losses are intersected by their
  maximum, not added.
- After the gap, the opposite-sign event is an event of two actual iid
  copies. Its probability is `2pq` and its conditional squared distance
  is `[1+beta(1-2p)+4m^2]/(2pq)`. Convexity in `p` and affinity in beta
  license the stated corner bounds. The event is not inferred merely
  from feasibility of a moment rectangle.
- The signed constant and linear bounds are whole valid envelopes. For
  a fixed nonnegative `|H|`, the target-parameter dependence is convex;
  both target endpoints suffice even when the constant charge is
  negative. The raw threshold root is enlarged by clamping the constant
  to its positive part. Weighted `nD` is retained at the actual `n`.

The selected-route theorem is explicitly conditional on the two finite
conditions, their complete cover, Fourier gates and ordered raw licenses,
as well as the external structural bound. This source review is not a new
independent replay of those finite calculations. In particular, earlier
signed-K and two-pass lemmas to which this reviewer contributed are not
claimed as newly independently accepted results here.

### Global implication and harmonic obstruction

The current `sections/08-certificates.tex` separates the weak finite base,
equality-inclusive local exclusion, and the positive-excess alternative.
The least index `n>=42` with `C_n>=CE` has both required predecessors;
at `n=42` they are base indices 40 and 41. Attainment then supplies the
nonnegative fixed-target witness. There is no circular use of the desired
tail bound in this composition. The local exclusion remains an explicit
missing assumption, not a consequence of the acquisition or confinement.

The independently read `sections/07b-harmonic.tex` correctly extends the
sine-chord argument to conditional span `b<1`, without extending any other
count gate. Its actual three-atom family is standardized because
`q[p+eps(1-eps)]=t^2 q^2`. Its sign conditional residuals are
`U0 in {eps-1,eps}` and `U1=0`; the fixed-count residual is an integer
translate of `(n-k)eps`, so the selected fractional-part gain vanishes.
The limit has arbitrarily small defect and noise with span exactly one.
The manuscript does not claim these laws satisfy maximizing contact.
This is a valid obstruction to the proposed moment-only shortcut, not
to the sharp conjecture.

The review found a second, distinct transfer defect in the initial v9
count appendix: its old numerical sine recipe used
`x=3.14159 b` and the degree-seven alternating polynomial as a lower
bound for `sin(pi b)`, after the abstract span domain had been enlarged
to `b<1`. For `b>1/2`, lowering the argument of sine is not a monotone
lower-bound operation. Near one the polynomial is negative, so squaring
it to make a positive rate is also invalid. This does not refute the
abstract span theorem. The proposed repair is to use
`x=3.14159 min(b,1-b)` and the identity
`sin(pi b)=sin(pi min(b,1-b))`. The argument then lies below `pi/2`,
where sine is increasing. Its degree-seven lower polynomial is positive:
the cubic truncation is positive and its fifth/seventh pair is positive
there. Alternatively the old recipe can remain explicitly restricted to
`b<=1/2`. Final-source verification of the repair is recorded below.

The scheduled signed-box comparison `11264` versus `239616` is scoped
to the coarse component. The old count comprises twelve signed stages
and one export evaluation; it is not a measured runtime or a count for
the complete proof. The independent finite base, larger-noise panels and
strict relative-noise comparison remain unresolved.

### Final source check and recommendation

A read-only active-input reference scan of the final integrated source
found 19 inputs, 259 unique labels and 196 references, with no missing
input, duplicated label or unresolved reference. The inspected tree is
coordinator commit `5f01d77` plus the final source polish described here.
This is a document consistency check only; compilation and visual review
are the coordinator's separate responsibilities.

The final sine recipe now uses the proposed fold, explicitly proves the
positivity of the degree-seven lower polynomial, and keeps the denominator
`b^2` in the rate. The domain defect is corrected. The guide also now
introduces `U` only after the raw license, avoiding an implication that it
is the unconditional left side of the exact conservation identity.
The shortened heat proof cites the full spatial/variance calculation in
the entry section: that calculation and its four remainders hold for every
`u>=1`, before the later large-radius `H4>0` optimization. Hence the new
confinement use at `u>sqrt(3)` imports neither that optimization nor a
prospective noise strip. The derivative calculation is likewise general.
The scoped old appendices are absent from the selected input list but
preserved in the repository.

**Recommendation:** no remaining blocking mathematical transcription or
dependency issue was found at the reviewed scope after the two corrections.
The selected conditional research manuscript is ready for the coordinator's
final document checks and human review. This is not approval of a completed
Berry--Esseen proof, the whole original Fourier atlas, the complete ROOT4
producer graph, any historical native acceptance, or any deletion of source
certificates. No external bibliographic claims were freshly verified in this
review. The finite base, complete larger-noise acquisition and full strict
count comparison remain open as the manuscript states.

The new `research/v9_checks/scalar.py` was separately spot-checked against
the two displayed cosine proofs. Its Machin bounds use the correct signed
combination of 32- and 12-term alternating intervals. It constructs
`K-Q/x` with the correct directed powers of pi, then the affine pullback
and Bernstein transform on `(2/K)/cells`. Odd truncations of five and
seven terms and the explicit decreasing-term gate justify the upper
Taylor polynomial. This discharges exactly the 80 and 896 scalar
coefficient obligations if the recorded run is accepted; it does not
expand a count domain or accept a comparison cover. No fresh run was
performed by this reviewer. Independently, the negative-control value
`K=4.5` is false at `x=3/8`, since its true ratio is
`(8+4 sqrt(2))/3>9/2` (already `sqrt(2)>11/8`). Thus that control is
not merely an otherwise valid bound failing a sufficient certificate.


## Reviewed final byte snapshots

These SHA256 values identify the read source bytes, not mathematical acceptance.
Paths are relative to `manuscript/arxiv-v1/`. Subsequent layout or cosmetic
changes require their own provenance; no such change silently extends this review.

| Path | SHA256 |
|---|---|
| `main.tex` | `7ff04e52c194e1b08485171a8a3e478448f50b7b2d74436069eff580f86ee68d` |
| `sections/02-fixed-target.tex` | `5a00687b76390fcaa4c57f9f893d070b23bf3119eda8aa4b82d66c3b4c0b509b` |
| `sections/04-fixed-entry.tex` | `db7156ca43f874b29216d6f297d74ea79ace4b988ec200a93a169e0d342498d8` |
| `sections/06-fixed-resources.tex` | `1c8c5357a7057cff203fc580847dfdd0ee5befa5788d20761cce4956b0bd5ad0` |
| `sections/07-fixed-confinement.tex` | `a1961a20b3dd8a6b6b465c82493e59a83d254559a9705e02e00626d2ce302fc4` |
| `sections/05c-counts.tex` | `4902cddc9465536ea7d8ff2208d8ed39d81de200759660e8bdbb918ffc1157f2` |
| `sections/07-curvature.tex` | `5ac12fec045400abb3f313665ad1a243e87f8245c423c826a5ea56420fb70698` |
| `sections/07b-harmonic.tex` | `30ded13d35b033d13c8fa48db55a25ff10d88888649df43901837c05362c1404` |
| `sections/08-certificates.tex` | `846d5fa8fb752aef117d3533038758154b4b97fd8bbb191042a0e068cf3117d7` |
| `appendices/fixed-fourier.tex` | `f13b162a5a6d69934dd8f0c0b1b19274d5ec942dd87a855b94490f9e60c79478` |
| `appendices/count-comparison.tex` | `b81146b5a8b80e46da99db6e468c148598a0a7c05ab5117e46a477c47c90435e` |
| `appendices/local42-refinements.tex` | `d44bc3dd9b0eaf0de85e8d44ba76ebcdf5fd19fa49b54a58978298dab248206f` |
| `research/v9_checks/scalar.py` | `a2387da4629d9abe09bb4bace634cd6b2172043815af68e2b609b95de2b70657` |


## Post-review cosmetic addendum

After commit `3ca58fb`, the coordinator made two requested source-only
corrections. This addendum compares the actual coordinator files, not the
older source copies on the review branch. For each file, the SHA256 of
`git show 5f01d77:<path>` exactly matches the earlier review pin. Applying
only the listed substitutions reproduces the new file bytes exactly:

- `sections/04-fixed-entry.tex:254`: the label `v9:fourier:high` is called
  a Proposition rather than a Lemma. Its target in `fixed-fourier.tex:226`
  is in fact a proposition. No inequality or hypothesis changes.
- `appendices/local42-refinements.tex:51,194-197`: four local prose/notation
  occurrences now use `zeta` for the count-increment lower bound and its
  curvature dependence. The fixed target remains `c=CE`; no formula,
  constant, domain or certificate predicate changes.

The final snapshot table above now contains the two new hashes. The previous
pins were:

- `sections/04-fixed-entry.tex`: `c1051e60e728fd9bb3a03734d889f2fce4fa7f6834d88dd7ddc3d00de5536032`.
- `appendices/local42-refinements.tex`: `55741dabacc3429a03dbfb6354890b460cd2ff55ee754f4e591215cbafcbcdc5`.

Execution status for this addendum: fresh byte comparisons passed; no
mathematical certificate, numerical replay or LaTeX build was run. The
scoped recommendation is unchanged. The earlier notation caution is resolved.
