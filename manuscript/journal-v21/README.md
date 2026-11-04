# A direct quartic comparison with exact certificates

[Read the complete manuscript candidate](main.pdf): **86 total pages**,
compared with 100 in v20. All analytic proofs, certificate explanations and
references are included, with unchanged typography. The approximately
60-page goal is **not yet achieved**.

The local argument now couples the conditional binomial counts and bounds
one resulting staircase function by a quartic polynomial. Exact moment
inequalities reduce the score comparison to finite polynomial checks.
This replaces the successive local confinement and noise comparisons.
An explicit four-polynomial calculation covers the unbounded central tail.

All new numerical obligations are complete: **30,030 finite row/index pairs**
across three families, together with the uniform central argument from
index 1,000. Each result retains its original acquisition hypotheses, whose
proofs remain in the manuscript. The overall claimed scope is unchanged:
the sharp weak inequality at every index, optimality of its constant, and
strictness for every index at least 47.

This is a locally derived and reviewed computer-assisted proof candidate
for independent human checking. Fresh arithmetic acceptance does not certify
the entire manuscript by itself, and no external referee or proof-assistant
verification is claimed.

- [Revision report](REVISION_REPORT.md): mathematical change, evidence and measured length.
- [Proof map](PROOF_MAP.md): selected dependencies and retained original evidence.
- [Certificate commands](certificates/direct-comparison/README.md): exact portable replays.
- [Further simplification](SIMPLIFICATION_NEXT.md): a proven fixed-location pilot and the unproved next full-row task.

The original evidence remains in
[`extended-v17/reproduction`](../extended-v17/reproduction/) at commit
`c31d0cbe2af867d26871fbae37a3a7f4066f4a55`. This revision does not claim a
new run of that entire campaign or its separate 114-command recipe. Earlier
manuscripts and original proof objects are unchanged.

With TeX Live, compile from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The delivered build uses TeX Live 2025. Its source/output record and bounded
analytic reviews are under `review/`. No merge or arXiv/journal submission
accompanies this draft.
