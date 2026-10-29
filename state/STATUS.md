# Current research status — v16, 29 October 2026

Review target: https://github.com/kolodziejek/berry-esseen-certificates/pull/5
Keep draft for author review. No merge, main push, force-push, branch deletion
or upstream change. Original reference:6346fc1b4432bc5982822aa696eb566ed9e1e1ee.
This round starts at published fb9e918bef3b0a932fb44bf1dae8d3e4a589f932.
Remote publication is verified separately; do not infer it from this file.

| Result | Mathematical status | Execution status |
|---|---|---|
| Scalar acquisition from compact standardized law,n>=700,nD<=32.20665378 | Locally derived and independently reviewed |63 constructor gates,24 exact laws/20 budget-eligible;61 independent gates,3 symbolic identities,7 actual-law identities PASS |
| Common amplitude.6 from two contact rays | Conditional on retained fixed-target contact/heat and true predecessor |Both complete rays checked by two separate polynomial derivations PASS |
| Elementary small noise on p[.375,.465],d<=.004,lambda<=.01 | All-law local theorem; independently reviewed |61 constructor gates;88 reviewer gates including40 tensor Bernstein coefficients;44 complete outward actual-law events PASS |
| Unified five-count comparisons, Compact row lambda[.01,.35] | All-law local theorem; independently reviewed |163 constructor gates;83 independent gates,64 product/curvature controls,16 atom cases PASS |
| Full common-strip comparison and acquired exclusion n>=700 | Complete local union; conditional acquired-witness consequence, independently reviewed |Exact normalization/noise/zero/reflection joins PASS |
| Wider right strip n>=200,lambda[.03,.36] | Locally derived; independently included by generic proof |Four endpoints,30 gates,45 actual events and source mutations PASS |
| C4,BASE41,unrestricted finite range,full conjecture | OPEN |No acceptance claimed |

Common local law:Y=B+U,E(U|B)=0,v=p(1-p),s=EU²,lambda=ns,
X=(Y-p)/sqrt(v+s),rho=E|X|³. At n>=700,p[3/8,93/200],
-.6<=U0<=a0,-a1<=U1<=.6,a0+a1<=.004,raw|H|<=1.84,
0<lambda<=.35, the full signed excess is less than -lambda/100.
At zero noise use strict Bernoulli directly. Contact/predecessor are needed
for acquisition, not intrinsic hypotheses of this local theorem.

Selected route:coarse budget/rawH -> scalar geometry -> two contact rays ->
one common support strip -> elementary small noise or unified five-count
comparison -> negative excess. The full tail is summed, not truncated.
Removed from this route:post-entry probability panels, old numerical noise
tables, left/right union, Pinelis/Poisson comparisons and291-cell compound
certificate. All original sources and smaller-index results are preserved.

Still retained:11264-box coarse Fourier entry,2coarse/4signed passes and its
internal100-panel acceptor contract; rawH; general gap-cost/cubic identities;
heat/contact; attainment/reflection; true sharp predecessor; external
structural/binomial theorems; genuine finite base. BASE41 plus least-failure
acquisition only confines a first failure to42..699. It is not an unconditional
cutoff700. A base through699 or independent closure of42..699 remains needed.

Read mathematics/simplification-v16/2026-10-29/README.md and composition.pdf.
Complete new proof notes:acquisition-direct.pdf(4pages),small-common.pdf(5),
unified-comparison.pdf(7);composition.pdf(2);wider-right counts-analytic.pdf(4).
All compiled and all pages inspected. Independent component reviews and
coordinator-review.md record derivations, corrections and final source pins.
These page counts are not the length of a future complete manuscript.

Bounded final replay:
python3 -I -B mathematics/simplification-v16/2026-10-29/run_checks.py NEWID
Final receipt:runs/simplification-v16-20261029/integration01/receipt.json.
All10bounded integration jobs passed with36source pins. The receipt, not
constructor markers alone, records the final integration outcome. No expensive generation, full Fourier replay or Lean
build occurred. Baseline2748entries and all85tracked manuscript files are
preserved. The89-page manuscript is unchanged this round.

Worktree:work/fork_audit_20261027/simplification-v16.
Research branch:research/simplification-v16-20261029.
Integration branch:manuscript/strategy-v4-20261027 in strategy-v4.
Previous four state files are preserved in runs/simplification-v16-20261029/stateBefore01.
