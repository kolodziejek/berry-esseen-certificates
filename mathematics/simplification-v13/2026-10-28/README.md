# Cancellation before counting

The most useful change in this round is an exact way to combine the conditional
counts before estimating them. The resulting loss is nonnegative throughout
the acquired noise range. A second argument reduces that range from
lambda<.616 to **lambda<.36** using only inward displacement and third moments.
Neither result completes the sharp iid Berry–Esseen conjecture.

Start with [the three-page crossing proof](crossing.pdf) and
[the four-page geometric proof](geometry-noise.pdf). They are complete proofs
of their stated implications. The manuscript is unchanged.

## What is proved

| Result | Mathematical status | Execution status |
|---|---|---|
| All conditional counts combine into an exact nonnegative crossing loss | Locally derived and independently checked; both conditional laws may have noise, with the explicit separated-support and upper-width hypotheses in crossing.tex | 109 exact constructor cases; independent 366 actual-law/threshold cases and 9,192 checks, including atom boundaries and weighted summation by parts |
| Inward-cubic geometric budget; global lambda<.36, left lambda<.32 | Proved implication from the retained coarse budget and actual central gap; no outer-strip or heat input to the new inequality | 139 positive rational Bernstein coefficients, independently reconstructed by interpolation; 22 constructor gates; 832 actual-law budget controls |
| Finite-index probability localization | Same geometric implication: p<=1/3 forces n<=168, p<=.4 forces n<=3598 | Exact rational endpoint comparisons; no finite-index theorem is inferred from localization |
| Ordered-count concentration and analytic binomial curvature bound | Locally derived; coordinator independently checked the proofs | 32 actual-law cases, 160 curvature and 96 interval controls |
| Symmetric central comparison, even positive n, any positive noise | Complete scoped direct comparison for p=.5, reflected conditional laws and a small explicit central threshold interval | Three exact symmetric controls; no claim for general laws or thresholds |
| Four-summand moment endpoint shortcut | Refuted by an exact actual iid five-point example, not a counterexample to Berry–Esseen | 374 finite checks, including complete quartic reconstruction and rejecting controls |
| Contact forces active support collisions | Proved conditional statement for finite atomic laws with a global contact potential | Exact moment and collision controls; contact and finite atomic support remain premises |
| General weighted comparison and independent finite base through 41 | Open | No acceptance claimed; no expensive generation campaign |

## Why this may shorten the proof

For independent conditional-noise pairs, put

\[
T_j=j+\sum_{i\le j}U_{1i}+\sum_{i>j}U_{0i}.
\]

The inward gap makes this sequence strictly increasing. Each count has the
correct conditional law of the original iid sum. For an interior threshold,
let K be the last index with T_K<=t. The actual CDF is exactly E F_B(K).

The useful kernel is

\[
h(x)=E(x-U_0)_+-E(x-1-U_1)_+-P(1+U_1\le x).
\]

It is nonnegative under the theorem's support assumptions. Its expectations
telescope to t−E K. This proves the sign without a count grid, a Poisson
comparison or a limiting argument. A stronger bound retains the expected
truncated distance from the threshold to its preceding mesh point.

Summation by parts keeps the actual binomial weights. The CDF equals the
linear interpolation of the binomial CDF, plus a **signed curvature term**,
minus a **weighted nonnegative loss**. The curvature term has a short uniform
upper bound in [counts-tools.tex](counts-tools.tex). The unresolved step is
quantitative: the weighted loss must absorb that curvature and the phase,
normal and cubic corrections for the same law. A sign alone does not suffice.
The smaller [renewal note](renewal.pdf) is an optional one-sided precursor;
it is unnecessary once the general crossing theorem is used.

The geometric improvement is separate. If Z is centered and Z<=a, then
E Z^3<=a E Z^2−(E Z^2)^2/a. Combining this reciprocal variance cost with the
central-gap displacement cost by AM–GM produces a stronger common-law
budget. Its scalar consequences use only eight polynomials, with eleven
closed polynomial intervals, not a sample-size grid.

## Exactly which computations become unnecessary

| Proposed removal | Justification and scope | What remains |
|---|---|---|
| Count analysis at lambda>=.36 for acquired witnesses | geometry-noise.tex, Theorem 3 excludes it from the retained coarse-entry premises | Coarse Fourier entry and its analytic acquisition ancestors |
| Count analysis at lambda>=.32 on p<=.4; >=.25 on p<=1/3; >=1/6 on p<=.3 | Same theorem, stronger probability-specific ceilings | The remaining smaller-noise domains are not automatically excluded |
| Probability panels p<=1/3 for n>=169, and p<=.4 for n>=3599 | Same theorem's integer-index localization, from D>=Q(p)/sqrt(pq) | Finite indices below these cutoffs; independent BASE41 |
| Detailed count certificates in the symmetric central subcase | counts-tools.tex, Theorem 2: interval concentration plus strict rho>1 proves the full comparison | Even n, exact symmetry, separated supports and the explicit threshold interval |
| Separate incoming-tail estimates in a future general crossing-based proof | crossing.tex supplies an exact alternative formula, with a nonnegative kernel | **Not yet a dependency removal from the accepted general theorem:** weighted absorption is open |
| Endpoint-only optimization on a four-summand moment segment | Cannot be used: finite-contact.tex gives an exact counterexample | Interior stationary points, or a whole-interval quartic bound, must be included |

No existing certificate is deleted. The reviewed v12 general comparisons remain
unchanged: lambda<=.01 on the left and <=.075 on the right. At the sharp
coefficient, the remaining general ranges are left (.01,.32) and right
(.075,.36), subject to the stronger local budgets above. The geometric theorem
permits p up to .54; the retained right count theorem only extends to .53.
No count statement on (.53,.54] is introduced.

## Finite-base obstruction and corrected route

On raw support {-2,-1,0,1,2}, weights
(.05+theta,.2−2theta,.5,.2+2theta,.05−theta) have fixed mean, variance and
absolute third moment. At four-sum threshold 1, the CDF at theta=0 is
25719/32000 and exceeds both endpoint values 4017/5000 and 7921/10000.
The iid objective is quartic along this segment, so a linear moment-extreme
principle cannot remove its interior. The signed third moment is not fixed.

With an actual global contact inequality, every finite support atom except
at most two must participate in an active four-sum collision. A support bound
of six follows only when there is one active unordered multiset. Multiple
collisions and non-atomic compact supports remain unresolved. These are not
disposable degeneracies or measure-zero cases.

## Evidence and review

- [crossing-independent-review.md](crossing-independent-review.md) rederives
  the kernel, selected-noise bias, telescoping, weighted formula and endpoints.
  Its implementation imports no constructor code.
- [coordinator-review.md](coordinator-review.md) records the independently
  reconstructed geometry and the remaining component checks and limitations.
- [geometry-status.md](geometry-status.md) and [finite-status.md](finite-status.md)
  bind component proofs and recorded runs. Counts evidence is in counts-status.md.
- Bounded exploration used 70 larger-noise actual iid laws, and another 115
  crossing diagnostics. These were discovery only. Eight selected full Delta
  events were subsequently checked with exact rational normal/root enclosures;
  event selection was not certified optimization and provides no domain coverage.
- False width-free crossing, zero selected-noise bias, moment-only selected
  reserve and independent-delay shortcuts have exact negative controls.
- Schulz's sharper Bernoulli formula retains its published p in [1/3,2/3]
  scope; the all-p strict Bernoulli theorem is a separate statement. The
  geometry note links and checks the primary source.

From the checkout root, run `python3 -I -B
mathematics/simplification-v13/2026-10-28/run_checks.py NEWID` with a fresh
alphanumeric identifier. The driver records sources, interpreter, command,
stdout, stderr and return code, and rejects modified reviewed sources.
Assertions remain enabled. It does not run discovery or inherited generation.

The selected 11,264-cell coarse Fourier entry, attainment/reflection, relevant
contact and sharp-predecessor acquisition, external theorems, and independent
finite base remain explicit obligations. This is research progress for the
existing draft PR5, not a completed sharp-conjecture paper or a merge request.
