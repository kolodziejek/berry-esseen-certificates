# Additional analytic bounds used by the V4 reader

The six-count identity, common beta polygon, common moment endpoints,
finite Cauchy fourth-moment term, denominator clearing and global ray
tests are those proved in `../construct_v1_frozen/SOUNDNESS.md`.
This note supplies every additional analytic implication used by
`model_v4.py`. It concerns the original positive, closed-CDF comparison
on n5 BN/p38, conditional on that contract's acquired same-law premises.
It does not reverify acquisition or assert an absolute-discrepancy theorem
for arbitrary laws in this oriented probability interval.

## Keep the normal term's dependence on the common noise

For fixed p and u put a=k+u−5p, v=p(1−p), and
g(lambda)=Phi(a/sqrt(5v+lambda)). Direct differentiation gives

    g''(lambda)=a*phi(a/sqrt(D))*(3−a²/D)/(4 D^(5/2)),
    D=5v+lambda.

Thus g is concave for a≤0 and a²≤3(5v+lambda).
On a complete p/u cell the reader requires

    a_max=k+u_hi−5p_lo≤0,
    a_min²=(k+u_lo−5p_hi)²≤15p_lo(1−p_lo).

These imply the condition for every p,u and every nonnegative noise.
For a fixed common gamma pair, the quartic expectation upper bound F is
convex in the common variance pair (x,y). Consequently
F−g(5(x+y)) is convex. Its maximum on the same fixed outer beta polygon
occurs at a vertex. The Gaussian is enclosed at each vertex's actual
noise 5(x+y), using

    Phi(a_min/sqrt(5p_lo(1−p_lo)+5(x+y)))

as a lower bound. The numerator is nonpositive; using the denominator
lower bound makes the ratio no larger. The actual Gaussian is subtracted
*before* invoking convexity; the separately enclosed vertex values are
used only afterwards. This is not an assertion that an arbitrary
collection of independently rounded vertex targets interpolates concavely.

If either condition fails, V4 falls back to the original sign-safe
constant lower Gaussian bound on the whole cell. No concavity is claimed
on a positive-numerator or sign-crossing cell.

## Price the same law's actual third absolute moment

The sign partition ensures p−U0≥0 and 1−p+U1≥0. With
gamma_i=EU_i³/EU_i² when the denominator is positive, exact expansion gives

    R = E|Y−p|³
      = v(1−2v)+3(px+qy)−gamma0*x+gamma1*y,
    rho=R/(v+x+y)^(3/2).

The formula also holds when either variance is zero, with the
corresponding product zero. The actual R is nonnegative. On a fixed
noise slab [L,U] and p cell, let w_max be an outward upper bound on
v+lambda/5. Then

    rho ≥ R/w_max^(3/2),    rho ≥ rho_lower=11/10.

Choose one rational theta∈[0,1], fixed throughout the entire cell. A
convex combination of these two lower bounds is still a lower bound.
The exact sufficient CDF target is therefore

    Phi(...) + C_E,lo/sqrt(5)_hi * (1−theta)*rho_lower
                + theta*c*R,
    c=C_E,lo/[sqrt(5)_hi * w_max * sqrt(w_max)_hi].

The reader uses downward c, so this is valid on the actual domain since
R≥0. Adding −theta*c*R to the upper loss retains affinity in each gamma
before endpoint reduction. At an inward endpoint it only adds an affine
term in the endpoint; the nonnegative quartic leading coefficient still
makes the expression convex. After the same nine common gamma choices,
R is affine in x,y, so the common variance convexity is unchanged.

R can be negative at an artificial extremal evaluation. This does not
invalidate the argument: R≥0 was used only to derive the upper loss on
actual laws. The resulting polynomial expression is then maximized over
an enlarged domain. It is not reinterpreted there as a moment of a law.

After multiplying by v², the R term has degree at most eight in p;
the full test retains degree at most (9,4). Theta is proof data, but the
reader requires a canonical exact rational and checks 0≤theta≤1. The
original C_E target and rho/beta/noise ranges have not been changed.

## Two original acquired constraints tighten fixed endpoint bounds

The contract's `acquired_mean` is m=E X_+=v/sqrt(w), w=v+lambda/5.
Thus m≥m_lo implies

    lambda ≤ 5(v²/m_lo²−v).

The reader verifies 2v_lo>m_lo², so the right-hand side increases with v
on the whole probability cell. It can therefore replace U by

    U_eff=min(U,5(v_hi²/m_lo²−v_hi)).

This is an additional halfplane for the common variance polygon. The
same U_eff also supplies the upper bound w_max=v_hi+U_eff/5. The logical
domain still includes the original full noise interval; its portion
violating the acquired mean bound contains no law under the premises.
V4 conservatively rejects an empty or degenerate noise slab instead of
claiming an exclusion from an unchecked success marker.

The positive constants `negative_endpoint_lower` and
`positive_endpoint_lower` assert that the original standardized negative
and positive conditional supports stay at least those distances from
zero. Consequently

    a0≤p−b_minus*sqrt(w),    a1≤q−b_plus*sqrt(w).

Since w≥v_lo+L/5, the fixed caps used on the whole cell are

    r0=min(d,p_hi−b_minus*sqrt(v_lo+L/5)_lo),
    r1=min(d,1−p_lo−b_plus*sqrt(v_lo+L/5)_lo).

They are checked nonnegative. Subtracting a lower square-root bound
enlarges, rather than shrinks, the permitted endpoints. The nine common
gamma choices become {-A0,0,r0}×{A1,0,−r1}. These are consequences of
the original acquired support; no later confinement or reflected
probability row is imported.

## Status and acceptance boundary

Only `accept_v4.py` with an externally supplied root rectangle checks a
complete root. The construction and repair drivers may leave explicit
failed leaves; their exit code alone is not proof of coverage. The repair
driver preserves old objects and freshly recomputes every old leaf it
reuses. Candidate discovery, numerical LP margins and candidate summaries
have no authority at acceptance.

Every complete-row assertion additionally requires the independent
original threshold census and exact joining of all three clipped roots.
The domain census is maintained separately under `../domain/`; assembly
is maintained under `../assembly/`. This file is an analytic license,
not a record that those executions have completed.
