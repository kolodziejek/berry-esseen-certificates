# Independent thirteen-panel low-noise support check

The direct heat argument covers all thirteen closed probability panels `[i/100,(i+1)/100]`, `i=40,...,52`, for the entire closed noise interval `0<=lambda<=3/40`. Conditional on the previously acquired `.6` strip and inward displacement `<.072`, and on the sharp fixed-target contact/Gaussian premises, it gives `|U|<1/2` for every actual `n>=42` and every raw threshold. No Fourier or project module is imported by this new check.

The statement includes `p>1/2`, the central probability seams, zero noise, and the shared `lambda=.075` endpoint. It does not cover panels25–39, larger noise, complete local count exclusion, or BASE41.

## Independent derivation

The proof is [low-noise-proof/main.tex](low-noise-proof/main.tex). In one common marginal write `X=ell(Z-p+U)`, where `Z=1{X>0}`, `E(U|Z)=0`, and `lambda=n E U²`. The actual central gap supplies the inward support directions. The preceding Y strip and displacement bound imply the prior `|U|<.6` before the new contact argument is used.

Variance gives `theta=lambda/(n p(1-p)+lambda)` and `ell²=(1-theta)/(p(1-p))`. On each whole interval use the smaller endpoint value of `p(1-p)` for `vmin`; the maximum `vmax` must include1/4 at or across1/2. The beta interval is exactly the safe monotone envelope

`1−2u−2(1−u)Theta <= beta <= 1−2l+2lTheta`.

The absolute cubic expansion is conditional on the same sign variable. Its noise coefficient is bounded by `(3 max(p,1-p)+.6)/(p(1-p))^(3/2)`. A single exact bound24 works for the entire p range: `24²*(6/25)³−(12/5)²=34416/15625>0`. This handles either orientation without identifying p with its reflection. The Bernoulli skeleton factor `(1−2v)/sqrt(v)` is decreasing in v, so it is maximized at vmin. These facts give `rho<=rhoB(vmin)+24*.075/42` with directed rational square roots.

Apply the retained absolute-quartic heat bound at `u_minus=ell_lower*(l+.5)` with signed beta coefficient `−beta_lower`, and `u_plus=ell_lower*(1.5−u)` with `beta_upper`. All boundaries have square greater than3. Strict negativity of each contact upper bound and the six Q/L derivative gates excludes its whole exterior ray, including boundary atoms. Together with the retained inward displacement `<.072`, this gives strict half-amplitude support.

## Fresh exact evidence

| Result | Mathematical status | Execution status |
|---|---|---|
| General-p cubic, scale and beta envelopes | Independently derived conditional-marginal identities and monotone bounds | Exact rational domain gates passed |
| Thirteen-panel exterior rays | Conditional on the stated contact/heat and acquired-strip premises | Fresh PASS:26strict boundaries and156strict continuation gates |
| Zero noise and seams | Included analytically without division by noise | All13closed intervals checked, adjacent endpoints equal |
| Larger noise and other panels | Not established by this result | Not run |

The checker [low-noise-independent.py](low-noise-independent.py) uses only Fraction, isqrt and JSON. Its directed roots have precision10^-12. It does not import the other agent's checker or data. Full rational outputs, interpreter/version, source hash, stdout/stderr hashes, return code0 and source snapshot are in `runs/fixed-target-v8-20261028/low-noise-independent01`.

The following decimal values are display-only approximations to the exact negative upper bounds; they are not used for acceptance:

| Panel | Negative boundary | Positive boundary |
|---|---:|---:|
| 40 | -0.517688482 | -0.213107097 |
| 41 | -0.516457003 | -0.246953457 |
| 42 | -0.513874522 | -0.278483558 |
| 43 | -0.509974899 | -0.307845566 |
| 44 | -0.504783480 | -0.335170410 |
| 45 | -0.498317688 | -0.360573624 |
| 46 | -0.490587481 | -0.384156916 |
| 47 | -0.481595691 | -0.406009472 |
| 48 | -0.471338259 | -0.426209056 |
| 49 | -0.459804371 | -0.444822924 |
| 50 | -0.444822924 | -0.459804371 |
| 51 | -0.426209056 | -0.471338259 |
| 52 | -0.406009472 | -0.481595691 |

The worst upper bound is panel40's positive ray and is strictly less than−.213. Seven controls reject: coefficient18 in the uniform cubic bound, an endpoint-only pq maximum across1/2, the wrong beta reflection, an unlicensed quarter-amplitude radius, omission of ell, replacement of strict negativity by equality, and the plus-Theta beta shortcut above1/2. The last control uses a centered variance-one three-point law with p=.52 and checks its moments exactly.

The constructor subsequently compared its independent1e−10-root table with this table: scalar probability/beta/variance quantities agree, its ell is no larger, and its rho is no smaller. That comparison is supplementary evidence; agreement is not an additional proof premise.

## Source interfaces and limitations

- `mathematics/fixed-target-v8/2026-10-28/moment-entry-v8-proof/main.tex` from commit0fbdc875: prior Y strip on panels40–52 and displacement<=.0719539227. The new argument does not change that proof and does not assert it is unconditional.
- `mathematics/fixed-target-v5/2026-10-27/entry.tex:64–155`: exact fixed-target contact, sharp predecessor, nonnegative excess, heat expansion, Gaussian bounds, whole-ray derivative inequality. The use here preserves the absolute quartic term for radii below the old positive-quartic range.
- `mathematics/fixed-target-v8/2026-10-28/phase-confinement-proof/main.tex:190–270`: the previous single-panel direct argument was read as a proposed starting point. Its p<1/2 specialization was independently replaced by the two-orientation derivation above; no numerical implementation from the new13-panel constructor was imported.

Source hashes are recorded in `low-noise-independent-sources.json`. The proof compiled successfully; the exported pages and compilation receipt accompany the evidence. This is a conditional low-noise lemma on these thirteen panels, not complete confinement for their larger-noise parts and not a certificate-deletion authorization.

## Continuous endpoint reduction

A second independent calculation verifies the common caps Theta=37/5000, ell>=249/125, rho<=221/200; all26 coarser panel boundaries also pass. This is recorded separately in low-noise-common-independent01 and imports only this reviewer's pinned evaluator.

The continuous proof appended to the TeX note replaces those13 new rows entirely: use the actual z=p on the negative ray and z=1-p on the positive ray, not an interval endpoint. Then t=(249/125)(z+1/2) and b(t)=2(1-Theta)t/(249/125)-2+3Theta cover[1.7928,2.1912]. The quartic is negative throughout, so the contact upper bound is one quintic. Its third derivative is a convex quadratic with negative endpoint values. Hence its first derivative is concave; positive values at both endpoints prove the quintic increasing and negative throughout. The continuation checks distinguish total derivatives along b(t) from fixed-beta radial derivatives.

The initial extra assertion Psecond(left)<0 is false: exact evaluation gives approximately+.022852502106885685. The failed run and diagnostic remain in low-noise-continuous-independent01. The corrected concave-first-derivative criterion passes in low-noise-continuous-independent02, with the same contact target and no grid. The maximum contact upper bound is approximately-.17797541617518625. This is a new sufficient proof criterion, not acceptance of the failed condition.

The general conditional lemma works on p in[.4,.6] if its strip/inward premises are supplied there. The presently acquired entry application is only[.4,.53]. The old13-panel strip antecedent remains; only the new low-noise boundary grid becomes unnecessary.
