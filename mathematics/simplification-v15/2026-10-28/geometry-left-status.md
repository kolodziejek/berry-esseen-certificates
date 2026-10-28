# Left signed exclusion from five neighboring counts

The completed component is Theorem 1 of `geometry-left.tex` (four pages).
For every integer `n >= 700`, `p in [1/3, 2/5]`, `lambda = n E U² in
[1/100, 8/25]`, `|H| <= 46/25`, and one actual iid marginal `Y = B + U`
with centered conditional noises satisfying

```
-7/10 <= U0 <= a0,   -a1 <= U1 <= 7/10,
a0,a1 >= 0,           a0+a1 <= 17/250,
X = (Y-p)/sqrt(p(1-p)+E U²),  rho = E |X|³,
```

it proves

```
sqrt(n) [P(X1+...+Xn <= H) - Phi(H/sqrt(n))] - C_E rho < -lambda/100.
```

The event is closed, and exact atom thresholds are included. This theorem
itself has no contact, predecessor, attainment, or geometric-budget premise.
Those hypotheses remain ancestors of acquiring its support and threshold
bounds for a putative extremal witness. Reflection is a separate application
with the reflected inputs. No statement about all laws, a finite base, or an
unconditional numerical cutoff follows from this component alone.

| Result | Mathematical status | Execution status |
|---|---|---|
| Full signed left theorem on the stated closed domain | Locally derived, with retained crossing/curvature lemmas and external strict Bernoulli theorem | Fresh PASS: 40 exact scalar gates; independent component review is recorded separately |
| Kernel minorant, four centered replacements, physical variance bounds, two signed normal repairs | Derived explicitly in the proof; no count-independent noise allocation | Fresh PASS: 35 pointwise kernel controls, 12 finite product controls |
| Two quartics on the whole noise interval | Strictly concave by a completed-square identity; all four endpoint values positive | Fresh PASS; smallest endpoint margin is `5442273179742877948871/97819312500000000000000000` |
| Selected actual iid full excesses | Exact finite product probabilities and rational normal enclosures; supplementary checks, not continuum coverage | Fresh PASS: 4 three-point laws, 12 events at `n=700` |
| Removal of the `c sqrt(T)` curvature term | Refuted by a tiny-noise actual law | Fresh expected rejection / exact negative control |
| Replacement of each normalized binomial weight by 1 | Refuted at `n=700,p=.4,j=280` | Fresh expected rejection / exact negative control |
| Cosine lower bound without the conditional width premise | Refuted at the integer displacement 1 | Fresh expected rejection / exact negative control |
| Entire acquired left range at `n>=700` | Conditional composition with retained LEFT-01 and geometry, as described below | Composition reviewed separately; this file does not assert a global cutoff |

## The simplification

The five neighboring omitted-coordinate laws are compared through a compact
smooth sine-square kernel. Regrouping adjacent translates leaves only four
centered replacements, whose cost is proportional to variance rather than
inward displacement. Characteristic-function decay supplies a positive loss,
and only five binomial weights need lower bounds. All remaining crossing
losses are nonnegative. Summable signed curvature and interpolation between
two actual Bernoulli anchors have order `1/n`.

The final noise calculation is two explicitly displayed concave quartics.
The identity

```
W''(lambda) = -(3/10) { z²[(z lambda - 1)² + 1]/4 + 3b²/8 } < 0
```

makes a probability/phase/noise subdivision unnecessary. The error quadratics
are convex. The scalar checker reconstructs this identity and all endpoint
margins with exact rationals. It does not read a fitted certificate or accept
sampled positivity.

## Dependencies and precise removals

1. `mathematics/simplification-v13/2026-10-28/crossing.tex`, especially the
   weighted identity beginning at line 111, supplies the finite iid crossing
   identity. Its separated-support, mesh-endpoint, and atom hypotheses are
   verified in the new proof. It remains an ancestor.
2. `mathematics/simplification-v14/2026-10-28/geometry-slack.tex`, lines 68–134,
   supplies the summable signed-curvature lemma. The new proof states its
   full bound and gives its short derivation; all physical moments belong
   to the same two conditional marginal laws. It remains an ancestor.
3. Schulz, *The optimal Berry–Esseen constant in the binomial case* (2016),
   Theorem 1, printed page 1, supplies the **strict finite-n all-p Bernoulli
   bound** at both integer anchors. The sharper restricted-probability gap
   is not used. Source: <https://d-nb.info/1197702695/34>.
4. The four-replacement mechanism is derived fully in this component and is
   shared with `loss-direct.tex` from v15. Its source is commit
   `f58c774ad9f74c1f7dcbe777278246810547e2b4`, proof SHA-256
   `a63ffae381844c45559f6637fc62ce0312d847109b2fc9cd1c3f0d6257bff0c9`.
5. On the **acquired** strip, v12 `leftcount.tex`, Theorem LEFT-01, handles
   `0 < lambda <= .01` for all `n>=42`; its interval of constants contains
   `C_E`. The external strict Bernoulli theorem covers `lambda=0`.
   V13 `geometry-noise.tex` supplies `lambda < .32` for `p<=.4` and
   `n<=168` for `p<=1/3`, under its own acquisition/budget hypotheses.
   Thus these retained results plus the new theorem leave no acquired left
   comparison at `n>=700`. They do not establish their own acquisition.

Within the stated left theorem domain, an independent finite-count grid,
Poisson-tail count certificate, Fourier comparison, phase split, signed
binomial expansion, geometric budget, and quantitative Bernoulli gap are
unnecessary. This is a new dependency route, not permission to delete their
existing proofs or certificates. Outside this domain, no ancestor is removed.
The right range, the finite indices below 700, BASE41, attainment, and the
contact/predecessor acquisition chain are not discharged here.

## Fresh evidence and reproduction

From the repository root, with assertions enabled:

```
python3 mathematics/simplification-v15/2026-10-28/geometry-left-check.py
python3 mathematics/simplification-v15/2026-10-28/geometry-left-actual.py
```

- `runs/geometry-left-v15-20261028/scalar02/`: fresh 40-gate acceptance bound
  to the final proof. In addition to exact endpoints, it reconstructs the
  global concavity identity, both physical allocation bounds, cosine-domain
  joins, five-count mass, curvature constants and favorable actual cubic
  correction. `scalar01` preserves the prior equivalent concavity check.
- `actual02/`: 35 kernel controls including five exact conditional atom
  collisions and tiny symmetric defects; 12 finite product four-replacement
  checks; 35 independent tiny-trinomial tests of the streaming exact CDF;
  four named three-point iid laws at the probability/noise corner pairs
  `(1/3,.01),(.4,.01),(1/3,.32),(.4,.32)`, with all noise alternately in
  one conditional side. For each law, the exact threshold atom and its
  neighbors at distance `10^-20` give 12 full signed excess checks.
  The minimum lattice spacing verifies that the neighbors cross no other
  atom. The actual CDF sums use integer multinomial probabilities, not a
  count or moment relaxation. All four laws satisfy the full theorem inputs.
- The normal interval helpers are **reused**, openly, from v10
  `actual_law_checks.py`, SHA-256
  `351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07`.
  The code invokes no discovery/main function from that source. The
  trinomial CDF and smooth-kernel controls are new. This is not claimed to
  be an independently implemented normal library.
- `actual01/` preserves a failed interval-precision test: degree-32 cosine
  Taylor enclosures were wider than the variance-scale four-swap margin
  for conditional defects of size `10^-12`. Increasing the rigorous Taylor
  degree to 48 resolved that enclosure issue. No inequality, law, or target
  was weakened or removed. All previously requested controls remain.
- `build01/` preserves a failed first TeX build due to a misplaced math
  delimiter. `build02/` compiles the final source cleanly to four pages.
  All four rendered pages were visually inspected; no clipping, overlap,
  unresolved reference, overfull box or missing symbol was found.
  The final PDF is also `geometry-left.pdf` beside its source.

No Fourier rerun, optimization search, external write, certificate-generation
campaign, main-branch edit, or baseline rewrite occurred. The four large-index
actual laws took about five seconds together on the local interpreter; this
is a bounded sanity check, not an exhaustive finite-index computation.

Final mathematical source SHA-256:
`ca8117614b0a3da379fa622c89befc010f5cbc14cb63d3e683a01b17dd163802`.
Final scalar checker SHA-256:
`8c29a67d659f92a74f0e42e3a5136b95247315cf681eefc98cc64f80c1e53946`.
Final actual-law checker SHA-256:
`e7cc91e69e35f3f7dce2d938108c38f731e9505b0e383fc2679bf69f5dd62c9f`.
