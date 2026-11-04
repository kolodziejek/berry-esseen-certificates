# Final independent scope and source audit

Baseline: `cd10654222f4b63d50f9d8f108597b140d263ec5`,
`manuscript/compact-v16`. Revised checkout: the current
`manuscript/revision-v16-20261029` working branch. Review date:
29 October 2026. This review covers the included source graph, the
reorganization, preserved scopes, and the new descriptions of certificates.
It supplements `independent-review.md`, which derives the changed
mathematical inequalities independently.

**Conclusion:** no loss of an original theorem, lemma, condition, labeled
equation, strictness assertion, or required finite-verification premise
was found in the revised included source. The global result remains
conditional on the finite base through 699 and the stated entry inputs.
This is a bounded source and mathematical-scope review, not an independent
reimplementation of the entry checker or a proof of the missing base.

| Item | Mathematical status | Execution status |
|---|---|---|
| Preservation of original result scopes and proof dependencies | Source comparison reviewed; changed arguments justified separately | Fresh recursive label/reference/citation scan passed |
| Moved entry argument and two finite conditions | Original formulas and conditions retained; no scope change found | Read/diff audit, not an entry replay in this review |
| Contact/off-contact split | Derived residual signs and checked every moved definition | Source review; no numerical claim |
| Description of certificate format, exporter, and isolated wrapper | Checked against the actual JSON and source | Read-only verification of source facts |
| New mathematical substitutions | Locally derived and independently checked | Prior exact checker: 79 checks, six negative controls, seven actual-law diagnostics |
| Final PDF layout and compilation | Outside this source review | Coordinator to build and inspect |

## 1. Complete source-graph checks

The scanner recursively expanded every `\input` from `main.tex` for the
baseline Git object and the revised working files. It found:

- Original labels: **119**. Missing original labels: **0**.
- Revised labels: **132**. Duplicate labels: **0**.
- Unresolved `\ref`, `\eqref`, or `\pageref` targets: **0** after the
  coordinator corrected the temporary `short:acq:scalar` typo.
- Distinct cited keys: **24**. Missing bibliography keys: **0**.
- Included TeX files: **17**, including all five appendices.

Environment counts change for explained reasons: seven original theorems
become eight, seven lemmas become nine, five propositions become six, and
three corollaries become four. The two certificate conditions remain two.
The new contact-only theorem, joint-budget lemma, explicit crossing lemma,
narrow-constant lemma, and soundness proposition are introduced; the old
simultaneous-gap lemma becomes an identical-scope corollary. Counts alone
are not the scope argument: the individual statements were compared.

## 2. Inventory of original results and their destinations

Labels are stable even though the PDF numbering changes.

| Original result label | Revised location and audit outcome |
|---|---|
| `v9:core:attainment` | `sections/02-fixed-target.tex`; fixed n and c>0, closed-support contact, compact support, and positive discrepancy preserved. The proof still distinguishes bounded third moments from uniform integrability. |
| `v9:core:first-failure` | Same file; finite base, least index, equality case and sharp predecessor preserved. |
| `v9:core:general` | `appendices/off-contact.tex`; arbitrary compactly supported standardized law, every H and c>0 preserved. |
| `v9:core:license` / `v9:core:phase-price` | `sections/03-conservation.tex`; strict raw bound T<N c_- l, negative-T exclusion and both resource conclusions preserved. |
| `ms:sharp-third` | `sections/02b-moment-domain.tex`; unchanged. |
| `ms:sign-moment` | Same file; unchanged and now cited instead of repeating its proof at entry. |
| `ms:physical-defect` | `sections/05-geometry-counts.tex`; full t>0 family, sharpness/equality, zero-in-support consequence preserved. |
| `ms:zero-defect` | Same file; oriented Bernoulli characterization preserved. |
| `ms:simultaneous-gap` | Same file; original inequality and hypotheses preserved as a corollary of the stronger joint budget. |
| `v9:entry:initial` | `appendices/entry-details.tex`; structural, moment and support outputs retained. |
| `v9:entry:signed-K` | Same appendix; unchanged statement and coefficient argument. |
| `v9:entry:two-pass-condition` | Same appendix; all two-pass predicates retained. |
| `v9:entry:signed-step` | Same appendix; both endpoint curvatures, ordered raw/resource update, weighted nD and phase ceiling retained. |
| `v9:entry:signed-condition` | Same appendix; all four passes, 11,264 nominal boxes, 100 panels, outputs and strict support conclusion retained. |
| `v9:entry:theorem` | `sections/04-fixed-entry.tex`; same conditional theorem, with all previously implicit displayed outputs repeated explicitly. Its proof remains in the entry appendix. |
| `short:acq:geometry` | `sections/07-direct-acquisition.tex`; compact support, n>=700 and nD bound preserved; no contact/predecessor assumption added. |
| `short:acq:strip` | Same file; attained pair, nonnegative excess, contact and sharp predecessor remain necessary. Strict outward support bounds preserved. |
| `short:count:local` | `sections/08-direct-comparison.tex`; every local law, full p/support/H domain, 0<lambda<=7/20, strict -lambda/100 conclusion and separate zero case preserved. |
| `short:acquired-exclusion` | `sections/09-composition.tex`; same entry and predecessor assumptions; new table explicitly matches local hypotheses. |
| `short:global` | Same file; base 1 through 699 and complete entry assumptions preserved; strict conclusion only for n>=700. |
| `v9:fourier:inversion` | `appendices/fixed-fourier.tex`; signed-measure hypotheses, absolute convergence and every real H preserved. |
| `v9:fourier:low` | Same appendix; all moment bounds and actual-index quantifiers preserved. |
| `v9:fourier:high` | Same appendix; all six contributions and every optional condition preserved. |
| `ms:gaussian-constants` | `appendices/normalization.tex`; all coarse constants preserved, followed by a separate narrow-enclosure lemma. |

The fixed-Bernoulli asymptotic lower bound remains independently stated at
`ms:bernoulli-limit`. The reflection inequality preserves the atom at H
and is not changed to an equality between the two closed-event branches.

## 3. Relocation did not discard technical obligations

Comparing the original entire `sections/04-fixed-entry.tex` with the new
`appendices/entry-details.tex` shows that the technical body is retained.
The differences are the new section introduction, citation of the already
proved signed-second-moment inequality, expansion of the negative-gap
Tonelli calculation, reference to the new narrow constant proof, removal
of a historical fresh-PASS assertion in favor of reproduction instructions,
and relocation of the final theorem statement. The final theorem's proof
remains in the appendix. No Fourier term, moment contraction, denominator
rule, support test, iteration, or closed-panel incidence was omitted.

The expanded Tonelli display uses `X_- 1_{X_->r}` and integrates only
from r to X_-. It therefore handles the truncation correctly. The original
conditions `1<=r<=rho` and bounded support are retained. The same Gamma
quotient supplies the charge; no new approximation is made.

The new main-text soundness proposition is conditional on the analytically
proved enclosure/exclusion rules and their directed evaluation. Its proof
tracks one realizable witness through the closed subdivisions, restores
the beta interval per gamma slice, handles degenerate matrix divisions,
and pools simultaneous bounds without deleting a witness. It retains the
all-index analytical comparison rather than inferring it from the floor
evaluation. It neither asserts that every feasible moment tuple is a law
nor turns the box count into a coverage proof.

For conservation, the main text proves the contact identity, while the
appendix retains the arbitrary-law extension. The residual rename
`B -> R_supp` is complete in that extension. The correction is
`+n^(3/2)(R_supp-H xi)`: the gap evaluation adds R_supp to A, and the
first-moment equation contributes `+H sqrt(n) xi` to sqrt(n)A.
The support integral is explicitly Lebesgue measure on K. The uniform-law
counterexample remains. Leakage uses `[u,v)` with zero left-endpoint
weight. The local definition `w=H²/(2n)` was restored before the e^w
step, and z is now explicitly restated at the remainder definition.

The geometric equality case now precedes conservation, eliminating a
duplicate proof rather than eliminating the proof itself. The weaker
joint-gap inequality remains available after the stronger budget, with
its exact original right-hand side. The local comparison remains
independent of attainment and the predecessor hypothesis.

## 4. Certificate and bibliography descriptions

Read-only inspection of `entry-proof.json`, `export_entry.py`,
`accept_entry.py`, and `isolated_entry_replay.py` supports the new
reproducibility description:

- The format and target names match the JSON; it contains four stage
  lists of moment-cell checkpoints and a complete panel list, not
  individually stored 11,264 leaves.
- The displayed first-cell checkpoint is the actual stored row.
- The exporter checks a six-stage discovery invocation and selects
  `history[:4]`, rounding selected ceilings outward.
- The replay reconstructs the two coarse passes and four signed passes;
  the source-isolated wrapper binds a 13-file allowlist and checks the
  stated 11,264/100/30/14 census, 19 checker controls and five wrapper
  controls.
- The manuscript describes these as implementation facts and separates
  them from the analytical proof, the scalar revisions, and the missing
  finite base. It does not claim independent implementations or formal
  verification of the whole manuscript.
- The old bounded driver still checks the historical mathematical inputs.
  Its old small-noise parameter is explicitly distinguished from the new
  parameter and checker. The new scalar driver exists and invokes the
  three specified programs, checking status and return code.

The initially documented relative argument `runs/compact-v16-bounded-review`
would have failed because the old driver's `mkdir` does not create missing
parents. The coordinator corrected it to `compact-v16-bounded-review`;
the explanation of its relative directory is now accurate. The stale
phrase “following sections” in the moved appendix was also replaced by
explicit section references.

The new methodological reference was checked against the primary
[Solovyev–Hales text](https://arxiv.org/pdf/1301.1702), §§2.2–3: it separates
solution-certificate search from formal checking. This supports precedent
for the broad method, not a guarantee for the present Python checker.
The probability-specific context was checked in
[Shevtsova's 2011 paper](https://arxiv.org/pdf/1111.6554), §2, printed
pages 5–6, which uses monotone majorants to reduce optimization to finite
computations. No coefficient from that paper is substituted for the
distinct 2013 structural input. Other pre-existing context references are
preserved as reported context and are expressly not proof premises; this
review did not repeat their full literature audit.

## 5. Remaining delivery checks and limits

The coordinator must compile and inspect the final PDF, including the
new tables, long URLs, appendix headings and changed numbering. Successful
reference scanning does not check page layout. Recheck the final source
graph after any further changes and record the actual execution evidence
separately from this review.

One inherited prose sentence was reported and corrected: geometry's
claim that higher moments are used “only for extremal laws” was too broad,
because the local theorem applies to arbitrary laws in its bounded strip.
The revised text states the accurate invariant: bounded support is
available whenever higher moments are used, from attainment in the
extremal analysis and from explicit support hypotheses in the local
comparison. I checked the corrected source. This wording correction does
not change a theorem hypothesis.

No complete finite base, unconditional cutoff 700, new all-n theorem,
formal proof-assistant result, or fully independent entry implementation
is claimed here. The approved scalar substitutions and the reorganization
preserve the selected manuscript's original conditional scope.
