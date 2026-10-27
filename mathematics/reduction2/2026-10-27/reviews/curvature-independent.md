# Independent review of the exact LOW curvature supremum

Reviewed commits: `b989359` and `edcb751385086226c0e235cb124012e4386bc249`.
Separate review branch: `simplify/review-curvature-20261027`.
Immutable reference: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
The reviewer did not author the curvature proposal. This review changes only
new review/evidence files and executes no archived program.

**Recommendation: accept the proof note and bounded diagnostic as a conditional
research result. No blocking defect was found in the supremum lemma, zero
clamp, cache direction, or corrected producer-grid count.** This is not
approval of a completed replacement LOW acceptor, the inherited analytic
chain, or the full conjecture. Such an implementation remains a separate
named proof/output contract.

| Reviewed claim | Mathematical status | Execution status |
|---|---|---|
| Exact three-candidate phase supremum | Independently derived below for the stated full continuous domain |8,505 exact piecewise comparisons PASS |
| Domination of each old curvature envelope, including CENTRAL cache reuse | Independently established pointwise, subject to the actual traversal order | Source read; reverse-order negative control detected |
| New correction clamped at zero preserves an old accepted cell's strict target | Independently derived, conditional on the supplied whole-count comparison and unchanged gates |180 rational convexity diagnostics; false floor/mass rules detected |
| Corrected potential-key count | Independently reconstructed from manifest-selected grids and resource tables |43,136 CENTRAL plus77,952 LEFT keys; counts reproduced |
| Original complete LOW certificates or a changed native implementation | Not reviewed as a complete proof | Neither executed |

## Directly inspected source

All archived locations below use the manifest/blob addressing of
`verification/finite-tail/sources/backend.zip`, SHA256
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`.
The manifest SHA256 is
`c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`.
Let `F` abbreviate the logical prefix
`work/toward40_20261007/audit43/capsule/work/below49_20261006/`.

| Source and actual lines | Checks made | SHA256 |
|---|---|---|
| `F/local/central42_v2/central42_kernel.py:62–65,80–114,127–189` | Domain, band-dependent joint gap, signed H quotients, actual mass, empty-cell pruning, cache, curvature and final gates | `9dc0754fe2dd4f2f7057247d3d62f3b71472c65a49d46f67d35fb0d66e3f8673` |
| `F/local/left42_final/central42_kernel.py:144–205` | Different cache key and signed Gaussian branches; final correction signs | `d025529aa2690c3cfc0f1c34a6af385d6fa69db8e069543057f29475cbb133c3` |
| `F/local/central42_v2/tiny42_normalization.py:33–78` | Positive span and probability domains; fixed, nonnegative Gaussian constants | `3650f39f618def7615d8be20ce8b9efd28e16202102fb8fa76dd8687deff4a6c` |
| `F/local/central42_v2/central42_contract.py:17–31` | Closed increasing noise bands and explicit producer grid arguments | `de30acd375d9d53d6a7068cd4b5397da6c775c21be29aca2e5c6b5da5f65a39f` |
| `F/local/left42_final/central42_contract.py:17–31` | LEFT band thresholds, phase radii and grid arguments | `10868c085cf69e6a0b1db01b6bcf638e2a13863db088bc966754ae44c22e2167` |

The proof source `work/toward40_20261007/audit43/capsule/proofs/local42_improvements.tex`
(SHA256 `1a634793af259cccd31cfb86cae8127be0af8bed15559b59d6baaf3f5f8215f6`)
was read at194–198 and209–216 for the sign clamp and conservative cache.
The transcription in `paper/analytic-supplement.txt:7474–7511,7652–7699`
was checked for the actual whole-count curvature, its `min(u,c/3)` denominator,
and the pre-floor correction formula. These are supplied analytic inputs;
this review does not independently establish all their probabilistic premises.

The new helper under test is `mathematics/reduction2/2026-10-27/check_local_curvature.py`,
SHA256 `3e3a35c30af20201fc5b3143f40f1439c235b7bfd4dd702f4fa8348356ff70dc`.
The corrected report is `local-kernel.md` at the reviewed head. Historical
run01/default-grid workload claims are superseded there explicitly; their
preserved source snapshot is not confused with the current helper.

## Independent analytic derivation

Use `b` as the source count-parameter ceiling, not a reflected probability.
For `1/2<c<=1` and `u` in a closed subinterval of `[-1/2,1/2]`, split

\[
f(u)=r(u)+g(u)=\frac{(b+u-1)_+}{(c-u)^2}
 +\frac{(b+u)_+}{[c+\min(u,c/3)]^2}.
\]

The two denominators are positive. Partition at `-b`, `1-b`, and `c/3`.
On a piece where `r` is active,
`r''=2[3(b+u-1)+(c-u)]/(c-u)^4>0`. If also `u<c/3`,
`g''=2(3b+u-2c)/(c+u)^4>0`, since `b+u>1` implies
`3b+u-2c>3-2u-2c>=0`. Above `c/3`, `g` is convex piecewise linear.
Thus pieces with active `r` have maxima at their boundaries.

Where `r=0`, `g` is zero, increasing linear, or the smooth function
`(b+u)/(c+u)^2`. In the last case its derivative has the sign of
`c-2b-u`, so the only possible interior maximum is `u=c-2b`.
It has positive numerator exactly when `c>b`; it belongs to this smooth
region only when `u<=c/3` and `u<=1-b`. Its value is `1/[4(c-b)]`.

Each kink has an upward derivative jump: at the positive-part activations,
the entering derivative is positive; at `u=c/3` the jump is
`2(b+u)_+/(c+u)^3`. Such a kink cannot create a strict interior maximum.
Constant pieces introduce no missing maximum. Consequently the two outer
endpoints and the eligible stationary point suffice. Equality at a kink,
singleton interval and `c=1` are included by continuity. This also verifies
the helper's stationary eligibility inequalities and exact attained value.

For each old subinterval `[a,d]`, both numerators are bounded at `d`; the
first denominator is minimized at `d`, the second at `a`. This gives exactly
the two terms at native kernel163–166, proving pointwise domination of the
old grid bound. The argument covers all real `b`, not just tested table values.
The additional native gate `b+u<2` remains necessary for the whole-count
probabilistic inequality, even though the scalar supremum helper does not
need it. All other positive-domain gates likewise remain.

## Cache, mass direction and the zero clamp

The CENTRAL cache key is `(pi,hj,outerl,outerh)`; LEFT additionally includes
`bi`. For a fixed CENTRAL key, `b=pu-min(H/ell)` is independent of the noise
band. Increasing lower noise endpoints decrease
`d_L=d0*(1-L/Lambda)` and increase `c=1-d_L`. Both positive denominators in
`f` increase with `c`, so its supremum decreases. The first populated cached
entry therefore remains outward for every later occurrence of that key,
including if earlier cells were skipped by `cap<=0`. The new exact helper
may be computed per band or cached in this same order; arbitrary reordering
is not justified. The third-root term and other `c`-dependent quantities
outside the cache must still be recomputed as in the actual kernels.

At each fixed positive noise cell, direct source inspection gives

\[
B(\lambda)=z+\frac{q}{a\lambda+G^2}+s\lambda-t,
\quad q\ge0,\ a>0,\ s\ge0,
\quad I(\lambda)=A_0+A_1/\lambda,\ A_1\ge0.
\]

The marked kernel, `z`, `cap`, Gaussian coefficients and harmonic terms are
fixed before varying `lambda`. On CENTRAL the inverse coefficient is the
nonnegative `normal*a`. On LEFT source196 explicitly requires nonnegative
signed Gaussian coefficients; the negative-phase variance and denominator
gates at191–192 are retained. Curvature changes only `A0`.

The event bracket must remain negative to replace the actual binomial mass
by the positive **lower** mass bound `m`. For negative `B`, actual mass
`m_actual>=m` gives `m_actual*B<=m*B`. Reversing this bound or dropping the
event sign would invalidate the estimate. The proposal correctly keeps
`B<0` and all mass/domain gates.

For the floor change, the valid inequality is

\[
I_{new}(\lambda)/n\le\max(0,I_{new}(\lambda))/N\quad(n\ge N).
\]

It holds by separate cases on the sign of `I_new`. Without the clamp it is
false for negative `I_new`. Both `B` and `max(0,A0+A1/lambda)` are convex
on positive noise. Therefore the negative-event and final score upper bounds
are controlled by their two noise endpoints, including an interior zero of
`I_new`. If the old endpoint passes `I_old>0` and the unchanged strict target,
then `I_new<=I_old` implies `max(0,I_new)<=I_old`; the same strict target
survives. This is a new mathematically justified gate, not permission to turn
off the old literal `inverse_n_positive` assertion without a new contract.

## Executable and coverage checks

The independent program partitions the phase interval at every kink and
checks each smooth piece, evaluating a stationary point directly when it
lies inside such a piece. This differs from the constructor's reduced
three-candidate algorithm. On8,505 rational parameter/interval combinations,
including arbitrary negative/large `b`, `c` just above1/2, `c=1`, all phase
endpoints and singleton intervals, its exact maximum agrees with the helper.
Every reported helper candidate is also checked to lie in the interval and
attain its stated value. This finite check supplements the derivation above;
it is not the reason for continuous coverage.

Three in-memory copies of the **new** helper were deliberately corrupted:
omit the stationary candidate, change its value, or remove the denominator
truncation. All disagree with the independent oracle on explicit rational
examples. Four further exact counterexamples reject an unclamped negative
correction, either wrong use of the mass bound, and reverse-order cache reuse.
There are also180 rational Jensen checks of the clamped final score.

The manifest grid/label reconstruction is independent of constructor counts:
CENTRAL row0 minus uses32/16 H/outer cells, its other77 configurations16/8,
and all74 LEFT configurations8/4. The original152 labels occur exactly once.
Using the literal resource noise ceilings and closed1/400-spaced bands gives
43,136 potential CENTRAL cache keys and77,952 LEFT keys before empty-cell
pruning. Thus7,749,632 old candidate evaluations versus at most363,264 new
ones is a correct **potential count**, not observed work or a time estimate.
The reduction is limited to curvature cache misses; no row, sign, phase,
noise domain, native task or base-case provider is removed by this result.

The corrected constructor diagnostic was separately reproduced with the
same stdout SHA256 `f50972b9da86850f19e5b8540eb7f6823cff4f02cd4468848241f84582a6184d`.
It reports3,648 selected calls,62,942 rational point diagnostics and2,997
strictly improved bounds. This reproduction is not labeled independent
mathematical verification. The two fresh review receipts are:

* `runs/reduction2-20261027/review-curvature01/receipt.json`: independent
  program, source/input hashes, Python3.9.6, return code0, empty stderr.
* `runs/reduction2-20261027/review-curvature-constructor01/receipt.json`:
  reproduction of the new bounded constructor diagnostic only.

Both use repository-relative commands and preserve stdout/stderr separately.
No archived program was imported, no Poisson/LOW score gate was run, and no
certificate-generation or complete native replay was attempted.

## Findings and integration limits

There are no blocking findings in this bounded review. The corrected
manifest-based workload interpretation at `edcb751` is necessary; the earlier
default-grid counts must not be presented as actual producer workloads.

The exact helper and clamp change output values, gate summaries and digests.
They therefore cannot be silently inserted into an adapter promising the
old byte-identical outputs. A future implementation needs a named new
acceptance/output contract and its own independent integration review.
Combining it with separately proposed resource-row pruning likewise requires
checking that new cover and every join; the present review does not add
independent component savings together automatically. The original same-law
acquisition, support/confinement, analytic whole-count inputs, strict local
comparison obligations and finite-base closure remain outside this result.
