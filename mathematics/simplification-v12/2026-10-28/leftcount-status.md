# LEFT-01: a joint count–moment estimate on the left range

Reference baseline: `a69dda8`. Component branch:
`research/leftcount-v12-20261028`. No inherited proof, certificate,
manuscript, or upstream file was edited.

| Result | Mathematical status | Execution status |
|---|---|---|
| LEFT-01, `leftcount.tex:23` | Locally derived and checked; external finite Stirling and Pinelis inputs retained; independent root review in progress at this checkpoint | 88 exact scalar gates, eight negative controls: fresh PASS |
| Joint own-count/marginal-cubic reserve, `leftcount.tex:208` | Locally derived from the same two conditional marginals; positive reserve is `7s/4`, where `s=lambda/n` | 36 actual marginals, 72 exact strict events, 144 endpoint-C comparisons: fresh PASS |
| Five full `Delta_CE` actual events | Selected adversarial controls, not a uniform proof | Fresh PASS with the expressly reused, source-pinned rational-normal kernel |
| Seven-page proof rendering | Expository check only | Final compile and visual inspection: PASS; no overfull, underfull, or warning lines |

## Exact statement and improvement

For integer `n >= 42`, `p in [1/4,2/5]`, `q=1-p`, actual conditional
centered laws `U0 in [-.7,a0]`, `U1 in [-a1,.7]`, and
`a0+a1 <= .068`, put `s=E U^2`, `lambda=ns`, `v=pq`,
`ell=(v+s)^(-1/2)`, `X=ell(B+U-p)`. If `0<lambda<=.01` and
the raw threshold satisfies `|H|<=1.84`, choose the actual integer
anchor by `np+H/ell=k+u`, `u in [-.218,.782]`.
Theorem LEFT-01 proves

`Delta_C < -lambda/100`

for every `819/2000 <= C <= .41`, including the Esseen target `CE`.
`Delta_C` is the exact difference between the signed normalized excess
of this actual iid law and its binomial anchor, including both normal
variance and third-absolute-moment corrections. The theorem has no
contact or predecessor premise. Its acquisition from an extremal
witness does have those premises.

This extends the completed all-panel `.002` comparison fivefold in
noise on the entire left interval. It does not use a Schulz reserve,
extrapolate one below `p=1/3`, subdivide `p`, or optimize a relaxation.
The two target domains must remain distinct: the older `.002` theorem
allows `0<=C<=.41`; LEFT-01 requires the displayed positive lower bound.

## Why the new estimate helps

The conditional raw third moments occur both in the quartic own-count
minorant and in the marginal third absolute moment. Pricing them together
uses the actual physical count multipliers `n-k` and `k`. On the guarded
outer support endpoints, their combined estimate is the old absolute-cubic
quartic lower bound plus

`C ell^3 s [A+3 min(p,q)-(3/2)(1-2pq)-3(1-2pq)s/(8pq)] > (7/4)s`.

The guard follows uniformly from `r<=.05`, `m=sqrt(n)pi_k>.72`,
`ell^3<12.5`, and `p/k,q/(n-k)<1/38`. The inward caps are used in
this guard and in fixing the signs; they were not erased.
This lowers the effective inner normal repair to `(3/4)s` in the
difficult interval `-3t/2<=u<=0`, with `t=Var W_k`.
Elsewhere the adverse third-moment repair is retained.

Four broad closed phase intervals, with an actual-variance switch inside
the central one, suffice. Negative-inner quartic monotonicity/concavity
reduces its rectangle to two corners; the positive rectangle reduces to
one corner. Incoming counts retain Pinelis quadratic hinges and an
infinite Poisson factorial tail. No tail is numerically truncated.

## Dependency edges and scoped computational removal

* Actual iid decomposition and inward caps -> LEFT-01: no relaxation law
  may replace the common conditional marginals.
* Finite Stirling -> normalization (`leftcount.tex:93`), with new exact
  left-range error bounds. The finite factorial argument remains in
  `manuscript/arxiv-v1/appendices/count-comparison.tex:131`.
* Published Pinelis quadratic-hinge comparison -> incoming bounds
  (`leftcount.tex:318`); the geometric series proof is supplied explicitly.
* Direct geometry `mathematics/simplification-v10/2026-10-28/geometry.tex:102`
  and retained raw-threshold acquisition -> `p>.25`, `d<.068`, `|H|<1.84`
  for the acquired witness. Their original hypotheses remain ancestors.
* v11 left heat/ray strips
  `mathematics/simplification-v11/2026-10-28/leftpanels.tex:113` ->
  `U0>-.6`, `U1<.7`. These imply the wider `.7` amplitude used here.
  Fixed-target contact, nonnegative excess and sharp predecessor remain
  strip prerequisites. The closed endpoint `p=.4` joins the right domain.
* LEFT-01 + strict Bernoulli theorem at `CE` -> signed exclusion in this
  exact acquired domain. Reflected acquisition must be checked separately
  before asserting the corresponding reflected result.

Within `p in [.25,.4]`, `0<lambda<=.01`, and these actual support/threshold
hypotheses, the count exclusion can now be established with this short
scalar package instead of a separate high-dimensional count certificate.
The newly covered part is `.002<lambda<=.01`; no old proof component has
been removed or rerun. This does not remove acquisition, raw threshold,
support strips, reflection handling, the sharp predecessor, the finite
base through 41, or any larger-noise exclusion. It does not prove the full
conjecture or a global propagation theorem.

## Reproduction and evidence

Run from the repository root with assertions enabled:

```sh
python3 mathematics/simplification-v12/2026-10-28/leftcount-check.py
python3 mathematics/simplification-v12/2026-10-28/leftcount-actual.py
```

Final scalar evidence is `runs/leftcount-v12-20261028/scalar02/`;
actual-law evidence is `runs/leftcount-v12-20261028/actual01/`.
Receipts contain commands, Python version, return codes, elapsed time and
input/output hashes. Scalar01 was an earlier arithmetic check before the
proof existed; scalar02 binds the final proof bytes.

Actual laws cover `p=1/4,13/50,1/3,2/5`, allocations `0,1/2,1`,
and `lambda=10^-10,.002,.01` at `n=42`. Two strict own events per
law include nine nonzero threshold-atom cases. The conditional convolution
and coupled comparison are implemented afresh. The five full comparison
events reuse `actual_law_checks.py`, hash
`351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07`,
for rational square roots, normal enclosures and full event arithmetic;
this reuse is not called independent verification. No floating maximizer
search is used by the new script.

Negative controls explicitly reject deleting the adverse cubic correction,
using an outer endpoint without its guard, using the second hinge beyond
its positive denominator domain, and attempting the `.01` proof without
its joint reserve. They reject missing, duplicated, reordered and gapped
phase covers. An actual law also rejects replacing the proved `7s/4`
reserve by `7lambda/4` (tested at the admissible target `C=.41`).

Build01 compiled but had three overfull boxes; the final source differs
only by display line breaks. Build02 is clean, and all seven rendered
pages were visually inspected. See its `receipt.json`, `inspection.json`,
compiler output and log. The deliverable PDF is `leftcount.pdf`.

Final mathematical source hashes:

* `leftcount.tex`: `f038aa62e039bfe48482fe69c1438553e90f7c246bf0fa74322115c33ea76ea9`
* `leftcount-check.py`: `2e5190c9b035e54cd9e89a164fc335dc7cc7a535cc77d4931d616f397f0cb6d6`
* `leftcount-actual.py`: `0fcb3178b445f692d2a4d44877133d6acf5c4a81180f7681a54b151ed4ee039c`

Hashes identify the inspected bytes; they are not proofs of correctness.
