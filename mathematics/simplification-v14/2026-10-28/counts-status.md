# Paired crossing kernels: v14 status

Baseline: `656232ea8d9561a3f47aefa083ead4f6ba4206ca`.
Branch: `research/counts-v14-20261028`.
Scope: new research files only; manuscript, existing certificates, and earlier results are unchanged.

| Result | Mathematical status | Execution status |
|---|---|---|
| Exact sum of two neighboring crossing kernels | Locally derived and checked; independent review pending | Fresh exact PASS |
| Raw quadratic hinge bounds the weighted first incoming count, under the stated hinge domain | Locally derived and checked | Fresh pointwise checks and genuine negative controls PASS |
| One-conditional-sum reserve using the inward gap | Locally derived and checked | Fresh actual-law controls PASS |
| Central adjacent binomial mass exceeds `1/(2 sqrt(n))` on the stated integer-mean domain | Locally proved by adding uniform lattice jitter; no Stirling input | Rational gate PASS |
| Two asymmetric conditional two-point families, `0 < lambda <= .36`, `H=0`, `np` integral | Locally proved; independent review pending | Fresh algebra and actual-law checks PASS |
| Selected-noise biases bounded by inward first moments when both noise widths are below the mesh gap | Locally derived and checked; independently suggested by coordinator | Six fresh exact product checks PASS |
| Full right-panel comparison beyond `.075` | Open | No coverage claim and no grid run |

## Precise new comparison theorem

For `n >= 42`, `p in [.4,.53]`, integer `k=np`, `A=3/5`, and `0 < lambda <= 9/25`, either:

1. `U0` is centered on `{-A, epsilon}`, `U1=0`, `epsilon=lambda/((n-k)A)`; or
2. `U0=0`, `U1` is centered on `{-epsilon,A}`, `epsilon=lambda/(kA)`.

At the raw central threshold `t=k` (`H=0`) and for every penalty `C>=0`, the direct normalized comparison satisfies respectively

- `Delta_C < -1/240`;
- `Delta_C < -(25/48)lambda`.

This is a theorem about actual iid three-point marginals. The first limit is discontinuous at zero noise because the own-count atom approaches the central threshold from above; the statement excludes `lambda=0`. Its strict outgoing event is therefore essential. Both families satisfy the right strip and inward bounds. The theorem is not an assertion for arbitrary conditional laws or arbitrary phases.

## Mechanism and dependency graph

`v13 crossing theorem` -> nonnegative local kernels `g_i` -> pair identity -> weighted loss lower bound.

`v13 signed-curvature lemma` + the paired loss + the new elementary mass bound + same-marginal cubic positivity -> the two central family comparisons.

For the pair, at any legal integer `k` and `u=t-k`,

`g_k+g_(k+1) = u + P(W_k>u) + E(W_(k-1)-u-1)_+ - E[(u-W_(k+1))1{W_(k+1)<=u-1}]`.

All farther incoming counts disappear because their local kernels are nonnegative; they are not deleted from an identity by dropping terms of unknown sign. The retained weighted first count includes its closed collision atom. In the family proof it is bounded directly by binomial factorial moments; no Poisson comparator, parameter box, or exponential enclosure is used.

Source dependencies and hypotheses:

- `mathematics/simplification-v13/2026-10-28/crossing.tex`, SHA-256 `0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec`: independent centered conditional copies; inward separation; upper conditional noise span at most one; raw threshold between the endpoint meshes. Supplies nonnegative local kernels and the exact weighted identity.
- `mathematics/simplification-v13/2026-10-28/counts-tools.tex`, SHA-256 `7e4defcb35a1711fc4104dec49aa03f91e04ef1529418398b1b3f1c1b957bb9b`: finite variances, actual conditional-count variance transport; at `t>=np-q` gives normalized signed curvature at most `lambda/(4pq sqrt(n))`. Our theorem uses `t=np`.

These are mathematical dependencies, not just file hashes. The constructor reads their exact bytes before running its controls; it does not execute inherited Python or cached bytecode.

## Fresh evidence

Reproduce from the worktree root:

```sh
python3 mathematics/simplification-v14/2026-10-28/counts-check.py
```

Final source pins:

- `counts-pair.tex`: `931fb88565922d525726ba264a867e2b0774051a4e56267d9f9d65f3142b01f4`.
- `counts-check.py`: `961cc647fc3cdc00935f70f659c70af0d144a7f3e36efe6930ec3e4b757c0109`.

`runs/counts-v14-20261028/check03/` contains source snapshots, stdout, stderr and a receipt with Python version, return code, measured time and hashes. Fresh PASS: 16 rational algebra gates; 28 actual family cases; 68 paired identities, including two noisy conditional laws and noiseless Bernoulli; 2,304 pointwise hinge checks; six full-product selected-bias checks. Cases include `n=42,50,100`, skew and symmetric probabilities, `mu=1/10000`, and the exact endpoints `mu=2/5,1`. Finite cases check the proof; they do not constitute a continuous-domain certificate.

`runs/counts-v14-20261028/build03/` contains the final clean four-page PDF, compile log, source snapshot and all four page renders. All pages were visually inspected; no overfull/underfull boxes or undefined references were reported. Earlier runs remain preserved as development evidence; the final source pin and final receipts identify the accepted constructor version.

## Negative controls and limitations

- Replacing the incoming closed event by a strict event overstates the exact paired identity by `1/13` in an actual three-summand example.
- Dropping the hinge admissibility condition permits the false pointwise inequality `2 <= 16/9`.
- Capping a weighted incoming expectation at one is invalid in general: centered `Z=+-3` gives `E[Z 1{Z>=1}]=3/2`. Use a raw quadratic-hinge quotient if adapting the existing compound evaluator; its ordinary-tail probability cap is not automatically licensed here.
- The previously refuted single four-moment reserve is not used. The new proof uses the actual binomial rare-jump structure of each conditional sum.
- The two-point-family theorem does not justify removing the general larger-noise count certificates. To do that, one still needs a sufficient paired or full weighted loss for arbitrary acquired conditional laws and all phases.

## Recommended next mathematical step

Preserve the two-kernel identity as the shorter target for general laws. The missing uniform estimate is a lower bound on the paired weighted reserve strong enough to dominate signed curvature and the normal/cubic phase repair. The general selected-bias cap may help reorganize that bound, but it is not a substitute for it. No larger numerical cover is proposed by this component.
