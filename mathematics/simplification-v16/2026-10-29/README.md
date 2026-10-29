# One strip, two noise estimates

The focused simplification replaces the post-entry part of the selected
`n >= 700` argument by three analytic components. The original manuscript
and all earlier proof objects remain unchanged.

1. **Acquire one strip.** Starting from a compact standardized law and the
   actual weighted defect budget `nD <= 32.20665378`, direct inequalities give
   `.375 < p < .465`, inward displacement `d < .004`, and noise `lambda < .35`.
   For an attained nonnegative fixed-target witness with the sharp predecessor,
   two contact rays give conditional amplitude `.6` throughout that interval.
2. **Small noise: fourth moments suffice.** For `0 < lambda <= .01`, retain
   the loss at one suitably chosen count. Its quartic minorant gives a loss
   larger than `.59 lambda`; the complete incoming-count tail costs less than
   `.53 lambda` before the binomial weight ratio. The actual count variances
   grow only linearly with count displacement, so reciprocal-power sums
   control the whole tail. No Poisson comparison is needed.
3. **Larger noise: five counts suffice.** For `.01 <= lambda <= .35`, use the
   compact sine-square minorant and four centered replacements. One fourth
   moment controls all omitted translates. After the signed curvature, normal
   and cubic corrections, two concave quartics need only four endpoint checks.

Both local estimates use the same actual iid marginal and give

\[
\sqrt n\{P(X_1+\cdots+X_n\le H)-\Phi(H/\sqrt n)\}
 -C_E E|X|^3<-\lambda/100.
\]

Their common assumptions are `n>=700`, `p in [3/8,93/200]`,
`-.6<=U0<=a0`, `-a1<=U1<=.6`, `a0+a1<=.004`, `E(U|B)=0`,
and raw `|H|<=1.84`, where `X=(B+U-p)/sqrt(p(1-p)+EU²)` and
`lambda=n EU²`. Zero noise is Bernoulli and has strict negative excess by
Schulz's finite-binomial theorem. The local estimates themselves do not need
contact or a predecessor; those are needed to acquire the strip.

## Read the proofs in this order

- [Composition and precise scope](composition.pdf), from [source](composition.tex).
- [Direct acquisition](acquisition-direct.pdf): scalar geometry and two contact rays.
- [Elementary small-noise comparison](small-common.pdf): the full incoming tail,
  quartic minorant, both outer phase intervals and exact normalization.
- [Unified five-count comparison](unified-comparison.pdf): one criterion, with
  the Compact row used here and the wider Right and Left rows retained as
  useful separate local results.

These component lengths are not an estimate for the eventual manuscript.
The manuscript still needs its retained attainment, conservation, contact,
Fourier and finite-base discussion. This round changes the mathematical
argument, not the manuscript.

The separate [right-strip improvement](counts-analytic.pdf) also lowers its
five-count noise threshold from `.075` to `.03` at `n>=200`. The elementary
inequality `sqrt(lambda) <= (5/3)lambda+3/20` is enough. With the retained
v11 small-noise theorem, this removes the 291-cell branch even on that wider
right strip. That corollary still uses v11's scalar Poisson-tail estimate;
the selected compact `n>=700` route above needs neither.

## What is removed from the selected dependency path

All removals below concern the acquired `n>=700` route. They do not erase
the old theorems at smaller indices or delete their certificates.

| Earlier component | Replacement and reason |
|---|---|
| v10 numerical global geometry and 30-panel post-entry export | `acquisition-direct.tex`, scalar acquisition theorem: starts directly from compactness and the actual D budget, and proves the interval and inward bound itself. |
| Thirteen right-strip and fifteen left-strip support checks | Same file, common-strip theorem: two physical boundaries exclude entire rays and give amplitude `.6` on the whole surviving interval. |
| v13 four noise ceilings, 139 Bernstein coefficients and index-table exclusions | Same file, noise section: the general one-sided cubic/AM–GM budget remains, but simple root bounds give `lambda<.35`; its old numerical tables are not used. |
| Separate left/right comparison join at `p=.4` | `composition.tex`, local theorem: both noise ranges use one interval and identical support assumptions. |
| v11 small-noise Poisson-tail estimates and v12 LEFT-01 | `small-common.tex`, Sections 2–5: finite normalization, the complete count-dependent fourth-moment tail, and one quartic minorant cover the whole compact strip. |
| v12 outer-phase comparison and 291-cell compound-Poisson negative-inner certificate | The same small-noise theorem covers through `.01`; the Compact five-count row starts at `.01`. No part of that phase/certificate split is needed. |
| Repeated crossing, curvature and normal-sign arguments in separate comparison notes | `unified-comparison.tex`, Sections 2–5: a single full derivation supplies every row. |

[The acquisition audit](acquisition-audit.md) gives the retained source locations,
exact hypotheses and the reasoning behind each acquisition removal. It first
joins its result to the independently established v15 union; the new
`composition.tex` replaces that last edge by the two common-strip theorems.
Consequently the audit's statement that the v15 small-noise ancestors remain
applies to its deliberately retained fallback composition, not to the selected
v16 route.

The coarse **11264-box Fourier entry** and its two coarse/four signed passes
remain. In particular, the old acceptor's internal 100-panel cover contract
has not been removed just because downstream probability panels are no longer
needed. Raw-threshold acquisition, the general gap-cost and one-sided cubic
identities, the heat/contact lemma, fixed-target attainment/reflection and the
sharp predecessor also remain. The external structural and binomial theorems
retain their stated roles.

## What this does not prove

This is a complete local comparison and a conditional acquired-witness
exclusion. It is **not an unconditional cutoff at 700**. With a genuine BASE41
and the retained implications at a least failure, a first failure must lie in
42–699. An unresolved earlier failure prevents using the sharp-predecessor
assumption at later rows. A base through 699 or another argument closing that
range is still required. Independent C4, BASE41 and the full conjecture remain
open in this audited branch.

Reflection is performed before acquiring the oriented witness. It does not
preserve the signed D budget or the probability interval, and a closed-CDF
atom gives an inequality rather than equality under reflection.

## Evidence and review

The proofs supply continuous-domain and infinite-tail coverage. Exact scalar
checks verify their finite inequalities. Actual-law controls and source
mutation tests supplement those arguments; they do not prove attainment,
Fourier inversion, acquisition from arbitrary laws or the finite base.

Constructor and independent-review evidence is recorded under the v16 `runs/`
directories, with commands, interpreter versions, input hashes, stdout/stderr
and return codes. The coordinator review describes the independent derivations,
corrections and remaining limitations. Source pins establish identity only.

The bounded final replay is:

```sh
python3 -I -B mathematics/simplification-v16/2026-10-29/run_checks.py NEWID
```

All ten jobs passed in `runs/simplification-v16-20261029/integration01/receipt.json`.
Independent reviews found no unresolved blocker within the stated scopes.
The selected route is ready for incorporation into a revised manuscript;
the retained foundation and finite-base boundary must accompany that revision.

Use a fresh alphanumeric run ID. No expensive certificate generation, coarse
Fourier replay or Lean build is part of that command. The baseline
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee` and all 85 tracked manuscript files
are checked separately for preservation. The review target remains draft
[PR #5](https://github.com/kolodziejek/berry-esseen-certificates/pull/5).
