# Retaining the score excess in the LOCAL42 resource

Starting fork commit: `42433b448d9389359e642a3384a949ffdd87b903`.
Reference baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
Branch: `simplify/tighter-resources-20261027`. No old source, certificate,
manifest, theorem, or runner is changed by this work.

**Result.** There is a small, concrete conditional reduction after the existing
confinement/acquisition stages. Keeping the positive score-excess charge in
the source phase resource excludes LEFT row0, removes LEFT row5's MID domain,
removes LEFT row8's entire LOW domain, and removes higher noise bands in LEFT
rows10 and13 and CENTRAL row28. The two signed LEFT row8 LOW producers could
be omitted in a newly named pipeline, reducing the selected LOW producer count
from152 to150. Four signed LEFT profile evaluations also become vacuous.
No acquisition or confinement producer is removed by this argument.

This is stronger than merely substituting the first-failure own-score cap
`73/175`: the calculation already works with the old cap `.4226` on LEFT and
the old row-dependent central caps. The useful change is retaining a term
that the scalar defect update had discarded.

| Result | Mathematical status | Execution status |
|---|---|---|
| Score-chord resource lemma below | Locally derived; conditional only on the stated resource/envelope hypotheses | Fresh exact arithmetic for all45 LEFT and47 CENTRAL rows |
| `4095/10000 < C_E < 40974/100000` | Elementary derivation below | Fresh rational Machin and square comparisons |
| Named empty rows/noise sectors | Conditional on the original same-law row acquisition and its scope | Fresh Fraction calculation;12 negative controls rejected |
| Underlying acquisition, Fourier/contact proofs, strict confinement gates and LOCAL42 comparisons | Supplied/conditional dependencies, not re-established here | No archived program imported or executed |
| Complete global theorem or new acceptance pipeline | Not established by this result | Not implemented or run |

## Source map and exact scope

Write `F` for the logical prefix
`work/toward40_20261007/audit43/capsule/work/below49_20261006/`
in `verification/finite-tail/sources/backend.zip`. Its SHA256 is
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`.
`finite61/MANIFEST.json` has SHA256
`c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`.
The manifest maps logical paths to `finite61/blobs/<sha256>`; line numbers
below refer to these decoded blobs, not historical same-named copies.

Full path/hash pins for22 inputs are in the checker and its JSON output.
The principal data and formula locations are:

| Source | Location and role | SHA256 |
|---|---|---|
| `F/package_audit/left42_confinement/post_sperner42_exact.json` | All45 exact post-confinement resource rows, original metadata `N=42,L=48` | `d0a1f547aa4c181d4ad64e9db403ae566760137d1fe75caedc4f317c8aec2ace` |
| `F/package_audit/left42_confinement/coupled_panel_core.py` | 20–28 binary/noise resource;41–53 weighted feedback;63–72 four signed score/moment corners | `adb21a5ee493fc9c257aa3ba67cdf1a162a841d40798d3e423bd2bc93a16aa3e` |
| `F/package_audit/left42_confinement/contracted_kernel.py` | 313–324 affine score dependence of `A,q`; finite maximum of affine linear coefficients | `b216161eec801c96a77df81fb77771e86e6ab55f0fc1b14cd2428508191a3dfc` |
| `F/package_audit/left42_confinement/corrected_phase_callback_extended.py` | 19–25 sign-corrected curvature, still affine in score | `036d32989f9c522e9d6151cf8898338e13ed2c9790a5d2c003bff095df270a63` |
| `F/acquisition/central42_confinement_candidate.json` |47 outward rounded central rows | `2f95d0271996eb9868c2fffcdfb0fa2646a99c2cf588e70d063178e27d07246d` |
| `F/acquisition/central42_acquisition_core.py` | 16,20–35 cap and directed rounding contract | `edd75b67061e484ba62e0266101c9fe3f98af8d15ac26218a259c630261b37ce` |
| `F/acquisition/central42_confinement_core.py` | 48–59 confinement before feedback, `.4247` cap, then directed rounding | `6c70e17dd81811d16f4bcc267db2a5a3aaac39f95552c065e93411ef79a79c8c` |

The underlying phase resource is `paper/analytic-supplement.txt:2265–2287`;
its Gaussian-weight removal license is at2238–2256. In particular, the
conserved phase curvature must not be charged twice. The actual LEFT
callback is installed in `confinement_core.py:7–10`; the uncorrected curvature
is not substituted here. The checker validates `Qbudget-Qraw` against the
single extra-curvature formula and the affine score differences exactly.

The original row metadata remains finite42–48. Application at a later index
requires the separate zero-decrement support/parameter bridge and all the
analytic inputs described in `mathematics/simplification/2026-10-27/uniform42.md`.
This note neither infers uniformity from `N=42` nor independently certifies
that bridge. At its literal finite scope the same resource calculation applies
whenever the stated original row hypotheses hold.

## Conditional score-chord lemma

Fix an actual acquired same-law witness at an integer `n>=N=42`. Put
`c=C_E`, `C` equal to its current score, `e=C-c>=0`, `rho=E|X|^3`, and
`kappa=997/15000`. Retain the original support, sign, phase, deleted-score,
moment, strict concentration and geometry hypotheses. Assume the source
conserved resource

\[
n(C-c)\rho+\kappa nD+n^{3/2}L\le\mathcal B(H),\qquad L\ge0,
\tag{1}
\]

and the original four-corner upper envelope. For each of its two moment
corners `j`, the endpoint scores are `C0` and `C1`. On either signed phase,
write `h=|H|>=0`. Its quadratic has the form
`A_j(C)+F_{j,sign}(C)h-Q_j(C)h^2`.

The source formula makes `A_j,Q_j` affine in `C`. Corrected phase curvature
adds `(.4-phi)*min(0,3.16*rho_j-3-d)/2`, independent of `C`; conserved extra
curvature is also independent of `C`. Each signed `F` is a finite maximum
of affine functions, plus a score-independent slope. Its linear chord between
the two endpoints is therefore an upper bound. Replace only `F` by that
chord. For fixed `j,h,sign` the resulting expression is affine in `C`.
Consequently its supremum over both corners, both signs and `h>=0` is convex:

\[
G(C)=\max_j\left\{A_j(C)+
 \frac{\max(0,\widehat F_{j,+}(C),\widehat F_{j,-}(C))^2}{4Q_j(C)}\right\}.
\tag{2}
\]

Positive curvature throughout follows from its positive endpoint values.
The maximum includes zero because the maximizing signed coefficient can be
negative; the unrestricted signed-square shortcut is not used.

Suppose `C0<c<chi<C1`, `C<=C1`, and the row gives `rho>=rho_min>0`. For actual
`C` in `[c,chi]`, discard the nonnegative excess charge in(1), and bound
`G(C)` using the endpoints of the larger formal interval `[C0,chi]`.
No actual witness with `C<c` is asserted. On `[chi,C1]`, use

\[
n(C-c)\rho\ge N(C-\chi)\rho_{\min}.
\]

Convexity, applied on these two **closed** intervals, gives

\[
\kappa nD\le B_*:=\max\{G(C_0),G(\chi),
                      G(C_1)-N(C_1-\chi)\rho_{\min}\}.
\tag{3}
\]

This includes `C=c` without assigning it a positive excess. It does not
assume attainment at an arbitrary prescribed score or interpolate different
laws: these are outward envelopes for the same fixed witness and acquired
moment rectangle. The original moment-corner reduction is a retained analytic
premise. For every LEFT row the exact calculation gives `B_*=G(chi)` even
using only the universal `rho_min=1`; no stronger paired moment floor is
needed for the excess charge. The actual paired corners remain in the
underlying quadratic envelope.

Here `C0=.4095`, `C1=.4226`, `chi=.40974`. To verify the bounds on `c`, set
`s_k(x)=sum_{i=0}^{k-1}(-1)^i*x^(2i+1)/(2i+1)`. Integrating the finite
geometric expansion of `1/(1+x^2)` proves alternating upper/lower bounds.
The angle identity `pi=16 atan(1/5)-4 atan(1/239)` follows from tangent
addition with the positive angle below `pi/2`, as detailed in
`mathematics/audit/2026-10-27/scalar-review.md:123–137`. Thus

\[
16s_6(1/5)-4s_1(1/239)<\pi<16s_5(1/5)-4s_2(1/239).
\]

Squaring `3.162277660<sqrt(10)<3.162277661` and using
`c^2=(19+6sqrt(10))/(72pi)` gives `.4095<c<.40974` by exact rational
comparison. No decimal approximation to `pi` or `c` is an acceptance input.

## Preserve the weighted and joint resources

Let the old row provide `nD<=N*d_old`. Equation(3) gives

\[
d_{new}=\min\{d_{old},B_*/(\kappa N)\},\qquad nD\le Nd_{new}.
\tag{4}
\]

This is a bound on **nD**, not a bare bound on `D` multiplied afterwards.
Keep the old same-law geometry `Theta,A,B,p` and its moment inequalities.
For `p` in the closed row `[l,u]`, set

\[
v_* =\max_{p\in[l,u]}p(1-p),\quad
b_*=(6+2s_l)\frac{\sqrt{(1-\Theta)^3}_{\rm lower}}
 {\sqrt{v_*}_{\rm upper}}
 \max\{0,(4-s_u)/2-u,l-(4-s_l)/2\}^{2},
\]
\[
K=\min\{3(s_l+1)B,3(s_l+3)A\}>0,
\quad r=d_{new}-b_*.
\]

The old same-law inequality yields
`nD>=N*b_*+6N(1-Theta)(A+B)d_in+K(1-Theta)lambda/v_*`.
If `r<0` the row is impossible. If `r>0`, the two new intercepts from
this **single** residual are

\[
\Lambda_{new}=\frac{Nv_*r}{K(1-\Theta)},\qquad
d_{new,in}=\frac{r}{6(1-\Theta)(A+B)},\qquad
\frac{d_{in}}{d_{new,in}}+\frac\lambda{\Lambda_{new}}\le1.
\tag{5}
\]

This is the parameterized argument in `uniform42.md:315–341`, tracing the
source `proofs/joint_resource.tex:170–205`. The new calculation does not spend
the residual independently on noise and inward displacement. It reconstructs
**both old LEFT intercepts exactly on all45 rows** before tightening either.
No row here has zero new residual; a zero residual would need a separate
zero-noise assembly and is rejected by this checker.

For CENTRAL, exported coefficients have upward `A,F` and downward `Q` rounding,
and the exact high score endpoint is not exported. The source contract gives
`raw_exact` in `[raw_out-2e-6,raw_out]`, hence
`C1` in `[min(.4247,chi+(raw_out-2e-6)/42), min(.4247,chi+raw_out/42)]`.
The checker encloses the chord weight `(chi-C0)/(C1-C0)` over this interval,
takes upper `A,F` and lower `Q`, and in the high-end charge uses its lower
endpoint and the universal `rho>=1`. These preserve(3). Outward `Theta`, lower
`A,B`, and the old weighted `D` give(5). All47 central rows remain feasible.

## Exact bounded consequences and coverage

All indices are zero-based and all probability panels are closed. The printed
new noise values below are rational **upper** decimal roundings; the receipt
stores the full fractions. Existing values are shown as diagnostics only.

| Row | Probability interval | Old noise ceiling, approximately | New conclusion | Computations that could be omitted in a new cover |
|---|---|---:|---|---|
| LEFT0 | `[.290,.292]` | .008504 | `d_new-b_* < -.0003` | Entire row excluded; its TINY subdomain becomes unnecessary |
| LEFT5 | `[.300,.302]` | .058729 | `lambda<=.049944478<.05` | Entire MID subdomain; TINY and zero-noise endpoint remain |
| LEFT8 | `[.306,.308]` | .086046 | `lambda<=.077273055<.08` | Both signed LOW producers; TINY and MID remain |
| LEFT10 | `[.310,.312]` | .102797 | `lambda<=.094055578<.10` | MID/LOW domains with `lambda>=.10`; two signed profile calls on `[.10,.12]` |
| LEFT13 | `[.316,.318]` | .125954 | `lambda<=.117287323<.12` | LOW domain with `lambda>=.12`; two signed profile calls on `[.12,.30]` |
| CENTRAL28 | `[.436,.438]` | .101378 | `lambda<=.099809552<.10` | Comparison sector `lambda>=.10`; its profile was already inherited, so no profile arithmetic saved |

The full45+47 scan shows these are **all** newly crossed named thresholds
`.05,.08,.10,.12` relative to the acquired rows. LEFT6 still gives
`lambda_new>.0595`, LEFT9 `>.0864`, LEFT14 `>.1239`; CENTRAL38, the last
selected central LOW row, still gives `lambda_new>.05309>.05`. Those are
obstructions to deleting the corresponding rows by this bound, not actual
laws or counterexamples to the conjecture.

Coverage follows by restricting the old complete cover to the newly proved
noise range for the same actual row. Its phase signs, nearest count, closed
phase seams and probability endpoints remain unchanged. A deleted band has
lower endpoint strictly larger than the new ceiling, so its entire closed
domain is empty. Existing comparisons on larger surviving bands remain
available; no positivity inference from a few samples is involved. At the
shared probability endpoint `.292`, row0 exclusion still leaves the adjacent
row's cover available. At `lambda=0`, the separate Bernoulli theorem remains.

The exact recipes are `F/local/left42_final/mid42_contract.py:5–20`,
`central42_contract.py:17–30`, and `bind_low42.py:22–39`. They currently select
74 LEFT LOW producers; omitting both signs of row8 would select72. The78
CENTRAL LOW producers remain, giving150, conditional on a new contract.
`F/package_audit/left42_confinement/profile_core.py:18–34` and
`accept_profiles.py:25,38–49` distinguish actual profile evaluation from
inherited amplitude. Inspection of the pinned profile objects confirms only
LEFT10 band2 and LEFT13 band3 supply the four newly unnecessary signed
profile evaluations. Their source outputs were not numerically replayed here.

## Limits and implementation boundary

The path to every newly tightened row still passes through initial support,
moment/resource acquisition, sign-corrected Fourier bounds, paired-domain
licenses, confinement, and support feedback. In particular, row0 is excluded
**after** its confinement resources have been acquired. This result does not
retroactively exclude its weaker ancestor or remove the computation producing
it. Profile stages needed by the retained domains also remain.

The stronger first-failure caps `.41714`, `.293/n`, zero decrement and deleted
scores below `.41` alone do not eliminate these stages. An upper excess bound
does not supply a positive lower charge when equality `C=c` is allowed; the
piecewise argument above is essential. Zero decrement does not imply zero
conditional noise. The lower deleted caps could improve strict confinement
gates, but no complete replacement of those gates is proved or computed here.

This work is **not automatically composable with the existing one-pass
adapter**. Its old index hashes/output bytes and152 LOW labels describe a
different fixed contract. The proposed150-label cover, changed budget values,
and skipped profile entries require a newly named complete output/index
contract and independent review. The19-action/152-producer plan cannot simply
be relabeled, and no old acceptor may be weakened to make these changes pass.
The internal TINY/MID savings are not entire native job removals. No new wall
time or total certificate-size saving is claimed. Finite-base closure and all
other global-composition premises remain separate obligations.

Fresh evidence is in `runs/reduction2-20261027/tighter-resources02/`:
`receipt.json` records the repository-relative command, Python3.9.6, input and
script hashes, stdout/stderr hashes and return code0. `stdout.json` contains
all92 exact row results, source bindings and12 rejected controls; stderr is
empty. Controls reject missing/reordered rows, wrong score/moment corners,
corrupted curvature, false intercepts, extrapolation, three unsupported row
deletions, misuse of the negative residual and a positive charge at equality.
These are checks of the new arithmetic and interfaces, not independent
verification of the complete archived analytic or numerical proof chain.
The earlier `tighter-resources01` receipt and checker snapshot are retained;
that run used the stronger paired moment floor in the charge. Run02 weakens
this to the universal floor1 and obtains exactly the same new budgets and
consequences.
