# Finite appendix: third editorial revision

Branch `manuscript/v3-finite-20261027`, starting commit `6299d97`.
Only the finite appendix and this report are changed. The supplied editorial
proposals were checked against the statements actually available in the
manuscript. No certificate or numerical acceptance condition is completed by
this revision.

| Item | Mathematical status | Execution status |
| --- | --- | --- |
| Replaced attainment/contact and moment/gap derivations | Applications to the existing analytic results checked at the exact hypotheses described below | Read-only source comparison; bounded algebra checks below |
| Finite numerical conclusions, including the sharp base | Conditional on the retained analytic and complete-certificate premises | No native certificate replay or generation |
| Heading hierarchy, labels and layout | Editorial changes only | Fresh source checks, complete-manuscript compile and rendered-page inspection |

## Structure and preserved scope

The file now has one top-level appendix, `ms:finite:scope`, titled
“Finite-index reductions and certificate conditions.” Its eleven former
internal sections become subsections; their internal headings become
subsubsections and paragraphs. All 165 original labels remain. The title
avoids the proposed restriction to `1 <= n <= 41`, since the retained final
comparison explicitly includes actual indices 40, 41 and 42. The opening
still says that the later tools do not form a complete cover of 6--41.
The coordinator places this appendix sixth and controls the final letter F;
no main-file ordering or preamble was changed here.

All 87 labelled `equation`, `align` and `gather` displays are identical to
the starting source after whitespace normalization. No numerical value,
coefficient domain, inequality, theorem statement, or certificate cover was
deleted. The repeated displays that translate notation are kept where their
labels or later substitutions are useful; only their redundant derivations
are shortened.

## Proof replacements and exact hypotheses

Main/Fourier line locations below refer to `6299d97`, so they remain
unambiguous while the other chapters are edited. Labels are the stable
integration references. Finite locations refer to this revision.

1. **Two- and three-summand attainment** (`finite-analysis.tex:851`,
   `ms:finite:n2:lem:attain`; line 1113, `ms:finite:n3:lem:attain`).
   Lemma `ms:attainment` in `sections/02-extremizers.tex:17` applies to
   every fixed integer `n >= 1`, over all standardized laws with finite
   third absolute moment. It produces a finite threshold with a positive
   **closed-CDF discrepancy**, including atoms. Thus it applies at 2 and 3
   before any support restriction. At a contrary maximum, the independent
   structural bounds `ms:finite:n2:eq:large` and `ms:finite:n3:eq:large`
   exclude respectively `rho >= 2` and `rho >= 15/8`. The restricted-class
   compactness proofs and repeated orientation argument are unnecessary.
   Neither a sharp finite-base bound nor a predecessor result is used.
   The subsequent distinct six-unit support proofs are retained in full.

2. **Two- and three-summand contact** (lines 872 and 1131,
   `ms:finite:n2:lem:contact`, `ms:finite:n3:lem:contact`).
   Lemma `ms:contact` in `sections/02-extremizers.tex:96` requires an
   unrestricted attaining pair and `n >= 2`; the preceding lemmas provide
   exactly that. In `ms:contact-majorant` (line 169), use `H=t`, `z=x`,
   `beta=m`, `C/sqrt(n)=lambda`, and `C rho/sqrt(n)=D`. The finite
   polynomial called `Q` is precisely `n Q_t` in the main notation.
   Therefore its left side is `n F_{n-1,P}(t-y)`, with the same inequality
   for every real y and equality at **every point of the closed support**.
   This replaces the repeated contamination derivatives and integral/upper
   semicontinuity arguments; it preserves their fixed raw event and atom
   convention. The finite contact displays and all support consequences
   are unchanged. The main proof has no reference back into this appendix.

3. **Signed second moment at five** (`ms:finite:five:eq:beta`, line 2126).
   Lemma `ms:sign-moment` in `sections/02b-moment-domain.tex:41` assumes
   only mean zero, variance one and finite third absolute moment. It proves
   both `|beta|<1` and the exact displayed inequality and admits a zero
   atom. It replaces the repeated signwise Cauchy derivation. The inversion
   defining `b(r)`, rational outward bounds and moment-domain cover remain.

4. **Pearson identities and Gaussian norm** (`ms:finite:paired-rectangle`,
   line 2543; `ms:finite:pearson-identities`, line 2561;
   `ms:finite:paired-mills`, line 2627).
   The polynomial identities `ms:fourier:rescore:fourier-pearson` at
   `appendices/fourier-analysis.tex:997` use the same standardized law.
   Bounded support in the finite statement makes all sixth moments finite;
   reflecting only the auxiliary norm replaces signed gamma by
   `t=|gamma|`. Their local notation and displayed identities are retained,
   with the derivation referenced rather than repeated.

   The proof of `ms:fourier:rescore:fourier-early-low` at lines 825--932
   separately proves convexity, simultaneous-sign symmetry, and the exact
   split-at-root identity for `J(z,c)`. That **norm calculation** applies
   to every real z,c independently of the sample-index assumptions of the
   complete transfer lemma. Substituting
   `integral_a^infinity exp(-x^2/2) dx = sqrt(2 pi)(1-Phi(a))` gives
   exactly the retained finite formula. Its signed Gaussian-tail term is
   kept before any upper bound. The complete transfer still requires
   `n>2`, positive damping and its other stated moment hypotheses.

   **The proposed blanket removal was not valid.** The finite coefficient
   enclosure allows `R<2g` and `M>=3`, unlike the particular paired
   rectangle at Fourier lines 1048--1080. It retains the positive part
   `(R-2t)_+`, the split at `R/2`, all derivative-root/end-point extrema,
   signed `c_l,c_u`, the exact norm rather than merely the looser upper
   `U`, the sixth-moment enclosure, and damping `(45-M)(1-2/n)/96`.
   The counterexample to dropping `R>=2g` from the older rectangle also
   remains. These are unique hypotheses and strengthened bounds, not
   duplicate text.

5. **Quadratic signed-moment loss** (`ms:finite:signed-loss`, line 2656).
   The weighted Cauchy calculation leading to
   `ms:fourier:rescore:eq:weighted-constant-loss` at Fourier lines 1928--1943
   uses `Y=|X|`, `Z=Y^2-rho Y`, `E|X|=2m>0`, and finite fifth absolute
   moment. It needs neither bounded support nor an acquired gap, despite
   appearing inside a supported-resource chapter. The reference explicitly
   applies that calculation at its actual weaker hypotheses. The local
   equality verification for every standardized two-point law, the zero
   atom convention and the eight-corner loss calculation remain. The loss
   is still applied only in its matching constant term.

6. **Outer-gap decomposition** (`ms:finite:outer-decomposition`, line 2732).
   Lemma `ms:physical-defect` in `sections/05-geometry-counts.tex:90` and
   equation `ms:defect-decomposition` at line 125 use the same standardized
   compactly supported law, its genuine central gap `(-A,B)`, and the same
   physical D and outer-gap sum. The finite statement now displays the
   already assumed signed support interval and positive mean explicitly;
   support radii `mathcal R_+,mathcal R_-` are distinct from moment
   residuals `R_+,R_-`. These results replace only the repeated outer-gap
   integration proof. The weighted improvement
   `ms:finite:outer-weights`, its positive weights, endpoint/radius
   replacement directions, common residual, negative-residual exclusion,
   and separately required outer-integral inequality remain in full.

A read-only review by `scalar_review` checked these references against the
combined main/Fourier statements and found no dependency cycle. Its wording
correction is included: “positive” modifies the closed-CDF discrepancy, not
the raw threshold. A second bounded review by `acquisition_audit` independently checked the
attainment/contact substitutions and the moment/gap/norm hypotheses and found
no blocking mismatch. These reviews are not numerical acceptance results.

## Certificate conditions and terminology

The four `condition` environments remain. Their changes are confined to:
removing the repeated warning after the complete 150-cell requirement;
changing “source hypotheses” to “analytic hypotheses”; and translating
program language in the final condition. In that condition, “both binders”
becomes **both binding conditions linking the comparison rows to acquired
bounds**, and all 304 original row-verification obligations remain. All ten
acquisition conditions, initial support, complete probability/moment cover,
small/intermediate-noise and full-count comparisons, binomial conditions,
closed boundaries and actual predecessors remain required.

In the prose, “checker” becomes an exact verification procedure; the two
Bernstein constructions remain distinct and fully specified. “TINY”, “MID”
and the local “LOW” comparison become small-noise, intermediate-noise and
full-count comparisons, respectively. Their numerical seams are unchanged.
The unrelated Fourier “LOW” terminology becomes low-frequency. “Callback”
and “wrapper” become the corresponding phase or signed-variance bound.
The exact input index ranges, strict positivity gates, weighted `mD`
invariant and actual-law requirement are retained. Source headers and
repeated disclaimers were removed; the numerical conclusions remain
explicitly conditional.

## Bounded verification and layout

Source checks performed with Python standard-library text comparison and
`git show HEAD:` gave 165/165 identical labels, no duplicates, no unresolved
source references, 87/87 unchanged labelled displays, and four/four
certificate conditions. Heading counts are one section, eleven subsections,
fifty subsubsections and eight paragraph headings. `git diff --check` passed.

A bounded standard-library algebra check independently expanded all three
Pearson identities as formal polynomials, substituted `E X=0`, `E X^2=1`,
`E X^3=t`, and matched the displayed right sides. Exact `Fraction`
arithmetic verified both strict structural moment cutoffs by squaring
positive sides. It also reproduced the retained negative control:

```text
Pearson identities: all three exact formal expansions agree.
Both contrary-witness structural cutoffs: exact positive-square comparisons agree.
Required R<2g counterexample: true120z=1315/216,
old bound=951/160, shortfall=623/4320.
Signed-loss two-point equality exact;
doubled penalty negative control rejected by margin 75/2197.
```

The two-point control has masses `4/13` at `3/2` and `9/13` at `-2/3`.
These are bounded identity/application checks, not native finite-certificate
execution or proof of complete coverage.

The complete local-baseline manuscript was compiled using the LaTeX compile
skill, TeX Live 2025, with:

```sh
python3 /Users/bkolodziejek/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py /Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/fork_audit_20261027/manuscript-v3-finite/manuscript/arxiv-v1/main.tex --compiler texlive --output-directory /private/tmp/be-finite-v3-20261027-build --json > /private/tmp/be-finite-v3-20261027-compile-final.json
```

Result: exit 0, 163-page PDF; no warnings, undefined references/citations,
multiply-defined labels or overfull/underfull boxes. Final PDF SHA-256:
`62373f94522a36fd3b03188b677ad2f08a8d170127cdee5789195a5ead2e84c8`.
The unchanged local main/Fourier ordering still labels the single finite
appendix H; the coordinator's global reordering will give F.

Rendered all 48 appendix pages 113--160 at 70 dpi and inspected all four
contact sheets. Additionally inspected pages 113, 124, 126, 128, 131, 148,
149, 150 and 160 at 110 dpi, covering the revised structure, four shortened
proofs, paragraph headings, unique paired bounds and final condition. No
clipping, overlap, missing glyph or equation-number collision was found.
Files are under `/private/tmp/be-finite-v3-20261027-build/render/`.
The integrated build and final layout check are recorded below; the local
build above remains the source of the preserved compilation evidence.


## Preserved evidence and integrated layout review

All bounded checks and the completed local-baseline build now have retained
receipts in `runs/manuscript-finite-v3-20261027/`; see its `README.md` for
commands, input hashes, separate mathematical/execution status and limits.
The fresh preserved source check confirms all 165 labels, 87 labelled display
entries, four certificate conditions and 174 resolved finite references.
The first preservation-script attempt had a Python 3.9 f-string syntax error;
its source, return code and streams are retained as `failed01`. The corrected
script exited 0. No certificate predicate was changed or replayed.

For the coordinator's 158-page integrated build01, PDF SHA-256
`8b880fac987aceedd5f4222555e32d4ab54bbd33e923413143de3f64da01ee4f`,
I inspected all five overview sheets spanning pages 109--158 with the image
viewer. I also rendered and inspected full pages 120, 124, 126, 144, 145,
154, 156, 157 and 158 separately. The appendix is now F and its numbered
paragraph headings form distinct blocks. No clipping, overlap, missing glyphs
or equation-number collision was found. Bibliography entries, including long
URLs, fit within the text area.

The page 126 proof still said “a positive maximizing raw threshold”; this
could imply `t>0`, which the attainment argument does not establish. I sent
the coordinator the correction “a maximizing raw threshold with positive
closed-CDF discrepancy”. The coordinator owns that correction and any
subsequent build. This evidence refers precisely to the build01 PDF above;
the visual review does not independently certify mathematical hypotheses,
finite certificates, complete coverage or bibliography accuracy.

The coordinator subsequently reported the page 126 wording corrected in the
root source, with a new build and changed-page review underway. This child
record does not claim inspection of that later build.
