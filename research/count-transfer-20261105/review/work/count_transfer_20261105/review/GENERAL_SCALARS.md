# Independent scalar reduction for either probability half

This note is a conditional analytic derivation. It does not assert that any new
row has passed a complete numerical comparison or acquired its premises.

Let n>=1 be an integer, 0<l<=p<=h<1, q=1-p and v=pq. The exact variance
extrema on the closed probability interval are

```
v_min=min(l(1-l),h(1-h)),
v_max=max(l(1-l),h(1-h), 1/4 if l<=1/2<=h).
```

This follows because v is a concave quadratic with its only stationary point
at 1/2. Both quantities are strictly positive. Neither endpoint direction can
be inferred from the left-half case when the interval lies to the right.

For the original sign-conditioned law, use the same centered U0,U1 in every
count, x=q E U0², y=p E U1², w=v+x+y and lambda=n(x+y). The acquired positive
first moment is m=E X_+=v/sqrt(w), not E|X|. Thus m>=m_lo>0 gives

```
lambda <= n(v²/m_lo²-v).
```

The right side is convex in v. Without any monotonicity assumption its maximum
on [v_min,v_max] is the larger endpoint value. If the reader explicitly checks
2v_min>=m_lo² it may use only v_max. Intersect with the old independent noise
cap. This clipping is a necessary consequence of the same-law mean bound; it
does not change the original affine resource intercept in a separate joint
budget. Empty or degenerate feasible sets need explicit treatment, not a
successful marker obtained from a rejected polygon routine.

If the acquired negative/positive standardized support gaps are b_minus,b_plus
>=0, then actual inward endpoints satisfy

```
a0 <= p-b_minus*sqrt(w),
a1 <= q-b_plus*sqrt(w).
```

On a slab L<=lambda<=U, a directed lower root r of v_min+L/n gives fixed
upper caps `min(d,h-b_minus*r)` and `min(d,1-l-b_plus*r)`. This derivation is
unchanged on the right half. It uses the actual endpoint and mean fields,
not a later comparison or any hypothetical reflection of their values.

## Normal CDF and rho term

Put a=k+u-np, a_min=k+u_lo-nh, a_max=k+u_hi-nl and
D=nv+lambda. A valid lower argument is

```
a_min/sqrt(n v_max+U)   if a_min>=0,
a_min/sqrt(n v_min+L)   if a_min<0.
```

This remains sound if the numerator changes sign inside the cell: a negative
lower value is below every nonnegative actual value. Directed roots must use
the upper root for a positive numerator and the lower root for a negative one.

For fixed p,u, g(lambda)=Phi(a/sqrt(D)) has

```
g''(lambda)=a phi(a/sqrt(D)) (3-a²/D)/(4 D^(5/2)).
```

Hence a_max<=0 and a_min²<=3(n v_min+L) imply concavity on the whole cell and
slab. The stronger guard a_min²<=3n v_min is also sufficient. The common moment
upper expression minus the actual Gaussian is then convex in x,y. Only after
taking its polygon vertex maximum may the Gaussian at a vertex be replaced
by a rational lower enclosure. The vertex's noise is n(x+y), and its safe lower
argument is a_min/sqrt(n v_min+n(x+y)). The shared variance polygon must be
the same one used in every count and the rho numerator.

There is a sharper endpoint rule when the entire threshold cell obeys
0<=t=k+u<=n. Direct differentiation yields

```
dz/dp = -n[np+t(1-2p)+2lambda]/(2D^(3/2)),
dz/dt = 1/sqrt(D),  z=(t-np)/sqrt(D).
```

For fixed p the bracket is affine in t. Its minimum on [0,n] is np+2lambda
when p<=1/2 and nq+2lambda when p>=1/2, both positive. Thus z decreases in p
and increases in t, on either p half. At fixed lambda its exact cell minimum
is therefore `(t_lo-nh)/sqrt(nh(1-h)+lambda)`. Choose lambda=L if its numerator
is negative and lambda=U otherwise. This also covers a cell where the numerator
changes sign. Without the full threshold gate, this monotonicity cannot be
assumed; the preceding v_min/v_max fallback remains valid.

Under a_max<=0 and that threshold gate, z<=0 everywhere and its minimum over
the noise slab is at (p,t,lambda)=(h,t_lo,L). Therefore the less restrictive
test `a_min²<=3(nh(1-h)+L)` implies z²<=3 throughout. This proves the same
Gaussian concavity and licenses the sharper vertex-specific argument
`a_min/sqrt(nh(1-h)+n(x+y))`. It does not replace the requirement that the
actual Gaussian be retained until after convex maximization.

The exact same-law absolute-cube numerator remains

```
R=v(1-2v)+3(px+qy)-gamma0*x+gamma1*y,
rho=R/w^(3/2).
```

For actual laws R>=0. Thus replacing w by its slab upper bound v_max+U/n and
using a downward coefficient remains valid on either p half. A fixed convex
blend with rho>=rho_lo retains common-gamma affinity and common-variance
convexity. Artificial corner R values need not be moments of a realizable law.

The support fourth-moment inequality, nine common gamma extrema, Cauchy factor
3(1-1/n), and positive denominator p²q² are independent of which p half is
used. With n=5 and fixed cellwise endpoints and vertices, the cleared degree
is still at most (9,4). There is no justification for changing the six mixture
counts or their ordering when p crosses 1/2.

## Reflection and atoms

For a strict sign gap, reflecting X swaps the two conditional classes,
p with q, and Ui with minus the opposite class. Beta and signed third moment
change signs, while rho, variance and positive first moment are unchanged.
However the event identity is

```
P(sum(1-Yi)<=n-z) = 1-P(sum Yi<z).
```

The strict inequality on the right matters at every atom. Moreover if X has a
zero atom, the sign convention B=1{X>0} prevents simply setting the reflected
positive probability to q. A direct right-half proof avoids both issues and
preserves the original acquired orientation. Reflected-law tests are semantic
controls, not a license to reuse an asymmetric acquisition contract.
