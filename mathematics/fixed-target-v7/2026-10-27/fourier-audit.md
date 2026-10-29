# Independent analytic closure of the v6 Fourier primitives

Task base: `ab4bb3f0353fedc68772159429e76b83dd79af78`, in the user's fork, separate branch `research/v7-fourier-audit-20261027`. Existing source and certificate files are unchanged. The accompanying `fourier-closure.tex` is a proof, not an inference from historical PASS markers or from the bounded checks.

## Precise result

For every integer `n>=N>=42`, let the actual standardized iid marginal have common ceilings

`mu4<=M<=11.1`, `|gamma|<=g<=1.85`, `mu6<=M6`, `|(3-mu4)/24|<=A`, `|(10gamma-E X^5)/120|<=Z`.

Let an actual event under the product of this same marginal have probability at least `alpha>0`, distance at least `d>0`, and conditional squared distance at most `M_E`. Assume all scalar damping/window gates stated in the proof. Define `I0(H)` and `Iinfinity` from the complete difference

`V_n(t)=f(t)^n-exp(-nt^2/2)(1-in gamma t^3/6)`.

The exact triangle LOW triple returned by the pinned `sixth` function, with its actual-support Pearson coefficient ceilings, satisfies

`I0(H)<=(L0+LH|H|)/sqrt(n)+L2/n`.

The complete six-piece HIGH sum at the floor gives `sqrt(n) Iinfinity<=KH`. The compensated inversion formula is valid, including atomic laws and arbitrary real thresholds, and consequently

`|E_n| <= (2/pi)(L0+KH+L2/sqrt(N)+LH|H|)`

`<= (16/25)(L0+KH+L2/sqrt(N)+LH|H|)`.

This is exactly the constant Fourier budget and H-slope used by the v6 wrapper. The law and H may vary with n: the proof is a family of inequalities for each law and threshold, not a fixed-law asymptotic assertion. No own-score cap, ratio optimality, sign of H or sign of gamma enters these Fourier lemmas.

The support premise is genuine. To use the pinned coefficient construction one supplies `1<=R<=6`, `|X|<=R` and `E|X|^5<=E5`; then `M6=R E5`, `A=max(2,M-3)/24`, and the displayed Pearson formulas produce Z. A third-moment ceiling alone supplies none of these higher moments. The v6 initial setting uses R=96/25, not the source module's unmodified default radius.

## Proof-level audit and source edges

Line locations below refer to task base `ab4bb3f`; full SHA-256 bindings are in the run receipt.

| Edge | Source location | Independent reasoning and scope |
|---|---|---|
| Zero mass/mean and absolute second moment to compensated inversion | `manuscript/arxiv-v1/sections/05b-conserved.tex:141–202` | Re-derived the nonnegative scalar compensation integral, its pi/4 constant by Tonelli/Laplace integration, and absolute Fubini. No CDF continuity or uniform integrability inference. |
| Inversion to Fourier error ledger | Same file, 219–229 | Checked Gaussian cubic comparator transform, hinge correction and factors n and 2/pi. This verifies only the ledger edge, not the rest of the conserved identity. |
| Six moments to low-frequency expansion and power remainder | `appendices/fourier-analysis.tex:788–904`; `cell-sources/kernel.py:63–83` | Independently expanded f and h through degree five, kept the sixth-order exponential term, and bounded the complex-segment Taylor remainder. Gaussian moments reproduce every triangle coefficient and L2. |
| Actual support/Pearson identities to Z | Fourier appendix 966–1020; kernel 65–78 | Re-derived both signs of E X^5−10gamma, the r−2|gamma| gate, M=5 split, clipped vertices and the concave P6 endpoint alternative. This licenses the exact minimum of these ceilings. |
| Actual event to full HIGH integral | Fourier appendix 1198–1374; `cell-sources/high_window_core.py:10–34` | Re-derived conditioning/Jensen, the distance-dependent partition, all peak cores and wings, both zero-cell parts and the complete comparator tail. All six pieces are retained. |
| Rational Gaussian tail to optional refinements | Fourier appendix 1156–1196; HIGH lines 22–30 | Re-derived the Laguerre division, factorial moments and polynomial derivative. The optional quarter gate is essential to the stated all-index proof. |
| Common scalar ceilings to all n>=N | Fourier appendix 902–904 and 1346–1359; HIGH 17–18, 24, 28, 31 | Explicit monotonicity only of bounding expressions. It compares no changing-law characteristic functions. The moving raw H is carried as |H| throughout. |
| Analytic bounds to directed rational output | kernel 19–29, 80–83; HIGH 11–34; `cell_check.py:74–92` | Read exact root/exponential rounding semantics and directed pi substitutions. The Taylor-denominator exponential helper is an upper bound even after clipping x at 64. Its own rounding monotonicity is not needed. |

The named paths beginning `cell-sources` are under `mathematics/fixed-target-v5/2026-10-27/`; source provenance is preserved in that directory's `provenance.json`. No inherited checker or kernel was imported or executed for this task.

## Vulnerable steps and negative controls

1. The all-index LOW bound requires the actual sixth moment. Bounded third moments do not imply it. Here it is obtained only after the explicit support and fifth-moment ceilings.
2. The damping gate cannot be omitted: the derivative of `sqrt(n) exp(-c n)` is positive at n=42 for c=1/1000. This is a counterexample to unguarded floor evaluation, not to the guarded source bound.
3. The optional zero-cell tail also needs a domain check. Its derivative numerator is `4-10x-22x^2-13x^3-2x^4`, positive at x=1/10 and negative at x=1/4. The pinned code correctly enables that option only at x>=1/4.
4. The imaginary fifth coefficient has a fixed sign: the comparator contains `+i gamma t^5/12` before subtraction, so `f-h=-a t^4-i z t^5+...`. Simultaneous reflection changes both odd coefficients. The exact polynomial control detects the sign-reversed alternative.
5. Zero first moment of the signed measure is essential to inversion. For `delta_1-delta_0`, the uncompensated imaginary numerator has a nonzero linear term and division by t^3 is not integrable at zero. The actual sum/comparator difference has both required cancellations.
6. Event averaging uses one actual product law. It does not permit an artificial lattice model or mixed moments from different laws. Distance atoms do not obstruct the partition, since the integration endpoints have zero Lebesgue measure for every fixed distance.
7. A HIGH minimum is a minimum of complete valid sums. A LOW choice remains one complete valid triple. No coefficientwise mixing of unrelated LOW triples was justified.

## Fresh bounded evidence

`fourier-check.py` uses only the Python standard library and exact rational arithmetic. It checks seven groups of formal polynomial identities, six standardized actual-law controls (symmetric and reflected skew Bernoulli, a gapped three-point law, a law with an atom at zero, and distant symmetric atoms), 1,394 scalar Pearson-envelope grid values, six initial HIGH window gates, and the four negative controls above. Its grid is explicitly a diagnostic; the continuous-domain argument is in the proof. It performs no Fourier quadrature, original certificate acceptance, dense/native campaign or acquisition schedule.

`runs/fixed-target-v7-20261027/fourier01/` and `fourier02/` record commands, interpreter, input hashes, stdout, stderr, elapsed time and successful return codes. The second run adds exact directed-constant checks. Compilation and visual-review evidence is recorded separately in `fourier-build01/` through `fourier-build04/`; the final build includes two display-layout fixes, with no mathematical changes after the second exact run.

## What this changes, and what remains

| Result | Mathematical status | Execution status |
|---|---|---|
| Compensated quadratic-hinge inversion and its exact Fourier normalization | Independently derived and checked at the stated signed-measure scope | Algebraic controls passed; no quadrature needed for the proof |
| Triangle sixth-order LOW and its pinned coefficient construction | Independently derived and checked under actual moment/support ceilings | Fresh bounded exact checks passed; original kernel not run |
| Complete six-piece HIGH with floor evaluation | Independently derived and checked under actual-event and damping gates | Fresh algebra/initial-gate checks passed; no full cell replay |
| v6 Fourier budget as an analytic inequality | Follows from the three proved modules above | Existing v6 arithmetic output was not rerun here |
| Paired signed-Gaussian/Mills LOW alternative; finite-window alternative | Outside this task's proof scope | Not run |
| Contact, initial support/moment acquisition, event acquisition, remaining conservation/resource algebra | Inputs to applying this Fourier result, not proved by it | Not rerun |
| Complete INITIAL42/LOCAL42, finite base, global sharp conjecture | Not established by this note | No native acceptance run |

No defect was found in the exact v6 triangle-LOW/six-piece-HIGH route at the required n>=42 scope. The previous generic phrase “retained Fourier primitives” can be replaced by the explicit proved propositions in `fourier-closure.tex`, subject to their input inequalities. This does not authorize removing acquisition hypotheses or accepting final numerical predicates.
