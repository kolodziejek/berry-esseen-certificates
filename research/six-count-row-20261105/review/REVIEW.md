# Independent review: continuous n=5 BN panel 38 reduction

The conditional six-count method, its two Gaussian/rho strengthenings, and the
reviewed source formulas are sound at the stated scope. No complete original
row or manuscript replacement is certified by this review. The original
acquisition and reflected-score obligations remain separate.

| Item | Mathematical status | Execution status |
| --- | --- | --- |
| Common-law beta polygon, nine common moment endpoints, finite Cauchy bound | Independently derived; full proof in `SOUNDNESS.md` | Exact actual-law tests passed |
| Cleared degree `(9,4)`, fixed-cell gamma and vertex coefficients | Independently derived | Full inverse expansion passed on four selected cells |
| Negative-phase Gaussian concavity and vertex-specific noise | Independently derived under the explicit curvature guard | V2/V3 algebra checked; no new full cover claimed |
| Fixed convex blend with the exact same-law absolute-cube numerator | Independently derived; actual numerator nonnegativity is used before relaxation | V3 target polynomial reconstructed exactly |
| Entire original p/phase/noise row | Requires complete accepted cover and original acquisition | Not asserted by these tests |

Read in full: `construct/model.py`, `model_v2.py`, `model_v3.py`, `accept.py`,
`controls_v1.py`, the pinned Gaussian core, the pinned Sturm positivity reader,
and `root/six_count_reduction.tex`. Source hashes for the first four readers and
native inputs are in the tensor result. At that checkpoint the V3 source SHA256
is `6f9e527f6bda1bdc1be2c5c3c7b1de44bf00f711c389527543fb73b5be179f62`.

The root note correctly distinguishes mixture counts j=0,...,5 from nearest
threshold roots k=1,2,3. Its raw-threshold interval was independently checked by
rational multiplication. Explicit `n>=1` and nonnegative support ceilings would
make its generic premises more formal; no mathematical defect was found.

The external V1 reader reconstructs all required moment rows, pins the original
contract, requires six ordered quartics, and checks both children of every
closed dyadic split. The model's optional cached-row parameter is internal and
is not exposed to the proof object. No independent admission of a final V3
tree is implied by reviewing its moment model.

## Fresh evidence

All paths below are relative to the project workspace. Each run has the actual
command, interpreter/version, return code, source hashes, stdout and stderr.
Both exact reviews returned zero with stable sources and empty stderr.

* `runs/count_row_20261105/review_semantics01/checked/RESULT.json`: 165 actual
  conditional-law pairs, 990 conditional convolutions, 165 complete iid/count
  mixture identities, 612 threshold-atom checks, 48 zero and 48 tiny-variance
  components, 495 common-corner and 333 admitted-polygon tests. Five exact
  controls refute unsafe alternatives, including the original negative
  diagonal correction under a convex-vertex argument and upper-noise
  substitution for a negative Gaussian numerator. These laws test the
  reduction; they are not asserted to satisfy every contact/acquisition filter.
* `runs/count_row_20261105/review_tensors01/checked/RESULT.json`: full inverse
  Bernstein expansion matched the independent direct moment formula in all
  144 selected rows, 7,200 moment coefficients and 7,200 target coefficients.
  Twelve compact-ray identities were checked independently. All 144 deliberate
  coefficient corruptions were detected. This compares continuous polynomial
  identities, not just sampled positivity.
* `runs/count_row_20261105/review_floor_discovery01/checked/RESULT.json`: bounded
  floating exploration of 18,000 actual two-point conditional-law pairs, of
  which 2,123 passed the selected noise/beta/rho filters. No violation of the
  fixed-rho-floor target was found; the best diagnostic margin was about
  -0.02244. This is neither an impossibility proof nor a proof that the floor
  suffices. It does not establish full contact/acquisition membership.

The common-rho identity is a useful rigorously justified strengthening even
without an obstruction. The eventual reader must keep theta in [0,1], preserve
all noise slabs and their shared endpoints, check the Gaussian curvature guard
before using vertex-specific noise, and retain the same vertex and gamma pair
in every count and in the rho numerator. Fixed candidate coefficients on each
cell and a strictly positive p²q² denominator are essential.
