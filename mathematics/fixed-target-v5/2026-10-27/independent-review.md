# Independent review of the count-cost reduction

Reviewed the constructor's `count-cost.tex` and `count_cost.py` in the separate `count-cost-v5` worktree. Their exact byte hashes are recorded in `runs/fixed-target-v5-20261027/count-review01/receipt.json`. This review concerns that count-cost argument, which this reviewer did not construct. It is separate from the entry proof constructed in this worktree.

**Verdict:** no blocking mathematical defect found in the stated component theorem. The replacement is a valid domination of the old curvature contribution under the same actual-law coupling, moment, phase and sign hypotheses. It is suitable for inclusion as a conditional research reduction. It is not a fresh acceptance of any complete LOCAL42 LOW cell or of its acquired inputs.

| Result | Mathematical status | Execution status |
|---|---|---|
| Disjoint quadratic crossing cost | Independently rederived for all integer crossings and every stated phase | Own bounded exact tests PASS |
| Fourth-moment crossing price | Independently rederived from the existing fourth-moment hypothesis; cubic alternative retained | Own bounded exact tests and rare-atom negative control PASS |
| Exact three-candidate phase maximum | Independently differentiated, with all endpoint/kink cases included | Own bounded rational phase diagnostics PASS; sampling is not the proof |
| Clamp and fixed-noise endpoint join | Independently checked against the manuscript's whole-count formulas | Exact negative clamp control PASS; no native LOW execution |
| 3,648 source cells / 152 signed configurations / measured gains | Constructor's bounded diagnostic claim; not independently reproduced by this reviewer | Constructor execution only |
| Complete local or global exclusion | Not established by this reduction | Not run |

## Independent derivation

The construction uses one independent family of centered conditional residuals `U_(0,i),U_(1,i)`. At each count j, its marginal sum is the genuine conditional sum; using the same coupled arrays for all j is legitimate. Constant extension of `V_j` outside legal counts gives increments one there. Within `[0,n]`, increments of `j+V_j` are at least `c=1-a0-a1`. Thus `1/2<c<=1` proves strict monotonicity everywhere and guarantees a unique finite integer inverse crossing. The independent binomial selector gives the same mixture CDF as the actual conditional decomposition, including closed endpoint events and selectors 0,n.

For the discrete binomial inequality, I derived the finite-difference relation directly from the adjacent-mass ratio. When `(n+1)p-j>0`, its denominator `p(n-j+1)` is at least `(n+1)p(1-p)`. For `r>0`, double summation gives weights `r-i+1` at `j=k+i`. Since `chi<2`, only i=1 can have a positive numerator; its weight is r. For `r=-h`, the weights are `h-1-i` at `j=k-i`, and

`sum_(i=0)^(h-2)(h-1-i)=binom(h,2)`,

`sum_(i=0)^(h-2)i(h-1-i)=binom(h,3)`.

Using `(chi+i)_+<=chi_++i` proves the stated inequality. Zero extension gives the correct negative difference at `j=n+1`; it must not be evaluated by the mass-ratio expression with a zero denominator. The proof only bounds its positive part, so this boundary is harmless.

On `R=r>=1`, monotonicity gives `-V_k>=cr-u>0`. The difference

`(cr-u)^2-r(c-u)^2=(r-1)(c^2*r-u^2)>=0`

is valid because `|u|<=1/2<c`. On `R=-h<=-2`, the count `K+1` fails the **closed** event, so the strict relation is `V_k>c(h-1)+u>0`. With j=h-1, differentiation of `j(j+1)/(2(cj+u)^2)` has numerator `j(2u-c)+u`. This is nonpositive for j>=1 when u<=c/3; for larger u, replacing it by c/3 only increases the upper bound. These give the two quadratic prices. Their events are disjoint, so their weighted sum is at most the **maximum** of the coefficients times `V_k^2`. It is not bounded by their minimum.

For h>=3, j=h-1>=2. The derivative of

`(j^3-j)/(6(cj-1/2)^3)`

has numerator with the sign of `2cj-(3j^2-1)/2`. It is strictly negative for c<=1 and j>=2: at c=1,j=2 it is -3/2, and it decreases as j grows. The maximum is therefore its j=2 value, `1/(2c-1/2)^3`. In this event `V_k>2c-1/2=d`, which gives the new fourth-power upper bound. Other crossings have `binom(R_-,3)=0`; it would be wrong to require the event-only inequality `V_k>d` globally.

For the n independent centered summands of `V_k`, the fourth moment is exactly the sum of individual fourth moments plus six times the variance cross-products. Bounded amplitude gives

`E V_k^4 <= A^2*t+3*t^2 <= t*(A^2+3T)`.

Cauchy yields `E(V_k)_+^3<=t*sqrt(A^2+3T)`. Taking the smaller of the resulting cubic and quartic prices is valid. This includes t=0 without dividing by t; at t=0, the centered sum is zero almost surely. Both price choices remain available on either side of `A^2+3T=d^2`.

For the phase maximum, the first branch is nondecreasing on its positive region: its derivative numerator `c+u+2b-2` is greater than `c-u>0`. The second branch below c/3 has derivative `(c-2b-u)/(c+u)^3`; above c/3 it is nondecreasing. The kink at c/3 can be a local minimum or an increasing join, not a missing interior maximum. Thus the only interior maximum is at `u*=c-2b`, when the stated eligibility conditions hold. At this point its value is `1/[4(c-b)]`, and `b+u*=(c+u*)/2<=3/4`, so the first branch vanishes. This independently gives the endpoint-plus-stationary formula, including singleton intervals, u=+-1/2 and c=1. The lower endpoint c=1/2 must remain excluded because denominators can vanish.

Both branches decrease as c increases; the clamped denominator `c+min(u,c/3)` is continuous and increases in c on each of its pieces. Consequently a previously valid cache at a smaller acquired c remains conservative. The proof does not authorize a cache across unrelated rows or different phase/threshold intervals.

## Joining the local formula

I checked the manuscript at `manuscript/arxiv-v1/appendices/fourier-analysis.tex:4020–4062`, especially the formulas for `V_0`, `B(lambda)` and `I(lambda)`, and `appendices/local42-refinements.tex:286–314`. For a fixed noise band, the valid upper amplitude, upper own-count variance, lower c, probability cell, threshold and phase intervals are frozen. The new prices therefore reduce the constant curvature part of `I(lambda)=A0+A1/lambda`, with `A1>=0`; they do not alter the sign-sensitive linear crossing term, the Gaussian repair or the positive reciprocal term in `B`.

The old `I>0` assertion need not survive a numerical improvement. The replacement `I_+=max(0,I)` is valid for n>=N and gives `I/n<=I_+/N`. The latter is convex in positive lambda as a maximum of convex functions; the full endpoint argument therefore remains valid, including a new interior zero kink. The negative event-bracket gate must still pass before using a lower binomial mass bound. The separate zero-noise binomial case remains outside this division-by-positive-noise argument.

The constructor clearly retains these conditions. No hidden acquisition of amplitude, c, T, binomial mass, a count displacement, or a complete signed cover follows from a smaller curvature coefficient.

## Checks actually executed

`count_review_check.py` is a new standard-library exact-rational program. It imports neither the constructor's checker nor an archived/native program, and it does not read the certificate payload. The fresh run checked:

* 4,340 integer-crossing parameter cases, including both phase endpoints, values near `c=1/2`, c=1 and h>=3;
* 13,365 direct finite-binomial difference inequalities for n=1..10, nine rational probabilities, legal k and crossings r=-16..16, subject to `chi<2`;
* 38,880 rational phase-grid diagnostics against a separately implemented two-branch maximum, with stationary-point attainment and singleton intervals;
* three negative controls: using the minimum of disjoint coefficients fails, omitting the individual fourth-moment term fails for rare atoms, and replacing a negative inverse-index coefficient by its value at N without clamping is invalid.

All checks passed with return code 0; stdout, stderr, Python version, exact command, wall time and source hashes are in `count-review01`. These are bounded diagnostics. The continuum and all-integer conclusions are justified by the derivation above, not by the grid.

No mathematical acceptance is inferred from the constructor's source-count statistics or from agreement between agents. The next integration step is to compose this component replacement with independently established acquisition and normalization premises, preserving the final strict exclusion target.
