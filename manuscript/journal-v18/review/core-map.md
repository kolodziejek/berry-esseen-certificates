# Core and Fourier consolidation for journal-v18

Mathematical status: analytic proofs retained or re-derived at the hypotheses stated below. The direct ratio-attainment argument and the closed-half-line majorant are proved in the new text. The equality-inclusive LOCAL47 application is reviewed separately; it is not a consequence of a numerical PASS alone.

Execution status: no numerical certificate was rerun or changed for this consolidation. The isolated two-section LaTeX build uses the existing TeX Live 2025 installation, 11-point type and 28 mm margins. The first complete version occupied 17 pages; adding the required closed-half-line majorant and its proof increased this to 19 pages. The final snapshot and QA are recorded below. Existing extended-v17 sources and all certificate data remain unchanged.

## Deliverables and scope

The two owned files are `manuscript/journal-v18/sections/core.tex` and `sections/fourier.tex` in the revision checkout. They introduce no new macros. Their labels begin `j:core:` and `j:fourier:`. They contain no references to an old appendix as a substitute for an analytic proof.

The core proof is ratio-only. For each fixed integer n>=2, it proves attainment of C_n by a compactly supported standardized law and a positive closed-event threshold, without assuming that C_n>C_E. A common third-moment ceiling supplies uniform integrability of the first two moments only. Lower semicontinuity of the third moment, closed-set convergence at moving thresholds, and maximality then recover the limiting third moment. Reflection handles the strict left-limit discrepancy by a dominating closed reflected event. Contamination keeps the raw event fixed, so its derivative remains valid at atom collisions. Upper semicontinuity extends contact equality to the whole closed support; the negative cubic coefficient then bounds that support.

One generic off-contact conservation identity is proved for an arbitrary positive coefficient c and a compactly supported standardized law. Its residual includes the Lebesgue integral over the support as well as gap terms. The ratio specialization sets c=C_n and a_c=0. Its nonnegative identity and first raw sign license need only e=C_n-C_E>=0, not e>0, not D<2, and not an already acquired central gap. No division by excess or defect is introduced.

The Fourier results concern the actual common marginal. Compensated inversion includes atoms and is justified by absolute Fubini. The LOW remainder is uniform for every n>=N>2 under explicit common fourth-, fifth- and sixth-moment bounds. HIGH covers the complete half-line and states the exact event probability, separation and conditional second-moment hypotheses. All integral tails have explicit bounds. The closed-half-line majorant has value one at the boundary; its real-part improper integral is distinguished from the potentially divergent complex integral.

## Interfaces imported from other new sections

| External interface | Exact use here | Condition retained |
|---|---|---|
| Definition of C_n and C_E in introduction | Ratio objective, sharp constant | Standardized iid law; finite third absolute moment |
| `j:cert:bernstein` | Finite positivity test in the scalar cosine-profile proof | Exact coefficients on a complete closed interval; not sampled positivity |
| Existing citation `Shevtsova2012`, Lemma 4.1, p.263 | Prawitz's four-term normal-discrepancy smoothing inequality | Characteristic function of the actual standardized sum, positive truncation parameters and declared endpoint conventions |
| `j:external:affine` (used by finite/local, not needed for attainment) | Two moment-dependent global ceilings | The same standardized marginal and its actual rho |
| Local acquired moments and profiles | Applications of LOW/HIGH, not their analytic proofs | Whole-cell valid M,g,M6,A,Z and a coherent event/profile for the same law |

The root-owned certificate positivity lemma is supplied in the same manuscript. No numerical certificate is imported as a replacement for inversion, compactness, Taylor remainders or the infinite HIGH tail.

## Interfaces supplied to finite and local sections

| New label | Supplied conclusion |
|---|---|
| `j:core:attainment`, `j:core:contact`, `j:core:Q` | Attained positive closed-event ratio and global contact majorant, equality on entire closed support |
| `j:core:scaled-Q` | Exact finite-module polynomial nQ with lambda=D0/rho=C_n/sqrt(n) |
| `j:core:predecessor` | Same-law support inequality with a signed predecessor difference; replacing it by a nonnegative allowance only weakens the bound |
| `j:core:normalization`, `j:core:conditional-moments` | One sign split, zero atom assigned nonpositive, exact rho/gamma/beta identities and Bernoulli zero-noise case |
| `j:core:moments` | Sharp third-moment domain and signed beta/rho constraint, with proofs |
| `j:core:defect`, `j:core:gap-defect` | Nonnegative physical defect, unique zero-defect Bernoulli geometry, and central-gap criterion only after its stated defect bound |
| `j:core:joint-defect`, `j:core:joint`, `j:core:simultaneous` | One shared physical/noise/endpoint budget; local signed cross-moment refinements remain local |
| `j:core:conservation`, `j:core:general-identity` | Full off-contact identity, including support-integral residual |
| `j:core:positive-identity`, `j:core:license`, `j:core:phase-price` | Ratio identity and sign/unweighting license valid also at C_n=C_E |
| `j:fourier:inversion`, `j:fourier:ledger` | Signed Gaussian transfer and the exact I0/Iinfinity ledger |
| `j:fourier:anchor`, `j:fourier:surrogate` | Anchored real/imaginary bounds, common-law sine circle, eta<=b(rho) under R^2<=rho^2+8 and zeta>=b(rho) |
| `j:fourier:compensated` | Supported fourth/absolute-fifth moment bounds, compensated finite power bounds and complete infinite tail |
| `j:fourier:profile`, `j:fourier:scalar-cosine` | Convex cosine profile with exact finite positivity reduction and analytic ray |
| `j:fourier:closed-majorant` | P(Y<=h) <= 1/2+2 Re integral K(t)exp(-iAth)f_Y(At)dt, integrable Y, every h and A>0, boundary value one |
| `j:fourier:prawitz`, `j:fourier:quadrature` | Four-term normal CDF transfer, endpoint estimates, larger tau range and differentiated cancellation tails |
| `j:fourier:low`, `j:fourier:high`, `j:fourier:conclusion` | Uniform remainder under precisely stated actual moments/profile, no gap/contact assumption hidden in LOW or initial universal HIGH |

Finite owns the actual-index two-corner refinements and sine certificates for indices26–30. Local owns paired LOW cancellation, Mills bounds, signed Pearson rectangles, the larger-M paired extension and acquisition/floor transfer. These are stronger application-specific steps; the common triangle LOW is not asserted to replace them.

## Mapping from extended-v17

All source paths below are relative to `manuscript/extended-v17` in the revision checkout.

| Old source / identifiable results | New disposition and reason |
|---|---|
| `sections/02-fixed-target.tex`: reflection, ratio-attainment, contact, Q | Retained in `j:core:attainment`–`j:core:scaled-Q`; direct ratio compactness proof replaces the detour through a fixed-target maximum |
| Same: separate fixed-target attainment and first-failure optimization | Unneeded for the chosen proof: LOCAL47 admits the closed excess endpoint and ratio attainment holds there. The auxiliary excess is retained only for the general identity. This removal depends on the separate equality audit and complete new local proof |
| `sections/02b-moment-domain.tex`: sharp-third and sign-moment | Retained with factorized/Cauchy proofs in `j:core:moments` |
| `sections/05-geometry-counts.tex`: Bernoulli coordinates, canonical decomposition, normalization, conditional moments and tau moments | Consolidated into the single normalization and conditional-moment identities; no alternate conditional law or higher-moment assumption introduced |
| Same: physical-defect definitions/theorems, zero-defect, Bernoulli defect | Retained in `j:core:defect` and subsequent decomposition; duplicate formulations removed |
| Same: general gap-family inequality at arbitrary t>0 | Unneeded by this route; the complete t=3 inequality and its equality case remain. The lattice-span consequence is retained in the final core paragraph |
| Same: outer-gap decomposition, joint-defect budget, simultaneous-gap formula | Retained in `j:core:gap-defect` and `j:core:joint` with explicit common budget and proof |
| `sections/03-conservation.tex`: R, contact conservation, first/second identities, first moment, defect identity, sign license and phase price | Consolidated into one generic proof and the ratio specialization; intermediate identities used in that proof remain displayed |
| Same: fixed-excess specialization | Not used by ratio-only composition; generic identity still covers it algebraically. No separate optimizer existence is asserted |
| `appendices/off-contact.tex`: residuals and general identity | Retained in full, including support Lebesgue integral. Diagnostic off-contact example omitted because it is not a dependency; the defect it guards against is prevented by the explicit residual definition |
| `appendices/normalization.tex`: Gaussian constants and derivative bounds | Broad rational enclosures and proofs retained in `j:fourier:constants`; the much narrower C_E interval for compact fixed-target entry is unused and omitted |
| `appendices/fixed-fourier.tex`: inversion and ledger | Retained with complete Fubini proof and atom conventions |
| Same: LOW, Taylor, HIGH, tail and conclusion | Retained with explicit constants and full-domain proofs. LOW written for N>2, which is the actual proof hypothesis and already the corresponding local-estimates hypothesis; no new numerical target is asserted |
| Same: clipped Pearson Z refinement | Retained as a coefficient option; not confused with local's stronger joint signed rectangle |
| `appendices/finite-fourier.tex`: anchor, surrogate, compensated HIGH | Retained with proof. The lower bound Z on zeta is stated as any proved whole-cell positive bound; the proof needs only zeta>=Z, and b(r) always supplies it |
| Same: scalar cosine profile and finite transfer/scalars | Retained, including finite exact Bernstein gate, infinite ray, quadrature endpoints and differentiated tails |
| `appendices/four-summand-details.tex`: closed-half-line majorant | Added as `j:fourier:closed-majorant` with full partial-fraction, Abel and absolute-Fubini proof. Its n4 normalization is explicit; no appeal to the absolute normal-discrepancy theorem is substituted |
| Old execution counts, capture paths and repeated interpretation prose | Moved to or already preserved in the companion evidence package; these are evidence metadata, not missing analytic lemmas |

## Mathematical changes requiring explicit justification

1. **Ratio compactness directly.** The closed-set limit gives discrepancy at least C_n b/sqrt(n), while rho(P)<=b. Since C_n>0, maximality forces equality and rho(P)=b. Thus no unjustified third-moment uniform integrability is needed. The positive lower bound on the maximizing ratios also bounds thresholds. This proves the same ratio-attainment conclusion without a fixed-target existence theorem.
2. **LOW for N>2.** The proof uses only n-1>0, n-2>0 and the stated M<=11.1,g<=1.85. Its a0,b0 and every power-integral comparison retain their signs. It is the same analytic theorem already used at smaller floors in the finite/local source, not a claim that every large-index numerical profile works at a smaller index.
3. **General zeta lower bound.** The compensated bound uses gamma^2<=rho^2-zeta^2<=r^2-Z^2, hence any proved positive Z is valid. Empty or inconsistent cells require exclusion; no sampled Z is permitted.
4. **Equality-inclusive application.** The ratio identity has nonnegative e=C_n-C_E, and the first raw sign license uses R<n C_n rho. Positive noise is excluded by a strict loss relative to the same binomial law; zero noise uses the strictly finite-binomial external theorem. This is audited in `foundations-review.md`; it does not extend LOCAL42 to equality automatically.

## Remaining integration obligations

The root must preserve the complete local paired/moment/acquisition/confinement/count arguments, finite actual-index refinements and numerical interfaces, and compile the assembled manuscript. This pair of sections is not by itself a proof of the all-index theorem. Their length is 19 isolated pages after the required majorant addition, one page beyond the preferred upper target. Reducing it further by deleting analytic proof bodies would undermine completeness; genuine duplicate material in other sections can instead be consolidated by cross-reference.


## Source identities and final isolated QA

Workspace-relative paths; SHA-256 records byte identity, not correctness.

| Path | Bytes | SHA-256 |
|---|---:|---|
| `work/manuscript_revision_20261029/manuscript/extended-v17/sections/02-fixed-target.tex` | 7828 | `ef8c659b15504981da728ba67ef8618dd32851a073d05f3a985f1b26e030a652` |
| `work/manuscript_revision_20261029/manuscript/extended-v17/sections/02b-moment-domain.tex` | 2065 | `7fc5d5a5e8039e3910434a6b9ac903aaba3a7a4ec77e1a09ec8b6a8558646a32` |
| `work/manuscript_revision_20261029/manuscript/extended-v17/sections/05-geometry-counts.tex` | 12487 | `4341f9c7407eed180e9da8f14a06e3d94a43ec135d50ac62ffd40619ced4ad0e` |
| `work/manuscript_revision_20261029/manuscript/extended-v17/sections/03-conservation.tex` | 9404 | `c619b2a81f7034a5f5947772657ec305410b3ea3d22f4089b116c162f1d6deae` |
| `work/manuscript_revision_20261029/manuscript/extended-v17/appendices/normalization.tex` | 4392 | `1a14afaad6b7d62a06fda7f64872d37ee9d1d2aa037539c3069b37b211421aca` |
| `work/manuscript_revision_20261029/manuscript/extended-v17/appendices/off-contact.tex` | 2638 | `957cb81c6710fba827b30eef09b5295a612cc41c1d7152bba6512bc03a27cd83` |
| `work/manuscript_revision_20261029/manuscript/extended-v17/appendices/fixed-fourier.tex` | 15687 | `b91f5c9bf6047c79ca049ef218872174f1813ba7db85cb82f7e199f8f4dcf488` |
| `work/manuscript_revision_20261029/manuscript/extended-v17/appendices/finite-fourier.tex` | 17588 | `d071f3718f4667dedf98579cd43a363dccb6499be2241c7c63f21a73bce03c77` |
| `work/manuscript_revision_20261029/manuscript/extended-v17/appendices/four-summand-details.tex` | 26702 | `e837f49b3abca29803502d7aa00c1ee3fd230188f5a6bf13f891819d1628b787` |
| `work/manuscript_revision_20261029/manuscript/journal-v18/sections/core.tex` | 16764 | `094bb27217caaf2a97c2569cf881e74ad3880860372bea2816993335d491a511` |
| `work/manuscript_revision_20261029/manuscript/journal-v18/sections/fourier.tex` | 36744 | `1aa47f967b1184c33b396d5ef89981910d6ef151b68977b68267b928fe27d064` |

Final isolated snapshot: `/private/tmp/be-journal-v18-core-fourier-20261104-v4/`. Existing TeX Live compile returned0 and produced19 pages,333654 bytes; log has no overfull or underfull boxes. The only unresolved reference/citation in this intentionally isolated wrapper is the external `j:cert:bernstein` label and existing `Shevtsova2012` entry. Visual inspection of pages11–13 found legible complete formulas and no clipping; the new majorant proof crosses the12/13 page break normally. Full-manuscript references and bibliography remain the coordinator’s final compile obligation. Earlier snapshots, including one failed plugin-path invocation, remain in `/private/tmp`; no successful run is substituted for that failed invocation.
