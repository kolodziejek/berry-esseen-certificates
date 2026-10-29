# Finite-base structural result, 28 October 2026

Baseline: `dde37e6f2fc8bfe654d6af8bf250756c6e2984d1`; branch `research/finite-v13-20261028`.
The task adds a proof and bounded controls. It does not modify the manuscript,
old certificates, reference material, or any remote branch.

| Result | Mathematical status | Execution status |
|---|---|---|
| A fixed-support moment-polytope extreme law need not maximize an actual iid four-sum CDF | Locally derived exact counterexample | Fresh PASS, `check03` |
| Correct replacement along a moment-null direction: check the full quartic, including cubic derivative roots | Proved finite signed-measure expansion with explicit moment hypotheses | Fresh exact coefficient/product controls |
| The same-law pair-CDF matrix must be negative semidefinite on moment-null directions at a local maximum | Necessary second-variation condition, not sufficient | Fresh rational Hessian identity control |
| A finite law satisfying the complete cubic contact inequality has at most two atoms outside active four-sum collisions | Locally proved, conditional on the stated full contact premise | Fresh exact collision controls; analytic premise is not certified by those controls |
| A unique active unordered four-sum multiset forces at most six support points | Corollary of the preceding conditional lemma | Fresh actual-law incidence controls |
| Universal six-atom reduction, complete C4, or a new finite base | Not established | Not run |

## Exact obstruction

On raw support `(-2,-1,0,1,2)`, use masses

`(1/20+theta, 1/5-2theta, 1/2, 1/5+2theta, 1/20-theta)`,
`-1/20 <= theta <= 1/20`.

The mass, mean, second moment and absolute third moment are fixed. The moment
matrix has rank four, so this is the entire moment polytope on the prescribed
support, and its only extreme laws are the two endpoints. Nevertheless, at
raw four-sum threshold 1,

`F(theta)=25719/32000 - 103 theta/2000 - 483 theta^2/200 - 123 theta^3/5 + 11 theta^4`.

`F(0)-F(-1/20)=51/160000>0` and
`F(0)-F(1/20)=1859/160000>0`.
The unique maximizer is `(190-sqrt(37233))/220`, strictly interior.
The standardized laws have `rho=3sqrt(5)/4<46/25`, support radius `sqrt(5)`,
`|E[X|X|]|<=1/4`, and raw standardized threshold `H=sqrt(5)/2`.
Thus this obstruction occurs within the bounded moment/threshold region
relevant to the current ROOT4 reduction. The signed third moment is not fixed.
This does not exclude a different law outside this prescribed support from
having a larger CDF, and it is not a counterexample to Berry--Esseen.

Proof: `finite-contact.tex:19`–90. The corrected quartic and same-law Hessian
conditions are at `finite-contact.tex:92`–144.

## What the contact lemma changes

For a finite support `S`, assume globally

`c|x|^3+a*x^2+b*x+d >= 8 P^{*3}((-infinity,H-x])`,

with `c>0` and equality on `S`. Any support point not in an active four-sum
collision lies in a neighborhood on which the right side is constant, and
therefore must be a local minimum of the same cubic potential. That potential
has at most two local minima; if both occur, their signs differ.

If only one unordered four-term multiset sums to `H`, at most its four distinct
points and two exceptional minima can be support atoms. Therefore a finite
fixed-target maximizer with at least seven atoms must have at least two active
occupancy vectors, hence a nonzero integer relation `sum v_j x_j=0` with
`sum v_j=0` and `sum |v_j|<=8`.

This offers a sound search organization: reject moment paths by their full
quartic/Hessian, and place larger finite candidates on explicit active
resonance strata. It does not justify discarding those strata or replacing an
infinite-support maximizer by a contact-preserving atomic approximation.
Proof: `finite-contact.tex:146`–232.

## Dependencies and potential computation removal

- The counterexample and quartic lemma need only finite-measure algebra. They
  do not use G2, G3, ROOT4, acquisition, Poisson comparisons or a certificate.
- The contact-to-collision implication uses precisely the global inequality
  and support equality stated above. Its application to a fixed-target
  maximizer retains the attainment/contact theorem in
  `manuscript/arxiv-v1/sections/02-fixed-target.tex:21`–89. Rearranging that
  theorem at n=4 gives the cubic potential printed in the new proof.
- No old finite-base computation becomes unnecessary from this result alone.
  In particular, neither `mathematics/fixed-target-v7/2026-10-27/base-audit.md`
  nor the physical bridge in
  `mathematics/fixed-target-v8/2026-10-28/root4-bridge.tex` is replaced. The new
  test can reject proposed candidate supports before dense computation, but
  it supplies no complete list of remaining supports or event chambers.
- The n=2 and n=3 certificate families were not replayed. Historical C4/C5
  headers are not treated as independent establishment of the finite base.

## Reproduction and limits

Run from the repository root:

```sh
python3 -I -B mathematics/simplification-v13/2026-10-28/finite-contact-run.py fresh-run-id
```

`runs/finite-v13-20261028/check03` records 374 exact checks, 164 collision
cases and 12 rejecting controls. Polynomial convolution is checked against
separate direct iid product enumeration; signed products reconstruct all
multilinear coefficients. Actual controls include symmetric/skew Bernoulli,
nearby three/four-point laws, a rare remote atom, endpoint zero masses, exact
threshold atoms and intervening thresholds. Negative controls reject endpoint
compression, convexity, omitted threshold atoms, missing combinatorial factors,
a falsely preserved signed third moment, omission of contact, one-minimum
compression, infeasible masses and malformed fixtures.

`check01` intentionally remains as the recorded failed development run: the
nearby-four-point test fixture had nonzero mean. The fixture was corrected;
no theorem target or assertion was weakened. `check02` passed before the final
text clarified signed-measure integrability and removed a duplicate equation
number. `check03` binds the final proof source.

The final four-page PDF compiled in `build02` without TeX warnings; all pages
were rendered and inspected. Source hashes, command, Python version and return
codes are in the run receipts. These finite controls substantiate the exact
identities and expose false shortcuts; they do not certify the analytic
contact premise, unrestricted optimizer structure, or a full C4 theorem.
