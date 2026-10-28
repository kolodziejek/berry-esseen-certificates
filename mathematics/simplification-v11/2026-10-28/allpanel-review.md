# Independent review of the all-panel small-noise comparison

**Outcome: no mathematical blocker found in the stated theorem or its join
to the acquired support strips.** This is a bounded review of the explicit
small-noise implication, not acceptance of a complete sharp-conjecture proof.

Review base: `6027b27f85473780eaf90542f490168873de5986`.
Separate branch: `research/allpanel-review-v11-20261028`.
The constructor's files were read but neither imported nor executed.
The reviewer previously constructed the left-panel strip, so this report is
independent of the **count theorem's** construction, not an independent
second review of the strip construction. The coordinator separately read
the strip proof and checker before integration.

## Statement and evidence

The reviewed statement concerns actual iid pairs `(B,U)` with conditional
mean zero, `n>=42`, `p in[1/4,53/100]`, conditional amplitude at most `.7`,
inward displacements summing to at most `.068`, `|H|<=1.84`, and
`0<lambda=ns<=.002`. For every `0<=C<=.41`, the displayed comparison
`Delta_C` is strictly below `-lambda/100`.

| Item | Mathematical status | Execution status |
|---|---|---|
| The stated analytic implication | Independently rederived; no blocker found; retains the published quadratic Poisson comparison, finite factorial estimate and elementary Gaussian constants | Constructor arithmetic read, not rerun by reviewer |
| Own-count quartic rectangles | Independent proof using original bivariate polynomials | All 40 tensor Bernstein coefficients strictly positive |
| Normalization, repairs, variance envelopes, switches and three final margins | Independent rational reconstruction with positive denominator checks | Fresh PASS |
| Actual conditional-count identity | Independently checked from exact iid convolution and separate conditional sums | Ten exact selected-event tests, including an atom collision |
| Infinite Poisson-tail coverage | General coefficient-ratio proof given below | Finite integer checks are controls only, not proof of the infinite assertion |
| All-panel acquisition join | Correct same-law scaling and closed-panel coverage | Reviewed against the strip and geometry results; earlier Fourier cover not rerun |
| Larger noise and finite base | Open, unchanged | Not accepted here |

The fresh independent result is
`runs/allpanel-review-v11-20261028/check01/stdout.json`.
Its receipt records Python version, command, source hash, duration, return code
and output hashes. The checker uses only Python integer/rational arithmetic.

## Independent derivation

### Conditioning, atoms and the legal count

For fixed count `j`, the conditional sum has the law of `j` independent
`U_1` terms and `n-j` independent `U_0` terms. This uses one common iid
marginal, not a separately optimized law for each count. At threshold `k+u`,
subtracting the binomial CDF gives outgoing events `W_(k-i)>u+i` and incoming
events `W_(k+i)<=u-i`. Their strict/closed directions are correct at atoms.
Discarding all outgoing terms except the own count makes an upper bound.
The displayed `Delta_C` therefore equals the binomial comparison in the
master inequality, with precisely the stated normal and moment repair.

Since `v>=3/16`, `s<=1/21000`, and `v<=1/4`, one has
`sqrt(v+s)<.501`. Thus `|delta|<1.71` globally and `<1` for `|u|<=.05`.
Both `p` and `k/n` lie strictly inside `(.2,.58)`, so the entire Taylor
segment lies there. In particular the count is interior. The phase interval
has width exactly one; the floor choice gives every threshold a valid anchor.
Closed phase endpoints remain covered even when two anchors are possible.

### Finite normalization

On the whole Taylor segment,
`r(1-r)>=.16` and `|1-2r|<=.6`. Independently differentiating binary relative
entropy gives the third derivative magnitude
`|1-2r|/[r^2(1-r)^2]<24`; the logarithmic prefactor derivative is below `4`.
The signed finite factorial remainder is bounded in absolute value by
`1/[12 n r(1-r)]<.53/n`. Consequently

`n|e| < 2 D_0 + .53 + 4 D_0^3/42`

is a valid finite, uniform bound. No fixed-law asymptotic is substituted.
The actual count stays fixed while differentiating the Gaussian phase.
Splitting its exact logarithm gives a variance coefficient at most
`1/(2v_*)+D^2/(2*42*v_*^2)<4`, plus the stated phase cross-term and `Z`.

The independent check reconstructs the lower masses `.69/.56`, derivative
bounds `[.9,1.08]` and `[2/3,3/2]`, and positivity of all exponential
denominators before using `exp(x)<=1/(1-x)`. At a mode, displacement is at
most one, and the upper mass is below one. This gives the global ratio
`1/.56<1.8`. In the inner interval, the first exact binomial recursion is
at most `1+p/(nv)<1.07`; later ratios are at most one since
`(n+1)p-k<1.53<2`. These arguments include `p>1/2`.

### Adverse moment repair

The inward bounds imply `a_0<p` and `a_1<q`, so the signs of `Y-p` are
fixed by `B`. Expanding its absolute cubic separately on the two signs gives

`E|Y-p|^3 >= v(1-2v) + (3*min(p,q)-d_*)s`.

This follows pointwise from `U_0^3<=a_0 U_0^2` and
`U_1^3>=-a_1 U_1^2`, including negative values of the noises.
Using the Taylor upper bound for `(1+s/v)^(3/2)` yields the displayed
possibly negative coefficient. Its adverse magnitude is bounded by `B_*`
using `min(p,q)>=1/4`, `v>=3/16` and `s<=U_*/42`. The exact square
comparison includes `B_*>0` and proves

`C*(rho_B-rho) <= (4/3)s` for `0<=C<=.41`.

The normal repair has derivative at most `(5/2)*delta_+` in `s`.
This proves the inner `4lambda/n` and global `6lambda/n` bounds.
The adverse three-point example is valid and correctly described as a
counterexample to discarding the repair, not to the theorem.

### Own-count variance and the original quartic

Because `|s_1-s_0|<=s/min(p,q)<=4s`, the own variance lies between
`19lambda/21` and `23lambda/21` in the inner interval, and is at most
`7lambda/6` globally. Incoming variances are at most `iVlambda` with the
displayed `V=6/5` or `4/3`. This follows from
`|delta+i|<=D+i<=i(D+1)` and `i>=1`.

For a centered independent sum of variance `t`, the expansions give
`|EW^3|<=At` and `EW^4<=A^2t+3t^2`. The quartic indicator minorant is
nonpositive on the negative half-line, zero at zero, and has positive
maximum below one. After shifting, its expectation gives exactly the
displayed polynomial `F`. Thus the strict event is handled correctly.

Instead of reproducing the constructor's quadratic truncation, this review
uses the **original** `F-claim`, of bidegree `(4,3)`. On
`[0,z_0] x [0,23/10500]`, its tensor Bernstein coefficients are

`sum a_(i,j) z_0^i T^j binom(k,i)/binom(4,i) binom(l,j)/binom(3,j)`.

All 20 coefficients are positive for each sign. The minima are
`10788447499/444528000000` and `569/5670`. This proves both full rectangles
by an independent polynomial representation, without sampled noise values.
The divided polynomial extends continuously to `t=0`; actual `t>0` follows
from `lambda>0` and the lower variance bound.

For the negative switch, Cantelli gives a lower bound for the strict
outgoing probability, by complementing a closed lower-tail event. The
Cantelli-minus-linear derivative first increases and then decreases.
Its positivity at `r=3t/2` leaves only a possible maximum afterwards.
Both endpoint comparisons hold at the largest `t`, and hence at smaller
`t` by monotonicity. On the positive side, after `r=t` the normal increment
alone exceeds `4t/5`. There is no gap at either switch.

### Complete incoming Poisson tail

The retained Pinelis theorem compares quadratic hinges for centered
independent summands bounded above by `A`, with **an upper variance budget**.
Applying it to `-W_(k+i)` and then Markov covers the closed incoming event.
The physical hinge is `A(j-mu)`; its denominator is positive exactly when
`j<x/A+mu`. The proof checks that condition before using each hinge.

For the first count, `j=1` is legal in the inner and negative phase ranges.
Its exact numerator is `mu^2-mu+1-exp(-mu)`, and Taylor bounds this by
`mu^2/2+mu^3/6`. Its ratio to `lambda` is increasing on the stated inner
range: differentiating leaves a numerator proportional to
`(a-mu)/2+a*mu/3>=0`, where `a=(1-b)/A-1` and `mu<=a`.

For `i>=2`, write `r=P-i>=1`. At `i=2`, the pointwise inequality
`r^2<=binom(i+r,i+1)` is equivalent to `(r-1)(r-2)>=0` for integer `r`.
For fixed `r`, increasing `i` increases the binomial coefficient. The
Poisson factorial-moment identity then bounds the numerator by
`(i*mu)^(i+1)/(i+1)!`.

For `i>=m`, the denominator is at least `i*(b_m+mu)`.
After division, the coefficient is `i^(i-1)/(i+1)!`. Its successive ratio is
`i/(i+2)*(1+1/i)^i<3`: expand the binomial and bound by the exponential
series, whose sum is strictly below three. Hence the infinite sum is bounded
by a geometric series of ratio `3mu<1`. The starting coefficients are
`1/3` for `m=2` and `3/8` for `m=3`, exactly as printed.

This is a proof of the full infinite tail, not a finite cutoff. Legal actual
counts form a finite subset; extending their positive scalar upper bounds
to all `i>=m` is harmless. At the upper phase endpoint the second hinge is
indeed illegal. Treating the first **two** counts by Cantelli and starting
the factorial tail at `i=3`, where `b_3=59/1050>0`, correctly repairs that
domain obstruction.

### The three phase intervals

The inner bound is relative to `lambda`, with no additive error surviving
at zero noise. For the negative outer interval, the Cantelli-minus-linear
function is concave because `3b^2>7U_*/6`; its minimum is at an endpoint.
For the positive outer interval, each Cantelli tail is convex in the phase
because `3(i-h)^2>i*(4U_*/3)` for `i=1,2`. Subtracting these tails from the
linear normal increment gives a concave function, again minimized at an
endpoint. The rest is the uniform `J_3` tail.

All three brackets are positive before a lower binomial mass is substituted.
The independently reconstructed positive margins are exactly

- inner: `17926467866165398367/1060536251855551002000`;
- negative outer: `303207159039/1226220050000`;
- positive outer: `1429750577643511489/102275398586900550000`.

In the outer intervals, increasing noise to `U_*` decreases the chosen own
lower bound or increases the subtracted tails and repairs. The resulting
margin exceeds `U_*/100`, and therefore also actual `lambda/100`.
The three closed phase intervals cover every phase and share both seams.

## Actual-law and negative controls

Two rational three-point laws were convolved directly on an integer lattice
for `n=42`. Separate conditional binomial sums reproduce the exact correction
at five phases for each law, including both seams and an own-count atom at
zero phase. Closing the strict outgoing event would change the answer by
the strictly positive mass of that atom. No rounded locations are used.

The finite integer checks of the factorial inequality supplement its general
proof above. They also exhibit its failure at `i=1,P=3`. The invalid second
outer Poisson hinge is rejected by its negative denominator. These are
mathematical domain controls, not merely intentionally corrupted hashes.

## Composition and remaining scope

The left-panel result supplies `-.6<U_0<=a_0` and `-a_1<=U_1<.7` on
panels 25--39; the right-panel result supplies the stronger `.6` amplitude
on panels 40--52. Together they cover all retained closed panels. Their
same-law scale is `U=(X-E[X|B])/ell`, so `s=theta/ell^2` and
`lambda=ns=n*theta/ell^2`. The inward displacements sum to `d<.068` and the
retained raw threshold is below `1.84`. Thus every acquired witness in
the small-noise range satisfies the theorem's premises.

For `C=C_E`, its `Delta_C` equals
`a+rho_B*(C_E-C_B)`. Schulz's strict finite-n bound makes the second term
positive. At zero noise, conditional noise vanishes and the law is Bernoulli
directly. No limiting argument at arbitrarily small positive noise is used.

The probability is that of the oriented positive closed-CDF witness. Negative
errors still use the existing reflection-and-attainment argument; the entry
is not identified with its reflection. Acquisition retains contact,
nonnegative excess and sharp predecessor. The small-noise theorem itself
does not require these premises once its actual-law domain is given.

This supports removal of the separate low-noise left/right count branches
and half-amplitude/marked-crossing/Poisson-cubic machinery **on this stated
small-noise domain**. A quadratic Poisson comparison remains a new explicit
external dependency. Larger noise, the coarse Fourier cover and `BASE41`
remain unresolved or retained as described by the coordinator.

## Source binding

The exact reviewed source snapshots are preserved under
`runs/allpanel-review-v11-20261028/source01/`:

- `allpanel.tex` SHA256
  `bd9d32de7000391edbc6a94547316b7c88234cc9aaf6d2c4f4c2d2de183dbf15`;
- `allpanel_check.py` SHA256
  `75c8e09509354ecfad9d1172b4a4f41f7b06e62195ced817b240f5471ad3d844`.

The review pins the final source after the source-location formatting change.
It does not independently reprove the complete earlier Fourier/contact
ancestry or the published Pinelis and Schulz theorems. Those inputs are
identified, and their actual hypotheses match the applications above.
