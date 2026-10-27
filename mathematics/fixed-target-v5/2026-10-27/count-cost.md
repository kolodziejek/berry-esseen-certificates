# Count crossings: disjoint costs and a fourth-moment price

The proof is `count-cost.tex`; the bounded exact checker is `count_cost.py`.
This changes a component of the existing local comparison, not its target.

| Result | Mathematical status | Execution status |
|---|---|---|
| A maximum replaces the sum of the positive/negative crossing prices | Locally derived, with a pointwise proof using disjoint crossing events | Checked on actual finite conditional laws and source parameter cells |
| The cubic large-crossing cost can be replaced by the smaller of its third- and fourth-moment bounds | Locally derived; uses the fourth-moment estimate already in the old proof | Fresh exact PASS, including rare-noise negative control |
| The phase maximum still needs at most two endpoints and one stationary point | Locally derived for every allowed interval | Fresh bounded exact comparisons; continuum conclusion comes from the derivative proof |
| The complete local comparison passes with the new coefficient | Conditional on all other terms, their acquisition and domain coverage | Not run; no native LOW acceptance claimed |

For centered independent conditional residuals, let the coupled count sums be
`V_j`, with consecutive count locations at least `c` apart, `1/2<c<=1`.
Write `t=E V_k^2<=T`, individual amplitude `A`, phase `|u|<=1/2`,
`chi=(n+1)p-k<2`, and `d=2c-1/2`. The curvature coefficient becomes

```
max((chi-1)_+/(c-u)^2, chi_+/[c+min(u,c/3)]^2)
  + min(sqrt(A^2+3T)/d^3, (A^2+3T)/d^4).
```

The first change uses that positive crossings require `V_k<0` and negative
crossings require `V_k>0`. The second uses that a negative crossing of order
at least three forces `V_k>d`, followed by
`E V_k^4 <= t(A^2+3T)`. The proof retains the strict outgoing endpoint for
the closed event, the marked-crossing linear term, the Gaussian repair,
the binomial mass factor, and the zero-noise case. The complete inverse-index
correction must be clamped at zero before replacing `1/n` by `1/N`.

The old source comparison is in
`manuscript/arxiv-v1/appendices/local-comparison.tex`, and the pinned
`central42_v2/central42_kernel.py` and `left42_final/central42_kernel.py`
inside `verification/finite-tail/sources/backend.zip`. The checker reads
their data through the earlier guarded helper
`mathematics/reduction2/2026-10-27/check_local_curvature.py`; no archived
program is executed. All input hashes are in the output. This is not an
independent implementation of those earlier acquisition procedures.

## Fresh bounded evidence

Run `python3 mathematics/fixed-target-v5/2026-10-27/count_cost.py` with
assertions enabled. The `runs/fixed-target-v5-20261027/count02/` record has
return code zero, Python version, source hash, stdout and stderr.

- 3,648 sampled cells represent all 152 signed LOW row configurations.
- The disjoint-price change is strictly smaller in 279 sampled cells.
- The fourth-moment change is strictly smaller in all 3,648 sampled cells.
- Exact actual-law enumeration checks 1,776 tuples in 12 law/phase cases,
  including 56 tuples with nonzero discrete curvature.
- Five malformed domains are rejected. Using a minimum instead of the
  required maximum, and dropping the individual fourth moments, both fail
  the negative controls.

These are component checks, not a full replay of every LOW cell or its final
score gate. No runtime improvement for the full proof is inferred.
The failed first run is retained under `count01/`, with its exact failed
source: a non-LOW row was incorrectly passed to the LOW-only data reader.
The accepted run restricts to the existing canonical LOW cutoff families;
it does not remove a required acceptance cell.

An exploratory direct variance price for the entire CDF difference was
also considered. It loses the useful linear cancellation and was weaker
in the small-noise regime. It is not used here; no claim of a replacement
for the marked-crossing argument follows from it.

No existing certificates, targets, production drivers or immutable sources
were changed. Independent review is recorded separately in the integration
branch; agreement does not replace the displayed proof.
