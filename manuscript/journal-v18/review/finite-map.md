# Finite chapter: coverage and upstream contracts

The actual chapter is `manuscript/journal-v18/sections/finite.tex`. It proves the finite base through 42 by an induction on the actual sample size. The only edited repository source owned by this task is that chapter. Earlier v17 sources and every numerical certificate/capture remain unchanged.

## Status and length

Mathematical status: rewritten mathematical reduction plus previously accepted exact numerical assertions; root integration review remains required. No new numerical run is claimed. Execution status: standalone layout build05 returned zero and produced **25 pages** using the root's 11-point A4, 28 mm preamble. No overfull or underfull boxes were reported. Upstream labels/citations were intentionally unresolved in this standalone test. Build01 failed on a TeX array-row syntax error and is preserved; it was fixed. Build04 was rendered at 65 dpi and all 25 pages were inspected through three contact sheets, with pages 9, 22 and 23 also viewed individually. Build05 changes only the type wording of three upstream references; its rendered-page comparison found changes only on pages 22–24. Those final pages were inspected; the other 22 pages were pixel-identical. No clipping or overlap was observed. The layout review is `runs/journal_v18_20261104/finite-layout05/LAYOUT_REVIEW.json`.

The target was 12–16 pages, with 20–24 later allowed if essential. The measured draft exceeds both: this is an explicit shortfall, not a claim of meeting the target. Main bottlenecks are the physical four-summand soundness, common COUNT filters, finite-frequency refinements and full application domains. The original n4 exposition has already been reduced from roughly seven standalone pages to about four without removing a numerical branch's analytic license.

## Complete upstream contracts

- `j:core:attainment`: ratio attainment and positive **closed** extremal event, including reflected negative discrepancy and threshold atoms. Needed at n2, n3, n4 and each first failure.
- `j:core:Q` / `j:core:contact`: whole closed-support contact. The chapter restates the explicit n2/n3 polynomial and derives the direct support criterion from its Gaussian/predecessor form.
- `j:core:moments`: both rho²(gamma²+4) >= (gamma²+2)² and (1+beta²)² <= rho²(1-beta²), with their original moment assumptions.
- `j:external:affine`: both published affine score bounds, .3031(1+.646/rho) and .3322(1+.429/rho), at every n. No unsupported support premise is attached to these inequalities.
- `j:smoothing:entry25`: the exact cap C_n < .41+4177/(13824n) under first failure for n>=25. The root's recurrence also supplies the displayed n39 and n40–42 entry constants.
- `j:cert:tensor`, `j:cert:bernstein`, `j:cert:cover`, `j:cert:arithmetic`: expectation of same-iid tensor features, exact closed-cell positivity, finite-tree coverage, and outward rational elementary enclosures. They do not replace a support or same-law domain argument.
- `j:fourier:closed-majorant`: the closed-half-line inequality with kernel 2K(t)=(1-t)+i[(1-t)cot(pi t)+1/pi]. Applied at standardized sum S4/2 and multiplier6, it gives the exact positive-imaginary-kernel/raw-frequency3t normalization used in n4.
- `j:fourier:anchor`, `j:fourier:surrogate`, the general compensated LOW/HIGH and CDF bound: same-law Fourier interfaces. The surrogate lemma must give eta<=b(rho) under R²<=rho²+8, zeta>=b(rho), and the exact centered two-point-mixture sine-circle identity. Foundation owner confirmed these.
- `j:local:moments`: simultaneous supported fourth/fifth/sixth moment and signed coefficient bounds, including A*, Z, M6 for finite LOW; signwise PSD contractions and common first moment. A coefficient corner from one marginal cannot be mixed with another.
- `j:local:budget`: physical defect lower bound with one shared budget for binary asymmetry, inward displacement and conditional noise; the finite COUNT chapter supplies its additional scalar/cubic filters.
- `j:local:acquisition`: finite enclosure preservation; support before higher moments; initial raw remainder before weight removal/defect feedback; coherent signed phase/score corners; complete initial moment covers and probability export.
- `j:local:sign-mass`: exact sign-mass lower bound that excludes six n6–9 panels and the two actual20 panels. It is a numerical necessary-condition exclusion, not an unrecorded omitted COUNT job.
- `j:local:transfer`: nD<=Nd and complete floor-dependent Fourier/contact/confinement monotonicity, signed phase inequalities, actual-index support and noise normalization, for N=25/31/40. Includes floor31 charged quadratic roots and the physical variance refinement; retaining only D<=d would be insufficient.
- `j:local:allowance`: positive39's sign-sensitive tests (min(mD,D), max(mB,B), tiny-noise denominator max(.05,Lambda)) with K=741/4000, actual n39, including zero noise.
- `j:local:finite-confinement` and `j:local:comparison`: parameterized confinement for n39 and 40–42, nearest/whole-count comparison, local phase cover and finite signed inverse-index substitutions. The finite chapter owns the binomial-slack formula and its actual-index scalar acceptance meaning.

These are explicit shared-chapter obligations, not delegations to a v17 appendix. The shared local and Fourier interfaces are now written. The finite chapter cites the dedicated closed-half-line majorant, not the separate absolute smoothing bound. The independent bounded review of confinement and local comparison is recorded in `finite-review-local.md`; its two findings have been repaired and reread. Final assembled cross-reference and evidence-catalogue checks remain with root.

## Old-to-new proof coverage

| v17 source / old labels | New location and retained content |
|---|---|
| sections/06a-small-cases.tex: ext:n123, n1-dual, n23-contact/affine | j:finite:n123 and starting-case paragraphs: n1 full-line dual and tails; n2/n3 contrary support at6 via explicit translated cubics; quantitative C3 retained. |
| Same source: n2/n3 feature formulas and moment domains | Explicit features, 70/111 threshold rows, D2/D3, expectation polynomial and both threshold tails; raw coefficient arrays are pinned certificate data. Interpolation identity tests are not substituted for positivity. |
| Same source: ext:n4-reference/excess/localization | j:finite:n4-reference, n4-excess, n4-localization: unrestricted law -> canonical Q, nonnegative physical excess, C3-dependent support bound and (w,beta,rho) region. |
| appendices/four-summand-details.tex: closed-half-line majorant and elementary enclosures | Shared j:fourier:closed-majorant and j:cert:arithmetic, with exact normalization restated in finite chapter. No reference to the old appendix is needed. |
| Same source: common measure/prices, quartic/disk lens, physical quadrature, low/large-excess, complete cover | j:finite:n4physical, n4measure, n4priced, n4low, n4numerical: all analytic branches retained in compressed form, including singular costs, same measure at all frequencies, nonlinear lens extremum, one quadrature reserve, one physical threshold reserve, Hermite series/derivatives, sign-mass Cantelli branch, affine cutoff, both reflected orientations and all260 parents. |
| appendices/direct-gaussian-support.tex | j:finite:direct-gaussian-support-criterion and support section: actual-n Gaussian expression, five polynomial ray gates, derivative bound, global threshold cell/tail enclosure. |
| appendices/five-summand-support.tex | j:finite:supportrows: four refined low radii and six complementary radii via the common criterion; repeated derivations removed. Coarser low radii are weaker consequences. |
| appendices/support-six-fourteen.tex | j:finite:supportrows: all26low+25high actual-index rows retained, including H0=18 at n9 high rows and both support rays. Data b endpoints remain exact checked rational inputs licensed by the signed-moment polynomial. |
| appendices/finite-small-refinements.tex, finite-low/two-corners | j:finite:finite-low, two-corners: finite integrals, actual n powers, damping, Taylor bounds, coordinate convexity gates, maximum before integration. |
| appendices/finite-sine.tex | j:finite:finite-sine-bound / b1-support-map: finite-frequency gates, centered two-point mixture, all55 resource-to-sine maps, weighted joint plane, common constants,23strips×5actual indices and integrated two-corner maximum. |
| sections/06b-finite-counts.tex | j:finite:finite-counts/count-identity/count-bound/conditional-moments/normalized-vertex/count-cell, with j:core:conditional-moments for the shared cubic identities: exact common iid count, strict outgoing and closed incoming events, quartic minorant, MGF/Hermite upper bounds, common cubic polygon and whole-cell normalized vertex theorem. |
| appendices/finite-count-filters.tex | Same count section: no repeated cubic definitions; defect half-plane, stronger scalar inequality, variance/noise floors, inward quadratic, single-event outgoing test and nearest-root coverage retained. |
| appendices/sign-mass.tex, inward-scalar.tex | Shared j:local:sign-mass and local acquisition/moment chapter by explicit owner agreement; their application panels retained here. |
| appendices/finite-small-refinements.tex: ext:gapfree5 | j:finite:gapfree-bound/gapfree5-result: actual positive signed corner, twelve beta slabs, all60 roots/1027leaves, complete Cantelli/Gaussian box formula and both infinite phase rays. No reflected beta claim introduced. |
| sections/06i-five-summand-assembly.tex,06h-finite-five-fourteen.tex | j:finite:assembly/numerical539: all12 n5count rectangles+signedcorner+6Fourier complements+affinetail; n6–9 and10–14 fullmoment domains, literal native caps/HIGH, count/exclusion census and actual-index support before Fourier. |
| sections/06g-finite-fifteen-thirtynine.tex | j:finite:assembly/numerical539: all low/high moment bands, own-score/HIGH order, actual20 coarsedomain join, all selected probability intervals, five explicit weighted moment exclusions, strict phase-max join and first-failure induction. |
| appendices/finite-acquisition.tex / floor-transfer.tex | Shared j:local:acquisition/transfer; chapter retains actual35–39 numerical schedules/domains, positive39 prerequisite and selected120forests. |
| appendices/positive-thirtynine.tex | j:finite:assembly positive39 paragraph + shared j:local:allowance/finite-confinement: actual39, K741/4000, full entry premises, retained K*rho charge,78probability rows/624signedcells/90whole rows and precise phase cover. This is proved BEFORE sharp39. |
| sections/06d-floor40.tex | j:finite:4042/binomialslack/numerical4042 + shared floor/confinement lemmas: actual40/41/42, correct weighted invariant and two-endpoint support, whole moment/probability cover,49left+48central rows, separate phase covers, both sign conventions, actual finite binomial slack and signed inverse-index rule. |

## What is data, and what is still mathematics

The coefficient arrays, rational prices, chosen geometry rectangles/refinement trees, midpoint meshes and exact upper/lower numerical values remain in pinned certificate inputs. The finite chapter defines the mathematical functions they bound, all their continuous domains, the rules extending numerical enclosures between mesh points and over infinite tails, and the same-law map into the domain. It is not enough for a source archive or a success flag to exist: each numerical proposition refers to full already-completed native acceptance plus complete domain joins. Root must bind these propositions to the final certificate catalogue.

No omitted historical n25 third/high-moment resource band is a premise: the unrestricted Fourier complement [6/5,19/10] is the selected replacement. No discarded failed/interrupted run is promoted. Exact execution counts are reduced to domain censuses relevant to coverage; runtime/provenance mechanics remain in the separate certificate package.

## Remaining editorial/integration checks

1. Confirm every shared upstream contract above in its finished chapter, including both Fourier coefficient rectangles and the n39/40 confinement parameters.
2. Root independent read of compressed n4 and common COUNT semantics, then bind numerical propositions to exact preserved evidence/catalogue IDs.
3. Compile assembled manuscript and inspect equations/tables; standalone test cannot resolve upstream labels or verify surrounding transitions.
4. The approx60TOTALpage goal is not yet established. Further shortening must preserve the displayed support/moment/count domain logic; no blanket deletion of all finite technical details is proposed.

## Current local labels

- `j:finite:chapter`
- `j:finite:starting`
- `j:finite:n123`
- `j:finite:n1-dual`
- `j:finite:n23-contact`
- `j:finite:n23-affine`
- `j:finite:n4-localization-section`
- `j:finite:n4-reference`
- `j:finite:n4-excess`
- `j:finite:n4-physical-moments`
- `j:finite:n4-localization`
- `j:finite:n4physical`
- `j:finite:n4measure`
- `j:finite:n4priced`
- `j:finite:n4low`
- `j:finite:n4numerical`
- `j:finite:support`
- `j:finite:direct-gaussian-support-criterion`
- `j:finite:direct-support-ray-gates`
- `j:finite:supportrows`
- `j:finite:small-fourier`
- `j:finite:finite-low`
- `j:finite:two-corners`
- `j:finite:finite-sine`
- `j:finite:finite-sine-bound`
- `j:finite:b1-support-map`
- `j:finite:finite-counts`
- `j:finite:count-identity`
- `j:finite:count-bound`
- `j:finite:conditional-moments`
- `j:finite:one-sided-mgf`
- `j:finite:normalized-vertex`
- `j:finite:count-cell`
- `j:finite:filters`
- `j:finite:defect-halfplane`
- `j:finite:defect-sharp`
- `j:finite:beta-noise`
- `j:finite:common-inward`
- `j:finite:gapfree5`
- `j:finite:gapfree-bound`
- `j:finite:gapfree5-result`
- `j:finite:assembly`
- `j:finite:numerical539`
- `j:finite:4042`
- `j:finite:binomialslack`
- `j:finite:numerical4042`
- `j:finite:base`

## Current upstream references in TeX

- `j:cert:arithmetic`
- `j:cert:cover`
- `j:cert:tensor`
- `j:core:attainment`
- `j:core:conditional-moments`
- `j:core:moments`
- `j:core:normalization`
- `j:external:affine`
- `j:fourier:anchor`
- `j:fourier:closed-majorant`
- `j:fourier:surrogate`
- `j:fourier:taylor`
- `j:local:acquisition`
- `j:local:allowance`
- `j:local:moments`
- `j:local:sign-mass`
- `j:local:transfer`
- `j:smoothing:entry25`

Current finite source SHA-256: `21672428d87404f8861acc868d65e326969ff3acb0f0699991480c3167faf8be`.
