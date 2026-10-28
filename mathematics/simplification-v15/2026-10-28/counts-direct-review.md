# Independent review: five-count reserve and signed right comparison

Review baseline `2c2c511ca1aecb5840d474608aba7c43d90db79e`; isolated branch `research/counts-direct-review-v15-20261028`.

This reviewer constructed the separate paired-count and anchor-obstruction notes, but neither of the two arguments reviewed here. The review rederives the compact minorant, centered replacements, physical variance, omitted-translate tail, weighted comparison and normal signs. Its checker imports neither constructor checker. It reconstructs the final quartics by rational interpolation of their defining formulas and evaluates actual bump expectations using a separate rational Machin/Taylor enclosure.

Reviewed sources:

- `loss-direct.tex`: SHA-256 `1bb19aee8183fbf70e81424dfb4503a54877a1938cd073bf58e751556e387ead`.
- `right-direct.tex`: SHA-256 `5946340c178bc54c5094fcde567ec2c260a1abd0d39daf16306dadbb12971d67`.

Both are under `mathematics/simplification-v15/2026-10-28/`.

| Result | Mathematical status | Execution status |
|---|---|---|
| Pointwise compact minorant of the separated-support crossing kernel | Independently derived; no blocker | Exact guards and outward pointwise controls PASS |
| Four centered replacements for five unequal conditional counts | Independently derived; no blocker | 20 fresh actual-law controls PASS |
| Frozen variance, characteristic function and entire omitted-translate tail | Independently derived; no blocker | Seven uniform table coefficients and negative controls PASS |
| Five binomial masses and increasing-side summable curvature | Independently derived; no blocker | Exact rational guards PASS |
| Both signed normal repairs, cubic sign and Bernoulli interpolation | Independently derived; no blocker | Exact formula reconstruction; primary source checked |
| Uniform signed right theorem for `n>=200`, `.075<=lambda<=.36` | Locally proved and independently reviewed at its stated scope | Four exact endpoint margins and concavity identity PASS |
| Acquisition, reflected-branch hypotheses and global finite base | Outside this review | No global conjecture or unconditional cutoff claim |

## 1. Compact kernel minorant

The separated supports imply the exact kernel formulas

`h(x)=E(x-U0)+` for `x<1-a1`, and

`h(x)=P(1+U1>x)-E(1+U1-x)+` for `x>=1-a1`.

For the first branch Jensen gives `h(x)>=x` when `x>=0`. For `B(x)=sin²(pi x)` on `[0,1]` and zero outside, `B(x)<=5x/2`: use the square bound for `x<=1/4`, the tangent at `1/4` on `[1/4,2/5]` (where sine square is concave), and `B<=1` above `2/5`. The tangent endpoint calculation uses only `pi<10/3`.

For the remaining interval `1-a1<=x<=1`, put `D=1+U1` and `L=E(D-x)+`. Since `L<= (8/5-x)P(D>x)` and `L>=1-x`,

`h(x)>=[(x-3/5)/(8/5-x)]L >=(41/84)(1-x)`.

Here `x>=116/125`; the ratio increases with `x`. Meanwhile `(2/5)B(x)<=(41/84)(1-x)` follows from `pi<22/7` and `1-x<=9/125`. Outside `[0,1]`, only kernel nonnegativity is required. The strict survival event remains strict at an atom of `D`; no endpoint probability is lost. Thus `h>=2B/5` globally.

The derivative of the compactly supported `B` vanishes at both joins and is globally Lipschitz with constant `2pi²`. Adjacent integer translates have disjoint open supports and matching zero derivatives, so their sum has this same Lipschitz constant. This is essential for the improved replacement count.

## 2. Four centered replacements, not six independent charges

Freeze `V=V_(k+1)`, consisting of `k` copies of `U1` and `n-k-1` copies of `U0`. For each `j=-2,...,2`, the actual omitted-coordinate sum `V^(j)=V_(k+1+j)` differs from it by exactly `|j|` conditional-law replacements. They are compared through distributions sharing an independent base; the original sums at different counts need not themselves be independent.

For a function whose derivative is `L`-Lipschitz, the centered Taylor bound is `|E F(r+Z)-F(r)|<=L E Z²/2`. Replacing `U0` by `U1` therefore costs at most `L(s0+s1)/2`.

Regroup the positive-side changes as one change for `B_1+B_2` and one for `B_2`; do the same on the negative side. There are four charges, each at most `pi²(s0+s1)`. The two-bump functions retain constant `2pi²` because their open supports are disjoint. This proves the actual five-count expectation bound with cost `4pi²(s0+s1)`, uniformly for unequal conditional laws. The coefficient `s0+s1<=5lambda/(2n)` produces exactly the displayed loss term `10pi²lambda/n` inside the factor `2/5`.

Eight of the independent actual-law controls have a strictly smaller sum of actual bump expectations than the fully frozen sum. Thus deleting the replacement cost is genuinely false; the review does not merely test the same expression twice. The corresponding strict rational lower gaps are recorded in the receipt.

## 3. The omitted translates and physical variance

For every real `z`, all integer translates of `B(u-j-z)` sum to `sin²(pi(u-z))`. With `0<=u<1`, any nonzero omitted translate `|j|>=3` requires `|z|>2`. At an integer join both neighboring bumps vanish. The sum of all omitted bumps is therefore at most `1{|z|>2}`, whose expectation is bounded by `E V⁴/16`. This covers the entire omitted tail, not a finite truncation.

Writing `delta=k-np in (-97/50,47/50)`, the frozen variance is physically

`tau=(nq-delta-1)s0+(np+delta)s1`.

Dividing these actual coefficients by `nq` and `np`, respectively, gives `(1-5/n)lambda<=tau<=(1+3/n)lambda`. There is no common-variance-allocation substitution. Independence and `|Uj|<=3/5` give `E V⁴<=(9/25)tau+3tau²`.

The conditional span is at most `84/125`; on that span `1-cos(2pi x)>=3x²`. Symmetrizing one conditional variable therefore gives `1-|phi_Z(2pi)|²>=6 Var Z`, and hence `|phi_Z(2pi)|<=exp(-3 Var Z)`. Multiplication uses only the independent frozen summands. It yields the periodic sine-square reserve `(1-exp(-3tau))/2`, uniformly in phase. Combining the preceding steps proves the exact five-count bound, including arbitrarily small noise and all threshold atoms.

The seven displayed uniform coefficients follow from concavity in `lambda`, the positive finite exponential sum `P6`, and monotonicity in `n`. The independent checker reproduces all seven strict rational margins. No table row is extended to smaller indices.

## 4. Binomial weights and summable curvature

For `n>=200`, the raw displacement is below `231/250`. The five count indices have `|i-np|<4`, so `i/n` and the segment to `p` lie in `[.38,.55]`, with variance product above `.23`. The explicit finite Stirling remainder gives the printed mass bound. Its numerical content is the rational inequality

`(199/250)[1-(8+1/12)/46] >13/20`.

All counts are interior. Multiplying the local reserve by this mass lower bound is legitimate because the actual five-kernel sum is nonnegative; all other weighted kernels are nonnegative as well. No distant conditional-count probability is discarded with an unknown sign.

The inherited summable-curvature lemma is applied only on the increasing side of the binomial masses. There `j<np-q`, so the actual conditional variance is at most `lambda/q <=(100/47)lambda`. This is a physical variance bound for the same conditional marginal. The corresponding fourth moment is at most `(9/25)T+3T²`.

The mode coefficient `.41` is valid on the whole right interval: for a mode of `Bin(N,p)`, `|m-Np|<=.6` and `|1-2p|<=.2`. Relative to `v>=.24`, this implies the displayed weaker ratio `r(1-r)>=v(1-1/N-2/N²)>39v/40`. Finite Stirling and `exp(1/(12N))<516/515` then give `.41/sqrt(Nv)`. The inherited curvature lemma includes both complete reciprocal-power tails. Its `c<=1` hypothesis holds here (`c<.46`).

## 5. Signed interpolation and the external theorem

The original primary source was inspected directly: [Schulz's dissertation](https://d-nb.info/1197702695/34), Theorem 1 on printed page 1 (PDF page index 10), states the strict binomial bound for every `0<p<1`, every positive integer `n`, and the closed CDF. After multiplication by `sqrt(n)`, its coefficient is exactly `C_E rho_B`. The stronger middle-probability theorem is not needed.

Convex interpolation of the two integer Bernoulli comparisons preserves this strict bound, including `u=0`. This is different from assuming the comparison at one prescribed floor anchor: the v15 counterexample to that assumption does not affect this interpolation argument.

For `G(z)=Phi((z-np)/sqrt(nv))`, the upper second-derivative bound on `[k,k+1]` is `phi(0)(u-w)+/(nv)^(3/2)`. The interpolation remainder multiplied by `sqrt(n)` is therefore at most

`phi(0)u(1-u)(u-w)+/[2n v^(3/2)]`.

For `H<=0`, the variance change from `v` to `v+s` is favorable; the displayed negative-side cost follows from `u(1-u)<=1/4` and `u²(1-u)<=4/27`. For `H>=0`, the interpolation cost has no `|w|` term, while the adverse variance change is at most `phi(0)ws/[2v^(3/2)]`. With `s=lambda/n`, this is exactly the positive-side `lambda/n` term. Neither normalization has a missing factor of `sqrt(n)`.

The marginal cubic expansion uses fixed signs on the two conditional supports and their actual inward third moments. It gives `(v+s)^(3/2)(rho-rho_B)>=s[87/250-(13/16)s]>0` throughout the domain. Therefore the cubic correction has the favorable sign at the positive coefficient `C_E`.

## 6. Four exact endpoints cover the continuum

The lower weighted reserve is the quartic `W`; both error terms `E_-` and `E_+` are convex quadratics with nonnegative coefficients. Put `z=3alpha`. Completing the square gives the global identity

`W''=-(13/50){ z²[(zlambda-1)²+1]/4+3b²/8 }<0`.

Thus `P_±=W-E_±/200-lambda/100` are strictly concave on the whole real line. Their minima on the closed interval `[3/40,9/25]` occur at endpoints. Independently reconstructed exact values exceed, respectively:

| Polynomial | `lambda=3/40` | `lambda=9/25` |
|---|---:|---:|
| `P_-` | `6075/10^6` | `2577/10^6` |
| `P_+` | `11528/10^6` | `11247/10^6` |

The checker reconstructs each quartic by Lagrange interpolation of its defining rational expression; its degree bound is analytic, not inferred from samples. It verifies the completed-square identity coefficientwise and, independently, checks all six degree-two Bernstein coefficients of the two second derivatives are negative. The exact endpoint fractions appear in stdout. This is a continuous-domain proof with no parameter subdivision.

Since `E_±>0` and `n>=200`, the full positive signed excess is strictly below `-lambda/100`. The statement retains all hypotheses listed in `right-direct.tex`; it does not supply its own support acquisition or reflected-branch conditions.

## 7. Fresh checks, controls and execution status

Run:

```sh
python3 mathematics/simplification-v15/2026-10-28/counts-direct-review-check.py --source-dir /absolute/path/to/the/v15/source/directory
```

The final fresh run is `runs/counts-direct-review-v15-20261028/check04/`: source snapshots, independent checker snapshot, stdout/stderr, versions, measured time, return code and hashes. It checks all seven uniform loss coefficients; reconstructs both right quartics; checks four endpoint margins and six derivative Bernstein coefficients; and uses 58 pointwise kernel controls plus 20 actual centered-swap controls at 20 legal raw thresholds. Actual laws include zero noise, equal symmetric noise, one noisy conditional law and unequal conditional noise. The bump evaluator uses exact Machin bounds for pi and alternating sine bounds with a Lipschitz enclosure for the angle interval. It imports no constructor code and uses no floating arithmetic for acceptance.

Eight actual-law controls reject freezing without a variance cost. Additional genuine controls reject deleting the omitted bump (one explicit omitted translate contributes `1/2`), dropping the conditional-diameter premise, and strengthening the normalized binomial mass bound to `4/5` at `n=200,p=1/2`. Disposable source mutations check fail-closed pin handling. An initial review-checker syntax failure is preserved as `check01/`; it was an implementation error in this independent test script, not a failed mathematical inequality. `check02/` passed before output fractions were rounded down for a compact final report; `check03/` uses those exact rational lower gaps.

The original loss-checker runner uses an isolated Python child without optimization. This review also requested a direct-entry optimization guard; the coordinator added it without changing the proof source or arithmetic. Existing receipts remain tied to their original checker bytes. The independent checker has its own explicit optimization guard.

No blocker remains within the reviewed scope. The constructor proofs were compiled and visually inspected by their owners; this review changes neither LaTeX source. No new certificate campaign, external repository write or manuscript edit was performed.

## Final endpoint wording repair

Before final acceptance the constructor corrected two literal endpoint strictness signs: the sine chord comparison is non-strict at `x=0`, and the upper-end kernel comparison is non-strict at `x=1`. The earlier strict signs were false at those exact endpoints; the theorem targets were already non-strict. The saved source diff confirms only these two signs changed. The corrected source is the final pin above, checked in `check04/` with all zero/one controls retained. Previous snapshots and receipts remain preserved. No numerical constant, variance cost or theorem domain changed.
