# Selective implementation of the Opus 5.5 suggestions

30 October 2026. Starting revision: `6339dda253238048aa75dcf1f2e8c4b73b7b6522`.
The user requested implementation of useful advice, not automatic acceptance of
the external document. Its SHA-256 is
`f67c895d2505e77776de584454452d1029579472857e712eecea73996d22fc6a`.
The manuscript remains the deliverable; this file records the decisions.

## Implemented changes

| Location | Issue and implemented improvement |
|---|---|
| Abstract and introduction | Lead with the conditional global implication and missing finite base. Separate the local comparison, localization and global result in an interface table; add a dependency figure. Retain the complete noise and verification qualifications. |
| Introduction and Appendix E | Explain the certificate as stored checkpoints plus deterministic reconstruction. Distinguish finding a successful sequence, exact acceptance, analytical coverage and independent checking. Add the six-step acceptance procedure, selected code-reading map and a measured, dated runtime. |
| Fixed-target section | Define the contact majorant before its proof, explain contamination and recentering, call it piecewise cubic, and use `a*` for the supremum. Retain the full compactness and atom arguments. |
| Geometry section | Prove `J>=h` for lattice laws, including countably infinite supports, and derive the sharp reflected moment-span inequality and equality case internally. Explain the moment circle and the two nonnegative losses. |
| Geometry and notation guide | Keep one exact Bernoulli/noise normalization in subequations. Distinguish central-gap endpoints `A_-`, `A_+`, conditional means, physical displacement and displacement in count units. Preserve the old labels through meaningful equation references. |
| Conservation section | Explain the two evaluations of the same zero-bias integral, name their proof stages, show the identity solved for excess, and give the explicit `D<=6T exp(H0^2/(2N))/(n phi(0))` consequence under its quantitative hypotheses. Explain why leakage is nonnegative without the predecessor bound. |
| Localization section | Add the predecessor-support lemma, derived directly from contact. It identifies the sole numerical use of the predecessor bound in the selected route, both for initial support and the final rays. |
| Acquisition section | Divide the proof into five purposeful stages. Explain why a fixed bound on conditional variance is insufficient for total count variance and why the cubic cost and AM–GM are retained. Separate the radial Gaussian majorant and its derivative bound from existing symbols. |
| Count comparison | Begin with exact conditioning, outgoing losses and incoming gains. Explain the quartic via Cauchy–Schwarz/Hölder and the sine average via its characteristic function. Name four reusable lemma interfaces, preserve all strict/closed atom conventions, and display the exact small-noise margin `4787/140000`. |
| Count notation | Distinguish binomial masses, mass ratios, normal increments, positive-part expectations, Jensen gaps, crossing kernel, sine bump, noise cutoff, sample-size floor and final comparison polynomial. The principal theorem statement is unchanged. |
| Gaussian constants and Fourier appendix | Prove the required square-root bounds from the same rational Machin endpoints and reference that proof from the Fourier appendix. Qualify the applicability of Appendix D by its retained entry conditions. Use `phi_z=phi(H/sqrt(n))` consistently; distinguish the scalar `eta_n` from the signed Gaussian comparator. |
| Appendix D | Explain the 24-cell/four-pass cover, why only 11,264 nominal boxes are processed, and the treatment of shared endpoints. Explain the central-gap column without changing its predicates. |
| Composition and discussion | Refer to the already proved reflection argument. Explain that 700 is a sufficient floor for both acquisition and count errors, and that a base through 41 leaves 42–699 unresolved. |

## Corrections and rejected proposals

- **Dropping Conditions D.3/D.5 or the structural premises would strengthen the
  theorem.** The external plan did not audit the entire Fourier-to-code
  correspondence. Arithmetic replay establishes its predicates; it cannot
  supply an unperformed analytical reduction or semantic audit. These premises
  remain in the localization and global statements.
- The suggested short local statement omitted `0<lambda<=7/20`. This bound and
  the full conditional-support domain remain explicit. Zero noise remains a
  separate strict Bernoulli case.
- `R_c=O(1)`, `D=O(1/n)` and proximity to a law require quantitative hypotheses;
  the implemented defect estimate states them. No uniform varying-law result
  is inferred from a fixed-law asymptotic theorem.
- The floor 700 is used in the count estimates as well as the defect bound.
  Improving localization alone does not establish a lower cutoff.
- The conditional sum `W_k` is bounded by `nA`, though generally not by the
  summand bound `A`. Its quartic minorant is global. The incoming-tail error is
  linear in `lambda`; it is not generally `O(lambda/n)+O(lambda^2)`.
- The joint defect budget is a lower bound, not an equality. Its displacement
  and signed noise terms must be handled together before discarding them.
- Kept the self-contained moment and Stirling proofs. Nine small lemmas,
  wholesale alphabet changes, or an additional local schematic would fragment
  the calculations without a corresponding gain in understanding.
- Did not add comments to pinned acceptance programs. The reading map explains
  their roles while preserving all reviewed bytes and acceptance predicates.
- A non-strict-binomial variant can yield a non-strict conditional global bound,
  but it does not preserve all current strict statements. The verified strict
  theorem already supplies the needed input, so this variant remains in the
  review notes rather than complicating the manuscript.
- Certificate-free entry, a new cutoff, an all-noise comparison, uniform
  asymptotics near lattice laws and other proposed research routes remain
  unproved alternatives. None is substituted for the present argument.
- Removed an irrelevant registry/formalization context sentence. A failed fetch
  is not evidence that a cited repository is nonexistent; no such claim was made.

## Mathematical and execution status

| Result | Mathematical status | Execution status |
|---|---|---|
| New lattice corollary, excess formula, predecessor-support lemma and explanatory count inequalities | Locally derived from the stated hypotheses and independently reviewed | Exact scalar comparisons and selected diagnostic laws passed; these are supplemental evidence |
| Existing local comparison | Domain and conclusions retained; principal theorem text preserved | Three scalar component checks passed freshly |
| Historical bounded inputs | Original scope retained | Nine unchanged programs passed; 36 reviewed source pins unchanged |
| Retained entry | Conditional on analytical validity, coverage and code correspondence | Fresh isolated 13-file replay passed; 11,264 boxes, 100 panels, 30 nonempty panels, 14 moment cells; 19 checker and five wrapper rejection controls |
| Manuscript preservation | All 119 original and all 132 preceding-revision labels retained | 140 unique labels in 17 included TeX sources; complete build and visual record in the current manifest |
| Finite base through 699 and unrestricted sharp conjecture | Open here | No acceptance claimed |

The coordinator read the accepted proofs and reconciled the independent reviews:
`reviews/opus-external-scope-review.md`, `opus-root-independent-review.md`,
`opus-geometry-conservation.md`, `opus-geometry-independent-review.md`,
`opus-count-exposition.md` and `opus-count-independent-review.md`.
Verified reference scopes and primary-source links are recorded in the external
review. Neither agreement among reviewers nor passing scalar programs replaces
these mathematical arguments.

Current evidence is under `publication/opus-20261030/`. Previous manifests,
compiler captures and execution records are preserved as historical records.
