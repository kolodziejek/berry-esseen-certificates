# Bounded independent review of the inherited signed moment/gap prices

This is a read-only analytic review of `../signed-entry-v7/mathematics/fixed-target-v7/2026-10-27/signed_core.py`, separate from the new fixed-target transport review assigned to another reviewer. Reviewed SHA-256: `1f40ccb90eb58a7f84dc61a0a5dd9bf6e6eb4e341aa6c9c6d049d08451f5211b`. A frozen snapshot and receipt are under `runs/fixed-target-v7-20261027/fourier-signed-review01/`. No signed kernel, inherited program or numerical acquisition was executed here. The review concerns the formulas below, not complete acceptance of every discard branch or a final local-exclusion theorem.

Notation: `a_+=(1+beta)/2`, `a_-=(1-beta)/2` are the actual signwise second moments; `b_+=(rho+gamma)/2`, `b_-=(rho-gamma)/2` are the actual signwise third moments. The common positive and negative first moment is `m`. The law is standardized and supported in `[-R,R]`. Cell suffixes denote outward endpoints for these quantities. Both sign classes have positive mass, so `a_+,a_-,b_+,b_->0` and `|beta|<1`.

## Moment feasibility and moment ceilings

The common-m constraints are actual-law inequalities: conditional Cauchy gives `m^2<=a_+a_-`, while `m b_s>=a_s^2`. Hence

`m<=(1/2)sqrt(1-beta^2)` and `m>=max((1+beta^2)/(2rho),a_+^2/b_+,a_-^2/b_-)`.

The signed gamma limits follow by inserting the upper m bound into each `m b_s>=a_s^2`. Each resulting endpoint function is increasing in beta; substituting the beta and rho endpoints used in the code has the correct direction. Projection of `X|X|` on the span of `X,|X|` gives

`mu4 >= rho^2+(gamma-rho beta)^2/(1-beta^2)`.

The trilinear interval `ds` contains the actual residual. Using its distance from zero and the **upper** denominator `1-bmin^2` therefore gives a lower bound, as required for exclusion.

The finite family of upper bounds for m follows from the polynomial `(y-a)^2(R-y)>=0` on `[0,R]`:

`2m <= (R-rho+2a+Ra^2)/(a(2R+a))`.

The lower rho endpoint enlarges this right side. Only positive rational a values are used.

The localizing moment-matrix corrections can be checked directly. On each sign let `y=|X|`, `p_s=P(sign)`, `c_s=E[y^4;sign]`, `e_s=E[y^5;sign]`, and put `D_s=R a_s-b_s`. Positivity of the matrices for the measures `(R-y)dP`, `y(R-y)dP`, and `y^2(R-y)dP` gives respectively

`(R p_s-m)D_s >= (R m-a_s)^2`,

`(R m-a_s)(R b_s-c_s) >= D_s^2`,

`D_s(R c_s-e_s) >= (R b_s-c_s)^2`.

Summing the first pair yields the code's `fmean` necessary inequality, even with an atom at zero since `p_++p_-<=1`. Replacing a numerator by its nonnegative lower bound and a positive denominator by its upper bound weakens the correction in the correct direction. The function used in the bisection is nondecreasing in m. Retaining the upper bisection endpoint and rounding it upward cannot exclude an admissible m. The same directed substitutions prove the `c4u`, `Mc` and `etac` ceilings.

At a zero denominator, dropping a nonnegative correction is safe; it does not manufacture a positive gain. The explicit `denm==0 and DL>0` exclusion is justified because the corresponding positive-semidefinite matrix would then have zero diagonal and a nonzero off-diagonal entry. Negative support deficits are likewise impossible. These statements explain the denominator rules, but they are not a mutation-test result for the whole program.

The newly added physical lower bound

`m >= (sigma_lower*rho_lower-gamma_upper-d)/6`

is valid independently of a central gap: `D>=sqrt(10)rho-gamma-6m` and `D<=d` imply it directly. Taking its maximum with the other lower bounds is an intersection of necessary conditions. A negative right side is harmless. This is a safe strengthening of the common-m interval; any claimed numerical improvement still belongs to its separately recorded execution.

The subsequent beta contraction is valid too. If `m>=m_forced>=0`, then `m^2<=(1-beta^2)/4` forces `|beta|<=sqrt(1-4m_forced^2)`. A forced value above 1/2 is impossible. The code rounds the root upward and intersects it with the original beta cell. It resets the original beta endpoints for every gamma subcell, so a restriction justified by one gamma subcell is not incorrectly inherited by its neighbour. Recomputing bmin and mU after this intersection is consistent; retaining the earlier broader gamma interval is conservative.

## Actual gap event and endpoints

The strict gate `d<(sigma_lower-1)rho_lower` supplies an actual central gap and excludes a zero atom. Conditional Cauchy then gives

`p>=2m_lower^2/(1+beta_upper)`,

`p<=1-2m_lower^2/(1-beta_lower)`.

The event probability `2p(1-p)` is at least both endpoint-minimum bounds retained in the code: the probability-panel bound, and `(1+bmin^2)^2/(2rho_upper^2)` from the lower m bound. Taking their maximum is legitimate.

The stronger central distance is also correct. With `S=rho_lower-d/(sigma_lower-1)>0` and `P0=(sigma_lower-1)rho_lower-d>0`, the actual endpoints satisfy

`m(A^2+B^2)>=S`, `6mAB>=P0`.

Thus `(A+B)^2 >= (S+P0/3)/m >= (S+P0/3)/m_upper`, exactly the new `gap2` expression. A downward square root supplies the HIGH distance.

For the same opposite-sign event, direct conditioning gives

`E[(X-X')^2 | XX'<0] = (1+4m^2+beta)/(2p)+(1+4m^2-beta)/(2(1-p))`.

The coefficients are positive. This expression increases with m, is affine in beta and convex in p. The complete endpoint maximum therefore bounds it, and taking its minimum with `2/event_probability_lower` is valid. This use would require revision if the actual-gap gate were absent, because an atom at zero then prevents `p+q=1`.

The endpoint quadratic follows from the nonnegative physical decomposition and `T-J_outer>=2B R_++2A R_-`:

`D >= (sigma-1)b_+ +6a_+ B -(sigma+5)m B^2`.

The reflected formula has `(sigma+1),a_-,b_-,A` and `(sigma+7)`. When the lower constant term exceeds d, the upward rearranged quadratic has one positive root, and B (or A) must exceed it. The code replaces the positive linear/constant terms downward and the quadratic coefficient upward; its lower square root and resulting root are therefore conservative. The upper endpoint estimates `A<=a_-/m`, `B<=a_+/m` are direct. The rectangle lower bound for the asymmetry square uses lower positive terms and upper subtracted terms before taking the positive part and squaring. Consequently `d-m_lower Q_lower` is an upper budget for the actual remaining defect, not an extra deduction counted twice.

## Central and outer charges

Using the manuscript's signed definition `J2=sum tau integral (t-a)t|t| dt`, the central polynomials are

`P1=B^3/3+AB^2/2-A^3/6`, `P2=B^4/4+AB^3/3-A^4/12`.

For `G=rho P1-P2`, `dG/dB=B(A+B)(rho-B)`, so maximization in B is bounded by B=rho. The resulting

`G(A,rho)=rho^4/12+rho^3 A/6-rho A^3/6+A^4/12`

is nonnegative, increases in A, and is convex in rho. Its A derivative is `(rho-A)^2(rho+2A)/6`; its second rho derivative is `rho^2+rho A`. Thus the code's upper A endpoint, both rho endpoints, and upper m endpoint give a valid central charge.

For a positive outer gap, its lower endpoint a satisfies a>=B. The product `(t-a)(rho-t)` is at most `(rho-B)_+^2/4`; after retaining the nonnegative t factor, Tonelli gives the price `(3/8)(rho-B)_+^2 T_+`. On the negative side, writing x=-t and dropping x<rho gives the product `(v-x)(x-rho)<= (R-rho)^2/4`, hence price `(3/8)(R-rho)^2 T_-`. Both are valid with the cell ceilings. The weighted budget `(sigma-1)T_++(sigma+1)T_-<=d-m_lower Q_lower` and the separate third-moment bounds each give a complete upper bound; their minimum is valid.

The coarse Gamma alternative also has the correct structure. On the negative portion, extending to all x>=rho and then to r=rho_lower gives

`integral_r^R (R-x)x(x-r) tau(-x) dx`.

Tonelli writes this as `E[Y integral_r^Y(R-x)x(x-r)dx; X<0]`, which is at most `Gamma E X_-^3` when Gamma bounds the integral divided by Y^2. Direct integration yields exactly the code's rational expression. Its 64-cell bound separately maximizes the concave quadratic and positive reciprocal term. The coarse cap 5/2 at r=1,R=6 follows from positivity of `3v^4-28v^3+66v^2-11` on [1,6]: endpoint values are 30,205, and the two interior critical values are `(85±35sqrt(5))/2>0`. Monotonicity in R and reverse monotonicity in r follow from the positive integral representation.

Finally `P1` increases in B, and its A derivative `(B^2-A^2)/2` changes from positive to negative. Its minimum and maximum therefore occur at exactly the endpoints/clipped point selected by the code. Multiplying a negative polynomial bound by the opposite m endpoint is necessary; the implementation does so. The outer signed J1 bounds `-R T_-/2 <= J1_outer <=R T_+/2` follow directly by integration. The K1 interval uses signwise fourth-moment lower/upper bounds with consistent endpoint signs. The three constant penalties are separately valid deductions and are combined by a maximum, as required.

For clarity, these penalties have direct proofs. Write `delta=gamma-rho beta` and `V=eta5-2rho mu4+rho^3`. Under the positive measure `|X|dP`, Cauchy gives `delta^2<=2m V`, hence the deduction `delta^2/(8m)` from `rho mu4/2-eta5/4`. Independently `mu4^2<=rho eta5` and the projection lower bound give the deduction `delta^4/[4rho(1-beta^2)^2]`. On each sign, `c_s>=b_s^2/a_s` and `e_s>=c_s^2/b_s` give

`rho c_s/2-e_s/4 <=rho^2 b_s/4-(c_s-rho b_s)^2/(4b_s)`.

The distance from `rho b_s` to the half-line `c_s>=b_s^2/a_s` gives the two signwise squared-positive-part losses. Their lower bounds in the code use the positive parts of the entire residual interval, upward denominator ceilings, and nonnegative lower sign-moment endpoints. Thus each of the three complete deductions is valid independently; their sum has not been asserted.

## Scoped conclusion

| Item | Mathematical status | Execution status |
|---|---|---|
| Listed common-m/localizing-matrix and signwise coefficient formulas | Independently re-derived; no mismatch found in the reviewed snapshot | Not executed |
| New physical m lower bound and stronger gap distance | Independently proved with explicit prior-defect gate | Not executed |
| Reviewed central/outer charge, endpoint and signed J1 formulas | Independently re-derived; endpoint signs and denominator directions checked | Not executed |
| Entire signed cover, transport, stage updates and numerical targets | Outside this bounded review; other reviewers handle new transport | No signed-kernel run |

The relevant analytic source is `manuscript/arxiv-v1/appendices/fourier-analysis.tex:1748–1981`, with the physical decomposition in `sections/05-geometry-counts.tex:148–175`. This report establishes no new numerical ceiling or final exclusion.
