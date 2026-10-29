# How fixed-target excess can shorten the complete proof

Audit point: fork commit `43f9f820a981d858181735c533e3d98dcc9eda79`, branch `research/v6-compression-map-20261027`. This report changes no manuscript, certificate, target or baseline file. The preserved original reference is `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.

## The substantive answer

The fixed-target approach can remove an entire **score-control layer** from the tail proof: first obtain a bound on the maximizing ratio, feed that bound back through score-dependent coefficient boxes, improve the score cap, charge its excess, and repeat. Instead, the contact coefficient is the known constant `c=CE` from the outset. The nonnegative excess `a` is retained as an extra resource, not used to determine that coefficient.

That is a meaningful conceptual simplification. It is **not yet a demonstrated large reduction of the entire 158-page proof package**. Most of the current length proves Fourier estimates, translates moment/gap information into acquired domains, proves confinement and count witnesses, or develops the independent finite base. Those tasks remain. The 14-page strategy note and 15-page follow-up are changes and partial advances, not a 29-page replacement for all 158 pages.

A considerable overall shortening needs one further structural success: a direct fixed-target estimate that replaces a large part of the ordered moment/resource acquisition, or a uniform count-comparison theorem replacing several local witnesses. The new common-response calculation is a credible route toward the first, but currently covers only one already acquired central domain and retains an unresolved actual-gap baseline and Fourier remainder. Alternatively, a separately completed finite-base proof could make the *tail paper* much shorter; that relocates the base proof and does not shorten the complete mathematical proof unless the base itself is simplified.

No total-page forecast or percentage reduction is justified yet. The measured breakdown below explains why, and the proposed architecture identifies exactly what must change for a large reduction to become real.

## Measured current documents

The read-only inventory used `pypdf` to read PDF bookmarks and search selected headings, and recorded hashes and source line locations. Evidence is in `runs/fixed-target-v6-20261027/compression01/`: `inventory.json`, command/version receipt, stdout and stderr. It executed no proof or certificate program.

| Document | Measured physical pages | What it contains |
|---|---:|---|
| `manuscript/arxiv-v1/main.pdf` | 158 | Main reductions, extensive analytic appendices, conditional finite-base material and references |
| `mathematics/strategy-v4/2026-10-27/main.pdf` | 14 | Fixed-target attainment/contact/conservation/conditional transport, plus separate structural proposals and inversion proof |
| `mathematics/fixed-target-v5/2026-10-27/main.pdf` | 15 | Initial entry, 24-cell first license and limited feedback, count-cost improvement, one-domain common response |

These documents total 187 PDF pages **with substantial overlap**. This is not a measure of the length of a consolidated proof.

The following intervals use measured starts of headings. A boundary page can contain material from both neighboring blocks; they are not disjoint page counts that may be added as exact savings.

| Current manuscript block | Physical page anchors | Principal source |
|---|---|---|
| Introduction and guide | 3–7 | `sections/01-introduction.tex`, `01b-guide.tex` |
| Ratio attainment/contact and moment domains | 7–11 | `sections/02-extremizers.tex`, `02b-moment-domain.tex` |
| One-step smoothing and first failure | 11–12 | `sections/03-smoothing.tex` |
| Elementary zero-loss support | 12–16 | `sections/04-support.tex` |
| Skeleton, physical defect, conservation and score-resource refinement | 16–26 | `sections/05-geometry-counts.tex`, `05b-conserved.tex`, `06-resources.tex` |
| Conditional counts and curvature | 26–30 | `sections/05c-counts.tex`, `07-curvature.tex` |
| Global contract, certificate soundness and status | 30–33 | `sections/08-certificates.tex`, `09-discussion.tex` |
| Full Fourier/resource/confinement/count appendix | 33–89 | `appendices/fourier-analysis.tex` |
| Elementary normalization | 89–91 | `appendices/normalization.tex` |
| Uniform floor-42 bridge | 91–93 | `appendices/uniform-bridge.tex` |
| Signed local refinements | 93–101 | `appendices/local42-refinements.tex` |
| Finite-index support with predecessor loss | 101–108 | `appendices/finite-support.tex` |
| Finite-index reductions and conditions | 108–156 | `appendices/finite-analysis.tex` |
| Bibliography | starts 156, ends 158 | Four bibliography files |

Within the largest analytic appendix, the complete remainder estimates begin on page 42, simultaneous-resource pricing on 52, the coefficient atlas on 56, rectangular feedback on 64, score/phase charging on 71, confinement on 74, and the conditional-count comparison on 80. Thus removing score interpolation does not remove the whole resource appendix. Within the main text, “Keeping the excess term” begins on 24 and the joint-noise bound begins on 25: the latter remains a required resource theorem.

## What disappears, and at what level of proof

Here “removable” means an edge or a block in a **new fixed-target tail composition**. It does not authorize deleting the corresponding source file from the repository, and it does not say that the old `LOCAL42` contract has been accepted under different hypotheses.

| Block or edge | Concrete change and reason | Exact current locations | Status and limitation |
|---|---|---|---|
| Ratio maximization as the selected tail witness | Replace it by maximizing `a=sqrt(n)(F-Phi)-c rho`. A first failure, including equality, gives an attained witness with `a>=0`; its contact coefficient is c. | `sections/02-extremizers.tex:14–176`; replacement `strategy-v4/.../excess.tex:45–166` | Replacement theorem proved. **Attainment and atom-safe contact do not disappear**; their proofs are still needed and are similar in size. |
| Recurrence -> upper own-score and upper-excess entry caps | The new initial support and first raw license use `C_(n-1)<=c` and `a>=0`, not `n(C_n-c)<.3` or `C_n<.4226`. | `sections/03-smoothing.tex`; `sections/08-certificates.tex:18–31,56–72`; replacement `fixed-target-v5/.../entry.tex`, Theorem 1 | Discharged for the new initial entry. Removal from a complete tail theorem remains conditional on transporting every later consumer. The recurrence is still used by finite-base candidates. |
| Actual-score interval in raw moment/Fourier coefficients | Put the formal multiplier equal to c. One no longer has to prove that `C_act=c+a/rho` lies in the scalar multiplier interval. | `appendices/fourier-analysis.tex:2325–2400`; `strategy-v4/.../excess.tex:390–485` | Algebraic specialization proved; downstream domain acquisition and all scalar predicates remain. |
| Variable-score corners | Exact specialization reduces the conceptual `(C,rho)` rectangle to its rho interval: four score/moment corners become two moment corners; the three-score/two-moment charged atlas becomes two moment endpoints at c. | `fourier-analysis.tex:2342–2400,2853–2887` | Conditional computational simplification, not an asserted factor-of-two/three speedup. A rigorous rational enclosure of irrational c can still use two numerical coefficient endpoints; signs, moment endpoints and H dependence remain. |
| Two-interval score charge and cap-endpoint interpolation | Directly estimate the fixed-c remainder/resource. There is no actual-score interval to split at `.40974` or an uncertain actual upper score endpoint to interpolate. | `sections/06-resources.tex:1–54,88–95`; `fourier-analysis.tex:2853–2887` | This specialized derivation is unnecessary in the new route. Its **joint noise/displacement conclusion**, acquired coefficients and strict margins remain necessary. The old conservative scalar bound can also be reused at c without re-proving an actual-score cap. |
| Score-cap feedback as an acquisition goal | Optional output `C_act<c+V/n` need not feed the fixed coefficient. The desired outputs are actual moments, gaps, weighted defect, threshold and conditional noise. | `fourier-analysis.tex:2370–2385`; `sections/06-resources.tex:88–95` | Role removed in the new route. Feedback for the remaining physical quantities stays. |
| Uniform first raw threshold `T<.4N` | Replace by the exact cell gate `T<N*c_lower*l`, or the normalized sufficient gate `R_c/rho<10` at N=42. | `sections/05b-conserved.tex:290–346`; `fixed-target-v5/.../entry.tex`, Lemmas 2–4; `numerical-cover.tex` | Derived and the 24-cell scalar gate freshly checked, conditional on complete Fourier primitives. It proves the **first license**, not the old full initial acquisition. |
| Separate positive/negative quadratic crossing prices | Disjoint events use their maximum. A cubic crossing occurring beyond a positive distance also has a fourth-moment price; take the smaller valid price. | `sections/05c-counts.tex:119` onward; `fourier-analysis.tex:3847–3878,4031–4060`; replacement `fixed-target-v5/.../count-cost.tex` | General component theorem proved and independently reviewed. This removes a loss in one coefficient, not the whole count argument or a complete LOW row. |
| Inner 64-subinterval curvature maximization | Use the exact phase endpoints and possible interior stationary point. | `sections/07-curvature.tex`; earlier `mathematics/reduction2/.../local-kernel.md`; new `count-cost.tex` | Already reduced before fixed-target; the new count formula preserves a three-candidate maximum. Do not count the earlier 64-to-3 replacement as a new fixed-target saving. |

The current 158-page manuscript already uses `BASE41 + first failure + LOCAL42` and already omits the old strong46/backward-loss tail assembly from its main composition. Earlier work also derived a conditional bypass of 12 of 31 finite61 bootstrap predicates while retaining 19 native predicates and all 152 LOW row predicates. That is documented in `mathematics/simplification/2026-10-27/finite-entry.md`; it is **not an additional fixed-target saving**. The finite-base-provider caveat in `base-closure.md` remains.

Two numerical details prevent a misleading reading of this table. First, the first fixed-target bound only gives `a/rho<10/n`; at n=42 this is nowhere near the old actual-score cap `.4226`. The new argument succeeds by not requiring that cap, not by having numerically proved it. Second, replacing the ratio multiplier by c does not remove the need to use the appropriate upper multiplier when a signed cubic coefficient is negative. A narrow valid enclosure of c is still required.

## What is retained in a complete proof

1. **The independent base through 41.** The current candidates include small-index tensor/physical Fourier arguments, indexed support and later finite transfers. They are not proved by a first-failure tail argument. `sections/08-certificates.tex:198–211` explicitly records missing complete base and provider closure. In particular `appendices/finite-analysis.tex:3295–3335` still uses a predecessor-smoothing own-cap construction and the positive term `.54 Q_+/m`. The tail's removal of that input does not remove this finite consumer. Appendices E/F, pages 101–156, cannot be discarded from an overall proof on present evidence.
2. **Closed-boundary variational analysis.** Fixed-target attainment must preserve moments 1 and 2 by uniform integrability, use lower semicontinuity of the third moment, handle moving CDF thresholds, and extend contact to the closed support. Fixed target removes the ratio bookkeeping, not these obligations.
3. **Actual-law support and moment acquisition.** Initial support `96/25` is now available without an own-score cap. The later radii `121/40` and the 63-radius family in `sections/04-support.tex:147–245` still need their preceding moment hypotheses. One initial support proof does not acquire those moments, a central gap or the final amplitudes.
4. **The full Fourier error and its uniformity.** Compensated inversion, low-frequency Taylor remainders, complete high-frequency cores/wings/zero-cell/comparator tails, all damping gates, and all-index bounds survive. In the new first license the selected sixth-order and six-part primitives replace neither their analytic proofs nor any unreviewed alternative needed later. Prawitz and the characteristic-function machinery have separate finite-index consumers (`finite-analysis.tex:43–56`), even if a particular tail pass does not use them.
5. **The shared physical defect and actual gap integrals.** Nonnegative D, weighted `nD`, leakage, conditional-noise budget, endpoint displacement and their common-law coupling survive. Fixing c does not justify separate optimization of their moments or allow the same defect to be spent twice.
6. **Confinement and both deleted sums.** The derivative of the new contact majorant has coefficient c; concentration still involves the actual `n-1` and `n-2` sums. Sharp predecessors supply both caps, but do not remove their different index factors, strict-width geometry, exceptional-event bounds or atom conventions. See `fourier-analysis.tex:3058–3457` and `uniform-bridge.tex`.
7. **Count normalization and all noise regimes.** The exact same-marginal binomial mixture, phase normalization, actual binomial mass bounds, signed variance/cubic repair, small-positive-noise limits, whole-count mark and harmonic terms remain. The count-cost improvement touches one curvature coefficient. It does not replace TINY/MID/LOW coverage, the negative event-bracket gate, or the clamped inverse-index correction.
8. **Zero noise and strict equality exclusion.** At zero noise the law is Bernoulli. The relevant binomial theorem is still needed; positive-noise leaves require `C_B<=c` and a strict negative fixed-target count RHS to rule out `a=0` as well as `a>0`. A weak estimate alone cannot prove the strict tail theorem.
9. **Certificate soundness and complete coverage.** A direct analytic proof could replace a particular certificate, but fixed target alone does not. Closed cells, signs, count-plane collisions, coherent moments, denominator positivity and exact arithmetic acceptance remain in every retained numerical argument.

## Where a genuinely large reduction could come from

| Possible new theorem | Block it could replace | What is missing now |
|---|---|---|
| One uniform fixed-c response bound for the **whole** raw remainder, with a usable same-law baseline and Fourier error | Much of the coefficient-by-coefficient atlas, repeated moment intersections and possibly several acquisition passes (current pages 52–74) | The v5 response theorem assumes `p in [209/500,21/50]`, support `46/25`, theta at most `.012657` and the other CENTRAL row-19 moments. It retains the original law's J,J1,J2 in the baseline and the original Fourier error. It cannot initialize the high-rho domain or replace the atlas globally. |
| A global initial contraction directly from fixed-target conservation, without a lengthy signed feedback schedule | The dense old initial acquisition and some phase/support iterations | The v5 first license has only three coarse updates. The worst defect ceiling is `4.9901197720`; five of 24 cells do not enter the sufficient `D<4` regime. A first license is not the old initial target `D<.784` or final local resources. |
| A strict uniform fixed-target count inequality spending the available binomial margin | Separate nearest-count/middle/whole-count witnesses and much of their case cover (current pages 80–101, with main preliminaries) | It must hold for every acquired sign, phase, noise level and n, including arbitrarily small noise. Unrestricted sign-skeleton domination is false; the strategy note has a counterexample. The present quartic price only improves one term. |
| A fixed-target theorem valid below 42 with a small independently verified base | Some indexed finite contracts and, if strong enough, substantial parts of Appendices E/F | Floor-42 heat/concentration/normalization gates do not automatically extend to small n. The current finite-base proof is not closed. This would be new mathematical work, not a reformulation of the existing tail proof. |

These are mechanisms for a considerable reduction, not promised results. The largest plausible saving is eliminating a *sequence of acquisition lemmas* by proving a stronger structural inequality, rather than making each cell's arithmetic slightly cheaper. One cannot estimate its proof length before seeing how the new baseline and uniform error are controlled.

This inventory is frozen at the stated commit. Parallel v6 work is investigating a stronger phase bound and moment ceiling. If a new 24-cell pass reaches `D<4` everywhere, that closes one initialization obstacle in this table. It still does not replace the old twelve-step acquisition, its final much smaller defect, or the downstream signed domains. No ratio of cell counts is a runtime claim when the two computations have different conclusions.

## A concise complete-proof architecture to aim for

The following is one proof, with each analytic fact proved once. A technical supplement may hold its exact finite tables and accepted proof objects, but remains part of the overall proof.

1. **Base and first failure.** State an independently proved `BASE41`. Choose the least n>=42 with `C_n>=c`; derive both sharp predecessor caps. Use fixed-target attainment, including the equality boundary. No scalar recurrence enters this tail composition.
2. **One contact/support theorem.** Derive the fixed-c contact majorant and the favorable `-na` support term. Prove initial structural moments and the complete two-ray support theorem; retain later support contractions only with their acquired inputs.
3. **One geometric/conservation theorem.** Define the physical D, same-law gap integrals and leakage. Prove the identity with `(n+H^2)a`, the moment-cell weight license and phase price. Export one weighted resource.
4. **One selected complete Fourier engine.** Prove compensated inversion and exactly the low/high alternatives actually required by the accepted new schedule. Put elementary rational-enclosure lemmas here once. Merely unselected alternatives can be omitted from this *tail presentation* only after a consumer audit; finite-base consumers still retain theirs.
5. **One ordered acquisition theorem.** Give the exact map from the initial moment band to the final signed probability/phase/noise domains, keeping raw and resource bounds distinct. Ideally replace much of this with a uniform common-response lemma; until that exists, retain the necessary ordered transitions and their certificate conditions.
6. **One count-comparison theorem.** State the exact fixed-target count identity. Prove the remaining nearest/whole-count witnesses, using disjoint quadratic costs, quartic price and exact phase extrema. Retain signed normalization, mark/harmonic terms, clamp, zero-noise branch and all strict target margins.
7. **One acceptance theorem and contradiction.** A complete closed cover supplies the previous theorem's hypotheses and strictly excludes every attained fixed-target witness. Combine with the base to conclude the sharp global inequality and the stated strict tail. Keep primitive arithmetic success separate from analytic premise acceptance.

This architecture removes a loop in the reasoning, not the main mathematical questions. It is considerably easier to explain because there is only one target coefficient and one resource identity. Its page length depends mainly on steps 4–6 and the finite base, not on the now-short first-failure paragraph.

## Consolidation versus mathematical deletion

The new notes should be **merged into** the manuscript, not appended verbatim. Replace the tail witness/contact/conservation formulation, merge the repeated heat-support derivation, and insert the new license and phase-price lemmas once. Replace the count-curvature component rather than presenting both as required arguments. The separate moment-circle explanation and compensated-inversion proof need only one home.

This removes repeated explanations across the three PDFs. It does not justify removing all of main Section 5 or Appendix A: the joint resource, full Fourier bounds and local interfaces there still carry mathematical obligations. The v5 initial support proof also does not contain all later radius-family consequences currently in Section 4. The current v3 manuscript already replaced several repeated finite attainment/contact and moment arguments by cross-references; those earlier editorial savings must not be counted again.

A useful quantitative distinction is that the recurrence starts on 11 and support on 12, while the main score-charge material starts on 24 and the retained joint-resource part already begins on 25. Their disappearance alone is a saving of a few page portions, not dozens of pages. The corner/charge passages in the appendix add local savings, but leave the surrounding atlas. Conversely, relocating the finite-support/base material starting on 101 and ending where references begin on 156 would remove about 55 **start-to-start page intervals from one document**. It removes zero obligations from the complete proof. This is why a proposed 50% reduction cannot be supported by adding the page spans of blocks whose conclusions are still needed.

## Remaining bridge list

Before declaring the score machinery absent from the complete tail proof, supply all of the following:

* A new local exclusion contract for fixed-target maximizers, rather than applying the old ratio-extremal `LOCAL42` assumptions verbatim.
* Completion of initial acquisition beyond the 24-cell license, including the high-rho cells that fail the sufficient small-defect gate.
* Proof-level transport of every selected support/resource/confinement step to the fixed coefficient, preserving actual-law moment order, signed H, strict budgets and the weighted invariant.
* A complete uniform index-42 version of the selected analytic primitives, both deleted-index concentration bounds and all final target domains. Finite upper-endpoint heat or score arguments cannot be extrapolated.
* Fixed-c versions of all signed repair multipliers and actual-phase resource exports; numerical intervals enclosing c are allowed, but must not be misidentified with the actual score.
* Complete positive-noise coverage and strict leaf inequalities, plus the separate zero-noise binomial comparison. The improved curvature component is not their acceptance.
* Independent finite-base closure, including the actual provider graph at 40 and 41. Tail-score machinery cannot be removed from a base provider that still consumes it without replacing that provider.

## Status and evidence

| Deliverable | Mathematical status | Execution status |
|---|---|---|
| Dependency-removal map | Static audit of explicit source hypotheses and existing proved/conditional replacements | Source/PDF inventory freshly executed; no certificate execution |
| Page spans | Measured physical-page anchors and explicitly nonadditive intervals | 158/14/15 pages confirmed; hashes and matched titles recorded |
| Proposed consolidated architecture | Conditional proof design with named missing bridges | Not implemented or compiled as a new proof |
| Large overall reduction | Research opportunity requiring new uniform lemmas or base simplification | No claimed percentage, new total length or computational speedup |

Only new research files and read-only inventory evidence are added. This report does not remove any existing certificate or weaken any theorem statement.

## V6 addendum: initial support geometry now acquired

The frozen inventory above remains a record of the starting point. The five-cell initialization obstacle is now closed, conditional on the same retained Fourier/contact/support inputs. The newly selected route uses the sign-coherent K1 bound and the fifth-moment square, followed by **two elementary quadratic passes**. Its full 24-cell cover gives raw <=11.5164967977, U<=9.9790315907, D<=3.5746638454 and a strictly positive central-gap margin on every cell. It requires neither an actual-score cap nor the new degree-six phase lemma. The first pass already gives D<4; one moment-circle/density update obtains the actual gap everywhere.

The stronger optional phase lemma gives that geometry in one pass (D<=3.8675294672); six optional actual-gap HIGH updates reach D<=2.9976105609, with only16/24cells below2. This is not the full INITIAL42 target D<.784/raw<2.24 or the final LOCAL42 domain. Therefore the dependency removal now justified is the old score-control path **to this initial support-gap conclusion**, replaced by two coarse exact passes. No complete dense acquisition, final cover or finite-base proof is deleted. Comparing24cells with18432cells is not a speedup estimate because their complete outputs differ.

For the short manuscript choose the two-pass route; retain the degree-six lemma as an optional quantitative refinement. The note's additional pages contain new proofs and reviewable comparisons, not a proposed addition to every proof path. The next large shortening still requires a direct bound reaching the final physical/noise domain or a uniform strict count theorem.
