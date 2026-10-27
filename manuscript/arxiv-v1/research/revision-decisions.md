# Editorial revision and disposition of the supplied proposals

27 October 2026. Starting manuscript commit:
`ec370aadc459460e75ffd6d8d3b7b1f9f8a9cb13`. Integration branch:
`manuscript/editorial-v2-20261027`. Separate branches were used for the
literature/independent review, conserved-identity derivation, and finite
appendix work. The result updates existing draft PR #3 in the user's fork.

The six supplied files were read as suggestions for judgment, not as
instructions authorizing changes to proof scope, authorship or publication.
Their original SHA-256 hashes and sizes are in
`runs/manuscript-v2-20261027/integration01/attachment-provenance.json`.
The proposed PDF has 168 pages; its opening pages and guide were inspected
alongside the supplied TeX and revision instructions. The proposals were
not copied wholesale into the manuscript.

## Changes made for readers

- Rewrote the abstract around the mathematical route and the actual
  conditional conclusion. The introduction now moves from the classical
  problem and extremal Bernoulli example through the relevant literature
  to the contributions of this paper.
- Added a guide to the argument, a dependency diagram, and a notation
  table. The guide states the exact smoothing recurrence and explains why
  a near-two-point comparison needs errors relative to the conditional
  noise variance.
- Moved the sharp third-moment domain proof from an appendix into the
  extremizer section. Its proof is preserved verbatim apart from whitespace.
- Reorganized support estimates as three reusable moment-to-support bounds,
  followed by the conditional 65-invocation consequence. The ordered moment
  assumptions remain explicit.
- Added the oriented equality case of the physical defect. Its proof shows
  that zero defect forces exactly the standardized Bernoulli law with
  `p=(4-sqrt(10))/2`; reflection is not another zero of this signed defect.
- Promoted the full integrated contact identity into the main narrative:
  gap integration, zero-bias evaluation, compensated hinge inversion,
  absolute convergence, endpoint conventions, and the complete remainder.
  The following resource derivation retains both positivity gates needed
  to remove the Gaussian weight and charge the phase term.
- Put conditional counts and discrete curvature together. Moved common-law
  expectation, Bernstein conversion and closed-cover soundness to the
  certificate section, where the reader needs that interface.
- Deduplicated shared Gaussian comparisons, the moment-domain exposition,
  the physical-defect setup and the finite appendix's common sign split.
  Kept the high-precision pi recipe where its tighter endpoints are needed.
  The detailed replacement map is in `revision-finite.md`.
- Kept every unique Fourier-atlas argument. A short navigation paragraph
  now explains the atlas's stages; a repository pointer does not replace
  its analytic content. The atlas and tail match the previous draft modulo
  decimal typography, whitespace and one updated reference sentence.
- Added a truthful finite-index roadmap, distinguishing individual helper
  domains from an unproved complete cover through 41. Improved transitions
  and removed repetitive audit commentary from the main argument; the
  verification section retains the full distinction between proof and run
  status.
- Distinguished the physical noise `W` from the count-noise sum `V_j`, the
  threshold `xi=H/ell` from the reciprocal span, and the strip width from
  `sqrt(10)`. Added leading zeros to decimals and repaired concatenated prose.

## Proposals corrected or declined

| Proposed change | Decision and reason |
|---|---|
| Paired weights `(4 minus/plus sqrt(10))/2` | Incorrect: those weights do not sum to one. Use `p=(4-sqrt(10))/2`, `q=1-p`. |
| Normalized smoothing error of order `n^(-3/2)` | Incorrect: `sqrt(n)/(n-1)^(3/2)` has order `1/n`. The guide states the exact recurrence. |
| Calling contact a cubic polynomial | It contains `abs(y)^3` and is piecewise cubic. The support argument only needs its growth on both rays. |
| Exact count identity guarantees a relative-to-noise error | The identity is exact, but uniform relative bounds are separate analytic obligations. |
| All analytic work is proved and only arithmetic remains | Not established. The retained Fourier/finite chain remains a supplied proof candidate; complete BASE41 and uniform LOCAL42 are still open. |
| Radius-floor explanation makes 42 necessary | The displayed crude comparisons also hold at some smaller indices. Forty-two is the floor of the proposed local contract, not a proved optimal floor. |
| Delete about 1,300 lines of the coefficient atlas | Declined because they include unique analytic estimates. Navigation and genuine deduplication improve access without hiding proof obligations. |
| Present the late finite tools as a cover of all 6--41 | Declined. They retain their individual actual-index domains and conditional composition. |
| Add all proposed bibliography entries | Added six relevant verified references. Corrected Shiganov's DOI/pages and Hipp--Mattner's English publication year; omitted unverified early numerical milestones and irrelevant background inflation. Details in `revision-literature.md`. |
| Invent fixed certificate labels as a complete acceptance contract | Declined. A small naming table would not establish domains, providers, coverage or implementation semantics. |
| Affiliations, contact details, or vendor-specific AI history from the template | Omitted, following the authors' explicit instruction and the actual available provenance. AI assistance and author-supplied model suggestions are disclosed. |

## Mathematical review

| Result | Mathematical status | Execution status |
|---|---|---|
| Promoted slack/conserved identity and compensated inversion | Independently rederived under the displayed contact and moment hypotheses | Exact symbolic coefficient checks and six false-rule controls pass |
| Gaussian unweighting and phase charge | Conditional implications with both sign gates retained | Sign controls pass; no particular resource row accepted |
| Zero-defect classification | Independently checked for compactly supported standardized laws, in the fixed orientation | Analytic derivation; no optimization required |
| Prior scalar/support/resource/curvature reductions | Preserved at their previously reviewed scopes | Earlier bounded receipts retained; no claim of a new full replay |
| Complete finite base, uniform local exclusion, entire retained analytic chain | Still conditional or supplied proof candidate as recorded in Section 7 | No full native replay or end-to-end acceptance |

`revision-independent-review.md` independently derives the two slack
integrals, hinge signs and normalization, conserved identity, equality
case, and scope of the least contrary index. It also gives a compactly
supported centered example with `gamma+3J<0`, showing why positivity
cannot be inferred merely from `D>=0`. That example challenges an omitted
hypothesis, not the Berry--Esseen conjecture.

No blocker was found in this bounded mathematical review. This is not a
review of every coefficient atlas or every finite proof provider. The
inclusion of the full analytical appendices makes that further review
possible; it does not assert its completion.

## Integration and delivery checks

- Every one of the original 462 labels is retained; the revised project
  has 474 labels, 266 distinct references, 35 cited works and 37 available
  bibliography entries across 20 included TeX files. All references and
  citations resolve.
- All 2,748 immutable-baseline entries preserve their modes/object identities;
  none is modified in the working tree. Certificates and production sources
  are unchanged.
- Exact rational checks justify the shared stronger Gaussian lower bound.
  Source comparison confirms the moved moment proof and retained atlas.
- The first build exposed a missing TeX token delimiter in the renamed strip
  width. This was corrected; its failed diagnostic is preserved in build01.
  Build02 completed with no warnings, undefined references or box warnings.
- Every page of build02 was rendered. The main text, diagram and tables were
  inspected, and independent reviewers covered the promoted identity,
  Fourier appendices, finite appendices and bibliography. Full-page equation
  checks found no clipping, overlaps or glyph problems. The reviews prompted
  two reference-wording corrections and five leading-zero corrections.
- Final TeX Live and desktop compilation succeeded. The portable ZIP was
  rebuilt with shell escape disabled; all 164 pages match the delivered PDF.
  Final TeX Live diagnostics have zero warnings; the isolated rebuild has
  only the expected disabled-shell-escape notice. All four pages changed
  after the initial visual review were rendered again at 120 dpi and
  inspected. Details and hashes are in
  `runs/manuscript-v2-20261027/final01/verification.json`.

The recommendation is to keep PR #3 in draft for author and mathematical
review. The revision is a clearer research manuscript, not an unconditional
proof or a publication-ready acceptance of the whole source chain. No
arXiv submission or merge was made.
