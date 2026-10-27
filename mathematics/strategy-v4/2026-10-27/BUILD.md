# Companion note source package

Authors: Bartosz Kołodziejek and Kacper Rodziewicz.

This 14-page research note proves new analytic reductions and explicitly
states the remaining scalar and local-exclusion assumptions. It is not a
complete proof of the sharp iid Berry–Esseen conjecture. AI use is disclosed.

With an ordinary TeX Live installation, run from this directory:

```
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

The generated main.bbl is included. After changing the bibliography, run
BibTeX between the first and second pdfLaTeX passes. No external fonts,
images or shell escape are needed. The full research audits and bounded
checkers are in the user's fork, under mathematics/strategy-v4/2026-10-27.
This package is not an arXiv submission.
