# Independent audit of the small-noise joint-count comparison

## Conclusion and scope

The proposed new incoming-count bound is sound, and the four fixed polynomial families establish the requested strict comparison on the two selected probability rows, conditional on the existing acquired same-law inputs and `C>=.4`. The domain is `n>=47`, `0<lambda<=1/20`, all phases `-1/2<=u<=1/2`, central row 10 (`p in [2/5,201/500]`) and left row 28 (`p in [9/25,181/500]`). The target remains `rho_B(C-C_B)<-lambda/1000`.

Mathematical status: locally derived and independently checked at this conditional application scope. Execution status: fresh exact acceptance of the original normalizer and four polynomial witnesses, plus independent finite formula/path controls. Acquisition, Fourier integrals and the remaining probability rows were not replayed. No larger-noise whole-count replacement or all-index theorem is asserted by this audit.

## Independent derivation

`INDEPENDENT_DERIVATION.md` was written before reading the new analytic proof or constructor's formula implementation. It derives the monotone joint-array coupling, the strict outgoing/closed incoming conventions, the own-count staircase majorant, both second- and fourth-power bounds, the combined expectation and all four phase branches.

The useful new step is

`floor((u-W_k)/c)_+ <= W_k^4/(c-u)^4`.

For an integer staircase value `r>=1`, `W_k<=u-cr<0` and `(cr-u)^2-r(c-u)^2=(r-1)(c^2r-u^2)>=0`. Squaring and using `r^2>=r` proves the bound under `|u|<=c` and `u<c`. Here `c=9819/10000>1/2` and `|u|<=1/2`, so the hypotheses hold on the full domain. This replaces the entire incoming tail sum by one fourth moment of the actual nearest-count noise. It does not assert that neighboring counts have the same law.

The shifted quartic minorant supplies the negative outgoing term. The unfavorable fourth moments combine into one negative coefficient in the loss, so their simultaneous replacement by `A^2 t+3t^2` is valid. The third-moment contribution is bounded with its actual phase sign. Negative far phase uses Cantelli on the closed event, hence gives the required strict-event complement; positive far phase uses nonnegativity of the outgoing probability. These estimates preserve a bound proportional to `t` as `t` tends to zero.

The independently read `analytic/EXPECTATION_RULE.md` gives the same implications. Its generic interval/ray witness also handles staircase jump endpoints: the interval beginning at an integer supplies the larger value, and the ray supplies the last boundary. Its moment generating polynomial is the product for the two actual conditional laws, not independently optimized moment data at different counts. The sole requested editorial clarification was to identify the derivative and maximum in its quartic argument as those of the numerator.

## Source and coverage review

The complete `construction/model.py`, `accept.py`, `polynomials.py`, the pinned native normalizer and both amplitude-contract sources were read. Their exact reviewed checkpoint is recorded before and after execution in `runs/joint_count_20261104/audit_targets01/RESULT.json`.

- The normalizer is pinned and its 41 original gates are freshly checked. The selected native rows are bound in full, with their index, probability interval and existing acquired constants. The actual amplitude tables are read from pinned sources; their selected amplitudes are bounded by the conservative `17/40`. Both threshold signs, variance/inward caps and the full chosen noise interval are checked against the normalizer.
- The four formulas agree with the independent expectation calculation. Near phases use `t=T*x`, `r=z0*t*y`; far phases use `r=z0*t+(1/2-z0*t)*y`, on the entire unit square. The negative and positive splits are `z0=5/3` and `6/5`, respectively, with `z0*T<1/2`; the two closed branches overlap at each split and cover every phase.
- All `c-r` denominators are strictly positive. The negative far denominator `t+r^2` is positive whenever `t>0`. Its value zero at the artificial corner `t=r=0` is never divided by in the application. The cleared polynomial has zero coefficients there, which is compatible with the proof.
- Acceptance reconstructs each fixed power polynomial from the full tensor Bernstein expansion. This inverse reconstruction is separate from discovery's forward conversion. The fixed degrees and complete ordered case list prevent silently losing a branch or coefficient. The four full rectangles use 244 rational coefficients, with no adaptive subdivision.
- Nonnegative coefficients prove a non-strict loss `>=t/10`; the checker does not need to infer strict positivity from them. The independent final calculation gives

  `m*(1/10)*omega_lo-kappa/47-1/1000 = 252847053/18800000000 > 0`.

  Since positive noise and `omega_lo>0` imply `t>0`, this strict margin proves the original strict score target. The repair uses `C>=.4`, which remains an explicit analytic premise. At zero noise the proof still invokes the separate Bernoulli result.

## Fresh controls

`runs/joint_count_20261104/audit_paths01` completed with actual return code zero in approximately 5.32 seconds. Its separate exact implementation checked 122,370 joint-array paths, including 13,662 exact event collisions, 1,122 expectation identities, 72 equalities between direct iid convolution and conditional-count convolution, and 5,220 staircase/scalar cases. The law families included symmetric and skew laws, reflected skew laws, either conditional component deterministic, tiny amplitudes, tiny outward atoms and zero-noise Bernoulli. These small-law controls test the universal probabilistic mechanism; they are not presented as all satisfying the selected acquired numerical inputs.

Four false variants were explicitly contradicted: replacing strict outgoing events by closed ones; dropping the phase guard in the quadratic bound; dropping it in the quartic bound; and claiming a larger inward spacing than the actual process has.

`runs/joint_count_20261104/audit_targets01` completed with actual return code zero and stable before/after input hashes. An independent implementation of the rational expectation expressions agreed with the constructor's target evaluations at 196 points, including every corner and very small positive variance. This finite grid is a regression check; the continuous positivity conclusion comes from the reviewed exact Bernstein reconstruction. Nine malformed or changed objects were rejected: a weaker target, changed loss coefficient, missing/reordered phase branch, missing coefficient row, changed coefficient, negative coefficient, noncanonical rational and duplicate JSON field.

## Consequences for shortening

On the proved small-noise domain, the incoming Bennett/Poisson comparisons, infinite tail sum and relative-tail monotonicity argument can be replaced by the short monotone-count fourth-moment proof and its four rational polynomial witnesses. The full manuscript may only remove those dependencies once the same application join is checked for every row that used them. The present two-row pilot alone does not authorize that deletion globally.

The inward support gap, actual iid conditional pair, sign-sensitive finite normalization and repair, simultaneous input bounds, full closed cover and zero-noise branch remain necessary premises of this route. Larger-noise cells still require an independent successful witness. The earlier examples showing unequal full CDFs with equal own-count data do not obstruct the new upper bound: recovering the exact CDF and bounding it are different mathematical tasks.
