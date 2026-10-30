# Independent review of the revised count argument

This review reconstructs the changed arguments from `sections/08-direct-comparison.tex` and its stated hypotheses. The constructor's review note was not used. The new checker was inspected but not imported by the independent calculation below.

Reviewed SHA256 values:

- `sections/08-direct-comparison.tex`: `ebbfd05de0424e00d85dc6a8f445f84ea01c3ecd79d8afa4ada3867003f76098`
- `tools/check_revision_count_constants.py`: `eb55bfd92bd3975dd904f1440d8a0a06ac286fd7d6e333388cf7c4f318bd9454`

## Conclusion and boundary of the review

No defect was found in the changed finite summation lemma, the new `alpha=1/2` minorant and rectangle argument, or the single-quartic envelope. They preserve the common-strip theorem's hypotheses and conclusion. The proof still treats zero noise separately, retains the complete incoming and curvature tails, and needs the cited strict finite-binomial theorem as an external input.

| Component | Mathematical status | Execution status |
|---|---|---|
| Finite interpolation identity and its boundary terms | Independently derived below under the displayed support/threshold assumptions | Fresh exact diagnostic checks at 11 thresholds, 10 of them actual atoms |
| Global minorant and shifted moment bound | Independently derived below; applies to an unbounded conditional sum with finite fourth moment | Four edge minima and derivative signs independently recomputed with `Fraction` |
| Common error envelope and concavity | Independently derived coefficient cancellation and differentiation | Both rational endpoint values independently reconstructed from the displayed constants |
| Whole retained count proof, external Schulz theorem, entry and finite base | Not newly re-proved by this bounded review | No claim of a new global theorem, external-theorem verification, or finite-base acceptance |

A fresh arithmetic check verifies the displayed finite calculations. It does not replace the analytic implications reconstructed here. No changes were made to the manuscript or checker during this review.

## 1. Finite summation and all boundary terms

Let `t=np+w=k+u`, with `|w|<xi`, `p>=r`, `q>=r`, and `a0,a1<=d`. Since `n(r-d)>=N(r-d)>xi`,

` t-na0 = n(p-a0)+w > 0`,

` n(1-a1)-t = n(q-a1)-w > 0`.

Thus `T0<=na0<t<n(1-a1)<=Tn` almost surely. Conditional centering gives `E T0=0`, so `L0=E(t-T0)=t`; similarly `Ln=0` and `P(T0<=t)=1`. This also places `t` strictly between 0 and n, making the anchor and interpolation indices legitimate. The text's weaker `na0<=t` is therefore sufficient and valid.

For `1<=i<=n`, the variable `Vi` omits coordinate i. Its independence from the fresh conditional noise gives exactly

`g_i = L_{i-1}-L_i-P(T_i<=t)`.

Multiply by `pi_i` and sum. The complete sum is

`P(sum X_i<=H) = pi_0 + pi_1 L0 + sum_{j=1}^{n-1}(pi_{j+1}-pi_j)L_j - pi_n Ln - sum_{i=1}^n pi_i g_i`.

Substituting `L0=t`, `Ln=0`, and `L_j=(t-j)_++B_j` leaves every term in the printed lemma. The deterministic part telescopes as

`pi_0+pi_1 t+sum_{j=1}^{n-1}(pi_{j+1}-pi_j)(t-j)_+ = F_B(k)+u*pi_{k+1}`,

which is precisely `(1-u)F_B(k)+uF_B(k+1)`, including `u=0`. The endpoint `i=n` remains in the loss sum and is not silently dropped. Jensen gives `B_j>=0`, since `E T_j=j`. All probabilities in the identity are closed; the defining kernel subtracts the same closed probability `P(1+U1<=x)`, so atoms cause no discrepancy.

The separate nonnegativity argument for `g_i` is also consistent. Below `1-a1` the second positive-part term and closed probability vanish, giving `h(x)=E(x-U0)_+>=0`. At and above `1-a1`, one has `x>a0` and put--call parity gives `h(x)=P(D1>x)-E(D1-x)_+`, where `D1=1+U1`. Since `x>A` and `D1<=1+A`, the positive difference `D1-x` is smaller than one, so this expression is nonnegative. The boundary `x=1-a1`, where an atom may enter the closed event, is handled by this second formula. No continuity assumption on a CDF is used.

An optional expository improvement would be to print the two threshold differences `n(p-a0)+w` and `n(q-a1)-w`; this is not needed to repair the proof.

## 2. Global minorant and finite fourth moments

The new quartic is

`h(x)=(4/5)x(1-x)(2x+1)^2`.

It is nonpositive on `(-infinity,0]` and `[1,infinity)`. Its derivative is

`h'(x)=-(4/5)(2x+1)(8x^2-4x-1)`.

Consequently the only critical point in `(0,1)` is `(1+sqrt(3))/4`. Direct substitution gives the maximum `(9+6sqrt(3))/20<1`, because `108<121`. This proves the pointwise bound on the whole real line, including `h(0)=0` for the strict event. It does not require the conditional sum to stay in the individual summand support.

For independent centered summands bounded in absolute value by `A`, a sum W of variance t obeys `|E W^3|<=At` and `E W^4<=A^2 t+3t^2`. The third identity follows by summing the individual third moments; the fourth follows by retaining the individual fourth moments and the pairwise variance products. Thus W has the fourth moment required for integrating h. These facts hold for the actual conditional sums in the theorem.

Set `r=zt`, `M=5/16`. Expanding `h(W+r)` and dividing by t gives the following lower bound, using the adverse sign of the third moment:

`(3/4-A^2-3t)/M + (4/5-4At/M)z + ((3/4)t-6t^2)z^2/M - t^3 z^4/M`.

For `h(W-r)` only the linear `4/5` changes sign. The normal increments supply `-101z/100` in the negative phase and `+99z/100` in the positive phase. This independently recovers both printed `F_{epsilon,b}` functions with their correct signs.

For every fixed `z>=0`, `F_tt=-(12z^2+6tz^4)/M<=0`; hence the entire t interval is controlled by its two endpoint functions. On `0<=z<=3/2`, the inequality `z^4<=(9/4)z^2` gives the claimed lower quadratic. Its coefficient is nonnegative at both t endpoints, so the largest derivative in the negative-phase case occurs at `z=3/2`, and the smallest derivative in the positive-phase case at `z=0`.

The independent exact calculation gave:

| Phase | t | Tested derivative | Lower-quadratic minimum |
|---|---:|---:|---:|
| Negative | 0 | `-21/100` | `933/1000` |
| Negative | `101/10000` | `-275932538127/1250000000000` | `3849022385619/5000000000000` |
| Positive | 0 | `19/100` | `156/125` |
| Positive | `101/10000` | `7027/62500` | `3597/3125` |

These verify both the monotonicity directions and all printed lower bounds. Every minimum exceeds `3/5`. Concavity in t, not a sample over t, then proves the whole rectangle. The later Cantelli switch and incoming-tail budgets are unchanged, and the preserved own-count conclusion `O>.59 lambda` leaves the same final `lambda/100` margin.

## 3. One envelope and one concave quartic

Subtracting the two error envelopes directly cancels `T/4`, their common fourth-moment term, and `phi_+*2/27`. The remaining constant and linear terms are

`(41/100)(79/200)(1/5)+(2/5)(93/100)/8 = 7889/100000`,

`(41/100)(79/200)(5/2)-(2/5)(93/100)/2 = 1751/8000`.

The residual fourth-moment contribution is positive for positive lambda and nonnegative at zero. Thus the printed identity proves `E_->E_+` for every `lambda>=0`, and choosing `E=E_-` is a valid common upper envelope. This retains both distinct normal-correction arguments; it does not assume their signs coincide.

Every coefficient of E is nonnegative, and its quadratic coefficient is positive. Independently differentiating W gives

`W'' = -eta*m_* [ (z^2/4)((z lambda-1)^2+1) + 3b^2/8 ] < 0`.

Therefore `P=W-E/700-lambda/100` is strictly concave. Direct reconstruction from `z=1041/350`, `b=703/700`, `T=200 lambda/107`, and the other displayed rational constants gives

`P(1/100)=19409025049390417531054861/8386908849900000000000000000 > .002314`,

`P(7/20)=16788798784733560132189/273858248160000000000000 > .061304`.

A concave function lies above the chord joining the endpoints, so P is positive on the complete closed interval. Since `E>=0` and `n>=700`, replacing `E/n` by `E/700` has the required direction. Combined with the already strict binomial comparison, this retains the theorem's strict conclusion.

At lambda zero, `W(0)=0` whereas `E(0)>0`. The revised explanation correctly says that this estimate cannot cover all tiny positive noise; the single-count proof remains necessary. Neither argument loses the common endpoint `lambda=1/100`.

## 4. Independent execution and checker semantics

A fresh one-off `python3 -I -B` calculation using only `fractions.Fraction`, `math.comb` and `itertools.product` recomputed the four rectangle rows and both quartic endpoints above. It did not import or execute the constructor's checker. Its return code was 0.

For the finite-sum diagnostic it used `n=4`, `p=2/5`, `a0=3/1000`, `a1=1/1000`, `A=3/5`, with the centered two-point conditional laws

`U0: (-A, a0/(A+a0)), (a0, A/(A+a0))`,

`U1: (-a1, A/(A+a1)), (A, a1/(A+a1))`.

It convolved each conditional sum separately, computed h directly from the two conditional laws, integrated h over each omitted-coordinate sum, and compared both sides of the finite identity. The thresholds were 1, 2, 3 and all atoms of T2 lying between `n a0` and `n(1-a1)`. All 11 comparisons were exact; 10 thresholds were actual atoms. This checks the identity and atom conventions, not the `n>=700` comparison theorem.

The constructor's new checker computes rational quantities from the displayed definitions, rather than merely comparing copied constants. Its polynomial operations use exact rational arithmetic. Its global-minorant code checks the factorization and last square comparison, while the critical-point argument remains an analytic premise in the manuscript; this separation is accurately described. Its in-memory corruptions test its predicates, and its finite-law tests are correctly labeled diagnostics. The diagnostic example with a summand of size one concerns the global minorant, so it need not satisfy the local theorem's `A=3/5` support assumption.

The checker does not replace the retained incoming-tail proof, the finite-sum derivation, or the analytical use of concavity. The existing historical checks concern the old scalar choice; the new checker and the independent calculations here support the changed scalar steps. Final source-bound replay and document compilation remain coordinator integration obligations.
