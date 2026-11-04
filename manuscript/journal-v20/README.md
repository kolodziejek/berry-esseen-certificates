# A joint-count moment proof with exact certificates

[Read the complete manuscript](main.pdf). It has **100 total pages**, including
all analytic proofs, certificate explanations and references. The preceding
v19 draft had 98 pages. This revision simplifies a probabilistic argument;
it does **not** achieve the requested shortening toward approximately 60 pages.
Typography and margins are unchanged.

The new idea is to couple the actual conditional count sums monotonically.
One fourth moment then bounds all incoming counts. Four polynomial checks
replace the small-noise tail-series and relative-tail monotonicity arguments
throughout their uniform and finite applications. The proof explains why
the bounds apply to the same iid law, preserve threshold atoms and remain
valid for arbitrarily small positive noise.

The manuscript retains the same claimed scope: the sharp weak bound for
every positive sample size, optimality of the universal constant, and
strictness for every index at least 47. Its status is a locally derived and
reviewed computer-assisted proof candidate with the stated published inputs.
The new bounded audits do not constitute human/referee acceptance or a
proof-assistant formalization of the complete argument.

## Read and reproduce

Start with Sections 1 and 8 for the strategy, Section 4 for certificates, and
the fourth-moment argument in Section 7.5 for the new result.

- [Revision report](REVISION_REPORT.md): changes, exact scope, evidence and
  the measured length result.
- [Proof map](PROOF_MAP.md): dependency graph, retained evidence and optional
  experiments that are not used in the main theorem.
- [New certificate commands](certificates/joint-count/README.md): portable
  standard-library Python checks for all 83 uniform and 267 finite inputs.
- [Further simplification experiment](SIMPLIFICATION_NEXT.md): a precise
  higher-moment comparison on coarser supports, still requiring proof.

The original acquisition, Fourier, finite-binomial and remaining comparison
evidence is preserved in
[`extended-v17/reproduction`](../extended-v17/reproduction/) at commit
`c31d0cbe2af867d26871fbae37a3a7f4066f4a55`. This revision freshly checks the
replacement small-noise obligations and their input interfaces. It does not
claim a new run of the whole original campaign or its separate 114-command
relocated recipe. Prior manuscripts and original certificate bytes remain
unchanged.

The optional `certificates/joint-count/mid/` package also verifies a new
intermediate-noise comparison on `[.05,.08]`. Its required mathematical
argument is supplied with that package, but it is outside the PDF's proof
dependencies: adding it would not remove the remaining larger-noise machinery.

## Compile

From this directory with TeX Live:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The delivered build uses TeX Live 2025. Its exact source/output bindings and
layout reviews are in `review/`. The proof data are finite arithmetic objects,
not an omitted essential analytic supplement. No merge, arXiv submission or
journal submission accompanies this draft.
