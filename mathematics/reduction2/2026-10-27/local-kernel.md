# An exact three-candidate replacement for the LOCAL42 curvature grid

Research date: 2026-10-27. Worktree branch `simplify/local-kernel-20261027`,
starting commit `42433b448d9389359e642a3384a949ffdd87b903`. The preserved
reference is `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.

**Result.** The inner 64-subinterval curvature maximization in both retained
LOW kernels can be replaced, in a new implementation, by an exact maximum of
two endpoint values and at most one explicit rational stationary value.
The new upper bound is never larger than the old outward grid bound. This is
a continuous analytic statement, not an inference from numerical sampling.
The final inverse-index correction must be clamped at zero after improving
the curvature; its old strict positivity is not automatically preserved.
With that clamp the old strict exclusion target remains unchanged.

| Claim | Mathematical status | Execution status |
|---|---|---|
| Exact supremum formula below for every allowed real parameter | Locally derived and proved here | Bounded exact diagnostics PASS; diagnostics are not the proof |
| Domination of the old 64-subinterval outward envelope | Proved pointwise, including both kinks and endpoints | PASS on 3,648 selected calls spanning all 152 LOW configurations |
| Transport of an accepted old cell to the new curvature/clamp formula | Conditional on the supplied whole-count comparison and the other old cell gates | No complete old or new LOW cell evaluated |
| Replacement of 64 curvature terms by at most 3 candidates per cache miss | Proved operation-count reduction at this component | No native timing or full replay; no overall speedup claimed |
| Full LOCAL42, acquired resource rows, or full conjecture | Not established by this work | Native certificates and source unchanged |

## Exact source and interface

Let `B` denote `verification/finite-tail/sources/backend.zip`. The manifest
`finite61/MANIFEST.json` maps each logical path to a SHA256, and its literal
bytes occur at `finite61/blobs/<sha256>`. Let

```
F = work/toward40_20261007/audit43/capsule/work/below49_20261006/
P = work/toward40_20261007/audit43/capsule/proofs/
```

All source line numbers below refer to decoded members, not ZIP offsets.

| Source | Relevant literal lines and role | SHA256 |
|---|---|---|
| `F/local/central42_v2/central42_kernel.py` | 62–65 domain; 80–95 joint gap; 96–114 signed H/phase; 159–169 curvature; 180–189 final gates | `9dc0754fe2dd4f2f7057247d3d62f3b71472c65a49d46f67d35fb0d66e3f8673` |
| `F/local/left42_final/central42_kernel.py` | Same curvature/domain lines; 180–205 signed Gaussian and final gates | `d025529aa2690c3cfc0f1c34a6af385d6fa69db8e069543057f29475cbb133c3` |
| `F/local/central42_v2/central42_contract.py` | 17–31 selected configuration, closed noise bands, 32 H cells, 16 outer phase cells | `de30acd375d9d53d6a7068cd4b5397da6c775c21be29aca2e5c6b5da5f65a39f` |
| `F/local/left42_final/central42_contract.py` | 17–31 corresponding LEFT selection | `10868c085cf69e6a0b1db01b6bcf638e2a13863db088bc966754ae44c22e2167` |
| `F/local/central42_v2/tiny42_normalization.py` | 33–40 domain; 42–78 directed constants; 80–146 normalization gates | `3650f39f618def7615d8be20ce8b9efd28e16202102fb8fa76dd8687deff4a6c` |
| `P/local42_improvements.tex` | 194–198 clamping before changing index; 209–216 conservative central cache | `1a634793af259cccd31cfb86cae8127be0af8bed15559b59d6baaf3f5f8215f6` |

The underlying whole-count argument is transcribed at
`paper/analytic-supplement.txt:7474–7511` (crossing moments), 7652–7681
(curvature envelope), and 7683–7699 (final expression and convexity).
In particular this really is the function with `min(u,c/3)` in its second
denominator. Omitting that truncation would be a different bound.

For a fixed row, signed H cell, noise band and outer phase interval, define

\[
 c=1-d_L,\qquad b=p_+-\min(H/\ell),\qquad J=[u_l,u_h]\subseteq[-1/2,1/2].
\]

The minimum uses all four signed H/span endpoint quotients exactly as the
kernel does. It is an upper bound for the count parameter appearing in the
whole-count lemma. It is **not** the probability, phase, or a parameter that
can be freely reflected. Both signs of H remain separate configurations.
The existing gates give `1/2<c<1`; the new lemma allows also `c=1`.
The phase radii in both contracts are at most `1/2`.

Only the phase supremum in

\[
 V_0={\omega_+\over v_*}
 \left(M(b,c;J)+{\sqrt{A^2+3T_U}\over(2c-1/2)^3}\right)
\]

is changed. The actual code uses a strict outward square-root enclosure for
the displayed root; that enclosure, the moment assumptions supplying it,
all mass/normalization bounds, and every other gate are retained.

## Supremum lemma and proof

For real `b`, `1/2<c<=1`, and a closed interval
`-1/2<=l<=h<=1/2`, set

\[
 f(u)={(b+u-1)_+\over(c-u)^2}
      +{(b+u)_+\over[c+\min(u,c/3)]^2}.
\]

Every denominator is strictly positive: `c-u>=c-1/2>0`, and
`c+min(u,c/3)>=c-1/2>0`. Define `u_*=c-2b`. Then

\[
 \boxed{\displaystyle
 M(b,c;[l,h])=\max\left(
 f(l),f(h),\left\{{1\over4(c-b)}:
 \begin{array}{l}
 c>b,\quad l\le u_*\le h,\\[-2pt]
 u_*\le c/3,\quad u_*\le1-b
 \end{array}\right\}\right).}
\]

An ineligible stationary value is omitted. The maximum therefore uses at
most three exact rational candidates when the input is rational. Each listed
candidate is attained at a point of the actual closed interval.

**Proof.** Write the first summand as `r` and the second as `g`.
On its active region `b+u>1`,

\[
 r''(u)={2[3(b-1)+2u+c]\over(c-u)^4}>0,
\]

because the bracket is `3(b+u-1)+(c-u)>0`. At `u=1-b`, the
first derivative jumps upwards, from zero to `1/(c-u)^2`.

For `u<c/3` and `b+u>0`,

\[
 g'(u)={c-2b-u\over(c+u)^3},\qquad
 g''(u)={2(3b+u-2c)\over(c+u)^4}.
\]

For `u>c/3`, `g=(b+u)_+/(4c/3)^2`, a convex piecewise linear
function. At `u=c/3` its derivative jumps upwards by
`2(b+u)_+/(c+u)^3`, or has no jump if the numerator vanishes.
At `u=-b`, the derivative of the positive part also jumps upwards.
Simultaneous kinks add nonnegative jumps.

Where `r` is active and `u<c/3`, `b+u>1` gives

\[
 3b+u-2c>3-2u-2c\ge0
\]

using `u<=1/2` and `c<=1`. Thus `f` is convex throughout the
active region of `r`, including any intervening `c/3` kink. It has no
interior strict maximum there.

Where `r=0`, the function is zero if `b+u<=0`; otherwise it is
`g`. On `u<c/3` the sign of `g'` changes from positive to negative
only at `u_*=c-2b`. This point is in the positive-numerator region
exactly when `c>b`, and in the region `r=0` exactly when
`u_*<=1-b`. Its value is `1/[4(c-b)]`. On `u>=c/3` the
function is nondecreasing until `r` activates. None of the three kinks
can be a strict interior maximum because its derivative jumps upwards.
A constant segment can contribute its endpoint value only; the whole zero
function is already covered by `f(l)=f(h)=0`. Hence the displayed candidates
contain a global maximizer. Continuity includes equality at every kink,
`l=h`, `c=1`, and stationary/kink/endpoint collisions. This proves the
formula without a bound or sign restriction on `b`. ∎

There is no endpoint-only or sign-pooling shortcut. For
`b=2/5,c=9/10,J=[0,1/5]`, the interior value at `u=1/10` is
`1/2`, strictly exceeding both endpoint values. Also `f(1/5)!=f(-1/5)`
for those same `b,c`. Both statements are checked exactly below.

## Domination of the old envelope

On any old closed subinterval `[a,d]`, nonnegative numerators and positive
denominators give, for every `u` in that subinterval,

\[
 f(u)\le{(b+d-1)_+\over(c-d)^2}
      +{(b+d)_+\over[c+\min(a,c/3)]^2}.
\]

These are precisely the two terms in each of the kernel's 64 loop
iterations. Taking maxima proves `M_exact<=M_grid` for every cell;
no floating estimate, attainment assumption about the underlying law,
or untested resource table is needed for this algebraic comparison.

CENTRAL's cache omits the noise band, whereas LEFT's includes it. This does
not invalidate the comparison with CENTRAL's *actually reused* bound. At
fixed `b,u`, increasing `c` increases both positive denominators, including
`c+min(u,c/3)`. Hence `f` and its supremum are nonincreasing in `c`.
The source visits bands with increasing lower endpoint, and the joint gap
`d_L=d0(1-L/Lambda)` decreases. Thus the first cached grid envelope dominates
each later band's exact supremum. The earlier acquired joint inequality and
the source band order remain hypotheses; arbitrary cache reuse is not
licensed. A new implementation can compute the exact supremum per band or
cache it under the same conservative rule.

## Safe transport through the final sign and endpoint gates

A smaller curvature bound can make the original correction `I` negative.
It is therefore wrong to promise that replacing one line leaves every
literal `inv>0` assertion true. Here is a complete mathematical replacement
for that sign step, preserving the existing score target.

Within one noise cell all coefficients are fixed, with

\[
 B(\lambda)=z+{q\over a\lambda+G^2}+s\lambda-t,
 \qquad I_{new}(\lambda)=A_0+{A_1\over\lambda},
 \quad q\ge0,\ a>0,\ A_1\ge0.
\]

The constants absorb the unchanged harmonic, marked-crossing and Gaussian
terms; these forms and signs are the exact ones in the two kernels.
Only the curvature contribution to `A_0` is reduced. Use instead

\[
 I_+(\lambda)=\max(0,I_{new}(\lambda)).
\]

The supplied whole-count upper bound at actual `n>=N` is bounded by

\[
 mB(\lambda)+{I_{new}(\lambda)\over n}
 \le mB(\lambda)+{I_+(\lambda)\over N}.
\]

This inequality is valid for either sign of `I_new`; it explicitly handles
the case where a negative correction must not be multiplied by `n/N`.
Both `B` and `mB+I_+/N` are convex on positive noise, because
`m>0`, the reciprocal terms have nonnegative coefficients, and a maximum of
two convex functions is convex. Their endpoint gates therefore cover the
entire closed noise interval, including a possible interior `I_new=0` kink.

If an old cell has passed its strict gates at an endpoint, then

\[
 I_{new}\le I_{old},\quad I_{old}>0
 \quad\Longrightarrow\quad
 0\le I_+\le I_{old}.
\]

Consequently its same strict target
`m B + I_old/N < -1/1000` implies
`m B + I_+/N < -1/1000`. The unchanged `B<0` gate still licenses the
mass lower bound. Every other original gate remains required. This proves
conditional acceptance transport for the new formula, with no weakening of
the exclusion conclusion and no reliance on an unreported full replay.
It does **not** edit or silently suppress an assertion in the old acceptor.

## Exactly what work is reduced

Each cache miss at kernel lines159–167 currently forms 64 outward rational
two-term bounds and takes their maximum. The replacement forms two exact
endpoint values, tests a few rational inequalities, and optionally includes
one additional rational value. Thus 61 or 62 candidate evaluations disappear
per such cache miss. This does not mean a 64-fold speedup of a LOW producer:
the marked-tail Poisson computations, 16 inner marked-crossing subcells,
mass/resource/repair arithmetic and all other work remain.

No row is removed. All 78 CENTRAL and 74 LEFT LOW configurations, both H
signs, their 32 H cells, 16 outer phase cells and all closed noise bands
remain. Their actual source domain and target are preserved. No native task
or finite base provider is proved unnecessary by this local result alone.

The checker also counts potential cache keys from the literal contracts,
before the `cap<=0` empty-cell pruning. For one sweep of the 152 producer
configurations the CENTRAL count is 164,864 and LEFT count is 1,247,232.
These are **upper bounds, not measured visits**: CENTRAL keys collapse
noise bands with equal phase radius, LEFT keys include the band, and some
keys may never reach the curvature calculation. If all potential keys were
visited, their 90,374,144 old candidate evaluations would become at most
4,236,288. No elapsed-time inference or claim about actual pruning is made.
Duplicate binder replays are a separate execution-plan issue.

## Fresh bounded evidence and its limits

The new standard-library program `check_local_curvature.py` reads and hashes
the source-only archive, parses only its two resource JSON tables, and
executes no archived module. It independently builds the relevant rational
`b,c` parameters from the literal row/contract/kernel formulas. For every
selected row and both H signs it chooses the first and last noise bands,
H cells0,15,31, and outer phase cells0,7,8,15. This gives 3,648 tested calls.
It compares the exact candidate formula to a direct transcription of the
old 64-term envelope, tests rational interior points and kinks, and verifies
that a listed candidate attains the returned maximum.

Fresh receipt: `runs/reduction2-20261027/local-kernel01/receipt.json`.
Stdout: `stdout.json`; stderr: `stderr.txt` (empty). Exit code0; measured
elapsed time 2.616317834 seconds on the receipt's Python/platform. Results:

* All 3,648 comparisons passed; 2,778 gave a strictly smaller bound.
* Nine sampled calls included an eligible stationary candidate. The other
  calls needed only the two endpoint values.
* 62,276 exact rational point diagnostics passed, including six additional
  adversarial cases covering `c=1`, arbitrary negative/large `b`, a singleton
  interval, kink coincidences, and both phase endpoints.
* Endpoint-only and phase-reflection shortcuts were refuted exactly.
* All six invalid-input controls were rejected: `c=1/2`, `c>1`, reversed
  endpoints, either endpoint outside the nearest-phase domain, and a float.
* Three exact clamp controls include a positive old correction becoming
  negative. They are sanity checks; the displayed inequality proves all cases.

Reproduce from this worktree with unoptimized Python:

```
python mathematics/reduction2/2026-10-27/check_local_curvature.py \
  --archive verification/finite-tail/sources/backend.zip
```

The receipt pins both the script and archive; stdout pins seven selected
source blobs. Exact diagnostics establish their stated finite comparisons,
not the continuous theorem or the validity of supplied moment/contact
lemmas. The continuous theorem is proved above. A future new acceptor needs
independent review of that proof, the helper semantics and the clamp join,
then a separately authorized bounded integration exercise. The existing
certificates, normalizations, numerical targets and native programs have
not been changed or executed.
