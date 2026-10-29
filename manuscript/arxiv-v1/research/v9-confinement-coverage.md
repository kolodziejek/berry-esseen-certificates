# Fixed-target resources and confinement: manuscript coverage

This integration adds only sections/06-fixed-resources.tex,
sections/07-fixed-confinement.tex, and this report, on branch
manuscript/v9-confinement-20261028, based on
924e6160bee44ed3a50eba35f7dbb8dcd5b9a9c7. The proof sections are committed
as 1de6700. The v7–v8 sources, programs, proof objects and earlier failed
diagnostics are unchanged. No numerical kernel, native certificate
campaign, external write or push was performed for this editorial task.

## Status and exact scope

| Component | Mathematical status | Execution status in this task |
|---|---|---|
| Common moment budget, ordered contractions, signed moment and weighted noise exports | Full conditional analytic derivations included; finite panel updates remain explicit inputs | Existing exact outputs read and compared as inert data; no producer rerun |
| Signed phase resource and necessary noise filter | Full derivation from fixed-target conservation and the complete raw Fourier bound; same-law cells and update order retained | Existing export census and arithmetic remain conditions, not freshly accepted here |
| Continuous low-noise confinement | Full conditional proof, including heat remainders, exact quintic endpoint criterion and held-beta ray continuation | Prior exact endpoint evidence retained; no new numerical experiment |
| Central-panel high-noise confinement | Complete analytic reduction with strict atom semantics, both deleted indices, one common resource and explicit finite gates | Earlier exact 128-box acceptance and separate reconstruction retained; no new replay |
| Source and layout integrity | Editorial verification only | Fresh structure check, bounded inert-data comparisons, compilation and visual inspection passed, except the standalone wrapper's expected external references |

The abstract low-noise lemma assumes the incoming strip and inward bound
on p in [0.4,0.6], and proves strict amplitude below 1/2 for lambda <=3/40,
all raw thresholds and n >=42. Its acquired application is only
p in [0.40,0.53]. Complete acquired-noise confinement is conditional only
on p in [0.41,0.42]. Other high-noise panels, strict count comparison and
the finite base remain open obligations.

Finite arithmetic assertions are stated as conditions. The derivations
explain why those inequalities imply the conclusions; their truth is not
inferred from a census, hash, source label or the existence of a log.

## Source-to-manuscript map

Paths are repository-relative. Line references are to the base sources
and the newly added files in source commit 1de6700.

| Retained source | New location and treatment |
|---|---|
| mathematics/fixed-target-v8/2026-10-28/moment-entry-v8-proof/main.tex:16–159 | 06-fixed-resources.tex:20–181: input hypotheses, outer-gap substitution, binary/noise/displacement costs, ordered iteration, both beta orientations, coherent rho turnover, weighted joint budget |
| Same source:161–220 | 06-fixed-resources.tex:182–267: conditional all-panel result and exact strip gates, using the independently scoped general heat lemma in the next section |
| mathematics/fixed-target-v8/2026-10-28/phase-proof/main.tex:42–183 | 06-fixed-resources.tex:268–409: raw signed polynomial, licensed density, new phase price, eight-corner extrema, both target endpoints, closed-region maxima and all-index noise filters |
| mathematics/fixed-target-v8/2026-10-28/low-noise-continuous-proof/main.tex:15–306 | 07-fixed-confinement.tex:11–316: full continuous proof, same-law cubic expansion, signed beta, four heat errors, polynomial coefficients, endpoint signs, radial continuation, zero noise and closed seam |
| mathematics/fixed-target-v8/2026-10-28/high-noise-review.md:28–139 | 07-fixed-confinement.tex:317–678: full analytic high-noise derivation, replacing an opaque reference to the short composition |
| manuscript/arxiv-v1/appendices/fourier-analysis.tex:3058–3468 | Same high-noise portion: endpoint costs, antichain, deletion, slopes, intervals and errors, with new index/strip/target/resource hypotheses explicitly rederived |
| mathematics/fixed-target-v8/2026-10-28/phase-confinement.py and phase-confinement-proof/main.tex:121–287 | 07-fixed-confinement.tex:680–746: exact closed 128-box cover, permitted exclusions, 56 strict gates, low-noise replacement and final conditional theorem |

The older literal confinement theorem used n >=47, strip 0.55, and an
actual-score coefficient. These hypotheses were not silently widened.
The new text derives fixed-target contact slopes, uses n >=42 and both
deleted indices at least 40, proves the 0.6 strip at its named scope,
and states all new slope and interval gates. The central high-noise
argument retains p <q; its count and deletion formulas are not exported
to above-half panels.

## Dependency and notation decisions

The initial strip proof invokes v9:confinement:heat. This general heat
lemma requires fixed-target contact and support bounds, but no incoming
strip or low-noise conclusion. Thus the forward reference does not create
a strip/confinement cycle. Its full derivation is retained here; any later
deduplication against the entry section must preserve that scope.

The central outward constants are weaker than the existing all-panel
result for panel 41. A separate four-round central contraction is therefore
not an additional premise. Fresh rational comparisons against the
existing moment03 output verified:

| Quantity | Existing panel-41 output | Used outward bound |
|---|---:|---:|
| theta | 0.053026061 | 0.054 |
| inward d | 0.0672060498 | 0.069 |
| rho | 1.2049635459 | 1.22 |
| lambda | 0.5728987925 | 0.6 |
| ell lower | 1.9716524903 | 1.9706 |
| ell upper | 2.0332091985 | 2.034 |
| beta lower | 0.0984897692 | 0.09736 |
| beta upper | 0.2234813701 | 0.234 |

The selected entry input also bounds |H| strictly below 1.814.
This compares existing evidence; it does not re-establish its producer.

Notation separates excess a from conditional mean magnitudes bar A=m/q
and bar B=m/p, physical gap endpoints A,B, and count endpoints a_0,b_0.
Physical noise W and count noise U=W/ell are distinct from Fourier Omega.
Binary moment charge mathfrak b_0 is distinct from Bernoulli indicator B_0.
Scalar leakage mathcal L (the core's leakage L) is declared separately
from the contact slope L. Endpoint distances M_+,M_- are distinct from
slope losses C_sl,+,C_sl,-.

Signed beta bounds retain both orientations across p=1/2. Phase filtering
uses the actual minimum and maximum of p(1-p), including 1/4 when relevant.
Every division domain and directed root required by a finite gate is
stated. The binomial constant and Bernoulli rho cap specify the directed
10^-10 roots used by the acceptance calculation.

The cover retains both phase signs and all eight closed noise bands.
The first 16 boxes use the continuous low-noise theorem. The remaining
112 have the retained census: 14 empty incidence lists, 5 negative
resources, 65 negative residual resources, and 28 pairs of strict ray
inequalities. Zero residual is retained. The 56 strict margins exceed
0.00892011917. The seam lambda=3/40 belongs to both adjacent bands.
Boundary atoms are included in the contradictions, and zero noise is
treated directly. No failed unassisted diagnostic was erased or relabeled
as a PASS; the proved low-noise replacement supplies that part of the cover.

## Labels and integration interface

The requested anchors v9:resources:section and v9:confinement:section
are defined. There are 53 distinct new labels, all in the two assigned
namespaces. No existing labels are changed.

Principal resource suffixes are input, moment-budget, iteration, beta,
all-panels, strip, central-entry, raw, price, quadratics, cell,
noise-filter, rectangle and phase-condition. Principal confinement
suffixes are theorem, heat, margin, application, resource-simplex,
concentration, deletion, slopes, intervals, errors, high-condition and
central.

The only external references in this two-section build are
v9:core:contact and v9:core:conservation (formulas),
v9:core:phase-price (a corollary), and
v9:entry:selected-route and v9:entry:ordered-update.
No new preamble edit or macro is required.

## Fresh bounded verification and layout

Only the three assigned repository files are added. Temporary wrappers,
receipts, stdout/stderr and build logs are under
/private/tmp/manuscript-v9-confinement-20261028-03/.
The coordinator supplies the persistent combined manuscript build.
The wrapper copies the existing preamble and inputs these two sections
by absolute path.

Final command actually run, displayed over lines for readability:

    /Applications/Xcode.app/Contents/Developer/usr/bin/python3
    /Users/bkolodziejek/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py
    /private/tmp/manuscript-v9-confinement-20261028-03/main.tex
    --compiler texlive
    --output-directory /private/tmp/manuscript-v9-confinement-20261028-03/build
    --json

It returned 0 in 1.4477310180664062 seconds and produced 16 pages.
There were no overfull or underfull boxes. Only the five expected external
references were unresolved. The structure check counted 53 unique labels
and 34 references, with every internal reference resolved.
Final PDF SHA256:
486028a46c19788388d27d28a9d3fd1a4d69db7ad9dafe73ab627f284911f4f7.

The inert-data comparison confirmed all thirty ordered input panels
24–53, exactly excluded panels 24 and 53, the central comparisons above,
and both boundaries plus all twelve ray signs in each of the thirteen
retained strip panels 40–52. This checks transcription scope, not fresh
certificate acceptance.

Rendering command:

    pdftoppm -png -r 100
    /private/tmp/manuscript-v9-confinement-20261028-03/build/main.pdf
    /private/tmp/manuscript-v9-confinement-20261028-03/render/page

It returned 0. All sixteen final pages were viewed in four contact sheets.
Full-page inspection covered final pages 2, 5 and 13, plus pages 9, 14 and
15 from the previous build, whose rendered bytes are identical in the
final build. No clipping or overlap was found. The wrapper's external
question marks are expected; their combined-build resolution remains the
coordinator's check.

Final source SHA256 values:

    06-fixed-resources.tex
    826ae89d9876257b61c5121970538ef28d347129099b66e41e6ea2ded5c81a01
    07-fixed-confinement.tex
    349ca2089eec056409696a59fbe75a4d423bce7c0a527f0df22c20f14c5e4e31

The source commit's whitespace check reported one extra blank line at
each EOF. No other whitespace issue was reported; this cosmetic issue
does not alter the compiled source.

The integrator also authored some prior confinement components; this
report is not an independent review of those components. The coordinator
read both sections. The separate scalar reviewer rederived the high-noise
slopes, interval placement, deleted-index factors and common-resource
errors, finding no blocking scope mismatch. Those reviews support the
displayed derivations; they do not replace explicit finite conditions.
