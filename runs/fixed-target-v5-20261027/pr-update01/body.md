The tail argument previously carried a variable extremal score through contact, acquisition and comparison. This PR develops fixed-target excess and now proves its initial support/moment entry without an upper actual-score cap. A new 24-cell calculation discharges the first Gaussian-weight license, conditional on the explicitly retained Fourier estimates. Separate analytic improvements lower the conditional-count cost and combine the actual moment responses.

The complete sharp theorem remains conditional. This PR preserves every original certificate and its target.

## Read first

- [Current decision and computation-removal map](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/mathematics/fixed-target-v5/2026-10-27/README.md)
- [New 15-page proof note](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/mathematics/fixed-target-v5/2026-10-27/main.pdf), with [portable TeX source](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/mathematics/fixed-target-v5/2026-10-27/source-fixed-target-v5.zip)
- [Coordinating review](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/mathematics/fixed-target-v5/2026-10-27/integration-review.md) and [independent count-proof review](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/mathematics/fixed-target-v5/2026-10-27/independent-review.md)
- [Earlier 14-page fixed-target companion](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/mathematics/strategy-v4/2026-10-27/main.pdf) and [transport review](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/mathematics/strategy-v4/2026-10-27/transport-review.md)
- [Updated 158-page manuscript](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/manuscript/arxiv-v1/main.pdf), [portable sources](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/manuscript/arxiv-v1/source-arxiv-v1.zip), and [latest correction record](https://github.com/kolodziejek/berry-esseen-certificates/blob/157db04df11416cc9f3578d8f519d117547a4251/manuscript/arxiv-v1/research/revision5-decisions.md)

## Findings

**Initial analytic entry.** Fixed-target contact, nonnegative excess, the sharp predecessor bound and the stated external structural inequality give rho<7361/4000, |beta|<321/500 and support inside (-96/25,96/25), uniformly for n>=42 and all raw thresholds. Higher moments enter only after support is bounded. Neither C_(n-2) nor an upper actual-score cap is assumed.

**First license and ordered refinement.** The sufficient raw gate is T<N*c_lower*rho_lower, rather than the stronger uniform T<2N/5. Exact evaluation on 24 closed moment cells gives R_c/rho<10 under the complete stated low/high Fourier estimates. The new phase price bounds the conserved resource separately from raw R_c. Three ordered updates lower the maximum defect ceiling from 6.1147234045 to 4.9901197720, with weighted nD<=209.585030422267. Five cells still fail D<4; no full INITIAL42 acceptance is claimed. A small support probe improves four candidate radii, but does not improve the last cell on its tested grid.

**Smaller count cost.** Positive and negative count crossings use disjoint events, so their quadratic prices can be replaced by their maximum. A crossing of order at least three also admits a smaller fourth-moment price in the low-noise regime, using an existing fourth-moment bound. The phase maximum still has at most three candidates. The marked-crossing linear term, Gaussian repair, binomial mass gate, zero-noise theorem and full signed cover remain. Clamp the complete inverse-index correction at zero before replacing 1/n by 1/N.

**Combined moment response.** On the simultaneous CENTRAL row19 domain, the entire moment polynomial has a common response bounded by CE*(1.105+0.18*abs(H)) times the available residual defect. The negative fifth-moment response is retained. The conditional-mean law is not silently standardized, and both sides keep the actual law's gap integrals. Acquisition for a fixed-target optimizer, the actual-gap baseline and the full Fourier remainder remain unproved by this result. No complete cell or atlas is removed.

**Corrections found during review.** The active manuscript's positive-gap phrase was invalid for a gap crossing zero. The corrected pointwise bound t*(rho-t)<=rho²/4, multiplied by the gap distance and integrated, yields exactly the same numerical coefficient. Separately, a feedback report called a lower bound on conserved D an identity; the corrected inequality gives the same numerical directions. Original archived sources remain untouched.

The earlier parts remain: attainment and atom-safe contact for fixed-target excess, the exact conserved term (n+H²)a, a shorter moment-circle gap proof, weighted conditional-noise budgets, and exact counterexamples to unconditional own-sign Bernoulli-skeleton domination, including n=42. Those are not counterexamples to Berry–Esseen. Pinned public Lean source inspection supplied no missing finite base or LOCAL42 endpoint; no fresh Lean build was run.

## Computation consequences

The recurrence used only to acquire an upper actual-score entry cap is absent from the new initial entry/license. Removing it from a complete tail proof still requires the rest of the ordered acquisition and strict exclusion. Finite recurrence consumers remain.

The new count formula universally dominates the old component under its stated hypotheses; where its quartic branch applies, that term needs no square-root evaluation. This is not a full LOW acceptance or measured whole-proof speedup. The 24-cell first license and the older dense initial schedule establish different conclusions, so their sizes are not a speedup ratio. No certificate or production computation is deleted.

## Checks actually performed

The new integration record contains eight passing bounded checks plus preservation of all 2,748 original baseline entries: 182 materialized files checked and 2,566 sparse blobs preserved in tree/index.

- Fresh exact first cover, all positivity/window/source gates, 12 malformed/source-corruption controls, and three separately ordered resource updates.
- Count constructor: 3,648 sampled cells representing 152 signed configurations; disjoint-price improvement in 279 and quartic-price improvement in all 3,648. Actual-law enumeration checks 1,776 tuples in 12 law/phase cases.
- Independent count checker, importing neither the constructor nor backend: 4,340 integer-crossing cases, 13,365 direct binomial differences, 38,880 phase diagnostics and negative controls. Continuum/all-integer conclusions come from the written derivation, not the grids.
- Exact combined-response stationary/sign tests and positive-noise actual-law identities, including controls rejecting replacement of actual gaps.
- Source/reference checking retains 478 manuscript labels and 271 references.

Both PDFs compile without final warnings. Both portable source archives rebuild with shell escape disabled and identical page text. All 15 new-note pages were visually inspected; the final abstract revision was reinspected. Only manuscript page59 changes from the preceding PDF; pages58–60 were inspected.

Commands, versions, hashes, stdout/stderr, return codes and failed attempts are preserved under `runs/fixed-target-v5-20261027/`; final integration is `integration04`, portable rebuilds `export01`. The first integration driver omitted an input argument; later baseline checks mishandled sparse/promisor files. Their failures are recorded and do not represent failed mathematical predicates. Raw compiler logs retain their original whitespace. Earlier checks remain under `runs/strategy-v4-20261027/`.

## Review outcome and remaining limitations

Independent scoped reviews found no blocking defect in the new count theorem or the raw/resource join after the stated corrections. Coordinating review checked the entry and common-response proofs; a separate reviewer checked the combined presentation against the premises. AI assistance is explicit. This is not human peer review or formal/end-to-end acceptance.

**Recommendation:** suitable for author review and eventual merge as documented research progress. Keep this PR draft pending that review. It is not ready to be treated as an unconditional sharp-conjecture proof or a completed arXiv submission.

The next precise obstacle is the final initial rho cell: its resource ceiling is 13.9304183554, while the conservative D<4 gate requires less than 11.1664. The current gamma lower bound stays -1.84025. A sharper same-law moment/charge inequality is needed; repeating the same coarse update does not close it. Complete Fourier estimates, BASE41, full acquisition/confinement and strict LOCAL42 remain separate obligations.

Fork main baseline is ca4943a; PRs1–4 were user-merged. Original reference 6346fc1b4432bc5982822aa696eb566ed9e1e1ee is preserved. Independent tasks used separate branches/worktrees and are combined here without duplicate PRs. No main push, force push, branch deletion, upstream mutation, expensive certificate campaign or automatic merge occurred.

