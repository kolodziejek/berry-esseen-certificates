# Release02 inherits the reviewed layout

All 86 pages of release02 were rendered with the same `pdftoppm -r 65 -png`
settings used for the actually inspected release01 contact sheets. Every
page has identical dimensions, image mode and decoded pixels. Every PNG
is also byte-for-byte identical. No page difference was found.

- Reviewed release01 PDF SHA-256:
  `b608a2838e110bf11e29d5ec7f0c2b78c7c25fbbd45dc52c5307529f8849bbdf`.
- New release02 PDF SHA-256:
  `e15bf3de23795e3312b68fc08e97dc6d8bc9bdb835c0ede8647ec19f841fe0f7`.
- Exact per-page result:
  `runs/direct_comparison_integration_20261104/release02_layout_compare01/RESULT.json`,
  SHA-256 `0efa2143c315e010aad578dc6db8b4b1defcd32b463e3c8104cb50e57a2ddc09`.

That run records the renderer identity, actual command and exit status,
all old/new PNG hashes and the complete 86-page pixel comparison. It also
checks the new successful, source-stable build record and that neither
PDF nor the reviewed baseline PNGs changed during the comparison.

The prior visual review therefore applies to release02 at the reviewed
65-dpi resolution. The PDFs themselves have different byte hashes; this
does not claim PDF byte identity or visual inspection of a separately
changed page. The original six enlarged follow-ups are recorded in
`release_layout_review.md`; this new comparison is the whole-document
65-dpi join requested for the whitespace-only release.

The coordinator separately records the single trailing-space source edit
in `runs/direct_comparison_integration_20261104/release02_source_change01/RESULT.json`.
Source equivalence is that separate check. No manuscript source was changed
here, and no mathematical or certificate campaign was rerun.
