# v15 phase/anchor component

Baseline `2c2c511ca1aecb5840d474608aba7c43d90db79e`; branch `research/counts-v15-20261028`. New files only. No old theorem, manuscript or certificate was edited.

| Result | Mathematical status | Execution status |
|---|---|---|
| Extend the central two-point-family theorem to arbitrary thresholds with `floor(t)` at all positive noise | Refuted by an actual iid three-point law | Fresh exact rational certificate PASS |
| The same counterexample law at the retained shifted anchor | Strict negative comparison proved for every `C>=0` | Fresh exact certificate PASS |
| Retained v11/v12/v14 anchor dependency audit | No retained theorem refuted; anchor rules differ by noise regime | Source-pinned audit complete |
| Curvature bound using actual first absolute moments | Locally derived and checked; independent review pending | 270 exact checks on 45 actual conditional-law cases PASS |
| Uniform arbitrary-phase family extension beyond `.075` | Open in this component | Bounded floating discovery only; no coverage claim |

## Exact obstruction

Use `n=42,p=1/2,A=3/5`, `U0=0`, and centered `U1 in {-epsilon,A}` with `epsilon=1/350000`. Then `lambda=9/250000`. At the closed atom `t=21(1-epsilon)=21-3/50000`, the floor anchor is 20. For every `0<=C<=1`, including the sharp coefficient,

`Delta_C(t,20) > 185046727061827375519549/37666554485145600000000000 > 1/250`.

The same law and threshold satisfy `Delta_C(t,21)<0` for every `C>=0`; the proved upper bound has negative margin `1344372651180417/42953967927296000000`.

The proof bounds the actual CDF by binomial rare-jump events and the Gaussian interval by an integrated quadratic-exponential Taylor bound. No approximate normal CDF enters acceptance. The closed collision is explicit. This is an anchor-comparison counterexample, not a counterexample to Berry--Esseen.

## Dependency propagation

- `mathematics/simplification-v11/2026-10-28/counts-v11.tex`, theorem at lines 10–30: integer anchor with phase `[-34/125,91/125]`.
- `mathematics/simplification-v12/2026-10-28/comparison-union.tex`, theorem and proof at lines 18–54: an integer anchor exists; the right row uses `[-.272,.728]`. Here it is 21.
- `mathematics/simplification-v14/2026-10-28/large-index.tex`, theorem at lines 18–42: floor anchor but `lambda>=.075`. The counterexample is outside that noise domain.
- The v14 small/large-noise join only needs a suitable anchor in each component, because the retained strict Bernoulli theorem bounds every integer anchor. It is valid with these different choices. Any future code or prose identifying them uniformly would be false.

No dependency removal is proposed on the basis of this obstruction. The useful correction is to make anchor existence, anchor selection and phase range explicit at every join.

## Additional proved curvature tool

Let `e_j=E(U_j)+=E(U_j)-`, `ell1=q e0+p e1`, and `c=(np-q-t)+`. The signed-curvature bound can be sharpened to

`sqrt(n) C(t) <= lambda/(4v sqrt(n)) + (c/v) min{sqrt(lambda)/(2sqrt(n+1)), sqrt(n)ell1}`.

The new branch uses `B_j<=E(W_j)+<=(n-j)e0+j e1` and the same exact Bin(n+1,p) difference identity. It preserves the actual conditional laws and their first absolute moments. For either one-noisy two-point family, `ell1=s/(A+epsilon)`, so this remainder is linear in arbitrarily small noise. A comparison theorem still needs to absorb the remaining terms; this lemma alone is not an all-phase result.

## Evidence and reproduction

Run `python3 mathematics/simplification-v15/2026-10-28/counts-phase-check.py`.

`runs/counts-v15-20261028/check01/` contains source snapshots, stdout/stderr, measured time, Python version, source hashes and return code. It freshly reconstructs the actual counterexample CDF, proves both comparison signs with rational bounds, checks the exact atom collision and audited source hashes, and performs 270 exact curvature checks on 45 actual laws. Controls include noiseless Bernoulli, skew probabilities, two noisy conditional laws and a tiny defect.

`build01/` contains the clean three-page PDF, log and page renders; all three pages were visually inspected. There were no overflow or undefined-reference warnings.

A bounded diagnostic checked 48 actual three-point laws with two anchor choices (96 records, 3,832 threshold evaluations). It found floor-anchor failures at tiny noise and no tested failures at moderate noise. Those floating scores are discovery only. `discovery01/` preserves an initial syntax failure; `discovery02/` is the corrected bounded run. No numerical grid or certificate generation was launched.

Further phase construction was stopped at the coordinator's request to prioritize independent review of the new signed all-law argument. No unproved nearest-mean or arbitrary-phase extension is claimed here.
