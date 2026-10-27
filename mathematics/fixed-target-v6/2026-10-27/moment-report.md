# Joint moment feedback: one initial gate closed, four remain

The exact six-update calculation improves the worst conserved defect ceiling
from the v5 value `4.9901197720` to `4.7353850385`. It closes the sufficient
`D<4` gate in one additional rho cell (index 19). Four cells still fail this
sufficient gate. No complete initial acquisition is claimed.

Work is on the separate fork branch `research/v6-moment-coupling-20261027`,
starting at `43f9f82`. All changes are additions; existing proof objects,
certificates, manifests and production code are unchanged.

| Result | Mathematical status | Execution status |
|---|---|---|
| Same-law moment circle and gap bound | Existing manuscript theorem, independently rederived here | Exact checks on six finite standardized laws; not inferred from samples |
| Inverse gamma bound from a previously established defect ceiling | Locally derived; full proof in `moment.tex`, Lemma `v6moment:inverse` | Exact branch, endpoint and rounding controls pass |
| Six scalar updates on all 24 closed rho cells | Conditional on the v5 fixed-target contact, support and universal Fourier enclosure | Fresh success, `moment01/moment-receipt.json`, exit 0 |
| Complete `D<4` initial acquisition | Not established by this component | 20 cells pass, 4 do not |
| Full small-defect acquisition, final probability panels, local exclusions and global theorem | Separate unresolved dependencies | Not run |

## Statement, derivation and retained hypotheses

All moments refer to one centered variance-one marginal with finite third
absolute moment. Put `rho=E|X|^3`, `gamma=EX^3`, `beta=EX|X|`, and
`m=EX_+=EX_->0`. Signwise Cauchy gives

\[
 m(\rho\pm\gamma)/2\ge((1\pm\beta)/2)^2,
 \qquad m^2\le(1-\beta^2)/4.
\]

Multiplying the first pair and using the second proves
`gamma^2+4m^2<=rho^2`. The proof explicitly allows a zero atom. This circle
already appears at `manuscript/arxiv-v1/sections/05-geometry-counts.tex:89–133`,
label `ms:physical-defect`; it is **not** presented here as a new theorem.
The signwise common-first-moment formulas are also at
`appendices/fourier-analysis.tex:1748–1763`.

The conserved defect is exactly
`D=(3+sqrt(10))*rho-gamma-3J`. The actual gap bound `J<=rho+2m` gives

\[
 D\ge\sqrt{10}\rho-\gamma-6m
 \ge\sqrt{10}\rho-\gamma-3\sqrt{\rho^2-\gamma^2}.
\]

The first relation is an inequality, not a definition of `D`. For a cell
`rho∈[l,u]` with a previously licensed `D<=d`, let
`a_l=sigma_l-d/l`, where `sigma_l=3.162277660<sqrt(10)`. Then

\[
 y+3\sqrt{1-y^2}\ge a_l,\qquad y=\gamma/\rho\in[-1,1].
\]

If `a_l<=-1`, retain `y>=-1`. Otherwise inversion on the increasing branch
of this concave function gives

\[
 y\ge Y(a_l)=\frac{a_l-3\sqrt{10-a_l^2}}{10}.
\]

The proof checks the branch and the sign before squaring. The square root is
rounded upward, hence this expression downward. If `y_l` is the resulting
lower bound, multiply by `l` when `y_l>=0`, and by `u` when `y_l<0`.
Using the wrong rho endpoint for negative `y_l` would be invalid.
Intersect this bound with `-g` and `sigma_l*l-3-d`. Also intersect the old
bound for `rho-gamma` with `u-gamma_lower`.

These are the only new moment restrictions in this component. Support remains
`[-96/25,96/25]`, `N=42`, and `rho` ranges over the same 24 cells
`[1+3361i/96000,1+3361(i+1)/96000]`, `0<=i<24`. There are no gamma
subdivisions, changes to K1, or new fourth/fifth-moment coefficients. The
candidate support radii of v5 are not used. The quarter-constant improvement,
stronger K1 bound, and root's new exponential phase bound are separate tasks
and are not silently included in these numbers.

## Raw/resource order and coverage

The initial first-cover computation is freshly recomputed by the pinned v5
constructor. A historical JSON output is never accepted as a substitute.
For each cell, each update uses its **previous** defect ceiling to obtain the
new gamma and charge bounds. Its density floor uses its **previous raw** `T`:

\[
 \phi_-=(997/2500)\{1-T/(42c_-l)\}.
\]

The curvature is

\[
 q(t)=\max\{tl-g/5,\;tl+\tfrac12\min(\phi_-g_l,(2/5)g_l)\}.
\]

The sign of the actual gamma is retained. This curvature is affine in the
formal coefficient `t`, since both alternatives have slope `l`; the remaining
raw polynomial is affine in `t` before square completion. Checking both
endpoints of the freshly enclosed `CE` interval is therefore valid.
The old and new raw upper bounds are intersected first. Only then is the
conserved phase price `(c_-l-T/42)/2` recomputed from the **raw** bound.
The resource ceiling `U` is computed separately and supplies
`nD<=6U/(997/2500)` and `D<=6U/(42*(997/2500))`. In particular `U` never
replaces `T` in the Gaussian license.

All retained raw, resource and defect ceilings are rounded upward to `10^-10`.
Gamma lower bounds are rounded downward. No cell is dropped: an inconsistent
moment interval causes this bounded calculation to reject. The first constructor
checks the closed contiguous 24-cell cover. The new code performs six updates
on every returned cell, so there are 144 update evaluations after the 24-cell
initial computation. No dense signed cover or native acceptor is invoked.

## Exact recorded outcome

| Update | Maximum raw T | Maximum resource U | Maximum D | Cells D<4 | Cells D<2 |
|---|---:|---:|---:|---:|---:|
| 1 | 16.7551374425 | 13.7271322652 | 4.9172991350 | 20 | 9 |
| 2 | 16.0851866084 | 13.2989541709 | 4.7639182444 | 20 | 9 |
| 3 | 15.9796790670 | 13.2319683403 | 4.7399227470 | 20 | 9 |
| 4 | 15.9628357233 | 13.2212837019 | 4.7360953224 | 20 | 10 |
| 5 | 15.9601408759 | 13.2195744379 | 4.7354830341 | 20 | 10 |
| 6 | 15.9597095614 | 13.2193008732 | 4.7353850385 | 20 | 10 |

The final defect bounds in the five formerly unresolved cells are:

| Cell | D upper bound |
|---|---:|
| 19 | 3.8395079253 |
| 20 | 4.0470078085 |
| 21 | 4.2699520174 |
| 22 | 4.5001995979 |
| 23 | 4.7353850385 |

In the last cell the final gamma lower bound is `-1.6210532343`, improved
from the old `-1.84025`. The exact raw polynomial coefficients for both formal
`c` endpoints are recorded under `endpoints` in every step of
`moment01/moment.stdout.json`, with keys `constant`, `linear`, `quadratic`.
They permit a separately justified stronger phase maximizer to use the same
polynomial without guessing how a resource ceiling was obtained.

## What this could shorten, and what it does not remove

The initial unsigned relaxation previously allowed very negative gamma and
large `m` simultaneously, although the same law cannot have those moments.
One already available analytic inequality now removes that inconsistency
before a dense parameter cover. Its implementation is a square-root enclosure
and a few scalar coefficient updates. This is a concrete shortening of that
coarse acquisition argument and closes one numerical gate without subdividing
its moment domain.

It is not yet a replacement for `INITIAL42_R384`: that acceptor also requires
stronger final resources and complete probability-panel outputs. Consequently
this isolated component makes **no existing certificate task unnecessary**.
A future independently proved and accepted combined acquisition could bypass
some old dense stages in a new proof plan; every downstream hypothesis and
probability-panel obligation would still need matching. Nothing is deleted,
weakened, or relabelled as a full PASS here.

## Source binding, adversarial checks and reproduction

`moment_check.py:9–14` pins the v5 constructor to SHA256
`6827a67e64cfea5b89d823ffd34821fa942b3c3add702ee9721c89d65f443aa5` before import.
That constructor validates the literal input contract and all four decoded
source pins before importing its two pure scalar modules. Those modules and
its wrapper were read before execution in v5; the wrapper was read again here.
The new inverse is at `moment_check.py:20–32`; update ordering is at `33–59`;
finite-law checks and controls are at `60–90`; the complete six-update loop is
at `92–115`. Input and output hashes are in the receipt, including all inherited
source files. No external services or upstream repository were modified.

The finite-law checks include symmetric Bernoulli, both reflections of a skew
Bernoulli law, a three-point law with a zero atom, a four-point law, and a tiny
far-atom law. The latter is outside the acquisition moment range and tests only
the universal analytic inequality. For each, the code checks the same-law sign
Cauchy inequalities, circle slack, exact gap sum, and the distinction between
conserved defect and its compulsory lower bound. These examples are controls;
the continuum proof is the argument above.

Four invalid-input controls reject negative defect, reversed rho interval,
out-of-domain inverse target, and a negative square-root argument. Two exact
adversarial inequalities expose a wrong inverse branch and an impossible moment
tuple; they are not advertised as a generic proof-object acceptance API.
The separate `moment_inverse_check.py` checks ten rational points on the unit
circle, including endpoints and both sides of the maximum. At the exact
increasing-branch boundary `y=-5/13`, `a=31/13`, reversing the root rounding
produces a purported lower bound greater than this valid y. The correct outward
rounding preserves it. This is a semantic rounding control, not just a hash test.

Commands actually run:

```sh
python3 mathematics/fixed-target-v6/2026-10-27/moment_run.py moment01
python3 mathematics/fixed-target-v6/2026-10-27/moment_inverse_check.py
```

The second was run under a recording process, with its receipt and exact
stdout/stderr in `moment-inverse01`. Python was 3.9.6 with optimization 0.
Both returned zero. The full analytic fragment is `moment.tex`; its standalone
wrapper is `moment-main.tex`. The final compile and page-inspection record is
in `moment-build02` and `moment-visual-review.md`. Successful compilation and
finite arithmetic do not independently establish the retained analytic inputs.
