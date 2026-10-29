# One probability panel: acquired strip and a strict confinement obstruction

Date: 2026-10-28. Branch: `research/v8-confinement-20261028`.
Parent commit: `2012ee6480efa93ef4ddc99acae3b95b9b0af416`.
The immutable source baseline remains `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
This is an addition-only bounded research result; no old target, certificate,
driver, or manifest is changed. All paths below are repository-relative.

## Result and boundary

For an actual fixed-target maximizing law at every `n >= 42`, with
`c = CE`, nonnegative excess, sharp predecessor `C_(n-1) <= c`, initial
support `|X| <= 96/25`, and the acquired **same-law** panel

\[
 0.41\le p\le0.42,\qquad \theta\le0.27,\qquad nD\le42(0.7),
\]

the new proof gives

\[
 \theta<0.054,\quad d<0.069,\quad \rho<1.218600,
 \quad0.09736\le\beta\le0.234,\quad\ell>1.9706,
 \quad\lambda<0.575188<0.6,
\]
\[
 \operatorname{supp}X\subset(-1.8,2.325),\qquad
 \operatorname{supp}Y\subset(-0.6,1.6),\qquad |U|<0.6.
\]

Here `X = ell(Y-p)`, `Y = B+U`, `E(U|B)=0`, `theta=E(X-E[X|B])^2`,
`lambda=n E U^2`, and `d=1-(A+B)/ell` is the normalized inward
displacement of the **actual** central gap `(-A,B)`. The physical defect is
`D=(3+sqrt(10))*rho-gamma-3J`. The weighted bound on `nD` is essential for
the all-index noise bound. The initial radius, moment iteration, support
improvement and subsequent diagnostic are applied in that order.

| Claim | Mathematical status | Execution status |
|---|---|---|
| Four same-law moment contractions and weighted noise bound | Locally derived, conditional on the displayed acquired input | Fresh exact rational checks; all directed square-root gates pass |
| Extended signed heat envelope for `u>sqrt(3)` | Locally derived from the retained expansion by using `abs(H4)` | Two strict boundaries and all twelve whole-ray signs pass |
| Entire-panel `|U|<0.6`, `d<0.069` | Conditional theorem, including both signs and zero noise | Fresh component PASS |
| Entire-panel `|U|<0.5` by the selected retained confinement formulas | Unproved; this invocation fails | 128 boxes, 4 resource exclusions, 195 failed gates among 248 ray gates |
| Buffer-independent obstruction at `H=5/4`, `lambda=3/20` | Exact obstruction to these error majorants with the fixed envelopes; not an actual-law counterexample | Fresh exact inequalities, for every permitted buffer and nonnegative tangent parameter |
| Frozen entry object's Fourier meaning | Acquired numerical premise in this note | Hash/structure checked; its producing computation is not rerun here |
| Full INITIAL42/LOCAL42, finite base, sharp global theorem | Not established by this note | No native acceptance or generation run |

The proof is `confinement-proof/confinement.tex`; the standard-library
acceptance/diagnostic is `confinement_check.py`. The final invocation has
the deliberately scoped status
`PASS_CONDITIONAL_PANEL_STRIP_WITH_UNRESOLVED_HALF_AMPLITUDE`.

## Source edges and exact hypotheses

1. **Contact and support.** `mathematics/strategy-v4/2026-10-27/excess.tex:107–165`
   gives closed-support fixed-target contact. Lines 171–208 give the support
   inequality with the favorable extra `-n*excess`, assuming the same-law
   sharp predecessor. We retain these premises; we do not replace `c` by an
   actual-score upper bound. Differentiation of the contact polynomial removes
   the additive excess constant. It does not supply deleted-score bounds.
2. **The common moment cost.**
   `mathematics/fixed-target-v5/2026-10-27/response-proof/response.tex:89–115`
   supplies the signwise variance-measure identity. The new proof rederives
   it from outer gaps and conditional centering, and uses it for all four
   contractions. Both sign measures and all moments refer to one marginal.
   We discard the nonnegative binary square; the present panel contains
   `p*=(4-sqrt(10))/2`. We do not assume a product-law realization for a
   relaxed resource optimizer.
3. **Heat expansion.** `manuscript/arxiv-v1/sections/04-support.tex:36–65`
   gives the four Taylor remainders. Their nonnegative `u^2-1` factor permits
   `u>sqrt(3)`. The old simple envelope at lines 68–98 assumes `u>=2.5`
   because both retained coefficients are then positive. Here the cubic is
   still positive, but the quartic may be negative, so we use its absolute
   value. We do not apply the old positive-quartic statement outside its
   domain. Lines 104–145 supply the scaling and derivative ray argument.
   At the negative boundary the beta coefficient is `-beta_lower`; at the
   positive boundary it is `beta_upper`. Each cubic coefficient is checked
   negative before multiplying by `c_lower=0.4095`.
4. **Actual floor and strip.**
   `manuscript/arxiv-v1/appendices/uniform-bridge.tex:14–43` requires the
   actual acquired strip in the conditional cubic gate. Our gate uses
   `sigma=0.6`, not the old `0.55` or `0.575`. Lines 45–93 provide strict-gap
   concentration at **both** `n-1` and `n-2`, hence floor 40. The concentration
   branch used here has no extra deleted-score premise; the sharp
   predecessor remains necessary for the preceding support acquisition.
   The alternative score branch would retain both deleted-score caps.
5. **Confinement algebra.**
   `manuscript/arxiv-v1/appendices/fourier-analysis.tex:3098–3148` retains one
   resource and one marginal. Lines 3150–3202 prove strict-gap antichain
   concentration. Lines 3210–3255 retain signed deletion, conditional
   centering, strict pair events, and atoms. Lines 3257–3319 supply the
   slope construction; our copied algebra uses `0.4095 <= c <= 0.40974` in
   place of the wider old multiplier interval. On the negative half-line
   the sign of the completed-square coefficient is explicitly checked;
   on the positive central interval `rho>=1` gives
   `rho*t-t^2 >= -t*(t-1)`. All lower beta coefficients here are positive.
6. **Geometry and errors.** The same Fourier file at lines 3327–3374 gives
   the two exterior geometries and strict-gap alternative. The old upper
   buffer `7*r0/15` fails `d0+2*tau<r0` at `r0=1/2,d0=.069` and is rejected.
   The new diagnostic uses `tau=1/5`, verifies the whole-strip widths and
   positivity `1-sigma-2*d0`, and covers both signs of the raw threshold.
   Lines 3376–3456 give the resource simplex and old/tangent error families.
   `uniform-bridge.tex:126–154` explains the inverse-index sign gates and
   why a minimum of individually valid resource bounds remains valid.
   These are necessary analytic inputs to the diagnostic, not a claim that
   the old numerical invocation was accepted at new parameters.

The diagnostic uses a new joint phase resource derived from a raw ceiling:
`B(H)=T-eta*H^2`, `T=2.016`, `eta=(c_lower-T/42)/2`, and

\[
 (n+H^2)\mathfrak a+n\phi(0)D/6+n^{3/2}L_{\rm leak}<B(H).
\]

This is the fixed-target Gaussian phase-price implication, not a deduction
from a stand-alone maximum of `D`. It retains the same law, threshold and
nonnegative leakage. The raw ceiling and its analytic enclosure are explicit
additional premises of the attempted half-amplitude step. The zero-noise
case has `U=0` by conditional centering and is handled without division.

## Why the half-amplitude attempt fails

At the exact singleton `H=5/4`, `lambda=3/20`, the upper contact side of
these scalar inequalities is `0.21605838825956997`. Geometry permits only
`0<tau<(1/2-.069)/2=.2155`. For every such buffer, every old error majorant
and every tangent error majorant with tangent parameter `t>=0` is at least

\[
 f(\tau)=A_0/42+A_1\tau/42+K/\tau.
\]

The last term is forced by the leakage vertex of the common simplex, whose
displacement coordinate is zero. The exact inequality
`A1*tau_max^2/42<K` proves that this floor decreases on the entire allowed
interval. Even at its excluded endpoint it is
`0.23161994089452626`, exceeding the contact side by
`0.015561552634956285`. Thus neither a finer mesh, another upper buffer,
nor additional nonnegative tangent parameters can make **these fixed
envelopes and error formulas** prove the desired upper contradiction.
This statement lower-bounds upper bounds; it does not lower-bound the true
probabilistic error or construct an extremizer.

The present resource is `B(5/4)=1.733578125`. Holding the other envelopes
fixed, removal of this leakage-vertex obstruction requires a resource below

\[
 \frac{298994662346001336406398218971185928048592767}
 {186832396094022358570345000000000000000000000}
 =1.600336283197556\ldots.
\]

That is a necessary condition for this attempted proof, not a sufficient
condition for confinement. A next bounded computation can export the
phase quadratic of each **same active moment cell** and its probability
incidence, then evaluate the joint resource at this phase. Favorable
separate maxima of `D` and `H` cannot be combined into that input.

## Reproduction and adverse controls

The input `confinement-sources/entry-proof.json` is a frozen copy of the v7
entry object, SHA-256
`61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae`.
It is bound as a complete ordered 100-panel table. Only nonempty panel 41
is used mathematically here; its 432 source incidences are not reaccepted.
Its recorded bounds are `D=17495769/25000000`,
`theta=5389533/20000000`, `raw=100753331/50000000`, and
`H=181363117/100000000`; each is strictly below the rounded ceiling used
above. The checker verifies the five analytic-source byte pins; this
identifies sources but does not prove them.

Actual arithmetic command: unoptimized Python 3.9.6 running
`mathematics/fixed-target-v8/2026-10-28/confinement_check.py` from this
worktree. Final receipt, exact rational stdout, empty stderr and script
snapshot are under `runs/fixed-target-v8-20261028/confinement03/`.
The receipt records return code 0 and elapsed time 0.1497509479522705 s.
Checker SHA-256 is
`2ef7e9c9eb28482af904ad502ebd5044e612d364a449e42f89a44a7586ff4bce`.
`confinement01` and `confinement02` preserve earlier bounded invocations;
the former tested amplitude .49, the latter .5. They are not overwritten.

The eight fresh rejection controls cover missing and reordered panels,
an understated defect input, duplicate JSON keys, false positive radius
2.3, wrong beta sign on the negative ray, reuse of the invalid old upper
buffer, and a false claim that all half-amplitude gates pass. There is no
generic API accepting unverified receipts. The trusted arithmetic stack is
Python integers/Fraction and `isqrt`, with explicit outward-root inequalities.
No archive program, native checker, expensive generation or external write
was performed. Compilation and page inspection are recorded separately in
`runs/fixed-target-v8-20261028/confinement-build01/`.

The next numerical contraction and all final count/comparison obligations
remain open here. No existing computational family is made unnecessary by
this one-panel result alone.
