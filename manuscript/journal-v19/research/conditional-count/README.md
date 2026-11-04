# Bounded conditional-count research

Read `STRUCTURAL_RESULT.md` for the proved common-majorant lemma, exact finite laws, and precise limitations. `MANUSCRIPT_MAP.md` gives the relation to the manuscript. The degree-elevation identity from the note is now incorporated in the curvature proof in the 98-page `layout06` build; it preserves the original bound and domains.

The counterexample concerns identification of a full CDF from its own-count law and listed normalization moments. It does not refute the manuscript, a majorant, or a claim restricted to attaining/contact laws. The displayed examples are below the comparison score floor `.4`.

From this directory, these portable commands use only the Python standard library. Replace each `NEW_*` with a different **nonexistent** output directory:

```bash
python3 -I -B own_count_obstruction.py NEW_PILOT
python3 -I -B check_structural_controls_v2.py NEW_CONTROLS
python3 -I -B complete_pilot_v2.py NEW_DETAILS
```

Keep assertions enabled; do not use `-O` or `-OO`. The controls and detail script locate their companion source and the included frozen `pilot01/checked/RESULT.json` relative to their own directory. The controls reproduce and compare the original exact pilot results. The detail script derives complete exact CDFs and support specifications from that included result and records the additional score classification. It does not acquire contact/resource hypotheses.

The `capture*.py` files are preserved historical launchers with fixed output names that already exist. Do not rerun them in the published tree. Their saved process records retain the actual original source paths, interpreter identity, streams and return codes. `controls01` and `details01` are failed exploratory probes, explicitly explained in the note; they are preserved rather than overwritten.

`MANIFEST.json` is the unchanged inventory of the original 36-file research package and its inspected inputs. `PACKAGE_MANIFEST.json` is the additive publication inventory including this README. Neither manifest constitutes mathematical verification.
