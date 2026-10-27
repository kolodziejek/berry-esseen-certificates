# Support without the signed fifth-order envelope or a positivity mesh

**New result:** all65 support invocations in the zero-loss LOCAL42 route can
be handled by three elementary cases: two fixed boundary checks and one
monotone polynomial on a continuous interval of radii. No Bernstein transform,
radial mesh, favorable upper-index term or signed fifth-order Gaussian tangent
is needed in this alternative proof. Actual moment acquisition and contact
remain premises. The earlier14-interval certificate is preserved.

| Result | Mathematical status | Execution status |
|---|---|---|
| Fourth-order heat remainder and two all-threshold Gaussian envelopes | Derived below, uniformly for every raw H | Algebra/source review; no finite-law numerical approximation |
| Continuous later-radius family plus two fixed support radii | Proved from exact endpoint and monotonicity inequalities | Fresh exact PASS; three cases, eighteen ray signs, eight rejection controls |
| All65 original moment/radius invocations fit these cases | Exact source/input identification | Fresh complete source binding; actual acquired resources not replayed |
| Full LOCAL42 or global theorem | Conditional on all remaining analytic/numerical premises and genuine base | Not accepted by this checker |

Worktree: `simplify/second-reduction-20261027`, starting at
`42433b448d9389359e642a3384a949ffdd87b903`. Reference baseline remains
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee` in the user's fork.

## Analytic inputs and the new lower-order derivation

Retain an attained positive closed maximizing pair `(P,H)` at actual integer
`n>=42`, standardized law, `C=C_n>=C_E`, finite `rho=E|X|^3`,
`beta=E[X|X|]`, and zero global predecessor decrement. The same-law contact
inequality from `paper/analytic-supplement.txt:340–404,582–615` is

    0 <= H_n(H,t) + C[-|t|^3+(3/2)rho t^2+3 beta t+rho e_n]

on the complete closed support. The same-owner predecessor score is bounded
by the global predecessor, so its discarded signed loss is nonpositive.
Here `e_n=n(sqrt(n/(n-1))-1)-1/2 < .384/n`, and

    H_n/n^(3/2) = F_v(H-t)-F_(v+1)(H)
                  +t F_(v+1)'(H)-(t^2-1)F_(v+1)''(H)/2,
    F_v(x)=Phi(x/sqrt(v)), v=n-1, s=sqrt(n/v).

The exact scale proof is the decreasing cubic in the earlier support note;
at `1/42` its positive margin is `118707/42875000`.

This proof expands the spatial term only through order four. Expand `F_(v+1)`
through second order in variance, `F_(v+1)'` through first order in variance,
and `F_(v+1)''` through first order in variance. Using the heat identity
`partial_v F_v=F_v''/2`, the cancellations leave

    H_n(H,±u)/s^3 = ±A(1-z^2)phi(z)+B phi'''(z)+R,
    A=(u^3-3u)/6, B=(u^4-6u^2+3)/(24sqrt(v)), z=H/sqrt(v).

For `u>=5/2`, absolute remainders satisfy

    |R| <= E_v(u)
          = (u^5/100+3u/20)/v + 51(3u^2-2)/(960 v^(3/2)).        (1)

To verify every coefficient: the spatial remainder contributes
`u^5 ||phi^(4)||/(120v)`; the variance remainder in `tF_(v+1)'`
contributes `u ||phi^(4)||/(8v)`; the other two variance remainders
contribute `[1/48+(u^2-1)/16] ||phi^(5)||/v^(3/2)`.
Gaussian Fourier inversion gives `||phi^(4)||<=3phi(0)<6/5` and
`||phi^(5)||<=8/pi<51/20`. These are exactly (1).
There is **no** seventh derivative of F or sixth derivative of phi, and
no additional `u/(8v^2)` term is needed. All suprema are uniform in H.
The usual rational Machin lower bound `pi>281476/89625>160/51` licenses
these constants and `phi(0)<2/5`.

For `u>=5/2`, A and B are positive. The simple envelope is

    H_n(H,±u) <= s^3 { phi(0)(A+2B) + E_v(u) }.                 (2)

Indeed `||(1-z^2)phi(z)||=phi(0)` and `||phi'''||<2phi(0)`;
this treats both signs without a sign reflection of the law.

Only the initial radius needs the sharper elementary envelope

    H_n(H,±u) <= s^3 { phi(0)[A+9B^2/(4A)] + E_v(u) },          (3)

under `B<=A/4`. For positive t and `|z|<=1`, bound the two retained
terms by `phi(0)[A-Az^2+3B|z|]` and complete the square. Outside this
region the first term is nonpositive and the other is at most2B phi(0).
For negative t the first term is at most `2e^(-3/2)A phi(0)<A phi(0)/2`;
together with2B phi(0) this is at most A phi(0). Thus (3) holds for
every H and both signs. This uses no lower tangent for `phi^(4)`.

The old support source `support50_proof.tex`, SHA256
`621863bdb727e6372cb845f42558612c9ad05c8e989182e926c0b7b55a135628`,
describes a fourth-order alternative but keeps an extra nonnegative remainder.
The derivation above is supplied explicitly rather than relying on that remark.
The original signed fifth-order proof is at supplement455–640; it remains
valid as an alternative, not a premise of this new support component.

## Freeze only adverse terms at42

Use the elementary rational constants `S=81/80` and `ell=6`, so
`S^2>42/41` and `ell^2<41`. Define

    H4=u^4-6u^2+3,
    E(u)=u^5/4100+3u/820+17(3u^2-2)/78720,
    Q_(r,b)(u)=-u^3+(3/2)r u^2+3b u+(8/875)r,
    c=819/2000 < C_E.

For `rho<=r`, `|beta|<=b`, the contact coefficient is at most Q.
Check Q<0 before replacing its actual multiplier C by c. Bound (2) gives

    H_n(H,±u)+cQ(u) <= (2/5)S^3[A+H4/72]+S^3E(u)+cQ(u).     (4)

At the initial radius, clear the positive denominator A in (3):

    A[H_n(H,±u)+cQ(u)]
      <= (2/5)S^3[A^2+H4^2/(256*41)] + S^3E(u)A + cQ(u)A.  (5)

The square of B uses the exact floor41; its coupling can use ell=6.
For the initial `u=96/25<6`, `H4=6uA-3(u^2-1)<6uA<36A`, so
`B<=H4/144<A/4`. All constants are outward, and all terms whose scale
is replaced by its floor are nonnegative.

## Three support cases and complete rays

Let `L_(r,b)(u)=(2/5)(u^2/2+1/2+8/875)+c Q_(r,b)'(u)`.
The retained direct derivative bound gives
`|partial_t H_n| <= (2/5)(t^2/2+1/2+e_n)`. If
`Q,Q',Q'',L,L',L''<0` at U, then they keep the required signs for all
u>=U, since `Q'''=-6` and `L''=2/5-6c<0`. The contact envelope for
either t sign decreases strictly from any already negative boundary value.
This covers full closed rays, atoms and every raw H, without a mesh.

**Initial case.** Take `R=96/25`, `r=1841/1000`, `b=321/500`.
The two retained published moment bounds give

    rho < min(.3031*.646/(c-.3031), .3322*.429/(c-.3322))
        =7361/4000 < r.

The retained sign-moment inequality gives `|beta|<b`, since
`(1+b^2)^2-r^2(1-b^2)=93288849/50000000000>0`.
The negative of (5) at R is

    2214258283536204102723/10250000000000000000000 > 1/5.

All six ray gates are strictly negative at R. Hence support lies in(-R,R).

**Common LEFT bridge.** Take `R=121/40`, `r=143/100`, `b=93/200`.
These outwardly cover the archived common preceding resource maxima
`71458741/50000000` and `46459359/100000000`. The negative of (4)
at R is

    2533499510174559/214958080000000000 > 1/100.

All six ray gates are strictly negative at R. This proves the same common
radius after those resource bounds have been acquired.

**All63 later LEFT contractions.** Their exact source inputs satisfy

    5/2 <= R <=111/40,
    rho <= r_R=7R/20+1/3,     |beta| <= b_R=3R/8-3/5.           (6)

These are bounds on certificate parameters, not lower bounds on actual rho.
At the boundary u=R, substitute r_R,b_R into (4), and let p(R) be its negative.
Writing `w=R-5/2`, exact expansion gives `p(R)=sum_(j=0)^5 a_j w^j`, with

| j | a_j |
|---|---|
|0|123579925563/1343488000000|
|1|-467155860219/1679360000000|
|2|705959271/13434880000|
|3|8703567/167936000|
|4|-7499223/839680000|
|5|-531441/2099200000|

Set h=11/40. For0<=w<=h, the signs of these coefficients give

    p'(R) <= a1+2a2 h+3a3 h^2 = -797749885413/3358720000000 <0.

Consequently

    p(R) >= p(111/40)
         =4403736280322409/214958080000000000 >1/50.            (7)

This is an analytic monotonicity proof on the complete radius interval.
It uses neither Bernstein positivity nor sampled positivity.
For the rays, every pair r_R,b_R in (6) is below the common rectangle
`r*=131/100`, `b*=441/1000`. At u=5/2 its six ray gates are

    -16991/700000, -3801/500, -1107/100,
    -11615533/7000000, -706633/200000, -2057/1000.

They are strictly negative. Therefore the derivative bound is negative for
all u>=R, for each **fixed** parameter pair r_R,b_R; (7) supplies its
negative starting value. The common caps majorize derivatives and Q signs,
not an unproved new boundary value. This excludes both complete rays for
all63 support invocations.

Do not continue the affine parameters r_u,b_u indefinitely: the radius R
is fixed when following a ray. That overly coarse affine continuation to
u=3.9 makes the contact bound fail. The new proof explicitly freezes the
moments after using the parameter family to prove the boundary sign.

## Exact source binding, evidence and removals

The fixed checker reads the unchanged archive
`verification/finite-tail/sources/backend.zip`, SHA256
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`.
It reads proof member `finite61/blobs/419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393`
and imports no archived code. The original caller is the LEFT acceptor blob
`a565247f6587f3bb07dd67ef2100d08f70aebbe7543937f1ab98f8d09cf31eb6`,
lines37–42,72–80; the initial caller is blob
`343046eaf0a3e6b2e140644cee19b7764d76b4171b844eaac27fb1a288b12d2e`, line7.
All55 ordered fine cells, the common coarse maxima, each preceding moment
pair, decreasing radius and all63 later inequalities (6) are checked.
These bindings do not establish the truth of acquired resources.

Run from repository root:

    python3 -I -B mathematics/reduction2/2026-10-27/check_elementary_support.py

Fresh receipt/stdout/stderr: `runs/reduction2-20261027/elementary-support01/`.
Return0, about0.26seconds. Eight controls reject missing/reordered source
cells or edges, changed moments, duplicate JSON keys, a false ray cap and
unlicensed radius changes. Two exact negative diagnostics show why neither
using (2) for the initial radius nor blindly extending the affine moment
family to3.9 is valid. These are failures of coarser bounds, not iid
counterexamples. Earlier bounded14-case fourth-order discovery is retained
under `heat-discovery01/`; it is not acceptance evidence.

For this alternative support proof, the following premises/computations are
unnecessary: signed fifth-order identity, fourth-derivative lower tangent,
its W and outer-domination gates, finite upper endpoint, old radial Bernstein
cells and the new672-coefficient grouped certificate. Each is replaced by
(1)–(7), complete direct rays and static input binding. The Gaussian Fourier
norm bounds through derivative5, contact, scalar scale bound, initial moment
inequalities, actual resources and all later local proof components remain.
No original theorem or certificate is changed or deleted. The171-task plan
from the first reduction is not reduced merely by counting these internal
support subchecks: they are parts of retained acquisition obligations.
