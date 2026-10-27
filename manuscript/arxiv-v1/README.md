# First manuscript draft

**Authors:** Bartosz Kołodziejek and Kacper Rodziewicz. Affiliations, email
addresses and ORCIDs are intentionally omitted at the authors' request.

`main.tex` is the editable manuscript. The main chapters explain the
extremizer/contact method, first-failure reduction, elementary support,
joint physical defect, conditional-count identity, improved resource bound,
exact curvature maximum and conditional global assembly. The appendices
typeset the retained analytic derivations at their actual scopes.

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
