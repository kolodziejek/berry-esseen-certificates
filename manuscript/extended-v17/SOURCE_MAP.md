# Proof route and source correspondence

The compact starting point is `manuscript/compact-v16` at commit
`41a6e22d521162d649d09068cb308fd7cc21bddf`. The earlier finite proof sources
are pinned at `3d053204f30eab39da39bfb7b85e380d83ec0646` in the
`rodziewiczk/berry-esseen-certificates` repository. Both are retained unchanged.
The extended manuscript is self-contained at the level of its continuous
arguments; its numerical claims use the accompanying reproduction package.

Read [PROOF_DEPENDENCIES.md](PROOF_DEPENDENCIES.md) for the precise hypotheses
and execution status of each implication. Paths below are relative to this
directory; LaTeX labels remain stable when page or theorem numbers change.

| Source | Role |
|---|---|
| `main.tex`, `sections/01-introduction.tex`, `sections/01b-guide.tex` | All-index statement, central idea, proof diagram, certificate explanation and notation. |
| `sections/02-fixed-target.tex` | Fixed-target attainment, compact support, contact and reflection; ratio attainment at `c=C_n` for the finite induction. |
| `sections/02b-moment-domain.tex`, `sections/05-geometry-counts.tex` | Signed moments, nonnegative support-gap defect, its equality case, one common resource budget and exact Bernoulli/noise coordinates. |
| `sections/03-conservation.tex` | Both evaluations of the zero-bias integral and the conservation identity. |
| `sections/04-fixed-entry.tex`, `sections/07-direct-acquisition.tex`, `sections/08-direct-comparison.tex` | Retained compact localization and strict comparison for `n>=700`, assuming a sharp predecessor. |
| `sections/06-one-step.tex` | Universal smoothing recurrence; exact first-failure bounds from 25,40 and42. |
| `sections/06a-small-cases.tex` | Indices1–3, quantitative C3, and the unrestricted four-summand localization/physical comparison. |
| `sections/06b-finite-counts.tex`, `sections/06c-count-domain.tex` | Conditional count identity, strict outgoing and closed incoming events, and the common-law domain supplied to COUNT certificates. |
| `sections/06h-finite-five-fourteen.tex`, `sections/06i-five-summand-assembly.tex` | Induction5–14, complete five-summand signed assembly, actual-index support/Fourier/resource/COUNT interfaces. The second file is included by the first. |
| `sections/06g-finite-fifteen-thirtynine.tex` | Induction15–39, weighted floor transfers, explicit excluded panels and actual35–39 charged-score comparisons. |
| `sections/06d-floor40.tex` | Actual40–42 comparisons with actual-index binomial probabilities. |
| `sections/06e-finite-bridge.tex`, `sections/06f-local-engine.tex` | Finite LOCAL42–48 and uniform LOCAL47, followed by the first-failure composition. |
| `sections/09-composition.tex`, `sections/10-discussion.tex` | Sharp upper bound for every index, strictness from700, global sharpness and the scope of computation. |
| `appendices/fixed-fourier.tex`, `appendices/normalization.tex`, `appendices/off-contact.tex`, `appendices/entry-details.tex` | Complete retained compact analytical estimates, exact constants and entry calculation. |
| `appendices/finite-soundness.tex`, `appendices/four-summand-details.tex` | Tensor/closed-domain acceptance soundness and the full four-summand physical comparison. |
| `appendices/direct-gaussian-support.tex`, `appendices/five-summand-support.tex`, `appendices/support-six-fourteen.tex` | Contact-based support bounds, including every complementary6–14 support interval and both exterior threshold rays. |
| `appendices/finite-fourier.tex`, `appendices/finite-small-refinements.tex`, `appendices/finite-sine.tex` | Common moment/Fourier calculus, small-index refinements and the direct resource-to-sine implication. |
| `appendices/finite-count-filters.tex`, `appendices/sign-mass.tex`, `appendices/inward-scalar.tex`, `appendices/finite-acquisition.tex` | Moment, probability and signed quadratic constraints used by finite acquisition and COUNT acceptance. |
| `appendices/floor-transfer.tex`, `appendices/positive-thirtynine.tex`, `appendices/local-estimates.tex` | Weighted index transfer, the necessary positive allowance at39, and complete finite/uniform local estimates. |
| `appendices/reproducibility.tex`, `reproduction/` | Numerical scopes, trusted arithmetic/runtime, source restoration, fresh execution commands and preserved execution records. |

The finite induction proves `C_n<=C_E` through42. At a least later strict
failure the smoothing recurrence gives sharp deleted predecessors, zero loss
and `n(C_n-C_E)<3003/10250<0.3`. LOCAL42–48 excludes43–48 and uniform LOCAL47
excludes every larger index. The resulting weak all-index bound supplies the
predecessor needed by the compact strict comparison. Esseen's fixed skew
Bernoulli limit supplies the matching global lower bound.

The former compact-only source map and early integration notes are preserved
under `reviews/compact-source-map-20261030.md` and
`reviews/extension-integration-working-notes-20261030.md`. Other earlier
editorial/audit records retain their original dates and narrower scopes.
Their old pending statements are historical records, not the status of this
extension. No eventual two-point optimality or proof-assistant formalization
is claimed.
