# Uniform LOCAL42 interface theorem with a new zero-decrement support bridge

This audit identifies a conditional route that removes the separate LOCAL47
numerical package from a **new** first-counterexample composition. The archived
LOCAL42 theorem itself remains finite: its statement explicitly assumes
`42 <= n <= 48`. The new route requires a zero-decrement support-lift lemma and
the full existing LOCAL42 numerical predicates, together with their analytic
reductions. Merely changing an `L=48` field is invalid.

| Result | Mathematical status | Execution status |
|---|---|---|
| The literal archived LOCAL42 theorem has a finite upper endpoint | Direct source inspection | No archived program executed |
| Locations of the favorable upper-index term and recorded support interfaces | Locally derived algebra and static source inspection | Fresh static census; 64 left support calls and source hashes checked |
| Support transfer from finite decrement `.19` to infinite zero decrement | Locally derived comparison below, conditional on the stated elementary bridge inequalities and old polynomial signs | Root's separate support-lift arithmetic is a dependency; not executed by this report |
| Uniform acquisition/confinement/local composition at floor 42 | Conditional theorem proved below from the named numerical and analytic premises | Existing archived acceptance was not replayed here |
| Global strict bound from index 43 or 44 | Conditional on an independently proved sharp prefix and scalar first-failure gates | Not claimed as an unconditional theorem here |

The starting source baseline is `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
This work began from fork commit
`2c418e73dc93b0622ab2b4e95ba042201d37604d` on the separate branch
`simplify/uniform42-20261027`. No inherited source, proof object, success marker,
or existing theorem was edited.

## Integration note after the support work

The original transfer argument below uses old finite polynomial signs as
premises. `grouped-support.md` now supplies an alternative direct all-index,
zero-loss support certificate for all65 calls:14 intervals and672 exact
coefficients. In that composition the old support-sign premises are replaced,
while actual-law resource acquisition and the non-support numerical predicates
remain. `finite-entry.md` also proves the endpoint42 scalar gate, so a genuine
BASE41 gives the strict tail from42. The narrower43/44 variants below remain
valid subcases. Neither addition changes the original finite wrapper.

## Exact source convention

All archive paths below are logical keys in
`verification/finite-tail/sources/backend.zip`, member
`finite61/MANIFEST.json`. The bytes must be read from
`finite61/blobs/<sha256>`; the manifest's historical `archive_member` pathname
is not a member of this compact archive. Define

```
A = work/toward40_20261007/audit43/capsule/
B = A + work/below49_20261006/
```

Line numbers refer to the decoded blob, not to a different historical copy
with the same basename. `S` denotes the physical file
`paper/analytic-supplement.txt` at this branch's starting commit. Full hashes
and line counts for the 34 selected archive sources appear in
`runs/uniform42-20261027/interface01/stdout.json`. Particularly important are:

| Alias | Logical source | SHA-256 |
|---|---|---|
| F | `A/proofs/cutoff44.tex` | `41af93935e4ebe64e38670bab222b1f8447b5dd7d95b3dc205ffc97236114f2b` |
| H | `B/package_audit/left42_exact/fifth_heat50.py` | `09a6e27ef42847cef0ac258504546eaef3a3035e83171143f1c2fd848736ac6c` |
| HC | `B/package_audit/left42_exact/heat_support50.py` | `650d7f3617775102fe92977605dfda5fb68a11e0ad738eb799aab77bc4a79e18` |
| LA | `B/package_audit/left42_exact/accept_acquisition.py` | `a565247f6587f3bb07dd67ef2100d08f70aebbe7543937f1ab98f8d09cf31eb6` |
| LP | `B/package_audit/left42_exact/acquisition42_proof.json` | `419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393` |
| SC | `B/acquisition/sperner_kernel.py` | `21249fe117c6756a7a84af481dea2c5a490f9c66013c331cc998ab6828e1bb08` |
| JR | `A/proofs/joint_resource.tex` | `afda69759618eba2a0671e66bac0afc27046e9dd596e8bff5c9e24c29f3fcc44` |
| LK | `B/local/left42_final/central42_kernel.py` | `d025529aa2690c3cfc0f1c34a6af385d6fa69db8e069543057f29475cbb133c3` |

The archive SHA-256 is
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`;
the manifest SHA-256 is
`c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`.
Hashes bind bytes, not mathematical correctness.

## The genuine finite obstruction and its proposed replacement

F:53–62 states the finite range and says that its support contractions use
finite heat estimates. LA:37–42 calls
`fifth.target(42,48,0,R,.19)`, first for the common radius `3.025` at LA:73,
then at every later radius contraction at LA:78. The initial `3.84` support
also uses `(42,48,0,3.84,.19)` in
`B/acquisition/check_local42_support.py:7`. Thus retaining only the old
all-index `3.84` support calculation does **not**, by itself, make LEFT42
uniform. Its later contractions also need repair.

Here is the exact obstruction and a sufficient repair. Put `N=42`, `L=48`,
`q=19/100`, `c=819/2000`, and retain the same rational `ell,S` as HC:55–66,
so `ell^2 <= 41` and `S^2 > 42/41`. For `u=|t|`, let

\[
A=(u^3-3u)/6,\quad J=u^5-15u,\quad
D_+=J/(120\cdot41),\quad D_-=J/(120\cdot47),
\]
\[
W=A-15D_+/2,\qquad
Q=-u^3+\tfrac32ru^2+3bu+\tfrac{.384r}{42}.
\]

H:11–27 and S:566–630 give the finite contact polynomial

\[
P_{48,q}=\tfrac25S^3\{(A-3D_-)W+H_4^2/(256\cdot41)\}
        +S^3E_*W+(cQ+rSq)W,
\]

where `H_4=u^4-6u^2+3` and the adverse remainder `E_*` is frozen at 42.
For the infinite range and zero decrement, set `D_-=0` and `q=0`. Exact
subtraction gives

\[
P_{\infty,0}-P_{48,.19}
=SW\left\{\frac{S^2J}{4700}-.19r\right\}.
\tag{1}
\]

The cleared domination gate for the fifth-order envelope gains `3D_-W`,
and the gates on `A,H_4,J,W,-Q` do not change. On any interval `[R,U]`
where the old strict polynomial gates hold and the braces in (1) are
nonpositive, the new infinite-range contact polynomial is strictly negative.
The denominator `W` is already strictly positive. This is an algebraic
domination argument, not numerical extrapolation in `n`.

At `u=U`, both signed whole-threshold endpoint contact bounds are therefore
strict. To extend beyond `U`, use the **direct support derivative lemma**
S:350–410, with zero decrement and `E=.384/42`:

\[
L(u)=\tfrac25(u^2/2+1/2+E)+cQ'(u).
\]

It is sufficient to check

\[
Q(U),Q'(U),Q''(U),L(U),L'(U)<0,\qquad 1/5-3c<0.
\tag{2}
\]

Indeed `Q'''=-6`, so `Q<0` on the whole ray. The actual score multiplying
the contact cubic may then be replaced by the lower bound `c`. Also
`L''=2/5-6c<0`, hence `L<0` throughout the ray. The actual heat/contact
upper envelope decreases strictly from its negative endpoint, uniformly in
the raw threshold `H`. Reflection covers `t=-u`. Contact is contradicted at
every exterior point, including atoms and accumulation points. The splice
does not require a new claim about the fifth-order polynomial past `U`, nor
does it use the old crude ray estimate below its documented cutoff `4.5`.

For all 64 recorded LEFT42 support calls, the static census finds

\[
1.16242091\le r\le1.42917482<3/2,\quad
0\le b\le.46459359<1/2,\quad 2.5\le R\le3.025.
\]

The first common call has exactly
`r=71458741/50000000`, `b=46459359/100000000`, obtained as maxima of the
same surviving coarse rows (LA:72). A bridge may therefore use
`U=39/10`, `r>=1`, `r<=3/2`, `b<=1/2` in (1)–(2). For the initial support
call it may use `U=21/5`, the fixed HC moment parameter in
`[46/25,37/20]`, and `b<=2/3`. The lower bound on `r` here is a bound on
the **certificate's upper-bound parameter**. It does not assert
`rho >= 46/25` for every actual law.

This report uses as a named **support-lift premise** that the elementary
inequalities (1)–(2), the initial parameter enclosure, and the retained finite
polynomial signs have been established. The separate root support-lift proof
and exact checker are to discharge its new small arithmetic part. This
report independently checks the algebra and the analytic splice; its static
census does not replay the old Bernstein signs.

## Interface matrix: what actually depends on the index

| Interface | Exact source locations | Uniformity reasoning and conditions retained |
|---|---|---|
| Initial support | `B/acquisition/check_local42_support.py:7`; H:11–45; HC:55–66 | Genuine favorable `D_-` at 48. Replace only via the new support-lift premise at zero decrement. All-law moment bounds, positive closed contact and the exact heat remainder remain inputs. |
| Initial signed moment entry | `B/acquisition/accept_initial42.py:6–14,30–68`; `B/acquisition/local_signed_core.py:22,29,79–139` | `nmax=98` appears in validation and `c0=.4095+K/nmax`. Here `K=0`, so no finite upper index enters that value. Fourier bounds use the floor 42, the raw resource and the weighted defect. Full signed moment and probability cells remain necessary. |
| General/paired feedback | `B/acquisition/coupled_panel_core.py:29–78`; `B/package_audit/left42_exact/paired_extended.py:19–44` | All-index Fourier remainders have positive coefficients and decreasing factors `n/(n-1)`, `1/(n-1)`, `1/sqrt(n)`. Positive damping denominators increase. Extended left domain requires `M<3`, `g^2<2`, `R>2g`, and the same actual `rho` lower bound. These conditions are checked per call; they are not discarded. `steps=48` is an iteration count. |
| High-frequency remainder | `B/acquisition/high_window_core.py:12–33` | Every selected frequency window retains six pieces and checks `2Nc>1` before using monotonicity of `sqrt(n) exp(-cn)`. The refined rational/exponential factors and comparator have their own domain gates, including `N>=5`. No upper index occurs. |
| Corrected phase curvature | `B/acquisition/corrected_phase_callback_v2.py:15–25`; extended callback at corresponding lines | `q=C*rho+min(phi_low*g0,.4*g0)/2`, `g0=3.16*rho-3-d`. The minimum is necessary when `g0<0`. Positivity and coherent four-corner use remain required. The extended callback takes the actual moment lower bound returned by the same paired kernel. |
| Central radius and first strip | `B/acquisition/central42_acquisition_core.py:38–52,57–78`; `B/acquisition/panel_exterior.py:38–94` | Bounded-threshold Taylor bounds freeze adverse inverse powers at 42, with both signs and strict exterior negativity. The moment feedback follows a proved contraction. No favorable upper-index term was found here. |
| Left heat radii | LA:37–42,70–82 | 64 finite heat calls, including the first common call. Each must use the support-lift lemma; replacing only the initial radius is insufficient. The same law's `rho,beta` bounds are mandatory. |
| Left first strip | `B/package_audit/left42_exact/panel_exterior42.py:38–94`; LA:84–91 | Polynomial terms and remainder use the floor 42; the scalar allowance `.54*Qpos/N` and decrement allowance `.19` remain valid for the stronger zero-decrement premise. `n_ceiling=48` is output metadata, not a term in the formula. Strict negativity and both signs are retained. |
| Global confinement and feedback | `B/package_audit/left42_confinement/confinement_core.py:27–44`; `B/acquisition/central42_confinement_core.py:16–34,48–60`; SC:19–142 | Requires the parameterized confinement proof below: left strip `.575`, actual cubic coefficient 30 for its first contractions, both deleted indices, all signs, and strict gates. Every new radius is derived after confinement. No hidden upper index occurs in these formulas. |
| Noise profiles | `B/package_audit/left42_confinement/profile_core.py:11–33`; `B/acquisition/central42_profile_core.py:8–40` | Bands are clipped by the same row's `Lambda`; the joint resource gives `d<=d0(1-low/Lambda)`. The profile cannot be inferred from two unrelated marginal maxima. Empty bands and inherited amplitudes have explicit branches. |
| Weighted inward/noise export | JR:170–205,222–241; coupled core:61–76 | The invariant is `n*D <= 42*D_row`, not merely `D<=D_row`. Both positive intercepts belong to one inequality and are rounded outward together. All four phase quadratics retain sign-specific linear terms and `Qbudget`, not `Qraw`. |
| Finite-binomial normalization | `B/local/left42_final/tiny42_normalization.py:33–77,98–140`; signed repair proof below | Actual count displacement is bounded on an entropy segment valid for every `n>=42`; `lambda=n*E(U^2)` is preserved. Positive denominators, counts, variance, mass and noise/span gates are required. Negative cubic corrections use the separately signed piecewise repair, not an unjustified positive correction. |
| TINY/MID/LOW local comparison | F:167–215; `A/proofs/local42_improvements.tex:69–98,155–221`; `A/proofs/local42_signed_gaussian_v2.tex:34–119`; LK:78–95,106–127,180–205 | These comparisons are already conditional on `n>=42`, with all acquired resources. The actual count and both phase signs are preserved. The negative Gaussian branch requires `delta^2<Nv` and `eta<N`; inverse-index coefficients are checked nonnegative before replacing `n` by `N`. Negative event brackets precede use of lower mass. |
| Finite metadata and native composition | `B/local/left42_final/bind_source42.py:14,35`; `B/entry/cutoff44/check_cutoff44_composition.py:51–56,64–88,146`; F:53–62 | These explicitly accept finite `N42,L48` sources and retain LOCAL47. They do not themselves certify the new range. Preserve them, then add a separately named theorem connecting their numerical predicates to the uniform hypotheses. |

The local signed-cubic repair is detailed in
`A/proofs/signed_cubic_repair.tex:70–155` (hash
`ad8360b6af1abe479b84a1070b4ac91a277c514051d78d7a71b5a3455e9e2696`).
It allows a negative cubic bracket using the upper score `.4226`, and clamps
the combined inverse-index cost at zero before the floor substitution. The
early left rows must use their selected piecewise TINY route
`B/local/left42_tiny_final/normalization_piecewise42_v2.py` (hash
`acc4055234a2629298cb665b12474ba5a9f35ed979dd3d238fffe9afd4aa5708`).
One cannot apply a positive-cubic-only normalizer to every left row merely
because another file of that basename is present. MID/LOW selection is
restricted to the rows whose acquired noise reaches the respective domain.

## Parameterized confinement at floor 42

The literal confinement statement S:6534 onward starts with `N=47` and
strip `.55`; citing that statement unchanged would leave a gap. The following
derivation explains the substitutions used by the actual LOCAL42 programs.
It retains the source's contact identity, moment resource, and finite Stirling
inequalities as analytic premises.

Let `n>=N=42`, `Y=B+U`, `E(U|B)=0`, `p in [l,h] subset (0,1/2)`,
`X=ell(Y-p)`, `lambda=n E(U^2)`, and `theta=ell^2 E(U^2)`.
Assume the already acquired strip `supp Y subset (-sigma,1+sigma)` and
inner gap `1-d`, with `d<=d0<sigma`. In the first LEFT42 step
`sigma=23/40`; after a successful step it is the newly proved smaller
amplitude. The source programs check both signs of `H`, rather than
reflecting the signed phase and then reusing an unsigned formula.

The inner support endpoints give `U0<=d` and `U1>=-d`; the outer strip gives
`|Ui|<sigma`. Conditional centering gives exactly

\[
\rho=\ell^3\{pq(1-2pq)+3pq(s_0+s_1)
                 +p\mathbb E U_1^3-q\mathbb E U_0^3\}.
\]

Consequently

\[
\rho\le\rho_B(p)+c_\rho s,
\qquad
c_\rho^2[l(1-l)]^3>[3(1-l)+\sigma]^2
\tag{3}
\]

is a sufficient bound, since `ell^3<=[l(1-l)]^(-3/2)` and
`pq(s0+s1)<=q s`. Thus `rho<=rho_B(l)+c_rho*lambda_high/N` throughout
the closed noise cell. SC:52 tests (3), SC:79 uses it. The left first-step
configuration takes `c_rho=30` with strip `.575`; later profile configurations
may take 24 only after the gate with their actual smaller strip passes.
The identity for signed `beta` and its outward bounds are unchanged.

For strict-gap concentration, independently couple the conditional noises.
The Bernoulli increment is at least `1-d`. An interval with diameter strictly
less than this increment is an antichain after conditioning. The elementary
random-chain counting argument in S:6632–6670 therefore applies for every
remaining index. For LOCAL42 the smallest one is

\[
J_0=N-2=40,\quad r_L=l-(1-l)/40,\quad r_R=h+h/40.
\]

The positive endpoint gates imply that all binomial modes at `j>=40` lie in
this interval. The same finite Stirling proof gives the uniform strict cap

\[
\sqrt j\,\max_k {j\choose k}p^kq^{j-k}
<\frac{.4}{\sqrt{v_*}(1-1/(12\cdot40))},\qquad
v_* =\min(r_L(1-r_L),r_R(1-r_R)).
\]

This is precisely SC:57–61 with `N=42`. It covers both `n-1` and `n-2`,
including an independent residual conditional noise. The score-derived
deleted concentration inequality still requires **both** predecessor caps
`C_(n-1), C_(n-2) < .4253`. The scale factor must satisfy

\[
F_d^2>\max\{(42/41)^3,42/40\};
\tag{4}
\]

each ratio decreases in `n`, and SC:30 tests both inequalities. Reusing
the old factor for floors 46 and 45 would be incorrect.

The signed deletion identities are algebraic at `m=n-1` and have no lower
floor 47. Conditioning one removed pair leaves `n-2` full summands. The
noise sum stays signed, so the conditional error uses `E(U)_+=E|U|/2`.
The same argument handles deterministic conditional laws and atoms. The
exceptional pair event is strict (`Delta>tau`), and its bound is

\[
\min\left\{\frac{s}{s+p\tau^2},\frac d{d+\tau}\right\}.
\]

Replacing `.55` by `sigma` in the interval geometry requires the actual
strict gates `1-sigma-2d0>0`, `1-2d0-2tau_+>0`, disjointness, and buffer
widths (SC:25–29). These ensure all antichain intervals have diameter
strictly below `1-d`; equality is not accepted. The upper contradiction is
`L-sigma*U-error>0`. For the lower ray the error is independent of the ray
length once strict-gap concentration is available, and the additional
positive slope gate proves the whole ray inside the previously acquired
strip. The new amplitude is used as a support update only afterwards.

Finally retain the **single strict resource**

\[
ne\rho+n\phi(0)D/6+n^{3/2}L_{\rm leak}<\mathcal B(H).
\tag{5}
\]

For a phase/noise cell let `R=Tcell/kappa-b_* E^2 lambda_low` and let
`P>=0` be its binary asymmetry penalty. The remaining resource is `R-nP`.
It is bounded above by `R-NP`; if the latter is nonpositive, (5) excludes
the whole cell. Otherwise `nd<G=(R-NP)/alpha`. The old error expression
is `(zR+A)/n-zP+B*bad`, so the explicit positive gate `zR+A>0` licenses
`n>=N`. The stronger tangent bound uses the same resource simplex and

\[
\frac{x}{N\tau+x}
\le\frac{N\tau}{(N\tau+t)^2}x+
       \frac{t^2}{(N\tau+t)^2},\qquad x,t\ge0.
\]

Its difference is `N*tau*(x-t)^2/((N*tau+x)(N*tau+t)^2)`. Relaxing
`R-nP` to `R-NP` and `1/n` to `1/N` is legitimate because the cost
coefficients are nonnegative. SC:120–137 implements these two individually
valid bounds. No monotonicity of a numerical minimum is assumed. Thus all
strict gates of SC at these changed parameters have the same all-index
meaning. This supplies the needed floor-42 confinement theorem, conditional
on (3)–(5), the source contact/moment identities and the numerical gates.

## Weighted resources and a precise conditional theorem

The same-law weighted invariant cannot be weakened during the extension.
Suppose the row gives `nD<=N*d_D` and

\[
D\ge b+6mS_*(\Delta_A+\Delta_B)+K\theta,\quad
b\ge0,\ K>0,\ \theta\le\Theta<1.
\]

Write `r=d_D-b>0`. JR:170–205 derives, for all `n>=N`,

\[
\frac d{d_*}+\frac\lambda\Lambda\le1,\qquad
d_* =\frac r{6(1-\Theta)S_*},\quad
\Lambda=\frac{Nv_*r}{K(1-\Theta)}.
\tag{6}
\]

Indeed `nD>=Nb+6N(1-Theta)S_*d+K(1-Theta)lambda/v_*`.
Both intercepts come from this single inequality. Outwardly enlarging both
positive intercepts preserves it. On `lambda>=lambda_low`, it supplies
`d<=d_*(1-lambda_low/Lambda)`; this is the input used by the profiles and
the signed local comparisons. The cases `r<0` and `r=0` require respectively
exclusion and the separate zero-resource/zero-noise conclusion.

**Uniform zero-decrement LOCAL42, conditional version.** Assume all the
underlying attained positive-contact, finite moment-cap, Fourier, resource,
finite-binomial, signed local-comparison and Bernoulli inequalities used by
F. Assume the complete exact numerical predicates selected for its LOCAL42
acquisition, confinement, profiles and TINY/MID/LOW comparison are true at
their recorded inputs. Assume the support-lift premise above. Then for
every integer `n>=42` there is no attained positive maximizing witness
satisfying all of

\[
0\le C_n-C_E\le .54/n,\qquad C_n<.4226,
\]
\[
C_{n-1},C_{n-2}<.4253,\qquad n(C_{n-1}-C_n)_+=0.
\tag{7}
\]

To prove this, obtain initial support by the lifted initial heat call and
apply the complete signed entry cover, with `K=0`. Exclude the outer
probability panels as in F:128–165. On central panels retain their existing
bounded-threshold contraction and strip predicates. On left panels use the
lifted 64 heat calls in their original order and then their first strip
predicates. Apply the parameterized confinement theorem to each sign before
each support feedback. Transfer the coherent quadratics and (6), then acquire
the complete closed-noise amplitude profiles. All these operations refer to
the same current law; no maximizing witness at a different index is inserted.

For positive noise, the TINY/MID/LOW coverage in F:167–215 is closed at its
phase and noise seams and compares the actual count distribution with the
matched Bernoulli law. The signed Gaussian and cubic repairs have explicit
all-index hypotheses and positivity gates. Their conclusion contradicts the
maximizing score. For zero noise, conditional centering makes the current law
exactly the matched two-point law. Apply the separate strict finite-index
Bernoulli theorem, rather than divide by noise or take an unproved uniform
small-noise limit. This proves the conditional statement.

The theorem keeps equality `C_n=C_E` in its assumptions. To obtain a global
strict conclusion from `n>=43`, one additionally needs a weak sharp prefix
through 42 and a proof that a least later index with `C_n>=C_E` satisfies
the scalar gates (7). Its predecessor values are at most `C_E`, so its
decrement is zero. A prefix through 43 gives the analogous route from 44.
Choosing instead the least index with `C_n>C_E` proves only the weak global
inequality; it does not exclude later equality. This report does not certify
either prefix, and it does not silently upgrade a conditional prefix input.

## Dependency consequences and limits

In the new conditional composition, the separate LOCAL47 acquisition,
confinement, profiles and local comparison become unnecessary because the
uniform zero-decrement LOCAL42 theorem covers the first contrary index.
The global positive ceiling, slow-decrement search, multi-loss telescope and
their finite strong-barrier calculations can likewise be omitted **only**
when the independent sharp prefix and scalar first-failure argument supply
all of (7). The original published theorem, finite wrappers, certificates
and historical dependency graph remain intact.

Without the support lift, one can retain the old all-index `3.84` support
proof for indices at least 47 and the finite LOCAL42 initial support below
that point, but the 64 later left heat contractions still block the uniform
claim. Without the joint resource, both the noise profiles and local
comparison lose their licensed hypotheses. Without the floor-42 confinement
derivation, the old literal floor-47 theorem cannot supply those profiles.
These are mathematical dependencies, not packaging details.

Fresh evidence for this report is the bounded standard-library script
`check_uniform42_interfaces.py`, run as recorded in
`runs/uniform42-20261027/interface01/run.json`. It verifies selected blob
hashes and lengths, enumerates 64 recorded support calls, checks their closed
coverage and moment rectangles with exact fractions, and rejects three
disposable malformed interfaces. Stdout, stderr, input hashes, interpreter
version and return code are preserved. No archived checker, discovery driver,
certificate generator or imported archived module was executed. The static
PASS does not reprove any archived polynomial sign or numerical acceptance.

The remaining analytic source proofs and external inputs retain their earlier
conditional audit status. This is an index-uniformity and composition result,
not an independent full reproof of attainment, contact, the Fourier remainder,
or the local score identity. A final accepted implementation should add the
new support-lift proof/checker and a separate composition binding; it should
not rewrite finite `L=48` metadata to suggest an old acceptance already proved
the new theorem.
