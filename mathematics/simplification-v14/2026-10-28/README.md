# A direct comparison beyond the small-noise range

The main new result is a five-page proof of the previously missing weighted
comparison for **every law in the acquired right strip, n>=6000, and
.075<=lambda<=.36**. It requires the inward displacement d<=3/n; the last
section derives this from the retained actual-gap geometric budget. This is
a local theorem with explicit hypotheses, not an unconditional cutoff for
the sharp iid Berry–Esseen conjecture.

Read [large-index.pdf](large-index.pdf) first. The argument is short enough
to follow directly; its companion checker verifies39 rational gates, not a
parameter grid. Definitions and every finite remainder are in the proof.

## Why this changes the argument

The v13 crossing identity combines all incoming and outgoing counts of one
actual iid marginal before estimating them. It gives nonnegative kernels g_i
and the exact expression

`Delta_C = -sqrt(n) sum pi_i g_i + sqrt(n) curvature`
`          + phase/normal correction + C(rho_B-rho)`.

Previously the sign of the first term was insufficient. The new proof supplies
its size, by the following finite steps:

1. A bounded-support characteristic-function inequality measures the noise
   of one fixed conditional count. There is no Fourier inversion or
   asymptotic expansion here: only the expectation of exp(2pi i W).
2. Coupling this count to the actual crossing index costs at most13d.
   The selected index is not assumed independent or its noise centered.
   The clipped crossing-age identity includes the bias exactly.
3. Retain21 counts around floor(t). Fourth moments bound the **entire**
   discarded tail by lambda/100. Every retained normalized binomial mass
   is greater than3/4, by finite Stirling with an explicit remainder.
4. The resulting weighted loss exceeds57lambda/400-117/(4n).
   The phase/normal correction is less than5/n, and the signed-curvature
   estimate is explicit. The cubic penalty is favorable. They leave
   `Delta_C<-lambda/200` on the full stated domain.

The small-noise right theorem from v12 already covers0<lambda<=.075.
Together these close the right local comparison at n>=6000 throughout the
acquired noise ceiling. The zero-noise law is Bernoulli and is handled directly.
The probability range is [.4,.53]; nothing here silently extends it to.54.

## Three further deductions

- [loss-closure.pdf](loss-closure.pdf), three pages, proves the sharp
  Berry–Esseen bound for **all n and thresholds** when a Bernoulli variable
  with p in[1/4,3/4] is perturbed by independent centered noise of support
  width at most1/5. The margin is3s/(1000[p(1-p)]^(3/2)). Conditioning uses
  Schulz's binomial theorem; a uniform Taylor replacement is paid for by
  the increase in the third absolute moment. There is no acquisition
  premise or bound on ns. Equal conditional noise laws give precisely
  this subclass. Unequal laws cannot be pooled to invoke the theorem.
- [geometry-slack.pdf](geometry-slack.pdf), four pages, excludes the entire
  acquired left region `1/3<=p<=.4`, `nQ(p)/sqrt(pq)>=24`, with signed excess
  `<-1/(10n)`. A new summable fourth-moment curvature bound preserves the
  reserve in Schulz's middle-p binomial inequality. Consequently an acquired
  contrary witness has n<=2681 when p<=.4; earlier v13 geometry handles
  p<1/3. The sharper subrange limits are given in the note. The quantitative
  binomial reserve is not applied below its published p=1/3 endpoint.
- [counts-pair.pdf](counts-pair.pdf), four pages, combines two neighboring
  crossing kernels exactly. It proves complete central comparisons through
  lambda=.36 for two asymmetric two-point conditional families, for all
  n>=42 with np integer and H=0. It also proves selected-bias caps under
  explicit width hypotheses. These are restricted results, not a theorem
  for general noise or all phases.

The optional [loss-common.pdf](loss-common.pdf) gives an elementary unweighted
common-noise bound and exact counterexamples to a positive gain over the
noiseless phase. It is not needed for `loss-closure.tex`.

## Exactly which computations become unnecessary

| Domain, after its stated premises hold | Replacement | Computations omitted in that domain |
|---|---|---|
| Right strip, n>=6000, .075<=lambda<=.36, d<=3/n | large-index Theorem1 | Parameter/count-tail or Poisson grids for the larger-noise local comparison; only elementary scalar inequalities remain |
| Independent Bernoulli noise, p in[.25,.75], width<=.2 | loss-closure Theorem1 | Every local count/Poisson comparison for this subclass, at every n and threshold |
| Acquired left strip, p in[1/3,.4], nQ/sqrt(pq)>=24 | geometry-slack Theorem1 | All local count-tail work in the excluded region, at every phase and admissible noise |
| The two central asymmetric families | counts-pair Theorem4 | Local incoming-tail certificates for exactly those families and central integer anchors |

These are logical replacement scopes. Existing certificates and proofs are
preserved. The new large-index proof still uses the v13 crossing and signed
curvature lemmas; it does not claim that every count-related idea is removed.

## What remains

General unequal-noise comparisons in the residual intermediate range
42<=n<6000 are open beyond the retained small-noise domains. Geometry now
excludes much of the left range, but not all of it. Independent C4/BASE41,
attainment, reflected-branch conventions, acquisition/contact and the
sharp-predecessor premises remain where previously required. In particular
the retained11264-cell coarse Fourier entry has not been eliminated or rerun.

The finite-base moment-endpoint shortcut refuted in v13 stays refuted.
The new all-n independent-noise theorem does not imply that an optimizer
has independent noise. A narrower remaining domain is not a finite-base proof.

## Evidence and review

Each proof's scope is separate from its executable checks. The all-law
assertions are the finite analytic proofs, not sampled tests or numerical
optimization. The component status files record constructor evidence.

- `large-index-check.py`:39 exact scalar gates and4 rejecting coefficient
  controls. Independent `counts-window-review.md` derives the complete
  window tail and a different uniform binomial lower bound; its checker
  adds27 exact binomial edge controls and2 false-extension controls.
- `geometry-slack-check.py`:28 scalar gates and5 integer-index comparisons.
  `geometry-slack-actual.py`:216 actual-law curvature controls and15 full
  outward-rational signed events, including exact atoms and immediate
  neighbors. Its normal-enclosure helper is explicitly reused and pinned.
- `loss-check.py`:507 checks,40 moment cases,120 separately enumerated
  product/conditional-mixture identities,156 outward-rational CDF events,
  and6 rejecting controls. These do not reprove the external binomial theorem.
- `counts-check.py`:16 algebraic gates,28 actual family cases,68 paired
  identities,2304 hinge points,6 direct-product selected-bias controls and
  3 negative controls, including the closed incoming collision.
- `coordinator-review.md` rederives the independent-noise and paired-family
  proofs; the separate reviewers cover the large-index and geometric proofs.
  Independent large-index review adds40rational gates and150exact product
  controls; independent geometry review adds2638checks and72physical curvature
  cases. All nine bounded integration jobs passed. Source bindings are in
  `reviewed-sources.json` and `runs/simplification-v14-20261028/integration01/`.

The bounded weighted discovery under `weighted01/` is **discovery only**:
52 laws and8978 central events, using exact atom locations but floating
probabilities/normal evaluations. It showed that the old curvature upper
bound can be too large even when the actual signed comparison is negative.
None of that floating output is an acceptance premise.

Reproduce the reviewed bounded checks, without discovery or certificate generation:

```sh
python3 -I -B mathematics/simplification-v14/2026-10-28/run_checks.py NEWID
```

The original baseline6346fc1b4432bc5982822aa696eb566ed9e1e1ee, existing
certificates and manuscript are unchanged. Starting v14 commit is656232e.
The sole review target remains draft PR5 in the user's fork; no merge or
change to upstream/main is part of this work.
