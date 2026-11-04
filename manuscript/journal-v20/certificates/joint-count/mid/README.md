# Optional joint-count MID certificate

This package proves a conditional comparison on intermediate noise using one quartic majorant of the coupled binomial-count payoff. It is an optional research replacement; its presence does not change the manuscript's proof dependencies automatically.

The domain is every integer `n>=47`, signed score `C>=2/5`, the existing acquired same-law inputs with `p in [.304,.47]`, and all phases `[-1/2,1/2]`. On each original input row, the noise interval is `[1/20,min(2/25,lambda_max(row))]`. Of the 83 original rows, 71 have a nonempty interval and 12 have an acquired ceiling below `1/20`. The target is unchanged: `rho_B(C-C_B)<-lambda/1000`.

Actual iid realization, conditional centering, the inward support gap, signed threshold and variance bounds, the normalizer's analytic soundness, and the joint-count expectation theorem remain mathematical premises. The four-moment envelope does not acquire them. Zero noise belongs to the separate Bernoulli argument. Noise above `.08` is outside this package.

The included `proofs/EXPECTATION_RULE.md` derives the coupling and expectation rule; `proofs/FIXED_PHASE_QUARTIC.md` derives the global certificate and moment-envelope conditions. `proofs/INDEPENDENT_REVIEW.md` records the independent review. Historical paths inside these notes are preserved as provenance, not as runtime requirements.

## Layout and execution

Use the frozen all-83 TINY package as the sibling directory `../tiny`. This MID package requires that sibling's native sources and source-bound applicability reader. Python's standard library suffices; never use `-O` or `-OO`.

From this directory:

```sh
python3 -I -B accept_mid.py proof_objects.json
python3 -I -B accept_mid_bound.py ../tiny proof_objects.json
python3 -I -B controls.py ../tiny
```

The first command checks the global polynomial witnesses and their numerical score gate. The second also checks the new `.08` normalization using the unchanged pinned gate formulas, binds all mathematical constants, and joins the result to all original rows while recovering their actual noise ceilings. Its child TINY census also performs the original small-noise polynomial acceptance. The third verifies this package's file hashes, independently identifies every leaf polynomial from five exact values, and rejects ten corrupted variants. These commands do not run acquisition or Fourier integrals.

The accepted proof object contains 200 closed phase cells. Each cell has nine finite staircase intervals and two infinite rays. The rays are compactified by `s=y/(1-y)`; omitting either ray is invalid. There are 4,243 Bernstein leaves and 21,215 exact coefficients. The positive final reserve beyond the original target is `5359299/400000000` times `lambda`.

## Provenance and evidence boundary

`accept_mid.py`, `mid_math.py`, and `accept_mid_bound.py` are unchanged copies from the parent task's `work/joint_count_20261104/root/`. The proof object is copied from `runs/joint_count_20261104/root_mid_construct03/proof_objects.json`; its SHA-256 is `b1f882b745e410dd34af9c2dbe609e5dfef47687a3f62bc4564a1cb57473331f`.

The independent analytic and source review is recorded in `work/joint_count_20261104/audit/MID_REVIEW.md`, and the source-bound independent execution in `runs/joint_count_20261104/audit_mid01/`. Paths here are historical workspace-relative paths, not runtime requirements. The package has no dependency on them.

An earlier discovered quartic had zero leading coefficient and a positive cubic coefficient. It becomes negative on the far-left ray and is not an accepted object. Its exact counterexample at `w=-100` is preserved in the controls. Positive sampled margins and optimizer status were never used as continuous-domain acceptance.

`PACKAGE_FILES.json` records the selected bytes and source provenance; it excludes itself. File hashes establish byte identity only. The polynomial and probability arguments, explicit assumptions and execution results have separate roles.
