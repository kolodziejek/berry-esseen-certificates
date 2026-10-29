# Independent review of the larger-index comparison

**Outcome: no mathematical blocker found at the stated scope.** The theorem
is a direct all-law comparison in the acquired right strip, for n>=6000 and
`.075<=lambda<=.36`, with signed improvement `Delta_C<−lambda/200` for every
C>=0. It is not an unconditional sharp Berry–Esseen cutoff theorem.

Reviewed source: `mathematics/simplification-v14/2026-10-28/large-index.tex`,
SHA256 `ad48f1eae57817b955016c6a12114e3929852a3e636afcfbb91646697b4c6509`.
The complete reviewed bytes are preserved in the final review run. This
review was made on a separate branch from baseline
`656232ea8d9561a3f47aefa083ead4f6ba4206ca`; it does not edit the constructor.

| Result | Mathematical status | Execution status |
|---|---|---|
| Selected-to-fixed-count transport | Independently rederived, with correct omitted-pair independence and full tails | Independent rational coefficient below12 verifies the source's bound 13; exact product controls PASS |
| Characteristic-function and clipped-age gain | Independently rederived on the whole support-width interval | Two closed trigonometric regions and all scalar guards PASS; positive actual-variance gain controls included |
| Window tail and binomial weight restoration | Independently reconstructed fourth moments, full tails and finite Stirling bound | Rational tail, mass and positivity gates PASS |
| Phase, normal-variance and actual cubic corrections | Independently rederived with the full1/n scaling | Reconstructed integrated polynomial and final margins PASS |
| Acquisition join nd<3 | Valid implication from the stated actual central-gap budget and right strip | Independent positive-price and variance-ratio gates PASS |
| Main n>=6000 comparison | Accepted as a complete scoped derivation with retained external inputs | 40 independent rational gates; no n6000 convolution is claimed |
| Global acquisition, reflection, attainment and BASE41 | Not proved by this review | No global or finite-base acceptance |

## Transport and selected-count conventions

Source lines 91–126. Let `D_i=U1_i−U0_i` and remove pair i to form V_i.
Centering and the one-sided caps imply `E|D_i|<=2d`, while
`Var(V_i)<=2.5lambda<=.9`. The events used in the proof are exactly

- `K>=i` iff `T_i<=t` for i>k;
- `K<i` iff `T_i>t` for i<=k.

Replacing U1_i by the relevant support endpoint makes the enlarged event
depend only on V_i. Only then is independence used to multiply its probability
by `E|D_i|`. The source never asserts independence of a stopped count and its
increment. Both complete Chebyshev tails are included.

As an independent reconstruction, using zeta(2)<5/3 gives the coefficient

    2 [3 + .9 {(5/3)/(.928)^2 + (2/3)/(.7)^2}] < 12 < 13.

The right tail uses `r−1−d >=.928(r−1)` for r>=2. The left tail uses
`r−.6>=.7r` for r>=2; r=0,1 are handled separately. This is a different
summation bound from the source's integral remainder and confirms its 13d
constant without changing the theorem or optimizing its cutoff.

A potentially dangerous alternative was checked and rejected: E W_K is
usually nonpositive, while E W_(K+1) is nonnegative. Therefore one cannot
replace g by an uncorrected mean age. The source instead uses the previously
proved **clipped-age** inequality, which already contains the selected bias.

## Characteristic function and weighted loss

Source lines 128–224. The width of each conditional noise law is at most.672,
so independent copies differ by at most that amount. The proof of
`1−cos(2pi x)>=3x²` covers both closed intervals [0,2/3] and [2/3,.672]
and then uses evenness; the positive sine lower bounds have the correct
squaring direction. This implies
`|phi_Z|<=(1+3Var(Z))^(-1)`. Multiplication retains the same conditional
marginals and yields `|phi_Wk|<=(1+3t_k)^(-1)`.

The relation `t_k>=(1−5/n)lambda>=37lambda/42` follows from the physical
count multipliers and `|k−np|<2`, with p,q>=.4. No randomized allocation or
independent moment optimizer is substituted.

The pointwise inequality
`min(r,.328)>=.3 sin²(pi r)` holds for every r>=0. Thus the clipped-age loss
bounds `.15(1−|E exp(2pi i W_K)|)`. Characteristic-function transport costs
at most `.3pi E|W_K−W_k|`, which is smaller than the transport bound itself.
It is paid only once. This resolves the possible double-spending of the
selected-mean bias. The resulting lambda/5 gain is valid throughout the
stated noise interval.

The discarded |i−k|>10 window uses the actual support of h, a uniform bound
h<=1, the full fourth-moment estimate and both complete inverse-fourth-power
tails. The retained window has positive total loss at the worst stated
n and lambda. Its integer counts are interior, and finite Stirling gives
`sqrt(n) pi_i>3/4`. Multiplication by the nonnegative g_i is justified.

## Phase, cubic correction and acquisition

Source lines 226–322. The curvature coefficient c<.46 uses the tighter raw
bound `1.84*.501−.47<.46`; it would not follow merely from the rounded
`|t−np|<.94`. The exact scalar gate checks the tighter expression.

I rederived the phase log-ratio. The negative factor x−1 reverses the
replacement of the lower phase endpoint correctly. Its integrated numerator
is the cubic

    (2a−1)u +(2−a)u² −(2/3)u³,  a=.94.

Its derivative is concave and positive at both endpoints of [0,1], so its
maximum is attained at u=1. The mass remainder, density, exponential and
normal-variance corrections retain their stated 1/n factors, yielding P<5/n.
The scalar reconstruction uses an independent Machin enclosure for pi.

The absolute-third-moment expansion has the correct signs
`−q mu0+p mu1`. Inward endpoint bounds leave a raw gain at least 1.128s;
the Bernoulli normalization costs at most `.78s+(13/16)s²`. Consequently
rho>rho_B throughout the positive-noise theorem, independently of C>=0.
The final rational relative margin remains strictly above 1/200.

For the acquisition join, the actual-gap inward expansion has positive
noise prices on the right strip, and all discarded terms are nonnegative.
Thus `nD>=6nv d(1−d)/(v+s)^(3/2)`. Independently,

    (v+s)^(3/2)/v < .501(1+1/4000) < .502,

which, with nD<=129/4 and 1−d>=.928, gives nd<3. This is a conditional join,
not a proof of the coarse entry or actual-gap acquisition. It uses the
actual inner endpoints; arbitrary loose support caps are not identified
with an actual central gap.

## Exact product controls and limits of the checks

`large-index-review-check.py` imports no constructor code. It rebuilds the
scalar gates from domain endpoints and enumerates independent conditional
pairs at n=2,3,4. Five conditional-law designs include both noisy sides,
each pure allocation, symmetric tiny noise and the zero-noise boundary.
Thresholds include actual mesh atoms and immediate rational neighbors;
both p=.4 and p=.53 are recorded.

The 150 controls correspond to 75 distinct mesh/threshold calculations.
They directly compute K, selected transport, g, clipped age and E W_K,
and verify the actual-variance CF/transport lower expression. There are 22
atom cases, 33 nonzero selected-mean cases and 22 strictly positive lower
expressions. They also test the requested lambda/5−13d bound. The record
marks whether the theorem's fixed-variance ratio happens to hold at each
small index. These are sanity checks of internal formulas, **not coverage
of the n>=6000 theorem** or evidence for changing that cutoff. Zero noise
uses a non-strict transport check; the main theorem has positive noise.

Final evidence: `runs/large-index-review-v14-20261028/check03/`, including
source snapshot, command, interpreter, return code, stdout, stderr and hashes.
`check01` retains a reviewer-script syntax error, corrected before execution;
`check02` correctly rejected a changed source hash. The final source change
only added explicit definitions of U_j and independent X_i; its exact diff
is saved with check03. The final run passes all 40 rational gates and 150
product controls. The reviewer did not run the constructor checker as a
purported independent verification.

The reviewed proof may replace larger-noise count exclusions for the stated
acquired right strip when n>=6000. The smaller-noise join still uses v12;
left probability exclusions still use the retained geometric or Bernoulli
arguments. No new statement covers p in(.53,.54] without its separate
probability acquisition. Remaining finite indices, BASE41, actual contact,
sharp-predecessor acquisition, attainment and reflected-branch hypotheses
remain explicit. No certificate or manuscript source was changed.
