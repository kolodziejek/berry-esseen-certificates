# Coordinator review of the direct comparison

This records the coordinator's analytic review of the selected replacement,
separately from its arithmetic acceptance. The central finite replay was still
running when this note was written. No full-campaign PASS is inferred here.

The reviewed mathematical text is `direct_comparison.tex`, SHA256
`1f55bd1506f03606e1801c19e5013324cb4dc149c43da0dbcbd4b42b532bb719`,
with the later editorial and composition transformations in
`root/prepare_release.py`. The earlier composition review is in
`work/earlier_local_comparison_20261104/integration/review_composition/`.

## Independent checks of the analytic implication

I read the complete replacement, its original left proof, the central tail
derivation, the earlier fixed-target interface, and the corresponding exact
moment and global-polynomial checking routines. The following are mathematical
checks, not conclusions drawn from execution status strings.

1. For a fixed target T, subtracting the two score definitions gives
   `rho(T-C)=rhoB(T-CB)+normal_correction-sqrt(n)*Q+T(rho-rhoB)`.
   The coefficient of the moment difference is T. In particular, the
   positive39 target includes 19/4000 in both places. When the cubic lower
   bound is negative, the positive multiplier's two endpoints are required;
   no premise `rho>=rhoB` is used.
2. Coupling the actual conditional laws makes successive count sums increase
   by at least `1-a0-a1`. Loss of the nearest count is exactly the strict
   event `Wk>u`; incoming count r requires `Wk<=u-r*c`. The resulting floor
   payoff therefore includes threshold collisions with the right convention.
   It uses the same two conditional laws for every count.
3. The fourth-moment support inequality follows by integrating
   `(U0+A0)(a0-U0)U0^2>=0` and its reflected counterpart. Independence gives
   the exact fourth moment of the conditional sum. Dropping its negative
   variance-square correction is valid with a nonnegative quartic leading
   coefficient. The score bound is concave in variance allocation, affine
   in the surviving third-moment ratio, and concave in its inward endpoint.
   The six extremal evaluations are bounds for this expression; they are not
   claimed fourth-moment inequalities for arbitrary actual moment tuples.
4. For each fixed positive multiplier endpoint, the remaining noise-quadratic
   coefficient is nonpositive. Mass enters affinely. This gives 48 tests,
   or 24 after separately proving the cubic bracket nonnegative. Translation
   by phase preserves the leading coefficient. Clearing positive denominators
   and tensor Bernstein positivity then proves the whole closed p/phase cell.
5. Centering gives `s<=max(q*A0,p*A1)*(a0+a1)`. Applying this together with
   the binary, inward and noise terms of the same defect budget gives the
   strengthened noise ceiling. Each update preserves a proved ceiling;
   sixteen updates require no limiting or convergence assertion. At a zero
   binary floor, strict resource exclusion cannot be inferred from equality
   of two zero bounds. The selected readers retain this guard.
6. The finite proof can pay for strict positive polynomial padding from a
   finite binary reserve. The uniform central tail cannot use that device
   at arbitrarily small noise. Its explicit matched-slope quartic, exact
   factorization, finite-index normalization and four scalar polynomials
   instead give a loss proportional to every positive noise value.
7. At noise zero the finite score formula evaluates the literal actual
   threshold: for negative phase the CDF differs from the value at the
   nearest integer. The polynomial evaluation handles this directly. The
   uniform proof uses the strict Bernoulli theorem at the actual threshold.
   Neither argument divides by vanishing noise.

## Acquisition and assembly

The new comparison consumes the early 45 central rows with their contact
strip and the 39 left rows with radius 3. The later left radius 2.7,
Sperner feedback and local confinement sequence are not needed. Their removal
does not remove the initial contact, complete probability initialization,
moment/resource acquisition or Fourier estimates. Historical files can remain
hashed for source integrity without becoming mathematical premises.

The finite induction retains its original proof through 38, obtains the
positive39 cap using the new 78 comparisons, and then applies the original
sharp39 proof. The 291 actual40--42 comparisons use their actual binomial
indices with the floor40 weighted resource. The remaining 368 earlier pairs
give the separate finite43--46 exclusion. The global composition can therefore
use finite43--46 and uniform n>=47 directly. Equality is excluded only after
the weak bound at every index has been proved.

These conclusions are a bounded review of the replacement and its interfaces.
They are not a new replay of the inherited acquisition campaign, an independent
implementation of all arithmetic, a proof-assistant formalization, or external
human/referee acceptance of the complete manuscript.

## Optional next method

I separately read the exact n5 coarse-spacing obstruction and the six-count
quartic proofs in `work/count_quartic_shortening_20261104/audit/`. The identity
`beta=[pq(q-p)-x+y]/[pq+x+y]`, with `x=q*s0,y=p*s1`, gives the stated halfplanes.
After the common skew/inward extrema, the Cauchy upper bound
`3(1-1/n)*t_j^2` leaves a convex quadratic on that fixed polygon. Maximization
at its vertices is justified. This optional fixed-p/phase result does not
enter the manuscript's proof dependencies and does not imply a complete row.
