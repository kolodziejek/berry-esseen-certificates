# Scope of the review records

The Markdown notes here preserve bounded construction maps and mathematical reviews. They identify the arguments read and the source identities at that review stage. They are neither external refereeing nor proof-assistant certificates. Agreement between reviewers is not a proof.

- `core-map.md`, `finite-map.md`, and `local-map.md` map the consolidated chapters to their analytic sources and state their hypotheses.
- `equality-audit.md` checks the equality boundary used to remove the separate strict tail route.
- `foundations-review.md`, `finite-review-local.md`, and `finite-composition-audit.md` record separate bounded reviews. The coordinating review read the assembled analytic chapters as well.
- `build-STARTED.json`, `build-PROCESS.json`, `build-RESULT.json`, `build-stdout.txt`, `build-stderr.txt`, and `build-main.log` capture the final stable TeX build. The process return code is zero. Source pins are relative to the manuscript directory.
- `final-layout-*.md` describe the actual visual inspection of all 102 pages of build04. Build05 differs only on pages 28–29, after adding space around a table's displayed fractions. `PIXEL_COMPARISON.json` records comparison of all 102 rendered pages; the corrected pages were separately inspected.
- `FINAL_REVIEW.json` records the delivered PDF identity and review boundary.

The earlier mathematical review receipts retain their original hashes. The final `finite.tex` hash differs because of the scoped `arraystretch` change; its formulas and numerical targets are unchanged. No earlier receipt has been silently repinned to a different file.

Some preserved notes use absolute or handoff-relative paths from the original work environment. These are provenance, not portable reproduction commands. Use the new manuscript's `PROOF_MAP.md` and the immutable `extended-v17/reproduction/REPRODUCE.md` for the portable numerical source and evidence routes. The shortening prototype is separate from that proof graph.

The delivered build06 removes one trailing blank line in `references-added.bib`. All 102 rendered pages are pixel-identical to build05; `FINAL_PIXEL_COMPARISON.json` records that check. Its PDF identity and source pins are the ones in the final build records.
