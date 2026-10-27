# One-pass LOW: a concrete candidate and bounded protocol evidence

The current protocol evaluates the same152 native LOW configurations twice: once
by the row producers and once by the full binders. A new candidate adapter
now performs generation and binding in one invocation, evaluating each
configuration once and retaining the original source, output, index,
coverage, numerical-summary and negative-control requirements. It accepts
no producer receipts or previously computed rows as arithmetic evidence.

The new protocol has been exercised with tiny synthetic kernels and the
unchanged binder bodies:304 reference calls became152 calls, with identical
row bytes, index bytes and numerical summaries. This is a concrete execution
protocol reduction, independent of the proposed uniform42 theorem. The
native arithmetic and production integration have **not** been run or
accepted. No current runner, certificate, manifest or theorem was changed.

| Result | Mathematical status | Execution status |
|---|---|---|
| Equality of the152 repeated native kernel obligations | Source-derived equality of fixed function, exact arguments and mathematical checks | Entire selected call inventory and source pins freshly checked; native kernels not executed |
| One evaluation suffices for each deterministic exact predicate | Locally derived program-level equivalence under the stated source/runtime assumptions | Executable adapter implemented; native path not run |
| Serialization, unchanged binding and controls in the new protocol | Bounded fixture equivalence, including full152-label cover and left empty-cell branch | Fresh PASS using unchanged binders with synthetic contract/kernel only |
| All152 actual LOW predicates or23,513,686 actual gates | Retained proof obligations | Not run; recorded count only |
| Acceptance by a current global provider | Unresolved integration and analytic-parent obligations | No new production acceptance; every candidate result retains `full_proof_pass=false` |

Work began at fork head `42433b448d9389359e642a3384a949ffdd87b903`
on branch `simplify/onepass-low-20261027`; the original reference remains
`6346fc1b4432bc5982822aa696eb566ed9e1e1ee`. Git status was clean before
these additions. The earlier `local-cover.md` was written by this same
agent; it is a prior observation, not independent review of the adapter.
This implementation and its argument require independent review.

## Precisely which old computations repeat

Sources are in `verification/finite-tail/sources/backend.zip`, whose SHA256
is `43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`.
Its direct member `finite61/MANIFEST.json` has SHA256
`c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`.
For logical paths below define
`F=work/toward40_20261007/audit43/capsule/work/below49_20261006/`.
Read bytes from `finite61/blobs/<files[logical].sha256>`; the historical
`archive_member` field is not the path in this compact ZIP. Source line
references refer to those exact decoded blobs.

The direct member `finite61/finite61_worker.py:65–78` reads the actual
target row, invokes `contract.selected(row,sign,H_cells,outer_phase_cells)`,
calls `kernel.evaluate(cfg)`, and serializes the returned proof/report with
fixed row labels. Its SHA256 is
`15e4d3d14dc4e8323ac561e0e65f788ff1268110c26bff6306edc5febf93234f`.
The selected native binders repeat precisely that call:

| Family | Selected tasks / exact grid | Original repeated call |
|---|---|---|
| CENTRAL42 | `61.low.central42_v2.00..38.{minus,plus}`:78. Row0/minus uses32 H cells and16 outer cells; the other77 use16 and8. | `F/local/central42_v2/bind_low42.py:34–45` |
| LEFT42 | `61.low.left42_final.08..44.{minus,plus}`:74. Every row uses8 H cells and4 outer cells. | `F/local/left42_final/bind_low42.py:34–48` |

The same ordered rows are selected by their fixed target ceiling:
`lambda_max>.05` centrally, `>.08` on the left. Contracts bind all47 central
and45 left probability rows, then select the complete LOW subset
(`central42_contract.py:9–30` in each family). All non-scalar noise bands,
amplitude/rate profiles and signed quadratics are constructed from that same
row. They are not independent inputs that a receipt may silently replace.

The complete native source closure for either family is five files:
`tiny42_normalization.py`, `central42_contract.py`, `central42_kernel.py`,
`bind_low42.py`, and the family's target JSON. The four Python files and
their imports were read in full before testing. The normalizer calls no
discovery code; its active dependencies are standard-library exact
fractions/integer roots. The kernel's three global memoized helpers are pure
functions of exact arguments; each evaluation's phase cache and all counters
are local (`central42_kernel.py:19–52`, central final output`:194–203`,
left final output`:210–219`). The candidate clears these three global
caches between rows to preserve the old producer isolation. No native
function is rewritten or rederived in the adapter.

The inventory result in `runs/reduction2-20261027/onepass-fixtures02/stdout.json`
records all ten family source entries, including their full hashes. In
particular the binders are pinned to
`37d902cf45ce826a4fcd97aa9674790f4c16fa6be8ad6c91ba7d6960e6e78f5b`
and `b21670bda62bcc2a97dad1f58a4e89eaf4e3e0907ba1b5de192f4c2f1617ec3c`;
the central and left kernels are
`9dc0754fe2dd4f2f7057247d3d62f3b71472c65a49d46f67d35fb0d66e3f8673`
and `d025529aa2690c3cfc0f1c34a6af385d6fa69db8e069543057f29475cbb133c3`.

## Why one evaluation can discharge both copies

Fix one selected row/sign/grid and its fully constructed exact configuration
`c`. Let `E(c)=(p,r)` be the pinned exact kernel's completed evaluation, with
all its strict gates. The old producer writes
`S(index,sign,p,r)`, where `S` is the fixed UTF-8 JSON serializer. The old
binder reads that object, performs its structural checks, evaluates `E(c)`
again, and compares **every** returned proof/report field with the object.

For this fixed deterministic implementation, the two calls have identical
input and gate sequence. A new invocation can instead evaluate `E(c)` once,
retain its full result in private memory, serialize it, and verify that all
subsequently bound bytes still encode exactly that retained result. Then
the same full-output equality holds directly against the just-completed
evaluation. The strict gates are actually executed once; they are never
inferred from a PASS string, hash or untrusted receipt. This is the same
exact-predicate premise used by the original checker, not a new theorem
about the Berry--Esseen reduction.

Source/runtime correctness remains a trusted premise. Repetition can have
engineering value for detecting transient faults; it is not a distinct
mathematical inequality or an independent implementation. The old frozen
index still binds the exact native result bytes. Changing a target or
report field that changes these bytes rejects rather than admitting a new
theorem. Hashes identify those bytes; they do not prove their mathematics.

The internal `_one_pass` helper takes modules explicitly to permit tiny
fixtures. Its return is only a protocol summary: that helper is not an
acceptance API for arbitrary injected evaluators. The native entry has no
injected evaluator or receipt parameter. It loads only the fixed archive,
manifest, tasks and pinned five-file closure. Its result is a distinctly
named candidate receipt and cannot be substituted for an old
`TASK-COMPLETED.json` or `PASS_FRESH_EXACT_REPLAY` record.

## What the candidate actually preserves

`onepass_low.py:81–139` authenticates the entire archive/manifest, source
bytes, exact family/index pins, complete ordered task labels and grids. It
checks the target-derived LOW subset against all152 fixed labels. Its
source scan permits only the inspected imports. It never stages old row
objects, indices, historical completion markers or discovery modules.

The internal mechanism at`:142–212` does the following in order:

1. Obtain the target table from the pinned contract and require equality
   with the pinned source table. Construct each actual configuration using
   the original selector. Preserve the entire typed configuration, including
   nested non-scalar fields, and reject mutation by the evaluator.
2. Call the original `evaluate` exactly once per selected row. Preserve
   every returned field; round-trip through the original row serializer and
   compare the complete typed value, not just scalar contract fields.
3. Write only newly created row paths and build the original canonical
   index in the original order. Require its exact original SHA256:
   central `a02638ae22a0efbcb5dd1a8e1e9b233fd1f957c8fc46ba32aef2270cc874519e`;
   left `aca7d7ac16a43a35750ddb173d5a30e169f7d80f61d68472e46934f10835cd52`.
4. Invoke the **unchanged** binder `check(...,replay=False)` and its
   **unchanged** `controls(...)`. This keeps schema, strict labels,
   order/cardinality, paths, hashes, scalar contracts, all integer counters,
   endpoint multiplicity, complete phase/noise grids, status, failed-gate
   emptiness, positive reserves, strict scores and the left empty-cell case.
5. Require all nine controls in the original order. Compare every original
   numerical-summary field (`rows`, `strict_gates`, exact `worst_score`,
   `row_digest`) against the frozen manifest expectation. Re-read every row
   and the index; require equality to the results computed in this invocation.
   Source/adapter bytes are checked before and after binding and around rows.

The exact old binder locations are central`:20–47,48–67` and
left`:20–51,52–71`. Both binders label their default mode as an integrity
check, not a second arithmetic acceptance (`:1–5`). The candidate does
not mistake that default mode for arithmetic: the immediately preceding
fresh kernel execution supplies arithmetic. The old static `arithmetic_run`
and scope strings are source-bound historical metadata; the candidate
does not relabel them as its current run. It emits a new honest status and
explicitly records `original_binder_replay_executed=false`.

The native entry at `onepass_low.py:215–294` requires a fresh unoptimized
isolated interpreter with site loading/bytecode disabled, an exclusive new
directory, immutable regular source files and a source-read/write trace.
It rejects preloaded native module names. That trace is not an operating
system sandbox or a sealed runtime. The result explicitly requires runtime
seal/supervisor integration, coordinator execution authentication, and all
current analytic parent licenses. It never sets an all-law/full-proof flag.

Default CLI mode is source inventory only. The opt-in native family path is
implemented for review but **was not invoked**. Running it would be an
expensive certificate campaign requiring the user's explicit authorization.

## Source-only package and the achievable saving

The source-only backend omits the old LOW row/index objects. This blocks
starting an unchanged replay binder by itself. It does not require the
candidate to trust a substitute receipt: the candidate constructs every row
fresh in the same invocation, reconstructs the original index, and rejects
unless the index meets the original pin. A missing old witness is therefore
not an input hole in this proposed one-pass algorithm. Producing its native
bytes still requires the retained152 real evaluations, which were not run.

Current `finite61_batch.py:57–84,101–103` separately imports all producer
outputs and reconstructs that same pinned index. Its worker execution and
receipt controls at`:170–207` are still in force for the current production
path. In particular `:205–206` says a producer output alone is not accepted
and still needs full binder replay. This patch does not modify that path or
claim that its current154 tasks have passed with fewer receipts.

| Call count, both families | Current protocol | New candidate after valid integration |
|---|---:|---:|
| Producer-equivalent exact kernel evaluations |152|152|
| Repeated binder exact kernel evaluations |152|0|
| Total |304|152|

After valid integration, the candidate would save exactly152 duplicated `evaluate` calls. It saves
no original selected row predicate or local family. Were a separately
chosen full-row cross-check retained, the total would be153 and the saving
151; that optional variant is not implemented or counted in this result.
Cheap selector/normalization and structural checks still repeat in the
unchanged binders. No claim is made that all arithmetic runs exactly once.

The duplicated gate count is the source-reported19,842,356 central plus
3,671,330 left =23,513,686 strict kernel gates. These counts also occur in
the frozen binder summary expectations. They are historical work counts,
not fresh native PASS evidence or measured runtime. No speedup duration,
memory bound or paid-compute estimate was invented.

## Bounded tests, failures and remaining work

After reading both scripts, I ran the new tests in an isolated interpreter:

```
python3 -I -B -S mathematics/reduction2/2026-10-27/onepass_low_test.py
```

The test executes the read, pinned binder bodies from temporary work copies,
with explicitly injected tiny synthetic contract/kernel modules. It does
not execute the original contract, normalizer or LOW kernel. Fake objects
say `SYNTHETIC_PROTOCOL_FIXTURE_ONLY`; their index hashes differ from the
native pins, and attempting to pass them under a real native plan rejects.
The reference side separately uses the worker's original serializer and
the unchanged binder's actual `replay=True` path with the fake kernel. The
new side invokes the candidate mechanism and unchanged binding/controls.
It tests all78+74 labels and the left zero-feasible-cell branch.

Fresh run02 passes: reference fixture calls156+148=304; new fixture
calls78+74=152; all152 row byte strings, both index byte strings and all
numerical summaries are identical. All nine original controls pass in
each family: missing, duplicate, reordered, boolean index/sign, extra scope,
path traversal, duplicate JSON keys, and corrupted row hash. Fourteen
additional cases reject: mutated nested configuration, wrong output
contract, non-finite JSON, partial kernel exception, post-binding row/index
corruption, lost control, changed source, wrong index pin, wrong summary,
fake outputs under native pins, missing row, supplied receipt argument,
and changed archive bytes. Exact rejection reasons are saved in stdout.

Run01 failed in a test-only mutation wrapper: it did not forward the
original binder's `load` keyword during negative controls. The wrapper was
corrected to preserve that signature; no adapter gate or native predicate
was weakened. Both run receipts/logs remain under
`runs/reduction2-20261027/onepass-fixtures01/` and `.../onepass-fixtures02/`.
The first harness version was preserved as `onepass_low_test.snapshot.py`
and its bytes checked against the failed receipt's input hash. Run02 has
exit0 and empty stderr; interpreter version, exact command, input/output
hashes and timestamps are recorded. The fixtures are disposable and were
not copied into any native proof directory.

Remaining before production acceptance: independent adapter review;
integration with the existing sealed runtime, timeout/process cleanup and
execution-authentication machinery; explicit user approval for the native
campaign; complete actual family results satisfying the original pinned
indices and summaries; a separately named downstream composition accepting
the new receipt and preserving all analytic/resource parents. No consumer
should accept an arbitrary JSON file merely because it has the candidate
schema or claims these checks ran. The native loading/trace path itself has
not been tested by the fake-kernel run. The current production task graph
and all existing certificates remain unchanged.
