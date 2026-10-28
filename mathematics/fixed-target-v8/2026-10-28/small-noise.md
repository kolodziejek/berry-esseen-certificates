# An all-threshold small-noise bypass for the confinement obstruction

28 October 2026. Independent theory branch `research/v8-small-noise-20261028`, worktree `small-noise-v8`, base `cf5f945167dfdc24b80da7ddebf97ba43c8f6362`. This work adds only research/evidence files. No native certificate, prior source, old log, finite base or upstream repository was modified.

**Result:** on p∈[.41,.42], the previously acquired `|U|<.6` strip and inward bound `d<.069`, together with fixed-target contact and a genuine sharp predecessor, imply `|U|<.5` whenever `0<=lambda<=.075`, for every raw H and every actual n>=42. This covers the entire first noise band of the original equal128-box confinement test without adding or redistributing cells. It does not rely on a resource upper bound at one fixed phase.

| Result | Mathematical status | Execution status |
|---|---|---|
| Actual conditional cubic expansion and coefficient24 | Independently derived from the existing .6 strip | Exact rational gate and four actual finite-law controls passed |
| Small-noise moment/scale caps | Independently derived for all n>=42 | All rational comparisons passed |
| Fourth-order heat extension to u>sqrt(3), complete rays | Independently re-derived, uniform in raw H | Two boundary and twelve ray gates passed using independent simpler constants |
| Full first noise band, including lambda=0 and .075 | Locally proved conditional theorem | No numerical phase/noise cover needed |
| Remaining seven noise bands/full panel composition | Conditional on their genuine complete finite gates and the earlier acquired strip | B reports a completed composition; this task did not replay that wrapper |
| Global confinement across all p or full conjecture | Not established | Not run |

## Exact statement and scope

The law is an actual standardized fixed-target maximizing witness `(P,H)` with nonnegative excess over CE at n>=42. Assume the true predecessor `C_(n-1)<=CE` and closed-support contact. Its sign split is `X=ell(B+U-p)`, with `B=1_(X>0)`, `p=P(X>0)` and `E(U|B)=0`. Assume the already acquired outer strip `|U|<3/5` and inward conditional bounds `U_0<d<69/1000`, `U_1>-d`. If `lambda=n E U^2<=3/40`, then `|U|<1/2`.

These are same-law hypotheses. We do not infer iid realizability from a relaxation, and do not invent independent conditional fluctuations. The iid predecessor and maximizing-contact inputs remain explicit; the conditional moment calculations themselves concern just one marginal. The .6 strip is acquired before the bounded cubic calculation and is never derived from the desired .5 conclusion.

## Independent analytic derivation

The full proof is in `small-noise.tex`. Its main simplification is to exploit `lambda/n`, rather than a noise-independent moment cap. Let v=p(1-p) and s=lambda/n. Conditional centering gives `ell=(v+s)^(-1/2)` and `theta=lambda/(nv+lambda)`. Sign consistency of the actual split gives the exact cubic identity

`rho=ell^3[v(1-2v)+3 E|B-p|U^2+E sign(B-p)U^3]`.

Since `|U|<.6`, its excess over the binary skeleton is at most `[3(1-l)+.6] v_l^(-3/2) lambda/n`, with l=.41 and v_l=.2419. The exact comparison `24^2 v_l^3>[3(1-l)+.6]^2` proves the retained coefficient24. No fourth moment of the original law is introduced. Also `rho_B(l)<21/20`, by squaring. Thus

`rho <21/20+24*(3/40)/42 <1093/1000`.

The identity `beta=1-2p-2(1-p)theta+2theta_+`, `0<=theta_+<=theta`, gives tight p-endpoint bounds because both bounding functions decrease with p. Independent outward rational caps are

`theta<733/100000`, `ell>1009/500`, `rho<1093/1000`, `.151<beta<.187`.

The heat expansion is re-derived directly: spatial order4 and variance orders2/1/1 leave a remainder with coefficient `[1/48+|u^2-1|/16] ||phi^(5)||/v^(3/2)`. Hence the source remainder is valid for u>=1; using its positive cubic coefficient only requires u>sqrt(3), rather than the earlier convenient u>=2.5. The signed fourth-order term is bounded by its absolute value. Gaussian norm estimates follow from elementary Fourier integrals. The proof also re-derives the all-H direct derivative bound by combining a normal-density Taylor remainder and its variance-change heat integral.

At fixed moment caps, take physical support boundaries `u_-=459/250=1.836` and `u_+=2179/1000=2.179`. The negative ray uses beta direction−.151; the positive ray uses+.187. The exact heat/contact upper bounds are

`-4204450376159697231939/8200000000000000000000 <0`,

`-504398409454360553183541/2099200000000000000000000 <0`.

All twelve full-ray derivative signs are strictly negative. The negative cubic contact bracket is checked before replacing CE by the lower rational819/2000. The moments are frozen while following the rays. The complete closed rays, including boundary atoms and accumulation points, are therefore excluded.

Both radii fit strictly inside `ell(p+.5)` and `ell(1.5-p)` for the entire probability panel, so `-.5<Y<1.5`. The previously acquired inward bounds finish both sides of `|U|<.5`. At lambda=0, U=0 directly; no division by noise or appeal to a nonuniform small-noise limit is made.

## Relation to B's attempted confinement and the seam

I read the current source proof and128-box calculation in sibling `phase-confinement-v8`, including `phase-confinement.py` and the existing `confinement-proof/confinement.tex`. Its earlier eight failed upper-ray gates all lie in the closed first noise band[0,3/40]. The new lemma supplies the desired amplitude conclusion directly on that whole band and all raw H. It is not an assertion that the previously failed error majorants become positive.

For the rest, retain the genuine passing gates on the other seven **closed** equal bands, whose union is[3/40,3/5]. The endpoint3/40 belongs to both routes. The earlier acquired bound `lambda<3/5` supplies the top endpoint coverage. All signed phase bands needed by the remaining route, both rays, excluded-box justifications, source binding and strict margins remain obligations of that finite composition. A count of passed gates alone is insufficient.

B's independent exact implementation `phase-confinement-heat.py`, reviewed SHA256 `23669542b58d2476977a0692234517ef05fce9034b9881a381b7c1708cef6954`, uses tighter directed roots and the same valid parameter domains. Its reported boundaries1.836985166744 and2.180158219872 and its all-ray sign structure agree with the independently derived theorem. My implementation uses the simpler constants above, does not import that source, and does not copy its evaluated radii. B reports that the resulting composition of the original equal128 boxes passes, with16 handled by heat,84 resource exclusions and28 boxes requiring both ray gates. This report is not a fresh replay of that combined wrapper; the parent is reviewing its complete acceptance separately.

## Evidence and dependency boundary

Run `python3 -B mathematics/fixed-target-v8/2026-10-28/small-noise-check.py`. It imports only the standard library. The exact receipt, output and stderr are in `runs/fixed-target-v8-20261028/small-noise01`. The checker also verifies the same-law conditional cubic and variance identities on a standardized skew Bernoulli in the panel and three nearby four-point mixtures of standardized Bernoulli laws, all within the stated noise range. These are genuine law controls, not optimizing witnesses or numerical proof of the contact theorem.

Source edges read include `mathematics/reduction2/2026-10-27/elementary-support.md` (fourth-order heat and direct rays), `mathematics/fixed-target-v8/2026-10-28/confinement-proof/confinement.tex` (the already acquired .6 strip and inward gap), and `manuscript/arxiv-v1/sections/05-geometry-counts.tex:12–52` (same-law normalization and conditional moments). The new proof spells out the only needed domain extension of the heat argument and derives coefficient24 independently.

The new dependency path is `acquired .6 strip + same-law lambda<=.075 -> moment/scale caps -> contact boundary/full rays -> |U|<.5`. It has no dependency on the failed128-box resource error in the first band. Fourier acquisition remains an ancestor of the already acquired strip, but the low-noise lemma needs no additional Fourier, phase-envelope or conditional-count computation. No existing certificate may be deleted merely because this alternative path exists.

## Typeset verification

The final three-page note compiled with TeX Live 2025, return code 0 and no warnings, in `small-noise-build02`. All three pages were rendered at 105 dpi and inspected; no clipping, overlap or equation-layout issue was found. The first build is preserved: its harmless bookmark and paragraph-width warnings were corrected only by changing a heading and displaying the two boundary inequalities.
