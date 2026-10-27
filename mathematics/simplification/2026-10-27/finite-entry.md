# A sharp-prefix replacement for the finite43–48 bootstrap

This is a new conditional composition, not a modification of an inherited theorem or certificate. Its scalar step is proved below. The supplied LOCAL42 and LOCAL47 implications remain separate mathematical and computational obligations. At a first contrary index after a sharp base through42, the old positive-ceiling bridge and the special43 backward bootstrap are unnecessary: sharp predecessors give decrement zero, and support-free smoothing gives excess less than `.3/n`. A second rational envelope strengthens this to a sharp base through41 and a strict tail starting42. Literal source inputs of the selected local producers match these stronger hypotheses.

| Result | Mathematical status | Execution status |
|---|---|---|
| Scalar entry at every integer `n>=42` with `C_(n-1)<=C_E<=C_n` | Locally derived; two rational envelopes checked | Fresh bounded PASS; four false endpoint/strength claims rejected |
| BASE42 + LOCAL42 on actual43–48 implies `C_n<C_E` on43–48 | Conditional theorem, proved here | No native LOCAL42 execution |
| BASE42 + LOCAL42 on actual43–46 + LOCAL47 on all `n>=47` implies strict `C_n<C_E` for all `n>=43` | Conditional theorem, proved here | Neither local chain certified by this run |
| Stronger variant: BASE41 + LOCAL42 on actual42–46 + LOCAL47 on all `n>=47` implies strict `C_n<C_E` for all `n>=42` | Conditional theorem, proved here | Same unexecuted local obligations |
| Twelve of the31 finite61 native predicates bypassed in the new composition | Derived dependency replacement, subject to the retained local implications | Static source identities and exact inventory partition freshly checked |
| Nineteen native predicates and152 LOW rows | Retained obligations, not certified by source inspection | Not run |

Working head before this change: `2c418e73dc93b0622ab2b4e95ba042201d37604d`, branch `simplify/finite-entry-20261027`, in the user's fork. Original reference `6346fc1b4432bc5982822aa696eb566ed9e1e1ee` is unchanged. No inherited files, native generators, collectors, manifests or certificate targets were modified or executed.

## Precise new statement and proof

Use the original constants

\[
C_n=\sup_{P:\,EX=0,\,EX^2=1,\,\rho=E|X|^3<\infty}
 \frac{\sqrt n}{\rho}\sup_x|P(S_n/\sqrt n\le x)-\Phi(x)|,
\quad c=C_E=\frac{3+\sqrt{10}}{6\sqrt{2\pi}}.
\]

Write `a_n=C_n-c` and `delta_n=n(C_(n-1)-C_n)_+`. The independently reviewed scalar inequality is

\[
C_n\le s C_{n-1}+\frac{\sqrt n}{15(n-1)^{3/2}}
                   +\frac{2\sqrt n}{25(n-1)^2},
\qquad s=\sqrt{n/(n-1)},\quad n\ge2. \tag{R}
\]

For completeness, its mechanism is independent of support acquisition. Conditioning on the last summand replaces the preceding sum by a Gaussian with error `C_(n-1) rho/sqrt(n-1)`. For `F_v(t)=Phi(t/sqrt(v))`, spatial Taylor expansion through order two gives error at most `rho/(15 v^(3/2))`, since `||phi''||=phi(0)<2/5`. The heat identity `partial_v F_v=F_v''/2`, integrated from `v` to `v+1`, gives discrepancy between `F_v+F_v''/2` and `F_(v+1)` at most `1/(4 pi v^2)<2/(25v^2)`; here `||phi'''||<=2/pi` follows by integrating `|t|^3 exp(-t^2/2)/(2 pi)`. Multiply by `sqrt(n)/rho`, use `rho>=1`, and take the suprema. The argument uses only the third absolute moment and controls both signs at every threshold. Detailed independent derivation and exact bounds for `c<41/100` are in `mathematics/audit/2026-10-27/scalar-review.md` (with the subsequent independent review in draft PR #2); (R) is also stated in the primary finite source `proofs/cutoff44.tex:108–114`.

**Scalar lemma at43.** For every integer `n>=43`, if `C_(n-1)<=c<=C_n`, then

\[
0\le n a_n < B:=\frac{102469}{350000}<\frac3{10},\qquad
\delta_n=0,\qquad C_n<\frac{1793}{4300}<.4226<.4247. \tag{S43}
\]

Indeed `(R)` and `n(s-1)=(n/(n-1))/(s+1)` give

\[
n a_n\le\frac n{n-1}
 \left\{\frac c{s+1}+\frac s{15}
                         +\frac{2s}{25\sqrt{n-1}}\right\}.
\]

For all `n>=43`, `n/(n-1)<=43/42`, `s>1`, `sqrt(n-1)>6`, and

\[
s<\frac{253}{250},\qquad 42(253)^2-43(250)^2=878>0.
\]

The ratio `n/(n-1)` decreases with `n`, so this single rational endpoint check applies uniformly. Using `c<41/100` bounds the braces strictly by

\[
\frac{41}{200}+\frac{253}{3750}+\frac{253}{18750}
=\frac{7149}{25000}.
\]

Multiplication by `43/42` gives `B`; the exact reserve below `.3` is `2531/350000`. Also `c+.3/n < .41+.3/43=1793/4300`, with reserve `1209/215000` below `.4226`. The ordering of `C_(n-1),c,C_n` makes the decrement exactly zero. The square-root estimate deliberately starts at43: at42 the corresponding integer difference is `41(253)^2-42(250)^2=-631`. This does not refute an alternative scalar argument at42.

**Stronger endpoint42 envelope.** Use `s<81/80` instead: at42 the exact square surplus is `41(81)^2-42(80)^2=201>0`. The same monotonic argument and `sqrt(n-1)>6` give, for every `n>=42`,

\[
na_n<\frac{42}{41}\left(\frac{41}{200}+\frac{27}{400}+\frac{27}{2000}\right)
=\frac{3003}{10250}<\frac3{10},\qquad
C_n<.41+.3/42=\frac{73}{175}<.4226. \tag{S42}
\]

The excess reserve is `36/5125` and the own-cap reserve is `191/35000`. This is a separate valid envelope; it does not change the failed endpoint42 control for `253/250`. The stronger observation was suggested during coordination and its arithmetic and monotonic proof were checked here independently.

**Finite theorem.** Assume `BASE42: C_j<=c` for `1<=j<=42`, and the supplied LOCAL42 implication at every actual index43–48:

\[
42\le n\le48,\quad0\le a_n\le.54/n,\quad\delta_n\le.19,
\quad C_n<.4226,\quad C_{n-1},C_{n-2}<.4253
\quad\Longrightarrow\quad\bot. \tag{L42}
\]

Then `C_n<c` for43–48. If not, choose the least integer `n` in that finite range with `C_n>=c`. Its predecessor is at most `c`; the second predecessor is also at most `c` (for43 it is41). `(S43)` gives the current score, excess and decrement conditions. Both deleted caps follow from `C_(n-i)<=c<.41<.4253`, `i=1,2`. Thus every hypothesis of `(L42)` holds, a contradiction.

**Global theorem with the existing tail implication.** Assume BASE42, `(L42)` only at actual43–46, and supplied LOCAL47:

\[
n\ge47,\quad0\le a_n\le.7/n,\quad\delta_n\le.19,
\quad C_n<.4247,\quad C_{n-1},C_{n-2}<.4253
\quad\Longrightarrow\quad\bot. \tag{L47}
\]

Then `C_n<c` for every `n>=43`. Choose the least contrary `n>=43`; `(S43)` and the sharp deleted predecessors apply. Use `(L42)` if `n<=46`, and `(L47)` otherwise. No positive ceiling at any later index has been used. In fact the terminal pair `C_41,C_42<=c` suffices for this strict tail conclusion; full BASE42 is needed to conclude the weak conjecture at every positive index.

**Stronger base41 variant.** Replace BASE42 by `BASE41: C_j<=c` for `1<=j<=41`, and include actual42 in the required finite `(L42)` domain. Choose the least contrary `n>=42` and apply `(S42)`. At42 the two predecessors are41 and40, both covered by the base; at every later first contrary index they are also sharp. Hence `(L42)` on42–48 yields a strict finite bridge42–48; or `(L42)` on42–46 together with `(L47)` yields `C_n<c` for all `n>=42`. The terminal pair `C_40,C_41<=c` suffices for that tail. Nothing here extends the finite heat proof past48.

Equality is intentional. Choosing the least index with `C_n>c` would establish only a weak result. The sources exclude `a_n=0` as well: their attained positive witness, strict positive-noise comparison, and all-parameter strict Bernoulli branch cover equality. This new composition does not establish attainment or repair that local analytic chain; it assumes the equality-inclusive implications exactly as stated. Reflection/closed-versus-left-limit treatment remains in those retained reductions.

## Exact source interfaces

All finite sources below are immutable members of `verification/finite-tail/sources/backend.zip`. Resolve logical path `p` by `finite61/MANIFEST.json["files"][p]["sha256"]` and read `finite61/blobs/<sha256>`. Line numbers refer to the decoded blob, not to JSON serialization. Abbreviations:

- `A = work/toward40_20261007/audit43/capsule/`
- `F = A + work/below49_20261006/`
- `acq/`, `local/`, `entry/`, `package_audit/` below are under `F`.

The manifest SHA256 is `c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`. The bounded checker pins the16 central source blobs and reports their full logical paths, hashes and line counts. Hash matches identify inspected bytes; they are not numerical proof evidence.

| Edge / actual hypothesis | Primary source location | How the new composition supplies it / what remains |
|---|---|---|
| Finite local domain is **actual** `42<=n<=48` | `A/proofs/cutoff44.tex:53–62,128–136` (SHA `41af93935e4ebe64e38670bab222b1f8447b5dd7d95b3dc205ffc97236114f2b`) | Used only at43–48, or43–46 in the global version. Floor42 calculations are not the assertion `C_42>=c`. |
| Exact local hypotheses `(L42)` | Same `:53–58` | `(S43)` is stronger on excess, decrement and own score. Sharp first and second predecessors give both deleted caps. |
| Attained positive contact at score `C_n`; published moment bounds | Same `:129–134`; `acq/check_local42_support.py:17–19` | Retained analytic obligations. Scalar smoothing does not establish them. |
| Initial support `|X|<3.84` at `42<=n<=48`, lower current score `C_n>=c`, decrement `<=.19` | `acq/check_local42_support.py:7–19` calls `target(42,48,0,3.84,.19)`; `acq/heat_support50.py:55–66`; `acq/fifth_heat50.py:11–28,30–49` | Uses zero barrier. Current lower bound and decrement hold. `heat_support50` computes moment ceilings from `.4095+K/L`; here `K=0`. The finite fifth-derivative bound still uses `L=48`; do not extend this to49. |
| INITIAL42 own cap `.4247`, support3.84, floor42, no positive excess lower bound | `acq/accept_initial42.py:2–14,48–64`; `acq/local_signed_core.py:19–29,123–139` | Own cap from `(S43)`. Recipe `n=42,nmax=98,barrier=0`: `nmax` enters the score lower bound only through `K/nmax`, hence creates no use of a positive ceiling or of an actual failure at42. Uniform floor semantics remain an analytic obligation. |
| INITIAL42 complete probability/resource cover, weighted `nD<=42 D_row` | `acq/accept_initial42.py:24–46,48–64`; `acq/central42_acquisition_core.py:1–6,53–78` | Retain its13 signed calls and100 closed probability panels. No smaller domains follow from the scalar bound alone. |
| Central and upper resource updates use own cap `.4247`; central exterior uses excess `.7/n`, decrement `.19` | `acq/central42_acquisition_core.py:16,38–78`; `acq/upper42_core.py:13–37`; `acq/panel_exterior.py:38–62,65–94`; `acq/accept_central42_acquisition.py:51` | `.3/n` implies `.7/n`; zero decrement implies `.19`. Central support contraction precedes its radius feedback. |
| Left branch own cap `.4226`; finite support contractions use `K=0,q=.19,N=42,L=48` | `package_audit/left42_exact/accept_acquisition.py:36–42,45–92` | `(S43)` supplies cap. Every selected left support call retains zero barrier; the special43 positive barrier is absent. Radius3.025 bridge and subsequent per-row contractions remain. |
| Left exterior needs excess `.54/n`, decrement `.19`, own cap `.4226` | `package_audit/left42_exact/panel_exterior42.py:38–62,89–94` | All follow from `(S43)`. This is the stronger finite exterior, distinct from the central `.7/n` exterior. |
| Confinement uses deleted cap `.4253`, both phase signs, acquired support, resources and quadratics | `acq/central42_confinement_core.py:16–37,38–65`; `package_audit/left42_confinement/confinement_core.py:27–46` | Sharp predecessor bounds license the cap. Support and amplitude are acquired before they are used in moment feedback; retain both signed checks and the common-law constraints. |
| Conditional amplitude profiles and joint `d/d0+lambda/Lambda<=1` | `acq/central42_profile_core.py:8–44`; `A/proofs/cutoff44.tex:200–226` | Retain the whole profile/feedback/interface chain. The new scalar estimate supplies none of these actual-law resources. |
| Left TINY own cap `.4226`, floor42; actual post-resource rows | `local/left42_tiny_final/accept_tiny42_actual.py:40–43`; `local/left42_tiny_final/normalization_piecewise42_v2.py:37` | Cap is available; retain normalization and all45 actual row checks. |
| Complete noise/phase coverage and strict local conclusion | `A/proofs/cutoff44.tex:167–215`; `local/central42_v2/central42_contract.py:9–31`; `local/left42_final/central42_contract.py:9–31` | All TINY/MID/LOW branches remain, including closed seams, both signs and actual row ceilings. Scalar excess does not imply a smaller noise ceiling or a narrowed `p` interval. |
| Existing `(L47)` | `A/proofs/cutoff44.tex:64–71`; independently inspected `BE_cutoff49_20260930.zip`, `BE_cutoff49_20260930/paper/sections/global_route.tex:81–115` | Global variant retains the separate uniform47 acquisition/local chain with exactly its own original gates and phase repairs. Finite61 does not certify that chain. |

The superficially similar `entry/check_support42_48.py` is **not** the initial LOCAL42 support check. Lines7–10 invoke `K=.54`, radius3.4 and `q=.54/41=27/2050`, after testing `.59` and `.7` own-score ceilings; line19 states its positive-barrier first-failure scope. That support predicate belongs to the old ceiling propagation and may be bypassed here. Dropping `acq/check_local42_support.py` instead would leave a real gap before higher-moment use.

The manifest describes the retained initial support action as semantically depending on “fresh .54 finite ceilings.” That is a sufficient license in the old DAG, not an intrinsic extra hypothesis of its literal zero-barrier check. The new scalar proof provides the necessary current/deleted score inequalities directly; it is not a claim that the old metadata already accepts this replacement. Likewise the special43 code's positive `K42=.19*42/43` and decrement `.31` solve a backward bootstrap at actual42. That scenario never occurs in this forward argument.

## The31 native predicates: exact partition for this composition

The following labels are `actions[*].id` in the pinned finite61 manifest. This is a partition of mathematical obligations, not an instruction to remove files or edit the existing31-action collector. “Bypass” applies only after accepting the new conditional composition with the sharp base, and is the same for the base41 strengthening.

| Native label | New status | Reason |
|---|---|---|
| `44.entry/accept4044_01` | Bypass | Its `.59/j` ceiling is replaced at the chosen index by `(S43)` and sharp deleted predecessors. |
| `44.entry/accept41_01` | Bypass | Positive `.54/41` anchor is unnecessary when `C_41<=c`. |
| `44.entry/accept4248_01` | Bypass | `.54/j` propagation is replaced by direct scalar entry at the chosen index. |
| `44.entry/support4044_01` | Bypass | Support is used only to prove the preceding positive-ceiling action; initial local support remains separate. |
| `44.entry/support41_01` | Bypass | Support is used only for the obsolete positive anchor. |
| `44.entry/support4248_01` | Bypass | Positive-barrier support for the obsolete ceiling propagation. |
| `44.acquisition/local42_initial_support01` | Retain | Actual support before local higher moments. |
| `44.acquisition/initial42_accept02` | Retain | Full100-panel initial resources. |
| `44.acquisition/central42_accept02` | Retain | Central resources and exterior contraction. |
| `44.acquisition/central42_confinement_accept01` | Retain | Both-sign confinement and feedback. |
| `44.acquisition/central42_profiles_accept01` | Retain | Noise-dependent amplitudes. |
| `44.acquisition/central42_interface01` | Retain | Acquired resources imply local target rows. |
| `44.acquisition/central42_profile_interface01` | Retain | Closed profile coverage through actual noise ceilings. |
| `44.acquisition/upper42_accept01` | Retain | Upper complementary probability exclusion. |
| `44.local/central42_v2_tiny_accept01` | Retain | Arbitrarily small positive noise, all phases. |
| `44.local/central42_v2_mid_phase_accept02` | Retain | Central nearest-count middle-noise cover. |
| `44.local/central42_low_fresh_replay01` | Retain |78 whole-count rows and complete binding. |
| `44.local/left42_tiny_actual_accept01` | Retain | Left arbitrarily small noise using actual resources. |
| `44.entry/harmonic_interpolation01` | Retain | Shared analytic-to-arithmetic harmonic predicate used by LOW. Its `entry/` directory does not make it a ceiling predicate. |
| `44.local/left42_source_bind01` | Retain | Actual left resources dominate conditional targets. |
| `44.local/left42_mid_exact01` | Retain | Left nearest-count middle-noise cover. |
| `44.local/left42_low_accept01` | Retain |74 whole-count rows and complete binding. |
| `44.package_audit/left42_accept02` | Retain | Actual finite support/radius and strip acquisition. |
| `44.package_audit/left42_confinement_accept01` | Retain | Left confinement and coherent feedback. |
| `44.package_audit/left42_profiles_accept01` | Retain | Left signed noise profiles. |
| `43.anchor_support01` | Bypass | Improved positive `.48/41` anchor has no role with a sharp base. |
| `43.anchor_accept01` | Bypass | Same improved positive anchor. |
| `43.initial_support01` | Bypass | Special actual42 support under positive `K42` and decrement `.31`, not the retained zero-barrier LOCAL42 support. |
| `43.scalar01` | Bypass | Backward-loss assembly establishing43 is replaced by the least-contrary proof. |
| `43.left_fixed01` | Bypass | Special actual42 positive-barrier reroute is never entered. Ordinary LEFT42 remains. |
| `43.central_fixed01` | Bypass | Special actual42 positive-barrier reroute is never entered. Ordinary CENTRAL42 remains. |

Thus the new finite-local component uses **19 of31 native predicates**. Two modes of `accept_central42_confinement_profiles.py` are distinct predicates and both remain; a filename count would be wrong.

All **152** LOW row predicates remain, with their original exact labels and domains:

- Central: `61.low.central42_v2.ii.minus` and `.plus` for `ii=00,...,38`:78 rows. They are all selected central target rows whose noise ceilings exceed `.05`.
- Left: `61.low.left42_final.ii.minus` and `.plus` for `ii=08,...,44`:74 rows. They are all selected left target rows whose noise ceilings exceed `.08`.

The other target rows are already covered by the original TINY/MID bounds; they are not new omissions. Central LOW uses phase widths `.09,.14,.19,.29,.5` on the source noise bands; left LOW uses `.19,.27,.5` starting at `.08`. All positive and negative signs remain. The manifest's `H_cells` and `outer_phase_cells` recipes, original row ordering, native binders, malformed-object controls and arithmetic acceptance semantics are unchanged obligations. Limiting actual indices to43–46 in the global version does not by itself remove any of these floor42 parameter rows.

The old finite61 collectors still demand their old31-action proof graph, including special43 and source-epoch metadata. They must not be described as passing this19-action argument. A future implementation would need a separately named composition/receipt contract binding the sharp base, new scalar lemma, retained19+152 predicates and shared analytic inputs (plus independent LOCAL47 for the global version). No such collector adaptation or full proof acceptance is claimed here. Shared sign repairs, support/contact/attainment proofs, moment inputs, analytic normalization, and strict Bernoulli comparison are not among the twelve bypassed predicates.

This partition gives savings only in the new finite-entry component. It is **not** a closed whole-repository task reduction until the chosen BASE41/BASE42 providers have been audited for independence: a provider for `C_40`, `C_41` or `C_42` could itself consume a ceiling or LOCAL47 result. This deliverable assumes the sharp base as a separate input and makes no assertion that existing finite-base code can supply it without such dependencies. The base41 variant removes the need for `C_42` from the global base but does not establish `C_40` or `C_41`.

## Fresh evidence and limits

Run `python3 mathematics/simplification/2026-10-27/check_finite_entry.py` from the fork worktree. The script uses only standard-library exact `Fraction` arithmetic, ZIP reads, JSON parsing and hashes. It imports no archive modules and launches no subprocesses. It checks both rational endpoint42/43 proof envelopes, strict score inclusions, all31 distinct action labels and the exact152 LOW labels; it also verifies16 primary-source blob hashes. It rejects the false claims that the `253/250` square-root bound works at42, that the old `1.011` bound works at43, that the43 coarse estimate proves `.29`, and that the finite support window extends to49.

Fresh stdout, stderr and a receipt containing interpreter version, return code, command and input hashes are saved under `runs/simplification-20261027/finite-entry01/`. This PASS certifies only the bounded arithmetic and source inventory reported by the script. The uniform-in-`n` step is the explicit monotonic argument above, not a sampled loop. No numerical iid experiments are needed for this composition: the law-dependent recurrence has already been independently derived and adversarially tested in the separate scalar review; the new logical step applies it only to the scalar sequence and does not change any local law domain.

This is a genuine conditional reduction of the required finite-entry work: twelve old predicates have a precise replacement proof, with their local analytic descendants retained. BASE42 and the retained local proof implications are not established by this deliverable. It neither proves the conjecture nor authorizes deleting certificates or launching the remaining native computations.
