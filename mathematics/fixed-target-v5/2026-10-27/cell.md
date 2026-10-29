# Exact first raw fixed-target cover at floor 42

This is a new bounded scalar result, `FIXED_C_FIRST_RAW_N42_R384_RHO24_V1`.
It does not accept the archived `INITIAL42_R384` proof, run a signed acquisition
stage, or certify a local exclusion. The existing certificate files are unchanged.
The fork branch starts at `78f0b7c`; the reference baseline remains
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.

| Result | Mathematical status | Execution status |
|---|---|---|
| The exact scalar expressions defined below satisfy all positivity gates, form a closed 24-cell cover, and have maximum normalized bound below 10 | Locally derived algebra and checked rational inequalities | Fresh success, `cell02/check-receipt.json`, exit 0 |
| These expressions enclose the fixed-target remainder for an attained witness, all `n >= 42`, actual support in `[-96/25,96/25]` | Conditional on the fixed-target contact/transfer derivation, initial structural/support bounds, and the retained universal Fourier primitive estimates | No full analytic acceptance inferred from this run |
| A positive initial Gaussian-weight license follows from that remainder bound | Locally derived implication, with the preceding analytic premises | All 24 sufficient scalar gates freshly checked |
| Full `INITIAL42_R384`, its 12 stages, 100 probability panels, and later local exclusion | Separate obligations; not established here | Not run |

## Exact statement and useful margins

Put `N=42`, `R=96/25`, `c=CE=(3+sqrt(10))/(6*sqrt(2*pi))` and

\[
 c_- =0.4097321837023<c<c_+=0.4097321837025,\qquad
 r_i=1+\frac{3361i}{96000}\quad(0\le i\le24).
\]

For each closed cell `[l,u]=[r_i,r_{i+1}]`, the program computes the rational
upper bound `T_i` below. It checks

\[
 \max_i T_i/l < 9.455732088645 <10,\qquad
 T_i<42c_-l,
\]

with the minimum adaptive-license margin greater than `13.996057920754`.
The displayed first upper bound is an outward rational rounding; the full exact
fractions, all coefficients, and six high-frequency pieces per cell are saved in
`runs/fixed-target-v5-20261027/cell02/check.stdout.json`.
The interval includes both endpoints and has no gaps or omitted sign class.
The signed quantities are bounded by absolute values at this first pass; no
sign-cell exclusions are performed.

Conditional on the stated analytic enclosure, `R_c <= T_i < 10 rho` for the
fixed-target remainder of every relevant witness in this initial domain.
No upper bound on its *actual score* is an input. The old variable-score
interval appears only in a comparison calculation.

The first cell is `[1,99361/96000]`; its raw upper bound is
`2.111688161347` and its adaptive margin exceeds `15.09706355415`.
The final cell is `[173303/96000,7361/4000]`; its raw bound is
`17.069861855816`, above the old uniform threshold `2N/5=16.8`, yet below
its adaptive threshold. This is why retaining the cell's lower `rho` matters.

For the same coarse cells and primitive bounds, the archived score-endpoint
formula with score floor `0.4095` and cap `0.4247` has maximum normalized
upper `9.494488658356`. The exact difference of these two maxima exceeds
`0.038756569711`. This comparison includes the source's pointwise structural
score-cap reductions, and is recorded separately from the still coarser full
interval comparison. It is **not** a comparison against the archived dense
signed first pass, whose different moment enclosures can be much sharper.

## Literal coefficients and why two target endpoints suffice

All moments concern one common centered, variance-one iid marginal. Write
`rho=E|X|^3`, `gamma=EX^3`, `beta=EX|X|`. On a cell, define

\[
 k_4=(R+1)^2/(R+1/2),\qquad
 k_5=(R^3+2R^2+3R+3/2)/(R+1/2),
\]
\[
 M=\min(11.1,Ru,1+k_4(u-1)),\quad
 g=\min(1.85,u,\overline{\sqrt{M-1}}),\quad
 E_5=\min(RM,1+k_5(u-1)),
\]
\[
 b=\overline{\sqrt{(u\overline{\sqrt{u^2+8}}-u^2-2)/2}}.
\]

Bars here mean the program's outward rational square-root bounds, not a new
analytic approximation assumption. The low triple `(L0,LH,L2)` is the complete
`sixth(42,M,g,E5)` triple, including its actual-radius Pearson bounds and all
remainder/damping gates. The universal independent-copy event has

\[
 d_0=3/5,\quad a=(2-d_0^2)^2/(2M+6),\quad m=2/a.
\]

For each of the six windows `1/8,4/25,9/50,1/5,11/50,1/4`, the entire six-piece
high-frequency bound is evaluated, including its gates. Their minimum `KH`
is a minimum of complete bounds; no piece is dropped or selected from a
different window. Define

\[
 K_F=\frac{16}{25}(L_0+K_H+L_2/\underline{\sqrt{42}}),\qquad
 s_F=\frac{16}{25}L_H,
\]
\[
 k=\min\left\{
 3ub+\frac{R(R+2-3l/2)}{R+1/2}(u-1),\;
 6u-\frac32u^2+3b,\;
 Ru/2+\max_{r=l,u}|R/2-3r/2|g+3b\right\},
\]
\[
 A=\min\left\{
 \frac32b(2u+1)+3\Gamma(R,l)u+\frac38u^2(u+1)
 +\frac8{27}u^3-l/2,\quad
 \frac32b(2u+1)+2uM-l/2\right\},
\]
\[
 v_H=\min\left\{\frac25\,3(u+1)+\frac1{15}\max(2,M-3),\quad
 \frac25\max(1/2,2M/3-1/2)\right\}.
\]

`Gamma(R,l)` is the pinned 64-interval negative-gap coefficient; this is a
small scalar polynomial/rational bound, not a local-frequency campaign.
For a formal positive contact multiplier `t`, put

\[
 q(t)=tl-g/5,\quad f(t)=tk+v_H+s_F,\quad
 B(t)=K_F+tA+\frac{f(t)^2}{4q(t)},\quad
 T_i=\max\{B(c_-),B(c_+)\}.
\]

The code checks `q>0`, `f>=0`, `k>=0`, `A>0` and the radial-coefficient gate.
Before square completion, the expression
`KF+tA+f(t)|H|-q(t)H^2` is affine in `t`. Its supremum over real `H` is
therefore convex. The two target endpoints bound all intermediate `t`, in
particular `CE`; this does not require an actual-score range. Square completion
is exact for the relaxed real `H` domain. The independent scalar reconstruction
is checked against the decoded `initial_cell` at `score_floor=own_cap=t`.
That cross-check shares the Fourier primitives and is not independent validation
of their analytic correctness.

## Gaussian weight and scope of the new license

For a fixed-target attained witness, let
`a=sqrt(n)(F_n(H)-Phi(H/sqrt(n)))-c rho >= 0`,
`e=exp(-H^2/(2n))`, `L>=0`, and `D>=0`. The fixed-target transfer identity gives

\[
 \phi(H/\sqrt n)(\gamma+3J)/6
 =(1+H^2/n)a+c\rho+\sqrt n L-\mathcal R_c/n.
\]

Thus `R_c <= T_i < N c_- l <= n c rho` makes the left side positive.
At `c=CE` this left side equals
`e(c rho-phi(0)D/6)`. The crucial coefficient is therefore positive.
In the equivalent conservation identity

\[
 (n+H^2)a+n c\rho(1-e)+n\phi(0)eD/6+n^{3/2}L=\mathcal R_c,
\]

all four terms on the left are nonnegative. Hence

\[
 e\ge 1-\frac{T_i}{N c_-l}>0,
 \qquad e>1-\frac{10}{42c_-}>0.418900326686.
\]

Rearranging with the now positive coefficient also gives
`n phi(0)D/6 <= R_c <= T_i`. These are the first licensed density and defect
bounds. They do not assert the stronger old initial targets `raw<2.24`,
`D<0.784`, or any later small-defect conditions. The maximum direct defect
bound can still exceed 4. Any further feedback must retain raw versus conserved
resource bounds separately and establish its own gates.

## Source and dependency map

Line references below are to this task's source state and the byte-identical
copies in `cell-sources/`.

| Source | Edge used here | Remaining scope condition |
|---|---|---|
| `manuscript/arxiv-v1/appendices/fourier-analysis.tex:2460–2542`, labels `ms:fourier:rescore:re-unsigned`, `...:re-unsignedbound` | Unsigned raw first-pass enclosure, radial and moment coefficients, curvature | Fixed-target transfer must have identical formal-multiplier remainder; initial support must hold for that witness |
| Same file `2325–2395`, `...:entry-remainder`, `...:entry-fourier-budget`, `...:entry-four-corners` | Full Fourier budget and convex endpoint/square-completion reasoning | A coherent low triple and complete high bound must apply for every `n>=42` |
| `kernel.py:19–45` | Outward square roots, exponential reciprocal truncation, elementary constants | Rational arithmetic semantics and source formulas audited, not a formal proof assistant result |
| `kernel.py:60–83` | Universal event and sixth-order low triple | Retained analytic event/Fourier/Pearson/remainder estimates; no actual-score premise in these functions |
| `high_window_core.py:10–38` | Six complete high pieces, window choice, all-index gates | The six-piece analytic bound and the widened window domain must be justified; gates alone do not prove them |
| `kernel.py:88–99` | Negative-gap coefficient, 64 exact intervals | Its analytic reduction to this scalar expression remains a proof dependency |
| `kernel.py:100–177` | Raw unsigned coefficient construction, with no previous ceiling/defect or phase rebate | Formula copied into an explicit scalar reconstruction; only the raw branch used |
| `local_signed_core.py:29,36–39` | Initial rho endpoint and 24-cell partition | Structural moment ceiling comes from the external affine Berry–Esseen bound, not from historical execution |
| `accept_initial42.py:6–14,25–64` | Comparison provenance and separation from existing full acceptor | Old acceptor additionally needs actual-score cap, 12 dense stages and full probability coverage; none is accepted here |

The structural endpoint identity is
`0.3031*0.646/(0.4095-0.3031)=7361/4000`.
The separate bound with coefficients `0.3322,0.429` alone would give
`712569/386500`, which is larger; it must not be used to justify the smaller
endpoint by itself. The initial support theorem is a separate Task A obligation.
The computation also encloses `CE` afresh by 40-term alternating arctangent
series, Machin's identity, and integer-square-root intervals; it does not copy
a floating-point decimal of `CE`.

Archive `verification/finite-tail/sources/backend.zip` SHA256:
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`.
Manifest SHA256:
`c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`.
`cell-sources/provenance.json` records every logical path, blob member and hash.
The four copies were read before importing the two pure scalar modules.
Neither `local_signed_core` nor `accept_initial42` was imported or executed.

## Reproduction, controls, and limitations

Run from the repository root with a fresh unused run id:

```sh
python3 mathematics/fixed-target-v5/2026-10-27/cell_run.py cell03
```

The launcher refuses an existing evidence directory. It saves stdout, stderr,
Python version, optimization flag, return code, input hashes and output hashes.
`cell01` preserves the initial two-cell exploration and the first full-cover
run, with that first checker snapshot. `cell02` adds duplicate-key rejection;
the numerical result is unchanged. Both use Python 3.9.6 without optimization.
The final checker has 12 negative controls: duplicate JSON key; missing or
corrupted radius; reversed rho bounds; wrong cell count or index; reversed CE
interval; unlicensed raw feedback; positive barrier; missing high-frequency
source; corrupted kernel bytes; sign-swapped curvature source. These controls
establish literal-contract and source-integrity rejection, not mathematical
independence. No supplied receipts can substitute for arithmetic evaluation.

The script computes exact fractions, with rigorously directed rational root
and exponential bounds. Its first-pass envelope is a new coarse computation,
not a replayed success marker. Shared analytic kernels remain the major
mathematical dependency. Their complete theorem scope, the fixed-target
witness/support construction, and later feedback/local exclusion still require
independent analytic review. No finite base, global conjecture, or saved native
campaign is claimed.
