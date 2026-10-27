# Integration and scalar-checker review

Date: 27 October 2026. Reviewed PR head:
`ac7bd069c9d5afe6d0dfe5a9c86c9a095644ff99`.
Baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
Review branch: `audit/review-computations-20261027`.

**Recommendation: approve the audit-only change for human review. No blocking
integration or fixed-invocation scalar-checker defect was found.** This is not
approval to merge automatically, delete a proof component, change an existing
theorem, or run an expensive campaign. The proposed global proof remains
conditional on all retained analytical and numerical predicates.

I authored `computations-review.md`. My re-reading of its shared-dependency
findings is therefore **not an independent review of my own report**. This
review independently checks the coordinator's integration of all three
component commits and the scalar checker, which I did not author. The
coordinator separately re-read the computational removal edges. No agent
agreement is treated as proof.

## Scope and results

| Item | Mathematical/source status | Execution status in this review |
|---|---|---|
| Baseline preservation | All original Git tree entries retain their original mode/type/object identity | Fresh comparison: 2,748 entries, zero modified or missing; 21 additions at reviewed head |
| Three component integrations | Acquisition and computation reports unchanged; scalar checker/review/logs unchanged; two scalar TeX layout edits identified | Fresh byte comparison against b7757f1, 4e8ccb5 and584ce25 |
| Fixed scalar program | Finite rational inequalities correctly implement the displayed bound; no represented law, supremum, acquisition or LOCAL47 predicate | Fresh isolated invocation: exit0, empty stderr,13 named controls rejected; output byte-identical to the component run |
| Scalar arithmetic cross-check | Explicit integer identities independently confirm bound and margins | Six separate integer identities pass; five additional invalid parameter probes reject |
| Task inventory and retention | Five bypass candidates exist, all original local/finite obligations remain declared | Fresh JSON inspection:240 distinct task IDs; unchanged baseline TASKS.json;32 explicit local-family predicates also checked |
| Shared finite coarse-cap consumer | Same source edge reported earlier; author rechecked it against its archive hash | Fresh read of actual caller; no inherited numerical execution |
| Analytical recurrence / strict-tail composition | Written proof reviewed at its stated scope; strict-tail conclusion still requires equality-compatible full LOCAL47 | The checker does not establish these analytic premises |
| Native finite/tail certificates, complete conjecture, Lean theorem | Not established by this review | Zero inherited/native certificate programs executed |
| PDF | Final source/PDF hashes match final verification record; layout changes preserve mathematics | No new compilation or page rendering by this reviewer |

Fresh scalar stdout, stderr, Python/platform details, return code, elapsed time,
script/output hashes and integration receipt are preserved at
`runs/least-counterexample-20261027/review-integration01/` in this review branch.
These records describe the bounded review only.

## Component integration and baseline immutability

Commands actually run from the review worktree included:

```sh
git status --short --branch
git rev-parse HEAD
git log -7 --oneline
git diff --stat 6346fc1b4432bc5982822aa696eb566ed9e1e1ee HEAD
git show --stat --oneline b7757f1
git show --stat --oneline 4e8ccb5
git show --stat --oneline 584ce25
git diff 584ce25 ac7bd06 -- mathematics/audit/2026-10-27/scalar-proof/main.tex
git rev-parse audit-baseline-20261027
```

A standard-library Python command read both trees with
`git ls-tree -r -z REV`, mapped every original path to its complete
`mode type object-id` record, and required equality at the reviewed head.
It found **2,748 original entries, zero changed/missing entries and21 new
entries**. This establishes byte/mode integrity of tracked baseline material,
not its mathematical correctness. The baseline tag still resolves to the
specified baseline commit.

For each original component commit, the comparison enumerated paths with
`git diff-tree --no-commit-id --name-only -r COMMIT`, then compared
`git show COMMIT:PATH` with `git show ac7bd06:PATH`:

- `b7757f1`: `acquisition-review.md` is byte-identical.
- `4e8ccb5`: `computations-review.md` is byte-identical.
- `584ce25`: `check_scalar.py`, `scalar-review.md`, the scalar compile receipt,
  and scalar run receipt/stdout/stderr are byte-identical.
- Its sole changed file, `scalar-proof/main.tex`, has two reviewed layout edits:
  the definitions are split into two displays, and a long source path uses
  `\path` instead of `\texttt`. Mathematical definitions and inequalities
  are unchanged.

All13 entries in the new `baseline.json` were also compared against actual
baseline blob SHA-256 values and matched. The final TeX and PDF SHA-256 values
match `scalar-proof/verification.json`:

- TeX: `f4173c5ef1a0beed109f048c36766cf9eb6f9db46a7ca89370f50fa061033e3a`.
- PDF: `5ad5da0e79663144d8196865995b7b733a7a8be8308cf4bbce15f0d465255cd7`.

The original component compile receipt concerns the pre-layout source; the
separate final verification record pins the final source/PDF. I did not
reinterpret the earlier receipt as a compilation of the later source.

## Fixed scalar checker: semantics and negative controls

I read all122 lines of `check_scalar.py` and the complete scalar review before
executing it. The actual fresh fixed invocation was:

```sh
python3 -I -B mathematics/audit/2026-10-27/check_scalar.py
```

The saved repeat used `sys.executable -I -B` with the same path, captured both
streams, and recorded version and hashes in `review-integration01/run.json`.
Both completed with exit0. The saved stdout exactly matches the component
commit's `scalar01/stdout.txt`. No inherited proof program was imported or run.

The correct scope is **this fixed invocation**, with its literal integer and
`Fraction` constants. `check(p)` is not a general external proof-object or
LOCAL47 acceptance API: it checks the parameter key set and selected signs,
but does not enforce a `Fraction` type on every supplied scalar or represent
mathematical owners and their acquired properties. No current command-line or
file input supplies a replacement parameter object. A future general-purpose
checker would need its own input schema and soundness review.

The finite gates match the proof:

- Tangent identities and rational arctangent lower bounds support the written
  Machin argument. Correct branch selection and the integral inequalities
  remain written analytical arguments, not arithmetic consequences alone.
- `(19+6*r)/(72*pi_lower)` bounds `C_E^2` when `r>sqrt(10)` and the proved
  positive lower pi bound is used.
- The Taylor gate verifies `phi(0)/6 < 1/15`; the heat gate verifies
  `1/(4*pi) < 2/25` under that lower bound. Uniform Gaussian remainders remain
  justified in the prose proof, not by testing finitely many laws.
- The square-root and denominator gates are strict. With `n>=47`, elementary
  monotonicity makes the endpoint bounds uniform. The checker itself does not
  quantify over infinite n; the source proof supplies that reduction.
- `zero predecessor-loss gate` is the tautology `0<=19/100`. This is honest
  bookkeeping after the written least-counterexample argument proves the loss
  is zero; it is not an executable proof about a law or a predecessor supremum.

Independently of `check(p)`, integer cross-multiplication gave:

```text
47*(41*750 +1011*10 +1011*2)/(46*150000) =335909/1150000
3*1150000 -10*335909 =90910
4247*47 -41*4700 -3000 =3909
46*1011^2 -47*1000^2 =17566
1681*11304 -1900*10000 =2024
1184*239 -4*375 =281476; 375*239 =89625
```

These confirm the `.3` margin `9091/1150000`, own-cap margin `3909/470000`,
root comparison, coarse Esseen-constant comparison and rational pi bound.

All13 built-in negative controls reject at the intended gate: too-small
square-root, square-root-of-ten, Esseen, Taylor and heat constants; too-large
lower denominator bound; the insufficient `.29` target; own/deleted cap
failures; index1; the current envelope at index46; missing and extra fields.
They exercise distinct logical seams rather than merely a success-string
comparison. They are not exhaustive parser/semantics tests. Rejection of
index46 or target `.29` says this chosen envelope does not prove that claim;
it does not refute a different sharper argument. The scalar review explicitly
makes that distinction.

Five extra probes, after loading only this newly written module without its
`main`, rejected `heat=0`, a negative deleted cap, `n0=0`, `sqrt_bound=1`, and
nonintegral `n0=95/2`. These reinforce domain rejection without enlarging the
claim to a general external-input checker.

## Task graph and retention

Fresh parsing finds240 unique declarations with exactly:

```text
finite-native31; low-row152; collector2;
tail-native10; tail-mapping3; tail-retained41; tail-umbrella1.
```

Every baseline task declaration remains byte-identical. The five conditional
bypass candidates occur exactly once:

```text
tail.new.composition49
tail.new.support46
tail.new.independent_support46
tail.new.independent_selectors
tail.new.corrected_barrier46
```

A separate explicit membership check found all32 listed local-family
predicates: corrected broad acquisition, later-phase and independent-phase
licenses, entry/local mappings, radius3.84 support, HIGH tail/window,
INITIAL47, central/left support and input, original confinement and feedback,
Sperner/profile refinements, signed resources and left-radius/input updates,
TINY/MID/LOW/normalization and complete local coverage. Other controls likewise
remain because the whole task file is unchanged. This is retention, not fresh
acceptance of any of these predicates.

I re-opened `backend.zip!finite61/MANIFEST.json`, recovered the actual
`.../entry/check_support42_48.py` member, and checked its SHA-256
`a51a70f459a4f3cd1fb5d2cbd561baa2cd6fdfadd30aa132222dbd04dbc4ca7d`.
Line9 is still literally:

```python
assert all(F('.40974')+F('.7')/n<F('.4253')for n in range(45,49))
```

Its neighboring lines7–10 establish the other caps and call the actual
`target(42,48,.54,3.4,27/2050)` support instance. This source check confirms
that integration did not silently discard the shared `.7/j` consumer. As its
original report author, I do not count this repeat as independent mathematical
verification of that earlier conclusion.

## Coordinator audit and state review

I read `AUDIT.md`, all three component reviews, and the four `state/*.md`
files (using `git show HEAD:state/FILE` because the worktree is sparse).
No blocking overclaim was found:

- Five task candidates are distinguished from deletion authorization and from
  the current complete55 execution predicate.
- The coarse-ceiling edge to finite43–48 is retained, and no per-index47/48
  savings or measured speedup is claimed.
- Support, corrected phase acquisition, confinement, complete local
  comparison and zero noise remain explicit obligations.
- The strict-tail argument is separately conditional on equality-compatible
  acquisition/exclusion. A least `>` argument is not relabeled as strict.
- Final finite collectors and public end-to-end `full_pass` remain incomplete.
  The missing-provider observation is limited to absent listed filenames;
  possible content-addressed locations are left unresolved.
- The derivative normalization issue is recorded as a bounded source-prose
  defect, with original bytes preserved. This review did not independently
  redo the entire attainment/contact analytic argument.

The phrase “immediate computational saving” in the verdict is immediately
qualified as candidate bypasses in a new assembly; it must not be quoted as an
implemented or measured saving. No wording change is required for the present
full paragraph, but future summaries should retain that qualification.

This review supports inclusion of the audit and its new scalar evidence only.
It supplies no acceptance of a native certificate, no completed global proof,
no permission to weaken targets, and no instruction to merge automatically.
