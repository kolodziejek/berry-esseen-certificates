# Resume the count-method simplification

This folder is additive to draft PR13 and the six-page common-law proof in
`../six-count-row-20261105/`. Original manuscript and certificate archives are
unchanged. Journal-v21 remains 86 pages; no 60-page or submission-ready claim
is made.

## Exact completed inputs

The two packages fix these original contracts:

- B0/p50: p in [1/2,51/100], original noise [0,32813/125000], roots k2,k3.
  Contract SHA256
  `2939dcca05896e1c6393c50944df8dd5e872efb26076a7304df45d9f6d07a93f`.
  Complete result SHA256
  `722ecb69e3bcac17206cc2035cd3f86802935bdd0cf9bb2d19eb590358099b9a`.
- B2 S3/p34: p in [17/50,7/20], original noise [0,206391/1000000], roots
  k1,k2,k3. Contract SHA256
  `a9e2574fbb79e8d21d7bf6d5a9bc152ba6981878101c0dafd3eb7088233ba6d5`.
  Complete result SHA256
  `dd6fde86aaad2ff58d7fdd89c039bf3cd3e31194622a4c802b2d83bb51b6b82d`.
- BN/p39: p in [39/100,2/5], original noise [0,12941/40000], roots k1,k2,k3.
  Contract SHA256
  `8d2a6ec51bf43b45a7ce2de62d5ed734a90498924cb60c833a3976394eef3d9a`.
  Complete mixed result SHA256
  `8f8752d58b5b630d0090980667465c7665122d6a5ffd458be252412b3946ee96`.
  Fresh replay: actual return code0, 417.842seconds, 1,126leaves, 13,512rays,
  2,116,800coefficients. Of the leaves, 1,115 retain the baseline rule and11
  use the explicitly tagged Taylor target. Original partial objects persist.

All three keep the original rho/beta/support/mean/sign/threshold premises, one
common iid marginal, original C_E and K=0. The noise bound from the mean is
intersected with the original domain; this is a licensed consequence, not an
unannounced replacement of the original input. m denotes E X_+, not E|X|.
External selectors reconstruct all original roots and cover the closed
threshold range, including atoms. Full phase enlargements are identified.

The sharp39 input has a different original contract schema. It is the sharp
K=0 branch, not positive39 with a positive allowance. Its resource intercept
Lambda is not an independent noise cap to be substituted in the acquisition
budget. Preserve the joint constraints when constructing the variance polygon.

## Mathematical rules to preserve

1. Write Y=B+U with p=P(B=1), q=1-p. Use the same conditional laws U0,U1 in
   every binomial count. Put x=q E U0², y=p E U1², w=pq+x+y, lambda=n(x+y).
2. Use n+1 different quartics, each globally above the closed-event step
   function. The mixed fourth-moment coefficient is 3(1-1/n); its justification
   uses common-marginal moments and a finite Cauchy inequality. The nine
   common skew/inward corners are a bound on the full expression, not nine
   independently realizable distributions.
3. Constant affine prices for the actual absolute cubic moment preserve
   variance convexity. A tangent price c R(5W-3w) is more accurate, but its
   quadratic term need not be concave; check the complete Hessian as proved in
   the four-page note. Never omit that PSD obligation.
4. A quadratic lower polynomial for Phi is evaluated only at fixed variance
   vertices after convexity of the loss with the actual Phi has been proved.
   Its own variance curvature is irrelevant. Rational gradient intervals and
   a uniform Hessian bound prove the entire rectangle; grids are controls.
5. For two probability halves use both endpoints of p(1-p), including 1/4
   when the cell crosses 1/2. Do not reflect a source contract without proving
   the effect on every acquired signed bound and open/closed event convention.
6. The cleared score degree is (max(n+4,10),4) when using the tangent price.
   With the original affine price n5 retains degree(9,4), including the new
   quadratic Gaussian target. Empty or degenerate polygons reject unless a
   separate valid exclusion or lower-dimensional rule is proved.

## Next research and manuscript decisions

The complete mixed BN39 replay and portable package are finished. Do not rerun
them merely to reproduce a success marker.

The next two planned steps from the earlier handoff are now completed in the
additive package `n5-all-taylor/`:

1. **All-Taylor Curvature-Corrected $n=5$ Reconstruction (`n5-all-taylor/`):**
   - `code/gaussian_scalar.py` generalizes `gaussian(n, k, pl, pu, ul, uh, lam)`
     to both probability halves ($0 < p_l < p_u < 1$) using the endpoint variance
     minimum $v_{\min} = \min(p_l(1-p_l), p_u(1-p_u))$, and adds
     `curvature(n, k, pl, pu, ul, uh, lo=0)` certifying
     $g''(\lambda) \le M = \frac{3\max(a_{\max},0)\Phi_{\mathrm{HI}}}{4 d_{\min}^2 s_{\min}}$
     under $\min(a_{\min}, 0)^2 \le 3 d_{\min}$.
   - `code/model_all_taylor.py` enforces $v^2(H_F(p) - 25 M J) \succeq 0$ via
     degree-7/14 univariate Bernstein certificates on every leaf, evaluates the
     both-half quadratic Gaussian Taylor polynomial directly at each polygon
     vertex's exact noise $\lambda = 5(x+y)$, and supports optional verified
     non-negative dual raw-moment prices $(a,b,c,d) \ge 0$.
   - On `BN39`, the all-Taylor reconstruction closes the entire original row
     (`k=1,2,3`) in **18 leaves** (`5+12+1`), compared with **1,126** mixed
     leaves in `n5-bn39/` and **809** old `COUNT` leaves.
   - Across **7 complete original $n=5$ rows** (`BN39`, `B0_50`, `B2_S3_34`,
     `BN38`, `B0_53`, `B3_S0_59`, `B3_S2_59`, 19 roots), the all-Taylor reader
     verifies **63 total leaves** (756 global rays, 1,953 PSD coefficients,
     121,500 score tensor coefficients) in 28.73 seconds (replay result SHA256
     `44abeb2d78e588d2dd308c3d255aa2448ff52eda18bbc5b93213c283ac3afc85` in
     `n5-all-taylor/evidence/replay01/accepted/RESULT.json`, independently
     audited in `review/runs/count_transfer_20261105/review_all_taylor01/checked/RESULT.json`,
     SHA256 `de48c0eac95091a7f8fa5f165c5a3518a823ff212e98d46bd7076df81d76202d`),
     compared with **2,736** old `COUNT` leaves (a **43.4x** reduction) and
     **49** leaves vs. **2,296** baseline/mixed six-count leaves across
     `BN39`, `B0_50`, `B2_S3_34`, `BN38` (a **46.9x** reduction).
2. **General External Contract Selector (`n5-all-taylor/code/selector.py`, `contracts/CENSUS_295.json`):**
   - Inventories all 295 original $n=5$ contracts across `B0` (29), `BN` (30),
     `B2` (92 across `S0..S3`), and `B3` (144 across `S0..S3`), handling
     $p \ge 1/2$, $\rho$ floor $1$, and the fourth active root $k=4$ (verified
     on `B0_53`, `B3_S0_59`, `B3_S2_59`).
   - Conservatively derives the complete active nearest-count root catalogue from
     each raw contract and rejects all 68 ambiguous `(band, index)` pairs when
     queried without a disambiguating `slab_family`, `rho`, `beta`, `path`, or
     `sha256` (43 exact negative and corruption controls in
     `n5-all-taylor/evidence/controls01/`).
3. **Remaining $n=5$ Wide-Polygon High-$\rho$ Observation:**
   - While `B3_S0_59` (4 leaves) and `B3_S2_59` (5 leaves) close immediately,
     the widest-$\beta$ high-$\rho$ panels near $p=1/2$ (`B3_S0/panel050`,
     `BN/panel050`) contain both $(0, y_{\max})$ (where $G(0, y_{\max}, g_1=0) > G_{\mathrm{hi}}$)
     and $(x_{\max}, 0)$ (where $G(x_{\max}, 0, g_0=0) < G_{\mathrm{lo}}$) in
     their $\beta$-mean polygon. Because cell-wide scalar dual prices $(c, d) \ge 0$
     are affine in $G$ and `DUAL_PRICE_LICENSE.md` forbids corner-dependent
     prices without a new proof, closing those panels before running all 295
     rows requires either a licensed vertex-level signed-moment restriction or
     inward-corner coupling on the mean-noise polygon.

Later-index replacement needs continuous p/phase coverage, every licensed
nearest-count root and every original resource domain. The n6 fixed-location
test and sharp39 rectangles prove transfer is possible, not full coverage.
A curvature bound on the actual Gaussian now removes the negative-numerator
restriction on the tested full-p/narrow-phase sharp39 rectangle. For
g(lambda)=Phi(a/sqrt(D)), certify g''<=M and require
H_price-n² M J positive semidefinite, where J is the two-by-two all-ones
matrix. Every successful implementation still needs an exact whole-cell
bound, source guards, PSD polynomials and the final score tensor. A PSD PASS
alone is not a completed comparison. The one-cell test failed the score gate;
two fixed closed cells, [.38,.385] and [.385,.39], passed with the same40
quartics, u in [-.01,.01], k15 and full noise[0,.185]. Result SHA256
`e6495b16fc3f7fadc236951f94e05142219d1e778f9aacdeafd7d125d8d8f8d4`.
This is the whole original p interval, not the whole original phase/count row.
Its public replay and proved correction are in later-curvature/.

Only integrate after a complete family of comparisons and their source-domain
joins pass. Section6.5 still serves n6--39; Section6.6's signed corner, Fourier
regions and Section7.2 acquisition have separate obligations. The best eventual
presentation is one common probabilistic reduction, a small menu of justified
scalar/curvature rules, and a finite list of explicit computational propositions.
It should not reproduce every search cell, nor hide why their verification
proves the propositions. If the remaining acquisition proof prevents60pages,
seek a replacement of that argument rather than cutting its logical steps.

## Local working and evidence paths

Workspace root: `/Users/bkolodziejek/Downloads/BE_Codex_Handoff`.
Constructor: `work/count_transfer_20261105/construct/`.
Later-index sources: `work/count_transfer_20261105/later/`.
Independent review: `work/count_transfer_20261105/review/`.
Actual fresh captures: `runs/count_transfer_20261105/`.
The packages contain portable acceptance closures; review snapshots and old
discovery captures retain original path provenance and are not advertised as
standalone relocated acquisition or review campaigns.

Do not rewrite earlier portable packages, failed objects or frozen receipts.
Use new epochs, ordinary unoptimized Python and fresh output directories.
Preserve mathematical and execution status separately, and update the PR and
state files with actual results before ending the next session.
