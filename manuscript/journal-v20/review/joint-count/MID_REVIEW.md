# Independent audit: the fixed-phase quartic comparison through noise .08

## Conclusion

No defect was found in the fixed-phase polynomial implication, its global ray checks, or the exact accepted object. The result applies to `n>=47`, `1/20<=lambda<=2/25`, every phase in `[-1/2,1/2]`, under the enlarged global normalizer and the original acquired same-law assumptions, including `C>=2/5`. The unchanged strict target is `rho_B(C-C_B)<-lambda/1000`.

Its join to the existing 83 rows retains the actual row ceiling: the domain for each row is `[1/20,min(2/25,lambda_max(row))]`. There are 71 nonempty domains and 12 empty domains. Empty rows receive no intermediate-noise claim; their acquired ceiling is already below `1/20`. Combined with the independently reviewed small-noise proof, this covers all allowed noise through `min(2/25,lambda_max(row))` on every original row. No statement about larger noise follows.

Mathematical status: locally derived and independently reviewed conditional implication with a checked application join. Execution status: fresh exact normalizer recomputation, full object acceptance, independent polynomial-identity verification and raw-input join. No acquisition, Fourier integration or all-index theorem was newly executed or accepted.

## Independent argument and source review

Before reading the proposed note, the auditor derived the fixed-phase rule from the already checked joint-array staircase bound. For fixed `w`, the staircase payoff `psi(w,u)` is nondecreasing in `u`, including at atoms. Thus a polynomial dominating `psi(w,b)` on the whole real line dominates the actual payoff throughout a closed phase interval `[a,b]`. Meanwhile `f(u)>=L_f(a)`, with `L_f(a)=lf*a` for nonnegative `a` and `hf*a` for negative `a`.

For `q=q0+q1*w+q2*w^2+q3*w^3+q4*w^4`, centering removes `q1`. The bound `q4>=0` permits

`E q(W)<=q0+(q2+A*abs(q3)+A^2*q4)t+3*q4*t^2`.

Adding `eta*t-L_f(a)` produces a convex polynomial in `t`. Its two endpoint checks therefore prove the entire containing variance interval, `t in [18319/400000,21681/250000]`. This interval is derived from `omega_lo/20` and `omega_hi*(2/25)`; actual variance is not identified with `lambda`.

The complete `root/mid_math.py`, `accept_mid.py`, `build_mid_v2.py`, and `analytic/FIXED_PHASE_QUARTIC.md` were read. The following boundaries are correctly represented:

- The 200 fixed closed phase cells have width `1/200` and cover `[-1/2,1/2]` without gaps.
- The right ray checks `q(w)+1>=0` for `w>=b`. The first finite interval separately enforces `q(b)>=0`, preserving the strict outgoing event at the threshold.
- For each integer staircase knot, the finite interval beginning there supplies the larger value. The last knot is supplied by the left ray. The nine finite pieces and two rays therefore form a global majorant.
- On the left ray `x>=9`, the linear requirement `q(b-c*x)>=R0*x` dominates the entire floor, not just its first nine levels.
- Compactification multiplies by `(1-y)^4`. Division back is only made for `y<1`, which represents all finite points of the ray. Nonnegativity at `y=1` is compatible with a vanishing leading coefficient but cannot compensate for any negative neighborhood before that endpoint.
- Every tree split requires both closed halves, every leaf has all five degree-four coefficients, and inverse Bernstein reconstruction binds it to the externally fixed target polynomial. Nonnegative coefficients establish positivity over the full closed interval. Both rays are mandatory.

The independent recomputation of the `.08` normalizer exactly matched the previously captured configuration and all 41 unchanged gate formulas. Its derivative bounds are `86879/100000` and `113121/100000`, and its nonnegative repair is `59549/25000`. The constants used in the quartic acceptor were checked against this configuration, rather than against the old `.05` normalizer. The final exact reserve beyond the requested target is `5359299/400000000` times `lambda`, which supplies strictness even when some polynomial inequalities are non-strict.

## Fresh evidence and the failed old ray

`runs/joint_count_20261104/audit_mid01` returned zero with all source and input hashes unchanged. It records the exact interpreter command, streams and before/after hashes. The accepted object is `runs/joint_count_20261104/root_mid_construct03/proof_objects.json`, SHA-256 `b1f882b745e410dd34af9c2dbe609e5dfef47687a3f62bc4564a1cb57473331f`.

The independent checker verified all 4,243 leaf identities by evaluating the two known degree-at-most-four polynomials at five distinct exact rational points. Equality at those five points proves polynomial identity; positivity still comes from the nonnegative Bernstein coefficients, not from sampling. It also made 8,800 direct target-substitution checks, checked all 400 variance-endpoint inequalities independently, and reconstructed all 83 original row applicability joins with their actual ceilings and both signed threshold bounds.

Ten malformed objects were rejected, including omitted rays, omitted/changed phase cells, swapped rays, a negative fourth coefficient, a changed polynomial, a boolean row index and a negative Bernstein coefficient.

The old discovery row 69 is a genuine counterexample to treating a bounded grid as a global ray certificate. After the original rationalization its fourth coefficient is zero and its cubic coefficient is positive. At phase upper endpoint `b=-3/20` and `w=-100`, its polynomial equals

`-16377612853439/100000000`,

whereas the required staircase value is

`5395521/50000`.

The inequality fails decisively. The new object rejects substitution of this old row. This failure concerns the old proposed majorant, not the manuscript theorem or the accepted replacement.

## Remaining limits

The proof replaces probability estimates only on the verified noise interval. Existing same-law acquisition, inward support, conditional centering, actual iid realization, finite normalization and `C>=.4` remain premises. The higher-noise whole-count argument and finite-index positive-allowance comparisons are not discharged by this object. No such broader conclusion was inferred from its PASS status.
