# Review of the signed proposition and theorem-scope promotion

Reviewed 30 October 2026 against the working diff of
`work/manuscript_revision_20261029` from commit
`77d7b4b2510a6ce5b2d8e162bd2a78ecbecec1b5`.
This review made no manuscript edits and did not rerun a full certificate.

## Finding

No target/source mismatch or new scope defect was found in the revised
four-signed-pass proposition, its proof, or the associated removal of its
previous finite-verification assumptions from the localization and composition
theorems. The promotion uses the same fixed proof object and the same actual
law and sample-size domain. It does not provide the independent finite base.

The reproducibility appendix is being updated separately by the coordinator;
the findings below apply to the mathematical edits already present. Its final
commands, archived evidence paths and document compilation require the
coordinator's final check.

## Python version: preserve the existing value

`runs/certificate_discharge_20261030/signed/independent.meta.json` records:

```text
python: 3.12.12 | packaged by conda-forge | (main, Oct 22 2025, 23:34:53) [Clang 19.1.7 ]
executable: /Users/bkolodziejek/miniforge3/bin/python
return_code: 0
```

Therefore `signed-audit.md` correctly says **Python 3.12.12** for the
independent signed diagnostics, and no correction is needed. The coordinator's
separate retained replay in `root01/entry312/receipt.json` correctly records
**Python 3.12.14**. These are distinct executions with distinct interpreters.
The metadata must not be normalized to one version.

## Exact correspondence of D.5 to accepted evidence

The unchanged retained `entry-proof.json` and the full fresh replay identify
the same SHA-256:

`61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae`.

The replay in
`runs/certificate_discharge_20261030/root01/entry312/stdout.json` reports
`PASS_INITIAL42_FIXED_TARGET_COARSE_V7`; its wrapper reports
`PASS_ISOLATED_REPRODUCTION_FIXED_ENTRY_V7`. The existing signed diagnostic
stdout independently checks the fixed object's sharper final constants.

| Revised proposition assertion | Evidence and scope |
|---|---|
| Four signed passes and 11264 nominal boxes | 24+24+24+16 processed original rho rows, each with 128 descendants; full replay reconstructs them |
| 14 surviving rho cells and 30 nonempty panels | Both replay summary and independent JSON census agree |
| Raw bound 2.1995174 | Exact accepted ceiling `10997587/5000000` |
| D bound 0.76682509 | Exact accepted ceiling `76682509/100000000` |
| nD bound 32.20665378 | Exact product `42*76682509/100000000`; the incoming/update invariant is weighted nD, not an assertion restricted to n=42 |
| Exact rho bound 71527/48000 | Original closed right endpoint at largest surviving index 13, i.e. r14; not the rounded serialized panel rho |
| Beta bound 0.50549963 | Exact panel maximum `50549963/100000000` |
| Phase bound 1.83605680 | Exact panel maximum `2295071/1250000` |
| Support inside the open interval with radius 157/50 | Largest surviving selected radius plus the previously proved strict whole-ray support exclusion |

The new proof explicitly distinguishes the rounded panel value 1.49014584
from the exact original rho endpoint. This resolves the main opportunity for
a false comparison of reported constants to the JSON. It also explicitly
instructs readers to use actual accepted maxima rather than the acceptor's
looser generic targets. The old generic limits are not silently changed.

The new proof's statement that exclusions use necessary conditions and that
zero denominators are treated before division agrees with the audited signed
code. Its reference to the finite-cover soundness proposition supplies the
induction and endpoint coverage argument. Strict support follows from the
analytic support theorem and its verified gates; it does not follow from the
mere presence of a radius field.

## Theorem scopes

The revised localization theorem still assumes an attained fixed-target
maximizer with nonnegative excess, actual n>=42, the sharp predecessor, and
the displayed external structural inequality. Its outputs and their joint
same-law meaning are unchanged. The two arithmetic propositions now prove
the former finite conditions. Floor evaluation at N=42 remains explicitly
justified for all actual n>=42 by the Fourier appendix.

The revised exclusion theorem still requires n>=700, attained nonnegative
excess, the predecessor inequality and the structural inequality. Its match
to the local theorem's common strip and phase domain is unchanged. Neither
the radius nor any accepted threshold has been weakened to obtain PASS.

The global statement is still a **finite-base implication**. It explicitly
assumes every `C_j<=C_E` through j=699, and cites the structural and strict
finite-binomial theorems. The proof retains attainment, reflection and the
least-failure step. Consequently describing the finite certificate conditions
as discharged is compatible with continuing to state that the finite base is
unproved. It would be incorrect to summarize this as a proof of the full
unconditional Berry--Esseen conjecture.

The abstract's phrasing “we prove that [finite base] implies [global result]”
matches this scope. The introduction's “certificate checks have been
discharged” is justified by the exact replay together with the analytic
audits, not by the replay alone. External structural/binomial results remain
cited inputs; this bounded promotion review does not reverify their original
publications.

## Evidence wording to retain in the final appendix

The frozen acceptor and wrapper deliberately still print a conditional
`mathematical_status` referring to contact, conservation, support, and
moment/gap premises. Preserve those machine outputs verbatim. Explain that
the programs establish arithmetic statements, while the manuscript and the
correspondence audits establish their stated analytic prerequisites. The
new theorem promotion does not require editing these historical status
strings, nor would changing them constitute mathematical evidence.

Similarly, distinguish the signed diagnostic run under Python 3.12.12 from
the full retained replay under Python 3.12.14. No remaining execution or
mathematical defect specific to the signed promotion was identified.
