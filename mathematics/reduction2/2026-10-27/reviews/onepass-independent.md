# Coordinator's independent review of the one-pass LOW candidate

Reviewed constructor commit `4dcbda7d81b250c5266a13a6952b4e85a0f2e62a`;
integration copy `d632651`. The coordinator did not construct the adapter or
its fixtures. I read the complete adapter, fixture harness, report, both
original binder bodies and the exact original producer call/serializer.

**Outcome:** no blocking defect found in the conditional one-pass equivalence
or fixture-level implementation. The native loader, real numerical execution,
sealed-runtime supervision and downstream acceptance remain untested or
unintegrated. The code is suitable as a reviewed prototype, not a replacement
production acceptance path. The old runners remain untouched.

## Independent equivalence argument

For a fixed authenticated family, the source manifest and target table fix
an ordered list of triples `(row, sign, grid)`. The original worker invokes
`selected(row,sign,H_cells,outer_phase_cells)` and `evaluate(cfg)`; the binder
reconstructs the same cfg and repeats that exact function. Source locations:
`finite61/finite61_worker.py:65–78`, CENTRAL binder34–45, LEFT binder34–48.
Both binders' complete pinned bodies were read directly from the archive.
The grids agree exactly: one32/16,77 at16/8,74 at8/4.

Let E denote the deterministic exact evaluator and S the original serializer.
The original path computes E(x), stores S(E(x)), computes E(x) again and
requires equality with the stored whole proof/report. Under the same trusted
runtime/source semantics, the second E(x) supplies no new predicate. A single
fresh E(x), followed by exact preservation of its entire value through S,
satisfies that equality. This reasoning requires **fresh execution**, not a
hash, a historical result or an externally supplied receipt.

The candidate supplies precisely that premise in `_one_pass`: each native
configuration is reconstructed, copied into a typed immutable snapshot,
evaluated once, checked for input mutation, serialized and round-tripped in
full. It saves typed snapshots of the returned entire objects and their byte
hashes. After original binder checks and all controls, it rereads every output
and compares it with that invocation's retained value. Thus no report field
omitted from the original scalar-contract checks is silently trusted.

The frozen original index hash and the complete old numerical summary remain
additional checks. The unchanged binder retains strict scores, reserves,
all integer counts, exact signed order and phase/noise coverage; LEFT retains
the explicit zero-feasible-cell case. Its default mode is correctly described
as structural binding, while the preceding fresh E calls supply arithmetic.
The candidate does not relabel the binder's historical run string as new
execution or make an existing producer receipt sufficient.

The native entry loads only the authenticated five-file closure, rejects
preloaded native module names, uses an exclusive new output directory and
unoptimized isolated/no-site execution, and checks source bytes around rows.
The source allowlist and filesystem audit trace are useful guards but do not
establish an OS sandbox or a sealed runtime. The prototype explicitly records
these remaining obligations and `full_proof_pass=false`.

## Checks performed and what they establish

After reading the original binder code, I freshly reran the supplied fixture
harness with `python3 -I -B -S`, saving a distinct receipt and all outputs in
`runs/reduction2-20261027/onepass-review01/`. This is a **reproduction** of the
constructor's fixtures, not an independent second arithmetic implementation.
Independent evidence is the source comparison and equivalence derivation
above. Neither reviewer nor constructor ran the native normalizer or LOW
numerical kernel in this work.

The fixtures execute the unchanged small binders with deliberately synthetic
contract/kernel modules. The legacy reference actually makes304 synthetic
calls; the candidate makes152. All row/index bytes and summary fields agree.
All nine original controls and fourteen additional invalid cases reject.
Synthetic hashes differ from native pins; fake outputs fail under a real
native plan. The supplied-receipt argument is rejected at the native API.
No source/program claim is based on a fixture's fake PASS-shaped status.

The full fixture cover includes both families and the LEFT empty-cell branch.
It exercises the internal one-pass mechanism, not the untouched native
loading/trace path. Consequently a statement that the new complete native
runner has been tested would be false. Both the report and receipt preserve
that boundary.

## Savings and compatibility boundary

On the unchanged152-label/native-output contract, the mathematical saving is
exactly152 duplicate evaluator calls:304 becomes152. Repetition may detect
transient hardware faults, but repeating the same exact implementation is not
an independent proof. No total runtime or memory saving was measured here.
The23,513,686 strict-gate total is a historical source count, not a fresh PASS.

The resource-pruning and exact-curvature proposals in this same research turn
are **not automatically stackable with this prototype**. They change selected
rows and/or numerical outputs. This prototype deliberately retains the old
index hashes, summaries and152 labels, so it should reject changed objects.
A combined faster implementation needs a separately named output/index
contract with a reviewed mathematical transport proof and new source bindings.
It must preserve complete domain coverage and every retained predicate.

Before production use: seal/supervise the runtime, authenticate the actual
execution for the coordinator, obtain explicit authorization for the native
campaign, reproduce the real fixed outputs and integrate a distinct receipt
contract with all analytic/resource parents. None of these steps is claimed
complete here. No original certificate or acceptance target was weakened.
