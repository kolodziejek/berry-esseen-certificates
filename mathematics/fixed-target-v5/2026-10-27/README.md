# Fixed-target progress: initial entry and smaller local costs

Read `main.pdf` for the new arguments in order. `main.tex` and the portable
`source-fixed-target-v5.zip` are the editable proof. This continues the earlier
`mathematics/strategy-v4/2026-10-27/` note; it does not claim a completed
sharp Berry–Esseen proof.

The starting point of this round is commit `78f0b7c`. The original reference
remains `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`. All changes are submitted
through existing draft PR #5 in `kolodziejek/berry-esseen-certificates`.

## What has advanced

| Statement | Mathematical status | Execution status |
|---|---|---|
| At a nonnegative fixed-target maximizer, `n>=42` and `C_(n-1)<=CE` imply `rho<7361/4000`, `|beta|<321/500`, support in `(-96/25,96/25)` | Derived from fixed-target contact and the stated external structural bound; no actual-score upper cap | Fresh rational support/moment checks; reviewed heat estimate and exterior rays |
| A first raw ceiling need only satisfy `T<N*c_lower*rho_lower`, rather than `T<2N/5` | Derived from exact conservation, including the positive phase coefficient | Exact scalar gates pass on all 24 closed moment cells |
| `R_c/rho<10` on the complete initial moment interval | Conditional on retained complete low/high Fourier estimates and the preceding actual-law entry | Fresh exact 24-cell evaluation; no native dense acceptance |
| Three ordered updates improve `D<=6.1147234045` to `D<=4.9901197720`, and prove `nD<=209.585030422267` | Conditional on the same premises; raw and resource ceilings kept distinct | Fresh exact evaluation; five cells still fail the sufficient `D<4` gate |
| Disjoint crossing events and an existing fourth-moment estimate lower the count-curvature cost | Locally derived for the full stated coupling/domain; independently rederived | Constructor actual-law/source-cell checks and separate reviewer checks pass |
| A common response bounds the entire raw moment polynomial on CENTRAL row 19 with cost `CE*(1.105+0.18*abs(H))` per residual defect | Locally derived conditional domain theorem; acquisition, actual-gap baseline and Fourier remainder retained | Exact stationary/sign checks and positive-noise actual-law controls pass |

The count proof is a useful analytic reduction independent of the incomplete
initial acquisition: it applies whenever its old moment and coupling inputs
have been acquired. It replaces a sum of crossing prices by a maximum and,
when `A^2+3T<(2c-1/2)^2`, replaces the cubic price by a smaller fourth-moment
price. The proof includes closed-event endpoints and the necessary zero clamp.

The remaining initial obstacle is now explicit. The last five rho cells
remain outside `D<4`; the worst retains `gamma_lower=-1.84025`. Repeating
the same coarse feedback does not improve its bound. A small per-cell support
probe suggests sharper radii for four of those cells, but not the last one
on its tested grid. It is not a completed new acquisition.

## Which computations this could remove

1. **First fixed-target entry:** the recurrence used only to acquire an
   upper actual-score cap, and its variable-score interpolation, are not
   inputs to the new initial support/raw license. The first license now has
   its own 24-cell result. The remaining ordered acquisition and exclusion
   must be transported before deleting those ancestors from a complete tail
   proof. Finite-index recurrence consumers are unaffected.
2. **Local count curvature:** the smaller closed formula is proved under the
   old component hypotheses. In its fourth-moment regime, this term needs
   no square-root bound. All other local terms, the strict event-bracket
   gate, mass bound, weighted resources, zero-noise theorem and full cover
   remain. The 3,648 sampled cells are diagnostics, not full LOW acceptance.
3. **Combined moment response:** the particular split response loses a
   favorable fifth-moment contribution; the new proof keeps it. This does
   not remove an old coefficient atlas or a whole cell until the remaining
   actual-gap baseline and signed Fourier remainder are controlled.

No existing computation is deleted by this change. In particular, a 24-cell
first license and the old 18,432-cell initial calculation have different
conclusions; their sizes are not a claimed speedup factor.

## Proofs, source locations and independent review

- `entry.tex`, `entry.md`: all-threshold support, moment bounds, actual
  independent-copy event, adaptive license and phase price.
- `cell.md`, `cell-refinement.md`: literal exact scalar formulas, every
  inherited primitive used, coverage, order of feedback and limits.
- `count-cost.tex`, `count-cost.md`: disjoint costs, quartic price and
  three-candidate phase maximum.
- `response-proof/response.tex`, `response.md`: exact common-measure identity,
  domain, budget, uniform ratios and remaining baseline.
- `independent-review.md`: count proof rederived without the constructor.
- `integration-review.md`: coordinating derivations, separate scalar review,
  corrections, and recommendation.

The manuscript's positive-gap argument had an invalid pointwise phrase:
`(t-a)*(rho-t)<=rho^2/4`. The correct bound is `t*(rho-t)<=rho^2/4`,
multiplied by `t-a>=0` and integrated. This includes a central gap crossing
zero and gives the same numerical coefficient. Only that proof explanation
changes in the long manuscript; its theorem statements and certificate
targets are retained. The corrected manuscript remains 158 pages.

## Reproduction

From the repository root, with assertions enabled and a fresh run id:

```sh
python3 mathematics/fixed-target-v5/2026-10-27/run_checks.py my-run-id
```

This runs eight bounded checks and verifies the original Git baseline,
including files outside the sparse checkout. It does not run native LOW,
the dense acquisition schedule, BASE41, or a Lean build. Component records
and integration attempts are under `runs/fixed-target-v5-20261027/`.
The first integration attempt omitted the first-cover checker's required
input argument; the second assumed every baseline file was materialized in this sparse
worktree, and the third tried to read a missing promisor blob. Its implicit
network fetch failed. Their failed drivers and bounded-check outputs are preserved.
The final driver verifies baseline tree/index objects and materialized bytes
without forcing the excluded certificates into the checkout.

The original component checkers and source-pinned Fourier functions are
separate from the document export script. Shared numerical primitives do
not constitute an independent proof of the Fourier lemmas. Complete
BASE41, full LOCAL42, uniform frequency estimates and all joins remain
separate mathematical obligations.

Final integrated execution: `integration04/receipt.json` records eight passing
bounded checks and 2,748 unchanged baseline entries (182 materialized files
and 2,566 preserved sparse blobs). `export01/receipt.json` records clean
15-page/158-page portable rebuilds with identical page text. Final visual
review is recorded in `visual-review.json`.
