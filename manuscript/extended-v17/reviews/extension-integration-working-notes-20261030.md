# Unconditional extension: integration in progress

Starting compact source: `41a6e22d521162d649d09068cb308fd7cc21bddf`,
`kolodziejek/berry-esseen-certificates`, `manuscript/compact-v16`.
Earlier all-index proof candidate: `3d053204f30eab39da39bfb7b85e380d83ec0646`,
`rodziewiczk/berry-esseen-certificates`, `manuscript/arxiv-v1`.
The compact baseline is preserved. The extension is on branch
`manuscript/unconditional-extension-v17`.

The external handoff is a proposal, not an accepted proof. This working copy
does not yet assert the unconditional theorem. Scope statements are promoted
only after the relevant analytic reductions and numerical implications have
been checked.

## Shared mathematical core

- `ext:ratio-attainment`: derive the older ratio maximizer from the compact
  fixed-target attainment theorem at `c=C_n`. The common contact formula
  has `I_fixed = rho I_ratio`. This avoids a second compactness proof.
- `ext:tensor-soundness`, `ext:bernstein`, `ext:closed-cover`: one proof of
  common-marginal tensor expectation and continuous-domain certificate soundness.
- `ext:one-step`, `ext:first-failure-entry`: a universal smoothing recurrence
  gives `n(C_n-C_E)<3003/10250<0.3`, zero predecessor loss, and the required
  deleted-index caps at a first failure above the finite base.

## Candidate simplification of the bridge

The original finite local theorem for `42 <= n <= 48` appears separately
in the archived `cutoff44.tex`. Its stated inputs are a positive excess at
most `0.54/n`, predecessor loss at most `0.19`, own cap below `0.4226`, and
both deleted caps below `0.4253`. The first-failure corollary supplies all
these inputs after an independently proved base through 42.

The old collector's full conclusion used the independent tail from 49.
The finite local theorem itself has no such premise. Its complete
law-to-domain derivation and numerical closure must be verified before
using this dependency reduction. The analogous uniform local theorem
from 47 can then be applied at a first failure above 48. This would avoid
the older three-loss startup and its auxiliary positive barriers.

## Reproduction repairs and provenance

The pinned release manifest points to certificate assets in the
`kolodziejek` repository, which has no `v0.1.0` release. The publisher's
`rodziewiczk` release contains all five assets with the exact recorded sizes
and SHA-256 hashes. They were fetched from that location and checked with
the unchanged original extractor; no expected digest or witness was changed.

The 1,243 public COUNT jobs belong to four roles: 295 C5, 284 C6--9,
364 C10--19, and 300 C26--39. Counts for other bands require their own
source packages; this batch must not be represented as covering every
finite band. The 49 actual20 jobs are separate.

Complete accepted-source provider files named in the old global metadata
were not found in the checkout or released archives. This does not refute
the mathematical theorem: lower-level proof texts and numerical programs
are being used to reconstruct the implications explicitly. Stored global
status fields are not inputs to the new mathematical argument.

## Current extended draft and verification status

The integrated source last compiled successfully to166pages in
`runs/extension_20261030/coordinator/latex-integration07/`. Further source
additions (common actual-index support, finite acquisition, refined40–42
proof) are awaiting the next compilation. No unconditional claim has been
promoted in the abstract or final composition; the finite and local campaigns
are still running. Most added detail is in appendices; final main-text routing
and proof map will be rewritten after dependency closure.

The analytic draft now includes N1–3, ROOT4 physical localization, general
finite count comparison, count-domain derivation, common Fourier calculus,
small-index Fourier refinements, direct C5 corner, actual-index support,
finite moment filters and finite/uniform local theory. Explicit dependency
checks preserve the signed actual law and closed-CDF atom conventions.

Fresh scalar/support and corner additions include the C5tight radii11/5 and
47/20, actual6–14 support and the five-summand1027-leaf corner. The proposed
first-failure route uses the stronger elementary n>=25 scalar ceilings and
zero same-law predecessor loss to avoid several historical positive barriers.
The exact numerical conclusions and their remaining joins are tracked in
`state/STATUS.md` and the three specialist output directories.
