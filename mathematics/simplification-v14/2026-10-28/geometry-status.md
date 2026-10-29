# A whole probability–index region is excluded

The new [proof](geometry-slack.pdf), with [TeX source](geometry-slack.tex),
proves a full signed Berry–Esseen exclusion. It combines the retained
common-law geometry with the published Bernoulli reserve; it is not merely
a lower noise ceiling or a sampled comparison.

For one actual iid marginal `X=ell(B+U-p)` with centered conditional laws,
assume `n>=42`, `p in [1/3,.4]`, amplitude `.7`, inward sum at most `.068`,
`lambda=n E U²<=.32`, raw threshold `|H|<=1.84`, and `nD<=129/4`.
If

    n Q(p)/sqrt(p(1-p)) >= 24,

then

    sqrt(n) [P(S_n<=H) − Phi(H/sqrt(n))] − C_E E|X|³ < −1/(10n).

Here `Q(p)=(6+2sqrt(10))(p−(4−sqrt(10))/2)²`. The incoming acquired budget
`32.20665378` is smaller than `129/4`, and its left noise bound `.32` is
already established in v13. The conclusion includes all phases, both signs
of H, zero noise and threshold atoms. Reflection of the law still requires
its own sign-specific acquisition.

## Proof mechanism

The v13 inward budget first forces `lambda<.09` in this region. The v13
crossing identity expresses the actual CDF as the linear interpolation of
the Bernoulli CDF, a signed curvature correction, and a nonpositive loss.
Discarding the last term is now sufficient: the Bernoulli reserve pays for
interpolation and curvature, and the actual third-moment change is favorable.

The reusable new curvature lemma is

    sqrt(n) C(t) <= beta/[n (pq)^(3/2)]
        * [T/4 + c sqrt(T) + (27 M/256)(5/3+5c/4)],

where `c=(np-q-t)_+<=1`, the increasing-mass counts have variance at most T
and fourth moment at most M, and the Bin(n+1,p) maximum mass is at most
`beta/sqrt((n+1)pq)`. For bounded conditional noise `|U_j|<=A`, one can use
`T=lambda/q` and `M=A²T+3T²`. This lemma holds independently of the geometry
and Bernoulli theorem, and can be reused on another probability range if
its explicit mass and moment hypotheses are established there.

The proof sums all integer distances from the threshold using the elementary
stop-loss bound `E(Z-a)_+ <=27 E Z^4/(256a³)`. Two neighboring positions are
handled directly; the complete remainder uses rational bounds for zeta(2)
and zeta(3). There is no numerical count cutoff or omitted infinite tail.
The term `c sqrt(T)` is necessary: an actual tiny-noise law violates the
version that drops it, even within the raw-threshold bound.

## Region removed and retained dependencies

For `1/3<=p<=b`, a nonnegative signed witness must satisfy:

| b | 1/3 | .35 | .375 | .39 | .40 |
|---|---|---|---|---|---|
| n at most | 125 | 195 | 490 | 1140 | 2681 |

Every column with `b>=.35` extends to the full acquired interval `[.25,b]`
by combining this theorem with the retained v13 bound `n<=168` below 1/3.
The first column does **not** extend below 1/3. The continuous statement
`nQ(p)/sqrt(pq)<24` is stronger than these rounded table entries on its
source-supported probability range.

- Direct count certificates and count-tail bounds are unnecessary in the
  entire new excluded region, including noise above the completed LEFT-01
  interval. The proof excludes nonnegative excess itself.
- The new estimate retains the same actual conditional laws and geometric
  allocation budget. No relaxation optimizer is treated as an iid witness.
- The left `.7` support strips, inward cap, raw threshold, actual central gap
  and coarse geometric budget remain inputs. Their contact, nonnegative-excess,
  sharp-predecessor and sign-specific acquisition ancestors are retained.
- The exact crossing identity and inward-cubic budget are the proved v13
  components. Finite Stirling and Schulz's sharper Bernoulli theorem remain
  external inputs; the latter is used only on `[1/3,.4]`, within its published
  `[1/3,2/3]` range. No quantitative reserve is inferred below 1/3.
- The region `nQ(p)/sqrt(pq)<24`, the smaller left probabilities at their
  remaining finite indices, independent BASE41 and general attainment remain
  open. No full conjecture or general propagation theorem is asserted.

Source locations: `geometry-slack.tex`, Theorem 1 and sections 1–3;
`mathematics/simplification-v13/2026-10-28/geometry-noise.tex`, Theorem 2;
its sibling `crossing.tex`, weighted identity and application-domain passage.
Schulz's primary source and exact theorem location are linked in the proof.

## Mathematical and execution status

| Item | Mathematical status | Execution status |
|---|---|---|
| New region exclusion and reusable curvature lemma | Locally derived with explicit continuous-domain inequalities; coordinator review pending | 28 exact scalar gates plus five fixed integer-endpoint comparisons PASS |
| Curvature conventions and moments | Exact actual-marginal controls; not a proof by sampling | 216 cases, including reflections, endpoint allocations and tiny noise PASS |
| Full signed exclusion on selected actual laws | Exact selected iid examples, not optimization or domain coverage | 15 events on five three-point laws with n=126,140,200 PASS; each exact heavy-atom threshold and both immediate rational neighbors |
| Omission of the square-root curvature term | Refuted by an actual tiny-noise atom | Exact counterexample with n=42,p=.35,t=14 and raw threshold in range |
| Favorable cubic sign below 1/3 | False in general | Exact nearby three-point law at p=.26 has rho<rho_B |
| Acquisition, full remaining comparison and BASE41 | Conditional/open as stated above | No Fourier replay, generation campaign or finite-base acceptance |

The selected actual examples satisfy all theorem inputs, including their
actual support-gap D. No candidate in the final five-law list was excluded
as outside scope. The exact normal/root/distribution helper is openly reused
from the source-pinned v10 `actual_law_checks.py`; these event checks are
not described as a second independent implementation of that helper.

Run, with assertions enabled, from the checkout root:

```sh
python3 -I -B mathematics/simplification-v14/2026-10-28/geometry-slack-check.py
python3 -I -B mathematics/simplification-v14/2026-10-28/geometry-slack-actual.py
```

Final source-bound receipts are `runs/geometry-v14-20261028/scalar02/`,
`actual03/`, and `build03/`. They preserve command, interpreter, return code,
stdout, stderr and input/output hashes. Earlier runs and the initial scalar
diagnostic are retained. The final PDF was compiled and every page inspected.
No baseline, manuscript, existing certificate, main branch or external
repository was changed.
