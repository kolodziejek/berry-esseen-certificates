# Front matter and main-proof visual review

Reviewed the rendered pages of `runs/certificate_discharge_20261030/root01/build01/main.pdf` using the existing 75 dpi PNGs in `root01/visual01/`. Every listed page was opened individually with `view_image`; this was a visual review, not a text-extraction proxy. The PDF skill was read and applied for this read-only inspection. No manuscript or PDF edits were made.

**Result: no clipping, overlaps, broken equations, unreadable table cells, or scope contradiction found on the inspected pages.** At 75 dpi the type is small, but ordinary text and equations are legible when each page is viewed individually. This review does not cover unlisted pages or independently establish mathematical correctness.

| PDF page | Inspection result |
|---|---|
| 1 | Title, author block, date, abstract, contents and footnote fit. The abstract explicitly retains the finite base through 699 as a hypothesis and says it is not proved here. |
| 2 | Definitions and displayed formulas fit. The results-and-hypotheses table is readable, its two columns do not overlap, and its final row explicitly states the finite-base hypothesis. The paragraph below distinguishes completed certificate discharge from that missing base. |
| 4 | All five flowchart boxes, arrows and caption fit. The final box labels the finite base as unproved here and the global sharp inequality as conditional on it. Certificate explanation paragraphs and the related-work heading have normal spacing. |
| 5 | Notation table has distinct columns and complete rows. Section transition and Proposition 2.1 fit; the long contact equation wraps as an aligned two-line display and its equation number is clear. |
| 6 | Dense attainment/contact proof remains inside the margins. Formula (5), the compensation argument, proof-ending square and subsequent reflection display are legible and do not collide. |
| 7 | Corollary 2.2 visibly includes its genuine finite-base premise. Moment inequalities and their polynomial proofs fit. The proof-ending square and subsequent lemma are separated. |
| 15 | Theorem 5.1 explicitly includes the predecessor and structural hypotheses and displays the acquired numerical bounds cleanly. The paragraph below says floor evaluation at 42 applies uniformly to actual indices at least 42. Lemma 5.2 and its equations fit. |
| 30 | The concavity formulas and endpoint checks fit. Theorem 8.1 states the index, predecessor and structural hypotheses. The two-column hypothesis-matching table is readable, including wrapped descriptions, and stays above the footer. |
| 31 | Theorem 8.2 visibly assumes the finite base through 699. The discussion preserves that restriction and explains why a base through 41 is insufficient. The role-of-verification and AI-assistance paragraphs fit. |
| 32 | Source-directory paths wrap at usable boundaries without extending beyond the margin. Appendix A's heading, integrals, hypotheses and Lemma A.1 fit. Its introductory text identifies support/moment/event acquisition as supplied by Appendix D under the stated entry conditions. |
| 33 | The inversion continuation, long epsilon identity, equation (44), LOW hypotheses and coefficient displays are readable and remain within the page. The next proof may continue on the following page, but no displayed equation is cut at the bottom. |

The review found no reason to revise these pages before delivery. The PDF and PNG hashes are recorded in `runs/certificate_discharge_20261030/fourier/visual-front-inputs.json` to identify the reviewed rendering.
