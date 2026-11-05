# Corrected independent polynomial audit: exact scope

This is a fresh audit of the seven selected acquired n=5 contracts. It does not re-prove original acquisition, the common conditional-moment reduction, Gaussian inversion or the full n=5 theorem. Its source is a new epoch; it does not edit the supplied review, proof objects or native reader.

## Two independently expanded cubics

Let `q=1-p`, `v=pq`, `x=q E U0²`, `y=p E U1²`. The actual centered sign-conditional variables satisfy `Y=B+U`, and the normalized law is `X=(Y-p)/sqrt(w)`, where `w=v+x+y`. Write `E U0³=gamma0 E U0²` and `E U1³=gamma1 E U1²` when the corresponding variance is nonzero. At zero variance both the second and third moments vanish, so the formulas extend without division.

Because the original sign premise places `Y-p` on the corresponding side of zero, direct expansion gives

    R = E|Y-p|³ = v(1-2v) + 3px + 3qy - gamma0*x + gamma1*y,
    G = E(Y-p)³ = v(1-2p) - 3px + 3qy + gamma0*x + gamma1*y.

For example the negative conditional contribution to R is `q E(p-U0)³ = qp³ + 3px - gamma0*x`; the positive contribution is `p E(q+U1)³ = pq³ + 3qy + gamma1*y`. The analogous signed expansion gives the second line.

Given original bounds on rho and signed gamma, and directed bounds `wl≤w≤wh`, set `sl=wl*sqrt_lower(wl)` and `sh=wh*sqrt_upper(wh)`. Then

    Rlo = rho_lo*sl, Rhi = rho_hi*sh,
    Glo = min(gamma_lo*sl,gamma_lo*sh),
    Ghi = max(gamma_hi*sl,gamma_hi*sh).

This handles either sign of the signed-moment interval. The four actual-law slacks are

    Rlo-R, R-Rhi, Glo-G, G-Ghi,

all nonpositive. Nonnegative exact dual prices may therefore be added to the score target. The corrected audit independently constructs these four polynomials and multiplies by the positive clearing factor `v²`. It checks all four dual coefficient arrays on every vertex/corner of all 63 leaves, even when their actual prices are zero.

The dual arrays are independent of phase. The audit verifies that all five phase coefficients at each probability index agree, then independently inverts the ten probability Bernstein coefficients and compares them with the sparse direct polynomial after affine substitution. This verifies the full 50-entry tensor without repeatedly expanding its constant phase factor.

## Score and Hessian reconstruction

The helper `independent_polys.direct` expands all six shifted quartic expectations from one common pair of conditional laws. Its fourth-moment bound uses `3(1-1/5)t²`, giving the `12/5` moment and `24/5` Hessian factors. The audit independently builds the Hessian entries, applies the Gaussian curvature correction `-25 M v²` to all three entries, checks the determinant, and checks each representation through a separate inverse Bernstein transform.

The Gaussian scalar itself, the outer variance polygon, inward ceilings, native normal constants and forward Bernstein conversion remain shared. The audit independently verifies the representation of the Gaussian-derived target, not the Gaussian scalar's analytic lower-bound property. The independent curvature calculation uses the direct derivative formula

    g'' = a(3D-a²) phi(a/sqrt(D)) / (4 D^(7/2)).

The nonpositive branch requires `min(a_min,0)²≤3Dmin`; the positive branch is bounded by `3 max(a_max,0) phi0_hi/(4 Dmin² sqrt_lower(Dmin))`. The calculation is compared with the shared implementation. The directed square-root calculation in this audit uses its own integer-square-root expression.

For each actual object leaf, the corrected score is reconstructed as

    Gaussian target + theta*cubic improvement
    + sum(price_i * dual_i) - quartic expectation.

Its inverse tensor must equal the independent direct polynomial and every Bernstein coefficient must be strictly positive. Its minimum, prices and PSD minima must then equal the actual native leaf admitted under the same object hash and source epoch. The equality is an evidence join, not a substitute for positivity.

## Coverage, controls and provenance

The seven external row IDs, all complete source-derived nearest-count roots, exact object headers, p/phase/noise domains and both dyadic children are checked. The observed counts are derived before being required to equal 7 rows, 20 roots and 63 leaves. The same 295 packaged records are independently passed through the elementary nearest-count formula; this does not authenticate 288 unbundled original source files or re-prove their acquisition.

For the nonzero-priced leaf, the audit also calculates the full coefficient minima with the price omitted and sign-reversed. Each changed tensor must differ from the exact independently reconstructed native score polynomial. Positivity of either alternate sufficient bound is recorded rather than presumed to fail. The object itself is unchanged.

A separate targeted control uses six globally valid polynomials `Q_j(z)=2+10^-12 z^4`. The native ray checks must all pass first; the positive-curvature PSD test must then reject. This isolates the Hessian obligation rather than mistaking an earlier ray rejection for a curvature test.

The complete fixed package manifest is verified before importing its code. The audit records hashes of every package file, its own source and the independent sparse helper before and after execution. Ordinary unoptimized Python and a fresh output directory are required. No historical success flag supplies a polynomial inequality. The final run reports separately what was reconstructed and what remains shared.
