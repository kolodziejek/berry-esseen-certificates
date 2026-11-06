# Conditional license for raw third-moment prices

This is an independently derived possible strengthening, not a numerical
acceptance record. The notation and common-law assumptions are those of
`GENERAL_SCALARS.md`. All prices are fixed nonnegative rationals on a complete
probability/phase/noise cell.

The exact raw absolute and signed third moments are

```
R = v(1-2v)+3(px+qy)-gamma0*x+gamma1*y,
G = v(1-2p)+3(-px+qy)+gamma0*x+gamma1*y.
```

They equal rho*w^(3/2) and gamma*w^(3/2), respectively, for the same actual
marginal. On a slab with positive fixed lower width w_min and upper width
w_max, the acquired rho interval gives outward bounds

```
R_lo <= rho_lo*w_min^(3/2),
R_hi >= rho_hi*w_max^(3/2).
```

Take R_lo with a directed lower root and R_hi with an upper root. Bounds for G
come from the minimum and maximum of the four products of the acquired signed
gamma endpoints with an enclosure of w^(3/2). In particular, a negative lower
gamma requires the *upper* width factor for a valid lower G bound; a negative
upper gamma requires the *lower* factor for a valid upper G bound. Positive
endpoints use the opposite choices. This sign distinction cannot be dropped.

Let T be any already justified sufficient CDF target, including the optional
fixed rho blend and the actual Gaussian used in the convexity argument. For
fixed a,b,c,d>=0, define

```
T_aug = T + a*(R_lo-R) + b*(R-R_hi)
          + c*(G_lo-G) + d*(G-G_hi).
```

Every added term is nonpositive for an actual law. Therefore proving the CDF
upper expression strictly below T_aug proves that it is below T. Equivalently,
the upper loss gains nonnegative constraint slacks on actual laws. Artificial
moment corners can violate those constraints, so their target can increase;
this is legitimate after forming the actual-law upper loss and maximizing it
over the enlarged domain.

The added terms are affine in each common gamma at fixed inward endpoints and
variances. After gamma endpoint selection they add only linear dependence on
an inward endpoint; the existing quartic term still has a nonnegative quadratic
coefficient. After the nine common endpoint choices the added terms are affine
in x,y. Consequently the same common-gamma and convex-polygon proof remains
valid, including a zero conditional variance and zero total noise. No new
moment choices may be made independently for different mixture counts.

R has p degree four and G degree three. Clearing by p²q² gives degrees at most
eight and seven, within the existing n=5 bound (9,4). Prices and raw bounds
must be constant on the cell; data that vary with p, phase or a moment corner
would need another proof. An exact reader must reject negative, noncanonical,
missing or extra prices and retain the original acquisition/whole-cover scope.
