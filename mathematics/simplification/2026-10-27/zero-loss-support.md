# Lifting the finite support certificates at zero predecessor loss

Source baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`, preserved in
`kolodziejek/berry-esseen-certificates`. Date: 27 October 2026.

This is a new mathematical lemma. It reuses the **polynomial inequalities**
certified for the finite interval 42–48, without applying that finite-index
theorem outside its stated domain. At zero predecessor loss, the same support
radii follow for every actual integer n >= 42. No existing certificate,
acceptor, theorem statement or acceptance target is modified.

| Result | Mathematical status | Execution status |
|---|---|---|
| Finite-to-infinite contact-polynomial identity and two whole-ray splices | Locally derived below and checked exactly | Fresh standard-library rational/polynomial checks; ten negative controls |
| Binding to the initial and all 64 LEFT42 support invocations | Exact source/input identification; actual acquired moment bounds remain premises | Fresh read-only archive/JSON inspection; 130 polynomial identities checked |
| All-index support conclusion | Proved implication from the retained analytic contact/heat inputs and old finite polynomial sign predicates | Old numerical sign predicates not rerun or accepted by the new checker |
| Uniform LOCAL42 and global sharp bound | Separate conditional compositions; see uniform42.md and the main simplification note | No full numerical campaign or whole-theorem acceptance |

## 1. Exact source boundary and notation

The contact bound and signed fifth-order envelope are in
`paper/analytic-supplement.txt:455–640`; the direct whole-ray derivative
argument is at :350–410. The archive
`verification/finite-tail/sources/backend.zip` contains the corresponding
finite-source bodies at `finite61/blobs/<SHA256>`:

- `fifth_heat50.py`, SHA
  `09a6e27ef42847cef0ac258504546eaef3a3035e83171143f1c2fd848736ac6c`;
- `heat_support50.py`, SHA
  `650d7f3617775102fe92977605dfda5fb68a11e0ad738eb799aab77bc4a79e18`;
- `acquisition/check_local42_support.py`, SHA
  `343046eaf0a3e6b2e140644cee19b7764d76b4171b844eaac27fb1a288b12d2e`;
- `package_audit/left42_exact/accept_acquisition.py`, SHA
  `a565247f6587f3bb07dd67ef2100d08f70aebbe7543937f1ab98f8d09cf31eb6`;
- the latter's `acquisition42_proof.json`, SHA
  `419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393`.

The logical prefix for these paths is
`work/toward40_20261007/audit43/capsule/work/below49_20261006/`.
The initial support call is `(42,48,0,3.84,.19)` at line7. LEFT's lines37–42
substitute already acquired moment bounds into the same kernel; lines72–80
give its common first contraction and later ordered contractions. The lower
score parameter is always `c=.4095`; no positive barrier K is involved.

Fix N=42, L=48, q=.19 and v=N-1=41. Let r and b be certified *upper-bound
parameters* for the actual rho and absolute beta. Write u=|t| and

    A=(u^3-3u)/6,  J=u^5-15u,  H4=u^4-6u^2+3,
    Dplus=J/(120*41),  Dminus=J/(120*47),
    W=A-(15/2)Dplus,  B2=H4^2/(256*41),
    Q=-u^3+(3/2)r u^2+3b u+(.384/42)r.

Use exactly the inherited rational square-root bounds ell and S:
ell^2 <= 41 and S^2 > 42/41, with
`S=202424330939/200000000000 < 81/80`. The adverse remainder polynomial E is
unchanged. With K=0 neither c nor these constants depends on the upper index.

The old finite-band contact polynomial, including its allowed loss q, is

    P48,q = (2/5)S^3[(A-3Dminus)W+B2]
             +S^3 E W + c Q W + r S q W.

Its corresponding domination gate is

    G48 = [A/2-3Dminus-3Dplus-H4/(12ell)]W+B2 > 0.

The inherited finite acceptance supplies strict signs for A,H4,J,W,G48,-Q
and -P48,q on every point of [R,4.5]. These are inequalities between frozen
polynomials in u. Their use below does not assume that the actual n is <=48.

## 2. The new domination identity

At an actual index n >= 42 with predecessor decrement zero, the uniform
infinite-band heat envelope sets the favorable lower bound on D to zero.
Keep its adverse bound Dplus, E, Q, ell and S unchanged. Its polynomial is
Pinf,0, obtained by setting Dminus=0 and q=0. Direct subtraction gives

    Pinf,0 - P48,q = S W [ S^2 J/4700 - .19 r ],
    Ginf - G48 = 3 Dminus W.

Thus the outer-domination gate improves. On any interval [R,U] where

    (81/80)^2 (U^5-15U)/4700 < .19 r_min <= .19 r,

the contact gate improves as well. Indeed J is positive and increasing for
u >= 2.5, S<81/80 and W>0. All other gates are unchanged. Consequently
Pinf,0<0 on [R,U], including U. The signed fifth-order envelope then gives
strict negative contact there for both signs of t and every real raw H,
uniformly over every n >= 42.

This is the step unavailable in a naive extension with the full .19 loss.
Dropping Dminus while leaving that loss unchanged increases the contact
upper bound; it is the additional **zero-loss hypothesis** that pays for it.

## 3. Continuing the entire rays from the splice point

It is unnecessary to assume the old coarse ray estimate works below4.5.
Instead use the direct derivative bound, valid for every H and t,

    |partial_t H_n(H,t)| <= (2/5)(t^2/2 + 1/2 + e_n),
    e_n = n(sqrt(n/(n-1))-1)-1/2 < .384/n <= E0=.384/42.

For completeness, setting x=1/n, the scale inequality is equivalent to the
positivity of

    (2a-3/4) - (a+1/4)x + (a^2-a)x^2 - a^2 x^3,  a=48/125.

After the positive constant, its coefficients are negative. Hence its minimum
on 0<x<=1/42 is at1/42, where it is `118707/42875000>0`. This establishes
the uniform scale correction without a fixed-law limit.

Choose common parameter ceilings r<=r_max and b<=b_max. Define Qmax by those
ceilings and define

    Lmax(u)=(2/5)(u^2/2+1/2+E0) + c Qmax'(u).

If Qmax(U), Qmax'(U), Qmax''(U), Lmax(U), Lmax'(U) are all negative, then
Qmax and Lmax remain negative for every u>=U: Qmax'''=-6 and
Lmax''=2/5-6c<0. The actual Q and its derivative are bounded above by these
majorants for u>=0. For each sign eta=+1,-1, the envelope

    H_n(H,eta u)+c Q(u)

is therefore strictly decreasing on [U,infinity), and its value at U is
already strictly negative by Section2. This excludes both complete rays.
It uses the same current law, raw H and contact identity as before; exterior
atoms, accumulation points and arbitrarily small atom masses are included.

## 4. Two rational splices cover every required support invocation

For the **initial radius R=3.84**, the original moment parameter is

    r=min(.3031*.646/(.4095-.3031), .3322*.429/(.4095-.3322))
     =7361/4000,

and its outward-rounded beta parameter is
`b=641562334877/10^12`. Use U=21/5, r_min=46/25, r_max=37/20,
b_max=2/3. The contact domination margin is
`3679155107/47000000000>0`.

For **every LEFT42 contraction**, use U=39/10, r_min=1, r_max=3/2,
b_max=1/2. The margin is `17940880361/3008000000000>0`.
The ray gates are:

| Gate at U | Initial splice | LEFT splice |
|---|---|---|
| Qmax | -585203/35000 | -269259/14000 |
| Qmax' | -2761/100 | -1329/50 |
| Qmax'' | -393/20 | -189/10 |
| Lmax | -10604493/1400000 | -5347197/700000 |
| Lmax' | -254667/40000 | -123591/20000 |
| Lmax'' | -2057/1000 | -2057/1000 |

The archived LEFT source has 64 support invocations: one common bridge at
radius121/40 and 63 later ordered refinements, all with radii between2.5 and
3.025. Their r parameters range from `116242091/100000000` to
`71458741/50000000`, and their b parameters are at most
`46459359/100000000`. Thus all fit the single LEFT splice above. The new
checker binds each later moment pair to the immediately preceding resource
row and the first pair to maxima of the preceding coarse rows.

**The lower bounds on r are bounds on certificate parameters, not lower
bounds on the actual moment rho.** In particular, the initial law is not
assumed to satisfy rho>=1.84. The actual relation used is rho<=r.

## 5. Exact conclusion, execution and limits

For an attained positive closed maximizing pair with n>=42, C_n>=C_E and
`n(C_(n-1)-C_n)_+=0`, the original initial support conclusion |X|<3.84 follows
from its old finite sign predicates and the retained analytic inputs. At each
subsequent LEFT support step, if its preceding same-law resource bounds hold,
the **same recorded contracted radius** follows for that actual n. No new
support radius is claimed, and no positive noise or inward defect is set to zero.

Run `python3 -I -B mathematics/simplification/2026-10-27/check_support_lift.py`.
It checks the two exact splices, both polynomial identities for all65 inputs,
source identities, strict ray gates and input ancestry. Ten rejection controls
cover changed loss, an invalid splice, a false ray cap, omitted/duplicated/
reordered cells, a missing support edge, changed moments and duplicate JSON keys.
Saved evidence is in `runs/zero-loss-support-20261027/algebra01/`.

This is not a fresh acceptance of any old support polynomial, Fourier bound,
resource table, confinement certificate or local comparison. Their mathematical
and numerical premises remain explicit. The benefit is a proved uniform
**reuse implication**: it removes the finite-index support obstruction without
generating replacement support certificates. A separate all-index LOCAL42
composition must still check every other index-sensitive proof edge and must
not relabel the old finite wrapper's acceptance as an all-index PASS.
