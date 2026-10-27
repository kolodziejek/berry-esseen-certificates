# Revised manuscript draft

**Authors:** Bartosz Kołodziejek and Kacper Rodziewicz. Affiliations, email
addresses and ORCIDs are intentionally omitted at the authors' request.

`main.tex` is the editable manuscript. The guide and dependency diagram
introduce the full contact/conserved-identity argument. The main chapters explain the
extremizer/contact method, first-failure reduction, elementary support,
joint physical defect, conditional-count identity, improved resource bound,
exact curvature maximum and conditional global assembly. The appendices
typeset the retained analytic derivations at their actual scopes, grouped into
six coherent appendices. Shared proofs are referenced after matching their
hypotheses; distinct finite-index and Fourier refinements remain explicit.

This is a review draft, not a claim that the sharp conjecture is proved.
The finite base, complete local predicates, their scope and the full new
composition remain obligations. Supplied analytic material is explicitly
distinguished from the new reductions and from independently checked
external results. AI use is disclosed in the manuscript.

## Build

Use an ordinary TeX Live installation with pdfLaTeX and BibTeX:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The generated review PDF and a source archive with a generated `main.bbl`
are delivered separately. No custom fonts, external image assets, shell
escape or online execution are required. An arXiv submission has not been
made and requires author approval and further mathematical review.

## Citation and proof correspondence

- `references-classical.bib`: historical and external analytic inputs.
- `references-added.bib`: six focused additions checked during the revision.
- `references-modern-a.bib`: Xiao–Li, Lin, He–Cheng v3, Tao's Problem19a,
  the earlier Hexagon manuscript and the sharp moment relation.
- `references-modern-b.bib`: Bell's individual manuscripts and the two
  distinct Lean projects.
- `research/classical-sources.md`, `research/modern-a.md` and
  `research/modern-b.md`: exact source/version choices and retrieval limits.
- `research/analytic-coverage.md` and the appendix coverage reports map the
  displayed arguments to their source material and retained obligations.

The reference baseline remains
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee`; the manuscript branch starts
from reduction state `8989ba054eda36f63e469832f1e00f7e6a7a9084`.
The original `paper/` directory, certificates and verification programs
are preserved. Changes are confined to the user's fork and submitted as
a draft for review, without merging.

## Delivered review artifacts

- `main.pdf`: 158-page revised draft; main exposition on pages 3–33 precedes the
  technical appendices. Explicit certificate conditions and AI disclosure.
- `source-arxiv-v1.zip`: portable source package, rebuilt in a fresh directory
  with shell escape disabled; it is not an arXiv submission.
- `research/revision-decisions.md`: disposition of the supplied proposals,
  reorganization, independent review and preserved limitations.
- `research/revision3-decisions.md`: the next editorial round, selective proof
  deduplication, corrected curvature derivative and retained hypotheses.
- `research/revision3-independent-review.md`, `revision3-fourier.md` and
  `revision3-finite.md`: bounded independent review and exact substitution maps.
- `research/manuscript-review.md`: original combined coverage, independent review
  outcomes, remaining limitations and actual validation.

The recommendation is author review, with the PR kept in draft. No final
publication, complete proof acceptance or merge is recommended at this stage.

The third round starts from manuscript commit `6299d97`. Its corrected
curvature derivative is also propagated to the earlier reduction note and
its PDF. The theorem and certificate predicates are unchanged. Compilation,
page-review and portable rebuild receipts are under
`runs/manuscript-v3-20261027/` at the repository root.

Draft review: https://github.com/kolodziejek/berry-esseen-certificates/pull/3
(stacked on audit PR #2; no merge or submission performed).
