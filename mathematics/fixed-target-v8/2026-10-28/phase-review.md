# Independent review: same-cell signed phase resource export

Date: 28 October 2026. Review branch `research/v8-phase-review-20261028`, separate worktree `phase-review-v8`, base `8e1aea5e54359f4d1c4caf416df9c53e26eed238`. The constructor's files are read from sibling `phase-entry-v8`. No constructor file, old certificate or immutable baseline was edited; no inherited arithmetic module was imported or executed by this review.

**Verdict:** no blocking mathematical defect found in the signed resource join, the literal probability/noise restrictions, or the bounded region evaluator. The export is a reversible additive instrumentation of the pinned v7 source. Its original arithmetic conclusions are unchanged on the licensed actual-gap domain. The conclusions remain conditional on the genuine accepted v7 cover and its analytic inputs. The pure JSON region evaluator is not by itself an acceptance procedure for the provenance/completeness of an arbitrary submitted export.

| Reviewed result | Mathematical status | Execution status in this review |
|---|---|---|
| Signed phase bound and CE endpoint maximization | Independently derived under retained actual-law moment/Fourier/resource bounds | All1,364 endpoint quadratics reconstructed exactly from682 saved cells |
| Ordered raw bound to extra quadratic phase price | Independently checked; new raw ceiling precedes resource subtraction | All682 eta prices and prior density floors reconstructed exactly |
| Probability and lambda filters | Independently derived for every n>=42; both signs and closed endpoints retained | Exact actual-law control plus full exported-filter evaluations passed |
| Additive export and last-stage census | Source transform and its call location reviewed; does not replace the old accepted prefix | Exact text reconstruction/reversal passed;2048 source boxes and682 active exported cells reconciled |
| Fixed point and nine closed-region evaluations | Exact evaluation conditional on a genuine exported cover | Fresh independent rational check, no original evaluator imported |
| Full confinement/contact-ray theorem or complete count comparison | Not established by this review | Not run |

## 1. Resource derivation and the order of its premises

Write c=CE, and let the actual index be n>=N=42. The relevant law must be an attained fixed-target witness with nonnegative excess a and the retained contact/conservation hypotheses. For that law the resource is

\[
\mathcal U=(n+H^2)a+n\phi(0)D/6+n^{3/2}L\ge0.
\]

On one accepted signed moment/gap cell, the existing derivation gives

\[
R_c\le K_F+cA+(cK_1+\varphi W)H
       -(c\rho+\varphi\gamma/2)H^2+s_F|H|,
\]

where `W=J1+(M4-3)/6` is the signed integral in the conservation remainder, not the conditional fluctuation variable used below. Bounds `K1 in [kl,ku]`, `W in [wl,wu]`, `varphi in [phlo,2/5]`, `rho>=rl`, `gamma>=gl` come from the same law/cell. The formal multiplier c is CE, enclosed by the two rational endpoints C0,C1. It is not an upper bound for the law's attained normalized score.

The former density floor uses the **previous raw** bound. The original absolute-phase quadratic then gives a new raw ceiling T=`new_raw`, intersected with the previous raw ceiling. Only after obtaining T does conservation imply

\[
\mathcal U\le R_c-\eta H^2,\qquad
\eta=(C_0r_l-T/N)/2>0.
\]

Indeed the raw license yields `exp(-w) M >= c rho-T/n>0`, where `M=c rho-phi(0)D/6` and `w=H^2/(2n)`. Therefore
`R_c-U=n(1-exp(-w))M >= H^2(c rho-T/n)/2 >= eta H^2`.
This is the ordered phase price already established by the fixed-target conservation argument. Replacing T by a resource bound in its own derivation would require another argument; the export does not do so.

For h=|H| and each endpoint c, set

\[
B(c)=K_F+cA,\quad Q(c)=c r_l+\min_{\varphi\in[\varphi_l,2/5]}\varphi g_l/2+\eta,
\]

\[
F_+(c)=\max(cK_1+\varphi W)+s_F,\qquad
F_-(c)=-\min(cK_1+\varphi W)+s_F.
\]

The maxima/minima run over the entire rectangular enclosure. For H>=0 use F+; for H<=0 use F-. Then

\[
0\le\mathcal U\le\min\left(T,\max_{c\in\{C_0,C_1\}}
       [B(c)+F_\pm(c)h-Q(c)h^2]\right).
\]

The c-endpoint step is valid: for fixed h>=0, F±(c) is the maximum of finitely many affine functions of c; B and Q are affine. Hence the displayed expression is convex in c and maximized over the enclosing interval at an endpoint. No reversal from the negative quadratic coefficient is involved. Signed slopes may be negative and must not be replaced by zero. A negative final upper bound is a contradiction with U>=0, not a numerical resource floor.

The independent coefficient checker uses the closed-form rectangle support, rather than repeating the constructor's eight-corner loop:

`max = c*ku + (phi_upper if wu>=0 else phi_lower)*wu`,

`min = c*kl + (phi_lower if wl>=0 else phi_upper)*wl`.

These recover all saved signed slopes exactly. It also reconstructs B,Q, the prior density floor, the ordered eta price, both event-probability endpoints and the row raw/defect maxima.

## 2. Actual probability and noise constraints

Use the manuscript's sign split `p=P(X>0)`, `q=1-p`, `v=pq`, `m=E X_+`, with a possible zero atom assigned to the nonpositive class. Conditional means are m/p and -m/q. Let theta± be the unnormalized conditional variance contributions and theta=theta++theta-=1-m^2/v. Define lambda=n*v*theta/(1-theta). Thus, exactly,

\[
\theta=\frac{\lambda}{nv+\lambda},\qquad
m^2=\frac{v^2}{v+\lambda/n},\qquad
\beta=1-2p-2q\theta+2\theta_+.
\]

The beta identity follows by writing `EX_+^2=m^2/p+theta+` and `EX_-^2=m^2/q+theta-`. Since `0<=theta+<=theta`,

\[
1-2p-2q\theta\le\beta\le1-2p+2p\theta.
\]

For a closed panel [pl,pu], let vlow be the minimum of pq at its endpoints, and vhigh the maximum of both endpoints and1/4 when the panel contains1/2. If `0<=lambda<=Lambda` and n>=42, then

\[
\theta\le\Theta=\frac{\Lambda}{42v_{low}+\Lambda},\qquad
\sqrt{\frac{v_{low}^2}{v_{low}+\Lambda/42}}\le m\le\sqrt{v_{high}},
\]

\[
1-2p_u-2(1-p_l)\Theta\le\beta
\le1-2p_l+2p_u\Theta.
\]

Here `v^2/(v+s)` increases with v>0, since its derivative is `v(v+2s)/(v+s)^2`; it decreases with s>=0. These restrictions are necessary, not sufficient to reconstruct a law. Outward square-root rounding enlarges the m interval, as required for safe exclusion. The literal probe with Lambda=3/20 is valid for the **whole noise range [0,3/20]**, not only equality. It does not cover lambda>=3/20 by this filter.

The fixed probe's endpoint-only vhigh formula is sound on its literal panel [.41,.42], which lies below1/2. Its generalization to an interval crossing1/2 would be unsafe. The new `phase_region.py` explicitly includes the interior1/4 candidate and so avoids that issue. Closed overlaps are retained for p,m,beta and H; no boundary plane is discarded.

An exact three-point actual-law control has p=4/5, q=1/5 and only positive-side conditional variance. Choose t=1/100,
`a=2(1-(16/5)t^2)/(1+(16/5)t^2)`, `epsilon=4t/(1+(16/5)t^2)`, `b=a/4`, and put masses q,p/2,p/2 at -a,b-epsilon,b+epsilon. This law is exactly centered and standardized and has beta=`1-2p+2p theta > 1-2p+theta`. It rejects the tempting but incorrect symmetric `+Theta` upper price above1/2. The same law checks the m/lambda identity at n=42,43,100,10000.

## 3. Instrumentation, coverage, and closed phase intervals

Reviewed constructor locations are `build_phase_core.py:6–27`, `phase_probe.py:11–35`, and `phase_region.py:29–61`. Frozen copies for the first two and the generated core are in constructor run `phase01`; the reviewed region source is copied into this review's `phase-review01`. All hashes are recorded in receipts.

The builder requires core SHA256 `1f40ccb90eb58a7f84dc61a0a5dd9bf6e6eb4e341aa6c9c6d049d08451f5211b`. It adds list initialization, an append immediately after every surviving cell's original active increment, and one return field. The inserted gap guard only rejects an unlicensed export. The new computations do not change original bounds. The loop aliases c,q finish at the same last coefficient endpoint as the preceding original loop; no later bound uses a changed value. The independent checker extracts the three literal patch pairs without executing the builder, reconstructs the archived generated source byte-for-byte, reverses the pairs, and recovers the exact pinned original.

The probe binds accepted proof SHA256 `61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae`, skips only persistently excluded rows, and replays the fourth stage from the recorded third-stage raw/defect bounds. This is a last-stage replay conditional on the accepted prefix; it is not a new replay of all earlier stages. Sixteen still-requested rho rows give2048 boxes. The source append position and length check cover every682 active cell. My checker reconciles the per-row export census with the recorded accepted rows and recovers their raw/defect maxima. It also checks each exported H ceiling lies on the decreasing side of both absolute quadratics and makes them nonpositive there.

For a closed phase interval [hl,hu], the relevant cell interval is `[hl,min(hu,cellH)]`; cells with `cellH<hl` are safely absent. Each Q>0 quadratic is concave in h. Its maximum is at an endpoint or at h=F/(2Q) if that point lies inside. The constructor uses a clamped vertex. My implementation separately compares both endpoint values and the interior vertex value, yielding exactly the same results. Taking the maximum of these complete cell bounds and intersecting with the cell's raw ceiling is sound. The negative control `2h-h^2` on[0,2] shows why endpoints alone cannot replace the interior vertex.

The saved export SHA256 is `b18599468c975032f4078e7a5f734fd6430b2b7da583789de58d9537d323f690`. Its count and coefficient self-consistency do not prove that an arbitrary JSON came from this complete computation. A source-bound exact replay acceptor is a separate provenance requirement; the constructor is adding one. That later acceptor is outside this snapshot. The existing evaluator correctly describes itself as a resource-interface calculation rather than a full confinement acceptor.

## 4. Independently reproduced bounds

All rows below have p in[.41,.42] and use outward rational bounds with denominator10^9. The signs refer to the original raw H, not a replacement of p by min(p,1-p).

| Absolute raw phase h | Noise ceiling | Retained cells | U for H>=0 | U for H<=0 |
|---|---:|---:|---:|---:|
| 1.25 | none |331|1.032820261|1.266287022|
| 1.25 | .15 |15|-.128026665|.206210125|
| [1.24,1.26] | .15 |18|-.094649077|.218329547|
| [1.20,1.30] | .15 |22|-.033287706|.265382458|

The first row lies below the proposed scalar barrier1.600336284 numerically. Whether that barrier applies to every needed confinement case is a separate analytic interface; this review does not infer it. Under the retained witness/entry hypotheses, the negative positive-phase bounds exclude those particular closed p/phase/noise regions. The negative-phase bounds supply resource ceilings only. Neither statement proves all panels, the full phase range, A<1/2, or d0<1/4.

`phase-review-check.py` imports no original module and performs no producer replay. Its fresh exact run reconstructs1364 quadratics, matches the original point probe exactly, and independently computes all nine saved phase/noise regions (including noise ceiling .16). Run02 additionally compares every exact region result with constructor `phase02`, not just decimal displays. Commands, interpreter, times, return codes and hashes are under `runs/fixed-target-v8-20261028/phase-review01` and `phase-review02`.

No claim of a full theorem follows from the arithmetic PASS alone. Remaining inputs are the genuine accepted cover, its contact/conservation/support/Fourier premises, complete source-bound export acceptance, and the separately proved global contact-ray/confinement joins.
