# Final visual layout review: pages1–36

This is a bounded, read-only visual review of `runs/journal_v18_20261104/final-review04/build/main.pdf`. The reviewed PDF has102 pages and expected SHA-256 `e97bef239dd9afe878712727207a61c7323871dcc0f47d4527d91580d7bd95a6`. It is not a mathematical revalidation or a claim about pages37–102. No TeX or published PDF was edited by this review.

## Pages actually inspected

I opened and visually inspected **all pages1–36** using the actual image viewer on these six complete contact sheets:

- `sheet-001-006.png`: pages1,2,3,4,5,6.
- `sheet-007-012.png`: pages7,8,9,10,11,12.
- `sheet-013-018.png`: pages13,14,15,16,17,18.
- `sheet-019-024.png`: pages19,20,21,22,23,24.
- `sheet-025-030.png`: pages25,26,27,28,29,30.
- `sheet-031-036.png`: pages31,32,33,34,35,36.

All sheet paths are beneath the run's `render/` directory. I additionally opened individual images `page-014.png`, `page-021.png`, `page-025.png`, `page-028.png`, `page-031.png`, `page-032.png`, `page-033.png`, `page-034.png`, `page-035.png` and `page-036.png` to inspect dense equations, table spacing and the four-summand transition. Enlarged crops of the table on page28, the Gaussian definition on page34 and the support table on page35 were also viewed. These inspection-only crops are in `/private/tmp/journal-v18-layout-crop-{028,034,035}.png`.

## Finding requiring correction

**Page28, support-polynomial table immediately below the affine bound (26).** The horizontal rule under the header is too close to the first data row: it touches/cuts across the tops of the fraction numerators2,67,23 and1 in the n=2 polynomial. This is visible in the individual page and enlarged crop, not just an artifact of the contact-sheet scale. Add space between that rule and the first formula row, for example with a suitably sized row strut. Then recompile and inspect the table again. The finding was sent to the coordinator before this receipt was written. It is a typography issue; this review does not propose changing the coefficients.

## Other observed layout

No other clipping, overlapping text, missing mathematical glyphs, visible unresolved-reference markers or broken equation numbering was observed on pages1–36. The title/abstract/contents and author footnote fit page1. The contact and conservation displays retain their equation numbers within the text area. The closed-half-line majorant on pages20–21 crosses the page boundary normally and retains its complete formulas. Prawitz's four-term inequality, the six HIGH terms and their tail calculation remain legible. The long actual-index Gaussian formula on page34 fits without clipping. The support table on page35 is complete and its explanatory continuation begins normally on page36.

Pages28 and35 use dense tables; apart from the page28 header-rule issue, the entries are separated and legible at the individual-page scale. Dense algebra on pages31–33 fits the page and does not collide with the footer. Ordinary paragraph and theorem continuations across page boundaries were not treated as defects.

This receipt records the observed frozen render. It does not certify later recompilations automatically; the corrected page28 table needs a new visual check.


## Image identity record

The local PDF hash was recomputed and matched the expected identity above.

| Contact sheet | SHA-256 |
|---|---|
| `sheet-001-006.png` | `642c65481a25eacd35e10425a60b4e3d4ffb168e282e9157135a435f30dbc67e` |
| `sheet-007-012.png` | `5f13383581d7e358cd2663fec5e5091d7a8e8038c689a6db242bc1eb1b5146ed` |
| `sheet-013-018.png` | `e272b0a8e0603669ab5b6530f191b5b90e8208ecf2af9d923e6708badef72c3c` |
| `sheet-019-024.png` | `d2b48c87a95f24f11258a68ab34f2f82664f212ae1c8ad4f1f5b613b4830c72e` |
| `sheet-025-030.png` | `1a9d34046aa1e2970f637c780b7da66c1d67a8d393d373c5bd0e22c68da0ddd4` |
| `sheet-031-036.png` | `93c0958183186c5bfb9177926a7f6c80765b761dba4b017030224f85018cd30c` |


## Resolution in final-review05

The coordinator corrected only the table row spacing. I independently opened and visually inspected the actual `final-review05/render/page-028.png` and `page-029.png` images. The page28 header rule now clears every numerator; both polynomial rows are legible and separated. The redistributed text and equations on pages28–29 fit without clipping, overlap or a broken continuation. The original finding above is resolved in this render.

The local05 PDF hash was recomputed as `d4bc23c6d1027c0cf1119194266fbf9e375a31f62b2f2b6c3cdf2f53ef81a1d2`. An independent pixel-array comparison of all36 pages in this review’s scope found changes only on pages28 and29; pages1–27 and30–36 are identical to the already inspected04 render. Thus all pages1–36 of05 are covered by the original inspection plus this two-page recheck. I do not make a pixel-comparison claim for pages37–102.

| Corrected image | SHA-256 |
|---|---|
| `page-028.png` | `551ce0aa3d47de8ec6988fb3190d6c09daaaabbcba6d23f09d119d616cc1a6b4` |
| `page-029.png` | `dfd87abf0792a0f728789c751502638e0309e4e380cea8ae68023f46db6d6298` |
