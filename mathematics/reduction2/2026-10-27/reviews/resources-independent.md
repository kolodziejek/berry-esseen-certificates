# Independent review of the retained score-excess resource

Reviewed construction: `15e48cb8d90e4187b9bcff1dabb5448cdfe59e00`, including
the resource construction `22a40df6336895f22fba644fa2d2df8798112873` and its
actual-score-domain clarification. Review branch:
`simplify/review-resources-20261027`. Immutable reference:
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.

**Verdict.** I found no blocking defect in the conditional resource reduction.
A separately derived, weaker binary-penalty calculation verifies all named
row exclusions and threshold crossings. The result licenses fewer downstream
comparisons after the original resources have been acquired. It does not
license omitting acquisition, confinement, their analytic premises, or any
input required by a current production acceptor.

| Claim | Mathematical status | Execution status |
|---|---|---|
| Two-interval score-charge lemma | Independently derived below, conditional on the retained phase resource and corner envelope | Exact arithmetic checks its constants and all 92 row consequences |
| LEFT0 excluded; LEFT5,8,10,13 and CENTRAL28 cross the named seams | Independently checked with conservative bounds weaker than the constructor's | Fresh PASS of this review's fixed Fraction/dyadic script |
| Two signed LEFT LOW predicates and four signed LEFT profile evaluations become unnecessary | Conditional domain consequence, with exact consumer mapping below | Source inventory checked; native predicates not executed |
| Original acquisition, confinement, Fourier/contact reductions and numerical comparisons | Retained supplied dependencies | No archived arithmetic program imported or run |
| All-index application and a complete revised acceptance pipeline | Conditional on the separate uniform42 bridge and complete new composition | Not established or executed by this review |

I did not author `tighter-resources.md` or its checker. During review I
suggested replacing the paired lower moment bound in the charge by the
weaker universal bound `rho>=1`; the constructor incorporated this before
the reviewed head. This is disclosed collaboration, not a claim of blind
review. The proof below and the alternative binary calculation were derived
separately. I previously authored the computational/local-cover reports and
the one-pass adapter; this report is not an independent review of those works.

## Bound source and consumer locations

Let `F` denote the logical archive prefix
`work/toward40_20261007/audit43/capsule/work/below49_20261006/`.
All `F/...` line numbers below refer to the decoded manifest-selected blob,
not to a same-named historical file. The archive is
`verification/finite-tail/sources/backend.zip`, SHA256
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`.
Its `finite61/MANIFEST.json` SHA256 is
`c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`.
The manifest's `files[path].sha256` selects `finite61/blobs/<sha256>`.

Write `L=F/package_audit/left42_confinement/` and
`A=F/acquisition/`. Exact source locations used in this review are:

| Source | Location and relevance |
|---|---|
| `paper/analytic-supplement.txt` | 2238–2256 Gaussian-weight license; 2271–2287 conserved phase resource and extra curvature; 2467–2487 weighted joint resource; 2534–2548,2572–2583 corner maximization |
| `L/contracted_kernel.py` | 313–324: affine score dependence of quadratic constant/curvature and finite maxima of affine linear coefficients |
| `L/corrected_phase_callback_extended.py` | 19–25: sign-corrected curvature with score-independent correction |
| `L/coupled_panel_core.py` | 20–28 binary/noise resource; 41–53 score cap and weighted update; 59–60 joint intercepts; 63–72 final score/moment corners |
| `L/confinement_core.py` | 7–10 installs the correction; 32–46 proves both signs before contraction and resource feedback; 41 uses cap `.4226` |
| `A/kernel.py` | 19–20 exact floor/ceiling implementation |
| `A/central42_acquisition_core.py` | 16,20–21,27–37: `.4247` cap and outward rounding contract |
| `A/coupled_panel_core.py` | 58–60 weighted update; 67–77 final endpoint `min(cap,.40974+raw/n)` and quadratic export |
| `A/central42_confinement_core.py` | 48–59: both signed proofs precede support feedback; `bounded(c.cell(...))` at 57 |
| `L/profile_core.py` | 11–16 coherent remaining inward resource; 18–34 empty/inherited/evaluated profile alternatives |
| `L/accept_profiles.py` | 20–28 parent binding, finite 42–48 metadata and four fixed bands; 29–49 full replay and closed cover; 32–34 active cubic bound 30 override |
| `A/central42_profile_core.py` | 8–9 bands; 22–41 row/sign/band loop; 33–34 inherited amplitude, otherwise 40 numerical evaluation |
| `F/local/left42_final/mid42_contract.py` | 5–20 MID noise/phase sectors and shared resource |
| `F/local/left42_final/central42_contract.py` | 17–30 LEFT LOW configuration, `.08` threshold and amplitude schedule |
| `F/local/left42_final/bind_low42.py` | 20–39 fixed 74 signed labels, scalar inputs and complete grid; 46–48 exact replay; 69 frozen index |
| `F/joint_resource.tex` | 119–154 same-law gap resource; 170–205 weighted triangle; 222–241 rounding and warning against a bare `D` substitution |

The supplement hash is
`dad4a3558b01bda4acfdfc9120a50ecbcd7a6f2389886ba3ce72a6602ec39018`.
The nine pins independently checked by this review are recorded in
`check_resources_independent.py:20–30` and its stdout, including the exact
45-row table, its confinement parent, both profile objects, the 47-row central
table and the principal formula/rounding sources. The construction's fuller
22-input pin list is at `check_tighter_resources.py:21–43`.
Hash binding identifies the source; the source proofs remain obligations.

## Independent mathematical derivation

Fix an actual acquired same-law witness at an integer `n>=N=42`. Let its
score be `C>=c=C_E`, let `rho=E|X|^3`, and put `kappa=997/15000`.
Normalization `E X^2=1` gives `rho>=1` by the monotonicity of integral means.
Retain the acquired geometry, moment rectangle, phase signs, deleted-score
caps, support and strict concentration hypotheses. The source resource is

\[
 n(C-c)\rho+\kappa nD+n^{3/2}L\le\mathcal B(H),\qquad L\ge0.
\]

For each fixed moment corner and phase sign, `h=|H|>=0`, the upper envelope
has form `A(C)+F(C)h-Q(C)h^2`. Source inspection shows `A,Q` affine in `C`.
The correction to `Qraw` is
`(.4-phi)*min(0,3.16*rho-3-d)/2`, independent of `C`; the extra conserved
curvature in `Qbudget` is also independent of `C`. It is included once.
For each sign `F` is a maximum of finitely many affine score functions plus
a fixed slope, so it is convex. Its endpoint chord majorizes it throughout
the score interval. Since `h>=0`, replacing `F` by that chord is an upper
bound; this sign condition matters.

For fixed corner, sign and `h`, the chord quadratic is affine in `C`.
Its supremum over those indices is therefore convex, with exact value

\[
 G(C)=\max_j\left[A_j(C)+
 \frac{\max(0,\widehat F_{j,+}(C),\widehat F_{j,-}(C))^2}{4Q_j(C)}\right].
\]

Positive curvature at both endpoints proves it throughout the interval.
The zero in the numerator accounts for a nonpositive linear coefficient:
the supremum on `h>=0` then occurs at zero. The moment-corner reduction is
an inherited analytic premise; this argument does not independently prove
that premise or replace the paired corners by `rho=1`. Only the excess
charge uses the universal lower moment bound.

Take `C0=.4095`, `chi=.40974`, and assume `C0<c<chi<C1` and `C<=C1`.
For actual `C` in `[c,chi]`, the excess charge is nonnegative, and convexity
bounds `G(C)` by the endpoints of the larger formal interval `[C0,chi]`.
For `C` in `[chi,C1]`, every factor has the needed sign:

\[
 n(C-c)\rho\ge N(C-\chi),\qquad
 \kappa nD\le G(C)-N(C-\chi).
\]

The latter right side is convex. Thus

\[
 \kappa nD\le B_*=\max\{G(C_0),G(\chi),G(C_1)-N(C_1-\chi)\}.
\]

This includes the equality case `C=c`: no positive charge is assumed there.
For all 45 LEFT rows the score cap is saturated at `.4226`; direct rational
comparison gives the middle endpoint as the largest of these three bounds.
The calculation preserves one actual law and its acquired enclosing
rectangle. Interpolating envelopes in score is not interpolation of laws or
an assertion that every formal score is attained.

I independently bracketed `c` from
`c^2=(19+6sqrt(10))/(72*pi)`. Alternating integrated geometric expansions
bound `atan`; this review uses 8/7 terms at `1/5`, whereas the construction
uses 6/5. Squared rational endpoints bound `sqrt(10)`.
For Machin's identity, tangent doubling gives `tan(4 atan(1/5))=120/119`;
subtracting `atan(1/239)` gives tangent 1. The resulting angle lies in `(0,.8)`.
It lies below `pi/2` since `pi/2=2 atan(1)>1`, the last inequality following
by integrating `1/(1+t^2)>1/2` on `(0,1)`. This fixes the branch. Exact
rational comparisons then prove `.4095<c<.40974`.

### CENTRAL rounding is part of the proof

The final exact central score endpoint is not exported. Reading both the
rounding implementation and its caller establishes the needed interval:
`kernel.up(x,10^6)` is `ceil(10^6 x)/10^6`; the acquisition wrapper adds
`10^-6` again. Therefore its exported `raw_out` encloses the exact final raw
value in `[raw_out-2*10^-6,raw_out]`. The source `c.cell` computes the final
score endpoint from that exact raw value before `bounded` rounds it.
Consequently

\[
 C_1\in[\min(.4247,\chi+(r_{out}-2\cdot10^{-6})/42),
          \min(.4247,\chi+r_{out}/42)].
\]

The two possible extreme chord weights enclose the true one. Coefficientwise
upper bounds on `A,F`, a lower bound on `Q`, and the lower `C1` in the high-end
charge give outward budgets. Positivity of the lower `Q` is checked.
The actual curved/chord envelopes need not equal these separate interval
extrema; domination suffices. All47 rows satisfy the middle-endpoint
dominance using these outward values. Treating the rounded `raw_out` as an
exact endpoint would lack this justification.

### The residual must stay joint and weighted

Combine the old `nD<=42*d_old` with the new inequality to obtain
`d_new=min(d_old,B_*/(42*kappa))` and **`nD<=42*d_new`**.
Let the acquired bounds be `theta<=Theta`, positive gap endpoints `A,B`, and
`p` in the same closed panel. Set `v_*=max p(1-p)` and
`K=min(3(s_l+1)B,3(s_l+3)A)>0`, with `s_l<sqrt(10)<s_u`.
The source gap resource, after discarding only nonnegative terms, implies

\[
 nD\ge42b_*+6\cdot42(1-\Theta)(A+B)d_{in}
             +K(1-\Theta)\lambda/v_*.
\]

Indeed `n>=42` multiplies the binary and inward terms; for the noise term
use the actual identity `lambda=npq*theta/(1-theta)` and
`1-theta>=1-Theta`, `pq<=v_*`. No unweighted replacement can supply the
factor `n` needed here. With `r=d_new-b_*`, a negative residual excludes the
row; a positive residual gives the one triangle

\[
 \frac{d_{in}}{r/[6(1-\Theta)(A+B)]}
 +\frac{\lambda}{42v_*r/[K(1-\Theta)]}\le1.
\]

It would be invalid to spend the full residual separately on the two
coordinates. A zero residual requires separate handling and is rejected by
the fixed checker; none occurs in these inputs.

My arithmetic uses a weaker binary lower bound than the construction:
convexity gives `(1-Theta)^(3/2)>=1-3Theta/2`, and a dyadic upper square-root
bound on `v_*` uses grid `2^-40` and an exact square comparison. Inserting
these in

\[
 b_*=(6+2s_l)\frac{1-3\Theta/2}{\sqrt{v_*}_{upper}}
       \max\{0,(4-s_u)/2-u,l-(4-s_l)/2\}^2
\]

is valid since all 92 rows have `0<=Theta<2/3` and positive geometry. It gives
larger conservative noise ceilings. Nevertheless every surviving new noise
and inward intercept is at most its inherited counterpart. This independently
verifies the named consequences without copying the constructor's root
routine or merely re-running its checker.

## Exactly what becomes unnecessary

All row indices below are zero-based. The bounds are this review's upward
rational roundings to nine decimal places, not claims to reproduce the
constructor's slightly stronger decimals.

| Row and closed `p` panel | Independently verified bound | Conditional downstream removal |
|---|---|---|
| LEFT0 `[.290,.292]` | Joint residual `<0` | Its final TINY comparison domain; no ancestor acquisition/confinement call |
| LEFT5 `[.300,.302]` | `lambda<=.049948982<.05` | The row's MID domain; its TINY and zero-noise obligations remain |
| LEFT8 `[.306,.308]` | `lambda<=.077281566<.08` | Both signed LOW predicates `61.low.left42_final.08.minus` and `.plus` |
| LEFT10 `[.310,.312]` | `lambda<=.094066694<.10` | Higher MID/LOW sectors and both signed profile evaluations in requested band `[.10,.12]` |
| LEFT13 `[.316,.318]` | `lambda<=.117301859<.12` | LOW sector from `.12` and both signed profile evaluations in requested band `[.12,.30]` |
| CENTRAL28 `[.436,.438]` | `lambda<=.099809748<.10` | Comparison sector from `.10`; its profile amplitude was already inherited |

The complete 92-row scan finds precisely these new crossings among
`.05,.08,.10,.12`, with only LEFT0 excluded. Rejecting proposed further
deletions of LEFT6, LEFT9 and CENTRAL38 is meaningful: these calculated
upper bounds remain above their respective seams. This is failure of the
particular bound to license those deletions, not a constructed iid witness.

The two LEFT8 labels reduce the selected LOW cover from 74+78 to 72+78=150.
If each label were still evaluated by both a producer and a replaying binder,
this removes four evaluator invocations; with an independently validated
one-pass pipeline it removes two. These counts cannot be added as independent
savings. They refer to a future complete contract, not today's fixed index.

The pinned LEFT profile object has `joint_resource_profile` for row 10 band 2
and row 13 band 3. Each has two signs, with recorded gate counts respectively
`[1795,295]` and `[2265,295]`: four signed evaluations and 4650 source-recorded
gates. Those are historical object counts, not fresh numerical passes or
measured runtimes. CENTRAL 28 band 2 has `proof.inherited=true` for both signs
and therefore contributes **zero** profile arithmetic savings. The independent
checker checks those object distinctions, not merely the requested band name.

Every removed band has its lower endpoint strictly greater than the new
ceiling, so its entire closed domain is empty. All remaining phase signs,
nearest-count branches, probability endpoints and phase seams retain their
old cover. Noise zero still requires the Bernoulli input. LEFT0 is excluded
only after its final row is acquired; the adjacent probability panel also
remains at the shared endpoint. These facts remove no acquisition or
confinement producer and no whole MID/TINY native job.

## Evidence, implementation boundary and recommendation

The fresh command actually run, after reading the script, was

```text
python3 -I -B -S mathematics/reduction2/2026-10-27/reviews/check_resources_independent.py
```

It ran under Python 3.9.6 with exit 0 and empty stderr. Evidence is in
`runs/reduction2-20261027/resources-independent01/`: `run.json` records the
resolved interpreter, command, worktree/head, version, input hashes,
timestamps, return code and stdout/stderr hashes. `stdout.json` records the
92 results, nine source bindings, rational constant bounds, exact profile
consumer counts, seven rejected controls and `full_proof_pass=false`.
The review script SHA256 is
`f0626274e150150beac0bd494e289efe82ac173b62e2f51ba82f115e36037959`.
The constructor's program was read but not imported or executed.

Seven controls reject missing/reordered panels, a changed score endpoint,
zero curvature, and the three unsupported row deletions. Two elementary
necessity examples show why forcing a positive charge at equality and using
an unweighted defect would be invalid; these are not iid counterexamples.
The checker is evidence for this fixed pinned invocation and its stated
conditional arithmetic. It is not an acceptance API for arbitrary externally
supplied resource tables, and it does not reconstruct the native row proofs.

Read-only inspection also covered the coordinator's combined
`mathematics/reduction2/2026-10-27/proof/main.tex:347–481` in its separate
`second-reduction` worktree. The score, rounding, joint-budget and consumer
formulas agree with this review. I requested that the local resource lemma
explicitly state `n>=N=42`, rather than rely on the earlier least-index
context; that hypothesis is essential to its charge inequality. This is a
transcription check of the resource section only, not review of the support
or curvature sections and not a TeX compilation result.

The original LEFT profile acceptor still requires 45 rows, four statuses per
row, target hashes and full exact replay. The LOW binder still requires 74
LEFT labels and its frozen index. No existing acceptor can omit these inputs
on the strength of this note. A new output/index/coverage contract must
represent the changed 150-label cover and vacuous profile entries explicitly,
then be independently reviewed. The old 152-label one-pass contract is
incompatible with those changes without that new assembly.

The source metadata remains finite 42–48. An all-index application needs the
separate zero-decrement support/parameter and uniform42 arguments; neither
the floor 42 nor this exact arithmetic supplies that extension. Finite-base
closure, equality-compatible attainment, full LOCAL42 numerical acceptance,
and complete global composition remain unresolved here.

Before staging, `git diff --diff-filter=MDRT --name-status
6346fc1b4432bc5982822aa696eb566ed9e1e1ee HEAD` produced no entries: no tracked
baseline file was modified, deleted, renamed or type-changed at the reviewed
head. The review itself adds only this report, its small checker and fresh
run evidence. `git diff --check` also passed.

Recommendation: accept the conditional resource lemma, source audit and
bounded evidence for integration into the research branch. Do not designate
this as complete certificate acceptance or use it to delete existing
certificates. No automatic merge or production replacement is recommended.
