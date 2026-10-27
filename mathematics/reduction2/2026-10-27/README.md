# Further reductions: elementary support, exact curvature, tighter resources

These are three mathematical reductions and one execution prototype, with
separate scopes. They extend the [earlier conditional uniform42 route](../../simplification/2026-10-27/README.md).
Read the [nine-page proof](proof/main.pdf), [TeX source](proof/main.tex), and
[independent review outcome](reviews/REVIEW.md). All work is in the user's fork;
the reference commit remains `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
The continuation starts at `42433b448d9389359e642a3384a949ffdd87b903`.

## Results and exact scope

| Result | Mathematical status | Execution status |
|---|---|---|
| Elementary support for all65 calls at actual n>=42 with zero predecessor loss | Locally derived and independently reviewed, conditional on attained contact and actual ordered moment resources | Fresh exact constructor and independent checks; no native acquisition replay |
| Exact LOW curvature supremum from at most3 candidates | Proved on the full real parameter domain; safe zero-clamp transport conditional on the original whole-count inequality and unchanged gates | Fresh exact diagnostics and independent piecewise oracle; no full LOW cell accepted |
| Tighter score-excess resource and empty sectors | Derived and independently reviewed conditional on acquired same-law phase/geometry inputs and the separate uniform-scope bridge | Fresh exact arithmetic on45 LEFT+47 CENTRAL rows; independent outward calculation |
| One-pass152-row LOW protocol | Equivalent serialization/coverage for the original contract, conditional on fresh trusted evaluator outputs | Synthetic protocol PASS; native execution path not exercised |
| Complete BASE41, LOCAL42, production replacement or conjecture | Not established here | No whole-proof or heavy native run |

### Support can avoid Bernstein certificates entirely

[Elementary support proof](elementary-support.md) replaces the signed
fifth-order Gaussian argument by a fourth-order expansion with an explicit
remainder uniform in the raw threshold. Two fixed boundary inequalities and
one monotone degree5 polynomial on the complete radius interval cover all65
calls. Eighteen common ray signs cover the infinite rays. Actual acquired
moments, attained contact, the direct derivative inequality and Gaussian norms
through derivative5 remain premises.

Thus this alternative support component does not need the old radial
Bernstein cells, the newer14-group/672-coefficient certificate, the signed
fifth-order identity, its fourth-derivative lower tangent, or its associated
domination gates. No old files are removed. This reduces internal support
reasoning; it does not eliminate the acquisition tasks producing the moments.

The [independent support review](reviews/elementary-independent.md) derives
the heat cancellations separately, reconstructs the polynomial by rational
Vandermonde interpolation, binds the original caller ASTs and fixed route,
and checks all65 individual endpoints plus390 ray signs.

### Each LOW curvature grid becomes an exact maximum

[Curvature proof](local-kernel.md) proves the exact supremum of
`(b+u-1)_+/(c-u)^2 + (b+u)_+/[c+min(u,c/3)]^2` on any closed
subinterval of `[-1/2,1/2]`, for real b and `1/2<c<=1`. Only the endpoints
and an eligible stationary point `u=c-2b` are needed. The exact value never
exceeds the old64-subinterval outward envelope. Conservative CENTRAL cache
reuse remains justified in its actual band order.

Improved curvature can make the final inverse-index correction negative.
The proved replacement clamps it at zero before replacing actual n by42;
it preserves the original strict target `<-1/1000` and negative-event gate.
No existing assertion is disabled. Per cache miss,64 candidate evaluations
become at most3; this is not a whole-job speedup estimate.

The [independent curvature review](reviews/curvature-independent.md) uses a
separate piecewise oracle on8,505 exact cases, three corrupted helper variants,
four false-rule controls and180 convexity diagnostics. Constructor diagnostics
cover3,648 calls on the actual152 producer configurations. Corrected potential
cache keys are43,136 CENTRAL+77,952 LEFT, before empty-cell pruning. Initial
default-grid workload claims were corrected; their original evidence remains.

### Retaining the excess charge removes actual comparison sectors

[Resource proof](tighter-resources.md) retains `n(C-C_E)rho` in the original
phase resource. A convex two-interval bound includes equality `C=C_E` and
uses only the universal `rho>=1` in the charge. Both new joint-resource
intercepts come from one residual; noise and inward displacement are not
charged independently. All bounds below apply after acquisition/confinement.

| Row (zero-based) | New outward bound | Computation made unnecessary in a new cover |
|---|---|---|
| LEFT0 | Negative joint residual | Entire final row's TINY comparison |
| LEFT5 | lambda<=.049944478<.05 | MID sector |
| LEFT8 | lambda<=.077273055<.08 | Both signed LOW producers |
| LEFT10 | lambda<=.094055578<.10 | Sectors above.10; two profile evaluations on[.10,.12] |
| LEFT13 | lambda<=.117287323<.12 | Sectors above.12; two profile evaluations on[.12,.30] |
| CENTRAL28 | lambda<=.099809552<.10 | Comparison sector above.10; profile already inherited |

The candidate upper-module inventory therefore becomes238->171->169 legacy
tasks:19 native obligations+150 LOW producers, before new joins. This is
not a whole-repository count. TINY/MID savings are internal sectors, not
additional whole native jobs. No acquisition ancestor is removed; row0
is excluded only after its final resource is acquired. Other signed rows,
closed seams and the zero-noise Bernoulli input remain.

The [independent resource review](reviews/resources-independent.md) uses
different outward square-root and geometry bounds, independently confirms
the same strict crossings, and checks the actual CENTRAL rounding contract.

### Separate one-pass prototype

[Protocol note](onepass-low.md) and [independent review](reviews/onepass-independent.md)
describe one fresh evaluation per original LOW configuration. Its synthetic
tests reproduce original rows, indices, summaries and binder controls with
152 rather than304 evaluator calls, plus14 additional rejection controls.
Native source loading and full evaluator execution have not been run.

The prototype deliberately pins the **original152-row output contract**.
It cannot accept changed curvature values, changed resources or150 labels.
Combining reductions requires a newly named acceptance contract, complete
coverage and independent integration review. Do not add or multiply their
potential savings as if a combined production implementation already existed.

## Reproduction and retained obligations

From the repository root, the following bounded commands are safe to reproduce
with ordinary unoptimized Python; they are not generation campaigns:

```sh
python3 -I -B mathematics/reduction2/2026-10-27/check_elementary_support.py
python3 -I -B mathematics/reduction2/2026-10-27/check_local_curvature.py \
  --archive verification/finite-tail/sources/backend.zip
python3 -I -B mathematics/reduction2/2026-10-27/check_tighter_resources.py
python3 -I -B mathematics/reduction2/2026-10-27/onepass_low_test.py
```

Independent checkers are in `reviews/`; receipts, hashes, versions, stdout,
stderr and return codes are in `runs/reduction2-20261027/`. The one-pass
native `run-family` command is intentionally absent here: it would run the
heavy LOW workload and requires separate approval. Do not use optimized Python.

The [base-closure audit](../../simplification/2026-10-27/base-closure.md)
remains unresolved: the pinned current40–42 provider body was unavailable,
while an older base join consumes tail43/early/single39. Genuine BASE41,
attainment/contact, actual resource acquisition, strict confinement, Fourier
and normalization inputs, surviving local comparisons, zero-noise Bernoulli,
lower approximation and a complete new composition contract remain obligations.
Independent review found no blockers at the stated conditional scope.
Recommend merge as research/audit material after explicit user approval;
not as replacement production acceptance. Keep the PR draft; do not merge.
