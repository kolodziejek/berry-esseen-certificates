# Portable corrected polynomial audit

Keep `check_all_taylor_v2.py` and `independent_polys.py` together. With ordinary unoptimized Python, run:

```sh
python3 -I -B -S check_all_taylor_v2.py /absolute/path/to/n5-all-taylor /absolute/NEW_AUDIT_OUTPUT
```

The input package must be the preserved seven-row epoch with FILES.json SHA-256 `b950e3f7457f66305d6626badaed26886cfb37b72bf8aa50575ac8aafdc3de27`. The complete package is required, including its original selected objects and native admitted evidence. The audit source has no author-machine input path and accepts relocation through the package argument. Only the standard library is needed; output must not already exist. The recorded fresh run took about 96 seconds.

The independent sparse expansions and inverse checks are described in SOUNDNESS.md. Gaussian scalar bounds, acquisition, inward/variance polygons and native global-ray acceptance remain shared dependencies. This is a corrected independent polynomial audit of 7 rows / 20 roots / 63 leaves, not an all-295 theorem or an independent proof of every analytic premise.

The original wrong-field review and its capture are preserved separately. This source reads the actual `prices` field, reconstructs all four dual polynomials and records the priced, zero-price and sign-reversed diagnostic margins on the affected leaf. The negative-price diagnostic is not an admitted proof object. It also isolates the positive-curvature PSD gate with globally valid tiny-leading quartics.

The fresh result additionally implies that all optional dual prices may be zero throughout this seven-row certificate family: 62 leaves already use zero and the remaining complete zero-price tensor is strictly positive. The same quartics, theta values, cover and other original hypotheses are retained. No native object was modified or replayed under a new identity, and this corollary does not cover the other 288 contracts.
