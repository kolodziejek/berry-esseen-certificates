# Independent adversarial review: zero-loss support lifting

Reviewed commit: `341c1e3f77806a4aaa178051f6f8c80c13bd63ac`, on separate branch `simplify/review-support-20261027`. This reviewer did not construct `zero-loss-support.md` or `check_support_lift.py`.

**Recommendation:** accept the support-lift argument as a conditional mathematical component. No blocking algebraic, endpoint, sign or ancestry defect was found. This recommendation does not accept the inherited polynomial sign predicates, all-index LOCAL42, the finite base or a global Berry–Esseen proof. Those remain separately named obligations. No existing certificate or theorem should be removed or relabelled on the strength of this review.

| Reviewed result | Mathematical status | Execution status |
|---|---|---|
| Finite `.19`-loss polynomial -> infinite zero-loss polynomial on the two splice intervals | Independently derived exact implication | Fresh submitted checker PASS; separate independent exact identity checks PASS |
| Complete support rays, both signs and every raw threshold | Independently derived from the original contact/heat/derivative inequalities | Exact endpoint gates checked; no threshold sampling used |
| Initial parameters and all64 LEFT support-call inputs | Static identity and ancestry verified; acquired moment bounds remain premises | Fresh independent source/JSON check PASS |
| Old Bernstein signs/resource acquisition | Supplied conditional proof predicates | Not run or accepted here |
| BASE41 + equality-compatible uniform zero-loss LOCAL42 -> strict tail from42 | Valid conditional least-index logic | No base or complete LOCAL42 execution |

## Exact statement reviewed

Let `n>=42`, and let `(P,H)` be an unrestricted attained positive closed maximizing pair, with `C=C_n>=C_E`, standardized law, finite third absolute moment `rho`, signed second moment `beta`, and global predecessor decrement

`d=n(C_(n-1)-C_n)_+=0`.

Assume the retained analytic contact/heat inequalities. For each of the65 frozen support-input tuples (one initial tuple and64 LEFT tuples), assume its original finite42–48 support polynomial gates hold strictly on its full closed radial cover, and assume that its upper-bound parameters `r,b` actually satisfy `rho<=r`, `|beta|<=b` for this same law at this step. Then the same recorded support radius holds at the actual index `n`, without an upper bound on `n`.

The LEFT conclusion is sequential: a contracted radius is available only after the preceding same-law resource enclosure. No assertion is made that all64 moment pairs apply to an arbitrary law simultaneously, or that zero scalar decrement forces zero conditional noise or defect.

The relevant primary source is `paper/analytic-supplement.txt`: contact at263–309; direct derivative/ray proof350–410; signed fifth-order identity and envelope455–564; finite/infinite polynomial construction566–640. The exact kernels are finite61 blobs `09a6e27ef42847cef0ac258504546eaef3a3035e83171143f1c2fd848736ac6c` (`fifth_heat50.py`) and `650d7f3617775102fe92977605dfda5fb68a11e0ad738eb799aab77bc4a79e18` (`heat_support50.py`). Their bytes and literal callers were inspected directly without importing them.

## Independent derivation of the transfer

Set `c=819/2000`, `N=42`, `v=41`, `q=19/100`, and retain the original rational square-root bounds `ell<=sqrt(41)` and `S>sqrt(42/41)`. Define

\[
A=(u^3-3u)/6,\quad J=u^5-15u,\quad H_4=u^4-6u^2+3,
\quad D_+=J/4920,\quad D_-=J/5640,
\]

\[
W=A-15D_+/2,\quad B_2=H_4^2/10496,
\quad Q_{r,b}(u)=-u^3+(3/2)ru^2+3bu+(48/(125\cdot42))r.
\]

At an actual `n>=42`, `D_actual=J/(120(n-1))` is bounded above by `D_+` but has only the uniform lower bound zero. This is why merely retaining the old finite theorem is invalid. The adverse remainder and positive scale factors can be frozen at42; `K=0` means there is no `K/L` score-floor dependence to change.

Subtracting the old finite polynomial from the uniform zero-loss polynomial cancels the unchanged `A`, `B_2`, remainder and cubic terms. The remaining coefficient is

\[
3(2/5)S^3D_-W-rSqW
=SW\left(\frac{S^2J}{4700}-.19r\right).
\]

Thus the denominator4700 is exactly `(5/6)*5640`, not an estimated constant. The domination polynomial gains exactly `3D_-W`. This independently confirms `zero-loss-support.md:78–79` and the implementation at `check_support_lift.py:90–108`.

For `u>=5/2`, `J=u(u^4-15)>0` and `J'=5u^4-15>0`. Old strict gates give `W>0`; therefore it is enough to verify

\[
(81/80)^2J(U)/4700<.19r_{\min}\le.19r,
\qquad S<81/80.
\]

This gives a strict improvement on the entire `[R,U]`, including `R` and `U`, not just a sampled value at the splice. The source domination gate stays positive, and the old signs of `A,H4,J,W,-Q` are unchanged. The positive envelope `T` remains above `A/2+2B_++3D_+`; hence replacing `phi(0)` by `.4` and the scale by `S` has the correct direction.

The source envelope treats positive `t` and `|z|<=1` by a Gaussian fourth-derivative lower tangent, handles `|z|>=1` by absolute derivative bounds, and treats negative `t` using the global first-term bound `<A phi(0)/2`. These three cases justify the simultaneous assertion for **both signs of `t` and every real raw `H`**. There is no fixed-law or fixed-threshold asymptotic argument.

The exact independent margins match the proposed ones:

| Splice | Parameter rectangle | Strict margin `.19r_min-(81/80)^2 J(U)/4700` |
|---|---|---|
| Initial `U=21/5` | `46/25<=r<=37/20`, `b<=2/3` | `3679155107/47000000000` |
| LEFT `U=39/10` | `1<=r<=3/2`, `b<=1/2` | `17940880361/3008000000000` |

**Parameter versus moment:** `r_min` bounds the certificate's upper-bound parameter `r`, not the actual `rho`. The initial value is exactly `r=7361/4000`. A law with `rho=1` can still satisfy `rho<=7361/4000`; nothing in this proof would then assert `rho>=46/25`. The old `.19r` allowance is part of a frozen certificate polynomial. Its removal supplies the algebraic reserve even if the actual third moment is smaller. The manuscript states this distinction correctly at162–164.

## Independent ray and scale check

For the original Gaussian expression `H_n`, set `z=H/sqrt(n)`, `y=(H-t)/sqrt(n)` and `s=sqrt(n/(n-1))`. Differentiating gives

\[
\partial_t H_n=n\phi(z)+Ht\phi(z)-ns\phi(sy).
\]

The Taylor remainder in `n phi(y)` after its linear term is at most `phi(0)t^2/2`; the linear term is **plus** `Ht phi(z)`. Also `partial_s[s phi(sy)]=-phi''(sy)`, so the scaling error is at most `n phi(0)(s-1)`. Consequently

\[
|\partial_tH_n|\le\phi(0)(t^2/2+1/2+e_n),\qquad
e_n=n(s-1)-1/2.
\]

With `x=1/n` and `a=48/125`, expanding `(1-x)(1+x/2+a x^2)^2-1` gives `x^2` times the stated cubic. Its nonconstant coefficients are negative, so its minimum on `0<x<=1/42` is its endpoint value `118707/42875000>0`. Squaring positive quantities therefore gives `e_n<a/n<=a/42`. The lower bound `e_n>0` follows similarly from `(1-x)(1+x/2)^2<1`. No discretization or limiting remainder is used.

For each fixed frozen tuple, let `Q=Q_(r,b)`. On `[U,infinity)`, `Q<=Qmax` and `Q'<=Qmax'` because `r,b` enter them with nonnegative coefficients. The computed strict gates for `Qmax,Qmax',Qmax'',Lmax,Lmax'`, together with `Qmax'''=-6` and `Lmax''=2/5-6c<0`, keep `Q` negative and the envelope derivative negative for every `u>=U`.

It matters that the actual envelope being continued is

`H_n(H,eta*u)+c Q_(r,b)(u)`, for the **original** tuple,

whose negative endpoint was proved by the polynomial transfer. The larger common caps are used to bound derivatives and the sign of `Q`; no unproved replacement of the endpoint by `H_n+c Qmax` occurs. For either `eta=+1` or `-1`, the chain-rule derivative is bounded above by the absolute `t` derivative plus `cQ'`. Thus the same strict decrease covers both whole rays.

Finally the contact inequality has bracket

`-|t|^3+(3/2)rho t^2+3 beta t+rho e_n <= Q_(r,b)(|t|)<0`.

Since `C>=c>0`, replacing its multiplier by `c` is valid only after this negativity is established; the source and new proof do so. The same-owner predecessor allowance is no larger than the global decrement, so its positive part is zero. Strict negative contact contradicts equality on the full closed support, including the exact radius, atoms of arbitrarily small mass and exterior accumulation points.

## All64 LEFT inputs and scope of the checker

The native caller is blob `a565247f6587f3bb07dd67ef2100d08f70aebbe7543937f1ab98f8d09cf31eb6`, logical path `package_audit/left42_exact/accept_acquisition.py`. Its lines37–42 replace only `r,b` by preceding resources and call `target(42,48,0,R,.19)`; lines72–80 make one common bridge and later contractions in their original order. Its literal structure checks at45–63 bind the fixed route, actual radii and final resources.

The independent check read the pinned acquisition proof `419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393`, route `df1631620cf1135a5bb6fb9cd28f6c514f6a0451f7c1699ad55054fa1b23dcd0`, and INITIAL input `bd2a808005703ac1fbdb5fb17bc63637f48ebb568f65220f99c47692108a23e0`. It checked:

- All15 ordered coarse cells and11 surviving coarse parents; the common `r,b` are their maxima and its radius is `121/40`.
- All55 fine cells are the five ordered subdivisions of each surviving parent, with matching route cells.
- Every fine trace begins at the common radius, later radii decrease strictly, excluded rows never continue, and final resources/radii match the last stage.
- Every later support call uses the immediately preceding resource's `rho,beta`; all63 later calls are present, making64 with the common bridge.
- Every old radial-cell list runs contiguously from its recorded radius to4.5; all tuple parameters lie in the claimed LEFT rectangle.

Observed ranges agree with the manuscript: `r_min=116242091/100000000`, `r_max=71458741/50000000`, `b_max=46459359/100000000`, and `2.5<=R<=3.025`.

These are ancestry/shape/identity checks. They neither recompute the old Bernstein signs nor establish that an actual law satisfies the recorded resources. The submitted checker appropriately states that limitation. Its helper is not a general acceptance parser for arbitrary replacement proof objects; the complete archive and proof hash pins are material. The independent check adds route/subdivision checks for the exact reviewed source without changing the submitted checker.

## Adversarial checks actually performed

Evidence is committed in `runs/zero-loss-support-20261027/review-support01/`. Both the submitted checker and the independent script ran under CPython3.9.6 with `-I -B`, no optimization. Both returned0 with empty stderr. Times recorded in the receipt were approximately0.37s and0.33s respectively; no archived/native certificate program was run.

The independent script imports no submitted implementation. It uses scalar formulas for both contact and domination polynomials, checks their differences at12 distinct rational values, and records their degree bound11. Twelve exact roots prove equality of each polynomial difference; this is **not** sampled positivity. It checks130 identities over65 tuples, with1560 exact identity evaluations, and rederives both splice margins, all twelve ray gates, the scale margin and the initial signed-moment parameter inequality.

The submitted checker rejected its ten controls. Eight additional independent controls rejected: retaining full `.19` loss; allowing loss`.01` in the broad `r>=1` LEFT rectangle; moving the LEFT splice blindly to4.5; enlarging the ray `r` cap to4; broken coarse ancestry; a missing support edge; a changed predecessor moment; and a reversed radius schedule. The loss`.01` failure is a counterexample to that **broader parameter-rectangle estimate**, not to a Berry–Esseen theorem or to every possible positive-loss extension using the tighter recorded `r` values.

No iid-law simulation or threshold sampling was performed. Such diagnostics would not establish the conditional polynomial implication; the relevant universal threshold and endpoint issues are handled analytically above. No old sign predicate was quietly promoted from historical metadata to a fresh PASS.

## Findings and global logic boundary

**Blocking findings:** none for the support-lift implication at the stated conditional scope. The algebra, loss direction, parameter interpretation, strictness, splice domains, both rays and all64 selected inputs agree with the original formulas.

**Important retained limitation:** support lifting alone is not uniform LOCAL42. Every other index-sensitive resource, Fourier, confinement, finite-binomial and signed local comparison edge in `uniform42.md` remains a separate premise/review. This review read its conditional theorem and the connection to support but did not independently re-audit its entire non-support matrix.

The proposed global composition is logically valid if that equality-inclusive uniform zero-loss LOCAL42 implication is supplied. From BASE41, choose the least `n>=42` with `C_n>=C_E`. Its predecessors are sharp; at42 they are40 and41. The scalar42 bound `n(C_n-C_E)<3003/10250<.3`, own cap `<.4226`, both deleted caps `<.4253`, and zero decrement supply its hypotheses. The retained attainment statement explicitly includes the critical value (`paper/analytic-supplement.txt:215–250`), so equality is not lost by extracting a maximizing witness. Uniform LOCAL42 then contradicts the first contrary index. Choosing `>` instead would prove only the weak conclusion.

No unconditional BASE41, full uniform LOCAL42, complete certificate acceptance, provider-graph closure or deletion permission follows. The appropriate review outcome is acceptance of this new conditional support component, with the existing proof obligations and baseline preserved.
