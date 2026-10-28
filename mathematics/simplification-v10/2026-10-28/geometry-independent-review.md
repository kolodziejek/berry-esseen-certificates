# Independent review of the direct geometry replacement

This review was performed on the separate branch
`research/geometry-review-v10-20261028`, starting at
`00ba714897f2e09995d78354ac3c8931e257cd05`. It concerns the new geometry
proof and checker in the constructor's `geometry-v10` worktree. No constructor
program was imported or rerun as an alleged independent implementation.
The exact bytes reviewed are recorded by the accompanying arithmetic run.

## Conclusion and scope

No blocking analytic or arithmetic defect was found in the reviewed direct
geometry implications. They replace the old eight-round iteration for the
listed global bounds, the two probability-panel exclusions, the thirteen
incoming .6 strips and the required central-panel moment/noise/scale vector.
The replacement preserves its actual-gap, entry and weighted-resource
hypotheses. The support strips additionally require the retained fixed-target
contact/true-predecessor heat theorem.

| Review item | Mathematical status | Execution status in this review |
|---|---|---|
| Common geometric cost and global scalar reduction | Independently rederived from the actual-law gap budget | Analytic source review; no inference from a success marker |
| Four quartics and two cubics | Independent rational reconstruction from the factored mathematical formulas | Fresh exact PASS; all coefficients match the constructor and all uniform derivative/tangent bounds hold |
| One-pass panel formulas and directed arithmetic | Independently checked for directions, domains and retained closed coverage | Full source inspection; constructor's 30-panel output inspected as data, not independently replayed here |
| Actual-law controls | Normalization, gap sum, Q(sqrt10) sign arithmetic and invalid maximum-sign-cost control inspected | Constructor's exact controls were not rerun in this review |
| Full confinement, count comparison and finite base | Not established by this component | No full acceptance or generation campaign |

The full v7 entry, its 30 nonempty-panel coverage, support radius, actual
weighted nD bounds and original signed-phase/raw-threshold inputs remain
dependencies. This review does not certify that every individual new panel
bound may replace an arbitrary old downstream bound without comparison.

## Independent analytic derivation

### Common cost

For a positive outer support gap (u,v),
`tau(v-u)^2 <= 2 tau integral_u^v(t-B)dt`, because u>=B. Summing the
gaps and applying Tonelli gives `J_outer+ <= E[X_+(X_+-B)^2]`; the
negative side is identical in magnitude coordinates. The central gap adds
`m(A+B)^2`. This argument includes endpoint atoms; their values do not
change the Lebesgue integrals.

Write `a0=(barA-A)/ell`, `a1=(barB-B)/ell`. Since `m ell=w`, the exact
inward term divided by ell is
`6w[d(1-d)+a0 a1]`. At x>=B the positive noise coefficient divided
by ell is at least `3(sigma+1)q-(sigma+5)a1`; on the negative sign it
is at least `3(sigma+3)p-(sigma+7)a0`. Replacing each ai by d and then
taking the minimum charges each sign's nonnegative measure once. The
maximum of these two prices cannot be used. The resulting inequality
does not use contact or a predecessor theorem.

### Global localization

The initial `AB>=z` follows from
`D >= (sigma-1)rho-6m AB >= sigma-1-3AB`. The actual conditional means
give `AB<=w` and `A+B>=2sqrt(AB)`. Thus
`d<=1-2sqrt(zpq/w)` and `theta<=1-z` hold without the old iteration.

The preliminary theta<.2 uses the stronger physical noise coefficients
before the crude linear K(p,d) is known positive. In particular
`B>=z/barA` gives `k+/ell >= q[(sigma+5)z/w+2(sigma-1)]`, and similarly
on the negative side. The stated lower bound3.13 and ell>=2sqrt(z)
therefore have the right directions.

For theta in[.056,.2), both branches are concave in d. Each branch must
be checked at both feasible endpoints; the minimum of branches is not
replaced by a maximum. At the larger endpoint the stated rational square
comparisons give .59<g<.77, hence g(1-g)>.17, ell>1.7 and positive
noise coefficients. The inward term alone exceeds D0. At d=0, differentiating
the whole square-root factor gives derivative sign
`(2-3theta)C-3(1-theta)Q`, not simply C-Q. The bounds C>4.4 and Q<.4
justify its positivity. The two theta quartics correctly square positive
bases.

After theta<.056, the global AB bound gives d<.42. This is sufficient
for each branch to increase in d. To rule out d>=.068, evaluation at
d=.068 and monotonicity in theta reduce to theta=0, producing the third
quartic. No output of the old eight-round procedure occurs in these steps.

For lambda, multiplying the *actual* common budget by n gives
`nD >= ell w[n Q + C lambda/(pq)]`. Using n>=42 in nQ is valid because
Q>=0. The given nD ceiling is then divided by ell w>=2(1-.056)^(3/2).
This yields the two cubics. For an actual feasible tuple their common
numerator is nonnegative; replacing Q and the positive denominator by
lower enclosures therefore enlarges the bound. The positive cubic's
initial increasing segment and its later concave segment jointly cover
the full probability interval. The negative cubic is concave throughout.

For rho, the positive coefficient ratio uses x<=3.14, barB<1.8 and
B>1.94(.46-.068); the negative ratio already exceeds sigma+1. Each
noise coefficient is therefore at least5/2 times the corresponding
third-moment coefficient. The resulting bracket
`1-2pq-(2/5)Q` is positive (at least .34), so replacing w^(3/2) by1
is safe. The fourth quartic squares two positive quantities. Finally,
Q/sqrt(pq) decreases on[.24,.25], since Q decreases toward p* while
pq increases. Its value at .25 exceeds D0, giving the strict lower
probability bound and excluding the whole closed panel24.

### One evaluation per panel

The first formula uses
`Q+theta(C-Q)=(1-theta)Q+theta C`. For theta in[0,1] this is separately
increasing in Q and C. Thus lower-bounding them by Q_I and C_I before
solving for theta is valid, despite the occurrence of Q in both terms.
The denominator C_I-Q_I is strictly positive. The new ell lower bound
then follows from this theta cap. These formulas do not feed their result
back into an earlier formula.

After global d<.068, K is positive. Dropping the noise term gives
`6d(1-d)<=J_I`. Because d<1/2, the correct implication uses the smaller
quadratic root. The code checks J_I in[0,3/2) before the root and rounds
the square root downward, hence d upward. Negative residuals exclude a
panel; equality is retained. Subsequent A and B lower bounds are positive.

The coherent rho bound is the maximum of two affine pieces:
`r_B(1-alpha theta)+min(L theta,r/k)`. It rises, if at all, to the smaller
of the theta cap and the turnover r/(kL), then decreases. There is no
combination of incompatible moment allocations. A requested clarification
has been incorporated: `1-alpha theta>0`, since alpha theta<=(3/2)*.056<1,
so replacing the Bernoulli third moment by its upper bound is licensed.

The beta bounds have the correct orientation even on panels above one
half. The weighted lambda formula retains nD<=42D_I, rather than deriving
it from an unweighted theta bound. Its numerator is nonnegative for any
actual surviving law, so replacing pq by its panel maximum is valid.

## Code and coverage review

`geometry-check.py` reconstructs four quartics and two cubics with exact
Fractions. Quadratic extrema include both endpoints and an eligible vertex;
affine second derivatives need only endpoints. Positivity is checked before
squaring the three uncertain bases. The rho base and target are manifestly
positive from the displayed bounds. Assertions and optimized-Python rejection
remain intact. No floating-point value participates in an acceptance test.

`geometry-panels.py` verifies the frozen v7 input SHA256, its name, all100
closed panel endpoints, exactly30 nonempty panels24–53, the maximum incoming
D and final active support radius. Its square-root lower enclosure is based
on an integer floor and is followed by exact squared comparisons. The upper
enclosure is strictly outward. All later lo/hi operations have the correct
directions in their positive domains. The panel53 exclusion is a strict
negative residual, not a discarded endpoint. Every retained panel25–52 is
still represented, including shared boundaries.

The support tests are the retained all-threshold heat and full-ray formulas,
now with explicit contact and predecessor premises in the proposition.
The tested radii `e_I(l+.6)` and `e_I(1-u+.6)` are lower bounds for the
actual physical .6 boundaries, so excluding all contacts beyond them is
sufficient. Positive and negative beta directions are separate. Both
boundaries and all derivative signs pass exactly on panels40–52. The
code requires that complete list and compares all eight central moment,
noise and scale bounds against their old required outward values. The
raw-H and signed-phase bounds remain separate ancestors.

`geometry-laws.py` uses raw centered rational laws and cancels the variance
normalization algebraically: the normalized D has degree minus3 in scale,
while ell has degree minus1, so multiplying the direct bound by V^(3/2)
correctly introduces the factor ell_raw*V. The sign test in Q(sqrt10)
distinguishes same-sign and opposite-sign coefficients before squaring.
The exact adjacent-atom gap sum uses the right survival value. Zero atoms
are rejected as outside the actual-central-gap hypothesis. Its deliberately
false maximum-sign-price condition is an appropriate negative control.

## Independent arithmetic

`geometry-independent.py` does not import any constructor. It evaluates
the factored mathematical expressions at rational nodes and solves the
Vandermonde equations exactly, a separate reconstruction from the
constructor's polynomial products. It then derives the derivative polynomials,
checks every relevant endpoint/vertex and proves the stated tangent bounds.
All four quartic and both cubic coefficient lists match the constructor's
recorded data. A deliberately false uniform lower bound .02 for the positive
theta quartic is refuted at p=.45, so this control is a real mathematical
counterexample to the stronger scalar gate.

The fresh receipt, stdout, stderr and all reviewed source hashes are under
`runs/geometry-v10-independent-20261028/check01/`. This independently confirms
the scalar polynomial certificates. It does not recast source inspection of
the 30-panel algorithm as an independently implemented full panel replay.

Recommendation: accept the claimed replacement at its expressly listed
dependency edges, subject to the coordinator's final integration checks.
Do not infer full larger-noise confinement, a final count comparison,
BASE41, or authority to delete historical proof objects.
