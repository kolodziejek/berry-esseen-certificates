# Two quadratic passes suffice for the first actual-gap entry

The shorter variant succeeds: the improved signed K1 cap and quarter constant,
followed by one gap-free circle update, give an actual central gap in every
one of the 24 initial rho cells using only the old quadratic phase price.
The new higher-degree phase-maximization lemma is not a dependency of this
particular two-pass conclusion.

The result remains conditional on the fixed-target contact/transfer identity,
the acquired actual support radius 96/25 and the complete retained LOW/HIGH
Fourier inequalities. It is not the full INITIAL42_R384 acceptance: fourteen
cells still do not satisfy the stronger sufficient D<2 gate, and the final
small defect, conditional noise, phase and probability-panel outputs remain.
No old certificate or source was changed or removed.

## Result and proof

The inputtable proof is
[signed-two-pass-proof/signed-two-pass.tex](signed-two-pass-proof/signed-two-pass.tex).
It can be mapped to the coordinating manuscript's `simple-route.tex`; its
standalone wrapper is [signed-two-pass-proof/main.tex](signed-two-pass-proof/main.tex).
The earlier signed theorem, quarter-constant identity and circle inverse are
used as already established components, not silently strengthened.

For every relevant witness with n>=42 and the stated premises, the two passes
give the following global upper bounds:

| Pass | Raw remainder T | Conserved resource U | Defect D | Cells D<4 | Cells D<2 | Cells with an actual gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 13.2818901598 | 10.9330610254 | 3.9164138937 | 24 | 8 | 23 |
| 2 | 11.5164967977 | 9.9790315907 | 3.5746638454 | 24 | 10 | 24 |

The final weighted bound is nD<=150.1358815051. These decimals are exact
upward-rounded rationals. In each final cell [l,u], the strict margin obeys

```text
(sigma_lower−1)l−d >= 526024602543/1600000000000 > 0,
sigma_lower = 3.162277660 < sqrt(10).
```

That condition proves an actual gap: if zero belonged to the closed support,
every complementary gap would lie on one side of zero and J<=rho. Then
D=(3+sqrt(10))rho−gamma−3J >=(sqrt(10)−1)rho, contradicting the margin.
This proof precedes any use of central-gap moment restrictions. Centering and
positive variance ensure support of both signs, giving positive inner endpoints
A0,B0 once zero is excluded. No quantitative endpoint or noise bound is claimed.

## Order of the two passes

Pass 1 uses the freshly evaluated first-cover Fourier constants, the new
gap-free K1 cap and the rho³/4 constant charge. Its quadratic curvature is
q(t)=tl−g/5. Square completion at the two enclosed CE endpoints gives a
raw bound; the minimum with another already valid raw bound is allowed.

For a raw bound T<N*c_lower*l, the conservation identity gives

```text
e M_c >= c rho−T/n >0,
M_c = c rho−phi(0)D/6,
n(1−e)M_c >= (H²/2)(c_lower*l−T/N) = eta H².
```

Here e=exp(−H²/(2n)); only exp(w)−1>=w is used. Thus the conserved resource
S=(n+H²)a+n phi(0)D/6+n^(3/2)L is bounded by the same raw quadratic with
curvature q+eta. The new raw T is computed before eta and U. U is never
substituted for T in the density license. The proof includes the n+H² excess
coefficient, and retains all nonnegative loss terms.

Pass 2 uses only pass 1's raw and defect bounds. Its density floor comes from
the prior raw bound; its signed gamma floor comes from the circle inverse
using the prior defect. This inverse needs no actual gap. The constant charge
uses the resulting same-law rho−gamma upper bound, and curvature uses the
minimum of both signed density-endpoint products. It then repeats the two
ordinary square completions, computing a new raw bound before its phase price.

The curvature is affine in the formal contact multiplier because both of its
alternatives have the same slope l. Therefore the two multiplier endpoints
cover every intermediate CE before maximizing over H. No gamma or probability
subdivision is added. The program checks exactly 48 cell passes after fresh
first-cover evaluation, retaining every shared closed boundary.

## Exact computation and source contract

The new program is [signed-two-pass-check.py](signed-two-pass-check.py).
It imports the reviewed circle helper and the frozen signed coefficient helper,
and calls the pinned v5 first-cover constructor to recompute its 24 rows.
It does not import `phase_check.py` or execute any dense acquisition stage,
native acceptor, generated certificate suite or archived campaign.

| Input | Exact scope |
| --- | --- |
| `signed-check.py`, SHA256 `c827917d18b241d7e6255b3c15184ca719044cc3b7ffb8c7474ea5482dd7a847` | Reviewed universal signed cap. The original file remains unchanged. |
| `moment_check.py`, SHA256 `c44f789c35198eabb2d6d07a3843437c4fa29e9b85ebf79505a3bb696987513f` | Reviewed gap-free circle inverse; only its helper and pinned base access are used, not its six-update run. |
| v5 `cell_check.py`, SHA256 `6827a67e64cfea5b89d823ffd34821fa942b3c3add702ee9721c89d65f443aa5` | Fresh first-cover rows, literal inputs, rational constants and full primitive Fourier bounds. |
| v5 `cell-sources/kernel.py`, `high_window_core.py` | Previously read pure scalar primitive implementation; full analytic inequalities remain explicit premises. All four source hashes, including unexecuted native-driver references, are recorded. |
| `signed-proof/signed.tex` and `moment.tex` | Universal moment coefficients and actual-law circle derivation. |
| v5 `cell-refinement.md`, phase-price derivation | Old quadratic phase price, rederived in the new proof. |

In the integrated tree, run:

```sh
python3 mathematics/fixed-target-v6/2026-10-27/signed-two-pass-check.py
```

This separate signed worktree keeps the circle files on their author's branch;
the recorded run therefore specifies its reviewed source explicitly:

```sh
python3 mathematics/fixed-target-v6/2026-10-27/signed-two-pass-check.py \
  --moment-source ../moment-coupling-v6/mathematics/fixed-target-v6/2026-10-27/moment_check.py
```

Latest evidence is `runs/fixed-target-v6-20261027/signed-two-pass02/`:
Python 3.9.6, return code 0, empty stderr, source/output hashes and all rational
coefficients at both endpoints of both passes. The earlier run and exact checker
snapshot are preserved. Its 48 numerical row results are unchanged.

Seven controls reject missing, duplicated and reordered cells, a broken shared
endpoint, an unlicensed prior raw bound, a false claim that pass 1 acquired
every actual gap, and the unsupported smaller final target D<3.5. The first
pass's actual-gap failure is retained rather than concealed by the successful
second pass. The standalone proof compiled successfully with the built-in
LaTeX compiler; the combined manuscript will be compiled and visually reviewed
by the coordinating task.

| Item | Mathematical status | Execution status |
| --- | --- | --- |
| Quadratic phase implication and two-pass ordering | Locally derived, with explicit contact/raw premises | Fresh positivity and ordering gates passed |
| All 24 cells have D<4 and an actual central gap after pass 2 | Conditional on the retained initial support and full Fourier estimates | Fresh exact 48-pass result |
| Degree-six phase theorem as an input to this conclusion | Unnecessary in this new two-pass route | Not imported or run |
| Full initial acquisition, final probability panels and local exclusion | Not established | Not run |

The logical simplification is precise: this entry conclusion can use two
ordinary quadratic passes instead of the newer higher-degree phase lemma.
The latter remains a separately reviewed optional stronger one-pass result.
This does not establish that the original dense initialization stages or any
finite-base certificate are unnecessary; their stronger output contracts still
need a complete replacement.
