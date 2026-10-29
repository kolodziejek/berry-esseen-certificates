# Independent review of the direct small-noise comparison

The reviewed claim is: for actual iid conditional laws with n>=42,
p in [2/5,53/100], absolute conditional amplitude at most3/5, inward
displacement at most9/125, raw standardized-marginal sum threshold |H|<=46/25,
and 0<lambda<=1/500, the fixed-target comparison error is strictly below
`-lambda/100`. The phase interval is [-34/125,91/125]. No contact,
half-amplitude, harmonic gain, marked-crossing or Poisson estimate is a
premise of this comparison theorem. Contact may be needed upstream to
obtain the incoming .6 strip.

**Mathematical status:** no blocker found in the full stated analytic
implication after independent derivation of its signs, domains and uniform
small-noise argument. This does not cover larger noise, the left probability
panels, or the independent finite base.

**Execution status:** the constructor's code was read, not imported or rerun.
A separate exact checker proves the two quartic rectangles by40 tensor
Bernstein coefficients, reconstructs the final margins and switch gates,
and rejects two genuinely false stronger estimates. It passed freshly in
`runs/counts-v10-20261028/small-noise-review01/`. This independent polynomial
check uses the original quartic on a two-dimensional rectangle; it does not
wrap the constructor's endpoint/quadratic-vertex implementation.

## Derivation checks

1. From v>=6/25 and s<=1/21000, sqrt(v+s)<501/1000. Thus the shifted
   phase gives |delta|<33/20 globally and |delta|<1 for |u|<=1/20.
   Both legal-count endpoints are strictly interior for every n>=42.
   The full Taylor segment from p to k/n lies inside (9/25,23/40),
   including probabilities above one half.
2. On that segment r(1-r)>.23 and |1-2r|<=.28. These independently
   justify entropy/logarithm/Stirling constants6,5/4,3/8. The signed
   Stirling remainder satisfies the absolute bound used in the proof:
   n|e|<5D/8+3/8+D^3/42. Its derivation uses the finite factorial bound,
   not a fixed-law asymptotic expansion.
3. With the actual count held fixed, splitting the exact logarithmic
   Gaussian derivative gives the variance coefficient
   `1/(2v)+delta^2/(2nv^2)`, bounded by8/3. The cross term uses
   `(2D b+b^2)/(2v)`. The displayed global and inner derivative intervals
   follow with their correct directions, uniformly along each integration
   segment from zero to the actual phase.
4. The mode displacement is at most1. The upper mode mass17/20 and
   lower own mass13/20 therefore imply the global ratio bound3/2.
   In the inner range, delta>=-1 bounds the first binomial ratio by
   `1+p/(nv)`; all later rising factors are <=1 because chi<1.53<2.
   This sharper ratio works above p=1/2 as well.
5. The cubic sign expansion uses r=min(p,q)>=.4. Its bracket is positive
   throughout the proposed domain, so rho>=rho_B and the fixed-c moment
   repair is favorable. Discarding it is valid. The remaining normal
   variance repair is <=(7/4)delta_+ lambda/n, giving2lambda/n in the
   inner interval and3lambda/n globally. No unknown score coefficient
   is used.
6. Own-count variances lie between79lambda/84 and89lambda/84 in the
   inner interval. Incoming variances obey `t_(k+i)<=i V lambda` with
   V=9/8 or7/6. The latter follows from
   `|s1-s0|<=s/min(p,q)` and `|delta+i|<=D+i<=i(D+1)`.
   Extending the incoming sum to all positive integers only increases
   its upper bound.
7. The fourth moment is at most A^2 t+3t^2 by independence and centering.
   Dividing by `(i-u)^4` gives exact zeta-series powers i^-3 and i^-2.
   Their elementary three-term-plus-integral upper bounds are below
   49/40 and17/10. Closed incoming events are covered by Markov; no
   non-atomic limit is needed.
8. The quartic indicator minorant is nonpositive on the negative half-line
   and has positive maximum `(9+6sqrt(3))/20<1`. Its value at zero is0,
   matching the strict outgoing event. On substituting r=zt, dividing
   by t is legal because t>=79lambda/84>0. The resulting polynomial is
   concave in t; its continuous extension to t=0 is used explicitly.
   There is no additive error independent of lambda.
9. Beyond the negative inner switch r=2t, the Cantelli-minus-linear
   derivative is first increasing and then decreasing. Positivity at
   the switch means that any subsequent stationary point is a maximum;
   the minimum is at the switch or r=1/20. All four necessary gates are
   checked. On the positive side, after r=3t/2 the normal term alone
   exceeds t. Both switches lie below1/20 for the entire noise interval.
10. On the outer negative phase, the Cantelli expression with total
    variance11/5000 is concave because3r^2>11/5000. Its minimum is at an
    endpoint. On the outer positive phase, multiply the bracket by
    `(1-u)^4`; the minimum of `u(1-u)^4` is at a phase endpoint. The
    resulting numerator is positive before dropping the denominator
    `(1-u)^4<=1`. This order is essential and is respected.
11. All three brackets are positive before substituting a lower binomial
    mass. The outer errors are increased to the upper noise endpoint;
    the resulting fixed positive margin exceeds lambda/100 for every
    smaller positive lambda. Closed phase intervals overlap at their
    endpoints and cover the full shifted interval. Both signs and zero
    phase are included.

## Independent arithmetic

The original scaled quartic minus its claimed constant is represented in
powers of z and t with bidegree(4,3). Map z in[0,z0] and t in[0,89/42000]
to the unit square. The tensor Bernstein coefficient at(k,l) is

`sum_(i<=k,j<=l) a_ij z0^i T^j binom(k,i)/binom(4,i) binom(l,j)/binom(3,j)`.

All20 coefficients are positive for each of the two rectangles. Their
minimum margins are respectively
`54845200937/1898794406250` and `8089/45927`.
This independently proves the two continuous rectangle inequalities,
without the constructor's quadratic truncation or vertex choice.

The final margins independently reproduce:

- inner per-lambda margin above1/100:
  `219609181/27367410000`;
- outer-negative margin at the upper noise endpoint:
  `39996724269/131600000000`;
- outer-positive margin at the upper noise endpoint:
  `4806449287359/5468750000000000`.

The negative controls are mathematical failures, not only failures of this
certificate format: the negative quartic rectangle does not support the
stronger own-count constant11/10 at its upper corner; a quartic denominator4
would exceed the indicator at x/alpha=4/3.

## Source binding and limitations

The read source snapshots are:

- `small-noise.tex`: SHA256
  `3ff41e1f9be57b844915a07d02d699987ad696b7756e00b5c96d4a36441e6526`;
- `small_noise_check.py`: SHA256
  `823c74206cfcf7c12610cecfda53c7b033ba272db54945f297970e557c78a8c4`.

The reviewer's checker and receipt pin these bytes. It accepts the published
finite Stirling and elementary Gaussian constant inputs at the manuscript's
already derived scope; it is not a new audit of the complete earlier Fourier
or confinement ancestry. It does independently verify that those inputs are
used on the correct actual count segment.

This establishes a useful dependency removal on the stated small-noise
domain: after obtaining the .6 strip, the half-amplitude confinement theorem
and the marked/harmonic/Poisson count machinery are unnecessary there.
It does not justify deleting those results or removing them on the remaining
noise domain. No global sharp-conjecture claim follows from this review.
