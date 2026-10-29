# Five counts replace the larger-noise transport argument

The new local comparison is shorter and has substantially weaker hypotheses.
For every actual iid law in the stated conditional support strips, it bounds
the full positive signed Berry–Esseen excess at every raw threshold
`|H|<=1.84`. The right result starts at n=200; the left result starts at n=700.
Both include all phases and threshold atoms. Neither local result needs the
geometric budget or an inward displacement of order 1/n.

This does not prove the sharp iid conjecture or an unconditional cutoff at
700. The exact acquisition and first-failure qualifications are below.

## The two comparison theorems

Use one actual marginal `Y=B+U`, with `B` Bernoulli(p) and `E(U|B)=0`.
Set `v=p(1-p)`, `s=EU²`, `lambda=ns`, `X=(Y-p)/sqrt(v+s)` and
`rho=E|X|³`. The new conclusion in both rows is

`sqrt(n){P(X1+...+Xn<=H)-Phi(H/sqrt(n))}-C_E rho < -lambda/100`.

| Theorem | Index | Probability | Conditional supports | Inward sum | Noise |
|---|---|---|---|---|---|
| [Right](right-direct.pdf) | n>=200 | [.4,.53] | -.6<=U0<=a0; -a1<=U1<=.6 | a0+a1<=.072 | [.075,.36] |
| [Left](geometry-left.pdf) | n>=700 | [1/3,.4] | -.7<=U0<=a0; -a1<=U1<=.7 | a0+a1<=.068 | [.01,.32] |

The conditional laws are centered and `a0,a1>=0`. The thresholds in this table
are raw thresholds for the sum of standardized summands, not standardized
thresholds for the sum itself. The normal argument is `H/sqrt(n)`.

The retained v12 small-noise theorems fill the remaining positive noise in
each row. They may choose a different integer Bernoulli anchor. Zero noise
is handled directly by Schulz's strict all-p binomial theorem. Consequently
the right local strip is closed for every `0<=lambda<=.36` at n>=200, and
the left for every `0<=lambda<=.32` at n>=700. This full-noise union has a
strict conclusion, without asserting the same quantitative margin in every
small-noise component.

## Why the proof is simpler

The exact crossing identity writes the CDF as a linear interpolation of two
binomial CDF values, plus a signed curvature correction, minus nonnegative
crossing losses. Earlier we transported a selected crossing count to a fixed
count. That introduced a displacement error and required a larger count
window. Instead, we put a smooth function directly below the crossing kernel.

The function is `B(x)=sin²(pi x)` on `[0,1]`, and zero elsewhere. Its first
derivative is globally Lipschitz. The actual crossing kernel dominates
`(2/5)B`. For five neighboring counts, group adjacent translated bumps before
comparing conditional sums. Only four centered replacements are needed.
Centering removes the first-order Taylor term, so the cost is proportional
to the variance, not to the inward displacement.

After freezing the middle count, the infinite translated bumps sum to a
periodic sine square. A single characteristic-function estimate gives its
mean. The entire missing part of the five-count window is bounded by `EV⁴/16`.
Five finite Stirling lower bounds restore the binomial weights. The retained
summable-curvature lemma and a signed normal interpolation bound pay for the
remaining errors. The increase of the actual third absolute moment is favorable.

The final noise calculation consists of two quartic polynomials in each
probability range, one for each sign of H. Concavity follows from the identity

`W''(lambda) = -r { z²[(z lambda-1)²+1]/4 + 3b²/8 } < 0`,

and convexity of the error polynomial. Four rational endpoint comparisons
complete each range. There is no subdivision or fitted numerical certificate
in these larger-noise comparisons. The complete arguments are in
[loss-direct.pdf](loss-direct.pdf), [right-direct.pdf](right-direct.pdf), and
[geometry-left.pdf](geometry-left.pdf), four pages each. These are component
lengths; the retained ancestors still have to be read for the complete proof.

## Exact dependency removals

| Earlier dependency | New replacement and reason | Scope of removal |
|---|---|---|
| Selected-count transport and its additive inward-displacement cost | `loss-direct.tex`, Sections 1–3: the compact kernel minorant and four centered replacements estimate the actual five losses directly | New larger-noise right row; the left adaptation derives its own constants |
| The 21-count lower-weight window and its old count-tail estimate | Five explicit binomial masses; the omitted bump translates are bounded in one step by a fourth moment | New larger-noise rows only |
| `d<=3/n` and its geometric derivation inside the v14 right comparison | All replacement costs are in variance; only the fixed strip and inward cap occur in `right-direct.tex` | Right n>=200, lambda>=.075; geometry is still used to acquire the noise ceiling |
| Sharper middle-p binomial reserve | Both anchors use Schulz's all-p theorem; the five-count loss pays for the finite corrections | New larger-noise rows; the older geometric-region theorem remains useful below n=700 |
| A common floor anchor across all noise regimes | Full signed excess in the new rows, and existence of a suitable shifted anchor in the old small-noise rows | The join, not the individual old theorem statements |

The v12 negative-inner 291-cell certificate remains an ancestor of the right
small-noise union. The retained 11264-cell coarse Fourier entry, support
acquisition, actual-gap geometry, attainment/reflection, sharp predecessor,
and an independently established finite base also remain. No existing proof,
certificate, manifest or success marker is deleted or weakened.

## What the union establishes about a first failure

The retained geometric theorem gives noise ceilings `.36` globally and `.32`
on the left. It excludes p<=1/3 when n>=169. The high-probability end can
either use the retained acquisition panels or the independently checked
geometric exclusion of p>=.53 when n>=106. Thus every acquired nonnegative
signed witness at n>=700 meets one of the two local unions and is excluded.

This is a conditional acquired-witness theorem. If genuine BASE41 and the
named attainment/reflection/acquisition implications hold at a least failing
index, any first failure must lie in 42,...,699. BASE41 alone does not give an
unconditional tail theorem: an earlier unresolved failure could invalidate
the sharp-predecessor premise at a later row. Closing 42–699, or a genuine
base through 699, is still required for that least-failure route.

[join-review.md](join-review.md) states the local theorem, acquired-witness
theorem and first-failure corollary separately, with exact source locations
and hypotheses. Reflected CDFs are handled by the closed-event inequality;
the reflected marginal must have its own acquisition. No equality at atoms
or automatic reflection of the probability strip is assumed.

## A useful counterexample

[counts-phase.pdf](counts-phase.pdf) proves that always choosing floor(t) is
false at tiny noise. For an actual three-point law at n=42 and p=1/2, an
arbitrarily small downward shift of a common atom changes the floor anchor
from 21 to 20. The comparison is strictly positive at 20 and strictly negative
at 21. The retained shifted-anchor theorem chooses 21, so it is unaffected.
This is a counterexample to an intermediate proposal, not to Berry–Esseen.

The same note proves an optional curvature bound using the first absolute
moments of the actual conditional noises. It is not needed for the new
n=200/700 comparisons. A previous n=1000 transport candidate was left on its
separate branch; only its 40 scalar gates had been checked, so it is not an
accepted dependency or result in this package.

## Review and reproduction

| Item | Mathematical status | Execution evidence |
|---|---|---|
| Five-count reserve | Locally derived; independent coordinator and component review | 519 constructor checks, including 97 actual cases and 5 rejecting controls |
| Right signed comparison | Locally derived; separate independent analytic review | 32 scalar gates; 45 outward-rational full CDF events from 5 actual iid laws |
| Left signed comparison | Locally derived; independent coordinator derivation | Exact scalar/concavity/endpoints; 35 kernel tests, 12 product swaps, 35 independent trinomial smoke checks, 12 full CDF events from 4 actual iid laws |
| Domain union | Independently derived conditional composition | 240 checks, 28 phase/noise strata, 12 actual normalizations and 17 rejecting controls |
| Floor-anchor extension | Refuted; shifted comparison proved at the same law and threshold | Exact rational counterexample; 270 optional curvature checks on 45 actual cases |
| C4, BASE41, unrestricted finite range and global conjecture | Open | No acceptance claimed |

The independent right review rebuilds the quartics by rational interpolation,
verifies all endpoint margins and the global concavity identity, and checks
the kernel and centered replacements with a separately written outward
trigonometric evaluator. It also exhibits actual-law failures of omitting
the replacement cost. The coordinator separately reviews the left adaptation.
Reports and source bindings are included alongside the proofs.

The final integration runner executes only the new bounded acceptance and
review checks, plus byte-preservation checks. It records versions, commands,
input hashes, stdout/stderr and return codes under a fresh run identifier:

```sh
python3 -I -B mathematics/simplification-v15/2026-10-28/run_checks.py NEWID
```

The actual-law controls supplement the proofs; they are not continuous-domain
coverage. Some normal enclosures reuse a pinned older helper, explicitly
disclosed. Historical and failed runs are preserved. No full Fourier replay,
Lean build or expensive certificate-generation campaign was performed.

Work is confined to the user's fork and existing draft PR5. The original
baseline is `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`; this round starts
at `2c2c511ca1aecb5840d474608aba7c43d90db79e`. The manuscript remains unchanged.
