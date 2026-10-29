# Structural count research, v13

Worktree: `counts-v13`; branch: `research/counts-v13-20261028`.
Starting commit preserved: `dde37e6f2fc8bfe654d6af8bf250756c6e2984d1`.
All changes are new research/evidence files. No manuscript, existing
certificate or baseline source was edited; nothing was pushed.

## Results

| Result | Mathematical status | Execution status |
|---|---|---|
| Interval concentration bounded by a consecutive block of binomial masses | Proved for every n, actual conditional laws, positive conditional separation | 96 exact concentration controls PASS |
| Symmetric p=.5, positive even n, central threshold interval comparison | Proved for every noise level and every C>0, with finite third moments and nonzero conditional variance | 3 exact symmetric central controls PASS |
| Signed binomial curvature upper bound | Proved for every n>=2, every p in(0,1), every real threshold, finite second moments | 160 exact checks on32 actual-law cases PASS |
| Positive selected stop-loss reserve from four own-count moments | Refuted as a moment-relaxation assertion | Exact value−5/144, with all stated moment bounds checked |
| Independent-delay renewal after a comonotone coupling | The claimed independence is false | Actual admissible conditional pair has covariance−216/15625 at lambda=.6048 |
| Coordinator's general unweighted crossing theorem and weighted identity | Independently audited; no blocker found | 24 full-product-space controls PASS,9 nonzero selected-noise biases |
| Full right comparison above lambda=.075 through acquired .616 | Not completed | No new full-domain certificate generated or accepted |

## What is new

For any closed interval of length less than m(1−a0−a1), the ordered
conditional mesh contains at most m consecutive count indices. Thus the
actual iid probability is at most the maximal m-consecutive-binomial mass.
The strict interval-length condition is necessary; an exact noiseless
boundary control demonstrates its failure when replaced by equality.

For p=.5, U1 distributed as−U0, U0<=a<.5, positive even n, and s>0,
the direct comparison at k=n/2 is strict for every C>0 and
0<=H<(1−2a)/(2sqrt(.25+s)). There is no lambda ceiling. The proof uses
only the concentration statement, symmetry and the strict inequality
rho>1. This is a complete special-case theorem, not general larger-noise
coverage.

For the curvature correction C(t)=sum_j(pi_(j+1)−pi_j)B_j(t),
B_j=E(t−T_j)_+−(t−j)_+, the exact analytic bound is

`C(t) <= s/(4pq) + (np−q−t)_+ sqrt(s)/(2pq sqrt(n+1))`.

It follows from the Bin(n+1,p) adjacent-mass identity, two elementary
stop-loss bounds and a weighted variance expectation. No count truncation
or parameter grid occurs. Below t=np−q its square-root term prevents an
automatic uniform bound proportional to arbitrarily small noise.

## Sources and dependency edges

`counts-tools.tex` gives complete proofs of the new structural results and
both obstructions. `counts-check.py` supplies exact arithmetic controls.
The coordinator's `crossing.tex` supplies the nonnegative local kernel,
exact unweighted loss and weighted summation-by-parts decomposition;
`counts-crossing-review.md` independently audits those arguments and pins
the final source. Its control program imports no constructor implementation.

New DAG: conditional separation -> ordered mesh -> interval concentration;
add symmetry, positive even n and s>0 -> strict central comparison.
Centered finite-variance conditional sums -> stop-loss bends and exact
binomial difference -> uniform curvature upper bound.
The full larger-noise route still needs the common weighted crossing loss
to absorb this curvature plus phase, normal and cubic repairs.

The new tools do not remove the accepted v12 component, the coarse Fourier
entry, attainment/contact/reflection hypotheses or the finite-base obligation.

## Bounded exploration and preserved failures

`counts-crossing-discovery.py` tested115 actual n42,p=.5 conditional
three/four-point laws at .075<lambda<=.616. Atom locations were exact;
probability sums were floating diagnostics. Among43,487 atom thresholds
near the mean, no positive E K−t appeared. The weakest observed loss was
about .0791503 at lambda=.0756. This is discovery only, preserved in
`runs/counts-v13-20261028/discovery01/`; it does not prove uniform positivity.
No further grid enlargement or expensive certificate campaign was run.

The moment obstruction has masses25/144,47/72,25/144 at−6/5,0,6/5.
It has variance1/2, zero third moment and fourth moment18/25<=93/100,
but P(Z>0)−E Z_+=−5/144. It is not claimed to be an iid convolution.
It blocks a specific proof relaxation, not the sharp conjecture.

## Reproduce and continue

```
python3 -I -B mathematics/simplification-v13/2026-10-28/counts-check.py
python3 -I -B mathematics/simplification-v13/2026-10-28/counts-crossing-review-check.py COORDINATOR_REPO_ROOT
```

Fresh evidence is under `runs/counts-v13-20261028/exact01/` and
`crossing-review01/`. The final four-page proof is compiled and rendered
under `build03/`; earlier builds are preserved.

The next useful claim is a quantitative **weighted** crossing-loss bound
for the same conditional laws, preferably combined with the signed curvature
and cubic repair before taking extrema. Positivity of the unweighted loss
alone, or positivity on the discovered atoms, is insufficient. Retaining
neighboring local kernels is a better direction than a single four-moment
selected-term bound, which has the explicit obstruction above.
