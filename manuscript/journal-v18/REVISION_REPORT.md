# Result of the complete-manuscript shortening attempt

The delivered manuscript has **102 total pages**. It retains the analytic reductions and is intended for mathematical review. The approximately 60-page target remains unmet. This attempt does not establish that a readable 60-page proof is impossible; it establishes that the implemented consolidation is insufficient.

## Measured comparison

| Version | Total PDF pages | What the shorter apparent count omitted |
|---|---:|---|
| Public original `2610.00590v1` | 159 | Its appendices begin on page 34 |
| Complete extension `extended-v17` | 194 | The 63-page main part was followed by analytic appendices beginning on page 64 |
| This `journal-v18` | 102 | Nothing: the count includes all analytic arguments and references |

The comparison uses the actual PDFs and the same 11-point A4 layout with 28 mm margins. The new version is 92 pages shorter than v17 and 57 pages shorter than the public original. No essential analytic supplement has been excluded from the new count.

The earlier growth was not solely the price of clearer explanations. The compact construction initially treated a finite base as an input. Completing that base and incorporating the local argument added a second substantial proof path, while the separate large-index route and many repeated derivations remained. The new version removes that structural duplication.

## Implemented changes

**One optimization framework.** Section 2 proves ratio attainment and contact directly, with explicit treatment of moving thresholds, closed events and atoms. The sign normalization, support-gap defect and conservation identity are shared by the later arguments.

**One all-index composition.** The finite induction proves the base through 42. A first later failure has small scaled excess, zero predecessor loss, and two sharp deleted predecessors. The finite local comparison excludes 43–48; the uniform comparison excludes all later indices. No finite verification through 699 is required.

**Remove the redundant strict tail proof.** The uniform local comparison already uses a zero-barrier acquisition and a loss proportional to every positive amount of noise. The boundary audit checks that it admits equality at the sharp constant. At zero noise the marginal is exactly Bernoulli and the strict finite-binomial theorem applies. After the weak all-index bound, attainment therefore excludes equality for every `n>=47`. This replaces the separate strictness route from 700 without changing a numerical target. The extension is not asserted for 42–46.

**Shared analysis and explicit numerical interfaces.** A single Fourier chapter supplies the inversion and remainder results. The finite chapter keeps the exceptional small-index arguments and joins their exact domains. The local chapter consolidates repeated moment, support, normalization and count-comparison calculations.

**Certificate explanation.** The introduction gives an accessible account; Section 4 proves the common expectation, polynomial positivity and closed-cover principles. It distinguishes floating-point discovery, exact acceptance, whole-domain coverage, analytic applicability and the trusted software/runtime. Large data arrays remain in the companion repository.

## Corrections made during review

The shortened draft initially needed a full one-sided closed-half-line Fourier majorant for the four-summand argument; an absolute discrepancy bound did not supply that interface. Section 5.5 now proves the exact kernel theorem, including its value on the event boundary and the limiting/Fubini steps.

The defect-feedback lemma now states its raw remainder sign gate explicitly. Shared confinement includes the positive-39 prerequisite. The bounded-threshold support formula is parameterized by the actual floor and its own constants, and the finite42 radius, strip and four amplitude profiles are stated separately from the uniform47 inputs. These repairs correct the consolidation; they are not reported as newly found counterexamples to the earlier theorem.

## Remaining length

The section starts in the final PDF are:

| Section | First page |
|---|---:|
| Problem, strategy and external inputs | 1 |
| Extremizers, geometry and conservation | 4 |
| First-failure recurrence | 9 |
| Certificate soundness and construction | 11 |
| Fourier analysis | 14 |
| Finite induction through 42 | 27 |
| Acquisition and local comparison | 51 |
| Completion | 101 |
| References | 102 |

Sections share boundary pages. Roughly half the PDF remains devoted to the local argument. Some of it is repeated algebra that could potentially be certified under a common soundness theorem. Much of it is probability and analysis: confinement, signed deletion, actual conditional counts, outgoing versus incoming mass, and losses uniform down to arbitrarily small positive noise. Deleting those proofs today would leave a gap.

The most concrete next attempt is described in [SIMPLIFICATION_PLAN.md](SIMPLIFICATION_PLAN.md): pilot a small certificate calculus for the acquisition and coefficient derivations; then measure the genuine saving before extending it. A more unified conditional-count theorem is a further mathematical target, not an established shortcut. The five-object polynomial pilot supplies a limited working example, not evidence of a 42-page saving.

## Evidence and limits

| Item | Mathematical status | Execution status |
|---|---|---|
| Consolidated all-index argument | Locally derived and reviewed proof candidate, with stated external inputs; no remaining gap identified in the reviewed scope | Selected numerical obligations reuse the unchanged completed v17 evidence |
| Equality-inclusive uniform comparison | Locally derived boundary improvement, independently reviewed at its analytic/numerical interfaces | No new target or numerical integration campaign |
| Full manuscript PDF | Reviewable presentation of the argument | Fresh successful TeX build; exact source and PDF hashes; layout review recorded in `review/` |
| Five-object algebra pilot | Bounded exact identities only; not a theorem dependency | Fresh acceptance and 23 corrupt-input rejections |
| Independent human/referee acceptance | Not established | Not performed |

The paper is ready for a careful human mathematical reading, not represented here as submission-ready on the strength of machine checks. The 60-page constraint needs further substantive work. No speculative certificate calculus or unproved propagation theorem has been used to shorten the delivered proof.
