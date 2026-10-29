# Independent review of the elementary compact small-noise comparison

**Outcome: no mathematical blocker found in the final stated domain.**

Review baseline `fb9e918bef3b0a932fb44bf1dae8d3e4a589f932`; separate branch `research/small-review-v16-20261029`. This reviewer constructed the separate v16 right-interval tangent extension, but did not construct `small-common.tex`. The present calculation derives its conditional variance transport, full incoming tail, quartic rectangle, normal repairs and joins independently. The checker imports no constructor checker.

Final reviewed source: `mathematics/simplification-v16/2026-10-29/small-common.tex`, SHA-256 `da583ea6712fa159345aa22d402faaa5cd60c518aec51c8aff033c09df636e11`.

| Result | Mathematical status | Execution status |
|---|---|---|
| Delta_C<−lambda/100 for every C>=0, n>=700, p∈[3/8,93/200], amplitude .6, inward sum .004, 0<lambda<=.01, raw abs(H)<=1.84, phase∈[−.3,.7] | Independently derived and checked; no blocker | 88 exact gates, including 40 full tensor-Bernstein coefficients, fresh PASS |
| Entire incoming sum from fourth moments | Independently derived; no Poisson theorem or tail truncation | Exact three series bounds and both complete coefficients PASS |
| Atoms, phase seam and vanishing/tiny conditional noise | Included by the analytic inequalities | 44 outward actual-law event checks on four iid laws PASS |
| Acquiring the compact interval/strip; full-noise and reflected union; unrestricted cutoff | Outside this component's scope | No claim made here |

## 1. Conditioning and normalization

The identity in Section 1 (`small-common.tex:49`) follows directly by conditioning on the actual count. The own outgoing event is `W_k>u`, not `>=u`; the incoming events are closed. Consequently discarding the other outgoing terms gives the displayed master inequality with the correct normal repair sign. This does not assume independent moment allocations across counts.

In the theorem's probability range, `v<=.465*.535`, so `v+s<1/4` even at `lambda=.01,n=700`. Thus `|t−np|<.92`. Subtracting the chosen phase gives `|delta|<5/3` globally and `<1` for `|u|<=.05`. The actual count lies inside the sample and its fraction is in `[.37,.47]`.

On that segment the largest absolute entropy third derivative and logarithmic-prefactor derivative occur at .37. Direct rational bounds give `<5` and `<6/5`; the factorial remainder is `<3/8`. The entropy contribution is at most `(5/6)D^3/n^2`, hence the stated `D^3/840` after multiplication by n>=700. This independently yields `Z(D)=3D/5+3/8+D^3/840`.

For the normal derivative, split the exponent difference exactly into

`delta² s/[2v(v+s)] − (2delta z+z²)/[2(v+s)]`.

Together with `log(1+s/v)<=s/v`, this gives the printed noise coefficient `11/5`; it exceeds `1/(2v*)+D²/(1400v*²)`. The bounds `exp(−x)>=1−x` and `exp(x)<=1/(1−x)` then prove both derivative rows, on the entire integration segment. No fixed-law limit or error independent of arbitrarily small lambda is introduced.

The global mass ratio is correctly obtained by dividing the global mode upper bound .85 by the own-mass lower bound .75. One must not infer that every ratio after the first decreases globally, since `p+Dglobal` can exceed 2. The final proof does not make that inference. In the inner interval `p+Dinner<2`, so the first exact ratio followed by decreasing ratios gives 1.02. The mode coefficient .41 follows by finite Stirling and the mode variance loss on `[1/3,2/3]`.

## 2. Cubic sign and normal repair

The two conditional supports lie on fixed sides of p, because their inward caps are .004. Expanding the actual absolute third moment and using

`E U0³<=a0 E U0²`, `E U1³>=−a1 E U1²`

gives the bracket

`9/8−1/250−51/64−(17/20)s>0`.

The normalization term uses the global inequality `(1+x)^(3/2)<=1+(3/2)x+(3/8)x²`, valid for x>=0. This establishes `rho>rho_B` for every positive noise in the theorem, including when one conditional noise vanishes. Therefore every C>=0 is licensed; no hidden positive lower bound on C is required.

The remaining variance-normalization error has coefficient `phi(0)/(2v*^(3/2))<2`, multiplied by `delta_+ lambda/n`. This proves the respective `2lambda/n` and `4lambda/n` repair bounds. The latter remains proportional to lambda at arbitrarily small noise.

## 3. Full incoming tail

With physical conditional variances s0,s1,

`t_i=lambda+(delta+i)(s1−s0)` and `|s1−s0|<=s/min(p,q)<=8s/3`.

For n>=700 this gives `t_i<=lambda(a+ci)`, where `c=2/525` and `a=1+cD0`. The same argument gives `.99lambda<t0<1.01lambda`. These statements use one common marginal and its actual count coefficients; no common-fraction shortcut is used.

Independence and `|U_j|<=.6` imply `E W_j^4<=.36t_j+3t_j²`. Markov applies to each closed incoming event because `i−u>0`. The complete reciprocal-power sums satisfy

`sum i^-4<13/12`, `sum i^-3<5/4`, `sum i^-2<5/3`.

The independent checker proves these by finite rational prefixes plus the integral remainder, not by a floating zeta evaluation. Extending the sum beyond existing counts only adds nonnegative terms. With `lambda²<=.01lambda`, the complete coefficients are exactly

- `Kinner=2237737/5250000`, and `Kinner/.95^4<.53`;
- `Kouter=84816089/198450000<.43`.

For u>=0 the distance inequality is `i−u >= (1−u)i`, explaining the factor `(1−u)^−4`. For u<=0 use `i−u>=i`. These estimates cover every incoming count and all count endpoints.

An actual-law negative control shows that the positive-phase factor cannot simply be omitted. Take n=700,p=3/8,lambda=.01, U1=0 and centered U0 supported on `{−3/5,1/26250}`. At t=262.7, choose k=262,u=.7. The first incoming count has 437 noisy summands; any one rare negative jump gives `W_263<−.3`. Bonferroni gives its probability at least

`357259/13057579 > .43*.01`.

This is an actual legal iid marginal and raw threshold, not an optimizer of a moment relaxation.

## 4. Independent quartic rectangle and Cantelli switches

For the strict-event minorant at alpha=13/25, its positive maximum is below one because `(9+6sqrt(3))/20<1`. Its value at zero is exactly zero, so no atom is silently moved to a strict event.

Expansion with `|E W³|<=A t` and `E W⁴<=A²t+3t²` gives the displayed full bivariate `F_sigma,b(z,t)`. The checker reconstructs that original polynomial. It does not use the constructor's substitution `z^4<=9z²/4` or its monotonicity reduction. Instead it computes all degree-(4,3) tensor Bernstein coefficients on `[0,3/2]×[0,101/10000]` after subtracting3/5. All 40 are strictly positive. The smallest exact margins are:

- negative phase: `803404433619/5849292800000`;
- positive phase: `1259697/2284880`.

The transform follows from the standard exact monomial-to-Bernstein identity in each variable. The checker also equates the power expansion with the directly evaluated formula at named rational points to catch transcription errors; the domain proof is the coefficient positivity, not those point evaluations.

For negative phases beyond `r=3t0/2`, the Cantelli function `r²/(t0+r²)−1.01r` has positive derivative at the switch. Its second derivative has the sign of `t0−3r²`, so it can have only a subsequent maximum, not an interior minimum. Both endpoint values exceed .6t0. The switch is always below .05. Positive phases beyond the switch are paid directly by `f(r)>=.99r`. Thus `O>.6t0>.59lambda` uniformly on the full inner interval, including u=0 and arbitrarily small lambda.

On the negative outer interval the same derivative argument checks both endpoints at the variance upper bound T. On the positive outer interval the function `.98u−(1.2)(.43)(.01)/(1−u)^4` is concave and both endpoints exceed .04. The three closed intervals meet exactly at ±.05 and cover `[−.3,.7]`.

## 5. Exact terminal margins and actual-law controls

After subtracting the requested lambda/100, the three terminal margins per lambda are

- inner: `3387/140000`;
- negative outer: `70681/7000`;
- positive outer: `2089/700`.

All are strictly positive. The last two deliberately use coarse lambda<=.01 conversions; their large slack is not extended beyond that domain.

`small-review-actual.py` independently constructs four actual iid marginals at n700/701: a rare noisy negative conditional, a rare noisy positive conditional, a tiny-defect law with lambda=10^-6, and independent symmetric noise with exact atom collisions. It checks 44 complete-CDF events at C=0, including eight evaluations of both legal anchors at the shared phase endpoint. Every law has its support, centering, noise, raw threshold and cubic sign checked rationally. The symmetric four-point law is evaluated by convolution of its actual independent Bernoulli and noise sums; this avoids an unnecessary four-atom occupancy enumeration.

The CDF/normal enclosure helper is reused explicitly from v10, SHA-256 `351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07`, loaded from verified source bytes with compile/exec. This actual-law run is regression evidence, not an independent normal implementation or a parameter-cover proof. C=0 is the weakest comparison because `rho>rho_B` was checked for each marginal.

## 6. Evidence, corrections and scope

Fresh evidence is under `runs/small-review-v16-20261029/`:

- `check02`: final proof pin, independent checker snapshot, 88 gates and the actual phase-factor counterexample, fresh PASS;
- `actual01`: four exact laws/44 events, fresh PASS in51.707 seconds; the unchanged actual checker is preserved;
- `mutations01`: changed proof, missing proof argument and missing source all reject;
- `check01`: earlier scalar pass retained before adding the stronger actual-law negative control.

The final independent checker SHA-256 is `3f19b5a048b88d7351d407d253286c2d5478e70a2f68a2d2c527f897bd4dd156`. Reproduce it with

`python3 -I -B mathematics/simplification-v16/2026-10-29/small-review-check.py --proof /absolute/path/to/small-common.tex`.

Run the actual script separately if desired; it requires no proof-object discovery or optimizer. The review also retains exact failures of three stronger sufficient bounds: outer coefficient .42, inner coefficient .52, and quartic constant .8. These are failures of the proposed scalar bounds, not claims about the full theorem.

Before final pinning the constructor fixed a missing TeX backslash and clarified that n is an integer and U_j is conditional noise. No mathematical formula, domain or target changed. The final source is the reviewed pin above. No old source, certificate, manuscript or external service was modified by this review.

This theorem supplies the positive-noise range through .01 for the newly acquired compact interval only. Coupled to the new compact five-count theorem from .01 and the all-p binomial theorem at zero, it can remove all Poisson/count-cell arguments from that selected acquired n>=700 route. The geometric acquisition of this compact interval and .004 inward cap is a separate premise; the present theorem cannot be applied merely from the older wider right or left strip hypotheses. Reflection, attainment and a genuine finite base remain separate obligations.
