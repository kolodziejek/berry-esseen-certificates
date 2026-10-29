# Thirty-panel elementary moment entry

The new conditional result excludes probability panels 24 and 53 of the accepted fixed-target v7 entry. It retains all 28 panels numbered 25–52 and proves the following outward bounds:

| Quantity | Exact upper/lower bound |
|---|---:|
| Probability | 1/4 ≤ p ≤ 53/100 |
| Total conditional variance theta | ≤ 297212757/5000000000 |
| Inward displacement delta | ≤ 719539227/10000000000 |
| Third absolute moment rho | ≤ 2909457709/2000000000 |
| Weighted count noise lambda=n theta/ell² | ≤ 6314459997/10000000000 |
| Scale ell | 78282527/40000000 ≤ ell ≤ 1443375673/625000000 |

These are bounds for the same actual law and its actual central gap. The global acquired support radius 157/50 is the maximum among all surviving final rho rows in the accepted v7 object. No support certificate is regenerated.

## Status and dependencies

| Result | Mathematical status | Execution status |
|---|---|---|
| Binary-cost subtraction and ordered moment iteration | Locally derived conditional consequence of the retained weighted gap inequality and v7 acquisition | Fresh exact PASS on all 30 panels, eight updates each |
| Two endpoint-panel exclusions | Conditional whole-closed-panel deductions; strictly negative residual required | Fresh PASS; both occur in update 1 |
| General signed beta bound, including p>1/2 | Locally derived from the two conditional noise masses | Six actual-law controls; explicit false-shortcut counterexample |
| Coherent rho cap and joint displacement/noise budget | Locally derived, retaining nD rather than replacing it by an unweighted claim | Fresh exact PASS |
| Sigma=3/5 support strips | Conditional on fixed-target contact and Gaussian heat/derivative inequalities | Both rays pass on panels 40–52; positive boundary sufficient estimate fails on 25–39 |
| Half-amplitude confinement, LOW/HIGH count comparison, finite base | Unresolved by this calculation | Not run |

The proof is [moment-entry-v8-proof/main.tex](moment-entry-v8-proof/main.tex). The checker is [moment-entry-v8.py](moment-entry-v8.py), written independently without importing a Fourier kernel, native checker, or the other v8 constructor. The exact accepted input is [moment-entry-v8-input.json](moment-entry-v8-input.json). Source SHA256 values are in [moment-entry-v8-sources.json](moment-entry-v8-sources.json).

Retained source interfaces:

- `mathematics/fixed-target-v5/2026-10-27/response-proof/response.tex:89–115`: common noise-measure budget, with binary floor B0, inward-gap cost E0, and separate positive/negative weights. Its outer-gap analytic input remains an explicit premise.
- `mathematics/fixed-target-v5/2026-10-27/entry.tex:64–155`: closed-support fixed-target contact, predecessor C_(n−1)≤c, nonnegative excess, uniform heat remainder, and whole-ray derivative bound. The new boundary estimate uses the absolute quartic term, so it needs t>sqrt(3), not the source's stronger positivity condition on its quartic coefficient.
- The source object is named `INITIAL42_FIXED_TARGET_COARSE_V7`, SHA256 `61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae`. Its acquisition and acceptance were reviewed separately. This new check does not replay or prove that analytic ancestry. All 100 probability panels are read; precisely 30 nonempty panels enter this calculation, including p>1/2.

The constant sqrt(10) is enclosed by 3.162277660 and 3.162277661, checked by squaring. All roots, lower prices, and upper budgets are directed with integers/Fraction; updates round outward to 10^-10. Only already proved bounds enter the next update. Eight iterations are a finite composition, not a fixed-point assumption.

## What is new in the deduction

The previous all-panel ceilings can be contracted without a dense characteristic-function evaluation. Before charging noise or gap displacement, pay the nonnegative binary asymmetry floor

`B0=(6+2sqrt(10)) (1−theta)^(3/2) (p−p*)²/sqrt(p(1−p))`, `p*=(4−sqrt(10))/2`.

The exact remaining budget pays both noise signs with their own weights. The rho export maximizes a single piecewise affine expression in the same theta, instead of adding separately maximized deterministic and noisy moments. The final joint inequality comes from multiplying the actual budget by n and using n≥42 and nD≤42D_I. An arbitrary unweighted theta bound is never multiplied by 42.

For p∈[l,u], the valid orientation-independent signed-moment interval is

`1−2u−2(1−u)Theta ≤ beta ≤ 1−2l+2lTheta`.

Replacing the upper coefficient 2l by 1 is licensed only when l≤1/2. The standardized three-point law with atom/mass pairs `(-26/25,12/25)`, `(1/2,52/6977)`, `(7226/7475,89401/174425)` has p=13/25, theta=1/625, beta=−599/15625. Its beta exceeds `1−2p+theta` by 1/15625. This refutes that shortcut outside its domain; it is not a Berry–Esseen counterexample.

## Panel outcomes

Panel i denotes the closed interval [i/100,(i+1)/100]. The following decimals are display-only approximations; exact rational values and every update appear in the JSON run output. All negative support rays pass on surviving panels. The last column reports the positive-boundary test, so “positive fails” does not assert failure of the true strip theorem.

| Panel | theta upper | delta upper | rho upper | lambda upper | sigma=.6 strip |
|---|---:|---:|---:|---:|---|
| 24 | excluded | — | — | — | — |
| 25 | 0.00593564 | 0.00466036 | 1.45472885 | 0.04825114 | positive fails |
| 26 | 0.01581950 | 0.01291514 | 1.43358111 | 0.13306193 | positive fails |
| 27 | 0.02426863 | 0.02057998 | 1.41343888 | 0.21059831 | positive fails |
| 28 | 0.03159515 | 0.02780186 | 1.39456816 | 0.28214288 | positive fails |
| 29 | 0.03788987 | 0.03456256 | 1.37684834 | 0.34734967 | positive fails |
| 30 | 0.04323494 | 0.04084458 | 1.36016992 | 0.40596593 | positive fails |
| 31 | 0.04770509 | 0.04663139 | 1.34443249 | 0.45782703 | positive fails |
| 32 | 0.05136870 | 0.05190764 | 1.32954308 | 0.50285078 | positive fails |
| 33 | 0.05428861 | 0.05665937 | 1.31541503 | 0.54103113 | positive fails |
| 34 | 0.05652287 | 0.06087421 | 1.30196700 | 0.57243142 | positive fails |
| 35 | 0.05792905 | 0.06431990 | 1.28866809 | 0.59503775 | positive fails |
| 36 | 0.05895334 | 0.06742832 | 1.27635042 | 0.61332240 | positive fails |
| 37 | 0.05944255 | 0.06997450 | 1.26449548 | 0.62536946 | positive fails |
| 38 | 0.05944003 | 0.07195392 | 1.25303853 | 0.63144600 | positive fails |
| 39 | 0.05707686 | 0.07092997 | 1.23691574 | 0.61016082 | positive fails |
| 40 | 0.05625929 | 0.07176770 | 1.22604650 | 0.60565694 | both pass |
| 41 | 0.05302606 | 0.06720605 | 1.20496355 | 0.57289879 | both pass |
| 42 | 0.05425528 | 0.06753595 | 1.19530463 | 0.59055550 | both pass |
| 43 | 0.05153872 | 0.06278528 | 1.17618858 | 0.56234656 | both pass |
| 44 | 0.05205117 | 0.06220318 | 1.16718073 | 0.57078180 | both pass |
| 45 | 0.04772561 | 0.05572418 | 1.14667578 | 0.52286583 | both pass |
| 46 | 0.04344158 | 0.04955258 | 1.12781114 | 0.47513506 | both pass |
| 47 | 0.04144566 | 0.04625449 | 1.11638191 | 0.45326920 | both pass |
| 48 | 0.03308273 | 0.03595481 | 1.09003554 | 0.35911007 | both pass |
| 49 | 0.02695164 | 0.02856707 | 1.07105640 | 0.29083058 | both pass |
| 50 | 0.01748915 | 0.01804563 | 1.04594903 | 0.18690490 | both pass |
| 51 | 0.01091962 | 0.01099311 | 1.03048477 | 0.11587547 | both pass |
| 52 | 0.00377714 | 0.00370818 | 1.01504531 | 0.03974667 | both pass |
| 53 | excluded | — | — | — | — |

On panels 40–52, the two whole-ray estimates imply `Y=X/ell+p` belongs to `(-3/5,8/5)`. Panels 25–39 have a nonnegative upper estimate at the positive boundary. No strip conclusion is drawn there, and no half-amplitude confinement is established anywhere by this artifact.

There is a concrete obstruction to excluding every remaining panel using only these necessary moment constraints: standardized Bernoulli p=13/50 lies in panel 25, has theta=delta=lambda=0, beta=12/25, rho=769/(25sqrt(481)), and D=(769sqrt(10)−2043)/(25sqrt(481)). Directed exact checks place it within the retained panel's D, rho and beta ceilings. This is a real law, not an optimizer of independent moment bounds. It is not asserted to have nonnegative excess; that missing analytic information could still exclude it.

## Reproduction and controls

Run, from the repository root:

```sh
python3 mathematics/fixed-target-v8/2026-10-28/moment-entry-v8.py
```

The current source is pinned by `runs/fixed-target-v8-20261028/moment03/receipt.json`; stdout, empty stderr, Python version, return code, and a source snapshot accompany it. Earlier distinct moment01/moment02 runs preserve the discovery progression and are not overwritten. The final run is PASS with return code 0, no optimization flags, no native/Fourier imports, and no sampled continuous-domain positivity claim.

Six exact-law controls cover symmetric/skew Bernoulli, reflection, a symmetric four-point law, tiny distant atoms, and the p=.52 one-sided-noise law. Seven deliberately false controls reject: wrong pq maximum across 1/2, wrong above-half beta shortcut, missing N in weighted count noise, altered input bytes, assertion that all panels are excluded, wrong reflected beta sign, and assertion that every support strip passes. These are bounded mathematical/code controls, not a replacement for a full mutation-audited certificate acceptance format.

The three-page proof compiles with the desktop compiler and installed TeX Live; the final TeX log has no warnings or over/underfull boxes. Every rendered page was visually inspected. Compilation and visual layout do not discharge the retained analytic inputs.

## Remaining work and possible savings

This artifact could replace repeated moment-acquisition calculations on the 30-panel fixed-target entry only after its interface is independently reviewed and integrated under a new named contract. It does not by itself remove any existing certificate or invalidate its need. The 15 failed positive-strip bounds, subsequent confinement, local count exclusion, and BASE41 remain separate obligations. No certificate, source baseline, historical log, or theorem statement was changed.

An independent bounded source review by the computation agent re-derived the ordered binary-floor update, weighted joint residual, coherent rho turnover, and both-orientation beta endpoints and found no blocker. That review did not replay these 30 outputs or re-establish the accepted entry ancestry.
