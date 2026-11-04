# Visual review: build01, pages 1–29

Reviewed 30 October 2026 using the PDF skill. Source PDF: `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_opus_20261030/root01/build01/main.pdf`.

Poppler rendered pages 1–29 at 90 dpi without errors. All 29 pages were inspected in eight four-page contact sheets; pages 2, 4, 5, 12, 15 and 27 were additionally inspected as individual images at original resolution. Renders, contact sheets and the input SHA-256 are under `runs/manuscript_opus_20261030/external/visual01/` in the handoff workspace. `render-record.json` records the command and exit status.

## Finding

One minor layout issue: Figure 1 at the top of page 4 interrupts the certificate-generation paragraph across pages 3–4. Page 3 ends “rounds its”, then the entire diagram and caption intervene before page 4 continues “reported bounds outward.” This is readable, but it disrupts the explanation precisely where the reader is distinguishing generation from acceptance. Prefer placing the figure before Subsection 1.4 begins, with a float barrier after it, or otherwise ensuring that this paragraph starts after the figure. Recheck subsequent page breaks after any adjustment.

## Passed visual checks

- Title, author block, abstract, contents and page numbers are readable and consistently aligned.
- The results-and-hypotheses table on page 2 and notation table on page 5 fit their columns. Mathematical symbols are distinguishable.
- Figure 1's boxes, connectors, shading and caption are intact; there is no overlap or clipping within the figure.
- The equations on all inspected pages remain inside the text area, including the dense displays and long formulas on pages 12, 22–29. Equation numbers remain separated from the formulas.
- The new predecessor-support lemma on page 15 is well contained. The conservation role table on page 12 has readable rows and consistent alignment.
- No heading was stranded by itself, no isolated proof-ending marker was visible, and no single-line paragraph widow was found. Multi-page theorem/proof continuations are ordinary and readable.
- No missing-glyph boxes, broken references, page overflow, overlapping text or unexpectedly blank page was observed.

This is a layout review, not an additional mathematical audit. Pages 30–57 were outside the assigned range. No source edits were made.

## Build03 recheck after figure placement repair

All existing renders of build03 pages 1–29 were re-inspected on 30 October 2026, using eight new contact sheets under `runs/manuscript_opus_20261030/external/visual03/`. Pages 4 and 5 were also inspected individually at original resolution. The source renders are `runs/manuscript_opus_20261030/root01/visual03/page-*.png`; no repeat rendering was needed.

The reported issue is resolved. Figure 1 and its caption now precede Subsection 1.4, whose certificate explanation remains uninterrupted on page 4. The resulting extra white space at the bottom of page 3 is acceptable and separates the strategy discussion from the diagram and computational explanation. The notation subsection and table are together on page 5.

The changed page breaks introduce no clipping, overlapping material, isolated heading or orphan proof marker. Corollary 2.2 continues across pages 6–7, and a few proof displays are followed by their definitions on the next page; these continuations are readable and do not require a further layout change. Equations remain inside the text area throughout pages 1–29. No actionable visual issues remain in the inspected build03 range. This recheck does not claim inspection of the subsequent build04 typo-only revision.
