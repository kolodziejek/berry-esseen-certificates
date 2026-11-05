# A complete acquired five-summand row using six quartic majorants

The new method now proves the positive closed-CDF comparison on the **entire
original n=5 BN/panel38 row**, conditional on its original acquired hypotheses.
It covers p in [19/50,39/100], the full noise interval [0,7687/25000], and all
three licensed threshold regions. The exact target C_E is unchanged.

A separate exact reader accepted **733 closed cells, 8,796 global polynomial
rays and 1,319,400 tensor coefficients**. The whole-row execution took about
9.2 minutes on the recorded machine. This is one completed row, not the whole
n=5 theorem or a new verification of the original acquisition.

[journal-v21](../../manuscript/journal-v21/README.md) remains unchanged at
**86 pages**. No page saving or approximately 60-page manuscript is claimed.

| Result | Mathematical status | Execution status |
|---|---|---|
| Complete original BN/panel38 positive score | Proved conditional implication by the common-law reduction and exact certificates | Fresh three-root acceptance: 246, 484 and 3 leaves |
| Original threshold domain and closed faces | Source-bound reduction to nearest k=1,2,3 | Original and relocated exact domain checks; 20 rejected mutations |
| New Gaussian, cubic-moment and mean/sign bounds | Derived in the analytic note and independently reviewed | V4 exact reader and 23 mutation controls; 21 assembly rejection controls |
| Independent arithmetic cross-check | Same conditional implication on the stated smaller V3 strip | Separate implementation accepts 8 leaves, 96 rays and 14,400 coefficients |
| Portable complete-row package | Unchanged readers, objects and original source closure | All-three source/header preflight and fresh k3 relocation check; full k1/k2 arithmetic was not repeated after copying |
| Manuscript replacement / all n=5 rows | Not completed by this checkpoint | 294 other selected n=5 rows and later consumers remain |

Read [the six-page analytic note](six_count_reduction.pdf), then
[HANDOFF.md](HANDOFF.md) and [the next-scope audit](NEXT_SCOPE.md).
The proof uses one common pair of conditional laws for every count. Support
bounds reduce common third moments to nine endpoint choices; convexity reduces
their variances to a polygon's vertices. Whole-cell Bernstein inequalities and
whole-ray positivity then give a finite exact check. The stronger target keeps
the normal term and third absolute moment tied to the same law. Original mean
and sign-gap bounds tighten the permitted noise and support endpoints.

## Reproduction and evidence

From this directory, use unoptimized Python 3.12 or later, standard library only:

```sh
python3 -I -B -S row-package/replay.py /absolute/path/to/NEW_OUTPUT
```

This command runs all three complete roots anew. The output must be outside
the package and must not exist. Floating-point LP discovery is separate and
needs NumPy/SciPy; acceptance does not. The reader reconstructs every moment
polynomial, checks closed dyadic coverage, and rejects malformed or incomplete
objects. The collector fixes the original root census independently of the
candidate data and ignores stored success messages.

The fresh full-row result is
`row-package/runs/count_row_20261105/analytic_complete_row_v4_01/RESULT.json`,
SHA256 `96f936b03aa0dc4cd2d174908cf45adb50186c6a03754c8b1be5a848701ccf57`.
Actual child return codes, streams, runtime and source/object hashes accompany
it. `row-package/COMPLETION.json` distinguishes the original full run from the
bounded relocation check. Hashes establish integrity, not mathematical validity.

`certificates/row-v4/` preserves construction, partial predecessor searches,
exact readers, objects and analytic licenses. Its historical candidate-only
status is intentionally unchanged; the later row-package result records final
acceptance. `review/independent-v4/` preserves the independent derivations and
smaller-strip admission, whose Gaussian normalization primitives are shared.
This is not an independently implemented full-row verification or a formalization.

The earlier narrow-region checkpoint and its `reproduce.py` remain available.
They concern only k2, u in [-.01,.01]. The original acquisition, reflected-event
conventions and all other manuscript ancestors remain separate proof obligations.
No certificate file or status flag establishes them by itself.
