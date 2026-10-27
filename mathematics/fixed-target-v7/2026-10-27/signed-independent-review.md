# Independent review of the fixed-target signed transport

The reviewed v7 transport has no blocking mathematical discrepancy in the bounded scope below. The selected `signed07` driver starts with the two simple quadratic passes, so the earlier full exponential-phase ancestor is no longer a dependency of this invocation. The six new signed passes still use the complete retained Fourier bounds, the fixed-target contact/conserved identity and actual-law support/moment geometry. Neither full INITIAL42/LOCAL42 acceptance, a count comparison, BASE41 nor the sharp conjecture follows from this review alone.

This report is on the separate branch `research/v7-review-signed-20261027`. The constructor's files were read in the sibling `signed-entry-v7` worktree and not edited. The reviewer previously authored the older signed-Cauchy and two-pass results: those ancestors are not claimed independently reviewed anew here. The independent contribution is the review of the coordinator's new v7 implementation and its coefficient transport, support selection, feedback, coverage, and revised driver. Prior independent review of the older two-pass result remains separate.

## Status and exact source scope

| Item | Mathematical status | Execution status in this review |
|---|---|---|
| Fixed-c raw polynomial, density and simple phase feedback | Independently derived below, conditional on the exact conserved identity and complete Fourier premises | Source read; constructor not imported |
| Same-law moment contractions, signed constants and actual-gap refinements | Independently checked directions against their displayed moment/measure proofs | Source read; no full arithmetic reimplementation |
| Per-rho support radius | Exact specialization of v5 heat/whole-ray implication, checked at the actual radius-selection domain | Helper read; no new support campaign |
| Ordered six-pass cover and reported peak accounting | Independently checked structural implication, not numerical leaf verification | Fresh PASS on saved `signed07`, five negative controls |
| Every signed-cell numerical bound and all inherited Fourier analyses | Not independently reproduced in this task | Constructor's saved successful run is distinct evidence |
| Entire global proof | Not established | No count or base replay |

Frozen sources under `mathematics/fixed-target-v7/2026-10-27/`:

| File | SHA256 |
|---|---|
| `signed_core.py` | `1f40ccb90eb58a7f84dc61a0a5dd9bf6e6eb4e341aa6c9c6d049d08451f5211b` |
| `signed_probe.py` | `1bec84b1d7be1046f02a5eded4242b253fc98ce040d5b94c5dbb1942c7166fd6` |
| `signed_support.py` | `eecb06e65d8520d7cc06fc34217e06e1c0b1840dd8d687621e6828923769a4c4` |

The source snapshots in `runs/fixed-target-v7-20261027/signed07/` match these live files. The selected invocation is six passes, eight beta intervals, eight gamma intervals, two common-first-moment intervals, per-cell support, and `--initial quadratic`. This review does not certify arbitrary inputs to these helpers. In particular the caller fixes the valid rational enclosure of CE; the helper's broad range check alone would not prove that an arbitrary chosen interval encloses CE. The parameter named `cap` is not a newly proved cap on the maximizing law's actual normalized score.

## Fixed-target algebra and ordered feedback

The exact input is `mathematics/strategy-v4/2026-10-27/excess.tex:260–312`, which distinguishes the fixed target `c=CE` from the actual score `c+a/rho`. Write

\[
\mathcal R_c=c\{\tfrac32\beta(J+\gamma)+3(\rho J_1-J_2)
+\rho M_4/2-M_5/4-\rho/2\}
+H(cK_1+\varphi U)-H^2(c\rho+\varphi\gamma/2)+E_n,
\]

where `K1=E[X|X|³]−3beta−3rho gamma/2`, `U=J1+(M4−3)/6`, and `varphi=phi(H/sqrt(n))`. I checked the signs against the source definition of Kq, rather than substituting the actual score into the fixed-target expression.

On a closed moment cell the program constructs a complete constant upper bound A, a signed interval for K1 and U, and a positive density interval. For either fixed endpoint t of the CE enclosure, its bound is

\[
\mathcal R_c\le\max_{t=c_-,c_+}
\{K_F+tA+f(t)|H|-q(t)H^2\},
\]

with `f(t)=max|t k+psi u|+s_F` over the full signed corners, and `q(t)=t rho_l+min(psi gamma_l)/2`. The constant is affine in t; the absolute-value maximum is convex; q is affine. Thus endpoint reduction is valid for each fixed H before completing the square, even if A is negative. Both density endpoints are retained for negative gamma. Positivity of every q is checked and failure stops execution rather than certifying a cell.

The prior raw ceiling T licenses
`phi_- = phi_l (1−T/(42 c_- rho_l))>0`. This uses the prior bound for the same law and cell. It does not use the smaller conserved-resource bound in place of the raw remainder. The newly completed raw quadratic is first intersected with the prior raw ceiling. Only afterwards is the new value used in

\[
\eta=(c_-\rho_l-T_{\rm new}/42)/2>0.
\]

Indeed, with `e=exp(−H²/(2n))` and `M_c=c rho−phi(0)D/6`, conservation gives

\[
eM_c\ge c\rho-T_{\rm new}/n>0,\qquad
n(1-e)M_c\ge\tfrac12H^2(c\rho-T_{\rm new}/n)\ge\eta H^2.
\]

Consequently the nonnegative conserved resource S is at most `R_c−eta H²`. Completing the two new quadratics with `q+eta` bounds S, and `D<=6S/(42 phi_l)` has the correct direction. The stronger invariant is also `nD<=6S/phi_l`: evaluation at floor42 does not set the actual sample index equal to42. Its validity for all n>=42 still requires the retained all-index LOW/HIGH estimates. Negative complete raw/resource envelopes can exclude a cell because the conserved identity gives their nonnegativity at an actual witness; a merely negative individual coefficient cannot.

## Same-law contractions and signed cost bounds

I checked the new code against `manuscript/arxiv-v1/appendices/fourier-analysis.tex:1748–1981`, including the following derivations and interval directions.

1. With `a_+=(1+beta)/2`, `a_-=(1−beta)/2`, `b_+=(rho+gamma)/2`, `b_-=(rho−gamma)/2`, the same positive first moment m satisfies `m²<=a_+a_-` and `m b_±>=a_±²`. The gamma interval, lower m endpoints, and signed Cauchy lower fourth moments all use the appropriate opposite interval endpoints. The fourth projection bound is `M4>=rho²+(gamma−rho beta)²/(1−beta²)`; the code's distance to the whole interval for `gamma−rho beta`, and its upper denominator `1−min|beta|²`, weaken it safely.
2. The support-localizing matrices successively give the probability, fourth-moment and fifth-moment deductions. In `fmean`, positive-part numerators are lower bounds and support-deficit denominators are upper bounds. The function is increasing in m, so the bisection preserves an upper endpoint. A zero denominator drops a nonnegative correction unless a separately positive numerator proves impossibility. The later fourth/fifth formulas retain this direction and the same m. Rounding is outward before making a new closed m cover.
3. The added lower bound `m>=max(0,(sigma_l rho_l−gamma_u−d)/6)` follows from `D>=sqrt(10)rho−gamma−6m`. It implies `beta²<=1−4m²`. The implementation rejects only an impossible forced m above1/2 or an empty beta intersection. It resets `bl,bu` from `bl0,bu0` for **every gamma subcell**, then recomputes bmin, mU and sign-moment bounds. The earlier gamma enclosure remains wider, which is harmless. There is no contraction carried improperly from one gamma subcell to the next.
4. For `delta=gamma−rho beta`, weighted Cauchy under `|X|dP` gives
   `delta²<=2m(M5−2rho M4+rho³)`. Therefore the constant loss is at least `delta²/(8m)`. Its interval implementation uses the lower squared distance and upper m. The two other square-completion losses are independently valid; taking their maximum is allowed, summing them is not. The program takes the maximum. Its other complete constant branch follows from `J1<=M4/2` and `−3J2−M5/4<=0`; the minimum is between complete upper bounds.
5. The signed K1 interval retains Cauchy lower fourth moments on each sign, support upper fourth moments on the other sign, and both signs of rho*gamma. The charge `3 beta(J+gamma)/2` is maximized jointly over the signed box. These are enclosures of one actual law, not realizability assertions about independent endpoint maxima.

## Gap event, endpoints and signed integrals

The actual gap is used only after `d<(sigma_l−1)rho_l`. At zero in closed support the outer-gap identity would force `D>=(sqrt(10)−1)rho`, so this strict gate licenses the nearest negative and positive endpoints A,B. Put `P0=(sigma_l−1)rho_l−d`. The gap decomposition gives

\[
A^2+B^2\ge(\rho-D/(\sigma-1))/m,
\qquad 6mAB\ge P_0.
\]

Adding these lower bounds proves exactly the implemented

\[
(A+B)^2\ge
\frac{\rho_l-d/(\sigma_l-1)+P_0/3}{m_u}>0.
\]

The event remains the actual opposite-sign pair of iid copies. Cauchy bounds p and1−p using the same m and sign second moments. The conditional squared distance is
`(1+4m²+beta)/(2p)+(1+4m²−beta)/(2(1−p))`; positive numerators make it convex in p, and it is affine in beta. The maximum at the stated corners is thus valid. The code intersects it with the unconditional upper bound `2/event_probability`. Complete six-term HIGH and its positive damping gates remain present.

The endpoint root for B comes from
`D>=(sigma−1)b_++6a_+B−(sigma+5)mB²`; the reflected version has sigma+1 and sigma+7. Lower positive coefficients, an upper quadratic coefficient and a lower square root produce the asserted necessary lower endpoint. If the positive constant does not exceed d, returning zero is weaker and valid. The asymmetry-square lower bound uses the distance between complete endpoint intervals and appropriate sigma root directions. The outer budget is `d−m_l*Q_lower`, not d again.

For the central constant, `G(A,B;rho)<=G(A,rho;rho)` increases with A and is convex in rho, giving the implemented upper A and rho endpoints. The separate outer charges retain positive/negative sign weights. The P1 central signed integral is minimized at the lower B and an A endpoint, maximized at the upper B with A clipped to B; the multiplier switches between m_l and m_u when the bound is negative. This sign switch is implemented. All these refinements use already acquired endpoints and budgets; none supplies a gap from a failed initialization.

## Support and coverage

`signed_support.py` retains the exact v5 `entry.tex` heat estimate and whole-ray derivative gates. For the actual invocation its R lies in `[5/2,96/25]`; A>0, `0<H4<36A`, Q<0 and the six Q/L derivative gates are checked before accepting a radius. The polynomial at the boundary is strictly negative. The beta enclosure uses the outer square-root endpoints. A radius is selected only after these sufficient inequalities hold for the entire rho cell. No Fourier value or optimization output is used to infer support. This is a valid parameterized specialization of that proof, conditional on its contact and predecessor premises; it is not validation of an arbitrary-radius API outside the invoked interval.

The driver constructs all24 original closed rho cells. Each stage partitions a whole beta enclosure, a necessary gamma enclosure, and then a necessary common-m enclosure into closed intervals. All exclusions are sufficient contradictions. Degenerate intervals can cause duplicated boundary work but not holes. The active-plus-excluded accounting remains `nr*nb*ng*nm`; dropping an enclosing box before its inner loops counts every descendant. Entire rho rows are retained as excluded only after a pass has no active signed box. All100 closed probability panels are considered for each surviving box's actual sign-probability interval. This does not prove a final count comparison on those panels.

## Corrected initialization and fresh structural check

Earlier signed runs initialized through `gap_check.run -> combined_check.step -> phase_check.envelope`, so they retained the full exponential-phase ancestor and six HIGH updates. That finding was reported before the driver changed. The frozen new driver, lines23–28, dynamically loads the unchanged `signed-two-pass-check.py` and calls `run(moment_check.py)`, then takes `row['passes'][-1]['raw']` and `['defect']`. The alternative branch remains explicitly selectable as `full-phase`; it is not reached by `signed07`. The selected quadratic ancestor performs its original closed24-cell check and two ordered passes, with its pinned signed and circle modules. There is no call to `gap_check` or `phase_check.envelope` in this selected path.

`signed_review_structure.py` is a new standard-library checker which imports no constructor. It compares the live/snapshotted three source hashes, reads the saved successful `signed07` result, and independently reconstructs all six passes' ordered raw/defect states starting from `signed-two-pass02`'s saved per-cell output. It checks all24 identities at every pass, exact parent values, closed rho endpoints, signed-box cardinalities, excluded-reason totals, outward rounding, monotone retention, all final states and every reported peak/count. It does **not** recompute numerical leaf bounds from their coefficients.

Fresh evidence is in `runs/fixed-target-v7-20261027/signed-review01/`. Return code0, empty stderr, and five rejected mutations (missing rho row, duplicate identity, wrong parent raw value, false peak, lost signed-cell count) are recorded with input/checker/output hashes. A total of14848 signed boxes is accounted for across the six passes. The independently reconstructed final summary is

\[
\mathcal R_c\le\frac{42891723}{20000000}=2.14458615,
\qquad D\le\frac{74519531}{100000000}=.74519531,
\qquad\rho\le\frac{71527}{48000},
\]

with14 surviving rho cells, all14 below the named .784 defect target. The constructor's recorded return code is0; that is constructor execution evidence, not an independent signed-kernel rerun. No expensive campaign was run in this review.

**Verdict.** The reviewed new transport supports the stated conditional acquisition improvement and the simplified selected ancestry. It crosses the two displayed raw/defect numbers. Preserve all other local-comparison premises, the complete Fourier inputs, weighted resource interfaces, exact zero-noise case, finite-base obligations and final certificate scope. No existing numerical family is authorized for deletion by this report.
