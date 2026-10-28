# Fixed-target manuscript integration — 28 October 2026

The requested deliverable is the manuscript itself, not another companion
note. `main.tex`, `main.pdf` and `source-arxiv-v1.zip` now present the selected
fixed-target approach. The review draft has 89 pages, compared with 158 before
this integration. This is a comparison of manuscript lengths, not a bound
on the length or cost of a future complete proof. In particular, old finite-base
candidates are preserved outside the compilation and their open obligations
have not disappeared.

The editorial starting commit is
`924e6160bee44ed3a50eba35f7dbb8dcd5b9a9c7`. The immutable reference baseline
is `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`. Component branches separate
foundations, resources/confinement and independent composition review. Their
reviewed results are integrated for existing draft PR #5 in the user's fork.

## What the manuscript actually proves

| Statement | Mathematical status and scope | Execution evidence |
|---|---|---|
| Fixed-n fixed-target maximizer and compact contact support | Full analytic proof for c>0, including moving closed thresholds, reflection and equality; higher moments only after compact support | Earlier finite-law identity controls retained; new source/composition review |
| Conservation with off-contact residuals | Full identity retaining the support Lebesgue integral and `(n+H^2)a`; nonnegative defect resource specialized to c=CE | Earlier exact algebra/atom controls retained; independent source derivation reviewed |
| Selected entry and signed resources | Complete analytic implication under true predecessors, external Shevtsova input and the stated finite gates/covers | Existing v7 isolated acceptance and v8 phase/moment replays retained; not rerun by this editorial task |
| Continuous low-noise confinement | Full conditional proof from an incoming .6 strip and inward displacement below .072; abstract p in [.4,.6], acquired application [.40,.53], lambda<=.075, all H and n>=42 | Existing exact 28 endpoint/domain gates and independent reconstruction retained |
| Full acquired-noise confinement on [.41,.42] | Complete conditional proof using the same resource, both deleted indices, correct strict/closed events and all support rays | Existing complete 128-box acceptance: 16 heat, 84 exclusions, 28 two-ray comparisons |
| Exact counts and scalar harmonic estimates | Full conditional identities/estimates, with probability, phase, interior-count and positivity domains retained | Fresh independent exact scalar calculation: 80 and 896 Bernstein coefficients; false K=4.5 control rejected |
| Four-summand original-law bridge | Full scoped analytic implication, including closed Prawitz input; not a complete C4 certificate | Earlier algebraic/atom controls retained; no whole-domain numerical acceptance supplied |
| Global sharp inequality | Conditional composition only; BASE41 and complete local exclusion remain open | No full native or Lean acceptance; no certificate-generation campaign |

## Analytical coverage and dependency decisions

The detailed source/line correspondence and edge hypotheses are in
`v9-foundations-coverage.md`, `v9-confinement-coverage.md` and the retention
matrix in `v9-independent-review.md`. The actual proofs, rather than just
those reports, are included in the TeX sources below.

1. **Fixed-target core.** `sections/02-fixed-target.tex` proves attainment,
   contamination contact, compact support, reflection, the zero-excess
   endpoint and the complete zero-bias conservation identity. The unknown
   attained ratio is no longer an entry input. Its removal does not follow
   from renaming a multiplier: the new coefficient is the fixed c, and
   the excess has coefficient `n+H^2`. The source includes the off-contact
   residual `n^(3/2)(B-H xi)` before setting it to zero under contact.
2. **Fourier replacement.** `appendices/fixed-fourier.tex` proves compensated
   inversion, the full triangle sixth-order LOW estimate and all six HIGH
   terms, with actual iid events, comparator tail and every positive-decay
   and inverse-index gate. It therefore supplies the selected Fourier edge
   without the old anchor/profile/rectangle atlas. These are alternative
   complete bounds; no term of the selected integral is simply discarded.
3. **Ordered entry.** `sections/04-fixed-entry.tex` includes the initial
   moment/support acquisition, complete heat remainder, sign moments,
   localizing inequalities, actual event before the gap, two quadratic
   passes, actual-gap event and four signed passes. Its final finite cover
   remains explicit. The degree-six phase routine and six intermediate
   HIGH updates are not ancestors of this route. The 11,264 versus 239,616
   signed evaluations compare the coarse component only, not total proof
   size or measured runtime.
4. **Same-law resource.** `sections/06-fixed-resources.tex` proves the binary,
   inward and noise charges from the actual conditional laws, their ordered
   moment contraction, the correctly oriented signed third-moment bounds
   above and below one half, and the weighted nD inequality. The signed
   phase refinement obtains a raw bound before licensing a density bound
   and a new phase price. Each intersection uses already established
   necessary conditions; independently optimal moment allocations are
   never combined as if they came from one law.
5. **Confinement.** `sections/07-fixed-confinement.tex` includes the full
   continuous low-noise argument: one folded quintic, all derivative signs,
   fixed-moment radial continuation, both physical rays and zero noise.
   Its heat estimate cites the general four-remainder proof in the entry
   section, whose domain includes this use; the large-radius optimization
   is not imported. The high-noise derivation re-establishes contact slopes,
   antichain constants for both deleted indices, signed deletion, endpoint
   atom conventions and one shared resource simplex at floor 42. The old
   floor-47/.55-strip theorem is not cited with changed hypotheses.
6. **Counts retained.** `sections/05c-counts.tex`, `sections/07-curvature.tex`,
   `sections/07b-harmonic.tex`, `appendices/count-comparison.tex` and
   `appendices/local42-refinements.tex` retain the full count mechanism.
   Direct subtraction gives

   `a+rho_B(c-C_B)=sqrt(n) pi_k (Q/pi_k-f)+R_c`,

   `R_c=sqrt(n)[Phi(delta/sqrt(nv))-Phi(delta/sqrt(n(v+s)))]+c(rho_B-rho)`.

   This replaces the old ratio-score left side and its repair coefficient.
   Both endpoints of a positive multiplier remain necessary when a signed
   cubic lower bound can be negative. The old numerical 45+47-row schedule
   is not an acquired cover for the new domain and is absent from the
   compilation. In particular, p<1/2 hypotheses in the one-sided count
   recipe are not extended to .53 by the confinement result.
7. **Finite base kept independent.** `appendices/half-line-smoothing.tex`
   contains the complete closed Prawitz construction needed by
   `appendices/original-law-four.tex`. The latter retains one common
   original-law defect measure, actual fourth-power remainder, midpoint
   reserve, threshold interpolation and reflection. It does not replace
   the missing BASE41 with a two-point relaxation or with a proof label.
   Old finite-analysis/support/uniform-bridge sources remain in the repo;
   their removal from the selected compilation is not their acceptance.

The proof guide introduces the main quantities and the licensed order of
operations. The literature review and checked bibliography are retained.
Implementation history, run paths and per-cell logs are kept in review
documents rather than interrupting the mathematical exposition. The
manuscript still states exactly which arithmetic conditions are needed and
distinguishes mathematical status from execution status.

## Review findings and corrections

The independent composition review found two real transfer defects in
intermediate drafts. Both were corrected before the delivered build:

- The count increment lower bound `1-d` is now consistently named zeta,
  separate from fixed c=CE. Joined terms such as `cr`, `cj`, `ci`, `cR`
  were corrected to their increment versions; distinct variance/mass
  coefficients were restored. Both the master identity and signed repair
  use the fixed target, not the unknown actual ratio.
- Extending the abstract harmonic span theorem to b<1 did not justify the
  old numerical recipe `sin(3.14159 b)`. For b>1/2 its direction is wrong,
  and squaring a negative polynomial is invalid. The final proof folds
  `y=min(b,1-b)`, uses `sin(pi b)=sin(pi y)`, and explicitly proves positivity
  of the degree-seven lower polynomial before squaring. The denominator
  remains b squared.

The guide also now places the nonnegative resource after the raw license.
The last two-file polish only corrects a Proposition cross-reference and
the remaining local-step notation. The reviewer independently confirmed
the exact cosmetic deltas and refreshed both source hash pins.

The scalar checks use exact Fractions, independently construct the affine
pullback/Bernstein coefficients, and derive directed pi bounds from Machin's
formula. All 80 coefficients exceed .04492; all 896 exceed .000123.
The false K=4.5 majorant is rejected. This is a genuine negative control:
at x=3/8 the ratio `(1-cos(2*pi*x))/x=(8+4*sqrt(2))/3` exceeds 4.5.
These checks discharge two specific scalar obligations, not a count cover.

## Final document validation

The evidence directory is `runs/manuscript-v9-20261028/`.

- `build04/receipt.json`: TeX Live compilation returned zero; 89 pages;
  no final reference, layout or other logged warnings. Versions, command,
  source hashes, return codes and stdout/stderr are retained.
- `build04/sources.stdout.json`: 20 active TeX files including main,
  259 unique labels, 132 distinct reference targets, 32 cited works and
  37 bibliography entries; no missing input, citation or duplicate label.
  The independent reviewer separately counted 196 reference occurrences.
- `build04/scalar.stdout.json`: both exact coefficient checks and the
  negative control passed. Earlier v7/v8 proof acceptance was not rerun.
- `visual-review.json`: all 89 pages inspected in overview sheets, selected
  formulas at higher resolution, then all three pages affected by the last
  cosmetic edits inspected again. The other 86 rendered PNGs are byte-identical
  to the inspected preceding build. No clipping or overlap was found.
- `export01/receipt.json`: the selected source archive was extracted to a
  fresh temporary directory and compiled with shell escape disabled. All
  three passes returned zero and all 89 page texts match the delivered PDF.
  The only final package notice says shell escape is not enabled, as intended.
- `preservation.stdout.json`: all 2,748 original baseline entries remain
  unchanged: 182 materialized byte checks and 2,566 sparse tree/index
  bindings. Nine inactive historical manuscript sources are byte-identical
  to the editorial starting commit. No promisor download was requested.

Build01's two overfull displays were corrected; build02 preceded the successful
polish; build03 was clean. Final build04 incorporates only the independently
checked cosmetic changes. Their receipts remain distinct rather than being
rewritten as final results. Full generated build trees and page renders remain
locally reproducible; the delivered PDF, archive, logs, receipts and final
overview sheets are the review artifacts.

## Remaining work and recommendation

The independent review found no remaining mathematical transcription or
dependency blocker **at the stated component scopes**. Some of the reviewer's
earlier contributions are expressly excluded from any claim of newly
independent verification. Source review, arithmetic replay and formal proof
are distinct evidence types.

The manuscript is ready for human review as an account of conditional
research progress. Keep the PR in draft. It is not yet ready for submission
as a completed proof of the conjecture: complete confinement outside the
central panel, the strict relative-noise count comparison on the actual
domain, its endpoint/zero-noise treatment, and a genuinely closed finite
base remain to be proved. There was no merge, main push, force-push, branch
deletion, upstream modification or expensive certificate campaign.
