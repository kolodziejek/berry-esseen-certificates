# Independent review of the circle feedback component

No blocking mathematical or scope defect was found in the reviewed new
component. This is a review of `moment.tex`, `moment_check.py` and
`moment-report.md`, not a review of this branch's own signed K1 result.
The constructor's final source commit at review was
156a23c52f49822a813052a269f1792be014b532.

## Derivations checked independently

1. **Moment circle with zero atoms.** Signwise Cauchy gives
   a_±²<=m b_± and m²/a_±<=P(±X>0). The sign probabilities sum to at
   most one, so m²<=a_+a_-; multiplication gives b_+b_->=m² and hence
   gamma²+4m²<=rho². No zero atom is assigned to both sign classes.
   This agrees with Lemma `v6moment:circle`.

2. **Correct defect direction.** The conserved quantity remains
   D=(3+sqrt(10))rho−gamma−3J. The gap bound J<=rho+2m yields an
   inequality D>=sqrt(10)rho−gamma−6m, and the circle then gives
   D>=sqrt(10)rho−gamma−3sqrt(rho²−gamma²). Neither step is an
   alternative identity for D. The gap proof includes the possible
   central gap and uses AB<=1; the no-central-gap case is also covered.

3. **Inverse branch and its domain.** For y=gamma/rho, f(y)=y+3sqrt(1−y²)
   increases on [-1,1/sqrt(10)] to sqrt(10). If f(y)>=a, its smaller
   inverse root is a necessary lower bound even though f later decreases.
   The formula (a−3sqrt(10−a²))/10 has a−y>=0, including negative a,
   so squaring does not introduce a spurious lower branch. For a<=−1,
   retaining y>=−1 is valid. This verifies Lemma `v6moment:inverse`.

4. **Directions in the program.** `moment_check.py:20–32` rounds the square
   root upward, hence the inverse downward. Multiplying a negative lower
   bound for gamma/rho by rho requires u; a nonnegative bound requires l.
   The implementation uses those endpoints and rounds down again. The
   intersection with −g and sigma_lower*l−3−d remains a valid lower bound.
   The three upper bounds for rho−gamma at lines 38–40 all have the
   correct directions.

5. **No feedback circularity.** Lines 33–59 use the previous licensed raw T
   for the density lower bound and the previous defect for the moment
   restriction. They obtain a new raw upper bound before recomputing the
   phase price. The resource U never substitutes for raw T in the license.
   Upward rounding and minima of already valid upper bounds preserve the
   implication. The six-update loop retains every cell and rejects an
   inconsistent moment interval rather than dropping it.

6. **Signed curvature and coefficient endpoints.** The minimum of the two
   density endpoint products retains gamma's sign. Both alternatives in
   q(t) have slope l, so their maximum is still affine in t. The raw
   polynomial is affine in t before square completion; checking both
   c endpoints is consequently justified. The added phase price is a
   cell constant computed from the newly licensed raw upper bound.

## Fresh independent bounded check

`signed-moment-review-check.py` reads the pinned recorded output as data,
without importing the constructor, its inverse routine, or any Fourier
kernel. For each of all 144 recorded inverse lower bounds y_l, it checks
the rational certificate

```text
y_l is on the increasing branch,
a−y_l >=0,
(a−y_l)² >=9(1−y_l²).
```

These conditions prove f(y_l)<=a and hence that y_l is no larger than
the required increasing-branch inverse. The inactive a<=−1 branch is
checked separately. This is different from reevaluating the constructor's
square-root formula. The check also verifies exact closed-cell coverage,
all six update indices, normalization by the prior defect, and the sign-aware
rho endpoint. All 144 recorded normalized bounds are negative, so their
conversion correctly uses the upper rho endpoint.

The new run passed with Python 3.9.6 and return code 0. A wrong root branch
and upward rounding at the exact valid boundary y=−5/13, a=31/13 are rejected.
Evidence is in `runs/fixed-target-v6-20261027/signed-moment-review01/`.
Its receipt identifies the command and input/output hashes; the constructor
source hash is `c44f789c35198eabb2d6d07a3843437c4fa29e9b85ebf79505a3bb696987513f`.

## Acceptance scope

| Item | Mathematical status | Execution status in this review |
| --- | --- | --- |
| Circle, defect inversion and rounding directions | Independently rederived; no blocker found | All 144 recorded inverse certificates freshly checked |
| Ordered scalar update and endpoint logic | Independently read and checked, conditional on the original raw envelope | No full update/kernel rerun |
| Retained contact, actual support, complete Fourier primitives | Explicit premises of the component | Not independently accepted by this review |
| Claimed six-update numerical summary | Correctly delimited as conditional; 20 cells satisfy the sufficient D<4 gate | Constructor's recorded run inspected, not repeated |
| Complete initial acquisition or certificate removal | Not claimed and not established | No acceptance run |

The report correctly distinguishes failure of a sufficient gate from an
actual law violating the intended conclusion. Its four remaining high-moment
cells, stronger final resources and complete probability-panel obligations
remain explicit. The component is suitable for integration as a conditional
scalar improvement, without promoting it to a complete initial acquisition.
