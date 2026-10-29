This PR retains the manuscript and all earlier acquisition, scalar and executable audits. The latest **v16** work simplifies the selected acquired `n>=700` argument to **one probability/support strip and two analytic noise estimates**. It removes the downstream probability panels, old numerical noise tables, Poisson-tail comparisons and **291-cell compound-Poisson certificate from that route**. The original certificates and smaller-index results are preserved. **The full sharp iid Berry–Esseen conjecture remains open.**

## Mathematical change

For a compact centered variance-one law, the actual weighted defect budget
`nD<=32.20665378`, at `n>=700`, directly implies

```
.375 < p < .465,  theta < .0036,  d < .004,  ell > 1.996,
rho < 1.125,  .066148 < beta < .2527,  lambda < .35.
```

Here `D=(3+sqrt(10))*rho-gamma-3J` uses the actual support-gap sum. The proof acquires its own central gap and sign probability; it assumes no exported probability panel or numerical support radius. For an attained nonnegative fixed-target witness with the true sharp predecessor, **two whole contact rays** then give conditional amplitude `.6` across the entire interval.

Write `Y=B+U`, `E(U|B)=0`, `v=p(1-p)`, `s=EU²`, `lambda=ns`, and `X=(Y-p)/sqrt(v+s)`. The new full local comparison proves

`sqrt(n){P(X1+...+Xn<=H)-Phi(H/sqrt(n))}-C_E E|X|³ < -lambda/100`

under `n>=700`, `p in [3/8,93/200]`, `-.6<=U0<=a0`, `-a1<=U1<=.6`, `a0+a1<=.004`, `0<lambda<=.35`, and raw `|H|<=1.84`. All phases and threshold atoms are included. The comparison itself requires no acquisition, contact or predecessor premise; these enter only to obtain its hypotheses for a witness.

- **Small noise, `0<lambda<=.01`:** one shifted count, a strict-event quartic minorant, finite Stirling and complete fourth-moment tails. The proof retains the actual linear growth of conditional variance with count displacement. No Pinelis inequality, Poisson comparison or parameter certificate is used.
- **Larger noise, `.01<=lambda<=.35`:** one generic five-count proof supplies the exact weighted crossing identity, four centered replacements, full curvature tail, both normal signs and favorable actual cubic correction. Four rational endpoints of two concave quartics finish the Compact row.
- **Zero noise:** the law is Bernoulli, so Schulz's strict finite-binomial theorem applies directly. No limiting inference is used.

The same generic argument also retains the wider Left row and extends the wider Right row down from `lambda=.075` to `.03` at `n>=200`. A better square-root tangent alone achieves that extension. Its wider right union still uses the older scalar Poisson estimate below `.03`; the selected compact `n>=700` route does not.

Read `mathematics/simplification-v16/2026-10-29/README.md` and `composition.pdf` first. Complete component proofs are `acquisition-direct.pdf` (4 pages), `small-common.pdf` (5 pages) and `unified-comparison.pdf` (7 pages), with a two-page exact composition. These are component lengths, not a claimed length for the eventual paper.

## Dependency removals and retained boundary

`acquisition-audit.md` gives baseline source locations, exact hypotheses and reasons for each removal. Direct scalar acquisition replaces v10 post-entry numerical localization and its 30-panel export. Two contact rays replace thirteen right and fifteen left support checks. The general same-marginal cubic/AM–GM budget remains, while its old numerical noise tables and 139 Bernstein coefficients are unnecessary on the narrowed interval. The new common-strip comparison removes the split at `p=.4`, v11/v12 small-noise branches, the separate outer-phase comparison and the 291-cell negative-inner subtree from the selected route.

Still retained: the **11264-box coarse Fourier entry**, both coarse and all four signed entry passes, the old acceptor's internal 100-panel cover contract, raw-threshold acquisition, general gap-cost/cubic identities, heat/contact lemma, fixed-target attainment/reflection, true sharp predecessor, and external structural/binomial theorems. This round does not re-prove or replay that whole foundation. Removing downstream panels does not license erasing panels internal to the existing entry certificate.

**This is not an unconditional cutoff at 700.** With a genuine BASE41 and the retained implications at a least failure, any first failure lies in 42–699. An unresolved earlier failure can invalidate the predecessor premise at a later row. A genuine base through 699 or a separate argument closing that range remains necessary. Independent C4, BASE41 and the full conjecture are not inferred from historical success logs.

Reflection selects the oriented positive witness before acquisition. It neither preserves the signed D budget nor the new p interval. The composition includes the closed-CDF atom inequality and the exact pointwise normalization `lambda=n theta/ell²`.

## Checks and independent review

**All ten jobs passed in the final bounded replay**, recorded in `runs/simplification-v16-20261029/integration01/receipt.json`, with exact commands, versions, source hashes, stdout/stderr and return codes. It runs the constructors, separate reviewers, actual-law controls and preservation check; it does not launch discovery or certificate generation.

- Acquisition constructor: **63 exact gates**, **24 actual laws** in exact Q(sqrt(10)), of which 20 meet the budget, plus three negative controls.
- Unified constructor: **163 exact scalar gates**, eight negative controls, **180 selected-count identities** from 36 actual-law cases, and four complete weighted identities at atoms and neighboring thresholds.
- Independent unified review: **83 scalar/interface checks**, **64 weighted product identities**, **64 full curvature controls**, including 16 exact atom cases. It reconstructs the quartics by rational interpolation without importing the constructor.
- Small-noise constructor: **61 exact gates**. Independent review checks **88 gates**, including all **40 coefficients of the original tensor Bernstein polynomial**, through a different reduction. **44 complete outward-rational events** on four n700/701 actual iid laws include tiny noise, collisions and both legal phase-boundary anchors.
- Acquisition and composition have a separate source-bound review: **61 rational gates, three symbolic identities and seven actual-law gap-cost identities**, including the unsimplified cost, monotonicity before discarding noise, same-law cubic allocation, two ray continuations, exact local-domain joins and first-failure logic. The coordinator independently read every accepted proof.
- The wider right extension has its own four rational endpoints, source-mutation controls and 45 actual signed events from five laws; the generic proof independently includes its row. The final bounded suite rechecks its scalars, without needlessly repeating that separate actual-law campaign.
- All final proof notes compiled and their pages were visually inspected. A test comment about odd-fold noise atoms and one overflowing prose phrase were corrected; no theorem statement was weakened.

Negative controls show why contact cannot be dropped from the support conclusion, why signed acquisition cannot be copied under reflection, and why the positive-phase fourth-moment denominator cannot be omitted. These are intermediate-claim counterexamples, not counterexamples to Berry–Esseen. Actual-law controls supplement the continuous proofs. The small-noise event regression reuses the explicitly pinned outward-normal helper; this is not described as independent arithmetic verification.

Original baseline `6346fc1b4432bc5982822aa696eb566ed9e1e1ee` is preserved: all **2748 entries** retain their tree/index bindings, with 182 materialized byte checks and 2566 sparse bindings. All **85 tracked manuscript files** remain unchanged. No expensive generation, full Fourier replay or Lean build was performed.

## Review and merge recommendation

Keep this PR **draft for author review**. Independent reviews found **no unresolved blocker within the stated scopes**. The new proof components have separate internal independent reviews and an exact composition with explicit retained inputs. This is ready to be considered for incorporation into the manuscript as a delimited simplification; it is not a completed proof of the conjecture. Human review of the analytic reductions and remaining assumptions is still needed before presenting it as such. No merge is requested or performed.

```sh
python3 -I -B mathematics/simplification-v16/2026-10-29/run_checks.py NEWID
```

## Earlier work retained

The 89-page manuscript remains at `manuscript/arxiv-v1/main.pdf`, by **Bartosz Kołodziejek and Kacper Rodziewicz**, with blank affiliations and explicit AI-assistance disclosure. This mathematical round has not rewritten it.

Earlier acquisition, scalar and executable audits, the finite-base localization without a base claim, the source-binding/bytecode repair, v14 subclass results, v15 five-count improvements and its floor-anchor counterexample remain with their original scopes and evidence. The v16 notes replace selected dependency edges; they do not rewrite those historical reports or remove smaller-index proof objects.

Work is confined to **kolodziejek/berry-esseen-certificates**. No main push, force-push, branch deletion, merge or upstream modification.
