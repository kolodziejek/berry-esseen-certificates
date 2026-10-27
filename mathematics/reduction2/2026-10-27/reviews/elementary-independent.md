# Independent review of the elementary zero-loss support component

Reviewed commit: `abd8927`, branch `simplify/second-reduction-20261027`.
Review branch: `simplify/review-elementary-20261027`. Original reference
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee` is unchanged in the user's fork.

**Finding: no blocking mathematical or arithmetic defect found at the stated
conditional scope.** The fourth-order expansion is sufficient, its remainder
has the stated coefficients, and the two fixed checks plus a continuous
radius-family argument cover the 65 identified support invocations. The
proof treats every real raw threshold and both support signs. It needs no
equality `C=C_E`, fifth-order signed Gaussian tangent, radial mesh, or old
support-positivity certificate. It still needs the retained attained contact
witness and genuine same-law moment/resource premises.

| Item | Mathematical status | Execution status |
|---|---|---|
| Fourth-order heat expansion, uniform remainder and both envelopes | Independently derived below | Exact cancellation sanity checks; no floating Gaussian diagnostic |
| Two fixed boundary inequalities and continuous radius family | Independently derived and checked | Fresh independent exact PASS; same fractions as submitted proof |
| Whole rays with frozen moment caps | Proved from direct derivative inequality and strict endpoint signs | All 390 individual signs for the 65 tuples freshly checked |
| Initial call, common LEFT bridge, all 63 later calls | Exact literal source/route/resource binding | Fresh source-only PASS; no archived code imported |
| Truth of acquired moments, attainment/contact, LOCAL42, finite base, global result | Retained conditional premises; not proved in this review | Not replayed or accepted |

Recommendation: integrate this as a reviewed conditional support replacement.
This recommendation does not authorize removal of original certificates or
claim a complete LOCAL42/global proof. No old file was edited or executed.

## Exact reviewed statement

Let actual `n>=42`, and let `(P,H)` be the retained unrestricted attained
positive closed maximizing pair, standardized to mean zero and variance one,
with `C=C_n>=C_E`, finite `rho=E|X|^3`, and `beta=E[X|X|]`. Assume
zero positive global predecessor decrement, so the same-law predecessor
loss in contact is nonpositive. The same-law contact inequality implies
strict support inside `(-R,R)` in each of these cases:

1. `R=96/25`, with the retained initial moment inequalities; their outward
   consequences are `rho<1841/1000`, `|beta|<321/500`.
2. `R=121/40`, with `rho<=143/100`, `|beta|<=93/200`.
3. A fixed `R` in `[5/2,111/40]`, with
   `rho<=7R/20+1/3`, `|beta|<=3R/8-3/5`.

The source identification shows that the one initial, one common, and 63
later invocations satisfy the corresponding parameter specifications, if
their preceding actual resources have been proved. In case 3, `R` is fixed
when following either ray; the caps do not become functions of `|t|`.

Reviewed locations: `elementary-support.md:24–88` for the analytic expansion
and envelopes, `90–113` for floor constants, `115–193` for the three cases
and rays, and `195–231` for binding/removal claims. The submitted checker
uses `rays` at lines63–71, `family_gate` at80–93, `bind` at95–119 and
its main checks at121–169. Source contact and direct derivative estimates
are at `paper/analytic-supplement.txt:340–404`; the initial moment and
same-law resource interfaces are at582–615.

## Independent heat derivation

Write `v=n-1`, `s=sqrt(n/v)`, `F_w(x)=Phi(x/sqrt(w))`, and let unlabelled
derivatives below be spatial derivatives at `(v,H)`. Direct substitution into
the Gaussian identity gives

\[
 \mathcal H_n/n^{3/2}
 =F_v(H-t)-F_{v+1}(H)+tF'_{v+1}(H)
                  -(t^2-1)F''_{v+1}(H)/2.
\]

The heat identity is `partial_w F_w=F_w''/2`. Applying ordinary Taylor's
theorem in space to order 4 and in variance to orders 2,1,1 gives

\[
\begin{aligned}
 F_v(H-t)&=F-tF'+\tfrac{t^2}{2}F''-\tfrac{t^3}{6}F'''
                       +\tfrac{t^4}{24}F''''+R_s,\\
 F_{v+1}&=F+\tfrac12F''+\tfrac18F''''+R_0,\\
 F'_{v+1}&=F'+\tfrac12F'''+R_1,\\
 F''_{v+1}&=F''+\tfrac12F''''+R_2.
\end{aligned}
\]

The first three derivative coefficients cancel. The remaining ones are
`-(t^3-3t)/6` for `F'''` and `(t^4-6t^2+3)/24` for `F''''`.
Since `F'''=v^(-3/2)phi''(H/sqrt(v))`,
`F''''=v^(-2)phi'''(H/sqrt(v))`, and `n^(3/2)/s^3=v^(3/2)`, this is exactly

\[
 \mathcal H_n(H,\pm u)/s^3
 =\pm A(1-z^2)\phi(z)+B\phi'''(z)+R,
 \quad A=(u^3-3u)/6,\quad B=(u^4-6u^2+3)/(24\sqrt v).
\]

For `u>=5/2`, the four absolute remainder bounds, after multiplication by
`v^(3/2)`, are respectively

\[
 {u^5\|\phi^{(4)}\|\over120v},\qquad
 {\|\phi^{(5)}\|\over48v^{3/2}},\qquad
 {u\|\phi^{(4)}\|\over8v},\qquad
 {(u^2-1)\|\phi^{(5)}\|\over16v^{3/2}}.
\]

The variance intermediate points are all at least `v`, so replacing their
variance factors by `v` is outward. The positivity of `u^2-1` is used only
on the stated radial domain. Fourier inversion of the Gaussian density gives

\[
 \|\phi^{(4)}\|\le{1\over2\pi}\int x^4e^{-x^2/2}\,dx
 =3\phi(0)<6/5,\qquad
 \|\phi^{(5)}\|\le{1\over2\pi}\int |x|^5e^{-x^2/2}\,dx
 =8/\pi<51/20.
\]

Combining the bounds produces precisely

\[
 |R|\le {u^5/100+3u/20\over v}
                +{51(3u^2-2)\over960v^{3/2}}.
\]

This argument uses neither a seventh derivative of `F` nor a sixth
derivative of `phi`; the absent old `u/(8v^2)` term is not needed. The norms
are uniform on the full real threshold line, so there is no hidden fixed-H
limit, asymptotic remainder, or threshold cutoff.

## Independent envelope and floor checks

The elementary norm identities/bounds are sufficient:

* `||(1-z^2)phi(z)||=phi(0)`. On `z^2>=1` its absolute maximum is
  `2e^(-3/2)phi(0)<phi(0)`; on `z^2<=1` the claim is immediate.
* Fourier inversion also gives `||phi'''||<=2/pi<2phi(0)`, since `pi>2`.
  Thus the simple envelope `phi(0)(A+2B)` treats both signs when `A,B>=0`.
  Both are positive for `u>=5/2`.
* For the positive sign and `|z|<=1`, the retained expression is at most
  `phi(0)[A-Az^2+3B|z|]`. Its quadratic maximum is
  `phi(0)[A+9B^2/(4A)]`. The bracket before replacing the density is
  nonnegative, so this replacement has the correct direction.
* Outside that region the positive branch is at most `2Bphi(0)`.
  For the negative branch the first summand is at most
  `2e^(-3/2)Aphi(0)<Aphi(0)/2`. The condition `B<=A/4` makes the
  negative branch at most `Aphi(0)`. For the exponential comparison,
  `e^(3/2)>1+3/2+9/8+27/48=67/16>4` suffices.

No signed lower tangent appears in this derivation. Only the initial radius
uses the sharper coupled envelope. At `R=96/25`,
`0<H4/(24sqrt(v))<H4/144<A/4` follows from `sqrt(v)>6` and
`H4=6RA-3(R^2-1)<6RA<36A`.

The floor choices satisfy `(81/80)^2>42/41`, `6^2<41`, and
`e_n<48/(125n)<=8/875`. Independently squaring the scale comparison gives
the source's decreasing cubic with endpoint margin `118707/42875000>0`.
All terms frozen in the heat bound are nonnegative. Thus

\[
 E(u)={u^5\over4100}+{3u\over820}+{17(3u^2-2)\over78720}
\]

is an outward bound. The sharper boundary calculation uses the exact
`B^2<=H4^2/(24^2*41)`, so `9B^2/(4A)<=H4^2/(256*41*A)`.
That distinction from the cruder `sqrt(v)>6` coupling gate is correct.

The independent checker derives rational lower/upper pi bounds from the
Machin arctangent identity, rather than taking a decimal pi value. It also
checks `C_E>819/2000` from the explicit formula in `paper/main.tex:51`,
using `(79/25)^2<10` and its rational pi upper bound. Hence the proof needs
only `C>=C_E`, not equality with `C_E`.

## Radius family and full-ray logic

I independently evaluated the negative contact boundary expression from
the scalar formulas and reconstructed its degree 5 polynomial around `5/2`
by solving a rational Vandermonde system. This is separate from the
constructor's polynomial multiplication and shift code. The six resulting
coefficients exactly match the submitted table. The degree bound follows
from the explicit formulas; four additional rational evaluations agree.

For `w=R-5/2` in `[0,11/40]`, the coefficient signs imply

\[
 p'(R)\le a_1+2a_2(11/40)+3a_3(11/40)^2
       =-{797749885413\over3358720000000}<0.
\]

The negative contributions of the degree 4/5 terms may be discarded in this
upper bound; both positive contributions increase with `w`. Consequently

\[
 p(R)\ge p(111/40)
 ={4403736280322409\over214958080000000000}>1/50.
\]

The two independent fixed calculations give

\[
 -A(R_0)\,[\text{sharp contact upper bound at }R_0]
 ={2214258283536204102723\over10250000000000000000000}>1/5,
\]

\[
 -[\text{simple contact upper bound at }121/40]
 ={2533499510174559\over214958080000000000}>1/100.
\]

For a fixed case, let
`Q=-u^3+(3/2)ru^2+3bu+(8/875)r` and
`L=(2/5)(u^2/2+1/2+8/875)+cQ'`. The signs of
`Q,Q',Q'',L,L',L''` at the stated starting point imply the needed signs
on the entire ray: `Q'''=-6`, `L''=2/5-6c<0`. The direct derivative
bound controls `d/du H_n(H,+u)` and `d/du H_n(H,-u)` by the same
absolute bound. It applies at every H and needs no moment above order 3.

For the radius family, the fixed rectangle
`r<=131/100,b<=441/1000` gives all six negative signs already at `u=5/2`.
For `u>=5/2`, each relevant derivative expression is nondecreasing in `r,b`
(or independent of them), so these signs apply to each **fixed** pair
`r_R,b_R` and all `u>=R`. The family inequality supplies the boundary
sign at that same pair. The rectangle is not substituted into the boundary
calculation, and the affine family is not continued along the ray.

Since `Q<0`, actual contact's cubic coefficient is negative before its
multiplier `C` is replaced by the lower bound `c`. The discarded predecessor
term is nonpositive. Every resulting envelope is strictly negative at the
boundary and strictly decreases along each ray. This excludes boundary
atoms and all exterior support/accumulation points. The conclusion is open
support containment, not merely absence of mass beyond a sampled grid.

## All 65 source bindings

The independent script hashes the original source-only archive and four
members; it imports none of their code. The logical prefix is
`work/toward40_20261007/audit43/capsule/work/below49_20261006/`.

| Member | SHA256 and binding |
|---|---|
| `acquisition/check_local42_support.py` | `343046eaf0a3e6b2e140644cee19b7764d76b4171b844eaac27fb1a288b12d2e`; AST verifies the literal line 7 call `(42,48,0,96/25,19/100)` |
| `package_audit/left42_exact/accept_acquisition.py` | `a565247f6587f3bb07dd67ef2100d08f70aebbe7543937f1ab98f8d09cf31eb6`; AST verifies helper line 41 `(42,48,0,R,19/100)`; source lines 37–42 install the supplied moment pair; 72–80 bind common/later resources |
| `package_audit/left42_exact/acquisition42_proof.json` | `419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393`; checks original scope, 15 ordered coarse cells, 55 ordered fine cells, predecessor resource pairs, all 63 later contractions |
| `package_audit/left42_exact/fixed_route.json` | `df1631620cf1135a5bb6fb9cd28f6c514f6a0451f7c1699ad55054fa1b23dcd0`; independently joins every complete radius path to its corresponding fine trace |

The first bridge's moment parameters are the maxima of the nonexcluded
coarse resources. They fit the common outward pair. Every subsequent
support call uses the immediately preceding resource in its own trace,
and all 63 calls fit the complete affine family. Every original call's
historical floor 42, last 48, barrier 0, loss cap `.19`, and lower score `.4095`
is identified. The new lemma has a different, explicitly stated zero-loss
all-index scope; it does not relabel those old finite predicates as proved.

The checker also directly verifies all 65 endpoint inequalities and all
390 ray signs at their individual moment caps. This is redundant with the
family proof, but it independently checks the source-to-formula join.
It does not validate the truth of any resource record or its acquisition.

## Fresh evidence, adversarial controls and limitations

Evidence is in `runs/reduction2-20261027/review-elementary01/`:

* `constructor.receipt.json`, stdout/stderr: submitted checker fresh PASS,
  exit 0, measured 0.160585542 seconds; all eight submitted controls rejected.
* `independent.receipt.json`, stdout/stderr: new independent checker fresh
  PASS, exit 0, measured 0.081942042 seconds; both stderr files empty.
* The independent check rejects a changed preceding moment, a missing route
  edge, reordered fine cells and duplicate JSON keys. It pins the initial
  caller, LEFT caller and complete fixed route in addition to the proof data.
* The initial simple envelope fails exactly, and continuing affine moments
  to radius 3.9 also fails exactly. These are obstructions to those coarser
  arguments, not counterexamples to the probabilistic theorem.

Reproduce the independent check with

```
python3 -I -B mathematics/reduction2/2026-10-27/reviews/check_elementary_independent.py
```

The submitted and independent programs share the proved scalar target, but
do not share evaluated code. Polynomial reconstruction, literal caller/route
binding and per-call arithmetic are independently implemented. The analytic
remainder, Gaussian norms, continuity and whole-ray proof above supply the
infinite-domain argument; finite checks and agent agreement do not do so.

No Bernoulli or multi-atom diagnostic was substituted for the analytic
uniform bounds. The heat identity is law-independent, and the remaining
law dependence is confined to the explicitly retained contact and moment
premises. No archived/native checker, acquired-resource replay, finite-base
check, full LOW run or certificate campaign was performed. Actual-law
attainment, the initial external moment inequalities, subsequent resource
acquisition and all other LOCAL42 components remain outside this review.
