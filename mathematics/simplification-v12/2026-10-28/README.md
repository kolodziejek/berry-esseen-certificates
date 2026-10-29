# Direct count comparison with joint moment costs

Start with [the two-page guide](comparison-union.pdf), whose exact statement
and proof of the joins are in [comparison-union.tex](comparison-union.tex).
The new route closes larger conditional noise ranges. It does not prove the
full sharp iid Berry–Esseen conjecture.

All comparisons below use one actual iid marginal, conditional centering,
n≥42 and the raw sum threshold |H|≤1.84. Write lambda=n E U². The support
convention is −A≤U0≤a0 and −a1≤U1≤A, with nonnegative inward caps.

| Comparison | p | A | a0+a1 at most | Positive lambda at most | C | Conclusion |
|---|---|---|---|---|---|---|
| New left theorem | [.25,.4] | .7 | .068 | .01 | [.4095,.41] | Delta_C<−lambda/100 |
| New right union | [.4,.53] | .6 | .072 | .075 | C≥.4 | Delta_C<0 |
| Retained v11 right theorem | [.4,.53] | .6 | .072 | .03 | C≥.4 | Delta_C<−lambda/100 |
| Retained v10 right theorem | [.4,.53] | .6 | .072 | .02 | Every C≥0 | Delta_C<−lambda/100 |
| Retained v11 all-panel theorem | [.25,.53] | .7 | .068 | .002 | 0≤C≤.41 | Delta_C<−lambda/100 |

The sharp Bernoulli coefficient C_E lies in [.4095,.41]. The new right
theorem has a weaker quantitative conclusion on a larger domain; it does
not weaken or replace either older theorem on its original domain.
Relative to the previous selected route, the left noise cap increases by
a factor of five and the right cap by a factor of 2.5.

## Why the argument is shorter

The own-count loss and the cubic marginal penalty involve the same two
conditional third moments. Estimating each separately pays for incompatible
worst cases. Combining their coefficients before taking support maxima gives
a useful reserve. On the left this is the explicit gain 7s/4 in the joint
lemma of [leftcount.tex](leftcount.tex), even though rho−rho_B can be negative.

On the right, the first incoming count retains the distinction between a
possible .6 jump and an inward jump of at most .072. Its centered quadratic
Poisson hinge is increasing in total variance and decreasing in the fraction
assigned to small jumps. This reduces the continuous comparison to a small
closed parameter cover. Because the jump sizes are 25 and 3 times a common
unit, the hinge expectation equals a full second moment minus a finite lower
complement. Its infinite upper tail is included exactly.

For the other incoming counts, Var(W_j)≤2.5lambda holds uniformly in j.
Using this bound gives a factorial continuation of the whole tail. No
truncated Poisson sum or sampled tail is accepted. The other right phases
reduce to two polynomials on one rectangle and five scalar endpoint checks.

## What becomes unnecessary, with exact scopes

| Earlier obligation | Replacement and reason | Dependencies retained |
|---|---|---|
| Additional half-amplitude confinement for the newly covered left domain | LEFT-01 accepts amplitude .7 directly; [leftcount.tex](leftcount.tex), main theorem and joint-reserve section | The acquired .7 strip, inward .068 and raw threshold; contact/heat/sharp-predecessor premises of that acquisition |
| Additional half-amplitude confinement for the newly covered right domain | [compound-proof.tex](compound-proof.tex), main theorem, together with [outer.tex](outer.tex), accepts the existing .6 strip | The .6 strip and inward/threshold hypotheses; all acquisition ancestors |
| Harmonic/fractional-part gain, marked crossings, count curvature and inherited full-count grid inside those domains | Exact conditioning plus joint moment prices and complete incoming bounds prove the required signed comparison without these inputs | External quadratic-hinge theorem, finite normalization, explicit new scalar/cell checks |
| A grid over sample size in the right negative-inner comparison | Separate concavity in eta=1/n covers [0,1/42], including every integer n≥42; [compound-proof.tex](compound-proof.tex), finite-check section | Correct physical count multipliers and all endpoint signs |
| Numerical truncation or generation of the first incoming compound tail | Finite complement identity, then rational exponential enclosures; [compound-proof.tex](compound-proof.tex), exact finite-expression section | Groupwise Poisson comparison and centered-hinge monotonicity |

These are dependency removals within the displayed domains. No old
certificate was deleted. The new 291-cell cover is explicitly retained;
the argument is not certificate-free. The two-page guide proves the joins
at lambda=.03, u=−.15, u=0 and the other phase endpoints. Distinct left and
right anchors at p=.4 are valid because the Bernoulli theorem applies at
every integer anchor. Zero noise is handled directly by the external strict
finite-n Bernoulli theorem. Reflection and attainment remain separate.

## Proofs and evidence

| Result | Mathematical status | Execution status |
|---|---|---|
| Left comparison through .01 | Complete scoped derivation; independently rederived joint prices, switches and infinite tails | 88 scalar gates; independent 40 positive Bernstein coefficients and six margins; constructor 36 marginals/72 strict events/144 coupled tests/5 full Delta events; independent 9 marginals/36 events |
| Right positive phases and negative outer phase through .075 | Complete scoped derivation, independent normalization and polynomial review | 56 gates, 144 coefficients; independent interpolation recovers all 144; 893 actual binomial-ratio controls; 11 exact full Delta events |
| Right negative-inner phase, .03≤lambda≤.075 | Complete scoped derivation; same-law support prices, physical transport and all-n concavity independently reviewed | 291 closed cells:200 quartic/91 Cantelli; 23 constructor gates; independent 21 gates and all 291 margins; minimum lower margin 256695813/10^12; 3 exact full Delta events |
| Compound cover and arithmetic semantics | Independent closed-cover proof by disjoint interiors and volume | Exact volume27/4000; 300 transform entries, 582 later-hinge domains, 91 Cantelli licenses; malformed/false/source-corrupted controls reject |
| Compound comparison primitives | External theorem plus explicit local derivations; two false shortcuts refuted | Independent transport/pgf/actual-law controls; 72 constructor evaluator cases and 11 malformed-input controls |
| Union and witness mapping | Exact identity U=(Z−m_B)/ell, s=theta/ell²; closed phase/noise joins | Source-bound independent union review and compiled two-page guide |
| Full conjecture, larger-noise comparison and BASE41 | Open | No full acceptance claimed |

The independent reconstruction of the 291 margins imports no constructor
code. It uses a probability-generating-function recurrence, a different
exponential enclosure, polynomial interpolation and analytic support-price
maxima. All 291 rounded lower margins agree with the constructor. The
separate coverage review does inspect and exercise constructor definitions
for mutation tests; it does not present that exercise as a second independent
implementation of the whole arithmetic.

Proof PDFs: [leftcount.pdf](leftcount.pdf), [outer.pdf](outer.pdf),
[compound proof](../../../runs/compound-v12-20261028/build01/texlive/compound-proof.pdf)
and [compound-review.pdf](compound-review.pdf). The component proofs are
7, 5, 7 and 5 pages respectively; these are not a claimed total-paper length.
The manuscript is unchanged in this research round.

Reviews: [left](left-independent-review.md), [outer](outer-review.md),
[compound primitives](compound-review.md), [compound coverage](compound-cover-review.md),
[compound composition](compound-composition-review.md), and
[union](union-review.md). Review roles are disclosed; the coordinator
constructed the outer component and independently reviewed the left and
compound arguments. The union reviewer constructed the negative-inner
component and separately checked the other-component joins.

## Refuted shortcuts

The old exploratory `counts-v11-compound-discovery.py:51–57` combined the
physical marginal allocation w with own-count variances (1−w)t and wt.
This is false away from k=np. An actual admissible four-point law violates
the intermediate bound by 423903/2500000000. The new proof retains
T0=lambda(1−w)(1−delta/(nq)) and T1=lambda*w(1+delta/(np)).

The centered two-jump hinge is not convex in its allocation, even at a
positive hinge anchor. [compound-review.tex](compound-review.tex) gives an
exact negative second derivative. Allocation monotonicity is valid and is
what the new proof uses. Neither defect affects the accepted v11 .002/.03
theorems or the correctly stated local variance-aware moment lemma.
The failed diagnostic sources and runs remain preserved.

## Reproduction and remaining work

From the checkout root, with assertions enabled:

```sh
python3 -I -B mathematics/simplification-v12/2026-10-28/run_checks.py NEWID
python3 -I -B mathematics/simplification-v12/2026-10-28/union-review-check.py .
```

The driver refuses an existing run directory, binds the reviewed sources,
and saves command, interpreter, stdout, stderr, return code and hashes for
14 bounded checks. The final integrated evidence is
`runs/simplification-v12-20261028/integration01/receipt.json`.
The separately integrated final union check is recorded in `union01/`:
28 exact refinement strata and 12 actual marginal mappings passed.
Discovery and inherited generation programs are not run by this driver.

At C_E, left p<.4 above lambda=.01 and right p≥.4 above lambda=.075
remain open up to the retained panel budgets. The global geometric bound
lambda<.616 does not close these gaps. The independent finite base through
41 and the 11,264-cell coarse Fourier entry remain obligations. There is
no new global propagation theorem, full Fourier replay or Lean build.

Work remains in the user's fork, on separate research branches and the
existing draft PR5. Baseline6346fc1b4432bc5982822aa696eb566ed9e1e1ee,
all original certificates and the manuscript are preserved. No main push,
merge, force-push, branch deletion or upstream change is part of this work.
