# Continuous low-noise confinement: scoped result and evidence

The new conditional theorem proves `|U|<1/2` for all `n>=42`, all raw thresholds, and `lambda=n E U² <= 3/40`, assuming the acquired `|U|<3/5` strip, actual inward displacement `d<.072`, fixed-target closed-support contact at `c=CE`, and the sharp predecessor. Its abstract probability range is `[.4,.6]`; the acquired application is only `[.40,.53]`. The result does not claim full-noise confinement on these 13 panels or strict count exclusion.

The primary human-readable artifact is `low-noise-continuous-proof/main.tex` and its matching `main.pdf`. The continuous theorem replaces the need for the 26 new per-panel heat boundary evaluations and 156 new per-panel ray-sign evaluations in this particular low-noise extension. Those successful row calculations are preserved below as discovery/evidence. No existing certificate or production target is deleted, edited or declared redundant globally.

| Result | Mathematical status | Execution status |
|---|---|---|
| Same-law cubic coefficient 24, signed beta bounds, common `Theta=.0074`, `ell>1.992`, `rho<1.105` | Locally derived and checked from the incoming strip; valid also above `p=1/2` | Exact rational gates freshly pass |
| Continuous contact boundary/ray argument | Locally derived conditional theorem, including all real raw thresholds, closed endpoints and support atoms | Fresh exact PASS of 28 endpoint/domain gates; no grid |
| Acquired incoming strip on panels 40–52 and inward `d<.072` | Prior conditional analytic acquisition retained; its Fourier/contact/base premises are not reproved by this task | Frozen elementary 30-panel iterator freshly replayed and fully matched; no Fourier kernel replay |
| Alternative 13-panel low-noise construction | Conditional consequence using separate outward moment caps on each closed panel | 26 boundaries and 156 ray signs freshly pass |
| General acquired strip on `(.53,.6]`, high-noise confinement on all 13 panels, finite base, strict count exclusion, full conjecture | Not established by this work | Not run / not claimed |

## Analytic dependency map

1. `mathematics/strategy-v4/2026-10-27/excess.tex:107–208` supplies fixed-target contact on the **closed** support and the predecessor support bound. Its extra term is `-n*a <= 0`; the contact coefficient is the fixed `c=CE`, not the actual score. The new note restates this at `low-noise-continuous-proof/main.tex:113–130`. Both support signs and all raw `H` remain explicit.
2. The frozen antecedent `low-noise-panels-sources/moment-entry-proof.tex:18–164` supplies the ordered same-law moment/gap contraction, paying the binary floor before noise and displacement and retaining weighted `nD`. Its support-strip check at lines 182–222 supplies `|U|<.6` only on panels 40–52; the separate global inward maximum is `.0719539227`. These statements depend on the accepted v7 input and its analytic premises. The fresh replay below checks its arithmetic, not those analytic premises.
3. The new common moments are derived in `low-noise-continuous-proof/main.tex:51–111`. The exact sign-preserving cubic identity uses one actual marginal, with `B=1_{X>0}` and conditional centering. Since `v=p(1-p)>=.24` and `max(p,1-p)<=.6`, the coefficient is bounded by `(3*.6+.6)/v^(3/2)<24`. The signed beta cap uses `1-2p-2(1-p)Theta <= beta <= 1-2p+2pTheta`; the false above-half shortcut is not used.
4. `manuscript/arxiv-v1/sections/04-support.tex:36–65,104–145` gives the Gaussian expansion and derivative method. The new note at lines 132–196 explicitly extends the expansion below its earlier `u>=2.5` presentation: the fifth-derivative remainder uses `|u²-1|`, hence the displayed error is valid for `u>=1`; the leading cubic is positive for `u>sqrt(3)`. The quartic is handled by its absolute value. The new radii exceed `sqrt(3)`. These are analytic derivations, not inferences from a numerical PASS.
5. The continuous fold in the new note at lines 198–278 uses the **actual** `z=p` on the negative ray and `z=1-p` on the positive ray. For both, `z in [.4,.6]`, `u=1.992(z+.5)` and `b(u)=4963*u/4980-9889/5000`. No reflection of a chosen closed discrepancy is assumed. The quintic boundary function is increasing by a convexity/concavity argument and remains strictly negative at its largest endpoint. Total derivatives of this boundary family are distinguished from fixed-beta derivatives along each physical ray.
6. The actual gap conversion at lines 280–309 supplies the missing inward sides of both conditional supports. Zero noise gives `U=0` directly. The noise seam `.075` is closed. The abstract `[.4,.6]` theorem is applied only on the acquired closed union `[.40,.53]`.

Thus the new extension needs no newly subdivided probability, phase or noise cover. The already acquired strip/gap and sharp predecessor remain necessary; there is no circular acquisition of the `.6` strip from the new `.5` conclusion.

## Continuous exact certificate

`low-noise-continuous.py` imports only Python standard-library `Fraction`, `json` and `sys`. It accepts no external certificate object, imports no project program and has no numerical sampling. The result is scoped to its fixed invocation, not a general proof-object acceptance API.

- Lines 78–84 check common moment and heat domains.
- Lines 88–104 build the polynomial by exact addition/multiplication and compare every coefficient with the displayed explicit expansion.
- Lines 105–112 prove the quartic sign and the endpoint conditions for `P'''<0`, then `P'>0`, then `P<0` throughout the whole interval.
- Lines 114–131 prove negativity of the contact coefficient and all fixed-beta continuation families throughout the same interval.
- Lines 133–151 reject six false or corrupted conditions, including a sign-swapped quartic coefficient, missing quintic term, and confusion between a total derivative and a held-beta ray derivative.

The exact worst heat value is

`-4560620039489147528734839 / 25625000000000000000000000 < -.1779`.

The initially suggested stronger shortcut `P''(left)<0` is false: the exact value is `3110682586789279179 / 136120000000000000000 > .0228`. This is preserved as an expected rejection. The valid argument instead uses convex `P'''` with two negative endpoint values, making `P'` concave with two positive endpoint values.

The independent constructor/reviewer in `phase-accept-review-v8` derived a separate continuous certificate, without importing this implementation; parent integration records commit `82f4ebc`. Its endpoint values agree. The coordinating reviewer also read this complete source and TeX. Their agreement is review evidence; the mathematical proof is the displayed derivative and domain argument.

## Fresh execution evidence

All paths below are relative to this fork worktree. Actual command arrays, Python version, return codes, elapsed times, source/output hashes and stdout/stderr are preserved in the named run directories. Python 3.9.6 ran without `-O` or `-OO`.

| Run under `runs/fixed-target-v8-20261028/` | Actual bounded work | Result |
|---|---|---|
| `low-noise-panels01` | `python -I -B .../low-noise-panels.py --evidence .../low-noise-panels01`; includes isolated elementary 30-panel replay and 13 new rows | Return 0, 0.2022547721862793 s; 26 boundaries/156 signs pass, minimum heat margin `.2131070970220608`; seven negative controls reject |
| `low-noise-common01` | `python -I -B .../low-noise-common.py`; common caps, still 13 rows | Return 0, 0.064849853515625 s; minimum heat margin `.1400483194992774` |
| `low-noise-comparison01` | `python3 -I -B .../compare.py`; compares inert constructor and independent JSON, imports neither checker | Return 0; same p/variance/theta/beta, valid outward root differences, maximum heat-output difference `<6.372e-10`; all ray signs agree |
| `low-noise-continuous01` | `python -I -B .../low-noise-continuous.py` | Return 0, 0.056176185607910156 s; 28 strict gates, zero grid cells, six rejected controls |
| `low-noise-continuous-build01` | Bundled compile helper with `--compiler texlive`; then `pdftoppm -png -r 110` | TeX Live 2025, return 0; five pages, no warnings/overfull/underfull boxes; all five rendered pages visually inspected |

The elementary replay source was read before execution and frozen under an exact file allowlist. The child used `-I -B -X pycache_prefix=<new empty directory>`; the cache remained empty. The complete fresh output matched the pinned old `moment03` output, not merely a status field. The fixed source tree has manifest SHA256 `f57fa08fb8ade69178b34a5c4dd57b5c083c758dc505e8457238763cbcd55e7a`; its proof, script, input, report and original output pins are recorded inside. This binds the replayed code, not the truth of its analytic reduction.

Primary new checker SHA256: `5b126057a526598fd6859590602adb9343a062ede22d4e2ffed2a268eba44dab`.
Primary exact stdout SHA256: `037075771afe38ae92a7e117cfd43e6620d06378e6869827d12e41f5d85eb91e`.
Primary TeX SHA256: `7ab1eaaf4820ae7e91e220c86883805937205aa933800cea0cc1bf4ecb448f1a`.
PDF/render hashes and visual inspection record are in `low-noise-continuous-build01/`.

The row construction retains a genuine standardized three-point countercontrol with `p=13/25`, `theta=1/625`, `beta=-599/15625`; it exceeds the false bound `1-2p+theta` by `1/15625`. This refutes that intermediate shortcut, not the Berry--Esseen conjecture. Missing/reordered antecedent panels, duplicate JSON keys, the wrong directional beta sign, an unlicensed cubic constant and a false variance maximum also reject. These fixed controls do not claim a generic certificate parser has been proved correct.

## Preserved state and next boundary

Work is on `research/v8-low-noise-panels-20261028`, based on `f1b4a13c2eaccb1ac195a0105906237d198d0d63`. Only new files in this fork task are added. The starting reference baseline, inherited certificates and production runners remain unchanged. No Fourier/native calculation, dense search, external write or heavy generation was performed.

The useful next boundary is the higher-noise part of the acquired panels, or a direct strict count inequality using the retained common weighted resource. Neither is solved or attempted in this bounded extension. No global theorem, finite-base claim or full local-package acceptance follows from the present low-noise lemma alone.
