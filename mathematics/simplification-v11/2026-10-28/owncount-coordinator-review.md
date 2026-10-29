# Coordinator review of the variance-aware own-count lemmas

The coordinator read the complete proof and checker before integration.
This is a separate analytic derivation of the central inequalities, not a
second computational implementation or an external referee report.

For a centered summand Z on a closed interval, write
`Z^4-kappa Z^3=Z^2 (Z^2-kappa Z)`. The second factor is convex in Z,
so its maximum is attained at one of the two endpoints. This proves the
two stated conditional coefficients for every real kappa, including when
one endpoint coefficient is negative. Independence gives the exact identity
`E W^4=sum E Z_i^4+3t^2-3sum Var(Z_i)^2`. Dropping the final nonpositive
term gives the claimed upper bound. No iid extremal-support theorem is used.

Expanding the quartic at W+r leaves the third-moment coefficient
`b3-4r`, second-moment coefficient `b2+3b3*r-6r^2`, and constant `M h(r)`.
This verifies the own-count inequality, with the strict event inherited from
the pointwise minorant. For the symmetric quartic, the two coefficients reduce
to `A^2-4Ar` and `A^2+4Ar` only when `4r<=A-a0`; the sufficient condition
`r<=(A-d)/4` is retained. The improvement relative to the absolute-third-moment
bound is exactly `8Ar T0/M`.

At fixed n,p,k,lambda the two variance totals are affine in the allocation.
The own-count lower bound is affine minus `3t^2/M`, hence concave. At a fixed
positive tilt, each incoming exponential is an exponential of an affine
function, hence convex; its positive convergent sum remains convex. The
geometric-series condition is sufficient even at allocation endpoints.
Subtracting this incoming bound preserves concavity. This conclusion does
not extend automatically to a pointwise minimum over tilt choices.

The raw absolute third moment is
`pq(1-2pq)+3pq(v0+v1)+p mu1-q mu0`. Adding its contribution before bounding
the own-count cubic changes the two coefficients to
`kappa-C ell^3 M q/(m N0)` and `kappa+C ell^3 M p/(m N1)`.
Both signs and both multiplicities agree with the exact expansion. The mass m
and scale ell are fixed under allocation. Their separate outward replacement
inside this expression would require a new sign argument, as the note warns.

For the optional Hermite bound, the difference between the original quartic
and the proposed quadratic is
`(x-A)(x+v/A)^2(x+A-2v/A-kappa)`. The first factor is nonpositive and the last
nonnegative on the stated support precisely under the given sufficient sign
condition. The variance bound `v<=Ab` makes the comparison two-point law
feasible. Evaluation on its two atoms verifies the expected quadratic value.

The finite-normalization domain and rational gates were checked against the
retained v10 Stirling estimate. The source's strict and closed events are
consistent. Actual-law tests are useful controls and are correctly described
as such; they do not substitute for the above continuous arguments.

**Outcome:** no blocker found for the stated local lemmas. They do not prove
the endpoint count comparisons or a complete theorem above lambda=.02.
The later count component must be assessed separately. Source and checker
hashes are captured by the integrated reproduction receipt.
