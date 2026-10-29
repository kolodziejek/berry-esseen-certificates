# One strip and two noise estimates

**Bartosz Kołodziejek and Kacper Rodziewicz — review draft, 29 October 2026.**

[Read the PDF](main.pdf) · [Editable TeX](main.tex) · [Proof/source map](SOURCE_MAP.md)

The manuscript has **30 A4 pages including references**. It keeps 11-point
body type and 28 mm margins, with 6% extra line leading and visible paragraph
spacing. The earlier 89-page draft and the first 45-page integration are
preserved in Git history. This revision shortens the argument by using one
proof route, one notation and one proof of each needed identity.

The complete selected analytical arguments are included: attainment/contact,
off-contact conservation, physical moment geometry, the Fourier enclosure
and ordered entry implication, acquisition of one support strip, and the two
noise comparisons. Atoms, both threshold signs and complete incoming tails
remain explicit. The numerical entry is stated as exact certificate conditions.

## Mathematical scope

This is a **conditional research draft**. The local comparison applies to
every law in its stated strip at `n >= 700`. Acquiring the strip for an
extremal witness requires the actual sharp predecessor and the complete
entry predicates. The global implication still requires a genuine base
through **699**. A base only through 41 leaves indices 42–699 unresolved.
Neither finite base is established here, and the manuscript does not claim
a completed proof of the sharp iid Berry–Esseen conjecture.

The source reference is [PR #5](https://github.com/kolodziejek/berry-esseen-certificates/pull/5)
at `1aa1dd015e3d73fbeecc1a7acbfa395cbb560b5f`. All 6,558 original tracked
blobs, including all 85 files in `../arxiv-v1/`, were checked unchanged.
Substantial AI assistance is disclosed on the title page and in the text.

## Build and checks

From this directory, with a current TeX Live:

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

The supplied `main.bbl` also permits compilation without running BibTeX.
The delivered PDF uses official Tectonic 0.17.0 in untrusted mode; another
TeX distribution may paginate slightly differently. No custom fonts, images
or shell escape are required.

[Validation](validation.json) records the 11 included TeX files, 106 resolved
labels, six cited works, layout review and a clean portable rebuild. The
[check summary](checks-summary.json) is explicitly a derived public record:

- All nine unchanged v16 mathematical checks passed during the preceding
  integration, including the 44-event actual-law check. Their source hashes
  were preserved; this editorial revision does not claim another full replay.
- The canonical revision freshly checks the off-contact identities, physical
  geometry and 19 exact scalar/polynomial gates. The elementary target bounds
  now explicitly license the fine entry constants, and the Fourier tail has
  a short positive-remainder proof.
- Scoped component reviews checked the reduced arguments against their actual
  consumers, including the complete 13-file entry source allowlist. No omitted
  sharp-moment theorem is required by the selected execution path.

`python -I -B tools/canonical-check.py` runs the standalone exact appendix
controls. In a complete checkout of the pinned repository,
`python -I -B tools/recheck.py` reruns the nine v16 checks, both algebra/geometry
controls and the appendix controls. The first historical attempt hit only
Python's decimal-output length limit; the successful rerun allowed long integer
serialization without changing mathematical sources or assertions.

These checks supplement the written proofs. They do not establish the full
coarse entry predicates, missing finite base, external theorems or a Lean
formalization. The original entry coverage, directed arithmetic and external
inputs remain part of the stated trust boundary. This draft PR requests author
review; no completed-proof acceptance, arXiv submission or merge is claimed.
