# Audit of the external seven-row continuation

The all-Taylor improvement is worth keeping. A fresh replay of the supplied
proof objects passed on all **seven original acquired rows, twenty threshold
roots and sixty-three leaves**. The mathematical review found no defect in
the new Gaussian bounds or curvature-corrected variance reduction. Original
acquisition remains a premise; this is not a proof of all295 rows or a new
shorter manuscript.

This audit concerns external commit
`6ebda7f5f54c8a2a56391ade39db982f537f02e4`. The supplied publication and its
historical evidence remain unchanged in `../count-transfer-20261105/`.
The original folder `/Users/bkolodziejek/Documents/BerryEsseen` was read only.
Fresh execution used an exact copy under the research workspace.

## Confirmed improvement

| Original acquired row | Earlier six-count leaves | All-Taylor leaves |
| --- | ---: | ---: |
| BN/p39 | 1,126 | 18 |
| B0/p50 | 383 | 11 |
| B2 S3/p34 | 54 | 7 |
| BN/p38 | 733 | 13 |
| B0/p53 | — | 5 |
| B3 S0/p59 | — | 4 |
| B3 S2/p59 | — | 5 |

On the same first four rows, 2,296 leaves become49, a factor of about46.9.
Across all seven rows there are63 leaves. The new reader rechecked756 global
quartic rays,1,953 PSD coefficients and121,500 score coefficients. Its fresh
captured return code was0 in23.741seconds, with empty stderr and unchanged
inputs. The43 supplied negative/corruption controls also passed freshly.
These timing figures describe this run, not a complexity guarantee.

An independent data-only audit matched all295 catalogue entries to the
original workspace contract bytes and entire row payloads. It separately
reconstructed every selected closed threshold domain and all63 dyadic leaf
domains; no missing root or branch was found. The native replay then checked
the arithmetic on those domains. Hash comparison, coverage and arithmetic
are separate obligations.

## Corrections to the external report

| External claim | Correct statement |
| --- | --- |
| `C_E=9199/25000` | `C_E=(3+sqrt(10))/(6 sqrt(2 pi))`, approximately0.40973. The code uses the correct directed lower enclosure; the README formula is wrong. |
| 19 roots | **20 roots**. All20 are actually present and checked; the summary count is wrong. |
| Bands B0=29,BN=30,B2=92,B3=144 | **B0=24,BN=32,B2=104,B3=135**, total295. The underlying catalogue is the unchanged correct one. |
| `raw_moment_prices` in a proof leaf | The actual accepted field is **`prices`**. One leaf has a nonzero price. |
| Method tag `taylor` | The actual accepted tag is **`gaussian_taylor_both_halves_v1`**. |
| Threshold derivation via `contract["raw"]` and `contract["derived"]` | Those interfaces do not exist here. Roots are derived from `p`, `acquired_scale_upper`, `Hminus`, `Hplus`, and checked against `nearest_roots`. |
| The old independent audit verified the actual dual-priced score everywhere | It reads the wrong field and substitutes zero prices, so it does not verify the same priced expression on that leaf. Its dual tensors also came from the acceptance code without independent reconstruction. |
| The43-control command checks every ambiguous catalogue pair | That command tests selected ambiguities; the separate external review visits all68 ambiguous pairs. |
| The computed denominator is exactly `sqrt(d_min)` | It is a **positive rational lower bound** for that square root. The numerator uses a bound for the density `phi(0)`, not the CDF. |

The field mismatch is at external `review/.../check_all_taylor.py:158`;
its root total is hardcoded at line254. The affected object is
`n5-all-taylor/objects/B2_S3_34_k1.json`, leaf path`11`, whose upper-absolute-
moment price is `2124448403/10000000000`. These audit defects do not change
the supplied native reader's formula or its successful fresh replay. They
do require a corrected independent check; its additive source and fresh
receipt are supplied with this audit rather than rewriting the old PASS.

The corrected independent audit passed in95.919seconds:7 rows,20 roots,
63 leaves,1,953 PSD coefficients,121,500 score coefficients and486,000
dual-tensor coefficients. It reconstructs the actual `prices` expressions
and matches every native score minimum. An isolated negative control uses
globally valid quartics that pass their12 ray checks but fail the curvature
PSD test. The shared Gaussian scalar, variance polygon and native constants
remain explicit dependencies; this is not a completely independent second
implementation of the entire proof.

On the affected cell, the score also remains strictly positive when the
optional dual price is omitted. Thus the old audit checked a different,
successful sufficient bound there. The same quartics and cover can support
a presentation without optional dual pricing for these seven rows. This is
an independently reconstructed inequality, not a claim that the supplied
nonzero-price object was rewritten or natively replayed as a new object.
It does not show that dual pricing is unnecessary on the other288 rows.

To repeat the corrected audit from this folder, with a new output directory:

```sh
python3 -I -B -S corrected01/check_all_taylor_v2.py \
  ../count-transfer-20261105/n5-all-taylor /absolute/NEW_AUDIT_OUTPUT
```

For the original full native replay use its unchanged public entry:

```sh
python3 -I -B -S ../count-transfer-20261105/n5-all-taylor/portable.py \
  replay --out /absolute/NEW_NATIVE_OUTPUT
```

Both require only the standard library. Historical capture paths are
provenance; these commands choose the local package and fresh outputs.

The original package's inaccurate README and receipts are retained as the
record of what was supplied. Use this audit for corrected counts and scope.

## Why the mathematical extension works

The common conditional-law reduction is unchanged. For each count j, choose
a quartic above the closed-event step on the whole real line, and sum its
conditional expectation with the binomial weight. The six counts use the
same two conditional laws. The earlier support and fourth-moment argument
reduces the expression to common moment corners and a variance polygon.

At each fixed variance vertex, a quadratic Taylor lower bound for the normal
CDF retains its dependence on probability and phase. Uniform derivative
bounds control the whole cell, including the Taylor remainder. Using the
minimum of both endpoint variances makes this valid on either probability
half; no reflection of signed acquisition bounds is required.

The actual normal CDF need not be concave in noise. Put
`g(lambda)=Phi(a/sqrt(D))`, `lambda=5(x+y)`. A uniform bound `g''<=M`
implies that the true loss has Hessian

    H_F - 25 g'' J = (H_F - 25 M J) + 25(M-g'') J,
    J = [[1,1],[1,1]].

Both terms are positive semidefinite when the certified first matrix is.
Thus the actual loss is convex in the common variances. Only after proving
this are its vertex Gaussian values replaced by their Taylor lower bounds.
The31 exact univariate Bernstein checks per leaf verify the two diagonal
entries and determinant of the cleared matrix. The score then fits the
existing degree-(9,4) tensor check. `ANALYTIC_REVIEW.md` gives the full
derivation, including mean/support/beta bounds and optional cubic prices.

## Consequences for the manuscript

This is a substantial reduction in certificate size and checking time on
the tested rows. It supports extending the method. It does not turn a46.9-fold
reduction in cells into a46.9-fold reduction in manuscript pages: the analytic
soundness proof is largely shared already. Journal-v21 remains86 pages.

The next construction target is the remaining288 original n5 contracts,
with bounded pilot runs on the difficult signed/noise domains before a full
campaign. The actual model must reject unsupported domains rather than
treat them as exclusions. Later indices6--39 still use shared count arguments;
the signed corner, Fourier complements and acquisition have separate
dependencies. Only complete replacements and their source-domain joins can
justify deleting those manuscript sections.

There is no claim of formal verification or external referee review. The
new arithmetic remains conditional on the original acquisition premises.
