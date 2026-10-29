# Fixed-target excess: first analytic entry

Branch: `research/v5-excess-entry-20261027`, starting commit `78f0b7c`.
All additions are in this research directory and `runs/fixed-target-v5-20261027/entry*`.
Original certificates, drivers, reference baseline and production manuscript are unchanged.

## Exact result

Let `c=CE`, `n>=42`, and let `(P,H)` maximize the fixed-target excess

`a=sqrt(n)(P(S_n<=H)-Phi(H/sqrt(n)))-c E|X|^3`.

Assume `a>=0`, the true predecessor cap `C_(n-1)<=c`, and the external structural inequality `sqrt(n) Delta_n(P)<=.3031(rho+.646)`. Then

* `1<=rho<7361/4000<1841/1000`;
* `|beta|<321/500`;
* the **closed** support is contained in `(-96/25,96/25)`;
* the radial fourth-, fifth- and sixth-moment ceilings in `entry.tex`, equation (5), and a genuine iid distance event are available before any defect feedback.

This proves the initial analytic entry without ratio optimality, an upper actual-score cap, a scalar smoothing recurrence, `C_(n-2)`, a positive barrier, or a previously licensed central gap. Fixed-target attainment/contact remains the previously proved companion input. The structural inequality remains an external input, not a consequence of our arithmetic.

The new first numerical gate is weaker than the historical uniform gate. On a closed moment cell `rho in [l,u]`, a complete raw enclosure

`R_c(H)<=T<N*c_lower*l`

valid for every real raw `H` licenses Gaussian-weight removal. It yields

`exp(-H^2/(2n))>=1-T/(N*c_lower*l)>0`

and

`(n+H^2)a+n phi(0)D/6+n^(3/2)L <= R_c(H)<=T`.

The coefficient of the excess remains `n+H^2`. The proof uses neither `a=0` nor an upper bound on `a`. The strict gate cannot silently be replaced by a weak one.

If a separate complete enclosure proves `R_c/rho<10`, the normalized-cover lemma gives the rational consequences

`exp(-H^2/(2n))>7199/17199>.418`, `D/rho<25000/6979`, and `a/rho<10/n`.

These follow for every `n>=42`. They are outputs of the first raw bound, not assumptions required to obtain it. The computation agent now reports a fresh 24-cell exact cover with maximal upper ratio `9.455732088645<10`, from the unchanged kernel primitives and a tight enclosure of c. This note does not independently certify that execution: its files are `../fixed-cell-v5/mathematics/fixed-target-v5/2026-10-27/cell_check.py`, `cell-input.json`, and `../fixed-cell-v5/runs/fixed-target-v5-20261027/cell01/check.stdout.json`. Parent review must reconcile those primitives and the complete coverage with the analytic conditions here.

A further first-phase price follows directly from the same exact identity: if the **raw** remainder is bounded by T, then with `M_c=c rho-phi(0)D/6`, `exp(-w)M_c>=c rho-T/n`. Thus its phase term is at least `H^2(c_lower*l-T/N)/2`, with no `D<2` premise. Subtract this from the raw quadratic polynomial before completing the square. The improved result bounds the **unweighted resource** `U=(n+H^2)a+n phi(0)D/6+n^(3/2)L`; it must not be reused as an improved raw-remainder bound. Both root and this agent rederived this step.

## Dependency edges and exact source locations

Locations below refer to the unchanged files at `78f0b7c`; their hashes are in the execution receipt.

| Edge | Exact premise and reason | Source | Status |
|---|---|---|---|
| Fixed-target witness -> contact | Fixed `n`, standardized laws with finite third moment; maximize excess, use closed CDF and closed support. Third-moment lower semicontinuity, not UI3, is sufficient in the attainment argument. | `mathematics/strategy-v4/2026-10-27/excess.tex:45–166` | Retained previously derived proof; not reconstructed by the arithmetic checker |
| Nonnegative excess -> rho cap | Actual positive score is `c+a/rho>=c`; external `.3031(rho+.646)` bound; `c>.4095`. | `manuscript/arxiv-v1/sections/01-introduction.tex:80–89`; new Theorem 1 | Locally derived conditional on the external inequality |
| rho -> beta | Signwise Cauchy, including a possible zero atom; `(1+beta^2)^2<=rho^2(1-beta^2)`. | `sections/02b-moment-domain.tex:41–58`; new proof | Locally rederived; exact endpoint comparison checked |
| Contact + predecessor -> Gaussian inequality | `C_(n-1)<=c`; closed predecessor CDF bound; excess contributes `-na` and can be dropped. No second predecessor needed. | `strategy-v4/.../excess.tex:168–202`; `sections/04-support.tex:11–36` | Locally rederived for the fixed target |
| Gaussian inequality -> radius | `n>=42`, frozen `rho<=1.841`, `|beta|<=.642`, both support signs, all real H. Fourth-order heat expansion, strict radius check, whole-ray derivative bounds. | `sections/04-support.tex:38–179`; new Theorem 1 | Locally rederived; fresh rational checks |
| Radius -> higher moments | Only now use `M4,M5,M6`; radial nonnegative measure of mass `rho-1`. | `appendices/fourier-analysis.tex:2072–2088`; new Section 2 | Locally rederived; finite-law identity checks |
| Moments -> actual distance event | Independent copies of the same law, `E={(X-X')^2>=9/25}`; Cauchy and `E(X-X')^4=2M4+6`. | `appendices/fourier-analysis.tex:1361–1374`; new (6) | Locally rederived |
| Compensated inversion -> Fourier error | Zero mass and first moment of signed difference, finite absolute second moment; all real H; cubic comparator retained. | `sections/05b-conserved.tex:143–200`; `strategy-v4/.../excess.tex:323–342` | Retained analytic proof; no score coefficient occurs |
| Sixth-order low transfer -> `(L0,LH,L2)` | `n>=N>2`, `M<=11.1`, `g<=1.85`, true sixth moment; complete Taylor remainders and positive damping. | `appendices/fourier-analysis.tex:798–905` | Analytic hypotheses and proof-level dependencies checked in this task; no ratio-score premise |
| Complete high transfer -> `K_H` | Actual event, six contributions on the entire half-line; rational Laguerre tail; all floor/window gates. | `appendices/fourier-analysis.tex:1147–1374` | Frequency partition, Jensen, Gaussian comparator and monotonicity inspected/rederived; numerical gates not evaluated here |
| Raw scalar -> first license | `q*>0`, nonnegative scalar ceilings; formal coefficient interval contains c; full moment cover. Then new **cell-sensitive** strict gate `T<N*c_lower*l`. | `appendices/fourier-analysis.tex:2460–2542`; new Sections 3–4 | Algebra rederived; whole cover is a separate computational deliverable |

The Fourier/source claims are not called freshly accepted certificates in this report. The proof note gives the exact scalar enclosure and its conditions. The computation agent's separate first-cell/cover work must retain its own provenance and be reviewed before its reported gates can be composed with this note.

## Proof-level checks on the raw enclosure

The raw remainder uses the formal contact coefficient `c`, not the actual score `c+a/rho`. In the constant term, the two unsigned bounds follow from gap-by-gap integration, `J<=rho+1`, the integral defining `Gamma(R,l)`, and `M5>=M4^(3/2)`. The `Gamma` expression was checked by direct integration; a finite interval computation of its supremum remains a scalar gate. All three `K1` alternatives are valid for the actual same marginal, and `U in [-1/2,2M4/3-1/2]` follows from the same gap integrals. Initially `q*=c_lower*l-g/5` is valid without assuming the sign of gamma or H.

The low-frequency proof expands `f-exp(-t^2/2-i gamma t^3/6)` through degree five, with a genuine sixth-moment remainder. The polynomial-power remainder uses the entire joining segment and positive damping. The comparator has both its cubic sine error and its H-dependent cosine error. No ratio score occurs in these calculations.

For the high-frequency proof, symmetrization first gives `|f|^n<=exp(-n E sin^2(t(X-X')/2))`. Conditioning on the actual event and convex Jensen gives the event-based exponential. The six contributions are: the interval `[1/2,.9]`, nonzero-cell cores, their wings, the near part of the zero cell, its far part, and the Gaussian/cubic comparator over **all** `[1/2,infinity)`. The whole expression, not an individual term, may be minimized over windows. Its use at N is a bound for every n>=N, including varying laws, only after all stated monotonicity gates pass.

The stronger license follows directly by dividing the conserved identity by n. It is not an extrapolation from a numerical example. The old `T<.4N` gate was sufficient because `c rho>.4`; it was not necessary. Large-rho cells can therefore be usable even when their raw upper bound exceeds `.4N`.

One inherited proof sentence needs a local correction. In `manuscript/arxiv-v1/appendices/fourier-analysis.tex:1971`, the stated pointwise positive-side inequality `(t-a)(rho-t)<=rho^2/4` does not cover the positive part of a central gap with `a<0`: `a=-1,t=1/2,rho=1` gives `3/4>1/4`. The required argument uses `t(rho-t)<=rho^2/4`, multiplied by the nonnegative gap distance `(t-a)` and integrated. Since the total integral of the latter is `J/2`, this proves exactly the same `3rho^2J/8` charge. The new proof note gives this corrected argument. No numerical coefficient or certificate needs to change, and the old source is untouched.

## Evidence and limits

| Result | Mathematical status | Execution status |
|---|---|---|
| Initial moment/radius lemma | Locally derived, conditional on the stated external structural inequality and retained fixed-target contact theorem | Fresh exact support arithmetic PASS |
| Higher moments and actual event | Locally derived inequalities for the actual law | Five exact finite-law diagnostics PASS; analytic proof is in the note |
| Moment-cell weight license | Locally derived identity/sign argument | Rational illustrative gate checked; no simulation needed for the general proof |
| First raw bound on a whole rho cover | Conditional on the complete Fourier enclosures and outward scalar gates | Not run by this agent; separate computation work pending review |
| Local exclusion / all-index sharp theorem | Not established by this note | Not run |

`runs/fixed-target-v5-20261027/entry01/` records the actual command, Python version, elapsed time, input hashes, return code, stdout and stderr. The checker uses only standard-library exact fractions and imports no inherited backend. It checks all six exterior-ray signs, the exact support margin greater than 1/5, the two structural fractions, Gaussian rational constants, and five finite-law cases: symmetric Bernoulli, both skew orientations, a zero-atom law, and tiny distant atoms. The latter two are explicitly outside the initial moment domain. They test algebra, not a claim that every such law is an extremizer.

The same envelope at radius 3 is positive; the negative control is correctly rejected. This says the proposed envelope does not prove radius 3, not that radius 3 is mathematically impossible. No native LOW/HIGH program or expensive generation campaign was run. No baseline component is deleted or newly declared dispensable outside the precisely restated fixed-target entry.

The source arithmetic was initially misstated in a coordination message as coming from the `.3322` bound alone. The `.3031` bound is the correct source, already present in the manuscript; the final proof and checker use it. No manuscript defect is claimed from that transient attribution error.

The final exact rerun is `entry02` (return code 0), after adding the rational normalized-cover corollary. `entry-build01` preserves the first successful compile and its three layout overflows; those were repaired in the new source. `entry-build02` is a clean six-page TeX Live build. All six final pages were rendered at 85 dpi and viewed individually; no clipping or overlap was seen. The final PDF hash and visual-only review record are in `entry-build02/visual-qa.json`.
