# Fixed-target conservation: analytic closure with explicit contact residuals

This new task starts from completed fork commit `b6a1bc7` in the separate worktree `conservation-v8`, branch `research/v8-conservation-20261028`. Existing proof sources, inherited logs and certificates are unchanged. The date is 28 October 2026.

The deliverable is a full locally derived proof of fixed-index attainment and closed-support contact, the contact-to-gap conservation calculation, physical defect positivity, and the moment-sensitive resource license. It adds an exact off-contact residual identity, permitting actual-law diagnostics without asserting that sampled laws maximize the objective. The prior v7 Fourier proof bounds precisely the error term appearing here.

## Exact result

For a standardized iid marginal and raw sum threshold H, fix c>0 and put

`a=sqrt(n)(P(S_n<=H)-Phi(H/sqrt(n)))-c rho`.

At each fixed n>=2 this objective attains its supremum. Its maximizing law has compact closed support and satisfies the fixed-target contact inequality everywhere, with equality on the whole closed support. A weak row failure `C_n>=c` gives an attained maximizing pair with a>=0, including the equality case. This uses no predecessor theorem, own-score ceiling, Fourier estimate, or fixed-law limit as n grows.

For that contact pair, the exact identity is

`(n+H^2)a + n c rho - n phi(H/sqrt(n))(gamma+3J)/6 + n^(3/2)L = R_c(H)`.

The raw remainder R_c has exactly the coefficients in v4 `excess.tex`; a is not normalized by rho. Specializing c=CE and using the physical defect D gives

`R_c = (n+H^2)a + n c rho(1-exp(-w)) + n phi(0)exp(-w)D/6 + n^(3/2)L`,

where `w=H^2/(2n)`. For a>=0 all four terms are nonnegative. If a common raw bound `R_c<=T<N c_lower rho_lower` has been proved, then

`gamma+3J>0`, `exp(-w)>=1-T/(N c_lower rho_lower)>0`,

`U=(n+H^2)a+n phi(0)D/6+n^(3/2)L <=R_c`,

`U <= R_c - (c_lower rho_lower-T/N)H^2/2`.

The last inequality prices the conserved phase term once. It does not turn an improved resource ceiling into an improved raw ceiling. Neither D<2 nor the stronger old absolute gate T<2N/5 is needed.

## What the new residual identity checks

For an arbitrary compactly supported law, let `Delta=Q_c-h`, where Q_c is the formal contact polynomial and `h(y)=P(S_(n-1)<=H-y)`. Define

`xi=E[X Delta(X)]`,

`B=integral_support tau(t)Delta(t)dt + sum_gaps tau_(u,v)(v-u)Delta(v)`.

Then the difference between the master left side and R_c is exactly

`n^(3/2)(B-H xi)`.

This identifies both uses of contact. The gap integration needs equality at upper endpoints and on any part of the support of positive Lebesgue measure; the truncated first-moment identity needs xi=0. At a maximizing pair, closed-support equality supplies all of them. Away from contact, deleting either residual is unjustified.

The support integral is necessary. For uniform `[-sqrt(3),sqrt(3)]` and H=0 there are no support gaps, but `Kq=3sqrt(3)/40` and `B=c Kq/n^(3/2)>0`. Omitting the integral would give a false identity. This is a counterexample to a contact-free simplification, not to the contact theorem or the Berry--Esseen conjecture.

The proof of the zero-bias CDF normalization does not rely on importing a named zero-bias theorem: apply signwise Fubini to `g_s(x)=min(s+x,H)` and use exchangeability. It gives directly

`integral tau h = E[X_n min(S_n,H)] = E[S_n min(S_n,H)]/n`

`=E[(Z^2-zZ)1_(Z<=z)]`.

The factor in the last expression is zero at the threshold, so endpoint atoms are covered.

## Source edges and hypothesis audit

Locations refer to task base b6a1bc7. Full content hashes are in the run receipts.

| Implication | Existing location | Checked requirement and reasoning |
|---|---|---|
| Maximizing sequence to fixed-index attainment | `mathematics/strategy-v4/2026-10-27/excess.tex:40–104` | c>0 bounds rho; bounded third moments give uniform integrability only of first/second moments. Moving closed thresholds use Portmanteau and right continuity. Maximality then forces equality of the limiting third moment. |
| Contamination to contact and compact support | Same file, 107–167 | Standardize the image of the fixed raw event, so its probability is a polynomial even at collisions. Closed-event contact is upper semicontinuous. Its zero integral and nonpositive sign force equality on closed support; the negative cubic leading term then yields compactness. |
| Contact to weighted gap integral | Same file, 210–251; manuscript `sections/05b-conserved.tex:41–94` | The interval is [u,v), including the lower endpoint and excluding the upper. No support term may be dropped away from contact. Countably many gaps are controlled by absolute bounds and bounded Fubini. |
| Contact to first truncated moment | v4 excess, 269–274 | Multiplication by X, actual iid exchangeability, and the residual xi give the precise factor sqrt(n). |
| Gap and moment evaluations to master identity | v4 excess, 253–322 | Direct conditional Fubini, the quadratic hinge, and the two slack evaluations produce the coefficient n+H^2. Both signs of H and atoms are retained. |
| Physical law to D>=0 | manuscript `sections/05-geometry-counts.tex:90–130` | Re-derived J<=rho+2m and gamma^2+4m^2<=rho^2 by signwise Cauchy and gap integration. This is an actual-law statement, independent of contact. |
| Master identity to unweighted resource and phase price | `mathematics/fixed-target-v5/2026-10-27/entry.tex:213–282` | The raw gate implies positive `M_c=c rho-phi(0)D/6`; only then may the Gaussian weight be removed. The stronger phase price uses `exp(-w)M_c>=c rho-T/n`, without multiplying unrelated lower bounds. |
| Error term to complete Fourier envelope | `mathematics/fixed-target-v7/2026-10-27/fourier-closure.tex` | Same signed Gaussian/cubic comparator and same E_n normalization. Its separate actual moment/event and damping hypotheses remain required. |

No own-score cap, a priori bound of order 1/n on the excess, least-index induction, three-loss bootstrap or finite certificate enters this analytic chain. Quantitative support R=96/25 still requires the separately proved predecessor/structural entry argument; compactness alone provides an unspecified finite radius.

## Bounded fresh evidence and negative controls

`conservation-check.py` imports no inherited program. It uses exact rational convolution and direct gap integration for seven standardized laws: symmetric and both orientations of skew Bernoulli, zero-atom, gapped three-point, four-point, and small far atoms. At n=4 and 9 it tests positive, negative and zero raw thresholds, including endpoint collisions. It checks 111 law/index/threshold cases and 666 affine-coefficient cases; 66 thresholds are actual sum atoms.

The normal values Phi and phi enter these identities affinely. The checker tests the three coefficient-basis assignments (0,0),(1,0),(0,1), so it verifies that formal affine dependence exactly. It does not mislabel rational placeholders as Gaussian CDF/density evaluations, and it does not assert that any test law maximizes the objective.

Detected negative controls include 52 cases where using a closed upper leakage endpoint changes the result, 582 cases where dropping H^2 a changes the identity, and nonzero boundary and first-moment residuals. It also checks the continuous-support example, failure of upper semicontinuity for open-event contact, and a standardized family with bounded rho but nonvanishing third-moment tails. The latter is why the attainment proof explicitly avoids a uniform-integrability-of-third-moments assumption.

Command, interpreter, hashes, stdout, stderr and return codes are under `runs/fixed-target-v8-20261028/conservation01/` through `conservation03/`. The second run adds the continuous-support control; the third verifies the closed-reflection identity, whose inequality is strict at all 66 atom thresholds. The proof explicitly bounds a negative closed-CDF error by the reflected positive closed-CDF error and assumes no equality at an atom. These checks support algebra and endpoint conventions; they do not prove compactness or a continuous-domain theorem by sampling. Those arguments are written in `conservation-proof.tex`.

## Status and remaining obligations

| Result | Mathematical status | Execution status |
|---|---|---|
| Fixed-n attainment, sign/equality interface, closed-support contact and compactness | Locally derived with the weak-limit and atom conventions explicit | No numerical optimization required or performed |
| Off-contact residual identity and contact specialization | Locally derived exact identity | Fresh bounded exact finite-law/affine checks passed |
| Physical defect sign and moment-sensitive resource/phase license | Locally derived under stated c=CE and raw-gate hypotheses | Algebraic identity controls passed; no acquisition rerun |
| Quantitative entry radius, numerical raw/resource ceilings, confinement and final exclusion | Separate named dependencies; not discharged by this note | No heavy/native or dense certificate run |
| Finite base or global sharp conjecture | Not established | Not run |

No defect was found in the retained fixed-target conservation formula. The exact off-contact version provides a stronger audit interface and makes clear why a contact residual cannot be silently discarded. The coordinating reviewer independently read the full proof and reported no blocker at the stated scope; this is a bounded mathematical review, not acceptance of the remaining numerical or global dependencies. The final closed-reflection bridge is stated explicitly and checked at atom thresholds.

The five-page standalone note compiled with TeX Live without warnings or overfull/underfull boxes in `conservation-build02`. All five pages were inspected in overview and pages 1–4 at full rendered size; no clipping, overlap or unreadable mathematical layout was found. Page 5 contains only the concluding scope paragraph. The visual review does not add mathematical acceptance.
