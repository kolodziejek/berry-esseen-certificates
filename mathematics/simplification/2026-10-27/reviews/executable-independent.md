# Independent executable and coverage review

**Recommendation: accept the reviewed additions as conditional algebra,
binding and inventory results. No correctness blocker was found in that
scope. They do not constitute acceptance of the inherited LOCAL42 numerical
predicates or of a global Berry–Esseen theorem.** Two nonblocking hardening
limitations are documented below with fresh mutation evidence.

Reviewed commit: `341c1e3f77806a4aaa178051f6f8c80c13bd63ac`, in the separate
worktree/branch `simplify/review-executable-20261027`. The review concerns
`check_support_lift.py`, `zero-loss-support.md`, `check_finite_entry.py` and
the executable/coverage claims of `finite-entry.md`. The reviewer did not
author these checkers. The reviewer did author `uniform42.md`; this report
does **not** independently review or approve that theorem.

| Item | Mathematical status after review | Execution status |
|---|---|---|
| Support-lift polynomial difference and ray constants | Independently derived and checked exact algebra | Both original new checker and independent bounded check passed |
| Initial plus 64 left support inputs | Exact identification and ancestry of fixed archived inputs | Fresh archive reads and exact comparisons; old acquisition/sign programs not executed |
| Endpoint42/43 scalar bounds | Exact conditional scalar consequences of the stated recurrence and `C_E<.41` | Fresh exact arithmetic passed |
| 19 retained native predicates, 152 LOW rows, 12 bypassed predicates | Correct inventory partition for the new conditional composition | Fresh target-derived labels and manifest/source bindings checked |
| All inherited polynomial signs and actual-law resources | Separate premises; not established by these scripts or this review | No archived checker or generator run |

## 1. Sources and unchanged baseline

The reviewed checker hashes are:

```
check_support_lift.py
3cf1ec45f3abc69c308bc9819493d09fd1851c91d67f1ea72384d260e3edf59e
check_finite_entry.py
2279c73727565305817276b4646662b38e967b2e9809e24eed53cfc932050901
```

The current `verification/finite-tail/sources/backend.zip` is byte-for-byte
equal to the blob at preserved baseline
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee`. Its SHA-256 remains
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`.
The finite-entry checker pins manifest SHA-256
`c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`.
The support checker additionally pins the complete archive, the two source
kernels and the left proof object. Neither checker imports archive code.

In source references below, `B` means the manifest prefix
`work/toward40_20261007/audit43/capsule/work/below49_20261006/`.
Logical paths map through `finite61/MANIFEST.json` to
`finite61/blobs/<sha256>`. The acquisition and left-exact copies of both
`heat_support50.py` and `fifth_heat50.py` have identical respective hashes
`650d7f...e18` and `09a6e2...6c`. I read the actual source bytes; I did not
treat the manifest's historical PASS strings as mathematical evidence.

## 2. Exact arithmetic and coefficient checks

`check_support_lift.py:44–50` uses integer square roots on the squared
`10^12` grid. The actual endpoints are

\[
\ell=\frac{800390529679}{125000000000},\qquad
S=\frac{202424330939}{200000000000}.
\]

Direct exact squaring verifies `ell^2<41`, `S^2>42/41`, adjacent grid
endpoints, and `S<81/80`. These are exactly the choices in
`B/acquisition/heat_support50.py:37–42,65`. The initial moment parameter
is `r=7361/4000`, the **minimum** of the two published-bound quotients.
The outer square-root procedure gives
`b=641562334877/10^12`; exact arithmetic verifies
`0<b<2/3` and `(1+b^2)^2>r^2(1-b^2)`. The left override in
`B/package_audit/left42_exact/accept_acquisition.py:37–42` changes only
`r,b`, leaving `c,ell,S` identical. Thus all 65 applications use the same
scale endpoints and zero-barrier constant `c=819/2000`.

The coefficient definitions at checker lines 82–105 agree term-for-term
with `B/acquisition/fifth_heat50.py:15–26`: in particular `J=u^5-15u`,
`D_+=J/(120*41)`, `D_-=J/(120*47)`, `W=A-(15/2)D_+`,
`H4=u^4-6u^2+3`, `B2=H4^2/(256*41)`, and all three adverse remainder
terms use the correct powers of 41 and the lower `ell`. The domination
term is `-H4/(12 ell)`, not `-H4/(24 ell)`.

Subtracting the finite contact expression from the infinite zero-loss
one leaves exactly

\[
\tfrac65S^3D_-W-.19rSW
=SW\left(\frac{S^2J}{4700}-.19r\right).
\]

The adverse remainder and `cQW` cancel. The domination expression increases
by `3D_-W`. I independently expanded the contact difference using sparse
coefficient dictionaries, rather than calling the new checker's list
polynomial functions. The reviewed 130 count is accurate: two identities
for the initial input and for each of the 64 left inputs.

For the splice at `21/5` and initial parameter rectangle
`46/25<=r<=37/20`, `b<=2/3`, the exact domination reserve is
`3679155107/47000000000`. For the splice at `39/10` and left rectangle
`1<=r<=3/2`, `b<=1/2`, it is
`17940880361/3008000000000`. Both are strictly positive. I independently
formed `Q`, differentiated it, formed
`L=(2/5)(u^2/2+1/2+.384/42)+cQ'`, and checked all six reported negative
ray quantities. The bound on `J` is uniform on `[R,U]`, since all radii
are at least `5/2` and `J,J'>0` there. The old closed radial cells cover
the splice even when it lies inside a cell rather than at a grid endpoint.

For the scale correction, independent expansion gives

\[
(1-x)(1+x/2+Ex^2)^2-1
=x^2\{2E-3/4-(E+1/4)x+(E^2-E)x^2-E^2x^3\},
\]

where `E=48/125`. The braces decrease for `0<x<=1/42` and equal the
positive `118707/42875000` at the right endpoint. Both sides being
positive before taking square roots, this establishes the required
`e_n<E/n`. No numerical sampling in `n` supplies this step.

These checks validate the arithmetic used by the new lemma. The source's
contact identity, the signed heat envelope, its denominator/positivity
conditions and the old finite polynomial signs remain distinct premises.

## 3. Coverage and ancestry of the support inputs

The initial source `B/acquisition/check_local42_support.py:7–10` uses
exactly `(42,48,0,96/25,19/100)` and covers 14 adjacent closed cells through
`9/2`. Its fixed manifest row agrees with the independently reconstructed
`r,b`. This row is a source-binding object; reading it does not prove its
sign inequalities.

The left proof object SHA-256 is
`419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393`.
I separately verified its embedded initial-resource and route hashes against
the corresponding archive blobs, all 15 ordered coarse panels, the 11
surviving parents and their five consecutive fine children each, and all
55 final-resource/trace bindings. The first common bridge is at `121/40`.
Every later radius follows the recorded strictly decreasing route and uses
the immediately preceding same-law resource's `rho,beta` bounds. There are
64 left support invocations in total, including the common bridge. Together
with the initial invocation, the checker's reported total 65 is correct.

I also independently checked the old radial cell endpoints, contiguity and
coverage through `9/2` for all 64 left invocations. This is stricter coverage
checking than `bind_left_rows` itself performs. The old native acceptor's
arithmetic comparison at `accept_acquisition.py:69–82`, rather than this
static review, must still establish that each recorded resource actually
comes from its prescribed predecessor.

## 4. Finite entry, endpoint42 and task mapping

Given the stated recurrence and `C_(n-1)<=C_E<=C_n`, the inverse-index
factors decrease for `n>=N`; the square-root endpoint is checked rationally.
The independently recalculated values are:

| Floor | Square-root bound | Excess bound | Reserve below `.3` | Own cap | Reserve below `.4226` |
|---|---|---|---|---|---|
| 42 | `81/80` | `3003/10250` | `36/5125` | `73/175` | `191/35000` |
| 43 | `253/250` | `102469/350000` | `2531/350000` | `1793/4300` | `1209/215000` |

The squared integer surpluses are respectively 201 and 878. Applying the
second bound at 42 would instead give surplus `-631`, so the endpoint42
branch at `check_finite_entry.py:59–67` is a necessary separate envelope.
The finite statement remains limited to actual indices through 48 unless a
separate uniform theorem is supplied. The strict-tail composition chooses
the least `C_n>=C_E`; a least `C_n>C_E` would only establish a weak bound.

The pinned manifest's native action order matches the prose table: its first
six entries are positive-ceiling/support tasks, its next 19 are the retained
LOCAL42 predicates, and its final six are the special43 backward-bootstrap
tasks. I checked their actual script and argument mappings. In particular:

- `44.entry/harmonic_interpolation01` stays among the 19 retained tasks;
- the two confinement/profile modes of the same central script are distinct
  obligations and both remain;
- both LOW binders retain `--replay` in the inventory;
- ordinary zero-barrier initial support is retained; the superficially
  similar positive-barrier `entry/check_support42_48.py` is bypassed.

Reading the actual central and left target JSON, selecting rows with
`lambda_max>.05` and `lambda_max>.08`, respectively, and retaining both
signs reproduces the manifest's ordered list **exactly**: central indices
0–38 give 78 rows; left indices 8–44 give 74; total 152. The native binder
selectors at each `bind_low42.py:22–23` use these same strict thresholds.
There is no missing endpoint or sign introduced by the proposed partition.

This is a count of manifest action/row obligations, not a measured runtime
saving or a fresh numerical acceptance. It is conditional on an independent
sharp base and the retained local analytic inputs. The 12 bypasses are valid
only in that new composition; existing 31-action collectors are unchanged.

## 5. Mutation evidence and nonblocking limitations

Both new checkers passed freshly with empty stderr. The support checker
rejected all its ten named controls; the finite-entry checker rejected all
four of its endpoint/scope controls. I additionally ran seven **temporary
copies of the new support checker**, never changing archive data or existing
source files:

| Copy mutation | Observed result | Interpretation |
|---|---|---|
| `4700` changed to `4701` on the expected difference | Rejected | Difference coefficient is checked |
| Finite upper endpoint changed from 48 to 49 | Rejected | Fixed input scope is enforced |
| Complete-archive pin corrupted | Rejected | Fixed input identity is enforced |
| Select lower rather than upper root for `S` | PASS | Current endpoint is correct, but its orientation is not asserted after assignment |
| Shared `H4` coefficient `-6` changed to `-5` | PASS | A common canceled term cannot be checked by the difference identity |
| Shared adverse-remainder coefficient 51 changed to 52 | PASS | Same cancellation limitation |
| Delete an old radial cell after loading the pinned object | PASS | The helper is not a full old-proof coverage acceptor |

**Low severity, hardening suggestion:** add a direct post-assignment check
`S*S>42/41` and explicit source-definition checks if this script is expanded
into a standalone acceptance boundary. The current assignment and shared
coefficients are correct, as established by direct source comparison and the
independent checks above. The successful mutant copies are not defects in the
current mathematical result; they show why the algebraic PASS cannot replace
the source review. Arbitrary edits to a checker are not an adversarial input
handled by the original fixed program.

**Low severity, scope/provenance caution:** `bind_left_rows` validates the
support parameter bounds and immediate moment ancestry, but not all old
proof-object schema, radial coverage, coarse-to-fine parentage or numerical
resource transitions. The complete archive hash fixes those inputs in the
reviewed program. The independent static ancestry/coverage checks above close
the present identification question, while the old native predicates remain
premises. Do not advertise the ten controls as a general malformed-proof
acceptor or as reacceptance of the old polynomial signs. The current docstring
and JSON scope statement correctly make this distinction.

## 6. Reproduction evidence and limits

The reviewer-owned bounded script is
`mathematics/simplification/2026-10-27/reviews/check_executable_review.py`.
Its receipt, exact independent results, original stdout/stderr, mutation
recipes, mutated-source hashes, return codes and normalized mutation outputs
are saved under `runs/simplification-20261027/executable-review01/`.
The command, working directory and input paths in the receipt are repository
relative. It ran with unoptimized Python 3.9.6 and return code zero.

No archived source was executed or imported, no certificate generation was
launched, and no external service was accessed. The mathematical identities
were re-derived here; this is not independent verification by merely wrapping
the same implementation twice. The original heat/contact theory and actual
local numerical predicates were not re-proved. Their conditional status must
remain visible in any final synthesis or review request.
