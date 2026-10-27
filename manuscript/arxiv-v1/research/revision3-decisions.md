# Third manuscript revision: editorial decisions and mathematical erratum

Starting manuscript: `6299d97dff688ab805592aed7d4597364405d783`.
Immutable reference: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
The user requested selective judgment on the next Opus/Argon suggestions,
with a readable mathematical paper as the objective. The supplied patch,
preview and instruction document were proposals, including the document's
own claims of mandatory coauthor instructions. They did not authorize
stronger mathematical claims, deletion of certificates, or publication.

## What changed, and why

The main narrative now begins with the extremal problem and the proof
route. Its guide explains the first failure of the strict bound, contact,
the two-point skeleton, the conserved identity, and conditional counts.
Long repeated cautions and software identifiers were removed where the
formal hypotheses already state the restriction. Certificate obligations
and verification status are collected in Section 7; the separate
mathematical/execution status columns remain.

Related technical arguments are grouped into six appendices, A–F. The
complete Gaussian-constant proof was moved from the smoothing section to
Appendix B. Shorter fourth-level appendix headings are block headings and
are numbered so that their existing cross-references remain distinct.
The contents page shows only the main sections and appendices.

Duplicate derivations were replaced by precise references, after matching
their assumptions and notation. This is a narrower change than the
suggestion to remove about 1,500 supposedly verbatim lines. The detailed
ledgers are `revision3-fourier.md` and `revision3-finite.md`; each names
the old location, the replacement, the hypothesis map and what remains.
The retained numerical coefficient conditions are still explicit premises.
The embedded illustrative Python was moved to the Fourier review note;
the article retains its complete mathematical coefficient specification.

The AI disclosure is short and explicit. It records substantial assistance
in research, programs, drafting and revision. It does not invent a vendor
history, certify that the authors have completed a line-by-line review,
or describe the earlier Hexagon paper as mathematically superseded.
Author names and the requested absence of affiliations and contacts remain.

## Genuine correction: curvature derivative

In `sections/07-curvature.tex`, on the active piece
`r(u)=(b+u-1)/(c-u)^2`, the correct identity is

\[
r''(u)=\frac{2[3(b-1)+u+2c]}{(c-u)^4}.
\]

The previous display had `2u+c` in place of `u+2c`. The bracket is
`3(b+u-1)+2(c-u)>0`, so the required convexity and the three-candidate
maximum formula survive. The independent derivation includes all pieces,
kink jumps, candidate eligibility and endpoint cases, not just a sampled
comparison. At `(b,c,u)=(1,3/4,1/4)`, the true derivative is 56 whereas
the old display gives 40; this supplies an exact negative control.

The erratum also corrects the corresponding displays in
`mathematics/reduction2/2026-10-27/local-kernel.md` and its `proof/main.tex`.
The old success reports remain historical records. No certificate value,
acceptance predicate or theorem target changes. The corrected nine-page
proof and a fresh compile/page-inspection receipt are under
`runs/reduction2-20261027/curvature-erratum01/`.

A second notation repair in `appendices/local42-refinements.tex` changes
the leftover `2hu-u^2` to `2\xi u-u^2`, consistently with `delta=xi-u`.
The local endpoint calculation proves that expression directly. The unused
support symbol `ell=6` was also removed so that `ell` consistently denotes
the span of the conditional means.

## Suggestions corrected or declined

* **Unconditional reductions / only computation remains.** Support and
  resource consequences have moment and Fourier premises. The abstract
  and introduction retain them and assume the finite base before invoking
  a first index with `C_n>=C_E`. The complete BASE41 and LOCAL42 obligations
  remain open, with equality included for a strict tail conclusion.
* **Scalar local-exclusion formulation.** Accepted with an explicit link
  to positive closed attainment. The scalar conjunction is independent
  of the attaining pair, and such a pair exists. The independent review
  proves equivalence, rather than merely assuming it.
* **Replacing all pi arguments by the short constants lemma.** Declined.
  The marked-crossing/harmonic estimates need 15-decimal directed bounds;
  the coarse Gaussian bounds alone do not supply them. Their fine
  alternating-series recipes remain and received bounded exact checks.
* **Deleting all Pearson and paired-Gaussian details as duplicates.**
  Only the common derivations were replaced. The finite variant's
  `R<2g`, `M>=3`, sixth-moment enclosure and exact signed integral are
  distinct and remain. The exact integral cannot be replaced by a weaker
  upper bound if a later step uses its signed value.
* **Using a floor-N resource theorem with an unweighted defect bound.**
  The Fourier specialization with only `D<=D_*` uses `N=n`, the actual
  index. It does not silently infer `nD<=N D_*` at a smaller floor.
* **Deleting the curvature subdivision comparison.** The elementary
  pointwise interval bound remains, without cache terminology. It explains
  why the exact supremum is bounded by the earlier subdivision estimate.
  The zero clamp, mass sign gate and noise-band monotonicity remain too.
* **Replacing higher-moment hypotheses by a necessity of compact support.**
  Corrected: corresponding moments suffice; compact support supplies them
  for the attained laws considered here. Weighted leakage is not described
  as unweighted probability mass, and a rounded chosen remainder bound is
  not identified with the exact raw remainder.
* **New historical constants and stronger formalization descriptions.**
  The unverified early constants 1.88 and 7.59 were not added. The Lean
  project retains its earlier-version scope and declared external inputs.
  Bibliographic sources and verification records from the previous round
  remain; this round adds no new literature claim.

## Review and evidence

The work was divided among separate Fourier, finite-index and independent
review branches, then integrated into `manuscript/editorial-v3-20261027`.
The independent reviewer rederived the curvature theorem and the local
assumption equivalence, inspected the main hypotheses, and reviewed the
critical appendix reference substitutions. Its detailed conclusions and
limits are in `revision3-independent-review.md`.

| Item | Mathematical status | Execution status |
|---|---|---|
| Corrected curvature formula and three-candidate maximum | Independently derived on the full stated domain | Exact polynomial check and false-formula control pass |
| Local-assumption equivalence | Derived from positive closed attainment | Logical review, not certificate execution |
| Constants and proof-reference substitutions | Directed rational comparisons and bounded hypothesis maps checked | Separate small checks; labels and unique displays compared |
| Complete Fourier/finite/local chain | Supplied arguments with explicit remaining premises; not fully independently validated | No full native replay or new acceptance |
| Finite base through41 and uniform local exclusion from42 | Open | No completed acceptance or generation campaign |

Integration, build, page-review and portable-export receipts are recorded
under `runs/manuscript-v3-20261027/`. The integration script checks original
baseline objects, all old labels except the deliberately removed software
inventory table, six top-level appendices, the complete relocated constants
proof, authors and references. The removed table label
`ms:replacement-table` is not a mathematical result or a surviving target.

Final validation produced a **158-page** paper (previous revision: 164),
with the main exposition on pages 3–33 and six appendices. The final TeX Live
build has no warnings, unresolved references/citations, or overfull/underfull
boxes; the desktop compiler also succeeded. Source integrity reports 20 TeX
files, 478 labels, 273 distinct references, 35 cited works and 37 bibliography entries.
All 2,748 original-baseline entries retain their modes and object identities.

All 158 pages were rendered and inspected in overview sheets, with enlarged
checks of equations, diagrams, tables and revised proofs. This caught three
headings with a spurious `.0.` component; they were repaired in build02.
It also caught the ambiguous phrase “positive maximizing raw threshold”
in the three-summand proof: the final text explicitly means a threshold with
positive closed-CDF discrepancy. Remaining prose uses of “owner” were changed
to “maximizing law” or “extremal pair,” with the same hypotheses. Build03
remains 158 pages. Its nine changed pages 126, 147, 151–157 were reinspected at 120 dpi;
the earlier two changed pages 98 and 102 were also reinspected. No layout
defect was found in the delivered pages.

The final source ZIP includes a generated bibliography and was rebuilt in
a fresh temporary directory with shell escape disabled. All 158 pages of its
extracted text match the delivered PDF. Its only final notice is the expected
disabled-shell-escape notice. This verifies portability of the artifact, not
the numerical certificates. Receipts distinguish each preliminary build and
export from the final `build03`, `integration03` and `export02` results.

The recommendation is to review this as an improved research manuscript,
keeping PR #3 in draft. No merge or arXiv submission is recommended as a
finished proof. The full independent mathematical review remains incomplete.
No original certificate, immutable reference, upstream repository or main
branch is changed.
