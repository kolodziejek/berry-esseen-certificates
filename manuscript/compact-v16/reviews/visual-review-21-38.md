# Visual review: PDF pages 21–38

Inspected all 18 pages individually as rendered PNGs: pages **21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, and 38**. The printed page numbers agree with these render indices.

Source PDF: `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_revision_20261029/root01/build02/source/main.pdf`.

PDF SHA256: `b3d8647f143bbe0f85e2ed2f6188301dd231a51ba74563751d3676dbde43f28e`.

Images: `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_revision_20261029/root01/render02/page-NN.png` for NN=21–38.

## Findings

No clipping, overlapping text, unreadable mathematical symbols, unresolved-reference placeholders, or isolated section headings were observed in these pages. Displayed formulas and their equation numbers remain inside the page. Headers, page numbers, and paragraph spacing are consistent.

- **21–23:** The normalization table, complete tail formulas, global quartic minorant, rectangle coefficients and endpoint table are legible. The endpoint table at the bottom of page 22 is wholly visible and does not collide with the page number. The discussion of `h_alpha(0)=0` and the separate strict-event interpretation are visible. Section 7.3 begins with sufficient following text and its full constant display.
- **24–26:** The crossing identity and finite index ranges are legible. Closed-event and atom wording is present below Lemma 7.2. The five-count reserve, omitted-translate explanation, error envelopes and one-quartic calculation fit. The wide W display on page 25 places its equation number below the display at the right; this is clear and has no collision. The concavity paragraph begins near the bottom of page 26 with its formula and continues normally on page 27.
- **27–28:** The composition hypothesis table fits both columns. Wrapped cells remain associated with the correct rows. The conditional theorem, reflected strict/closed atom formula, finite-base limitation and separate AI disclosure are readable.
- **29–34:** Appendix headings and the Fourier estimates are legible. The compensated-inversion statement, low/high-frequency formulas, six-term list and weighted-Cauchy derivation have no visible clipping. The discussion of moving thresholds, atoms, and conditional-distance atoms remains present. Appendix B starts on page 34 with its lemma statement; the proof continues on page 35 without an orphan heading.
- **35–38:** Directed constant enclosures, the off-contact residual definition and identity, uniform-law example, support-integral convention and entry appendix are readable. Lemma B.2's short statement is complete at the bottom of page 35, with its proof on page 36; this is an acceptable page break. Equation (50), including the support residual, is fully visible. The leakage endpoint wording `[u,v)` appears on page 37. No formula or theorem statement is lost at the transition into Appendix D.

This is a visual layout review of exactly pages 21–38 of the identified build. It is not a further mathematical proof audit and makes no claim about pages outside that range. No manuscript or rendering files were changed.

## Final build correspondence

Independently compared the SHA256 hashes of all 18 reviewed page images (21–38) in `render02/page-NN.png` against the final `render03-page-NN.png` files. Every pair is byte-identical. Therefore the visual findings above also apply to these exact pages of `build03/source/main.pdf`, whose SHA256 is `0edb424f8c49eb0feae9439bc149d98623bde54ef40cbf5302d6ea7f7cfe26e1`. This comparison makes no assertion about other pages of the final build. No source or image files were edited.
