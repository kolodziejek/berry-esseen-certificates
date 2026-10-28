# A fixed-target approach to the sharp iid Berry–Esseen inequality

**Authors:** Bartosz Kołodziejek and Kacper Rodziewicz. Affiliations, email
addresses and ORCIDs are omitted at the authors' request. AI assistance is
disclosed on the title page and in the discussion.

`main.tex` is the editable manuscript; `main.pdf` is the 89-page review draft
of 28 October 2026. The paper now develops the fixed-target approach in full,
including its analytical proofs and explicit certificate conditions. It
replaces the previous 158-page manuscript as the current exposition.

This is a complete account of the stated reductions, **not a proof of the
sharp conjecture**. The sharp finite base through 41, the remaining
confinement domains and a complete strict count comparison remain open.
Acquisition, confinement and final exclusion are separate statements.

## Reading the paper

The introduction and guide explain the problem and proof strategy. Sections
2–6 establish fixed-target attainment and contact, exact conservation,
coarse Fourier entry, common moment resources and conditional confinement.
Sections 7–9 give the count comparison, harmonic estimates, conditional
global implication, evidence boundaries and unresolved steps.

The six appendices supply the full selected Fourier proof, conditional-count
toolbox, scalar normalizations, local refinements, closed-half-line smoothing
kernel and original-law four-summand bridge. The last bridge remains
conditional on genuine whole-cell numerical bounds and complete coverage;
it is not a complete four-summand proof. Analytical steps are included in
the manuscript, rather than delegated to the research companions.

Older TeX files that are no longer included by `main.tex` remain in the
repository. They describe other routes or historical finite-base candidates.
Their omission from this compilation does not discharge their premises,
delete certificates or certify the missing finite base.

## Build and portable sources

Use TeX Live with pdfLaTeX and BibTeX:

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

`source-arxiv-v1.zip` contains the selected TeX inputs, four bibliography
files, this README and the generated `main.bbl`. When using the archive,
three pdfLaTeX passes suffice without running BibTeX. No external images,
custom fonts, shell escape or online execution are required. The archive is
a portable source package; no arXiv submission has been made.

From the repository root, the following bounded checks write JSON to stdout:

```sh
python3 -I -B manuscript/arxiv-v1/tools/check_sources.py
python3 -I -B manuscript/arxiv-v1/research/v9_checks/scalar.py
```

The first checks source integrity, references, citations and author metadata.
The second independently reconstructs the two displayed scalar cosine
majorants with exact fractions: 80 and 896 Bernstein coefficients, together
with directed Machin bounds and a false-majorant negative control. Neither
command proves a full count cover or replays the earlier entry certificates.
The build/export helpers beside them record local tool versions, commands,
source hashes and return codes. They use the coordinator's local TeX/runtime
paths; ordinary manual compilation is portable.

## Review and evidence

- `research/v9-foundations-coverage.md`: fixed-target core and selected
  Fourier/entry correspondence.
- `research/v9-confinement-coverage.md`: full resources, continuous low-noise
  proof and central-panel confinement correspondence.
- `research/v9-independent-review.md`: independent composition review,
  retained hypotheses and corrections found during integration.
- `research/v9-integration-review.md`: final manuscript decisions,
  dependencies, validation and remaining obligations.
- `../../runs/manuscript-v9-20261028/`: source checks, scalar checks, build,
  visual review and standalone archive-rebuild evidence.

The earlier mathematical checks remain in their original v4–v8 research
directories and run records. This manuscript revision does not relabel those
checks as newly executed. It does not change the original `paper/` directory,
proof objects or acceptance programs. The reference baseline remains
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee`; this editorial work starts from
`924e6160bee44ed3a50eba35f7dbb8dcd5b9a9c7` on the existing PR branch.

The bibliography retains the classical literature and separately identifies
recent papers, repositories and formalization projects. The source/version
choices and retrieval limits are documented in `research/classical-sources.md`,
`research/modern-a.md` and `research/modern-b.md`. No new bibliographic claim
was introduced or independently rechecked during this editorial round.

The review recommendation is human review of the conditional research draft.
Keep PR #5 in draft; neither a merge nor submission as a completed proof is
recommended at this stage.
