# One strip and two noise estimates: compact manuscript

**Bartosz Kołodziejek and Kacper Rodziewicz — review draft, 29 October 2026.**

[Read the PDF](main.pdf) · [Editable TeX](main.tex) · [Source and dependency map](SOURCE_MAP.md)

The current compilation has **45 A4 pages**, including references, at the
original 11-point type size and 28 mm margins. It integrates the selected
v16 argument from [PR #5](https://github.com/kolodziejek/berry-esseen-certificates/pull/5),
pinned at `1aa1dd015e3d73fbeecc1a7acbfa395cbb560b5f`. The reduction from the
89-page draft comes from selecting one proof route, replacing its obsolete
branches and removing repeated exposition. It does not come from smaller type.

The text gives the needed analytical proofs in one compilation: fixed-target
attainment and contact, conservation and moment geometry, the selected coarse
entry implication and its Fourier enclosure, direct acquisition of one strip,
and complete small- and larger-noise count comparisons. The count arguments
retain every phase, threshold atoms and complete incoming tails.

## Exact mathematical scope

The local comparison holds for every actual marginal in the stated strip at
`n >= 700`. To acquire that strip for an attained nonnegative-excess witness,
the argument still needs the true sharp predecessor and the complete coarse
entry predicates. Consequently the global theorem is **conditional on a
genuine base through 699**, together with those retained inputs. A base only
through 41 would locate a first failure in 42–699; it would not exclude it.
Neither base is established by this manuscript. This is not a completed proof
of the sharp iid Berry–Esseen conjecture.

The original 89-page manuscript and all 85 of its tracked files remain
unchanged in `../arxiv-v1/`. Earlier smaller-index results, diagnostic failures
and certificates are preserved. The compact document is a separate editorial
integration, ready for review rather than a change to their acceptance status.
Substantial AI assistance is disclosed on the title page and in the discussion.

## Build

With TeX Live, from this directory:

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

The supplied `main.bbl` also permits three pdfLaTeX passes without BibTeX.
No custom fonts, external images, network execution or shell escape is needed.
The delivered PDF was compiled with the standalone official **Tectonic
0.17.0** compiler. It is not an exported desktop-preview PDF; the page count
can differ slightly with another TeX distribution.

## What the checks mean

All **nine unchanged v16 mathematical checks passed again** during this
integration: eight fast checks and the full 44-event actual-law check. A derived public
[check summary](checks-summary.json) records their status, return codes and
source/output hashes. Full original commands and raw captures are retained
in the local source handoff; they are not included in this public PR. Source checks also
account for **13 included TeX files, 119 labels and 23 cited works**. The
integrated comparison's four endpoint margins and its parameter guards were
separately reconstructed with exact rational arithmetic.

The first check attempt stopped only at Python's 4,300-digit decimal-output
limit; its record is preserved in the local handoff. Repeating the unchanged programs
with `-X int_max_str_digits=0` permits serialization of the large exact
fractions; it changes neither their arithmetic nor their assertions.
The original v16 records of ten bounded jobs, including the separate source
preservation job, also remain unchanged. Neither replay is a full coarse
Fourier reproduction or a proof of the finite base.

The numerical trust boundary still includes the complete entry checkers,
their coverage and directed-enclosure semantics, the executing arithmetic
implementation, and the stated external mathematical theorems. A successful
document build, an AI review or a recorded PASS label does not discharge those
inputs. This draft PR claims no full Lean formalization, new numerical generation
campaign, completed-proof acceptance, arXiv submission or merge.
