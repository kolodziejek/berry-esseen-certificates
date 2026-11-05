# Analytic audit of the external all-Taylor n5 extension

Reviewed read-only source:
`/Users/bkolodziejek/Documents/BerryEsseen/research/count-transfer-20261105/n5-all-taylor/`.
The selected file identities are in `SOURCE_PINS.json` beside this review.
No external checkout file was changed and no inherited program was imported
or executed for this audit. The required working directory was made with
`tools/prepare_worktree.py`; its capture is
`runs/argon_audit_20261105/analytic_prepare01`.

| Aspect | Mathematical status | Execution status in this audit |
|---|---|---|
| Both-half Gaussian quadratic lower bound | Independently re-derived; no defect found in the reviewed formulas | Source read only; no inherited arithmetic run |
| Uniform noise-curvature bound and corrected n5 Hessian | Independently re-derived; no defect found | Source read only |
| Mean cap, beta polygon, common moments and cubic prices | Valid outer bounds under the original same-law acquisition premises | Source read and prior-byte comparison only |
| Seven entire rows /63 leaves | Conditional claim requiring the complete source-domain and exact-object replay | Supplied claim; not freshly replayed by this reviewer |

## Findings needing correction

1. **Wrong stated target constant.** README.md:5 says
   `C_E = 9199/25000`, which is0.36796. The actual mathematical constant is
   `(3+sqrt(10))/(6 sqrt(2*pi))`, approximately0.40973.
   This is a documentation defect, not a changed acceptance target in the
   reviewed code: model_all_taylor.py:99 uses `normal.CE_LO`, and
   native/finite_binomial_core.py:19–23 constructs the original rigorous lower
   enclosure `(3+sqrt(10)_lo)*phi(0)_lo/6`.
   The entire native file and algebra.py are byte-identical to our prior
   accepted copies. No precision reduction was found.

2. **Wrong total root count.** README.md:38,54 say19 roots. The seven displayed
   root families contain `3+2+3+3+3+3+3=20` roots. The local object directory
   likewise contains20 named row/root objects. This must be reconciled with
   the actual aggregate reader result; it does not invalidate the independently
   checked analytic reduction.

3. **Directed denominator notation.** README.md:13 should say
   `0 < s_min <= sqrt(d_min)` and use a lower rational enclosure, rather than
   identifying the computed `s_min` with the exact irrational square root.
   Also use `phi_HI` for the density-at-zero bound, rather than ambiguous
   `Phi_HI`. The code correctly uses the lower root and density bound.

There is no `proof/` directory in the supplied n5-all-taylor package. The
README provides the new inequalities but not the full Taylor-remainder or
nine-corner derivation. For a reader-facing proof, explicitly link the retained
common-law proof and Gaussian derivative/Taylor proof, and include the short
curvature-to-PSD argument below. This is an exposition dependency; the
reviewed formulas have a valid derivation.

## Independent Gaussian derivation

Write `a=k+u-np`, `D=np(1-p)+lambda`, `z=a/sqrt(D)`.
For a fixed variance vertex, lambda is fixed. On any closed
`0<pl<pu<1` probability interval,

    vmin=min(pl(1-pl),pu(1-pu)),
    vmax=max(pl(1-pl),pu(1-pu),1/4 if the interval meets1/2).

Thus the change in gaussian_scalar.py:32 is valid on either probability half
and across1/2. No reflection or altered closed-event convention is used.
The derivatives are

    z_u=D^(-1/2), z_uu=0,
    z_p=-n D^(-1/2)-a D'/(2D^(3/2)),
    z_pu=-D'/(2D^(3/2)),
    z_pp=n(D'+a)/D^(3/2)+3a(D')²/(4D^(5/2)),
    D'=n(1-2p).

For `G=Phi(z)`, `G_ij=phi(z)(z_ij-z z_i z_j)`. The bounds at
scalar lines33–36 follow from `|a|<=A`, `|D'|<=B`, the directed positive
sqrt(Dmin) lower bound, and `phi(z)<2/5`. They are whole-rectangle bounds.
The center exponential uses the unchanged degree24/25 alternating bounds
under the explicit `0<=a_center²/(2D_center)<=1` guard. Gradient endpoints
are rounded outward (10^20 grid), Hessian bounds upward (10^16 grid), and
the center CDF uses the unchanged exact native enclosure.

The integral Taylor remainder, together with
`2|dp du|<=eta dp²+du²/eta`, proves the quadratic lower polynomial at
lines37–39, including its gradient-rounding subtraction. Its expanded signs
are correct. Multiplying by `(pq)^2` has degree at most(6,2), so it fits the
existing score degree(9,4). The scalar rejects unsupported exponent domains;
it does not silently extrapolate the alternating-series bound.

For varying noise, direct differentiation gives

    g''(lambda)=a phi(a/sqrt(D))(3-a²/D)/(4D^(5/2)).

The negative-numerator guard at scalar line50 ensures every negative-a case
has nonpositive curvature on the entire noise half-line lambda>=lo.
For a>=0, dropping the negative cubic term gives

    g'' <= 3 amax_+ phi(0)_hi/(4 Dmin² sqrt(Dmin)_lo) = M.

This proves lines44–53 for both probability halves and for cells crossing
zero numerator. It uses the actual noise lower endpoint, not a sampled
lambda or a sign inferred from phase u alone.

## Why the variance-vertex step remains valid

Let x=q E U0², y=p E U1² and t_j=(5-j)x/q+j y/p. After the common
nine-corner reduction, the only quadratic variance term in the quartic
expectation bound is

    (12/5) sum_j binom(5,j)p^j q^(5-j) c_(j,4) t_j².

Consequently its Hessian is

    H_F=(24/5) sum_j b_j c_(j,4) v_j v_j^T,
    v_j=((5-j)/q,j/p).

Every c_(j,4)>0 is checked. Clearing the positive factor `(pq)^2` gives
exactly the three polynomials at model lines117–120: factors `(5-j)^2 p²`,
`(5-j)j pq`, and `j² q²`. These have degree<=7. The determinant has degree<=14.
The8+8+15=31 nonnegative Bernstein coefficients checked at lines124–127
suffice for a positive-semidefinite symmetric2x2 matrix on the whole p cell.

Because lambda=5(x+y), the Gaussian Hessian in x,y is `25 g'' J`, with J the
all-ones matrix. The code checks `H_F-25 M J` PSD. Therefore

    H_F-25 g'' J = (H_F-25 M J)+25(M-g'')J >= 0.

All absolute/signed raw-cubic prices used here are affine in x,y at each
fixed common moment corner; they add no Hessian. Thus the actual upper loss
is convex on the outer variance polygon. It may be bounded at its vertices.
Only then is each actual Gaussian value replaced by its fixed-lambda Taylor
lower polynomial. No concavity of the polynomial in lambda is needed.

The nine common gamma/inward endpoints must be selected after summing all
six count expectations. The source does this: model lines65–75 and101–111
use the same vertex and common corner across every j. The old moment proof
first maximizes affine gamma dependence at support endpoints and then convex
inward-endpoint dependence at0/r_i. The new Gaussian and affine prices do
not change this argument. It would be wrong to assert a pointwise fourth
moment bound `E Ui^4 <= gamma_i² E Ui²` before that endpoint reduction; the
reviewed code uses it only in the reduced corner expression.

## Domain, support and price checks

- Model lines37–40: from `m=v/sqrt(w)>=m_lo`,
  `lambda<=5(v²/m_lo²-v)`. The explicit `2vmin>m_lo²` gate makes this function
  increasing throughout the cell, so its maximum is at vmax. An unsupported
  domain rejects. This is valid on the right half too.
- Lines41–44: actual sign endpoint bounds imply
  `U0<=p-epsilon0 sqrt(w)` and `-U1<=q-epsilon1 sqrt(w)`. The fixed r0/r1
  use safe p/q maxima and a directed sqrt(vmin+lo/5) lower bound. They remain
  relaxations of one actual conditional pair; no reflected row is substituted.
- Lines48–59: beta equals `[v(1-2p)-x+y]/(v+x+y)`. Its two inequalities have
  exactly the displayed affine left sides and cubic right sides. Replacing
  each right side by its maximum Bernstein coefficient over p enlarges the
  feasible set. The nonnegative variance/noise planes make the outer polygon
  compact. All feasible pairwise plane intersections are enumerated. Empty
  polygons cannot pass; fewer than3 intersections reject conservatively.
  The computation does not claim every retained point is a realizable law.
- Lines77–92 and99–111: actual
  `R=v(1-2v)+3(px+qy)-gamma0*x+gamma1*y=rho*w^(3/2)>0` and
  `G=v(1-2p)+3(-px+qy)+gamma0*x+gamma1*y=gamma*w^(3/2)`.
  The fixed upper w enclosure gives a valid affine lower price for
  `C_E*rho/sqrt(5)`, blended with the original rho-floor price by0<=theta<=1.
  R may become negative at artificial corners; that does not invalidate the
  bound established first on actual laws and then extended as an upper loss.
  The four optional slacks are nonpositive on actual laws and have the
  correct target signs. Signed G endpoints use sign-safe products, including
  intervals crossing zero. Their prices are required nonnegative.
- Zero conditional variance and zero total noise cause no division by x or y.
  Unsupported zero-dimensional polygons are rejected rather than treated as
  automatic proofs. The closed threshold/atom majorants and original root
  catalogue still require the separate complete reader audit.

No analytic unsoundness was found in this reviewed scope. Correct the stated
constant/root count, supply explicit proof links, and require the separate
fresh full object/census replay before promoting the seven-row execution claim.
