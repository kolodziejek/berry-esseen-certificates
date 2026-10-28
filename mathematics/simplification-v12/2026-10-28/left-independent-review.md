# Independent review of LEFT-01

The proof establishes the stated local comparison with no unresolved blocker
found in this review: for n≥42, p∈[1/4,2/5], conditional centering,
−.7≤U0≤a0, −a1≤U1≤.7, a0+a1≤.068, raw |H|≤1.84,
0<ns≤.01, and C∈[819/2000,.41], its Delta_C is less than −ns/100.
This is a count-comparison implication, not acquisition of its premises or
a proof of BASE41 or the full conjecture. The reflected branch must satisfy
its own acquired premises. The old all-panel .002 result is unchanged.

| Item | Mathematical status | Execution status |
|---|---|---|
| Joint own-count / marginal-third-moment identity and endpoint guards | Independently rederived below | 9 actual iid marginals, 36 strict own-count events pass independent rational enclosure controls |
| Inner quartic inequalities | Independently reconstructed from shifted moments, with no constructor imports | 40 strictly positive tensor Bernstein coefficients; four off-grid polynomial identities PASS |
| Complete incoming tails and six closing margins | Analytic derivation read and rederived; full infinite continuation included | Six independently reconstructed rational margins PASS |
| Finite normalization, signs, atom conventions and scope | Source read; no blocker found | Constructor's 88 gates and source hashes inspected; these are not called independent normalization tests |

The independent source is `left-independent.py`. The saved run is
`runs/left-review-v12-20261028/check01/receipt.json`; it records the interpreter,
command, output and source hashes. The reviewed proof SHA256 is
`f038aa62e039bfe48482fe69c1438553e90f7c246bf0fa74322115c33ea76ea9`;
the reviewed scalar checker is
`2e5190c9b035e54cd9e89a164fc335dc7cc7a535cc77d4931d616f397f0cb6d6`.
The independent script does not import either file or the previous event helpers.

## The joint estimate preserves the same law

In the proof's joint-reserve section write N0=n−k, N1=k,
T0=N0 E U0², T1=N1 E U1² and gamma=C ell³ M/m. Direct expansion
of the shifted quartic gives cubic coefficients
−4r N0−gamma q and −4r N1+gamma p. Thus the endpoint prices use
kappa0=−4r−gamma q/N0 and kappa1=−4r+gamma p/N1.
The bounds q/N0<1/38 and p/N1<1/38 follow from |k−np|<1,
n≥42, p≥1/4, q≥3/5. The displayed guard places the price maxima
at −A for group 0 and A for group 1.

The resulting fourth/cubic term is exactly bounded below by
−A²(T0+T1)+4Ar(T0−T1)+gamma A(q E U0²+p E U1²)−3t².
The favorable gamma term is gamma A s with the actual marginal s.
No common-fraction substitute for T0,T1 occurs. After T0−T1≥−t,
the marginal cubic expansion leaves the bracket
A+3 min(p,q)−(3/2)(1−2pq)−3(1−2pq)s/(8pq).
It is uniformly positive and the stated C lower bound makes the reserve
strictly greater than 7s/4. This does not claim rho≥rho_B on the left.

The independent event controls use n=64 (so sqrt(n)=8 exactly), three
probabilities including p=.26 and .4, and one-sided or two-sided rare noise.
Six marginals have nonzero k−np, exercising the physical count conversion.
All conditional products and threshold collisions are retained. Square-root
enclosures use integer square roots with checked enclosing squares.
These examples validate conventions and arithmetic, not universal coverage.

## Continuous reductions

The shifted quartic is concave in t. Its negative-phase derivative in z is
negative on the indicated rectangle; its positive-phase derivative is
positive there. Independently, exact interpolation of the original shifted
moment expressions gives positive Bernstein arrays of degrees (3,4) on
the whole t,z rectangle for both target coefficients. This is a different
acceptance route from the constructor's derivative and corner tests.

For the Cantelli extension the derivative is initially positive and has
one maximum before decreasing. A minimum is therefore at an endpoint.
The switch r=3t/2 uses the actual variance, and both branches include it.
All lower bounds extend to every positive t allowed by the theorem; no
fixed-law limit is used.

The incoming quadratic hinge uses the correct closed event and upper
bound on −Uj. For index i≥2, (P−i)_+²≤binom(P,i+1) is a pointwise
integer inequality. The coefficients after the i-dependent variance
inflation have ratio less than 3mu, including the infinite tail. The first
two counts at large positive phase instead use Cantelli because the
second Poisson hinge there is inadmissible. The denominators and the
Q/lambda, J2/lambda monotonicities have the asserted signs.

The four closed outer phase intervals have no gap. On the positive far
interval both Cantelli terms are convex; subtracting them leaves a concave
expression whose minimum is at an endpoint. The six independent final
margins match the constructor's printed fractions.

## Dependency consequence

At C_E this extends the left count exclusion from ns≤.002 to ns≤.01.
It removes the need for another count certificate only on this newly
covered domain once its strip, centering and threshold hypotheses have
been acquired. The heat/contact/sharp-predecessor acquisition chain,
coarse Fourier entry, remaining larger noise and independent finite base
are still obligations. No certificate deletion or manuscript claim follows
from this scoped review.
