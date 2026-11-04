# Bounded visual review of journal-v20, pages 35–66

Date: 2026-11-04. Reviewer: `/root/resume_finite`. Read-only review; no TeX edits.

Source PDF: `runs/joint_count_20261104/analytic_v20_layout03/build/main.pdf`.

SHA-256: `dc484d79d282f57f23f34834c42e0ccc2cf622fe788c2c211d8f9a053eddce4e`.

The source PDF has 100 A4 pages. The assigned visual review covers pages 35 through 66 inclusive, not the other pages.

## Actual inspection

All 32 assigned pages were freshly rendered at 85 dpi with Poppler `pdftoppm` in `runs/joint_count_20261104/audit_layout03/`. Rendering returned 0 with empty stdout/stderr. `RENDER.json` records the exact command, PDF hash, page scope, and hashes of the page images and six contact sheets.

The following contact sheets were actually viewed using `view_image`:

* `sheet-035-040.png`: pages 35–40;
* `sheet-041-046.png`: pages 41–46;
* `sheet-047-052.png`: pages 47–52;
* `sheet-053-058.png`: pages 53–58;
* `sheet-059-064.png`: pages 59–64;
* `sheet-065-066.png`: pages 65–66.

Page 46 was also viewed as its individual 85-dpi image to check the long equation (45) and its separately positioned number. Pages 36, 48, 50, 55, 63 and 66 were freshly rendered at 130 dpi and actually viewed individually. `DETAIL_RENDER.json` records the six exact commands and their successful return codes. These follow-ups examine the two finite-cover tables, the finite-base conclusion, the long support inequality (47), the signed-moment bounds (61)–(68), and the complete feedback lemma (75)–(76).

## Observations

No clipping, overlapping text/equation numbers, off-page displays, broken table rows, black replacement glyphs, or visible unresolved-reference markers were found in the inspected images. The support table on page 36 is dense but its rows and columns remain distinct. Table 1 on page 48 has readable line wraps and complete borders. The finite-base theorem and its proof fit together on page 50. The long equations on pages 46, 55, 63 and 66 fit their margins; equation (45)'s number on a separate line does not collide with the following text.

One minor directional wording issue was observed: the first row of Table 1 on page 48 says “with the positive corner below,” although the positive-corner proposition is Proposition 6.9 on page 46. The source location is `sections/finite.tex:1506` in the frozen build source and current v20 source. Suggested wording is “with the positive corner of Proposition 6.9,” or simply “with the positive corner.” This was reported to the owner; no correction was made by this reviewer.

This is a visual layout record. It does not claim a fresh mathematical proof audit of all text visible in the sheets, nor acceptance of a theorem from the appearance of the PDF. The independent finite small-noise audit is recorded separately in `FINITE_REVIEW.md`.
