# Independent review of the global composition and savings boundary

**Recommendation:** the proposed first-failure composition is logically valid
as a conditional theorem from a genuine weak BASE41, the scalar recurrence,
critical-value attainment and an equality-compatible uniform LOCAL42
exclusion. Its conclusion is strict for every index at least 42. The
`238 -> 171` figure is a correct conservative count within the existing
finite-tail task inventory, before new checks/joins and base obligations.
It is not a proved reduction in total proof work or runtime.

Reviewed starting commit: `90ec7c586caad2abbb93fca599a8bf1169943ffa`.
This report was prepared on the separate branch
`simplify/review-composition-20261027`. The additional grouped-support note at
commit `65c1beb002988a6ceefdfcc2d067def6eedfa80e` was read for its interface
and claimed scope; its coefficient certificate is reviewed separately.

The reviewer authored `uniform42.md`. Accordingly, this report treats its
uniform exclusion statement as an explicit premise and **does not claim an
independent review of its derivation**. The independently reviewed material
here is the logical composition, how its hypotheses are supplied, the scope
of the count, and the remaining provider-closure boundary.

| Result | Mathematical status | Execution status in this review |
|---|---|---|
| BASE41 and the named uniform exclusion imply strict tail from 42 | Independently derived conditional implication below | No numerical/native run required or performed |
| Equality and both deleted predecessors are covered | Exact quantifier and source-interface check | Source text read, including critical-value attainment |
| 238 current runnable finite-tail tasks versus 171 conservatively retained tasks | Exact static inventory count | JSON/source reads only; no tasks executed |
| BASE41 and all uniform LOCAL42 premises are established | Not claimed by this review | Current base provider closure and full numerical acceptance remain unresolved |
| Grouped support removes the old finite support signs from the alternative support proof | Separate proposed certificate interface | Note read; no grouped checker run or certificate acceptance here |

## 1. Precise abstract implication

Let `c=C_E` and `C_n` be the supremum over all standardized iid laws with
finite third absolute moment, at the actual index `n`. Assume:

1. **BASE41:** `C_j<=c` for every integer `1<=j<=41`.
2. **Scalar input:** `c<41/100` and, for every `n>=2`,

   \[
   C_n\le\sqrt{\frac n{n-1}}C_{n-1}
       +\frac{\sqrt n}{15(n-1)^{3/2}}
       +\frac{2\sqrt n}{25(n-1)^2}.
   \]

3. **Attainment/orientation:** when `C_n>=c` at a fixed index under
   consideration, it has an unrestricted positive closed-discrepancy
   maximizing witness, with the retained contact hypotheses. The supplied
   statement explicitly includes equality at
   `paper/analytic-supplement.txt:215–250`; this source theorem remains an
   analytic premise of the composition.
4. **U42:** for every actual `n>=42`, no such maximizing witness satisfies

   \[
   0\le C_n-c\le .54/n,\qquad C_n<.4226,\qquad
   C_{n-1},C_{n-2}<.4253,\qquad n(C_{n-1}-C_n)_+=0.
   \tag{U}
   \]

Here U42 means the complete equality-compatible uniform zero-decrement
LOCAL42 implication, including all its named analytic and numerical
premises. It is not the original finite theorem whose range ends at 48.
The relevant assumption interface is `uniform42.md:331–369`; its internal
proof is outside this review's independent scope.

Suppose the set `{n>=42 : C_n>=c}` is nonempty, and choose its least element
`n`. This uses only well-ordering of the integers, not an eventual positive
ceiling, a later bound, a slow-decrement search or an attained maximum over
indices. Both predecessors satisfy `C_(n-i)<=c`, for `i=1,2`:

| First contrary index | First predecessor | Second predecessor |
|---|---|---|
| 42 | 41 is in BASE41 | 40 is in BASE41 |
| 43 | 42 is strict by minimality | 41 is in BASE41 |
| at least 44 | both are at least 42 and strict by minimality | same |

Weak predecessor bounds suffice. They give

\[
n(C_{n-1}-C_n)_+=0,\qquad
C_{n-1},C_{n-2}\le c<.41<.4253.
\tag{1}
\]

Write `s=sqrt(n/(n-1))`. Multiplying the scalar recurrence by `n` and
using `n(s-1)=(n/(n-1))/(s+1)` yields

\[
0\le n(C_n-c)\le\frac n{n-1}
 \left(\frac c{s+1}+\frac s{15}
                  +\frac{2s}{25\sqrt{n-1}}\right).
\]

For `n>=42`, `n/(n-1)<=42/41`, `s<81/80` and `sqrt(n-1)>6`.
The strict square-root bound follows from
`41*81^2-42*80^2=201>0` and the decreasing ratio. Thus

\[
0\le n(C_n-c)
<\frac{42}{41}\left(\frac{41}{200}+\frac{27}{400}
                                  +\frac{27}{2000}\right)
=\frac{3003}{10250}<\frac3{10}<.54.
\tag{2}
\]

Also

\[
C_n<c+\frac{.3}{n}<\frac{41}{100}+\frac{.3}{42}
=\frac{73}{175}<.4226<.4247.
\tag{3}
\]

The reserves are `36/5125` in (2) below `.3` and `191/35000` in (3)
below `.4226`. The endpoint42 envelope is a separate valid bound; the
`253/250` square-root estimate used for floor43 is invalid at 42. These
facts agree with `finite-entry.md:66–74` and the separate executable review.

Equations (1)–(3) supply every scalar hypothesis of (U). Attainment supplies
its actual witness at this same fixed index. U42 gives a contradiction.
Therefore `C_n<c` for every `n>=42`. Combining this with BASE41 gives the
weak global upper bound `C_n<=c` for every positive integer.

The terminal pair `C_40,C_41<=c` alone suffices for the strict-tail statement.
The full prefix is required to assert the weak bound at all smaller indices.
No new reason to discard the smaller-index providers follows.

## 2. Equality and same-law conditions that must survive the join

Choosing the least index with `C_n>c` would prove only a weak upper bound.
The set above intentionally includes equality. Equations (1)–(3) remain
valid when `C_n=c`; no division by its excess is used. The contact/witness
input and local exclusion must therefore include this case. A strict-only
attainment lemma would be insufficient as the only source for this join.

At the chosen maximizing law `P_n`, its own predecessor score is at most
the global `C_(n-1)`. Hence the positive part of its predecessor decrement
is bounded by the global decrement in (1) and is zero. This licenses the
zero-loss support theorem for this law; it does not replace the law by an
optimizer at `n-1`. Laws at different indices may be different.

Zero predecessor decrement is **not** zero conditional variance or zero
moment defect. The join must retain the following interfaces of U42 rather
than infer them from (1):

- Actual initial support, ordered subsequent contractions and the preceding
  same-law moment bounds for every support call, including both exterior
  signs and all thresholds/atoms.
- Complete initial and complementary probability exclusions; the surviving
  left and central local rows alone do not cover all laws.
- Weighted `nD<=42D_row`, the common joint inward/noise inequality,
  coherent sign-specific phase quadratics and corrected curvature.
- Both deleted indices in concentration, strict antichain widths, the
  floor42 confinement parameters, and proof of each amplitude before using
  its resulting radius in feedback.
- Full closed noise/phase coverage and actual row ceilings; signed Gaussian
  and cubic repairs and their denominator/sign gates before replacing
  inverse-index factors by their floor42 bounds.
- Arbitrarily small positive noise in TINY and the separate exact
  zero-noise Bernoulli conclusion. A positive-noise comparison does not
  establish the zero-noise endpoint by an unproved limit.

These are explicit remaining inputs, not conclusions independently certified
by this integration review. `local-cover.md:65–218` details their source
interfaces. The reports' status distinctions correctly prevent a small
scalar/algebraic PASS from being promoted to full LOCAL42 acceptance.

The global **upper** conclusion also differs from optimality of the universal
constant. The latter still requires the separate lower-approximation input.
`mathematics/global-contract.json.lower` requires that, for every `b<c`,
some integer `n` has `b<C_n`, and explicitly does not assert equality at a
fixed finite index. Strictness for every tail index is compatible with that
asymptotic lower bound. This join supplies no new lower-bound proof.

## 3. Exact meaning of 238 to 171

I directly inspected `verification/finite-tail/TASKS.json`. Its 240 task IDs
split as follows:

| Existing inventory class | Count | Runnable in that inventory |
|---|---:|---|
| finite-native | 31 | yes |
| LOW row | 152 | yes |
| tail-native | 10 | yes |
| tail-mapping | 3 | yes |
| tail-umbrella | 1 | yes |
| tail-retained | 41 | yes |
| finite collectors | 2 | no |

Thus the current runnable component is `31+152+55=238`. The conservative
new component retains `19+152=171` legacy obligations. The 67 conditional
bypass candidates are exactly 12 finite ceiling/bootstrap tasks plus 55
tasks of the separate tail route. The two non-runnable collector IDs,
`61.collect.cutoff44` and `61.collect.cutoff43`, are excluded from **both**
sides of this comparison; subtracting from 240 would be a different count.

The exact 19/12 finite partition is specified in `finite-entry.md:138–169`;
its mapping and target-derived 152 LOW labels were checked in the independent
executable review. This integration review independently checked the outer
238-task decomposition. It agrees with `local-cover.md:230–248`.

The reason for each removed branch is an implication in the new proof:
sharp predecessors plus (2)–(3) replace the finite positive-ceiling ladder
and special backward bootstrap; the complete uniform U42 exclusion replaces
the separate LOCAL47/tail route. No shared analytic lemma is removed merely
because its source file lies in the old tail archive.

Three qualifications are necessary:

1. **Component, not whole proof.** The base, shared upstream consumers,
   lower approximation, new support certificate/transfer, analytic
   applicability obligations and new joins are outside the 171 figure.
   The smaller sharp base through41 removes a need for sharp42 as a logical
   premise of this tail, but the current floor40 provider may package40–42
   together; no executable savings inside that provider has been proved.
2. **Inventory, not measured cost.** The classes include mapping and
   umbrella tasks as well as arithmetic and retained child executions.
   Different tasks have different costs and overlap in evaluation. The
   separate opportunity to avoid duplicated LOW evaluation is not included
   in the 67 count and has not been implemented.
3. **New composition, not an existing accepted run.** The current runner
   still demands 152 producers plus31 native acceptors
   (`verification/finite-tail/replay.py:104–117`), and the tail-full branch
   still checks14 top-level plus41 retained executions (:100–103).
   Neither old collector nor final global provider is relabelled by this
   mathematical argument.

The grouped-support note at commit `65c1beb` offers a different proof of the
same support-radius interface using14 intervals,672 coefficients and84 ray
signs. Conditional on acceptance of that certificate and the analytic
envelope, old finite support sign predicates can cease to be premises of
that alternative support proof. The stored65 call descriptions then identify
parameters and order; they are not numerical sign evidence. This does not
remove64 same-law resource acquisitions or152 LOW rows. This integration
review does not alter the conservative171 count to claim an additional
runner-level saving from that certificate.

## 4. Why the base/provider boundary is still open

`base-closure.md` distinguishes a new mathematical parent contract from the
old executable graph. I directly checked the corresponding primary text:

- `paper/analytic-supplement.txt:9241–9307` states a new conditional
  floor40 interpretation for actual40,41,42. It assumes strict failure at
  the current index and consumes genuine weak38/39, then weak40/41 in
  sequence. A strict-failure contradiction is sufficient for this **weak**
  base induction; it is not the equality-inclusive strict-tail argument.
- The actual remaining inputs at :9473–9497 include the independent
  high-rho complement, ten original acquisition component meanings,
  indexed initial support, all304 LOW row passes, two binders and nine
  comparison companions. Initial support alone is not the base theorem.
- `paper/main.tex:434–443` separates this floor40 component from the
 183-parent finite43–48 component. The 152 LOW rows in the new tail do not
 replace the separate304 base rows.

The nominal provider
`current4042_low_mathematical_assembly_v2.py` is required by
`mathematics/global-contract.json` and pinned there to
`aa819f3fff77d4cdad2b7a8b5c69be2719b8e9df26c85ba5041aa7c0b8bd2d7b`.
Its body is absent from this inspected checkout. The contract similarly
names the current26–39 provider; a declared filename/hash does not expose
either full parent graph. The contract's `production_acceptance_claimed`
field remains false.

There is concrete contrary evidence against assuming that an old join is a
drop-in independent base provider. The old62F graph in
`source/original/proof/finite4348_source_action_plan.json:6976–7078`
explicitly consumes `tail43`, `early`, and `single39`, among other parents.
Those dependencies cannot be silently removed by quoting the new mathematical
A17 statement. Conversely, their existence does not refute the new conditional
induction; the new provider must implement and prove the different parent
contract. This distinction is correctly made in `base-closure.md:99–124`.

To turn this result into a closed global proof or a total execution saving,
the exact current BASE41 providers and their upstream sharp38/39 inputs must
be inspected and accepted, and any remaining consumers of the candidate
bypassed tasks must be retained. The same applies to the independent high-rho
branch and the lower approximation. A lack of current provider closure is a
blocker for an **unconditional global acceptance claim**, not a flaw in the
conditional implication proved in Section1.

## 5. Review findings and work actually performed

No blocking defect was found in the abstract composition, equality treatment,
endpoint42 predecessor logic or qualified238-to171 count. The final synthesis
should present the strongest proved conditional statement as “BASE41 plus
the complete equality-compatible uniform zero-loss LOCAL42 implication gives
a strict tail from42,” while keeping BASE41, analytic truth and retained
numerical acceptance visibly separate.

The conservative BASE42/from43 statements in earlier notes are compatible
weaker variants. They should not obscure the stronger endpoint42 result, and
they should not be interpreted as a claim that the original finite LOCAL42
theorem already had an unbounded range.

Actual work in this task consisted of Git/source reads, the displayed
independent logical derivation, static JSON task classification, and checking
the primary attainment/base/provider declarations against the reports. No
new arithmetic checker, grouped checker, native certificate, generator or
external service was run. No merged/published change or certificate deletion
is recommended by this report. It accepts a precise conditional reduction
for review, with the unresolved premises stated above.
