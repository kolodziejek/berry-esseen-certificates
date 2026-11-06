# Audit of the supplied all-Taylor independent review

The supplied review was read, not executed, from `/Users/bkolodziejek/Documents/BerryEsseen/research/count-transfer-20261105/review/`. The sources there remain unchanged. The current accepted package was also inspected as data. Original acquisition and the analytic reduction to these acquired rows remain premises.

## Concrete mismatches

1. **Wrong price field.** `check_all_taylor.py` reads `leaf.get('raw_moment_prices', zeros)`. The final reader and selected objects use `prices`. In `objects/B2_S3_34_k1.json`, leaf path `11`, the actual second price is `2124448403/10000000000`; the other three prices are zero. The supplied review's `priced_leaves: 0` is therefore incorrect. Its score computation omits the actual price on this leaf. This is an audit mismatch, not by itself a failure of the native certificate. A fresh corrected audit must separately determine whether the unpriced alternative also passes.

2. **Wrong root total.** The actual target has seven distinct rows and twenty roots: BN39 (3), B0_50 (2), B2_S3_34 (3), BN38 (3), B0_53 (3), B3_S0_59 (3), B3_S2_59 (3). The total of 63 leaves is correct. `roots_verified: 19` is hardcoded and wrong. `rows_verified: 7` is also hardcoded rather than derived by that script.

3. **The dual reconstruction claim is unsupported.** The script obtains `row.dual_tensors` from the accepted implementation and adds those arrays directly. It never constructs the four raw-moment slack polynomials independently or inverse-checks their coefficient arrays. The result's phrase “independent ... dual Bernstein inverse audit” is stronger than the code establishes. In the supplied run the wrong field makes every price zero, so the dual terms do not enter its score at all.

4. **The target-coefficient mutation is weak.** It adds a nonzero value to a vector and checks that the inverse differs from the original inverse. This tests injectivity for that example; it does not exercise rejection by the certificate acceptor and does not establish robustness of the domain, source join or dual signs.

5. **Positive curvature is not the same as crossing zero.** The review text calls all 23 positive-curvature leaves sign-crossing. Direct traversal of the final 63 objects finds 40 nonpositive-numerator leaves, 7 sign-crossing leaves and 16 entirely nonnegative-numerator leaves. The curvature formula handles both positive cases correctly; this is a description error, not a defect in that formula. The read-only census and exact priced-object identity are preserved in `STATIC_SOURCE_AUDIT.json`.

## What is actually independently calculated

The review separately forms the uniform noise-curvature scalar using integer square roots. It separately expands the three quartic Hessian polynomials in a sparse representation and checks their Bernstein representations by an inverse transform. Its `independent_polys.direct` separately expands the six countwise moment expectations. It also reconstructs the cubic-price polynomial and checks the target and improvement tensors against sparse polynomial expansions.

The underlying Gaussian quadratic lower polynomial is still returned by the accepted `gaussian_scalar.gaussian`; checking its inverse representation does not independently prove that it bounds the Gaussian. The mean/noise/beta outer polygon, inward ceilings, source selector, scalar normal enclosures and original acquisition are also shared. The review does not independently replay the global quartic ray reader. Its mathematical text about both probability halves and the curvature correction is consistent with the direct derivative calculation; this is distinct from its executable independence claims.

The actual moment expansion is sound at its stated relaxed common-corner scope. Put `T=(5-j)xp+jyq`, `G=(5-j)gamma0*x*p+j*gamma1*y*q`, `L=(5-j)gamma0²*x*p+j*gamma1²*y*q`, `v=pq`, and `a=j-k-u`. Then the cleared expectation is

    v² Q(a) + vT [Q₂ + 3aQ₃ + 6a²Q₄]
    + vG [Q₃ + 4aQ₄] + Q₄[vL + (12/5)T²].

Its variance Hessian has the `24/5` factor used in the independent sparse expansion. The Gaussian correction subtracts `25 M v²` from all three cleared entries. These formulas retain the same conditional marginal across every count; the selected moment endpoints are a justified relaxation, not a claim that every actual fourth moment equals a squared-skew endpoint.

## Coverage and provenance limits

The supplied script traverses both dyadic children and reconstructs their cells. However, it does not independently require that the selected roots equal the entire original root catalogue, does not fully bind all object header fields, and does not count distinct row/root identities before reporting them. Its current objects do cover the intended twenty roots; the defect is the strength of the review's validation and reported count.

Its 295-selector exercise checks the packaged catalogue and ambiguity behavior through the shared selector. It does not compare 295 separately supplied original contract files to that catalogue. Only the seven bundled contracts are byte-bound by the package's own selector. A claim of independently verified original acquisition would be unjustified.

The external capture reports return code 0, 71.88597679138184 seconds, empty stderr and source stability. Its script hash `8004ce48ec293ca88952f70324f6785eb050c886d3b37231414f61adaf32e0fd` matches the current review source. The result hash is `de48c0eac95091a7f8fa5f165c5a3518a823ff212e98d46bd7076df81d76202d`. These are supplied historical observations, not a fresh local execution. The script hashes package inputs internally before and after, but does not serialize that full map or the package manifest hash in its result; the outer capture also omits those package dependencies. A new source-bound run against an immutable snapshot is preferable to treating the historical PASS as a complete binding to current package bytes.

Current package manifest SHA-256: `b950e3f7457f66305d6626badaed26886cfb37b72bf8aa50575ac8aafdc3de27`. Target SHA-256: `4e7ca427be4df9b3bde101b804d271d4a9da59ee3056e2484e62f6ba220ce14e`. The sparse polynomial helper's current hash is `43ab0a7bb54e00b19de6205d1ed624ef7b9c3fd8f1d132a6fbffe65a327aaebe`, matching the earlier separately reviewed helper.

## Corrected epoch

`corrected01/check_all_taylor_v2.py` is a new source, using the immutable workspace snapshot. It fixes the actual price field, derives and checks the complete 7/20/63 census, independently expands both raw cubic expressions and all four duals, compares each reconstructed score minimum with the actual native admitted leaf, and isolates the curvature PSD gate using globally valid tiny-leading quartics. Its independent derivation and exact scope are in `corrected01/SOUNDNESS.md`. The old source and observations are retained; a fresh result will be recorded separately.
