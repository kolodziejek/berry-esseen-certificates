# Fourier appendix: source coverage and verification boundary

Prepared on 27 October 2026 on branch `manuscript/fourier-20261027`, starting
from fork commit `8989ba0`. The original reference commit
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee` and the supplied source are unchanged.
The deliverable is `../appendices/fourier-analysis.tex`.

This is an editorial reconstruction of complete supplied analytical
arguments, with explicit conditional numerical interfaces. It is not an
independent verification of the complete Fourier/resource/local chain.
The new appendix does not certify a global Berry--Esseen theorem or remove
any certificate. Hashes below establish source identity, not validity.

## Source and coverage

All source line numbers below refer to the physical lines of
`paper/analytic-supplement.txt`, SHA-256
`dad4a3558b01bda4acfdfc9120a50ecbcd7a6f2389886ba3ce72a6602ec39018`.
These are supplement line numbers, distinct from its original-manuscript
`M...` locators. The original ranges were read, including the proofs.

| Source lines | Retained argument and destination anchor | Mathematical status | Execution status in this task |
|---|---|---|---|
| S1, 128--150; A1, 7913--8212 | Exact kernel, real-part improper integral, Beurling construction, partial-fraction identity, Abel limit, closed boundary, cardinal values, expectation/Fubini and physical ROOT4 signs; `ms:fourier:kernel` | Supplied proof candidate, rewritten as a connected proof with explicit integrability and endpoint conventions | Typeset and inspected; no numerical predicate involved |
| S3, 808--1218 | Real/imaginary characteristic-function bounds, scalar cosine certificate, convex modulus profile, complex-power rectangle and external four-term smoothing; `ms:fourier:afcore:sec:fourier` | Analytical implications retained; scalar Bernstein premise conditional; Shevtsova smoothing is a cited external theorem | Bernstein program included as a specification, not executed |
| S3, 1219--1507 | Contact slack, its two integrations, compensated inversion, exact conserved identity and explicit remainder ledger; `ms:fourier:afcore:sec:conserved` | Supplied proof candidate, conditional on its contact witness and integrability hypotheses | No independent numerical or optimizer verification |
| S3, 1508--2236 | Paired LOW, actual-index finite LOW, complete HIGH, supported compensated HIGH; `ms:fourier:rescore:sec:setup` | Supplied analytical transfer arguments with explicit domains and divisors | No quadrature or native checker executed |
| S3, 2237--2602 | Positive-measure rule, simultaneous gap budget, state/update/export, enclosure theorem; `ms:fourier:rescore:re-operator` | Supplied conditional implications for one common law and one conserved budget | No enclosure schedule accepted |
| S3, 2603--3898 | Signed moment atlas, gap/outer costs, common-moment boxes, event/rectangle bounds, feedback, signed phase and all finite-schedule propagation; `ms:fourier:rescore:re-atlas` through `ms:fourier:rescore:u-propagation` | Supplied conditional derivations; support callbacks and every finite gate remain premises | No resource table or coverage replay |
| S8, 6529--6946 | Confinement with two concentration choices, antichain, signed deletion, slopes and two budget error bounds; `ms:fourier:cut49:conf:re:confinement` | Supplied proof candidate at the stated floor **47**, using both actual deleted laws | No confinement certificate accepted |
| S8, 7099--7196 | Exact local identity and parameterized strict comparison theorem; `ms:fourier:cut49:shortloc:theorem` | Supplied analytical implication conditional on the displayed witnesses and signs | No local endpoint test run |
| S8, 7197--7473 | Binomial normalization, common repair, quartic/Poisson/Bennett estimates and nearest-count witness, including small positive noise | Supplied candidate arguments; normalization and tail gates are explicit | No TINY or MID finite cover accepted |
| S8, 7474--7690 | Whole-count witness, marked crossing with deleted laws, fractional-part bound and final functions (B,I) | Supplied analytical implications; the 80-coefficient scalar premise and all endpoint tests remain conditional | No LOW grid or scalar coefficient test run |
| S8, 7757--7770, argument only | Separate zero-noise endpoint, `ms:fourier:zero-noise` | Elementary reduction to the actual Bernoulli law followed by an external binomial theorem with its own hypotheses | No external proof replay |

The complete S3 block is retained. In particular, the positive-measure and
joint-budget material between lines 2237 and 2484 is needed by later
updates, even though an earlier task range started mid-proof at 2485.
Likewise the identity at 7099--7196 is retained before its normalization.
These additions prevent hypotheses from being hidden behind an excerpt.

## Exact scope that integration must preserve

The three top-level sections have namespace `ms:fourier:*` throughout.
They use only the common manuscript macros and theorem environments.
No extra preamble definition is required. The only bibliography keys are
`Shevtsova2012` and `Schulz2016`. The former locator is corrected to
**Lemma 4.1, printed p. 263**, following the primary-PDF check by the
coordinator. The kernel proof itself is written out, rather than replaced
by a Prawitz citation.

| Interface | Required hypotheses and preserved limitation |
|---|---|
| Exact half-line kernel | Positive exponential and positive imaginary part of (K); take the real part before the improper limit. The majorant is for the closed negative half-line; the reflected minorant is for the open half-line. Expectation interchange uses an integrable random variable. |
| Characteristic bounds | One centered, variance-one law with finite absolute third moment. The independent-copy modulus uses (D\ge E|X-X'|^3/2), with the valid universal choice (D=\rho+1). It does not substitute a stronger unproved symmetrization bound. |
| Four-term smoothing | The entire four-term expression and infinite Gaussian tail must be bounded. Normalize a moment band by its lower third-moment endpoint. Any branch selection in quadrature must hold on the entire cell. |
| Conserved resource | The actual contact witness, common slack, sign, score and threshold must agree. Source contact/attainment results are prerequisites, not consequences of a numerical enclosure. Every LOW/HIGH remainder is retained. |
| Enclosure/update | All coefficients refer to one marginal and one positive measure. Support and moments must be acquired before use. Weighted (nD) bounds remain weighted; an unweighted bound cannot be multiplied by a larger band endpoint to invent a weighted one. |
| Confinement | The displayed source floor is (n\ge N=47); the initial strip is ((-0.55,1.55)). It uses (p<1/2), conditional centering, the row's signed phase/resources and separate concentration bounds at **both** (j=n-1,n-2), with (C_0=0.4253). A confinement amplitude is an output before becoming a support update. |
| Local comparison | Same actual marginal, (d\le d_0<\min(p,q)), (d_0\le A), legal interior count (1\le k\le n-1), (|u|\le1/2), and (C\ge c_*>0). Normalizers, reciprocal bounds and all denominator positivity conditions are required. |
| Nearest-count test | (D=O-R_0T>0) is used before multiplying by the lower mass bound. The exact gate is (mD-\kappa\lambda/n>\varepsilon\lambda). Outgoing events are strict and incoming events are closed. |
| Whole-count test | Use (B<0) before replacing the mass factor by its lower bound, and (I\ge0) before replacing (n) by (N). The final strict gate is (mB+I/N<-\varepsilon). These signs are hypotheses, not conventions. |
| Marked crossings and collisions | The forward and backward deleted laws remain distinct. Independence is used only after deleting the entire marked pair. Strict/open events, zero variances and integer collisions remain in the argument. |
| Zero noise | Conditional centering and (\lambda=0) force both conditional noises to vanish. This is a separate endpoint, not a limit of a bound divided by (\lambda). The strict Bernoulli conclusion still invokes the external theorem with its stated hypotheses. |

The parameterized local identity can be stated for a formal floor (N), but
this does not prove that the supplied confinement constants, normalizers,
resource acquisition or finite covers apply at (N=42). The appendix's
scope remark makes that distinction explicit. The coordinator's separate
uniform-floor bridge is now cross-referenced in the integrated manuscript; its
conditional input obligations must not disappear in that cross-reference.

## Editorial changes and omissions

The inherited A1 plain-math text was converted to numbered TeX equations,
with its proof retained. Source headings were arranged into three appendix
sections and subordinate headings, all labels were namespaced, and source
cross-references were adjusted consistently. The six overwide displays
found in the initial build were split across lines without changing their
constants or signs. The clipped optimizer in the moment bound is defined
separately from its piecewise expression for readability.

The scalar cosine lemma now explicitly assumes its stated finite rational
positivity condition. Its (81\cdot14) coefficient formula and source
acceptance program are present, but the program is not represented as
freshly run. Similarly, the fractional-part argument exposes its
(8\cdot10) Bernstein coefficient condition. Historical phrases asserting
that selected normalizers or sign-sensitive gates passed were replaced by
requirements that those gates be checked. This is a change in reported
verification status, not a weakening of a certificate target.

The obsolete index-46 barrier assembly at lines 6947--7098 is omitted.
The old tail-completion/table-acceptance narrative at lines 7691--7771 is
also omitted; only its separate zero-noise mathematical argument is
restated. No historical row count, success marker or claim of complete
finite coverage is imported. S1's sharp third-moment theorem is assigned to
the coordinator's separate appendix, so the source's unverified
Shevtsova-2014 theorem-number locator is not repeated here.

## Checks actually performed

`runs/manuscript-20261027/fourier01/preview.tex` is a standalone driver with
the shared preamble and two bibliography stubs. It was compiled with the
existing TeX Live 2025 / pdfTeX installation and latexmk 4.86a. The retained
stdout, stderr, final TeX log and JSON receipt record the result and hashes.
The PDF has **61 pages**. The final TeX log contains no undefined-reference,
citation, overfull-box or underfull-box warning. A static check found no
duplicate labels, unresolved internal references or unbalanced TeX
environments; all 61 pages were text-extracted without an unresolved `??`
marker.

All 61 pages were inspected in contact sheets. Pages 1, 3, 14, 27, 46, 58,
60 and 61 were also inspected at larger size, covering the kernel signs,
finite LOW display, joint-resource costs, preserved floor, marked crossing,
fractional-part gate and zero-noise endpoint. These are layout and
transcription checks. They are not a proof of the displayed inequalities.

For reproduction, run from `runs/manuscript-20261027/fourier01`:

```sh
/Library/TeX/texbin/latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -synctex=1 preview.tex
```

No archived/native checker was imported or run, no certificate campaign was
started, and no package was installed. No independent counterexample search
or arithmetic acceptance test was performed in this manuscript task. The
analytical candidates, exact input coverage and all pending numerical
premises require their own review before this appendix can support a claim
of a complete proof.
