# A shorter acquisition-to-comparison chain at n >= 700

This audit establishes a new post-entry theorem, not merely a reorganization
of the old diagram. Starting from a compact standardized law and the single
bound `nD <= 32.20665378`, it derives an actual central gap, then

```
.375 < p < .465,   theta < .0036,   d < .004,   ell > 1.996,
rho < 1.125,       .066148 < beta < .2527,
lambda < .35,     and lambda < .32 when p <= .4.
```

For a nonnegative attained fixed-target witness with a true sharp predecessor,
**two whole-ray contact checks** then give the common conditional amplitude
`.6` on this entire interval. No downstream probability panel is used.
The final `.6` bound is stronger than the `.7` left amplitude needed by v15.

The full proof is `acquisition-direct.tex`. The scalar checker imports no
constructor or panel export. The mathematical conclusion is conditional only
where explicitly stated below. The predecessor/entry hypotheses are not
removed by the fact that the final comparison has no such premises.

## Results and evidence

| Item | Mathematical status | Execution status |
|---|---|---|
| Scalar acquisition from compact law, n>=700, nD<=32.20665378 | Locally derived; direct proof displayed, no old numerical geometry assumed | Fresh exact gate checks and actual-law controls |
| Common `.6` strip from the two new boundaries | Locally derived conditional on the retained contact and all-threshold heat lemma | Fresh exact boundary and full-ray continuation gates |
| Composition into the baseline v15 acquired-witness exclusion | Direct domain implication from the two stated local union theorems | Exact endpoint/normalization joins; old count constructors not rerun |
| Attainment/contact, conservation, initial support, Fourier reduction | Supplied analytic proofs with earlier reviews; retained inputs, not independently re-proved in this audit | Source locations and hashes recorded; no new claim of full replay |
| Complete two-coarse/four-signed entry certificate | Supplied finite conditional input to its stated analytic reduction | Historical acceptance retained; 11264-box calculation not rerun here |
| External Shevtsova and Schulz theorems | External theorem inputs with the manuscript's stated scopes | No new literature verification in this bounded audit |
| Finite base, unrestricted rows, unconditional cutoff700 | Not established | Not claimed |

`check02` is the final exact run. It checks 63 rational scalar predicates,
including two broad probability exclusions, both refined probability endpoints,
all square-root directions, the two contact boundaries and their outward-ray
signs, and both noise ceilings. There is no parameter subdivision. Twenty-four
actual finite laws are checked in exact Q(sqrt(10)); twenty satisfy the geometric
budget and therefore must satisfy the new conclusions. Three negative controls
are described below. The source and evidence are separately pinned.

## Minimal theorem contracts

These are the smallest contracts established in this audit. They are not
claims that no different mathematical approach can be shorter.

**F: oriented fixed-target witness.** At a fixed index n>=700, take a maximizer
of `sqrt(n)(P(S_n<=H)-Phi(H/sqrt(n)))-C_E rho` with nonnegative value and
true predecessor `C_(n-1)<=C_E`. The closed-support contact equality and
compact support must hold. No hypothesis about the maximizing ratio, C_(n-2),
or an order-1/n excess is added.

**E: two coarse outputs for that same law and threshold.** Require the proved
weighted budget `nD<=32.20665378` and raw `|H|<=1.83605680`. The selected
fixed-target entry theorem supplies E under its full existing conditions.
The meaning of D is unchanged: `(3+sqrt(10))*rho-gamma-3J`, with the actual
weighted support-gap sum. A mere small third-moment defect or artificial gap
is not an alternative input.

**G: scalar actual-law geometry.** Compactness, standardization and E's
weighted budget imply Theorem 1 of the new proof. It acquires its own central
gap and sign probability. Its normalization is exactly
`X=ell(B+U-p)`, `E(U|B)=0`, `ell=(pq+E U²)^(-1/2)`, and
`lambda=n E U²=n theta/ell²`.

**S: two contact rays.** F supplies the contact upper expression and retained
heat/ray lemma. Insert only G's `rho,beta,ell,p` bounds. The two constant
physical boundaries are

```
t_minus = 1.996*(.375+.6) = 1.9461,
t_plus  = 1.996*(.535+.6) = 2.26546.
```

They exclude the complete negative and positive rays, including boundary
atoms, uniformly in H. Dividing by the *actual* ell, with its correct sign,
gives `-.6<U0<=a0` and `-a1<=U1<.6`; the inward endpoints sum to d<.004.
Neither an artificial two-point law nor a reflection of the signed budget is
used.

**L: local comparison.** On `p<=.4`, G and S imply every hypothesis of the
v15 left union, including amplitude<=.7, d<=.068 and lambda<=.32. On `p>.4`,
they imply every hypothesis of the right union, including amplitude<=.6,
d<=.072 and lambda<=.36. The raw threshold from E lies in both domains.
At zero noise apply the external strict Bernoulli bound directly. Positive
noise uses the retained small-noise comparisons and the new v15 five-count
proofs. Each concludes negative excess for the same law, index and raw H,
contradicting F.

The logical graph is therefore:

```
positive strict-row failure
  -> [reflection + fixed-target attainment] -> F
true sharp predecessor --------------------> F
external structural bound + F
  -> [initial support + conservation + complete Fourier + two coarse passes
      + four signed passes] -> E
compact support + E.budget -> G
F.contact + retained all-threshold heat lemma + G -> S
E.raw_H + G + S + baseline v15 local union -> negative excess -> contradiction
```

The graph is conditional at the acquisition and predecessor edges. BASE41
only allows the predecessor at a *least* failure. It therefore confines that
first failure to 42..699; it does not establish unconditional bounds for every
later row after a possible earlier failure. A genuine base through699 or an
independent closure of42..699 is still needed for that induction route.

## Source locations and retained hypotheses

All locations refer to baseline `fb9e918bef3b0a932fb44bf1dae8d3e4a589f932`.
Byte hashes appear in `acquisition-sources.json`; hashes verify identity only.

| Edge | Source and location | Exact role and limitations |
|---|---|---|
| Failure -> oriented attained pair | `manuscript/arxiv-v1/sections/02-fixed-target.tex:22` and `:91` | Fixed n and C_E; closed-event attainment, compact support, reflection including the atom correction. Nonnegative excess includes equality. |
| Sharp predecessor -> support contact bound | `manuscript/arxiv-v1/sections/04-fixed-entry.tex:70` | The extra term is `-n a`; it may be discarded only for a>=0. The predecessor is genuinely `C_(n-1)<=C_E`, not a bound by an unknown actual ratio. |
| Initial moment/radius | Same file `:28` | External affine iid inequality `.3031*(rho+.646)`; support acquired before fourth/sixth moments. This remains internal to E. |
| Contact -> positive conserved resource | `02-fixed-target.tex:180`, `:271` | Same actual law/gaps, nonnegative leakage, no missing support integral. Phase price requires a prior raw ceiling; resource is not raw remainder. |
| Complete Fourier enclosure | `04-fixed-entry.tex:207`; `appendices/fixed-fourier.tex` | Both low and high frequency windows, actual event distance/mass and all gates. This audit neither replaces nor reruns it. |
| Two coarse passes | `04-fixed-entry.tex:418`, condition `:490` | 24 closed rho cells, raw license before phase price, actual first central gap. That internal gap remains necessary for later signed passes. |
| Four signed passes -> E | `04-fixed-entry.tex:735`, `:834`, condition `:862`, theorem `:889` | 11264 nominal signed boxes, complete cover and all necessary-condition exclusions; same-law nD and raw-H outputs. |
| G's integral algebra | `mathematics/simplification-v10/2026-10-28/geometry.tex:36` | General common-cost inequality, rederived in the new proof. Its numerical global/panel outputs are not invoked. |
| G's cubic/noise algebra | `mathematics/simplification-v13/2026-10-28/geometry-noise.tex:51`, `:78` | Centered one-sided cubic bound and actual allocation budget, rederived here with dbar=.004. Its old scalar domain/table is not invoked. |
| S's heat/ray envelope | `04-fixed-entry.tex:98`, `:146`; `06-fixed-resources.tex` subsection “Acquiring the incoming strip” | All n>=42, all raw thresholds, exact contact signs. Eight tests per ray include coefficient sign before replacing C_E by its lower endpoint. |
| Comparison join | `mathematics/simplification-v15/2026-10-28/join-review.md`, section1 | Right n>=200 versus left n>=700; different shifted/floor anchors are allowed because their conclusion concerns the same excess. |

The new proof does not assert an independent re-verification of the complete
fixed-target foundation or the Fourier inversion theorem. It states the exact
inputs it consumes and supplies the new implications in full.

## Dependencies that can be bypassed, and why

The following removals are **from the n>=700 post-entry route only**. Existing
sources/certificates are preserved, and their smaller-index uses remain.

| Old work | Why it is unnecessary on this route |
|---|---|
| v10 numerical global geometry: four quartics, two cubics and its p>.25/theta/d/lambda/rho outputs | G starts before those outputs and bootstraps from D<.047, with no inherited p interval or numerical radius. |
| v10 one-pass export on all30 nonempty panels and old eight-round contraction | The new proof has one interval and direct theta,d,rho bounds; it consumes no per-panel D, beta, gap or joint-noise export. |
| v10 thirteen `.6` right-strip tests and v11 fifteen wider left-strip tests | S uses exactly two fixed physical boundaries and establishes `.6` on the whole surviving interval. The old strip-panel decomposition is not used. |
| v13 four numerical noise ceilings/139 Bernstein coefficients and six index-table exclusions | Its general actual-law budget with dbar=.004 is enough; three rational square-root bounds give lambda<.35 and left lambda<.32. No degree-eight polynomial is needed here. |
| Separate p<=1/3 and p>=.53 exclusions in the v15 acquired join | G already places p strictly between .375 and .465. |
| Exported radius3.14 and probability cover[.24,.54] as post-entry inputs | The new geometric theorem requires compactness only. It derives probability and rho without a numerical radius. |
| Central-panel resource triangles, sharper signed-phase resources, half-amplitude confinement, old selected-count transport and its displacement cost | None is an ancestor of G, S or the invoked v15 local unions. Several were already bypassed in v15; they are not claimed as new removals by this audit. |

The **general** gap-cost inequality and one-sided-cubic lemma are retained,
not deleted together with their numerical tables. Likewise the all-threshold
heat lemma and actual contact hypothesis remain, even though the old support
panel computations disappear.

What is not removed:

- The two coarse and four signed entry passes, including their support/event
  and Fourier prerequisites. Their internal use of a central gap and moment
  cells is logically prior to the new budget theorem.
- The old entry acceptor's 100-panel export/coverage checks are still part of
  its supplied proof-object contract. Since global maxima suffice downstream,
  a future *new* acceptor could pool final-cell budget and phase ceilings
  directly, but this audit has not rebuilt or replayed that certificate.
- The baseline v15 small-noise ancestors, including its 291-cell right
  negative-inner certificate and LEFT-01, remain for this baseline composition.
  Separate v16 comparison work may replace them; no unfinished result is
  assumed here.
- Raw-H acquisition. The support rays are uniform in H, but the comparisons
  are not. A small D alone does not license replacing the raw-H bound.
- The sharp predecessor, contact, attainment and reflected-law selection.

The first three signed-pass global nD ceilings, read from the preserved
entry proof object, are 77.51258466, 58.80363006, and 34.22831118. They are not the
selected 32.20665378 contract. In particular, the third-pass budget alone does
not certify the selected final raw-H ceiling. No pass is silently omitted.

## Adversarial checks and execution limits

The actual-law tests construct standardized two-, three- and four-point
marginals at n700 and n1400, with zero noise, noise10^-12, one-sided allocation,
and split conditional allocation. The exact support-gap sum J is recomputed
from the actual sorted atoms, not inferred from a desired geometry. Exact
Q(sqrt10) comparisons verify the budget and common-cost inequality; an eligible
law must satisfy every new geometric output. The four budget-ineligible cases
are retained and labeled, rather than accepted or discarded as impossible.

The three negative controls are:

1. `n=700,p=.42,lambda=10^-6`, with all noise on the negative conditional side
   and a rare atom at `U0=-.8`. It satisfies nD<=B* and the old radius3.14,
   yet violates amplitude.6. Therefore contact cannot be erased from S.
2. A Bernoulli law at `n=42,p=.3` satisfies nD<=B* but violates p>.375.
   Therefore the large-index premise cannot be erased from G.
3. The reflected Bernoulli law with p=.58 fails the same signed D budget.
   Reflection must reacquire the oriented witness; it does not preserve E.

These controls refute stronger intermediate implications, not Berry–Esseen.
No Fourier replay, certificate-generation campaign, external publication,
old-file edit or manuscript edit was performed. The discovery prototype uses
floats only for diagnostics; final acceptance uses exact rationals and field
arithmetic. The full analytic reductions, not sampled controls, supply the
continuous domains and countably-many-gap argument.

Final reproduction: `python3 mathematics/simplification-v16/2026-10-29/acquisition-check.py`.
The four-page proof compiles cleanly in build02; all final pages were visually
inspected (unchanged pages1–2 by exact render-byte comparison).
Final proof SHA-256: `c996f20f2202def6fb945f6e7c809a0517930a1a97402e1d11aedd840f88a6fd`.
Final checker SHA-256: `e5513d294a2564f350e17d2d581a8d2033ce7832e8a55e23219bfb479a3c910d`.
