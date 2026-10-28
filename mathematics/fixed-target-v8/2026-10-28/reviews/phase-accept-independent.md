# Independent phase-export executable review

The repaired phase acceptor has no remaining blocking issue in the reviewed scope: authenticity and completeness of the fixed 682-cell signed export, conditional on the accepted v7 entry and its analytic premises. The original acceptor had a reproducible source-binding defect. It accepted an export changed by unpinned Python bytecode even though every pinned source file was unchanged. The repaired version rejects that export and reproduces the original bytes while both a poisoned cache and an import-shadow file are present.

This review concerns executable source binding, complete deterministic replay, serialization, and corruption rejection. It does not independently reprove the signed transport, Fourier inequalities, conservation, actual-gap acquisition, whole count comparison, or BASE41.

## Versions and findings

| Object | SHA256 | Outcome |
|---|---|---|
| Original accept_phase.py | `3a0fc9dda618bfc463073971058fba9f9240850ff050aa10f0f30dc0badcf0bd` | Source-authenticity defect reproduced |
| Original phase_probe.py | `fe59af3964c7cb6800d7f667c1ffd958ecf2bf7ae42728129999d6914b523fc8` | Name-based import could also select a shadow module |
| Repaired accept_phase.py | `416ab9b7bf957c57062e929743dad200f9ac002f879cb2516eeb9c6a2ac2e6b7` | Fresh adversarial replay passed |
| Repaired phase_probe.py | `90ca756fde0425505013444ab1a5ff5ffa9fb9bb0ff125fbdda6a132eb64167d` | Executes pinned project source paths directly |
| phase_core.py, unchanged | `c9cc7e5a0e5637faafc912882cdb9bcd28bda5fa9982304ede2ab412c724ee7a` | Add-only export patch independently checked |
| Full phase export, unchanged | `b18599468c975032f4078e7a5f734fd6430b2b7da583789de58d9537d323f690` | Repaired replay is byte-identical |
| Fixed v7 input | `61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae` | Separate full isolated reproduction passed |

**Resolved blocking finding: a source hash did not bind the executable imported module.** In the original acceptor, the subprocess used `python -B phase_probe.py`. The `-B` flag prevents writing bytecode; it does not prohibit reading a valid cache. The independent test created a timestamp/size-valid cached `phase_core` in a disposable inherited cache prefix. The source bytes and all nine pins stayed unchanged. The cache wrapped `stage` to add `unreviewed_cache_field: true` to every exported active cell. The altered producer output was then accepted by the original acceptor, return code 0. This is an execution of an actual altered export, not a hypothetical attack or a claim that the original clean arithmetic result was wrong.

**Resolved source-resolution finding.** The original producer inserted the v7 directory before importing `phase_core` by name. An additional `v7/phase_core.py` therefore shadows the pinned v8 source. The independent resolver test confirmed that selection without executing the sentinel. The repaired replay was subsequently tested with an actual sentinel shadow file whose execution would raise an error.

The repair is at current `accept_phase.py:30–38` and `phase_probe.py:7–16`. The acceptor pins sources before launching an isolated child with `-I -B -X pycache_prefix=<fresh directory>`. It checks that this prefix stays empty. The producer preloads every project dependency by its known source path using `compile`/`exec`, under its expected module name. Consequently project import caches and same-name search hits do not supply executable bytes. The trusted interpreter/standard library and no hostile concurrent source mutation remain ordinary explicit assumptions.

## Independent coverage and coefficient checks

The reviewer read the acceptor, producer, generator, generated core, v7 acceptor, support module, and the two executed scalar kernels before running any copy. All executions and mutation tests used a separate review worktree and disposable subdirectories. Root files and old sources were unchanged.

- The frozen v7 shape validator supplies exactly four ordered 24-row stages. The producer replays stage 4 from the recorded stage-3 upper bounds; it does not rerun the first three stages. There are 16 scheduled stage-4 rows, each with a complete 1×8×8×2 cover: 2048 scheduled cells. Their inherited active counts sum to 682. The reviewer checked those counts, row order, and per-row active/excluded counts independently from the frozen object.
- `phase_probe.py:21–29` checks the support radius again and uses `accepted.check_row` for the outward stage outputs and exact census. `phase_core.py` appends one phase record for each active cell and retains the old complete-cover assertion. The reviewer checked that applying the generator's three literal, unique patches to the frozen v7 core gives the exact generated core. Thus no pre-existing arithmetic or exclusion was silently replaced by the export patch.
- For each of the 682 records and both fixed-c endpoints, the reviewer separately reconstructed the constant term, signed positive and negative linear coefficients, and positive quadratic coefficient from the exported source intervals. All 1364 endpoint quadratics match. Both signed linear bounds are at most the retained absolute bound. These are independent algebra/serialization checks, not an independent reimplementation of the Fourier kernels producing the interval inputs.
- The full list is compared in deterministic order. Missing, duplicated, or reordered records cannot be hidden behind aggregate counts. The `probe` summary is also compared, but it is only the stated bounded diagnostic evaluation. Acceptance of this export does not accept the separate continuous-region evaluator or a full confinement theorem.

## Serialization and rejection

`accept_phase.py:21–26` rejects duplicate JSON keys at every nesting depth. Canonical JSON comparison preserves list order and distinguishes integer, floating, boolean, string, missing, and unknown values; key order and whitespace may vary harmlessly. `allow_nan=False` rejects non-finite JSON numbers. Rational fields are accepted only if they equal the exact regenerated rational strings, so a separate permissive rational parser is not used on candidate fields.

In addition to the acceptor's 13 controls, the reviewer tested ten independently chosen comparisons: nested boolean index, nested floating index, noncanonical rational text, a numeric rational replacing its string, lost fixed-c endpoint, changed curvature, unknown nested field, NaN, changed parent hash, and a nested duplicate key. All reject. The repaired command-line tests also reject optimized Python, a changed pinned core, a nested duplicate key, and the entire formerly accepted cache-altered export.

## Fresh evidence and remaining trust

| Claim | Mathematical status | Execution status |
|---|---|---|
| Original source-binding flaw | Concrete executable counterexample | Fresh accepted altered export, with all source pins unchanged |
| Repaired phase export | Complete deterministic serialization of the reviewed stage-4 calculation; inherited analytic inputs remain conditional | Fresh PASS with poisoned cache and shadow file present; unchanged export SHA |
| All phase cells and both endpoint coefficient records retained | Independently checked census, ordered rows, coefficient identities and add-only source transformation | 2048 scheduled cells, 682 active records, 1364 reconstructed quadratics |
| Frozen v7 parent | Same conditional mathematical statement as its original source; no new theorem claimed | Fresh full isolated reproduction described below |
| Full local comparison, BASE41, global theorem | Not established here | Not run or claimed |

Evidence directories are `runs/fixed-target-v8-20261028/phase-accept-review01`, `phase-accept-review02`, and `phase-accept-review03`. Review01 records a harness setup failure after a successful clean replay: the macOS Python default cache prefix lay outside the disposable tree. No poisoned file was created there. Review02 uses an explicit disposable inherited prefix and records the successful counterexample plus all independent checks. Review03 records the repaired adversarial acceptance and rejections. Each subprocess has a return code and raw stdout/stderr hashes. Committed readable views normalize environment paths; the large altered producer output is preserved losslessly as gzip. Original and repaired source snapshots are retained separately.

The replay-based acceptor intentionally trusts its pinned implementation; executing that same implementation twice is not independent mathematical verification. The new coefficient and coverage checks narrow that trust but do not remove it. Standalone `phase_probe.py` output remains exploratory until the acceptor checks its pins and complete output. The repaired acceptor itself does not provide a fresh v7 ancestry replay.

## Isolated reproduction of the unchanged v7 ancestor

The bytecode limitation also applies to the historical v7 importer pattern. This does not show that a historical run loaded bad code. It shows that source pins alone did not rule that out under untrusted caches or extra modules. The new `isolated_entry_replay.py` provides fresh evidence without modifying any v7 source:

1. Check the fixed acceptor SHA before parsing its AST; extract only its literal `PINS` and `PRELOAD_PINS`.
2. Read and verify exactly 13 files: the acceptor, fixed proof, two immediate pinned modules and nine transitive source/data files. Hold those verified bytes in memory.
3. Copy only those files to a fresh private tree preserving relative paths. Check the allowlist and copied hashes. No external proof path or alternative target is admitted.
4. Launch trusted Python with `-I -B`, a fresh cache prefix and a small `runpy` bootstrap that inserts only the copied v7 directory for project imports.
5. Require successful complete acceptance; verify all copied bytes remain unchanged, no extra project files appear, and the cache remains empty.

Fresh result in `runs/fixed-target-v8-20261028/isolated-entry-review01`: all 11264 selected signed-stage cells, 100 probability panels, 30 nonempty panels, 14 surviving rho rows, all 19 inherited rejection controls, and five wrapper controls. The wrapper rejects a missing proof, modified proof bytes, modified acceptor before AST parsing, an unlisted executable, and a modified inherited kernel. The full child stdout is byte-identical to the historical accept02 stdout; this is an observed reproduction result, not a premise taken from the old PASS. The fixed-target two-quadratic ancestor was recomputed by the unchanged v7 code as part of this execution.

Run the new wrapper from the repository root:

```sh
python3 -B mathematics/fixed-target-v8/2026-10-28/isolated_entry_replay.py --output-dir runs/fixed-target-v8-20261028/isolated-entry-new
```

The output directory must be new. This is named isolated reproduction of one fixed object, not a general certificate acceptor or a new analytic theorem. The coordinating reviewer independently read the wrapper and found no blocker in this restricted trusted-runtime scope. No inherited source, proof object, or historical log was rewritten.

Recommendation: accept the repaired phase-export code and the fresh isolated reproduction evidence within their stated computational scopes. Keep all analytic premises, complete local count obligations and BASE41 explicit. Do not use the old unisolated import pattern as a general tamper-proof source-binding claim.
