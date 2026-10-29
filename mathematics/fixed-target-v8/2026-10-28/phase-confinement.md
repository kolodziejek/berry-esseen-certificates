# Complete conditional half-amplitude confinement on one panel

Date: 2026-10-28. Work branch: `research/v8-phase-confinement-20261028`.
Base: `cf5f945167dfdc24b80da7ddebf97ba43c8f6362`.
Immutable source baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
All changes are additions in this fork. No old certificate, target, native
runner, manifest, or theorem statement is modified.

## Statement and status

For **every actual `n >= 42`** and fixed-target maximizing witness with
nonnegative excess over `c=CE`, assume fixed-target contact, the sharp
predecessor `C_(n-1)<=CE`, the accepted v7 signed entry cover with its
analytic Fourier/ordered acquisition hypotheses, and the retained signed
confinement identities. On the entire probability panel

\[
                 0.41\le p\le0.42,
\]

the new composition proves **`|U|<1/2`** and retains **`d<.069<1/4`**.
Here `X=ell(B+U-p)`, `E(U|B)=0`, `lambda=n E U^2`, and `d` is the
normalized inward displacement of the actual central gap. This is a
complete conditional confinement result for this panel, **not** a count
comparison, LOCAL42 acceptance, finite base, or global sharp theorem.

| Component | Mathematical status | Execution status |
|---|---|---|
| Same-cell signed phase-resource join | Derived all-index implication, conditional on the named raw Fourier/entry inputs | Fresh final-stage replay: 2048 boxes, 682 active; all 1364 signed endpoint reconstructions pass |
| Original equal 128-box confinement without the new heat lemma | Incomplete sufficient test | 87 boxes excluded, 74/82 ray gates pass, 8 fail |
| One predeclared redistributed 128-box test | Incomplete sufficient test | 55 boxes excluded, 145/146 ray gates pass, 1 fails |
| Direct contact support for all `0<=lambda<=.075` | Derived same-law consequence of prior `.6` strip, contact and sharp predecessor; every raw `H` | Both strict boundaries and all 12 continuation signs pass; 5 controls reject |
| Original equal cover plus direct low-noise lemma | **Complete conditional panel theorem** | **Fresh PASS:** 16 boxes use direct heat, 84 are excluded, 28 pass both rays; minimum of the 56 remaining strict margins is `0.008920119173442213` |
| Final count inequality and other probability panels | Not established by this task | Not run |

The proof is `phase-confinement-proof/main.tex`. Final acceptance is
`phase-confinement.py --partition equal --compose-heat`, with the run
directory supplied explicitly. The standalone direct lemma is
`phase-confinement-heat.py`. Exact rational outputs, rather than the
decimal summaries above, determine every gate.

## What is new in the proof

The initial `.6` strip, `d<.069`, moment and scale bounds come from
`confinement-proof/confinement.tex`, committed at the parent base. They are
acquired before either new refinement is used. In particular this task
does not assume the `.5` strip to derive a moment bound needed to prove it.

Each active v7 moment cell has a raw polynomial

\[
 R_c\le K_F+cA+H(cK_1+\phi W)+s|H|-q(c)H^2.
\]

Its independently valid raw ceiling `T<N*c_lower*rho_lower` supplies
`eta=(c_lower*rho_lower-T/N)/2>0`. Subtracting the phase price bounds the
**same-law joint resource**

\[
 U=(n+H^2)a+n\phi(0)D/6+n^{3/2}L_{\rm leak}.
\]

For positive and negative `H`, the linear coefficients are respectively
`max(c*K1+phi*W)+s` and `-min(c*K1+phi*W)+s`. The curvature is `q+eta`.
The script reconstructs those coefficients, the constants, density license
and phase price before using them. The two fixed-target endpoints bound
the full multiplier interval by convexity. Each concave quadratic is
maximized on its entire clipped closed phase interval, including the
vertex when present. Taking the maximum over **every incident active
moment cell** gives the whole-rectangle resource; it is not a favorable
choice of incompatible moment maxima.

Necessary noise filtering is independent of the desired confinement:

\[
 \theta=\frac{\lambda}{npq+\lambda},\qquad
 m^2=\frac{(pq)^2}{pq+\lambda/n}.
\]

Monotonicity gives a lower `m` bound at `n=42` and an upper at the
`n -> infinity` endpoint. Conservative beta bounds retain both orientations.
Only disjoint `p,m,beta` ranges or a phase ceiling below the rectangle
exclude a moment cell. Closed intersections and all seams remain included.

The direct low-noise proof uses the **already acquired** `|U|<.6` and
conditional centering in one marginal's exact signed cubic expansion.
The checked coefficient gate
`24^2*[.41*.59]^3 > [3*.59+.6]^2` yields

\[
 \rho\le\rho_B(.41)+24\lambda/n.
\]

For `lambda<=3/40`, this and the exact variance identities give
`theta<=.00732793996951577`, `ell>=2.0186650184`,
`rho<=1.0923997312753875`, and
`beta` between `.1514995896353617` and `.18600891077500292`.
The signed physical radii

\[
 u_-=1.836985166744,
 \qquad u_+=2.180158219872
\]

correspond exactly to the desired `Y` boundaries `-.5,1.5`, using the
outward scale and probability endpoints. Both exceed `sqrt(3)`. The
fourth-order heat estimate uses `abs(H4)`; it does not apply the old
positive-quartic statement below its domain. Its boundary upper values
are below `-.51645700` and `-.24695345`, with all 12 ray signs strictly
negative. Thus boundary atoms and whole exterior rays are excluded for
**every raw threshold**, independently of the phase partition. The inward
bound then gives both conditional amplitudes strictly below `.5`.
Zero noise is included directly by conditional centering. The shared
`lambda=.075` endpoint is covered by both adjoining closed arguments.

For a shorter human presentation, these exact bounds imply
`theta<.00733`, `ell>2.018`, `rho<1.093`, `beta in (.151,.187)`.
A separate reviewer independently derived the same marginal cubic bound
and checked simpler radii `1.836,2.179` under these rounded caps. That
independent derivation is supplementary; the present acceptance uses the
exact radii and recorded arithmetic above.
The independent low-noise proof/review is commit
`1172d87ad3a662a179035a2fc84074929dd87fc6` in the `small-noise-v8` branch.

## Source and hypothesis map

- `confinement.md` and `confinement-proof/confinement.tex` give the prior
  panel acquisition and its exact dependency map. No premise is removed
  from that theorem by the present composition.
- `mathematics/strategy-v4/2026-10-27/excess.tex:107–208` gives fixed-target
  closed-support contact and the favorable `-n*a` support term, retaining
  the sharp predecessor. The derivative's additive excess constant
  disappears; this does not supply deleted-score bounds.
- `mathematics/fixed-target-v6/2026-10-27/signed-two-pass-proof/signed-two-pass.tex:42–65`
  gives the Gaussian phase price from a **raw** ceiling. A resource upper
  bound is not used to license itself.
- Frozen `phase_core.py:138–165` records the old raw maximum followed by
  the new phase price and the signed export. The export is generated by
  reversible additions to pinned `signed_core.py`; the original arithmetic
  and its exclusions are recovered byte-for-byte by undoing those additions.
- `manuscript/arxiv-v1/appendices/uniform-bridge.tex:14–43` gives the
  conditional cubic bound at the actual strip. Lines 45–93 retain strict-gap
  concentration at **both** deleted indices `n-1,n-2>=40`.
- `manuscript/arxiv-v1/appendices/fourier-analysis.tex:3210–3255` gives
  atom-safe signed deletion. Lines 3257–3374 give the slopes, disjoint
  interval geometry and strict-gap alternative; lines 3376–3456 give the
  shared resource simplex, inverse-index sign gates and strict rays.
  This invocation uses the antichain concentration branch. It does not
  silently add or discard a second deleted-score premise.
- `manuscript/arxiv-v1/sections/04-support.tex:36–65,104–145` gives the
  heat expansion/remainder and full-ray derivative estimate. The new
  `u>sqrt(3)` absolute-quartic extension is derived in the prior panel note
  and rechecked independently for the low-noise lemma.
- The new implementation's `source_bound_replay`, `validate_coefficients`,
  `rectangle_resource`, and `compose_heat` provide the executable edges.
  The final composition checks every complementary ray; it never relabels
  an unassisted failed gate as passed.

The independent phase-coefficient review is commit
`261776a9dc570f41ac16348ecc3b61009779ba11`, file
`mathematics/fixed-target-v8/2026-10-28/phase-review.md`. It independently
reconstructed the 1364 quadratics, 682 licenses/ranges, 2048-box census and
nine probe regions. This report's author constructed the confinement join
and does not describe self-replay as independent mathematical review.

## Evidence, bounded work, and remaining obligations

Frozen coefficient object SHA-256:
`b18599468c975032f4078e7a5f734fd6430b2b7da583789de58d9537d323f690`.
Frozen source manifest SHA-256:
`a3fcce0cf41c76fe02027e143e50adee521d297eb0938eebd89c21c46f12870e`.
The sources under `phase-confinement-sources/replay-root` are inspected
copies. The final invocation checks **exact file membership**, all byte
pins, no symlinks, and reversible export instrumentation before execution.
Its base and heat modules are compiled directly from verified source bytes.
The final child uses `-I -B -X pycache_prefix=<fresh empty directory>`;
the prefix must remain empty. An explicit `runpy` bootstrap inserts only
the pinned producer directory, restores its script arguments, and runs that
file. These precautions address external Python search paths, existing
bytecode and extra project-module shadowing; source hashes or `-B` alone
would not address those issues.
The Python runtime and standard library remain part of the trusted stack.

The final `phase-confinement06` invocation freshly recomputes all final-stage
cells from the pinned accepted v7 prior state and compares the complete
ordered export. It does **not** trust saved status strings or rerun the
earlier accepted ancestor stages. A prior success log is therefore not
substituted for the new computation, while the ancestor's numerical and
analytic premises remain named. All computation is exact rational/integer
arithmetic with directed square-root checks.

Evidence under `runs/fixed-target-v8-20261028/`:

- `phase-confinement01/02`: original equal-grid diagnostic, eight failures;
  run02 also verifies reversible source instrumentation.
- `phase-confinement03`: the one predeclared redistributed grid, one failure.
- `phase-confinement-heat01`: tiny direct heat check, return code 0.
- `phase-confinement04`: composed equal cover with isolated child bytecode.
- `phase-confinement05`: composed cover with exact replay-root
  allowlist; all arithmetic and composition equal run04.
- `phase-confinement06`: isolated parent and child invocation, with the
  fixed bootstrap and explicit fresh bytecode prefix; all arithmetic and
  composition equal run05. Python 3.9.6, no optimization; exact time, source
  hash, arguments and return code are in its receipt.
- `phase-confinement-build04`: final proof, TeX/log/receipt and rendered-page
  inspection. Earlier builds are preserved separately.

Final checker SHA-256:
`8f5260920d73d1ef8bf63f192a2adcbc0cfc67ab1fc87368c8764dee3689186d`.
Direct heat source SHA-256:
`23669542b58d2476977a0692234517ef05fce9034b9881a381b7c1708cef6954`.
Ten phase/join controls reject missing, duplicate, reordered and
sign-swapped cells, altered curvature, unlicensed phase price, reversed
intervals, negative noise, duplicate keys and a false unassisted success
claim. Five heat controls reject an invalid cubic coefficient, incorrect
negative-ray sign, unlicensed smaller amplitude, missing physical scale,
and a non-strict boundary target.

The final count comparison, all other probability panels, and finite base
remain separate obligations. This result supplies one complete conditional
panel confinement input. It alone authorizes no certificate removal and
establishes no global sharp Berry--Esseen theorem.
