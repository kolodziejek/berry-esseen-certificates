# Finite appendix v3 evidence

These files preserve bounded algebra and source checks for source commit
`eafc01fdc41318f4583ec68488a91c27280a8ffb`, its local-baseline LaTeX build,
and a read-only layout review of the coordinator's integrated build01.

| Result | Mathematical status | Execution status |
|---|---|---|
| Formal Pearson expansions and exact structural-cutoff substitutions | Locally checked algebra with displayed hypotheses; not a new global theorem | Fresh bounded Python run, exit 0 |
| Two-point controls | Retained wider-domain repair necessary; doubled-loss variant refuted by the displayed law | Fresh exact arithmetic, exit 0 |
| Label/display/certificate-condition preservation | Textual comparison only | Fresh source check, exit 0 |
| Local-baseline document | Typesetting only | Fresh 163-page compile, exit 0; saved log and receipt |
| Integrated build01 pages 109--158 | Visual presentation only | Actual image inspection; no clipping or overlaps found |
| Full finite certificates and complete finite-base coverage | Still conditional / unresolved at their stated scopes | No native certificate runs in this task |

`check_finite_references.py`, `check.stdout.txt`, `check.stderr.txt` and
`check-receipt.json` preserve the bounded exact checks. The script is
standalone; its receipt also pins the manuscript files used in the manual
hypothesis audit. The script does not parse those formulas or establish all
their applications by itself.

`check_source_integrity.py` and the `source-check` receipt/streams preserve
the comparison to baseline `6299d97`: 165 labels, 87 labelled display entries,
four certificate conditions and 174 resolved finite references. An initial
Python 3.9 f-string syntax error is retained separately in the
`source-check-failed01` files, with the failed source snapshot. The corrected
script only moves a regex calculation out of the f-string expression.
Neither attempt executes an inherited proof program.

`compile.stdout.json`, `compile-receipt.json`, `main.log`, `main.aux` and
`main.toc` preserve the completed local-baseline build. Its final output was
copied from the distinct temporary directory recorded in the receipt.
Original compiler stderr was not captured separately; no separate successful
stderr capture is claimed.

`integrated-render-receipt.json` records the exact nine successful
`pdftoppm` commands and image hashes. `integrated-layout-review.json` pins
the integrated PDF and five overview sheets actually examined. All pages
109--158 were inspected in overview; pages 120, 124, 126, 144, 145, 154, 156,
157 and 158 were additionally inspected as separate 1700-pixel page images.
This covers the shortened contact proofs, numbered paragraph blocks,
retained paired-domain formulas, final conditional bridge, and bibliography.
No clipping, overlapping text, missing glyphs or equation-number collisions
were found. Bibliographic URLs remain within the text area.

One prose issue was found on integrated page 126: “a positive maximizing raw
threshold” could assert positivity of the raw threshold. Only the discrepancy
is guaranteed positive. The coordinator was sent the suggested replacement
“a maximizing raw threshold with positive closed-CDF discrepancy” and owns
the correction/rebuild. This review pins build01 before that correction.
No root files were modified by this child task.

The coordinator subsequently reported the page 126 wording corrected in the
root source, with a new build and changed-page review underway. This child
record does not claim inspection of that later build.
