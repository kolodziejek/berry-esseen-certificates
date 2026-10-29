# A fixed-target approach to the sharp iid Berry–Esseen inequality

**Bartosz Kołodziejek and Kacper Rodziewicz — revised review draft, 29 October 2026.**

[PDF](main.pdf) · [TeX](main.tex) · [Revision notes](REVISION_NOTES.md) ·
[Dependency/source map](SOURCE_MAP.md) · [Current validation](publication/validation.json)

This revision implements independently checked changes suggested by an external
review of commit `cd10654222f4b63d50f9d8f108597b140d263ec5`. It explains the
proof as rigidity followed by a comparison with a Bernoulli law, gives a concrete
account of the certificates, and replaces several calculations by simpler
arguments. It retains all 119 original labels and the original theorem scopes.
The PDF has **53 A4 pages**, including appendices and references, at 11-point
size with 28 mm margins. The additional explanation is intentional.

## Mathematical scope

The local comparison applies to every actual marginal in its explicit bounded
strip at `n >= 700`. Acquiring that strip for an extremizer requires the true
sharp predecessor and the complete entry/contact hypotheses. The global result
remains **conditional on a genuine base through 699** and the retained entry
conditions. No such finite base is proved here. A base only through 41 would
leave possible first failures at indices 42–699.

All incoming tails, threshold atoms, both signed correction bounds, the
stronger off-contact identity, and the complete coarse entry argument remain.
Historical proofs, certificates, acceptance programs and source pins outside
this manuscript directory are unchanged. AI assistance remains disclosed.

## Build

With TeX Live, from this directory:

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

The supplied `main.bbl` also permits three pdfLaTeX passes without BibTeX.
The delivered PDF was built with TeX Live 2025. All 53 pages were visually
reviewed; the final log has no unresolved references, missing citations or
overfull boxes. The notice about disabled shell escape for `epstopdf` is benign:
this document requires no external conversion.

## Reproduce the checks

The new scalar checks use only the Python standard library and run from a
standalone copy of this manuscript directory:

```sh
python3 -I -B tools/check_revision_constants.py --output-dir revision-scalar-review
```

Use a new output directory for every run. The driver captures the three
component outputs, return codes and hashes. These check the changed rational
identities and inequalities; the continuous mathematical arguments are in the
text. Diagnostic laws and negative controls supplement those arguments.

The unchanged historical bounded checks require the baseline repository:

```sh
python3 -I -B tools/recheck.py compact-v16-bounded-review
```

The isolated coarse-entry replay is run from the repository root:

```sh
python3 -I -B mathematics/fixed-target-v8/2026-10-28/isolated_entry_replay.py --output-dir /absolute/path/to/new-entry-run
```

The last two commands need the historical `mathematics/` tree from the pinned
baseline; it is not bundled in the source-only archive. Appendix E explains
the certificate format, generation, verification and trust boundary in detail.

## Fresh evidence and its limits

| Result | Mathematical status | Execution status in this revision |
|---|---|---|
| New quartic minorant, common error envelope, shared budget, ray comparisons and constant bounds | Locally derived and independently reviewed | Three new scalar checkers PASS, including negative controls |
| Historical v16 scalar and actual-law checks | Retained at their original scope | All nine unchanged checks PASS; 36 source pins preserved |
| Coarse-entry checkpoint | Conditional on the analytical enclosure and coverage arguments | Isolated 13-file replay PASS: 11,264 boxes, 100 panels, 30 nonempty panels, 14 cells; 19 checker and five wrapper controls |
| Revised source graph and original result preservation | Read/diff reviewed | 17 included TeX files, 132 unique labels, all 119 old labels retained, 24 cited works; no unresolved references/citations |
| Finite base through 699; full sharp conjecture | Open | No acceptance claimed |

Current publication receipts and complete fresh stdout/stderr are under
[`publication/`](publication/README.md); derivations and independent reviews are
under `reviews/`. `checks-summary.json`, `validation.json` and
`revision-validation.json` are preserved records of earlier compilation stages,
not the final publication manifest. The current source and PDF hashes are in
`publication/validation.json`. Successful execution does not establish
the analytic reduction, the missing finite base, or a full formalization.
