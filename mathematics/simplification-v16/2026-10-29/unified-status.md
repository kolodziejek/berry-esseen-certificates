# One five-count proof, three specializations

Baseline: `fb9e918bef3b0a932fb44bf1dae8d3e4a589f932`.
Branch: `research/unified-v16-20261029`. All outputs are new; inherited
proofs, certificates, the manuscript, and remote branches are untouched.

The local conclusion in `unified-comparison.tex:29` is

\[
\sqrt n\{\Pr(X_1+\cdots+X_n\le H)-\Phi(H/\sqrt n)\}
-C_E E|X|^3<-\lambda/100.
\]

It concerns every actual iid marginal represented by
`Y=B+U`, `E(U|B)=0`, `X=(Y-p)/sqrt(pq+EU²)`, with conditional supports
`U0 in [-A,a0]`, `U1 in [-a1,A]`, `a0+a1<=d`, `lambda=n EU²`, and
the original raw standardized-sum threshold `|H|<=1.84`.

| Row | Exact domain | Mathematical status | Execution status |
|---|---|---|---|
| Selected compact | n≥700, p∈[3/8,93/200], A=3/5, d=1/250, λ∈[1/100,7/20] | Locally derived analytic criterion and checked constants; independent review by root pending | Fresh PASS |
| Extended right | n≥200, p∈[2/5,53/100], A=3/5, d=9/125, λ∈[3/100,9/25] | Same criterion; sharper affine square-root bound extends the v15 row down to .03 | Fresh PASS |
| Retained left | n≥700, p∈[1/3,2/5], A=7/10, d=17/250, λ∈[1/100,8/25] | Same criterion; recovers the v15 scope | Fresh PASS |
| Acquiring these hypotheses for an extremal witness | Coarse entry, attainment, contact and predecessor hypotheses | Separate conditional argument; not proved by this note | Not run here |
| Arbitrary-law theorem / finite base | All iid laws and all n | Not established by this component | Not claimed |

The proof has six pages of mathematics and a seventh page containing the
reference. All seven rendered pages were inspected. `build01` compiled
without warnings, undefined references, or overfull/underfull boxes.
The source SHA-256 is
`2be0dc58973a281accb66cf3c8dffd7209592e68278ef4c0c46805708e374938`.

## What has actually been consolidated

The generic criterion is at `unified-comparison.tex:64`; its four-endpoint
reduction is at line 118. It retains the exact weighted crossing identity
(line 129), kernel minorant, four centered replacements and frozen
characteristic function (line 166), finite binomial weights and the full
summable curvature estimate (line 256), and both signed normal corrections
and actual cubic moment (line 341). The constants are checked at line 399.

| Earlier source | Replacement and reason |
|---|---|
| `mathematics/simplification-v15/2026-10-28/loss-direct.tex:68` and `:114`, `:166` | Unified section 3 gives the same pointwise minorant and four-swap derivation with explicit generic support/variance guards. The frozen sum always has n−1 actual conditional summands. |
| `mathematics/simplification-v15/2026-10-28/right-direct.tex:42`, `:102`, `:181` | Unified sections 4–6 give finite weights, both signed corrections and one concavity identity. The new tangent `sqrt(lambda/q*) <= (5/2)lambda+9/40` permits λ=.03, so the right row no longer needs the v12 outer/compound route between .03 and .075. |
| `mathematics/simplification-v15/2026-10-28/geometry-left.tex:73`, `:159`, `:232` | Identical analytic mechanism with the left constants table. Its weaker cosine coefficient and larger curvature correction are retained explicitly, rather than hidden in a supposedly uniform right-strip bound. |
| `mathematics/simplification-v13/2026-10-28/crossing.tex:112` | The weighted identity is rederived by finite stop-loss summation by parts in unified section 2. No stopped-noise theorem is left as an unexplained input. |
| `mathematics/simplification-v14/2026-10-28/geometry-slack.tex:68` | The summable curvature proof, including quartic tail majorant, adjacent binomial identity and complete infinite tail, is inlined in unified section 4. The geometric budget and restricted-p Bernoulli reserve from that older note are not used. |

Thus these historical component files need not be separate dependencies of
this local comparison. They are preserved, and their other theorems are not
being removed. This consolidation does **not** justify deleting acquisition
certificates or bypassing finite-base obligations. For the selected compact
row, the intended join is a separately proved acquisition theorem, a separate
all-phase comparison for `0<lambda<=.01`, and this note for `.01<=lambda<=.35`.
Zero noise is a separate direct binomial case. The join must also preserve
the reflected-law and raw-threshold hypotheses.

## Fresh evidence

`runs/unified-v16-20261029/check01/receipt.json` records source hashes,
Python/platform versions, exact commands, elapsed times, stderr and return
codes. Both programs use only the Python standard library and reject
optimized execution. No constructor is imported.

* `unified-check.py`: 163 exact rational guards, three completed-square
  polynomial identities, all twelve endpoint comparisons, and eight
  negative controls. The endpoint proof is concavity, not sampling.
* `unified-actual.py`: 36 actual-law cases at every row's lower and upper
  noise endpoints, both conditional variance-allocation endpoints, and
  raw displacements −1/2, 0, 1/2. Integer-prefix conditional convolutions
  verify 180 five-count stop-loss identities and their reserve bound.
  Four further full weighted identities include threshold collisions and
  neighboring thresholds for a common-noise actual marginal.
* `build01`: TeX Live 2025 compilation, clean log, seven inspected PNGs.

The negative controls reject a right cosine coefficient on the left support,
extension to diameter 1, strict inequalities at the zero bump endpoints,
uncentered replacements, a false binomial mass coefficient 4/5, reuse at
n=100, the old right tangent at λ=.03, and the false replacement of the frozen
n−1 summands by n. These are failures of intermediate strengthenings, not
counterexamples to the iid conjecture.

Replay from the worktree root:

```sh
python3 mathematics/simplification-v16/2026-10-29/unified-run.py fresh02
```

Use a new alphanumeric identifier each time; the runner refuses to overwrite
a receipt. For an integrated suite, invoke `unified-check.py` and
`unified-actual.py` directly, with no arguments. Source hashes establish byte
identity only. The mathematical reduction, primary binomial theorem, and
correctness of exact arithmetic semantics remain part of the review.

## External input and remaining limits

The sole non-elementary probability input is Schulz's strict finite-binomial
Berry–Esseen bound for all p and all real thresholds (2016 dissertation,
Theorem 1, printed page 1; URL in the TeX bibliography). The proof uses its
closed-CDF convention at both adjacent integer anchors. Elementary finite
Stirling, Wallis and elementary trigonometric inequalities are used with
explicit remainders or rational enclosures.

This is a constructor deliverable, not an independent review of itself.
Finite-law controls do not establish continuous-domain validity; that comes
from the displayed analytic guards and concavity proof. A full conjecture,
an unconditional cutoff at 700, and the finite base are not asserted.
