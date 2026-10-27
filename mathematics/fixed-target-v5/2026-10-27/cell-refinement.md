# Three coarse fixed-target resource updates

This follow-up uses the exact 24-cell first cover in `cell.md`, recomputed at
run time. It performs exactly three ordered, inexpensive scalar updates on the
same cells. It does not call a dense signed stage or change an inherited source.

| Result | Mathematical status | Execution status |
|---|---|---|
| Three defined scalar updates, positive divisors and ordered upper bounds | Locally derived and exact-arithmetic checked | Fresh success, `runs/fixed-target-v5-20261027/cell03/refine-receipt.json`, exit 0 |
| Improved bound on the conserved resource and defect of a fixed-target witness | Conditional on the first-cover analytic premises and conservation identity | This run checks only the scalar implications |
| Uniform entry into the old `D<4` or generic-gap `D<2` regimes | Not obtained | Five final cells still have a bound at least 4; fifteen have a bound at least 2 |

The maximum acquired defect ceiling decreases from `6.1147234045` to
`4.9901197720`. The maximum conserved resource is at most `13.9304183554`,
compared with the retained raw maximum `17.0698618559`. The corresponding
weighted bound is `nD <= 209.585030422267` (outward decimal rounding).
Sixteen cells improve their raw upper bound over the three updates. The global
maximum raw bound does not improve. These statements keep a raw remainder bound
and a conserved-resource bound distinct.

| Update | Maximum raw ceiling | Maximum conserved-resource ceiling | Maximum defect ceiling | Cells with D<2 | Cells with D<4 |
|---|---:|---:|---:|---:|---:|
| 1 | 17.0698618559 | 13.9304183554 | 4.9901197720 | 8 | 19 |
| 2 | 17.0698618559 | 13.9304183554 | 4.9901197720 | 9 | 19 |
| 3 | 17.0698618559 | 13.9304183554 | 4.9901197720 | 9 | 19 |

In zero-based indexing the five cells failing the sufficient `D<4` gate are
19–23. For example, cell 23 is `[173303/96000,7361/4000]`; its final gamma
lower bound remains the initial `-1.84025`. Thus these coarse unsigned moment
bounds do not initiate further contraction there. Failure of a sufficient
scalar gate is not evidence that an actual counterexample exists.

## New phase price, independently derivable from the raw license

Use the notation of `cell.md`, let `w=H^2/(2n)`, `e=exp(-w)`, and set

\[
 M_c=c\rho-\phi(0)D/6.
\]

This `M_c` is a phase coefficient, not the fourth-moment cap `M` in the code.
The fixed-target transfer identity and `a,L>=0` give

\[
 e M_c=(1+H^2/n)a+c\rho+\sqrt nL-\mathcal R_c/n
 \ge c\rho-T/n>0.
\]

Consequently, using `exp(w)-1 >= w`,

\[
 n(1-e)M_c=n(e^w-1)eM_c
 \ge\frac{H^2}{2}(c\rho-T/n)
 \ge\frac{H^2}{2}(c_-l-T/N).
\]

The source conservation identity rearranges to

\[
 (n+H^2)a+n\phi(0)D/6+n^{3/2}L
 =\mathcal R_c-n(1-e)M_c.
\]

Hence if `eta=(c_-l-T/N)/2>0`, a quadratic bound
`R_c <= KF+cA+f(c)|H|-q(c)H^2` yields the conserved-resource bound

\[
 (n+H^2)a+n\phi(0)D/6+n^{3/2}L
 \le U:=\max_{t=c_-,c_+}
 \left\{K_F+tA+\frac{f(t)^2}{4(q(t)+\eta)}\right\}.
\]

In particular `nD <= 6U/phi_lower` and
`D <= 6U/(N phi_lower)`, with `phi_lower=997/2500<phi(0)`.
This is stronger than separately inserting a lower bound for `e` and a lower
bound for `M_c`; the product is bounded directly. It uses the **raw** `T`,
not `U`, to license the density and to form `eta`.

## Exact order of each update

The initial `T` is the first raw bound rounded upward to a multiple of
`10^-10`; set initially `U=T` and `d=6U/(N phi_lower)`, also rounded upward.
At each of the three updates:

1. Use the previous raw bound to form
   `phi_min=phi_lower*(1-T/(N*c_-*l))`. Check `0<phi_min<2/5`.
2. The conserved defect is exactly
   `D=(3+sqrt(10))*rho-gamma-3J`. The gap bound `J<=rho+2m`
   therefore gives the inequality `D>=sqrt(10)*rho-gamma-6m`,
   as stated at `fourier-analysis.tex:1844–1847`; it is not an identity.
   Use this inequality, the previous licensed ceiling `D<=d`, and
   `m=EX_+<=1/2` to obtain
   `gamma_min=max(-g,sigma_lower*l-3-d)`, where
   `sigma_lower=3.162277660<sqrt(10)`.
   Also `rho-gamma <= min(2u,(1-sigma_lower)*l+3+d)`.
3. Replace the `2u` factor in the negative-gap part of the old constant
   coefficient by that last upper bound. Retain the minimum with the old `A`.
   All other moment caps, low triple, complete high bound, and linear
   coefficient remain those of the first pass.
4. Use the sign-correct curvature

   \[
   q(t)=\max\left\{tl-g/5,\quad
   tl+\tfrac12\min(\phi_{\min}\gamma_{\min},(2/5)\gamma_{\min})\right\}.
   \]

   This follows by multiplying the signed gamma lower bound by the positive
   actual density and minimizing over its two endpoints. Reflection is not
   used to replace gamma by its absolute value.
5. Compute the new raw envelope at both `c` endpoints, round upward, and take
   its minimum with the previous `T`. This depends only on already licensed
   bounds. Recompute positive `eta=(c_-l-T/N)/2` with this raw bound.
6. Compute the resource envelope with curvature `q+eta`, round upward, and
   take its minimum with the previous `U`. Update the defect ceiling by the
   minimum of its previous value and `6U/(N phi_lower)`, rounded upward.

The same formal endpoint argument as in `cell.md` applies: `q(t)` is affine
in `t` because the two alternatives have the same slope `l`. All other cell
bounds are held fixed during the endpoint maximum. Square completion is valid
for all real `H`, including zero. Closed cell boundaries are retained.
No cell is discarded; an inconsistent gamma interval would reject this bounded
experiment rather than silently change its coverage.

This order avoids using a newly desired defect to prove itself. It also avoids
substituting the resource budget into the earlier raw-density license.
Rounding upward and taking minima of already justified upper bounds preserve
all inequalities. The slightly larger displayed maximum normalized raw value
`9.455732088691` compared with `cell.md` is only the new `10^-10` upward
rounding, not a deterioration of the underlying exact initial expression.

## Source scope, evidence, and remaining gap

`cell_refine.py` checks the SHA256 of the first-cover constructor before import,
then freshly runs its 24 cells. It does not accept an output JSON or a historical
success receipt as an input. The retained sources and primitive premises are
exactly those tabulated in `cell.md`. In particular the new update uses the
signed curvature reasoning at
`manuscript/arxiv-v1/appendices/fourier-analysis.tex:2399–2458` and the unsigned
constant charge at `2509–2515`; the raw/resource distinction follows directly
from the displayed conservation derivation here.

The analytic reviewer found a source proof wording error in the positive-gap
argument used by that coarse constant charge. The applicable pointwise step is
`t*(rho-t)<=rho^2/4`, multiplied by the nonnegative gap distance `t-a`, then
integrated using its gap-mass bound. The source phrase involving
`(t-a)*(rho-t)` alone does not justify the central positive segment when `a<0`.
The corrected derivation has the **same** coefficient `3*rho^2*J/8`, so this
calculation does not change any supplied coefficient. Acceptance of this edge
requires that corrected analytic argument, as documented separately by Task A.

Command actually run:

```sh
python3 mathematics/fixed-target-v5/2026-10-27/cell_refine.py
```

The parent recording process saved exact stdout, empty stderr, Python 3.9.6,
optimization 0, input hashes, output hashes, timestamps and return code under
`runs/fixed-target-v5-20261027/cell03/`. Three gate controls reject an unlicensed
raw ceiling, a negative defect input, and a density lower bound above the normal
upper bound. These controls test the new gate directions; the first-cover source
and literal-input controls remain in their separate recorded run.

The remaining obstruction is specific: this cheap cover leaves the last five
rho cells outside `D<4`, so it cannot be handed unchanged to an old feedback
routine whose precondition is `D<4`; still less does it establish global `D<2`
or the final `D<0.784`. A finer coherent moment/charge bound or a separately
proved structural restriction is needed. The three-step run is a rigorous
conditional resource reduction, not a completed initial acquisition or evidence
of any independent local-certificate saving.
