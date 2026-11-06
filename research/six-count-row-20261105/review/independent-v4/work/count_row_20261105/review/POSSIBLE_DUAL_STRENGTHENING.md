# Optional common-moment constraints

This note derives a possible further certificate rule. No numerical cover using
it is asserted here. All multipliers below must be fixed nonnegative rationals
on the cell. The original target is unchanged.

With the same notation as `SOUNDNESS.md`, sign conditioning also gives

```
G := v(1-2p)+3(-p*x+q*y)+gamma0*x+gamma1*y
   = (E X³)*(v+x+y)^(3/2).
```

This follows by expanding the cubes of U0-p and U1+q, using their zero
conditional means. The third-moment variables remain common to all six counts.
The absolute-cube numerator is

```
R := v(1-2v)+3(p*x+q*y)-gamma0*x+gamma1*y.
```

On a fixed p/noise slab let 0<w_lo<=v+x+y<=w_hi, and let the acquired standardized
signed third moment lie in [g_lo,g_hi]. Directed square roots give a positive
enclosure for w^(3/2). The minimum and maximum of the four endpoint products
give rational bounds G_lo<=G<=G_hi. In the selected row g_lo<0<g_hi, so safe
values are g_lo*w_hi^(3/2) rounded down and g_hi*w_hi^(3/2) rounded up. In
particular multiplying a negative lower gamma by the lower w endpoint would
have the wrong direction.

The acquired rho interval similarly gives
`rho_lo*w_lo^(3/2)<=R<=rho_hi*w_hi^(3/2)`, with outward rounding.

Let H denote the original moment upper expression minus the normal and chosen
valid rho target. For any a,b,c,d>=0, define

```
H_aug = H + a*(G-G_lo) + b*(G_hi-G)
          + c*(R-R_lo) + d*(R_hi-R).
```

For an actual law every added term is nonnegative, so H<=H_aug. Therefore a
certificate H_aug<0 is sufficient. The signs are important: subtracting these
nonnegative slacks would not give an upper bound for an actual law.

The new terms are affine in each common gamma before endpoint reduction and
affine in x,y after it. Their dependence on an inward endpoint at the inward
gamma corner is linear. Thus they preserve the nine-corner and convex-polygon
proof; no assertion that each relaxed corner satisfies the added constraints
is needed. With fixed coefficients, p²q² times G has degree at most 7, and the
corresponding R term at most 8, below the existing n=5 degree bound 9. These
constraints may exclude bad relaxed corners; actual effectiveness still needs
construction and exact acceptance.
