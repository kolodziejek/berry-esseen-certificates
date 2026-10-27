# Finite appendix editorial revision, 27 October 2026

Scope: only `appendices/finite-analysis.tex` and this report, on
`manuscript/v2-finite-20261027` from `ec370aa`. The supplied revision notes
were evaluated as editorial proposals. No certificate, native program,
reference source, main-text file or other appendix was changed.

| Result | Mathematical status | Execution status |
| --- | --- | --- |
| Reorganization and duplicate removal below | Editorial equivalence checked against the exact main-text formulas; no new finite-index theorem | Source comparison and label checks completed |
| Retained finite-index implications | Conditional on their existing analytic inputs and complete certificate conditions | No native certificate acceptance or generation run |
| Typesetting | Does not establish any analytic or numerical premise | Fresh complete-manuscript compilation, exit 0; visual inspection described below |

## Roadmap and notation

The opening now separates the conditional reductions for indices 1--5 from
the later tools. It identifies the exact-phase helper's literal domain
`n in {6,7,8,9}`, the B1 sine interface at `26,...,30`, and the conditional
resource transfers at floors 25, 31 and 40. It explicitly says these tools
do **not** supply a complete cover of `6 <= n <= 41`; the global finite-base
condition remains open. The fifth-index support/Fourier, moment-domain,
resource, six-root and gap-free cover conditions remain explicit.

The count setup gives the dictionary `h = ell^{-1} = v/m = sqrt(v+s)`.
Here `m = E X_+`; later index transfer writes the actual index as `m` and
the positive mean as `mu`. The separate symmetrization convention for `h`
is identified, rather than silently forcing two different variables to agree.

## Exact replacements for repeated material

Locations below refer to the revised appendix and unchanged Section 5 in
this branch. Every original `ms:finite:*` label is preserved.

| Appendix change | Main-text source that supplies the same argument | Scope retained and material kept locally |
| --- | --- | --- |
| Sign split and its conditional-centering derivation shortened at appendix lines 94--118, label `ms:finite:countcore:representation` | `sections/05-geometry-counts.tex:32`, `ms:bernoulli-coordinates`; moments at line 57, `ms:conditional-moments` | One standardized iid marginal with finite third moment, positive and nonpositive classes with zero atoms in the latter, `s=0` face without division, actual conditional moments, and bounded support before higher moments. The reciprocal-span representation, conditional variances and variance-allocation formulas remain displayed. |
| Duplicate full count-identity display and conditioning proof replaced by the main identity at appendix lines 123--137 | Section 5 lines 253--280, `ms:count-identity` (line 267) and `ms:count-difference` (line 274) | The remaining inequality is the same closed count bound, obtained by dropping only the nonpositive outgoing terms at counts below `k`. The outgoing event stays strict, incoming events closed, and all event-plane atoms remain included. Both existing finite labels are retained; the lemma's descriptive title is now “Closed count comparison.” |
| Repeated derivation of the three moment identities shortened at appendix lines 180--195 | Section 5 line 57, `ms:conditional-moments` | All three reciprocal-span identities and their labels remain. The signed cubic moments have their original signs. The subsequent mean/noise, harmonic, beta and rho contractions remain byte-identical. |
| Repeated definitions of the physical defect, gap residuals and outer-gap integration shortened at appendix lines 271--280 | Section 5 line 84, `ms:physical-defect-definition`; lemma at line 91, `ms:physical-defect`; identity at line 124, `ms:defect-decomposition` | Compact support and a genuine central gap with positive endpoints are explicit. The displayed bound `D >= sigma rho - gamma - 6mAB + 6B R_+ + 6A R_-` remains. Every following reciprocal-span halfplane, sharpened contraction, zero-endpoint case, sign gate and whole-interval derivative requirement remains byte-identical. |

For the last replacement, the main lemma gives
`J_o <= T_+ + T_- - 2B R_+ - 2A R_-`, with
`T_+ + T_- = rho - m(A^2+B^2)` and central contribution
`m(A+B)^2`. Substitution into `D=(3+sigma)rho-gamma-3J` yields precisely
the retained displayed bound. This uses the same marginal and genuine gap.
No linear extreme-point argument or new support acquisition is inserted.

The proposed blanket deletion of the early count material was not used:
Section 5 does not replace the unique reciprocal-span contractions,
outgoing polynomial witnesses, incoming exponential and stop-loss bounds,
common-cubic-moment treatment, phase coherence, normalization, or complete
root requirements. Those arguments remain in the appendix.

## Other editing and retained conditions

Repeated reports that an algorithm description is not a successful run
were shortened after keeping a clear opening statement of conditionality.
The conditions themselves retain the complete domains and inequalities.
In particular, all four `condition` environments remain. The one-summand
and B1 conditions are byte-identical. The three-summand condition changes
only its closing sentence pointing to the exact tests; its displayed
polynomial inequalities are unchanged. The floor-40 condition changes its
title and restates positively that all 304 LOW row processes are retained.
Its ten acquisition components, binders, companions, actual predecessors,
indexed support primitive, probability and moment coverage, and shared
boundary remain requirements.

The exact-phase section still assumes the conserved inequality and a proved
whole-threshold bound, at its literal indices, and retains the implementation
gate `L^2/(2n) <= 7`. The B1 conclusion remains limited to its five actual
indices and retains resource acquisition and sharp predecessors. The
floor-31 passage retains actual-index support, contact allowance, own-score
cap, downstream refinements and complete surviving counts. The floor-40
passage retains all signed inverse-index maxima and its restriction to
`m=40,41,42`. No coefficient domain or numeric acceptance predicate is
extended. “Completed old INITIAL variant” was changed to “retained INITIAL
variant,” avoiding an unsupported completion claim.

Concatenated prose such as `floor25`, `floor31`, `index42`, `weak40/41`,
`finite40--42` and `tail43` was expanded into ordinary prose with mathematical
indices. Leading zeros were added to decimals, including those immediately
following TeX control words. Literal source names such as `CENTRAL40`, all
label/reference keys, numerical values, and mathematical powers were kept.

## Verification performed

- Checked Git status before editing; only the owned appendix was modified.
- Compared old/new labels using Python `re`/`collections` and `git show HEAD:`:
  exactly 165 label occurrences before and after, no additions, removals or
  duplicates. Every `ref`/`eqref` in the appendix resolves in the local source.
- Compared all four condition environments and inspected both changed ones.
- Direct text comparisons confirmed the necessary-contraction block and
  the reciprocal-span physical-defect translation/gates are byte-identical.
  The strict outgoing through complete-root section and the signed-moment
  refinement section are also unchanged apart from decimal normalization
  (which made no change in those sections).
- `git diff --check` passed. A final scan found no omitted leading zero
  immediately before a decimal digit, and no remaining concatenated prose
  cases; preserved label/source identifiers are intentional.

The complete manuscript was compiled with the existing TeX Live 2025 stack
through the LaTeX compile skill. The final command was:

```sh
python3 /Users/bkolodziejek/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py /Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/fork_audit_20261027/manuscript-v2-finite/manuscript/arxiv-v1/main.tex --compiler texlive --output-directory /private/tmp/be-finite-v2-20261027-build --json > /private/tmp/be-finite-v2-20261027-build/compile-final.json
```

Result: exit 0, 161-page PDF, no warnings, undefined references/citations, or
overfull/underfull boxes in the final log. Output and compile receipt are in
`/private/tmp/be-finite-v2-20261027-build/`. The final PDF SHA-256 is
`f2b1321bf9c36e476a2d3bb7442607fe7dd6bdc18b4812725722f9e75c130edd`.

Rendered PDF pages 110--159 using `pdftoppm -r 80 -png`, inspected all five
contact sheets covering those 50 pages, and inspected full pages
111, 112, 113, 114, 142, 157, 158 and 159. Three leading-zero omissions after
TeX control words were caught and corrected during the first inspection;
the final compilation and pages 158--159 were rerendered and reinspected.
No clipping, overlap, missing glyph or equation-number collision was found.
The final source still requires the coordinator's integration review and
full manuscript review. This editorial work does not certify BASE41 or any
unrun finite predicate.
