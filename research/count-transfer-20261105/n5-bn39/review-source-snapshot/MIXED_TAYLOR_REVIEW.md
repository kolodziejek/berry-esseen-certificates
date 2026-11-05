# Eleven-cell Taylor transfer and mixed-reader review

This is an additive checkpoint. `FILES01.json` and all files it lists are unchanged.

Mathematical status: **the new scalar target and mixed-method soundness are independently derived and audited**. Execution status: the eleven repairs passed the constructor's local exact checks; my independent target algebra passed freshly; the complete mixed-row numerical replay is a separate remaining admission at this checkpoint. No complete BN39 result is inferred from the repairs alone.

## Exactly what changes

`construct/model_taylor.py` subclasses the previously reviewed original-row model and replaces only `target_tensors`. The conditional moment tensors, six count weights, nine common moment corners, probability/phase/noise domains, acquired beta/support/mean bounds, original target and affine absolute-cube price remain unchanged.

At a fixed probability/phase cell the genuine Gaussian must be concave in the common variance. The subclass explicitly requires

\[
0<p_-<p_+<1/2,\qquad k+u_+-5p_-\le0,\qquad
(k+u_--5p_+)^2\le15v_{\min}.
\]

These are sufficient for the already proved negative-numerator curvature criterion. Once the true objective is maximized at the variance-polygon vertices, its Gaussian value at each vertex is replaced by the quadratic lower polynomial reviewed in `GAUSSIAN_TAYLOR_REVIEW.md`. This does not require that lower polynomial itself be concave in variance. The vertex noise is exactly \(5(x+y)\).

Multiplication by \(v^2\) gives Gaussian target degree at most \((6,2)\), within the existing tensor degree \((9,4)\). The implementation transforms probability coefficients first and phase coefficients second, retaining the original probability-major/phase-minor order. It repeats the same Gaussian vertex target over the nine common moment choices, with their individually computed original affine rho-price improvements. The blend parameter remains fixed for the whole leaf.

The four scalar function bodies `down`, `up`, `interval_mul` and `gaussian` are byte-identical to the reviewed `later/gaussian_taylor01/check_broad.py` functions. Namespace routing uses the same pinned normal core and the same directed lower-CDF algorithm, with an additional explicit lower range guard. It does not introduce floating arithmetic into acceptance.

## Bounded construction and exact coverage

`try_taylor_repairs.py` binds the original partial object SHA-256
`b283408792a6d813424d4b1d6706b1711f195974baf8fe63739bdb206db2bcbb`.
It reconstructs its original root and every closed dyadic child domain, selects exactly eleven failed leaves, and performs no subdivision. Floating discovery remains separate from the exact `row.admit` call. Local success means only that each proposed repair satisfies the new sufficient target on its specified cell.

`make_mixed.py` preserves the original 963 baseline leaves and branch partition, checks exactly eleven new leaves, and tags those with `method="gaussian_taylor_v1"`. Its result explicitly says that the full original row is not admitted by this construction step.

`accept_mixed.py` obtains the original row and complete ordered root census from the unchanged external selector. For an unchanged root object it invokes the original full reader. For a mixed object it reconstructs every closed child domain from the external root:

- an untagged quartic leaf invokes the unchanged baseline sufficient inequality;
- a correctly tagged Taylor leaf invokes the new sufficient inequality and all its guards;
- unknown methods, failed/PASS markers, missing children, extra fields and unsupported split axes reject.

Both methods bound the same positive closed-CDF score at the original \(C_{\rm E}\) target. Therefore their union on the common closed cover is a valid proof of that same implication. Method tags select a proved analytic rule; they are not success flags. The source/data closure is checked again after the entire run. Global ray checks and atom conventions are unchanged in both methods.

The full expected row has 1,126 leaves: 149 baseline leaves in root 1, 963 baseline plus eleven Taylor leaves in root 2, and three baseline leaves in root 3. These counts describe the selected candidate; completion still requires the actual full replay receipt. Original acquisition is a premise throughout.

I read `controls_mixed.py`. It exercises a real accepted Taylor leaf, 22 malformed/domain/target/object changes, three analytic-domain guards and duplicate-key parsing: 26 negative controls in total. The captured control result is `runs/count_transfer_20261105/construct_BN39_mixed_controls01/checked/RESULT.json`, SHA-256 `cd07ef82cecdd8f00d313863e0a039f1883522e1efa81edbaefee38ead859a0c`. No optimized-interpreter probe is used.

## Fresh independent arithmetic review

My source `review/check_taylor_transfer.py` has SHA-256
`1b5c86d7c144298abd999d6cc20ee56a4b99aa5330a94ffb16e3c7816d2d8ae5`.
It independently traverses the hash-bound old tree to reconstruct the same eleven failed domains. For every vertex and all nine common moments, it reconstructs the full target polynomial using the separately implemented sparse polynomial algebra and inverse Bernstein expansion. It verifies both the new Gaussian target and the retained affine price.

Fresh capture: `runs/count_transfer_20261105/review_taylor_transfer01/PROCESS.json`, actual return code 0, 4.045497894287109 seconds, empty stderr, source/input closure unchanged.

Result: `runs/count_transfer_20261105/review_taylor_transfer01/checked/RESULT.json`, SHA-256
`f1dc438f8ff6ba4c1e4e5ed4504f7c102f548212186292828450644816158046`.

It checks all eleven cells, 55 variance vertices, 49,500 inverse coefficients and 495 coefficient mutations. The Gaussian scalar itself is shared with the already independently derived review; no second scalar algorithm or complete mixed-tree replay is claimed.

Reviewed source identities:

| File under `construct/` | SHA-256 |
| --- | --- |
| `gaussian_scalar.py` | `d69e659c6fa8d696a07a45756873e6dabeeecab1eb7ffc18664bce3ce18edc14` |
| `model_taylor.py` | `fbfc615e7f3b9b9d7aecee949960176e9c878cde393c50e706439de47f4015ba` |
| `try_taylor_repairs.py` | `c7009d48866f62604ceb3d899ff6f112c739e13efbc85894c6c43ea309ae1326` |
| `make_mixed.py` | `fe5052e042b2f2b485a8e3dac921d4af6f5888e0af8b2d6e4190de412372e66b` |
| `accept_mixed.py` | `ce7eaf841d13fef24807e6dab75acb2feba516e15e8912f8a6fc5f9eed7edf57` |
| `controls_mixed.py` | `781e0223c19d5bc3362cd5986435f1ad113ba16945909f2c0e632c9aa5a37f84` |

No mathematical defect was found; the full numerical replay is ready to run. The old portable package and old historical failures remain unchanged.
