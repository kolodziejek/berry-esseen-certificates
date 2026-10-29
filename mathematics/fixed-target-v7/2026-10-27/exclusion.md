# Strict count: a wider harmonic domain and an actual-law obstruction

The new component proof extends the conditional-span hypothesis of the
fractional-part estimate from `b<1/2` to `b<1`. The boundary at one is real:
an explicit rational standardized three-atom law has `D<7.475e-8`,
`lambda<2.441e-8`, a wide actual central gap, and positive conditional noise,
yet its marked fractional-part gain is exactly zero. The same construction
works with arbitrarily small positive defect and noise. Therefore a direct
replacement of support confinement by moment resources alone is false.

This is not a counterexample to the sharp conjecture, the retained LOCAL42
theorem, or an implication that uses an actual maximizing contact inequality.
No score above CE or maximizing contact is asserted for these laws.

| Result | Mathematical status | Execution status |
|---|---|---|
| Harmonic estimate for every conditional span `0<b<1` | Locally derived and checked; full proof in `exclusion-proof/exclusion.tex:88–139` | Analytic result; exact rate example at `b=3/4` checked |
| No positive uniform gain at span one, even with arbitrarily small actual `D,lambda` | Locally derived using actual rational iid laws; not a relaxation | Fresh exact PASS: four laws, 104 conditional-sum states |
| Scalar marked-parameter feasibility test | Exact one-variable minimization under the existing count formula | Seven exact boundary cases, including strictness and constrained optimum |
| Complete strict count exclusion from the new coarse entry | Not established; conditional support and score gates remain | No native LOCAL42, TINY/MID/LOW or dense acquisition run |

All additions are on `research/v7-exclusion-20261027`, starting at
`ab4bb3f0353fedc68772159429e76b83dd79af78`, in the user's fork.
The original baseline and all production certificates are unchanged.

## Exact minimal interface, rather than a replacement numerical target

The fixed-target master identity has nonnegative left side
`a+rho_B(c−C_B)` when `a>=0`, `c=CE` and the Bernoulli theorem supplies
`C_B<=c`. Its repair uses the fixed multiplier `c`, not an actual score
upper bound. The two sufficient local witnesses are in
`manuscript/arxiv-v1/sections/05c-counts.tex:77–107`:

1. **Nearest count.** A strictly positive outgoing-plus-Gaussian minus
   incoming bracket `D0=O−R0*T` must precede the lower binomial-mass
   substitution. Then `m0*D0−kappa*lambda/n>0` excludes.
2. **Whole count.** With `lambda>0`, first prove `B(lambda)<0`, then
   `m0*B(lambda)+max(0,I(lambda))/N<0`. The clamp is needed before
   replacing `1/n` by `1/N`. A chosen positive margin can be retained.

The exact whole-count formula is at
`manuscript/arxiv-v1/appendices/fourier-analysis.tex:4024–4058`.
For a fixed positive noise value it is `B=z+A_lambda/z−F_lambda` with
`A_lambda>=0`, `0<z<=1/U`. After subtracting
`max(0,I)/(N*m0)` from the available gain, write that gain as `F` and
`Z=1/U`. If `A_lambda>0`, feasibility is exactly

```
F > 2 sqrt(A_lambda)       when Z² >= A_lambda,
F > Z + A_lambda/Z        when Z² <  A_lambda.
```

In the first case this is the rational test `F>0` and `F²>4*A_lambda`.
If `A_lambda=0`, feasibility is `F>0`. Equality fails. This eliminates
blind search over `z` at one noise value; a common `z` must still satisfy
both noise endpoints before using the retained convexity argument. The
checker is not an external acceptance API for arbitrary count inputs.

The final expressions additionally require all of the following edges;
none is supplied merely by lowering a scalar defect target.

| Required input or gate | Exact source and reason |
|---|---|
| One common iid marginal; exact conditional centering; legal interior count; closed incoming and strict outgoing events | `sections/05c-counts.tex:10–50`; this justifies the mixture identity and own-count variance conversion |
| Positive `omega_-=1-c_v*Delta/N`, actual phase bounds, positive binomial mass | `appendices/fourier-analysis.tex:3574–3618,4024–4046`; moment variance is not automatically the own-count variance |
| Conditional inward gap and amplitude, `c=1-d0>1/2` in retained crossing proof | `fixed-target-v5/2026-10-27/count-cost.tex:10–105`; the v5 maximum and quartic improvement retain these hypotheses |
| Positive first-mark and tail denominators; actual deleted conditional laws; `0<eta=z*lambda<=1` | `appendices/fourier-analysis.tex:3880–3961`; this supplies the linear marked-crossing term, not only curvature |
| Fractional-part gain from a proved conditional span or another nonresonance estimate | `appendices/fourier-analysis.tex:3963–4022`; only this component's span domain is extended here |
| A single weighted resource and coherent joint `d/lambda` budget | `mathematics/simplification/2026-10-27/uniform42.md:288–338`; separate extreme choices must not spend the same resource twice |
| Signed Gaussian and cubic repair, including a possibly negative cubic bracket | `appendices/local42-refinements.tex:327–435`; the upper multiplier is required when the bracket is negative |
| Closed probability, noise and phase coverage; both threshold signs; zero noise separately | `appendices/local42-refinements.tex:460–495`, `uniform42.md:342–377`; the new scalar component supplies no replacement cover |

In the first-mark individual bounds, positivity is precisely
`1−2*d0−u_h>0` and `1−A+u_l>0` for the nearest mark. Thus on the full
phase interval `[-1/2,1/2]` the simple sufficient geometric targets are
`d0<1/4` and `A<1/2`. These already give `A+d0<3/4<1`: the extended
harmonic lemma removes the extra old requirement `A+d0<1/2` at that step.
The optional common-mark bound has additional gates, and a larger span
lowers the available harmonic rate. These geometric targets are useful
acquisition outputs, not a promise that the resulting final score is negative.

## Why 0.784 and 2.24 are not universal count thresholds

`mathematics/fixed-target-v5/2026-10-27/cell-sources/accept_initial42.py:36`
requires `raw<2.24` and `d<.784` as the fixed final initial target;
line 44 requires them for every nonempty probability panel. The same
object also requires a particular ordered 12-stage cover of 18,432 cells
and the 100-panel output, with further moment/threshold caps at line 45.
They remain mandatory for that unchanged acceptor.

They do not appear in the abstract final local witness above. A different
acquisition could bypass that acceptor by proving every needed later
hypothesis directly. Neither replacing its target nor declaring its
complete output accepted from a smaller new calculation is justified.
The exact retained uniform theorem still assumes its complete acquisition,
confinement, profile and local numerical predicates
(`uniform42.md:342–377`). No current certificate dependency is deleted here.

## New harmonic proof and its exact limitation

For independent summands of span at most `b<1`, concavity of sine on
`[0,pi]` gives

```
|E exp(2 pi i Z)|² <= 1 − 4 sin²(pi b) Var(Z)/b².
```

Products and `1−x<=exp(−x)` give the rate
`r=2 sin²(pi b)/b²`. If `1−cos(2*pi*x)<=K*x` on `[0,1]`, then
`E{w−W} >= (1−exp(−r*t))/K` for all phases. The old `K=23/5`
(or 4553/1000) keeps its separate scalar proof obligation. The note also
proves `K=8` elementarily, so the extended-domain theorem has an entirely
analytic version without any inherited finite positivity predicate.
At `b=3/4`, `r=16/9` exactly.

At span one, the centered residual with atoms `epsilon−1,epsilon` and
probabilities `epsilon,1−epsilon` has positive variance but lies on one
integer coset. Its sum's fractional part can be zero exactly. For the
limit `b` tending to one from below, take `Z=±b/2` and `w=−b/2`:
`E{w−Z}=(1−b)/2` tends to zero with variance tending to 1/4. This directly
proves failure of a uniform fractional-gain rate; failure of a sufficient
characteristic-function bound alone would not prove it.

## The rational iid family, including the response theorem's missing edge

Choose rational `epsilon,t>0` and set
`q=(1+epsilon−epsilon²)/(1+t²)`, `p=1−q`, `r=t*q`, with `epsilon<p`.
Let `Y` have atoms `epsilon−1,epsilon,1` and probabilities
`q*epsilon,q*(1−epsilon),p`; put `X=(Y−p)/r`. Its mean is zero and
variance exactly one. Its actual sign split is `U1=0` and
`U0=epsilon−Bernoulli(epsilon)`; its normalized central-gap increment
is `1−epsilon` and `lambda=n*q*epsilon*(1−epsilon)`.

The checker constructs the actual closed support gaps and their zero-bias
weights. It does not use the skeleton's J in the physical defect. Exact
rational moments and a squared rational enclosure of sqrt(10) give:

| epsilon | t | D upper bound | lambda upper bound | v6 rho cell |
|---|---:|---:|---:|---:|
| 0.01 | 21/25 | 0.670241 | 0.246199 | 3 |
| 0.001 | 21/25 | 0.070624 | 0.024625 | 1 |
| 0.000001 | 21/25 | 0.000738 | 0.000025 | 1 |
| 0.000000001 | 849/1000 | 0.0000001 | 0.0000001 | 1 |

Each law satisfies its own recorded v6 defect and weighted `nD` bounds,
the strict actual-gap criterion, the support radius 96/25, and `D<.784`.
These comparisons read the pinned table; they are not a fresh Fourier
reproduction or a claim that the law has nonnegative fixed-target excess.
At `n=42,k=17`, choosing `u=eta=25*epsilon/2` gives a legal marked
phase. All 26 possible conditional sums have fractional part zero at
`w=u+eta=25*epsilon`, despite strictly positive own-count variance.

The last law also satisfies the probability, theta, rho, beta and both
inner-endpoint bounds in the v5 response theorem's central row 19:
`response-proof/response.tex:119–140`. Its only failed listed domain
bound is the support radius 1.84, because the rare outer atom has magnitude
greater than 2.875. This is an exact source-specific reason that the response
theorem cannot be reused just because moments and the central gap look good.
Its common-measure identity and single residual budget remain valid at
their stated general scope (`response.tex:44–115`); its particular numerical
response bound remains conditional on that full narrow domain.

The corollary in `exclusion-proof/exclusion.tex` proves arbitrary smallness:
as epsilon tends to zero, D tends to the matched Bernoulli defect
`(6+2sqrt(10))(p−p*)²/sqrt(pq)`. Rational t can approximate the minimizing
probability arbitrarily closely. The rare outer atom remains within radius
3, but its positive weight keeps conditional span exactly one. Thus neither
arbitrarily small D nor a wide central gap controls this support feature.

## Bounded evidence and next proof obligation

`exclusion_check.py` imports only the Python standard library. It executes
no inherited driver or Fourier primitive. Its fixed invocation checks four
actual laws, two Bernoulli controls, 104 exact conditional-sum states, seven
one-variable barrier cases, and 15 rejected mutations/domains. The controls
include missing/reordered atoms, changed weights, wrong variance, zero noise,
wrong sign classes, span equality, source corruption, incomplete/reordered
input coverage, duplicate JSON keys, a false positive resonance gain, and
invalid mark parameters. All read source hashes are embedded in the output.

The exact command is:

```
python3 mathematics/fixed-target-v7/2026-10-27/exclusion_check.py
```

Distinct run records under `runs/fixed-target-v7-20261027/exclusion01/`,
`exclusion02/`, and `exclusion03/` retain snapshots, stdout, stderr, Python
version, input pins and return code. Earlier passing runs precede adding
the scalar barrier and narrow-response-domain checks, respectively.
The final proof is compiled with the installed TeX Live via the bundled
compile helper; its full command, streams, source/PDF/log hashes and render
receipt are retained in `exclusion-build03/`. All four final pages were
visually inspected; this layout check is not mathematical acceptance.

The next useful acquisition target is a proved conditional-span or
nonresonance bound, together with the marked denominator and signed repair
gates, using actual contact/support information. Repeatedly tightening only
an unweighted or weighted moment defect cannot establish that missing edge
for arbitrary laws. Whether the new fixed-target contact inequality can
exclude the rare resonant tail directly remains open here. The existing
confinement proof is a possible route and has not been removed.
