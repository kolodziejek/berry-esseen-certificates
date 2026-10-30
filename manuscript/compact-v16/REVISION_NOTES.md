# Current revision — 30 October 2026

See [Opus revision decisions](OPUS_REVISION_NOTES.md) and
[the current validation](publication/opus-20261030/validation.json).
The dated record below describes the preceding revision and is preserved.

---

# Revision decisions and evidence

The user asked for implementation and authorized independent judgment about
an external model's revision plan. The plan was treated as advice; its claim
that an alternative was verified was not used as a proof. Baseline:
`cd10654222f4b63d50f9d8f108597b140d263ec5`. The user subsequently authorized a GitHub pull request on
`manuscript/revision-v16-20261029`. The publication follow-up and its validation
are recorded separately under `publication/`.

## Changes accepted

- Reordered the text around extremizers, defect rigidity, conservation,
  quantitative localization, and count comparison. Added the exact canonical
  Bernoulli/noise decomposition and a table matching acquired/local hypotheses.
- Explained the actual certificate as checkpoints checked by deterministic
  recomputation. Identified its JSON, exporter, acceptor and isolated wrapper;
  gave an actual stored row and a conditional coverage/soundness proposition.
  Distinguished discovery, verification, execution and analytical proof.
- Kept the contact proof in the main text and moved the full off-contact
  identity, both residuals and counterexample to Appendix C. Kept the complete
  coarse-entry argument in Appendix D and its full theorem in the main text.
- Proved the shared joint defect budget once, retaining the old weaker
  inequality. Simplified probability localization and the two-ray monotonicity
  checks under exactly the original assumptions.
- Replaced the small-noise parameter 13/25 by 1/2 using a global strict-event
  quartic minorant. Proved its full rectangle estimate, including threshold
  atoms and endpoint parameters. No bounded-sum assumption was introduced.
- Proved that the negative-branch error envelope dominates the positive one,
  leaving one final concave quartic and two rational endpoints. Retained the
  derivations for both signs and every incoming/curvature tail.
- Replaced the Fourier tail calculation by weighted Cauchy with the same bound,
  and supplied exact Machin-series arithmetic for the narrow Esseen constant.
- Removed notation collisions and duplicated derivations. Added conceptual
  explanations of zero bias, crossing losses, complete tails, and the need for
  a separate estimate when noise is arbitrarily small.

## Suggestions not adopted

The optional additional Bernoulli stability penalty was not needed for any
retained conclusion. Adding it would introduce a stronger claim and additional
hypothesis matching without simplifying this proof. This is a scope choice,
not a finding that the suggested penalty is false.

A certificate-free entry, alternative Stein/comparison route, pooled moment
replacement and finite-atom reduction remain research directions, not premises.
No speculative replacement was inserted. No claim about the missing finite
base or the full conjecture was upgraded.

## Mathematical reconciliation

The coordinating review read the revised proofs and the independent derivations:
`count-review.md`, `geometry-review.md`, `independent-review.md`,
`count-second-review.md`, `geometry-second-review.md`, and
`final-scope-review.md` under `reviews/`.

In particular, the count minorant is valid on all of R, not merely on the
support of an individual noise summand; its value at zero preserves the strict
event. Concavity plus the proved edge monotonicities cover the entire parameter
rectangle. The common-envelope subtraction has nonnegative coefficients, so
reducing the final comparison to two endpoints does not lose a sign branch.
The joint budget charges all costs under one common marginal, and its unused
terms are nonnegative when obtaining the retained corollary. The Cauchy-tail
replacement preserves every hypothesis and every high-frequency contribution.
The off-contact extension keeps the support integral and correction
`+n^(3/2)(R_supp-H xi)`; moving it does not restrict it to extremizers.

All 119 original labels remain, with 132 unique labels in 17 included TeX files.
The review found no dropped theorem hypothesis, entry predicate, strictness
assertion or conclusion. The source-based audit is bounded; agent agreement
and label counts are not themselves mathematical proof.

## Fresh validation

- Isolated entry replay passed with unchanged 13-file source pins and its full
 11,264/100/30/14 census;19 checker and five wrapper rejection controls passed.
- All nine unchanged historical bounded jobs passed with 36 unchanged input pins.
- All three new scalar checkers passed. They include exact comparisons,
 actual-law diagnostics, and rejected in-memory corruptions. Sampling is not
 used to prove a continuous claim.
- Final TeX Live 2025 build passed; all 53 pages were visually checked. Final
 references/citations resolve and no overfull boxes remain. Page count grew
 from 45 because explanations and reproduction details were added.
- Detailed hashes and evidence locations are in `revision-validation.json`.
 The old `validation.json` and `checks-summary.json` remain historical.

The first build's stale bibliography and two overflowing lines were repaired.
The final TOC fits on the title page. No mathematical target or assertion was
weakened to obtain an execution PASS.

The missing finite base remains the central unresolved global obligation.

## Publication follow-up

The follow-up review's signed-quotient criticism was accepted: denominator
rounding is now restricted to nonnegative numerators, and signed ratios use
all endpoint extrema after proving a positive denominator interval. Reproduction
commands use literal verbatim blocks with shell continuations. The retained
entry wrapper requires `--output-dir`; the README's positional example was
also corrected. The main text now defines c_-, c_+ and phi_l before use,
identifies count coordinates explicitly, and states the finite third moment
before defining gamma in Appendix A. The inversion lemma retains its weaker
second-moment assumption. The first certificate interval is identified as
reconstructed from its stored cell index. The probability polynomial is now
mathcal Q, distinct from the contact majorant Q. These changes do not alter
any theorem's domain or conclusion.
