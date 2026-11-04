# Revised manuscript and measured shortening experiment

Read [the complete PDF](main.pdf). This revision has **98 total pages**,
including the analytic proofs, certificate explanation and references. It
reduces the preceding 102-page draft by four pages. The requested total of
about 60 pages remains unmet; no essential analytic appendix is excluded
from this count, and the readable typography is unchanged.

The manuscript presents the sharp iid Berry–Esseen bound for every positive
sample size, optimality of the universal constant, and strictness at every
index at least 47. Its status remains a locally derived and reviewed
computer-assisted proof candidate with the stated published inputs. The new
algebra tests and reviews do not constitute independent human acceptance or
proof-assistant verification.

This revision consolidates the paired Fourier argument and index transfer,
removes a duplicated conditional-moment derivation, and replaces finite-range
bookkeeping with one complete region table. The attempted broader algebraic
certificate replacement saved **zero pages** after its necessary mathematical
licenses were included. It is therefore retained as an optional audit outside
the proof's dependencies. [REVISION_REPORT.md](REVISION_REPORT.md) records the
measurements, changes and limitations. [SIMPLIFICATION_NEXT.md](SIMPLIFICATION_NEXT.md)
states the next mathematical target and the result of the structural pilot.

## Read and check

Start with Sections 1 and 8 for the strategy and composition, then Section 2
for extremizers, contact and the nonnegative support-gap defect. Section 4
explains certificate discovery and acceptance. Sections 5–7 give the analytic
reductions and complete numerical interfaces. [PROOF_MAP.md](PROOF_MAP.md)
links those interfaces to the immutable numerical evidence.

The required selected numerical families and their same-law joins were
completed in the earlier work. This revision preserves their targets and
data at commit `c31d0cbe2af867d26871fbae37a3a7f4066f4a55` in
[`../extended-v17/reproduction/`](../extended-v17/reproduction/). It does not
claim a new run of the whole numerical campaign. In particular, the separate
114-command fresh-workspace recipe has not been rerun as one relocated campaign.

The new [coefficient audit](research/coefficient-audit/) checks fixed exact
identities, adversarial inputs and named correspondences with native formulas.
Its portable [prefix replay](research/coefficient-audit/native-prefix/)
matches all 87,963 reached moment-contraction rows, before any Fourier call.
It does not accept the original feedback states or numerical exports.
The [review directory](review/) contains the new bounded mathematical and
layout reviews, build receipts and source mappings.

## Compile

From this directory with a standard TeX Live installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography sources and generated `main.bbl` are included. TeX Live 2025
produced the delivered PDF; the build receipt pins its exact source and output.
Compilation verifies typesetting and reference resolution, not mathematical
truth. No merge, arXiv submission or journal submission accompanies this draft.
