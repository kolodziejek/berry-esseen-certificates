# Finite analytic appendix: coverage and proof boundary

Date: 2026-10-27. Worktree: `manuscript-finite`, branch `manuscript/finite-20261027`, starting head `8989ba054eda36f63e469832f1e00f7e6a7a9084`. This is a typesetting and dependency-preservation contribution, not independent verification of every inherited analytic assertion. The author previously constructed computational/local-cover reports; this contribution is not described as independent review of those reports.

The deliverable is `manuscript/arxiv-v1/appendices/finite-analysis.tex`, with no preamble and only `ms:finite:*` labels. It contains full continuous derivations for the included count and finite-index reductions, and explicit conditions for numerical acceptance and analytical inputs supplied elsewhere. In particular, it proves no BASE41 predicate and no universal finite-base reducer.

## Status

| Result | Mathematical status | Execution status |
|---|---|---|
| S4 common-law count representation and analytic majorants | Supplied analytic proofs retained, with exact zero-noise, atom, support and common-moment scope; not independently re-proved in this typesetting task | No count program run |
| N1 cubic-dual implication | Full elementary implication from the stated whole-line dual cover; no existence/completion assertion for that cover | Native 150-cell acceptance not run |
| G2 and G3 | Supplied attainment/contact/support and majorant-expectation derivations; final bounds conditional on exact complete positivity covers | Native certificates not run |
| ROOT4 | Supplied analytic candidate retained, including common defect measure, physical smoothing/interpolation, all thresholds and canonical cover; final bound explicitly conditional on G3 and complete bounded-law certificate | No ROOT4 certificate run |
| C5 | Conditional composition and full gap-free comparison proof; quantitative support, Fourier, resource and surviving count coverage remain conditions | No fifth-index campaign run |
| A3–A11 scalar refinements | Mathematical derivations converted to ordinary TeX, with explicit hypotheses and the signed/noise/domain caveats; no claimed independent review of all premises | No numerical consumers run |
| A12–A13 B1 interface | Conditional 55-resource/115-integral cover at literal actual indices 26–30; pointwise sine/Fourier input remains separate | No quadrature or native adapter run |
| A14–A18 floor-index interpretation | Conditional finite saved-sequence induction, preserving weighted physical defect and literal index domains; source implementation applicability remains an input | No inherited producer, binder or local comparison run |
| Standalone typesetting | Formatting, labels and reference syntax checked; this is not mathematical acceptance | Fresh TeX Live compile PASS; 50 pages; no undefined references or overfull/underfull boxes; all 50 pages rendered |

## Immutable source identification

The source files are unchanged against the reference commit `6346fc1b4432bc5982822aa696eb566ed9e1e1ee` (the scoped `git diff` is empty):

- `paper/analytic-supplement.txt`, SHA256 `dad4a3558b01bda4acfdfc9120a50ecbcd7a6f2389886ba3ce72a6602ec39018`.
- `paper/main.tex`, SHA256 `1bc15cf4823ea58666d1e7cae8636b3f2b90fbd622f5ab04cbe61cd8a6b92b67`.

No source coefficient, certificate, manifest, success marker, existing analytic statement, reference/history file or production runner was edited. No repository outside the fork was changed.

## Exact source coverage

Line numbers below are physical lines in the current immutable source, not its embedded historical manuscript line numbers. Output anchors are stable labels; current output starting lines are included for review.

| Source | Output start / anchor | Retained mathematical content and scope |
|---|---|---|
| S4, supplement 3907–4630 | 69, `ms:finite:countcore:sec` | Entire common-law conditional count calculation: conditional independence, variance allocation, signed moment identities, genuine-gap defect, quartic strict outgoing minorant, one-sided MGF and tangent, stop-loss comparison, joint cubic polygon, convex phase coefficients, positive-denominator vertex ratio, original roots and finite closed forest. No relaxation point is assumed to be an iid law. |
| main 525–541 | 796, `ms:finite:n1` | Whole-real-line cubic dual, expectation cancellation, 150-cell-format conditional cover, both threshold tails and closed-CDF reflection with atoms. |
| S6, supplement 4666–4955 | 830, `ms:finite:n2:section` | Contrary-witness compactness uses uniform integrability only of the first two moments, atom-safe contact, support inside (-6,6), same-law tensor expectation, 70-row/1050-coefficient format, whole quadratic moment domain, quadrant/triangle Bernstein proof, scalar domain rejection and Gaussian series. |
| S6, supplement 4956–5331 | 1119, `ms:finite:n3:section` | Three-summand contact/support, 59-feature symmetric tensor, independence-null fourth/fifth-moment features, exact expectation without invented higher-moment parameters, ordered sign boxes, closed event-plane affine Bernstein test, full moment-domain cover and tails. Constant explicitly written as 59/250. |
| S6, supplement 5332–6023 | 1492, `ms:finite:n4all:section` | Canonical three-point reference; one defect measure at every frequency; finite-index localization consuming G3; exact moments; Hermite response; quartic remainder; Prawitz regularization and midpoint curvature; physical smooth interpolation rather than CDF interpolation; signed ratio denominators; complete 260-parent cover and both reflected orientations. |
| S6, supplement 6024–6468 | 2174, `ms:finite:five:section`; 2308 gap-free section; 2497 acquisition section | Zero predecessor allowance only from genuine C4; exact moment-band and signed-beta cover; direct sign-count/Cantelli proof in the corner, zero variance at integer boundary, whole-box Gaussian argument with correct negative sign, both infinite phase rays; acquired same-law resource/count composition conditional on complete coverage. |
| A3, 8252–8300 | 2623, `ms:finite:paired-rectangle` | Signed Pearson identities, piecewise coefficient maxima at R/2, both coefficient signs, whole Gaussian cancellation norm, sixth-moment bound, correct (45-M) damping. Added explicit integration-by-parts formula for the positive-quadrant norm rather than an unexplained Mills-formula reference. The original R>2g substitution counterexample is retained. |
| A4, 8306–8343 | 2734, `ms:finite:signed-loss` | Weighted Cauchy loss, equality on every standardized two-point law, zero atom, corner enclosure and correct matching constant-term use. |
| A5, 8349–8377 | 2763, `ms:finite:sign-probability` | Sharp sign-probability lower bound including zero atom; scalar derivative and sharp three-point example. |
| A6, 8383–8423 | 2793, `ms:finite:outer-decomposition` / `outer-weights` | Genuine-gap residual decomposition, bounded support weights, one common residual, correct directions of endpoint/radius replacements. The pre-existing outer integral inequality is explicitly an input. |
| A7, 8429–8458 | 2843, `ms:finite:gap-localizing` | Positive weighted moment matrix; negative/zero denominator cases; monotone common-mean contraction and finite bisection without a limit assumption. |
| A8, 8464–8544 | 2878, `ms:finite:exact-phase` | Literal n in {6,7,8,9}; acquired Hmax and conserved identity are inputs; exact Gaussian phase, all four C/rho corners, both H signs, whole quadratic cells, positive total denominator and kernel gate L²/(2n)≤7. No widened n=5 or n=10–19 claim from the source heading. |
| A9, 8550–8595 | 2925, `ms:finite:central-price` | Same physical D in central/outer rearrangement; multiaffine constant and possibly negative price; total denominator and complete-score maxima remain mandatory. |
| A10, 8601–8715 | 3025, `ms:finite:bernoulli-envelope` | Every p/s/rho/C/Q/D hypothesis, exact zeta polynomial, eta derivative determinant and proof of the entire virtual level path. Constants remain fixed along the path, without claiming physical acquisition at virtual p. |
| A11, 8721–8817 | 2960, `ms:finite:fixed-h` | Same-sign deficit identity, exact fixed-h formulas, admissible-domain derivatives, lower-noise/inward refinement, all-allocation zeta concavity and endpoint minimization. |
| A12, 8823–8880; A13, 8886–8923 | 3118, `ms:finite:sine-interface`, `ms:finite:b1-cover` | Resource mapping, finite-frequency support minimization, endpoint beta direction, all closed rho seams, 55 source rows and 115 integral conditions at n=26–30. No consumer numerical acceptance asserted. |
| A14, 8929–9105 | 3175, `ms:finite:floor-transfer`, especially `floor-envelopes`, `floor-phase`, `floor25-31` | Floor25 literal scope, Cantelli event, fixed upward M, signed product-gap prices, nonnegative LOW/HIGH factors, coherent phase/score charge, finite feedback, actual support reacquisition, scaled count interface, theta versus actual lambda. |
| A15, 9111–9191 | `ms:finite:floor25-31` | Three index-free p-local mean caps and B0 finite induction; complete support/interface/empty-cover requirements. Source review counts and historical acceptance narration are not converted into new theorem premises already discharged. |
| A16, 9197–9239 | `ms:finite:weighted-induction`, `floor-phase`, `floor25-31` | INITIAL31 weighted induction and sharp K=0 charge; missing actual support, own cap, downstream resource applicability and actual count obligations explicitly retained. Intended complete bridge 31–39; no complete all-index theorem. |
| A17, 9245–9505 | 3380, `ms:finite:floor40` | Literal actual indices 40,41,42; same unrestricted owner; genuine predecessors; scalar caps; independent indexed initial support versus monotone later CENTRAL support; deleted-index/Sperner domains; signed density/phase; binary penalty; bad-pair tangent; finite inverse-correction max; local noise/phase union including zero. |
| A18, 9511–end | `ms:finite:floor-envelopes`, `signed-curvature`, `floor40-condition` | Active six-piece HIGH and optional improved Mills monotonicity; actual extended paired domain and (45-M) damping; negative-g0 curvature endpoint; index-free signed-variance gates. Runtime installation order is an implementation applicability condition, not a replacement analytic proof. |

## Deliberate changes to inherited presentation

1. G2 proof language “verification establishes” now reads “assumed complete verification establishes.” The row/coefficients numbers specify a format, not a run result.
2. The G3 continuous-domain assertion is a **certificate condition**. The supplied checker algorithm is fully explained but does not establish that all its calls terminate successfully. Undefined source macros were expanded; in particular Lambda is 59/250, not an accidental tautology.
3. ROOT4 explicitly assumes the G3 conclusion used in its localization. The inherited table reporting 54 empty, 129 direct, 43/34 child portfolios and zero uncovered parents was removed from this *new transcription*, because it would assert a completion this task has not verified. The required 260-parent domain and complete four-child rule remain. No original certificate or theorem text was deleted.
4. All 18 inherited references outside S4/S6 are mapped to seven explicit analytic-input items. These are prerequisites with exact scope, not empty references that appear to prove themselves. References to these items are styled as assumption items rather than as nonexistent section/lemma numbers.
5. A3's signed Gaussian norm now has the full integration-by-parts identity. A6 distinguishes support radii from moment residuals that otherwise share R+/R- notation. A10/A11 use eta_s/zeta_s to avoid the ROOT4 excess eta; their first absolute moment h is explicitly local.
6. Floor25/31/40 are separate contracts. The finite LOW upper inverse correction of either sign is max(I/40,I/42), with no all-index interpretation. Historical source/composer narration is replaced by the exact analytic and complete-acceptance conditions it would have to establish.

## Inputs deliberately not discharged here

The opening `ms:finite:inputs` assumption identifies (1) global attainment/contact/structural caps, (2) actual-index quantitative support, (3) sharp third-moment domain, (4) closed Prawitz and complete four-term Fourier bound, (5) half-open gaps/conserved identity, (6) resource propagation and phase interfaces, and (7) directed elementary arithmetic. Relevant integration labels already exist in the root manuscript:

- `ms:attainment`, `ms:contact`, `ms:structural-classical`, `ms:sharp-third`, `ms:sign-moment`.
- Fourier labels have the form `ms:fourier:ORIGINAL`, for example `ms:fourier:afcore:prop:conserved`, `ms:fourier:rescore:re-enclosure`, `ms:fourier:rescore:sec:setup`, `ms:fourier:rescore:u-phase-interface`.

These can be connected after the coordinator verifies exact hypotheses. In particular, the new elementary support theorem restricted to indices at least42 does **not** discharge the n=5 quantitative support condition. The fifth-index support radii in the listed moment bands need their own valid actual-index analytic exclusion and complete certificate. The generic contact theorem can justify compact support before higher moments, but not those quantitative radii by itself.

Other obligations intentionally left explicit:

- All G1/G2/G3/ROOT4 coefficient objects, complete continuous-domain positivity, exact thresholds, both tails and accepted coverage; no native run is implied by compilation.
- The full C5 initial unseeded resource acquisition, genuine central gap, signed contracted resources, supported Fourier strips and all six original nearest-count roots on each surviving domain.
- The outer integral inequality consumed by A6; the sine-circle and finite-frequency Taylor bounds consumed by A12–A13; the complete LOW/HIGH Fourier integrals and compatible profile. Those proofs are not present in A12/A13's ordinary adapter notes and are not invented here.
- All floor-source LOW/HIGH coefficient derivations, positive-domain gates, actual support states, own caps and contact allowances, exact finite sequences and current implementation bindings; the appendix proves the stated scalar floor directions once those analytic expressions are licensed.
- The binomial mode/deletion, Sperner, signed Gaussian and noise-profile comparison theorems consumed by A17, including their true minimum index and full geometric domains. The finite appendix spells out their required conclusions and the floor arithmetic; it does not replace those entire source theorems by “no nmax appeared.” If another source has an unproved lower-index restriction, it stays unresolved.
- No complete bridge for every index 6–41 follows from the few conditional families above. Missing actual-index resource and local coverage remain missing. No universal base reducer is supplied.

S5 is the global predecessor-smoothing argument assigned to the manuscript's main smoothing section. A0 and obsolete long support campaigns were omitted as requested; A1/A2 kernel/support material belongs to the other analytic appendices. Source-family filenames, installation statements, exact source-byte bindings and historical arithmetic receipts are implementation evidence rather than mathematical derivations; they remain in the unchanged original source and existing audit ledger rather than being presented as newly completed results.

## Commands actually run and typesetting evidence

Read-only source work used `sed`, `rg`, SHA256 hashes, and `git diff 6346fc1... -- paper/main.tex paper/analytic-supplement.txt`. A small local Python extraction/typesetting transformation copied only the requested S4/S6 ranges and added ordinary TeX proofs/conditions; no inherited program was imported.

A temporary standalone wrapper copied the coordinator's preamble and classical bibliography, then input the appendix by its absolute path. Compile command, run from the bundled LaTeX plugin directory:

```sh
python3 scripts/compile_latex.py /private/tmp/be-finite-typeset-20261027-fhz_2ko0/main.tex --compiler texlive --json
```

The first compile exposed an unexpanded inherited indicator macro; the second exposed a control character in one new TeX fraction. Both were repaired. Long displays were split without changing mathematics. Final compiler: TeX Live2025/pdfTeX, via latexmk4.86a; exit0; 50-page PDF. The final log has no undefined references/citations, no overfull or underfull boxes, and no fatal diagnostics. This does not mean the appendix's mathematical inputs or certificates have passed.

Every page was rendered with:

```sh
pdftoppm -r 72 -png /private/tmp/be-finite-typeset-20261027-fhz_2ko0/main.pdf /private/tmp/be-finite-typeset-20261027-fhz_2ko0/pages/page
```

All50 thumbnails were inspected on five contact sheets. Full-page inspections included pages6,14,24,27,38,43,48 (MGF proof, iid tensor expectation, shared frequency defect measure, quadrature/interpolation, sign-aware Gaussian norm, eta/zeta derivative proof, and weighted finite-index support). No clipping, missing formulas, overlaps or misplaced equation numbers were observed. Temporary compile/log/render files remain at the stated `/private/tmp` directory for coordinator inspection; they are not a substitute for the combined-manuscript final render.

Label inventory: no duplicates and no missing local reference targets. No external writes, heavy arithmetic, numerical generation, native proof acceptance, author contact, installation, or merge occurred.
