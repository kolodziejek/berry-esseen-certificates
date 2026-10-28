# Direct comparison through lambda = 3/100

Baseline: reviewed fork PR #5 head
`6027b27f85473780eaf90542f490168873de5986`. All outputs are new research
files on `research/counts-v11-20261028`; inherited manuscript/certificates,
reference/history, other branches and external repositories are unchanged.

## Accepted mathematical result

`counts-v11.tex` proves the same strict comparison with the matching Bernoulli
count as the preceding direct theorem, now for **0 < lambda <= 3/100** and
**C >= 2/5**. The remaining hypotheses are unchanged: n >= 42;
p in [2/5,53/100]; conditional centering; absolute noise bound 3/5;
one-sided gaps with total at most 9/125; |H| <= 46/25; and phase in
[-34/125,91/125]. The margin is Delta_C < -lambda/100.

The old theorem allowing every C >= 0 for lambda <= 1/50 is unchanged.
Taking C equal to the sharp Bernoulli constant satisfies the new penalty
restriction. This is an actual iid conditional-law theorem, not an optimization
relaxation or an acquisition theorem.

The key change is to retain the gain in the normalized third moment. Exactly,

    (v+s)^(3/2) (rho-rho_B) >= s (87/250 - 13s/16).

Since C >= .4 and s <= .03/42, the gain C(rho-rho_B) exceeds s=lambda/n.
It lowers the inner normal repair from the previous allowance 2lambda/n
to 3lambda/(4n). A different quartic scale and a switch at r=3t/2 supply
the own-count bound. Negative inner phases use the incoming bound with h=0;
using the positive-phase tail bound there loses the proof.

Six closed phase intervals finish the argument. There is no numerical mesh,
new large polynomial certificate, asymptotic n cutoff, or positive lower
cutoff on lambda. The proof is uniform as lambda tends to zero.

| Item | Mathematical status | Execution status |
|---|---|---|
| The comparison for lambda <= .03, C >= .4 | Locally derived with complete new proof; coordinator and independent component reviews found no blocker | Fresh PASS of 70 rational gates (69 strict, one exact non-strict repair identity) |
| Finite normalization reused from v10 | Previously derived finite Stirling/normal estimates, rechecked at the new endpoint | Hash-pinned source bytes executed; 28 gates selected explicitly |
| Quadratic-hinge Poisson tail comparison | External theorem, Pinelis Proposition 2.8/Corollary 2.11 | Primary source checked in v10; same precise hypotheses |
| Rare-jump and collision controls | Exact actual-law algebra and event checks, not uniform coverage | 18 laws, 72 event cases, 18 own-count collisions, 9 Bernoulli endpoint cases PASS |
| Full .075 extension with compound Poisson bounds | Promising discovery only | 80 finite-n and 80 formal n-infinity sampled cases positive; truncated floating Poisson sums |
| Global acquisition, smaller n, remaining parameter panels | Not established by this component | Not claimed |

## Exact dependencies and proposed removals

Theorem 1 in `counts-v11.tex` uses the exact conditioning identity, finite
Stirling normalization, the conditional cubic expansion, a quartic polynomial
below the strict half-line indicator, Cantelli, and the rational quadratic-
Poisson incoming bound already proved in
`mathematics/simplification-v10/2026-10-28/moderate-noise.tex`.

The external theorem is [Pinelis, On the Bennett–Hoeffding inequality,
Proposition 2.8 and Corollary 2.11](https://arxiv.org/abs/0902.4058).
It allows the total variance to be **at most** the comparison variance and
applies to quadratic hinges. Markov's inequality gives the required closed
incoming event. The outgoing polynomial controls the strict event even at zero.

The direct comparison's domain without half-amplitude confinement, fractional-
part smoothing, marked crossings or count curvature now extends from lambda
<= .02 to lambda <= .03 **at the stated positive penalty**. These downstream
components and their checks are unnecessary for this domain once its incoming
3/5 strip and other premises have been acquired. They remain necessary wherever
another retained branch still uses them. No existing certificate was removed.

Acquisition of the 3/5 strip, the threshold bound and conditional representation
remain independent obligations. The proof does not remove finite Stirling or
the Bernoulli endpoint theorem. It does not cover p outside [.4,.53], n < 42,
or noise above .03.

## Reproduction and source binding

From this worktree:

    python3 mathematics/simplification-v11/2026-10-28/counts-v11-check.py
    python3 mathematics/simplification-v11/2026-10-28/counts-v11-actual.py

The checker reads the v10 source bytes, verifies SHA-256
`13c4c27a66cb692a5ac480a986e8240a8ab38b59c066cb3f24d81d9676a13f11`, then
uses `compile`/`exec` in an isolated namespace. It does not load Python bytecode.
Retained gates are named explicitly rather than selected by output order.

Final theorem source SHA-256:
`209f173c19a73c4fecf5aaf9aa2732c30b72266ff3f1673ddd52fa4a4e6c4641`.
Final checker SHA-256:
`dfeba7bc10dcdcd41bdfde30c415239f5776434acf36415a919339db0a928225`.
Final actual-law checker SHA-256:
`ec91e51f8dce07ce7ff4d7b338c519153c6e982712dc147e70b1032174fc94fa`.

Independent review is committed separately in
`f0e306c12e1ab36cde5d226f3e9e1c5d53897f22`. It reproduces all six terminal
residuals, proves the full quartics with 40 tensor Bernstein coefficients,
and verifies 36 actual cubic gains with 144 own-event checks. Its exact
counterexample control confirms that the gain exceeds lambda/n but is
less than lambda for each tested law, detecting the normalization error.

Evidence is in `runs/counts-v11-20261028/accept01/` and `actual02/`.
The negative controls reject removal or reversal of the cubic gain, omission
of its 1/n scaling, an unjustified larger own-count coefficient, use of the
positive-phase incoming envelope on negative phases, and enlargement to .04.
The coverage check rejects a gap, a missing interval, reordering and a duplicate.

The narrowest essential new per-lambda terminal surplus, after allowing the
target lambda/100, is

    19650157/2820720000 > 0

on the negative inner phase interval. Other exact terminal margins are printed
in the checker output and in the proof. Every count-mass multiplication uses
a bracket already proved positive.

The full TeX note compiles to four pages in `build02/`. The final compiler log
has no warnings or overfull boxes; all four rendered pages were inspected.
The first compilation failed on TeX parsing of an array row beginning with a
square bracket after a line break; braces fixed that formatting issue.

The initial actual-law run also rejected a test input: choosing floor(np)
put one collision threshold outside |H| <= 1.84. Choosing the nearest integer
count keeps every tested input inside the stated threshold domain. The failed
run is preserved, and `actual02/` is the passing run. No theorem condition or
acceptance assertion was weakened.

## Neighboring outgoing counts and the remaining obstruction

A neighboring outgoing count need not contribute at all. For example take
n=42, p=1/2, U_1=0, and U_0 supported on {-3/5,1/420}, with its unique
centered probabilities. Then lambda=3/100, k=21, u=0, H=0. The sum W_(k-1)
has maximum 22/420=11/210 < 1, so

    P(W_(k-1) > 1+u) = 0.

All strip/slack premises hold. Thus no strictly positive distribution-free
neighbor correction can be inferred from those premises alone. The exact-law
controls include 36 zero-neighbor cases and 36 cases with a positive neighbor.
The successful .03 argument instead uses the cubic gain and still discards
all other outgoing counts.

The separate exploratory scripts preserve the next possible route. The
support-specific fourth/third-moment coupling is proved in the independently
constructed `owncount.tex` component. Keeping conditional variance allocation
prevents pairing an adverse own-count skewness with an incompatible incoming
tail. For a fixed quartic and a fixed split Bennett tilt, the resulting lower
margin is concave in that allocation, so its endpoints suffice. However the
common-tilt Bennett envelope was too loose in the bounded 360-case exploration;
see `discovery01/`.

Replacing that envelope by a quadratic hinge of the **two-jump-size compound
Poisson** comparator was positive at all 80 tested points at lambda=.075,
n=42, negative phase in [-.15,0], and allocations 0,.25,.5,.75,1. The worst
sampled margin was about .00538. The 80 formal n-infinity points were also
positive, worst about .00890. Evidence: `compound-discovery01/` and
`compound-limit01/`. These are truncated floating sums and endpoint samples,
not continuous-domain certificates or a uniform-in-n proof.

A useful next evaluator would condition on finitely many large Poisson jumps,
bound the small-jump quadratic hinge by a full second moment or an exponential
bound, and use factorial moments for the remaining large-jump tail. Continuous
allocation/noise/phase coverage and the finite-n normalization still have to
be proved. This turn does not claim that extension and launches no larger
certificate campaign.
