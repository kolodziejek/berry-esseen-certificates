# Own-count progress with the conditional variance allocation retained

The separate bounds for the fourth and third moments conceal a useful
dependence: negative conditional noise improves the own-count lower bound
precisely where it worsens the incoming lower tail. A short moment inequality
preserves this dependence for any quartic indicator minorant.

Worktree: `owncount-v11`; branch: `research/owncount-v11-20261028`.
Reference commit: `6027b27f85473780eaf90542f490168873de5986` in the user's
fork. All new files are under this directory and
`runs/owncount-v11-20261028/`. No old source, certificate or manuscript is
changed; no push or remote mutation was performed.

## Exact result

For independent centered conditional noises on `[-A,a0]` and `[-a1,A]`,
write T0,T1 for their variance totals in the actual own count, and t=T0+T1.
Then, for every real kappa,

`E W^4-kappa E W^3 <= c0 T0+c1 T1+3t^2`,

where

`c0=max(A^2+kappa*A,a0^2-kappa*a0)` and
`c1=max(A^2-kappa*A,a1^2+kappa*a1)`.

The proof is the endpoint maximum of the convex quadratic
`x^2-kappa*x`, multiplied by x^2 and integrated. Independence supplies
the fourth-moment cross terms. For nondegenerate supports the linear
per-summand coefficients are asymptotically sharp; this does not claim
that an arbitrary relaxed moment optimizer is an actual convolution.

For the v10 quartic and negative phase u=-r, the new estimate improves the
old own-count lower bound by exactly `8*A*r*T0/(5*alpha^4)` whenever
`r<=(A-d)/4`. With A=.6 and d=.072, this includes r<=.132. At
`r=t=.075`, alpha=.5 and T1=0, the bound after adding f(-r) is
**.06934875**, whereas the old bound was **-.01705125**. These parameters
are realized by n=42, p=.5, U1=0 and centered U0 on `{-.6,1/168}`.
The improvement is not a sampled claim about an unrealizable moment tuple.

The same proof applies to the more general quartic being investigated by
the coordinator. The note also combines the exact marginal third-moment
repair with the own-count third moments before optimizing either one.
This gives two modified coefficients, preserving their common origin.

## How this can enter a shorter argument

At fixed n,p,k,lambda and fixed support caps, parameterize the conditional
variance allocation by `eta=p Var(U1)/s`. The quartic bound above is concave
in eta. A fixed Chernoff tilt applied separately to the two conditional
groups produces an incoming bound that is a sum of exponentials of affine
functions of eta, hence convex. The difference is therefore concave and
its minimum is attained at an allocation endpoint.

This reduces that allocation coordinate to two endpoint inequalities.
The endpoint inequalities still have to be proved uniformly in the other
parameters. The note does not report that they pass. In particular,
pointwise optimization of the incoming tilt does not automatically preserve
the required convexity. The same warning applies to retaining a favorable
finite-sum variance correction in the own-count estimate.

The normal slope estimate also extends cleanly: for p in [.4,.53],
n>=42, lambda<=.075 and |H|<=1.84, the bound `.95<f'<1.05` holds
throughout the phase range |u|<=.1. It follows from the existing finite
Stirling estimate with D=21/20, rather than from a new numerical grid.
The retained source locations are
`mathematics/simplification-v10/2026-10-28/moderate-noise.tex:78` for
the entropy/prefactor constants, `:85` for the finite mass remainder and
`:98` for the fixed-count logarithmic derivative. The finite factorial
remainder is proved at
`manuscript/arxiv-v1/appendices/count-comparison.tex:131`.
The new checker verifies that the entire near-phase count segment stays
inside the interval on which those constants were established.

## Mathematical and execution status

| Result | Mathematical status | Execution status |
|---|---|---|
| Conditional fourth/third-moment coupling | Complete local analytic derivation | Exact actual-law moment checks |
| Own count for a general quartic | Complete pointwise/minorant deduction, strict event convention retained | 360 exact own-event checks on 36 actual marginals |
| Marginal cubic repair coupled to own count | Complete algebraic derivation from one actual marginal | 360 rational weighted checks |
| Allocation endpoint reduction with fixed split Chernoff bound | Complete analytic concavity argument | Explicit counterexamples to two invalid convexity shortcuts |
| Normal slopes through phase .1 and noise .075 | Uses the retained v10 finite Stirling proof on a verified domain | Fresh exact positive margins |
| Optional fixed-variance Hermite majorant | Complete local proof under its explicit sign condition | Exact polynomial reconstruction and moment checks |
| Full comparison for .02<lambda<=.075 | Not established by this component | No complete interval acceptance or generation campaign |

The actual-law controls use n=42 or 43, p=.4, .5 or .53, lambda=.05
or .075, and conditional variance allocation 0, 1/2 or 1. Their inward
endpoints are chosen from the exact variances and stay inside the stated
budget. Two quartic minorants and five negative phases are tested per law.
The full convolutions and their moments are rational, including atoms.

The negative controls demonstrate that assigning the favorable negative-noise
coefficient to positive noise is false, that the finite-sum correction can
destroy allocation concavity, and that a minimum of convex incoming bounds
need not be convex. These are defects of proposed intermediate shortcuts,
not counterexamples to the Berry--Esseen conjecture.
Separate actual-law counterexamples also reject dropping the amplitude
hypothesis or the sign condition in the optional Hermite majorant.

Proof: [owncount.tex](owncount.tex); checker: [owncount_check.py](owncount_check.py).
Fresh arithmetic and build receipts are recorded under the named run directory.
The proof PDF is a research note, not a manuscript revision.
