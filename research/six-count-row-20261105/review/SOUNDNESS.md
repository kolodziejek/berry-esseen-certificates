# Independent six-count reduction review

This is a conditional analytic reduction, not acquisition of the original row
and not a completed probability/phase cover. The derivation below was made
before reading the new constructor. The executable checks are separately
recorded under `runs/count_row_20261105/review_*`.

Let `n>=1` be an integer, `0<p<1`, `q=1-p`, and let the same two centered
conditional laws occur in every count. Write `x=q E U0²`, `y=p E U1²`,
`v=pq`, `lambda=n(x+y)`. The sign conditions are `U0<=p` and `U1>=-q`.
They imply exactly

```
beta = [v(1-2p)-x+y]/[v+x+y].
```

Consequently the two beta halfplanes printed in the constructor and note have
the correct signs. Cubic right-side upper bounds on a closed probability cell
give a fixed outer polygon. The polygon must be fixed before the moment and
vertex reductions; using an independently optimized variance pair for each
binomial count would not be this argument.

For the support intervals `[-A0,a0]` and `[-a1,A1]`, integration of
`(U0+A0)(a0-U0)U0²>=0` and its reflection gives the two fourth-moment upper
bounds. Independence gives the exact fourth moment of each count sum, and
Cauchy applied to its n individual variances gives

```
E Wj^4 <= (n-j)E U0^4 + j E U1^4 + 3(1-1/n)t_j²,
t_j = (n-j)x/q + j y/p.
```

First sum all count expectations with their nonnegative binomial weights.
At fixed variances and inward endpoints this upper expression is affine in
each common `gamma_i=E Ui³/E Ui²`. Each gamma is between its support endpoints.
At the outward endpoint its fourth-moment price is `A_i² s_i`; at the inward
endpoint it is `a_i² s_i`. The remaining expression is convex in each a_i
because its quadratic coefficient is a nonnegative sum of quartic leading
coefficients. Thus independent constant caps r_i permit the nine COMMON
choices `gamma0 in {-A0,0,r0}`, `gamma1 in {A1,0,-r1}`. These are extremal
evaluations of an upper expression. They do not assert `E Ui^4<=gamma_i² s_i`
for an actual law. If a variance is zero its whole conditional law is zero;
no gamma quotient is taken.

After this reduction, each expression is affine in x,y except for nonnegative
multiples of squared linear forms t_j². It is convex, so its maximum over the
compact polygon occurs at a vertex. Retaining the original negative diagonal
variance correction would invalidate that convexity: for n=5,j=2 the quadratic
`6s0²+12s0*s1+2s1²` is 6 and 8 at (1,0),(0,2), but 19/2 at their midpoint.

For fixed vertex and gamma pair put

```
T_j=(n-j)p*x+j*q*y,
G_j=(n-j)p*gamma0*x+j*q*gamma1*y,
L_j=(n-j)p*gamma0²*x+j*q*gamma1²*y,
a=j-k-u.
```

For `P_j(z)=sum c_r z^r`, direct expansion gives

```
v² E_upper P_j(Wj+a)
 = v² P_j(a)
 + (c2+3a*c3+6a²*c4)*T_j*v
 + (c3+4a*c4)*G_j*v
 + c4*L_j*v + 3(1-1/n)*c4*T_j².
```

The expression is then multiplied by `binom(n,j)p^j q^(n-j)` and summed.
This independently proves degrees at most `(n+4,4)`, hence `(9,4)` for n=5.
The clearing factor v² is strictly positive on the original closed p cell.
All gamma caps, vertex coordinates and quartic coefficients here are fixed
on that cell; p-dependent chosen endpoints cannot silently enter this proof.

The event majorant must satisfy `P_j(z)>=1` for every `z<=0` and `P_j(z)>=0`
for every `z>=0`. In particular P_j(0)>=1. Conditioning on the common iid
marginal then proves the binomial mixture inequality with all threshold atoms.

## Gaussian term and two legitimate strengthenings

Write `a=k+u-np` and `D=npq+lambda`. The basic cellwise lower bound uses the
smallest numerator; for a negative lower numerator it uses the smallest
denominator, and for a nonnegative one the largest denominator. This remains
sound on a sign-crossing cell. Using the upper noise endpoint for a negative
numerator would have the wrong direction.

A sharper derivative check is

```
sign(d/dp [a/sqrt(D)]) = -sign(np+(k+u)(1-2p)+2lambda).
```

For n=5, p in [.38,.39], and k+u>=-.5 the displayed bracket is strictly
positive. Thus at fixed lambda the smallest normal argument is at p=p_hi,
u=u_lo. This is an optional tightening, not needed for soundness of V1.

More usefully, for fixed p,u, `g(lambda)=Phi(a/sqrt(D))` satisfies

```
g'  = -a*phi(a/sqrt(D))/(2D^(3/2)),
g'' = a*phi(a/sqrt(D))*(3-a²/D)/(4D^(5/2)).
```

If a<=0 and a²<=3npq, g is concave for all lambda>=0. Hence the moment
upper expression minus g is convex in (x,y), and the vertex test can retain
that vertex's actual `lambda=n(x+y)`. A sufficient whole-cell guard is
`a_max<=0` and `a_min²<=3n*v_min`. The lower normal argument at a vertex can
then be `a_min/sqrt(n*v_min+lambda_vertex)`, with directed rational rounding.
This handles lambda=0 as well. The proof must use the curvature condition
before replacing the Gaussian at vertices by its numerical lower bound.

The exact absolute-cube coupling is

```
rho*(v+x+y)^(3/2)
 = R := v(1-2v)+3(p*x+q*y)-gamma0*x+gamma1*y.
```

It holds for actual laws because of the sign partition. On a noise slab
`L<=lambda<=U`, R>=0 for actual laws implies
`rho>=R/(v_max+U/n)^(3/2)`. Any fixed convex blend of this lower bound and
`rho>=rho_min` is valid. Subtracting the corresponding fixed positive multiple
of R from the mixture bound preserves affinity in gamma and convexity in x,y.
R is not required to stay nonnegative at relaxed moment corners: positivity
was used for the actual-law denominator inequality before the outer reduction.
The candidate blend weight must lie in [0,1], all denominator powers must be
rounded in the correct direction, and the slab must be included in the polygon.

## Bounded source review

Read `construct/model.py`, `construct/accept.py`, and the root's
`six_count_reduction.tex` in full. The displayed moment, beta, degree, ray,
Gaussian and cover rules agree with the independent derivation. The external
reader reconstructs every tensor and retains both closed children at each
split. The internal model's optional cached-row argument is not exposed to
proof objects. The selected raw-threshold bound implies only k=1,2,3, separately
from the six mixture counts j=0,...,5. No mathematical defect was found in this
bounded V1 review. Explicit n>=1 and nonnegative support ceilings would make the
generic note's premises more formal. No acceptance of a full original row is
claimed by this note.
