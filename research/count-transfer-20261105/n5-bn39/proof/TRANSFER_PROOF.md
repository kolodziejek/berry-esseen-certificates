# Analytic delta for the three fixed n5 transfer targets

The original six-count/common-variance argument is unchanged. Its full proof
is in `work/count_row_20261105/construct_v1_frozen/SOUNDNESS.md`, with the
normal/noise correlation, same-law cubic price and acquired support/mean
improvements in `work/count_row_20261105/construct/THEORY_V4.md`.
This file gives the additional rules used by the new parameterized reader.

The three targets are separately identified by their full original path and
SHA256 in `CONTRACT_SELECTION.json`. In particular, `B2_S3_34` means the S3
endpoint contract, not another B2/p34 slab. Each has actual n=5 and K=0,
so the comparison target remains C_E. Its original acquisition is a premise;
hashes and old COUNT success records do not prove applicability.

## Both probability halves, without reflection

For a closed cell [l,h]⊂(0,1), put v(p)=p(1−p). Concavity gives

    v_min=min{l(1−l),h(1−h)},
    v_max=max{l(1−l),h(1−h),1/4 if l≤1/2≤h}.

These formulas include p=1/2 literally. All moment, signed-beta and raw
third-moment identities use the original conditional class orientation;
there is no reflection and no conversion of a closed CDF to an open event.

The mean cap is still
lambda≤5(v²/m_lower²−v). The reader verifies 2v_min>m_lower², so this
function increases with v on the whole cell. The cap uses v_max, not a
probability endpoint chosen under a left-half assumption. If this guard
fails the current reader rejects; it does not infer monotonicity.
The three selected rows satisfy the guard.

For a noise slab [L,U], the fixed inward caps use

    r0=min(d,h−epsilon0*sqrt(v_min+L/5)_lower),
    r1=min(d,1−l−epsilon1*sqrt(v_min+L/5)_lower).

The meaning of m and epsilon_i remains the original one-law acquired mean
and closest-sign support premise. The physical inward d is not the affine
resource intercept d0. Neither affine resource denominator is altered.

## A stronger common probability endpoint for the normal term

Let t=k+u and D=np(1−p)+lambda. On 0≤t≤n,

    d/dp [(t−np)/sqrt(D)]
       =−n[np+t(1−2p)+2lambda]/(2D^(3/2)) <0.

For p≤1/2 the bracket is at least np+2lambda; for p≥1/2 it is at least
n(1−p)+2lambda. The standardized argument increases with t. Therefore
its minimum over the p/u cell, for each fixed lambda, occurs at p=h and
t=k+u_lower. Both numerator and variance may use that same endpoint.

For the constant normal lower bound, take the lower noise endpoint if
the endpoint numerator is negative, and the upper endpoint otherwise.
For the correlated negative-Gaussian method, use each polygon vertex's
actual lambda=5(x+y). The code retains the sufficient concavity guard

    a_max=k+u_upper−5l≤0,
    a_min²=(k+u_lower−5h)²≤15v_min.

It then subtracts the actual concave Gaussian before maximizing in x,y,
as in the V4 proof. If the complete t-cell is outside [0,n], the new
endpoint rule is not invoked: the reader falls back to the general
sign-safe v_min/v_max enclosure. Thus a right-half or crossing cell
cannot use an unjustified monotonicity shortcut.

## Complete threshold catalogue

The original raw threshold is H=(t−5p)/sqrt(w), not H/sqrt(5).
The source bounds H∈[−Hminus,Hplus] and sqrt(w)≤S imply

    a=5p_lower−Hminus*S ≤ t ≤ b=5p_upper+Hplus*S.

Every nearest integer representation t=k+u, −1/2≤u≤1/2, is covered by

    ceil(a−1/2)≤k≤floor(b+1/2),
    max(−1/2,a−k)≤u≤min(1/2,b−k).

Both representations survive at a half-integer. The selected contracts
give root sets {1,2,3}, {2,3}, {1,2,3}, respectively. A clipped root need
not contain both signs of u; empty phase portions are excluded by this
explicit raw-threshold inequality, not by dropping an unsupported root.
The current reader conservatively rejects degenerate root intervals and
polygons. No selected row requires a degenerate case to be silently skipped.

The whole-row entrypoint fixes these roots from the pinned original
contract, requires every root once in order, and reconstructs every
complete p/noise/phase tree. It may accept the explicitly larger whole
phase interval [−1/2,1/2], but never an unproved smaller one.

## Optional exact prices of the original rho/gamma restrictions

The baseline model does not use this optional strengthening. The separate
`model_dual.py` keeps the original normalized domains and uses

    R=v(1−2v)+3(px+qy)−gamma0*x+gamma1*y,
    G=v(1−2p)+3(−px+qy)+gamma0*x+gamma1*y,
    rho=R/w^(3/2), gamma=G/w^(3/2).

Here x=q EU0², y=p EU1² and every occurrence uses the same two actual
conditional laws. The shared support proof supplies the same nine common
gamma endpoint evaluations. In particular, G is not an independent
free signed moment optimized separately for each count.

Let positive directed bounds satisfy s_lower≤w^(3/2)≤s_upper. The fixed
raw bounds are

    R_lower=rho_lower*s_lower, R_upper=rho_upper*s_upper,
    G_lower=min(gamma_lower*s_lower,gamma_lower*s_upper),
    G_upper=max(gamma_upper*s_lower,gamma_upper*s_upper).

These expressions handle negative, positive and sign-crossing gamma
intervals correctly. For any four fixed nonnegative rational prices,
adding

    a(R_lower−R)+b(R−R_upper)+c(G_lower−G)+d(G−G_upper)

to the sufficient CDF target lowers it on every actual law. Consequently
a strict quartic bound against this priced target still proves the
original C_E comparison. The slacks can have the other sign at artificial
moment corners; that is legitimate because the actual-law upper loss was
formed before extension to the larger domain.

Each added term is affine in common x,y and gamma. After an inward gamma
endpoint is substituted, it remains affine in the inward endpoint. The
original nonnegative quartic quadratic coefficient is unchanged. Hence
the same nine common endpoint choices and convex polygon maximum apply.
After clearing p²q², these new terms have degree at most eight in p and
zero in phase, preserving the fixed (9,4) tensor degree. The exact reader
requires four canonical rational prices and checks their nonnegativity.

An inconclusive LP or a rejected tensor is never called infeasible.
Discovery's stopping rules only bound work; its remaining failed leaves
are explicit unresolved cells. Complete-row status requires the separate
exact acceptance process, not the discovery return code.
