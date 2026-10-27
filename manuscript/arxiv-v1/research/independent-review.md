# Independent review of the new manuscript implications

Review date: 2026-10-27. Reference baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`. Review branch starts at `8989ba054eda36f63e469832f1e00f7e6a7a9084`. The reviewed manuscript was a live draft in the separate manuscript worktree; `independent-review-inputs.json` records repository-relative paths and content hashes. A commit identifier alone would not identify these then-uncommitted source bytes.

## Conclusion and independence boundary

No unresolved blocking mathematical defect was found in the reviewed **new conditional implications**: the zero-loss support argument, the exact curvature formula with its zero clamp, the elementary moment-domain inequalities, the binomial-normalization extension, and the equality-inclusive global composition. The floor-42 appendix is correctly presented as an interface implication conditional on retained analytic identities, all their gates, and the complete selected numerical predicates. It does not establish that these predicates have been accepted.

The review supports integration as a conditional research manuscript. It does not establish BASE41, the uniform LOCAL42 assumption, the full inherited Fourier/confinement/count chain, or the conjecture. Completeness of the longer Fourier and finite-analysis appendices requires a separate integration check: their final content was not part of this review. Main-text assertions that those arguments are supplied must be checked against the completed delivered manuscript.

The reviewer authored the earlier score-charge construction, the earlier uniform42 interface report, and manuscript Sections 2, 3 and 5. Accordingly, Section 6 received only a transcription and interface check here; this report is **not an independent review of that construction or of Sections 2, 3 and 5**. The floor-42 appendix received a transcription/interface check and a fresh derivation of its displayed elementary inequalities, not a second independent validation of the earlier full bridge. These earlier contributions require the separate reviews arranged by the coordinator. Curvature was independently reviewed by this reviewer earlier; the current review checks its manuscript transcription and its joins. The new support and moment arguments were derived directly from the displayed formulas, without treating the author's prose or numerical success markers as proof.

| Item | Mathematical status in this review | Execution status in this review |
| --- | --- | --- |
| Support envelopes and exterior-ray implication | Independently derived at the stated contact, score and acquired-moment hypotheses | No native program or certificate campaign run |
| Curvature supremum and clamped transport | Independently checked as continuous-domain statements | No repeat of the earlier diagnostic suite |
| Moment inequalities and binomial-normalization extension | Independently checked from the displayed factorizations/derivatives | No numerical acceptance asserted |
| Score-charge chapter | Transcription/interface check of the reviewer's own construction | Earlier constructor/reviewer evidence remains separate |
| BASE41 + equality-inclusive LOCAL42 implication | Independently checked, conditional on both assumptions and attainment | No base or LOCAL42 acceptance run |
| Complete floor-42 acquisition/exclusion chain | Conditional interface only; full retained analytic chain not independently reproved here | Native predicates not run |

## Findings and corrections

1. **Missing support hypothesis, corrected.** `sections/04-support.tex:5–18` now assumes `C_{n-1} <= C_n`. Merely assuming `n >= 42` and `C_n >= C_E` did not justify discarding the predecessor loss in the displayed contact inequality. The added hypothesis supplies zero positive global loss; the current law's predecessor score is bounded by the global predecessor score. This is a mathematical hypothesis repair, not a cosmetic change.

2. **Squared gates needed positive constants, corrected.** `appendices/uniform-bridge.tex` now requires `c_rho > 0` and `F_d > 0` as well as their squared inequalities. A negative `c_rho` can satisfy the squared gate while making the claimed upper third-moment bound false. The intended constants 30 and 24 are positive, so the intended application is unaffected.

3. **Gaussian derivative and scalar remainder explanations, corrected.** Section 4 now includes the direct derivative estimate and the identity `n e_n = s^2(2s+1)/(2(s+1)^2)`. The former is what licenses the entire exterior ray; a boundary sign alone would not do so. The latter gives the exact bound `793881/2073680 < 48/125` at `s=81/80`, and hence `e_n < (48/125)/n <= 8/875`.

4. **Normalization factor, corrected.** `appendices/normalization.tex:29–42` now puts the factor `1/2` in the logarithmic variance-prefactor estimate. Without that wording, the preceding estimate did not yield the displayed final `L |delta|/2` bound. The final result and its corrected proof agree.

5. **Dependency attribution, corrected.** The introduction correctly calls the structural third-moment estimates the first *quantitative moment cap for support*, rather than an input to fixed-index attainment. The least-index argument supplies the deleted bounds and zero predecessor loss; smoothing supplies the current excess/score caps. The corrected abstract and Section 8's proof have the same dependency order.

6. **Coordinate and mass notation, corrected.** The expansion in Section 4 now uses `z_v=H/sqrt(n-1)`, leaving `z=H/sqrt n` unambiguous. Section 7 now distinguishes the cell constant `z_mark` and the mass lower bound `m_0` from the global threshold and the physical first absolute half-moment, including in the final strict target. Section 6's exported raw quantity is correctly called a resource remainder ceiling, rather than a score.

7. **Unreviewed retained analysis stays conditional.** `sections/08-certificates.tex` and `appendices/uniform-bridge.tex` explicitly retain the full Fourier and signed phase bounds, ordered actual-law acquisition, strict confinement gates, signed normalization, profile acquisition, positive-noise comparison, and zero-noise theorem. This is the correct status. Neither importing their source text nor matching source hashes independently establishes those analytic arguments. The final manuscript must not promote this conditional status merely because the appendices have been typeset.

## Support proof: independently checked reasoning

Source: `sections/04-support.tex`, especially the displayed contact, expansion, error, envelope and ray formulas.

Let `v=n-1`, `s=sqrt(n/v)`. Heat differentiation gives `partial_v F_v = F_v''/2`. Expanding the four terms of the Gaussian expression as specified cancels the constant, linear and quadratic spatial terms. The remaining coefficients are `(-t^3+3t)/6` and `(t^4-6t^2+3)/24`, giving the displayed signed cubic and common quartic terms. The four remainder scales are respectively `u^5/v`, `1/v^(3/2)`, `u/v`, and `(u^2-1)/v^(3/2)`, with exactly the printed factorial factors. These bounds are uniform in the raw threshold and require no moments beyond those already licensed by contact/support.

Gaussian Fourier inversion yields `||phi^(4)|| <= 3 phi(0)` and `||phi^(5)|| <= 8/pi`. The printed rational bounds therefore give the stated `E_v`. The coarse envelope follows from `||(1-z^2)phi(z)||=phi(0)` and `||phi'''||<2phi(0)`. For the sharper envelope, on the positive branch with `|z|<=1`, completing the square in `A-Az^2+3B|z|` gives `A+9B^2/(4A)`. Outside that interval the cubic term is nonpositive. On the negative branch its positive maximum is `2 exp(-3/2) A phi(0)`, less than `A phi(0)/2`; `B<=A/4` then suffices for both signs. No sign-reflection of the marginal is used inside this calculation.

For the ray estimate, exact differentiation gives

`partial_t H_n = n phi(z) + H t phi(z) - n s phi(sy)`,

where `z=H/sqrt n` and `y=(H-t)/sqrt n`. Taylor's theorem bounds the spatial difference by `phi(0)t^2/2`, and `partial_s[s phi(sy)]=-phi''(sy)` bounds the variance difference by `phi(0)(s-1)`. Thus `|partial_t H_n| <= phi(0)(t^2/2+1/2+e_n)`. This estimate applies to both `t=+u` and `t=-u` after the chain rule. It supplies the printed `L` envelope.

The order of sign substitutions matters and is correct: first prove `Q<0` and `Q'<0`, then replace the actual multiplier `C_n>=C_E>c_0` by `c_0`. For a fixed acquired pair `(r,b)`, the six negative values at a boundary persist because `Q'''=-6` and `L''=2/5-6c_0<0`. Consequently the actual contact upper bound decreases on each whole exterior ray. Endpoint atoms are covered by contact on closed support; a negative boundary excludes the boundary itself.

For the affine family of 63 calls, `r_R` and `b_R` are frozen at the selected boundary `R` while extending its ray. Differentiating them along the exterior ray would be a different argument. The manuscript explicitly freezes them and uses larger common caps for the derivative tests. The moment tuples and their ordered acquisition remain prerequisites. This review did not rerun or independently recertify the 65-row binding and every listed rational arithmetic margin; the separate support review and run records have that scope.

## Curvature: continuous domain and transport

Source: `sections/07-curvature.tex:5–88`.

On the active first branch, the printed second derivative is positive because its numerator is `3(b+u-1)+(c-u)>0`. Below the denominator kink, the second summand has derivative `(c-2b-u)/(c+u)^3`; where the first summand is also positive, its second derivative is positive on `u in [-1/2,1/2]`, `1/2<c<=1`. Above the denominator kink the second summand is piecewise linear and convex. Derivative jumps at both positive-part kinks and the denominator kink are nonnegative, including collisions. Thus the only possible interior nonconstant maximum with first summand zero is `u*=c-2b`, subject to exactly the stated eligibility tests. Its value is `1/[4(c-b)]`. Endpoints, singleton intervals, `c=1`, and simultaneous kinks are covered.

Both denominators increase with `c` for fixed `u`, so the monotonic cache comparison is in the stated direction. The CENTRAL cache assertion also requires that the other cache-key inputs remain fixed and that its first band has the smallest `c`; it is not a license to cache every other `c`-dependent term. Those other local terms are retained.

For positive noise, `B` is convex and `I_new=A_0+A_1/lambda` is convex when `A_1>=0`. The positive part `I_+=max(0,I_new)` is convex. For every `n>=N`, `I_new/n <= I_+/N`, also when `I_new<0`. Hence the entire new upper bound is convex and checked at the closed-cell endpoints, even across an interior clamp kink. At an accepted old endpoint, `I_new<=I_old` and `I_old>0` imply `I_+<=I_old`. The separate negative event-bracket gate is retained before a positive mass lower bound multiplies it. This proves conditional transport from accepted old cells; it does not establish their acceptance.

## Elementary moment and binomial arguments

Sources: `appendices/moment-domain.tex` and `appendices/normalization.tex`.

The displayed two half-line factorizations of `w` have nonnegative factors, with `ab=1`, `a+b=s` and `b-a=gamma`. Taking expectations gives exactly `rho-(gamma^2+2)/sqrt(gamma^2+4)`. Every term is integrable under the finite-third-moment assumption. The signed-second-moment proof uses `m^2<=p_+a_+` and `m^2<=p_-a_-`, then `p_++p_-<=1`; its second Cauchy inequality gives `m rho >= (1+beta^2)/2`. This proves the stated bound including a possible zero atom. No support or higher-moment hypothesis is introduced.

For normalization, `a+b<1` puts the entire Taylor interval inside `[a,1-a]`. Symmetry and monotonicity of `r(1-r)` on `[a,1/2]` give both derivative envelopes even when the interval crosses `1/2`. Taylor's entropy error is `E|delta|^3/(6n^2)` in the exponent; the log-prefactor error is `L|delta|/(2n)`. The factorial remainder is bounded using the compatible one-sided inequalities `e<1/(12n)` and `e>-1/[12n r(1-r)]`, giving `|e|<R/n`. This verifies the printed error bound. Interior and adjacent-factorial gates remain necessary. The finite Stirling inequality itself is a retained analytic input here; the complete appendix must provide or cite its proof.

## Floor 42 and the global implication

Sources: `appendices/uniform-bridge.tex` and `sections/08-certificates.tex`.

The floor-42 conditional-moment estimate follows from `|mu_i|<=sigma w_i`, `pq(w_0+w_1)<=q s`, `ell^3<=[l(1-l)]^(-3/2)`, and monotonicity of the Bernoulli third moment. Conditional centering ensures the inner-gap bounds are nonnegative; together with their sum below `sigma`, the strip gives `|U_i|<sigma`. A positive `c_rho` satisfying the stated gate therefore licenses coefficient 30 at the first left contraction; coefficient 24 cannot be copied from a narrower strip without checking its gate.

The strict-gap concentration argument uses one independently coupled pair of conditional noises per coordinate. A label change increases a summand by at least `1-d_Y`, so an interval of smaller diameter has an antichain inverse image. The random-chain proof gives the weighted antichain inequality and the binomial-mode bound. Equality in the interval-width restriction is deliberately excluded. The asymmetric mode limits are `p-q/j <= k/j <= p+p/j`; with `j>=40` they give the displayed outer interval. Its strict endpoint gates ensure interior modes. The finite-Stirling estimate and `exp(x)<=(1-x)^(-1)` then give the stated common concentration ceiling. The two alternative deleted-score scale ratios are decreasing in `n`, so the positive factor gate at 42 is sufficient at every larger index.

The remaining signed-confinement discussion retains its actual-law deletion identities and strict resource premise. It correctly explains why `(zR+A)>0` is required before substituting `1/n<=1/42`; nonnegativity of the removed resource `P` gives `R-nP<=R-42P`. The tangent bound has nonnegative error `42 tau (x-t)^2/[(42 tau+x)(42 tau+t)^2]`, so taking the minimum of two valid error bounds is permitted. These observations check the stated index changes. They do not independently prove the inherited deletion, Fourier, local-count or profile formulas. Those remain explicit premises in the final assembly paragraph.

The conditional global theorem is logically valid at equality. If BASE41 holds and strict tail failure occurs, choose the least `n>=42` with `C_n>=C_E`. Its two predecessors are at most `C_E`; at `n=42` they are exactly base indices 40 and 41. Therefore the loss is zero and both strict deleted caps hold. The support-free recurrence supplies the stated current score and excess caps. Attainment at `C_n=C_E>0` supplies the closed positive maximizing pair, which the equality-inclusive LOCAL42 assumption excludes. A theorem excluding only `C_n>C_E` would give only the weak conclusion; the manuscript makes this distinction. The lower bound for the supremum over all indices separately uses the fixed-law Bernoulli limiting theorem.

Changing a literal source wrapper from `42<=n<=48` or a confinement theorem from `n>=47` is not part of this proof. The new support lemma removes the finite-heat obstruction, and the parameterized bridge describes the needed new interpretation, but all selected numerical domains, source bindings and predicates still need an accepted new composition. In particular, a historical PASS under the old wrapper is not a fresh uniform acceptance.

## Computation claims and remaining limits

The inventory `238 -> 171 -> 169` is explicitly confined to a selected upper-module component. The final number is 150 surviving signed LOW producers plus 19 other obligations, before new composition checks. Removing final row 0's comparison requires first acquiring the resources that exclude that row; acquisition or confinement ancestors are not removed. The source's complete sign/phase/count cover, strict comparison margins, and zero-noise Bernoulli branch remain necessary.

The 152-row byte-preserving prototype is a different acceptance contract from the changed curvature/resource outputs and a 150-row inventory. The manuscript correctly refuses to multiply these savings or claim an already accepted combined implementation. No measured runtime saving or whole-repository task count follows.

This review made no change to production code, old certificates, the reference baseline, or the reviewed manuscript. It ran no inherited checker, generation campaign, or native local predicate. No TeX/PDF rendering was performed by this reviewer. The final compile, reference resolution, appendix inclusion, layout inspection, literature verification, all numerical source bindings, and full base/local acceptance remain with their separately identified tasks. Hashes in the companion record identify what was read; they are not mathematical evidence of correctness.
