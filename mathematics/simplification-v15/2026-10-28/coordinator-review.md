# Coordinator's independent review of the five-count and left comparison proofs

The coordinator rederived the five-count construction and the left comparison
from their displayed assumptions. No mathematical blocker was found. This
review is independent of the two component constructors; the coordinator did
construct the right comparison, which is reviewed separately in
`counts-direct-review.md`. Agreement is not used as a premise.

The mathematical results are local all-law inequalities. Their use in excluding
an extremal witness remains conditional on acquisition. Arithmetic execution,
source identity and analytic justification are distinct kinds of evidence.

## Five counts and the actual iid law

`loss-direct.tex`, Sections 1–3, is accepted at its stated scope. The following
steps were checked separately rather than inferred from its numerical table.

1. For `D=1+U1`, put–call parity gives `h(x)=P(D>x)-E(D-x)+` above
   `1-a1`. The strict survival event is necessary at atoms. Since
   `E(D-x)+ <= (1+A-x)P(D>x)` and `E(D-x)+ >= 1-x`, the kernel is at
   least `(x-A)(1-x)/(1+A-x)` on the final part of `[0,1]`. Below
   `1-a1`, centering gives `h(x)>=x`. These prove the compact minorant
   `(2/5)sin²(pi x)` in both strips, with its stated zero extension.
2. The positive-index replacement errors regroup into one replacement applied
   to `B1+B2`, followed by one applied to `B2`. The negative indices give
   two more replacements. The open supports of adjacent bumps are disjoint
   and their first derivatives vanish at the join, so the Lipschitz constant
   of their summed derivative is still `2pi²`. Each comparison is between
   distributions of actual sums of the two conditional laws. Independence
   between sums at different counts is neither needed nor assumed.
3. The infinite translated bumps sum exactly to a periodic sine square.
   An omitted nonzero translate requires `|V|>2`; the whole omitted sum is
   bounded by one, not by the number of omitted counts. Thus its expectation
   is at most `EV⁴/16`. Boundary bumps vanish and no collision is dropped.
4. The frozen variance is `(nq-delta-1)s0+(np+delta)s1`. The printed
   bounds come from these physical coefficients. The fourth moment follows
   by expanding a sum of independent centered bounded variables, retaining
   `sum EUi⁴ + 3tau² - 3sum(Var Ui)² <= A²tau+3tau²`.
5. The cosine inequalities apply to the diameter of each conditional support,
   not to an unbounded sum. Squaring an individual characteristic function
   uses an independent copy of that conditional variable. Only afterwards
   are characteristic functions multiplied over the independent frozen
   summands. This avoids independence at a selected random count.

The reserve is uniform in phase and includes atoms. Its lower bound may be
negative at small n; the theorem never asserts positivity there. In particular
the table starting at n=125 does not settle n=42.

## Left-strip adaptation and all remaining corrections

`geometry-left.tex`, Theorem 1 and Sections 1–4, has the exact hypotheses
`n>=700`, `p in [1/3,.4]`, conditional outward amplitude `.7`, inward sum
at most `.068`, `lambda in [.01,.32]`, and raw `|H|<=1.84`.
There is no geometric-budget or predecessor premise in this local theorem.

The coordinator independently checked the following constants and implications.

- `v+s<1/4`, so `|w|<.92` and `-1.92<delta<.92`. These give interior
  crossing, five interior counts, and the frozen-variance factors
  `1-6/n` and `1+3/n`.
- On the final kernel interval, the ratio `(x-.7)/(1.7-x)` is at least
  `29/96`. This exceeds `(2/5)(22/7)²(.068)`. The wider cosine domain
  is `.768`; the chord on `[0,.75]` and the derivative bound on
  `[.75,.768]` give `1-cos(2pi x)>=(7/5)x²`. These are new constants
  checked for the left strip, not an invocation of the narrower right lemma.
- Each of the five masses has `|i-np|<4`. At n=700 the whole interpolation
  segment is contained in `[1/3-4/700,.4+4/700]`, with variance product
  greater than `.22`. Finite Stirling and the entropy second derivative
  then give `sqrt(n)pi_i>3/4`. This is a finite bound uniform for every
  larger n, not a local central limit theorem.
- In the curvature lemma, positive adjacent mass differences have `j<np`.
  Their variance is at most `lambda/q<=5lambda/3` and fourth moment at
  most `.49T+3T²`. The lemma keeps at most two near mesh points and sums
  the entire fourth-moment tail; no count coverage is omitted. Its binomial
  mode bound `.41/sqrt((n+1)v)` applies on this probability interval.
- Normal interpolation uses the positive part of the CDF's second derivative
  throughout the unit interval. For `H<=0`, changing the variance is
  favorable. For `H>=0` it incurs the explicitly retained positive cost.
  The two resulting errors are precisely the printed `E-` and `E+`.
- The actual third moment has the fixed conditional signs. Its linear noise
  coefficient is at least `1-5/6-.068`, and its quadratic penalty at most
  `(15/16)s`. At `s<=.32/700` the correction is positive. No third
  moment of an unrelated relaxed marginal is substituted.

The concavity can be seen without coefficient estimates. If the quartic gain
has prefactor `r` and exponential coefficient `z`, then

`W''(lambda) = -r { z²[(z lambda-1)²+1]/4 + 3b²/8 } < 0`.

The error polynomials are convex quadratics. Hence each final polynomial
`W-E/N-lambda/100` is strictly concave on the whole real line. Its positivity
on the prescribed closed interval is therefore equivalent to its two endpoint
checks. The final proof uses four endpoint comparisons, without a subdivision
certificate. The left constructor's exact checker was read line by line; its
Fraction formulas match these derived expressions. Its PASS establishes those
arithmetic comparisons, while the preceding reasoning establishes why they
suffice continuously.

## Anchor obstruction and optional curvature tool

`counts-phase.tex`, Theorem 1, was also checked directly. At its actual closed
three-point atom, floor(t)=20 but the almost noiseless count is 21. The lower
bound uses the event of no rare jump; the opposite anchor uses the definite
loss of the count-21 atom when a rare jump occurs. The two normal-integral
bounds and the third-moment signs have the required directions. This refutes
the proposed universal floor-anchor extension, not the retained shifted-anchor
theorems and not Berry–Esseen.

The optional first-absolute-moment curvature lemma is valid. For the bend
`B_j`, put–call parity gives `B_j<=E(W_j)+`, while subadditivity gives
`E(W_j)+<=(n-j)e0+j e1`. After the exact adjacent-binomial identity,
extend the nonnegative sums over Bin(n+1,p): the variance sum is at most
`(n+1)s`, and the first-moment sum at most `(n+1)(qe0+pe1)`.
This gives the printed bound. It is not needed for the new n=200/700 result.

## Execution and limits

Source hashes and reproduction outputs are recorded by the final integration
manifest and receipts. Constructors supplied exact scalar checks and bounded
actual-law controls. The coordinator read those programs and the proofs;
the independent right reviewer supplies separately written swap and polynomial
checks. Reusing the older outward normal/occupancy helper is disclosed and is
not called independent arithmetic verification.

The coordinator added explicit assertion-enabled guards to the five-count and
join checkers' direct entry points. Historical successful runs already used ordinary
Python; no mathematical constant or target changed. A missing probability
macro backslash in the anchor note was also corrected, with a fresh build.

The accepted conclusion is a local signed comparison under the displayed
support, noise and raw-threshold assumptions. Acquiring those assumptions,
handling the oriented reflected witness, the finite base, and the remaining
small indices are not certified by these programs. The exact joins and
first-failure qualification are in `join-review.md`.

The final source pass also corrected two endpoint strictness displays in each
of the five-count and left notes: the sine-chord estimate is weak at zero,
and the final kernel comparison is weak at one. The target inequalities were
already weak and no theorem domain, coefficient or endpoint margin changed.
The final builds and source-bound reviews use the corrected files.
