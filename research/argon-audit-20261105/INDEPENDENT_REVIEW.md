# Corrected audit of the seven all-Taylor acquired rows

The supplied review had two concrete reporting/implementation errors: it read `raw_moment_prices` instead of the actual `prices` field, and reported 19 roots instead of 20. Its claim of independently reconstructed dual tensors was also unsupported by its code. These findings and the unchanged original source/capture identities are documented in `ORIGINAL_REVIEW_FINDINGS.md`.

**Mathematical status:** locally derived and checked polynomial identities and continuous certificate representations for the seven selected original acquired n=5 rows, conditional on the stated acquisition and shared analytic reduction. **Execution status:** fresh corrected audit PASS; the supplied native acceptance was also separately replayed by the coordinating agent. Neither result is an all-295 n=5 theorem, original-acquisition replay or formal proof.

## Actual corrected result

The new source is `corrected01/check_all_taylor_v2.py`, SHA-256 `2a0f7756e99b6342a7e75759a0f2a1ac8001035490828501c7c4670b901c2802`. Its separate sparse polynomial helper has SHA-256 `43ab0a7bb54e00b19de6205d1ed624ef7b9c3fd8f1d132a6fbffe65a327aaebe`. Both are portable with an explicit package-path argument.

Fresh capture: `runs/argon_audit_20261105/review_corrected01/`. The actual process returned 0 in **95.91911595803685 seconds**, with empty stderr and unchanged sources/package. The full result hash is `3d9bb32f0829309a03d6bf6b5edcfc505782f1fabcce19219753c40de5202c1f`.

The complete checked census is:

- 7 distinct rows, **20** complete source-bound nearest-count roots, 63 dyadic leaves;
- 1,953 curvature-corrected PSD Bernstein coefficients;
- 121,500 strict score coefficients;
- **486,000 dual tensor entries**, representing all four independently expanded raw-moment slacks on every vertex/corner of every leaf;
- exactly one nonzero-priced leaf;
- all 295 packaged threshold catalogues independently derived, and 68 ambiguous/58 unique `(band,index)` selector groups checked.

The probability/phase/noise headers, original contract identities, root census and complete binary splits are checked explicitly. Every reconstructed leaf has the same actual price vector, score minimum and PSD minima as its source-bound native admission. No stored PASS supplies a polynomial inequality.

## The omitted price is not essential to this particular leaf

The affected leaf is `B2_S3_34`, `k=1`, path `11`, in object `objects/B2_S3_34_k1.json` (SHA-256 `6c275df31fa163e0df9aeba57133ed672460a015d11169029374cf31b5e14c49`). Its actual prices are `[0,2124448403/10000000000,0,0]`.

The fresh exact audit records these cleared score minima (decimals below are descriptive; the full rationals are in the result):

| Expression | Minimum |
|---|---:|
| Actual admitted price | 0.0012965820053565855 |
| Price omitted | 0.0012197031202327933 |
| Price sign reversed, diagnostic only | 0.0011428242351090012 |

All are positive. The old review therefore accidentally checked a valid stronger zero-price sufficient bound on this leaf, rather than revealing a failed native certificate. It still did not check the actual admitted priced expression or justify its claimed dual audit. The corrected audit detects 90 nonvacuous coefficient-identity mismatches when the price is removed or reversed across the vertex/corner rows. These are identity tests, not a false claim that both mutated inequalities fail positivity.

A negative dual price is not licensed by the original inequality argument, even when its diagnostic tensor happens to be positive.

**Derived zero-price corollary.** The same 63-leaf certificate family is valid with all four optional dual prices set to zero on every leaf, retaining the same quartics, theta values, source-bound cover and other original hypotheses. Indeed, 62 leaves already have zero prices and passed the fresh coefficient audit; the remaining leaf's complete zero-price coefficient array has the strictly positive exact minimum recorded above. The global majorants, moments and Hessian tests are unchanged by removing these affine dual terms. Thus the optional raw-moment dual argument can be omitted from the mathematical justification of these seven selected rows. This is a derived statement from the fresh arrays, not a claim that a modified native object was written or replayed. The accepted objects remain unchanged, and no conclusion is drawn for the other 288 contracts.

## Independence and shared dependencies

The corrected source separately expands the six shifted conditional-count expectations, both raw cubics `R=E|Y-p|³` and `G=E(Y-p)³`, all four raw-moment slacks, the corrected Hessian polynomials and their inverse Bernstein representations. The full derivation is in `corrected01/SOUNDNESS.md`. Zero conditional variance is handled algebraically without division by that variance.

The following remain shared with the native implementation: Gaussian Taylor lower polynomials and normal constants, the mean/noise and beta outer polygon, inward ceilings, the forward Bernstein transform (checked against a separate inverse), and the original analytic/acquisition hypotheses. The audit does not independently rerun every global quartic ray. The separate native replay covers those checks. The 295-selector check authenticates the packaged fixed census and its internal root/ambiguity rules, not 295 independently replayed original acquisitions.

The targeted curvature control is nonvacuous: all six `Q_j(z)=2+10^-12 z^4` polynomials passed all 12 global ray checks, then the positive-curvature PSD gate rejected them at `BN39/k2/path011`. This separates the Hessian obligation from an earlier ray rejection.

The scalar census also corrects a prose error in the supplied review: among 63 leaves, 40 have nonpositive Gaussian numerator, 7 cross zero and 16 are entirely nonnegative. All 23 latter leaves require the positive curvature allowance; “positive curvature” does not imply “crosses zero.”

## Reproduction

With the unchanged `n5-all-taylor` package (manifest SHA-256 `b950e3f7457f66305d6626badaed26886cfb37b72bf8aa50575ac8aafdc3de27`):

```sh
python3 -I -B -S corrected01/check_all_taylor_v2.py /absolute/path/to/n5-all-taylor /absolute/NEW_AUDIT_OUTPUT
```

The standard library suffices. The output must be fresh. All package bytes and the audit source/helper are recorded before and after the run. The original supplied review, its observations and the accepted certificate objects remain unchanged.
