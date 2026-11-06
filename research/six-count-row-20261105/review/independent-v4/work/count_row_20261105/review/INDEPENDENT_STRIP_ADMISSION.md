# Independent acceptance of one complete continuous strip

For n=5, nearest threshold k=2, p in [19/50,39/100], u in [-1/2,-49/100],
and the full original noise interval [0,7687/25000], the supplied eight-leaf
V3 object passes an independent exact polynomial admission. The result is
conditional on the original acquired common-law premises and covers the
positive closed-CDF comparison. It is not a full probability-row cover,
acquisition replay, or reflected-branch claim.

Selected proof object:
`runs/count_row_20261105/construct_cubic_pilot01/objects/proof_object.json`,
SHA256 `32c59ab41623b34832ac7ecc21986ef04e1760ee2f9f79df2fc10fd17cad4f0c`.

Independent entrypoint: `admit_strip_independent_v2.py`. It uses the following
separate arithmetic routes:

* Direct sparse cleared moment polynomials, rather than the constructor's
  moment-tensor construction, followed by its own power-to-Bernstein conversion.
* Adaptive exact Bernstein positivity on both compactified rays, rather than
  the constructor's Sturm root counter.
* A direct rational 40-term Gaussian-integral Taylor enclosure, rather than
  the constructor's directed integer grid recurrence. The Gaussian density
  normalization and Esseen lower constant remain shared pinned primitives.

For the Gaussian check, the even 40-term Taylor sum for exp(-s) is a lower
bound, and the next term bounds the nonnegative remainder. Integrating at
0<=z<=2 gives an explicit positive integral lower bound and upper error
z^81/(2^40*40!*81). The reader verifies its range and signs, uses directed
square roots, and applies symmetry for the negative argument.

All 15 tree nodes, eight leaves, 288 common moment rows and 14,400 score
coefficients passed. The 96 global rays required 656 exact subdivision nodes.
The whole root is fixed externally; altered phase coverage and a missing
closed child are rejected.

Fresh selected evidence:
`runs/count_row_20261105/review_strip_independent02/checked/RESULT.json`,
SHA256 `9576a098a3d6ff2400b6295c090ca05fe7a7a568deed7bbc431b55939fb181be`.
Its parent `PROCESS.json` records actual return code zero, 23.99 seconds,
stable sources and empty stderr. The result inventories all transitive source
imports and the proof object. The preceding `review_strip_independent01` also
passed; the additive V2 entrypoint only expands the recorded source closure.
Neither original reader nor proof object was changed.
