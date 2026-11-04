# Independent analytic license for the signed coefficient pilot

This note supplies mathematical premises for the constructor's fixed algebraic family. It is not a certificate-acceptance report. The existing manuscript remains unchanged.

## One marginal and three nonnegative measures

Let `E X=0`, `E X²=1`, and let the actual support on each sign have its own finite radius. Put `p=P(X>0)`, `q=P(X<=0)`, `m=E X_+=E X_->0`. Then `p,q>0`. The signwise moment measures and the two conditional variance measures all come from this same law. A coefficient family may intersect necessary bounds on these moments; it must not assign different first moments or substitute a different law in individual coefficients.

For a sign-class magnitude `Y=|X|` with radius `r>0`, write its unnormalized moments `s_j=E[Y^j; class]`, `j=0,...,5`. In particular both signs have `s_1=m`. The matrices

`H_j=[[s_j,s_(j+1)],[s_(j+1),s_(j+2)]]`,

are positive semidefinite whenever defined, because their quadratic forms integrate `Y^j(a+bY)²`. The three localizing matrices `r H_j-H_(j+1)`, `j=0,1,2`, are positive semidefinite because their quadratic forms integrate `Y^j(r-Y)(a+bY)²`. This proves the entire signwise 2×2 family simultaneously, including different positive/negative radii and zero atoms.

## Quotient guards, including exact zeros

Every localizing matrix has nonnegative diagonal entries and nonnegative determinant. For `[[A,B],[B,C]]`, the quotient deduction `C>=B²/A` requires `A>0`. If `A=0`, the determinant forces `B=0`; the valid remaining assertion is `C>=0`. No division or continuity argument is necessary. The symmetric rule handles `C=0`.

Thus the three manuscript contractions are

- `s_0 >= m/r + (rm-s_2)²/[r(rs_2-s_3)]` when `rs_2-s_3>0`;
- `s_4 <= rs_3 - (rs_2-s_3)²/(rm-s_2)` when `rm-s_2>0`;
- `s_5 <= rs_4 - (rs_3-s_4)²/(rs_2-s_3)` when `rs_2-s_3>0`.

At a zero denominator, use the corresponding zero off-diagonal condition and discard the nonnegative correction. If an interval contains zero and the checker cannot establish strict positivity, it may retain only the uncorrected bound. An interval that contains zero is not evidence that its actual denominator equals zero. A negative necessary diagonal or a nonzero off-diagonal with a provably zero diagonal excludes the state. A radius-zero input cannot use these quotient formulas; an actual centered unit-variance law has positive `m`, hence cannot have either whole sign class supported only at zero.

For intervals, a correction is bounded below by a lower bound for the square divided by a strictly positive upper denominator. The distance of the numerator interval to zero is a valid square root of this lower square bound. For the localizing off-diagonals, nonnegativity also permits the positive part of an independently proved lower endpoint. It is incorrect to square a negative lower endpoint merely because that has larger absolute value.

## Conditional signed cancellation

The proposed `conditional-family.tex` independently derives

`K1(X)-K1(V)=integral F(x,a_+;rho+gamma_V)dnu_+ - integral F(x,a_-;rho-gamma_V)dnu_-`,

where `dnu_s=(X-V)² 1_s dP` and

`F(x,a;t)=x²+2ax+3a²-3-(3/2)t(x+2a)`.

The same two measures give all unsigned/signed moment increments of orders 2–5. Their masses are precisely `theta_+`, `theta_-`; no division by either mass is allowed or needed. The product decomposition retains actual `rho` with the change in `gamma`, and actual `gamma_V` with the change in `rho`. Replacing both by independently chosen original-moment bounds inside an asserted equality would be wrong.

Since `F_t=-(3/2)(x+2a)<0`, use the relevant endpoint of a proved `t` interval. For fixed `t`, its Hessian is positive definite. Its maximum is among the four corners. The complete minimum list consists of corners, the clipped stationary point of each edge, and `(3t/8,3t/8)` if inside. This licenses the complete signed rectangle, not only positive coefficients. If its range is `[L,U]`, an unknown variance mass in `[0,Theta]` gives `[Theta min(0,L),Theta max(0,U)]`. Omitting the zero option can reject the exact Bernoulli case.

## Central signed integrals

The already explicit central-gap integration gives

`P1=B³/3+AB²/2-A³/6`, `P2=B⁴/4+AB³/3-A⁴/12`, and `J_(j,c)=m Pj`.

For `A,B>=0`, both polynomials increase in `B`; their `A` derivatives are `(B²-A²)/2` and `(B³-A³)/3`. Thus a rectangle minimum is at `B_l` and an `A` endpoint; a maximum is at `B_u` and `A` clipped to `B_u`. These conclusions include zero-width rectangles. Multiplication by positive `m` is sign-sensitive: a negative lower/upper polynomial value uses the opposite `m` endpoint from a positive one.

For `G=rho P1-P2`, `G_B=B(A+B)(rho-B)`. Its unrestricted `B>=0` upper bound is `G(A,rho;rho)`; this increases with `A`, since its derivative is `(rho-A)²(rho+2A)/6`, and is convex in `rho`, since its second derivative is `rho²+rho A`. These calculations justify the older coarse central bound.

For the sharper complete rectangle, affine substitution into `[0,1]²` and degree-four tensor Bernstein expansion gives 25 coefficients, each affine in actual `rho`. The Bernstein basis is nonnegative and sums to one. Retaining **both** products `m_l b_ij(rho)` and `m_u b_ij(rho)` bounds `mG` regardless of sign. Their maximum is convex in `rho`. This is the full continuous-cell license; an algebraic checker need only verify the fixed polynomial substitution and the degree-four conversion, not rediscover analytic extrema. Degenerate side lengths cause no division and remain valid.

## One outer budget

After the central gap is licensed, the exact defect identity supplies

`(sigma-1)T_+ +(sigma+1)T_- <= D-mQ`,

with `T_+,T_->=0`, `Q=(sqrt(sigma+1)A-sqrt(sigma-1)B)²`, `sigma=sqrt(10)`. It is this same budget, and the same two variables, that pays for outer moment, signed phase and integral costs. Individual caps `T_+<=u_+`, `T_-<=u_-` may be intersected with it.

For a cost `b_+T_+ +b_-T_-`, the exact feasible set is a rectangle intersected with a half-plane. Its vertices are the origin, feasible clipped axis endpoints, feasible rectangle corners, and intersections of the budget line with the two positive cap edges. Evaluating the signed linear cost at all those vertices is sufficient. With no individual caps, the upper bound is

`(D-mQ) max(0,b_+/(sigma-1),b_-/(sigma+1))`.

An implementation may use a weaker outward budget, but it must prove that replacement in the safe direction and preserve nonnegativity before applying the simplex rule. If the cost is a sum of several terms, sum their coefficients first. Reusing the same nonnegative deduction by adding independently derived deductions is not licensed; independent upper bounds for the same quantity are intersected by a minimum.

The outer integral formulas still need the manuscript's short integration proof. In particular,

`3(rho J1-J2)_o <= (3/8)[(rho-B)_+² T_+ +(R-rho)² T_-]`,

and `-R T_-/2 <= J_(1,o) <= R T_+/2` are analytic input rows, not consequences of polynomial expansion alone. Keep those formulas and their signwise integration argument visible in the manuscript. Likewise central-gap formation, raw-remainder licensing, the weighted actual-index invariant and the closed-cover induction must remain analytic text.

## Execution evidence and limits

`check_conditional_family.py` was freshly run with exact fractions in `runs/certificate_consolidation_20261104/analytic_examples01`. It passed ten rational actual-law cases, including symmetric/skew Bernoulli, zero atoms, reflected skewness, four-point perturbations, positive noise of arbitrarily small chosen rational magnitude, a tiny far atom and exact support collisions. The test verifies all conditional identities for orders 2–8, the exact `K1` identity, the common mean/variance relation, and all three signwise localizing determinants. It explicitly exercises zero-denominator branches. A finite rational grid also checks the derived rectangle-extremum list and detects four unsafe shortcuts.

These are regression/adversarial examples. The continuous-domain proofs are the derivations above and in the candidate TeX; the examples do not certify every law or every parameter cell. No native Fourier or count certificate has been rerun.
