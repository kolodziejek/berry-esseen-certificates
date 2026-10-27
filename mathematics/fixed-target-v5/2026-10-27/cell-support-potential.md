# Bounded support-radius follow-up and defect wording correction

The conserved defect used throughout the scalar run is

\[
 D=(3+\sqrt{10})\rho-\gamma-3J.
\]

The manuscript gap bound `J<=rho+2m` gives
`D>=sqrt(10)*rho-gamma-6m`, not equality. This is stated explicitly at
`manuscript/arxiv-v1/appendices/fourier-analysis.tex:1844–1847` and the companion
`entry.tex:199–207` defines the same conserved defect. The previous prose in
`cell-refinement.md` incorrectly called the lower bound an identity. It is now
corrected. The program already used the valid directions

\[
 \gamma\ge\sigma_l l-3-d,\qquad
 \rho-\gamma\le(1-\sigma_l)l+3+d
\]

from `D<=d`, `m<=1/2`, `rho>=l` and `sigma_l<sqrt(10)`. No formula, input,
output, or arithmetic status changes.

## Can a cell-dependent support radius help the five remaining cells?

Potentially four of them; this check does not resolve the worst one. I evaluated
only 175 small rational polynomial probes: 35 candidate radii `3.50,3.51,...,3.84`
for each of the five unresolved rho cells 19–23. There were no Fourier calls,
imports of inherited programs, signed-cover runs or further acquisition loops.

The contact/heat argument of the companion
`../excess-entry-v5/mathematics/fixed-target-v5/2026-10-27/entry.tex:128–155`
uses the cell's upper `rho=u` and its outward sign-moment bound

\[
 b\ge\sqrt{[u\sqrt{u^2+8}-u^2-2]/2}.
\]

Every occurrence of these upper bounds has the correct sign in the contact
polynomial, and the negative polynomial value is checked before replacing `c`
by `819/2000`. The boundary heat gates `A>0`, `0<H4<36A`, the negative boundary
value `P(R)<0`, and all six exterior-ray signs `Q,Q',Q'',L,L',L''<0` are checked
at each accepted radius. The argument is uniform in raw threshold `H`, both
support signs and all `n>=42`, conditional on the predecessor bound `C_(n-1)<=c`
and fixed-target contact/heat proof. No Fourier result is needed to establish
the candidate radius, so there is no acquisition/support cycle.

| Cell index | rho interval | First passing tested radius | Previous radius |
|---|---|---:|---:|
| 19 | `[159859/96000,8161/4800]` | 3.56 | 3.84 |
| 20 | `[8161/4800,166581/96000]` | 3.63 | 3.84 |
| 21 | `[166581/96000,84971/48000]` | 3.70 | 3.84 |
| 22 | `[84971/48000,173303/96000]` | 3.77 | 3.84 |
| 23 | `[173303/96000,7361/4000]` | 3.84 | 3.84 |

These are first passing points on this finite grid, **not** minimal radii.
In particular the final row does not rule out a smaller improvement between
3.83 and 3.84. Radius 3 is a separate negative control: its boundary polynomial
is positive, so this envelope rejects it.

| Claim | Mathematical status | Execution status |
|---|---|---|
| Listed polynomial values and required signs | Locally reconstructed rational expressions and checked | Fresh success, `cell04/support-receipt.json`, exit 0 |
| The accepted radius excludes both exterior support rays | Conditional on the companion contact/heat lemma and predecessor hypothesis | Analytic implication, not proved by arithmetic alone |
| Smaller radii lower the moment ceilings `R*u`, `1+k4(R)(u-1)`, `R*M4`, `1+k5(R)(u-1)` | Locally checked monotonicity from the radial formulas | No new Fourier evaluation |
| Those smaller radii yield a new complete initial acquisition | Unresolved; in particular the last cell keeps the old tested radius | Not run |

A next bounded experiment could recompute the four affected coarse scalar cells
with their individual radii, carefully recomputing every dependent moment,
negative-gap coefficient, low triple and complete high bound. Existing `cell02`
and `cell03` cannot simply be relabelled as that result: their input contract
fixes `R=96/25`. This support improvement alone supplies no new bound for the
worst cell and therefore is not evidence of a complete `D<4` acquisition.

The standalone `cell_support_probe.py` reproduces the small polynomial algebra
without importing the companion checker. Its source and the read-only companion
sources are hashed in `runs/fixed-target-v5-20261027/cell04/support-receipt.json`.
Exact stdout, empty stderr, Python version, optimization flag and return code are
saved there. Actual child command:

```sh
python3 mathematics/fixed-target-v5/2026-10-27/cell_support_probe.py
```
