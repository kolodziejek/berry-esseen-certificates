# Public COUNT inputs and fresh replay

The 1,243 forests are untrusted proof candidates. Installing them checks byte
identity only. Each original checker must still evaluate its complete forest,
and the resulting conditional inequalities must be joined to their acquired
same-law hypotheses before they support the manuscript's theorem.

The exact public asset is available from the
[verified byte-identical mirror](https://github.com/rodziewiczk/berry-esseen-certificates/releases/download/v0.1.0/count-candidates.zip).
Its size is **94,179,896 bytes** and SHA-256 is
`5c08ddbd642e5da7eea9d7053df721a89bdce1e91a17c82cc46b2a66c34a84e0`.
The original release catalog named the `kolodziejek` repository URL; that URL
was unavailable when these inputs were obtained. The mirror download matched
the original size and SHA exactly. Both URLs and the verification-receipt hash
are recorded in `COUNT_CANDIDATE_ASSET.json`.

The ZIP has exactly 1,244 regular file members: the unchanged original
`MANIFEST.json` and 1,243 distinct candidate blobs. They occupy 1,249,228,509
uncompressed bytes. The manifest SHA-256 is
`0431403e05326655f316991eae6fcdaa8c64bef244f055a40e1dc6958c892f5f`.
Neither the ZIP nor its manifest has been rewritten.

## Install or verify the inputs

Run these commands from the physical release directory. Select one Python
3.12 interpreter and use it for the fresh numerical campaign and its subsequent
joins. Do not use `-O` or `-OO`. The installer has no network operations.

```bash
COUNT_PY=/absolute/path/to/python3.12
env -u PYTHONOPTIMIZE "$COUNT_PY" -I -B tools/install_count_candidates.py \
  --archive /absolute/path/to/count-candidates.zip --workspace "$PWD/workspace"
```

The installer first checks the whole ZIP, original manifest, exact namespace,
member types, sizes, and every member hash. It then checks all existing target
files before any write. It creates missing files exclusively or verifies
identical existing files. Different files, additional files, symlinks, unknown
directories, duplicate ZIP members, and unsafe names reject. It never replaces
existing inputs or execution results. Use a physical path without symlink
ancestors; for example, macOS's `/private/tmp` rather than its `/tmp` alias.

The fixed destination is
`workspace/work/unconditional_legacy_20261030/certificates/count`.
To require that the entire installed tree already exists, add `--verify-only`.
The tool prints an input-restoration receipt to stdout; that receipt explicitly
states that it did not execute native arithmetic.

The accompanying negative controls can be rerun without invoking any native
inequality checker:

```bash
env -u PYTHONOPTIMIZE "$COUNT_PY" -I -B tools/test_count_candidate_installer.py \
  --archive /absolute/path/to/count-candidates.zip
```

## Fresh complete numerical campaign

The original public `batch_verify.py`, `count_worker_v2.py`,
`capsule_worker.py`, source registry and all its source blobs must also have
been restored from the source package. Their frozen pins are recorded in
`COUNT_CANDIDATE_ASSET.json`. The candidate ZIP contains inputs only; it does
not supply these programs.

Use an absent output directory and run **all** jobs:

```bash
env -u PYTHONOPTIMIZE "$COUNT_PY" -I -B \
  workspace/work/unconditional_legacy_20261030/verification/count/batch_verify.py \
  --manifest workspace/work/unconditional_legacy_20261030/certificates/count/MANIFEST.json \
  --worker workspace/work/unconditional_legacy_20261030/verification/count/count_worker_v2.py \
  --output workspace/runs/extension_20261030/coordinator/count1243-01/native \
  --jobs 2 --timeout 1800
```

This unchanged batch program creates one fresh `native/run-<uuid>` directory.
It records every job in `RESULTS.jsonl`, complete native outputs and worker
observations in each job directory, adapter logs, and a final `SUMMARY.json`.
No saved PASS is reused. Keep the complete directory, not just its summary.

The current n=5 composition reader requires exactly one `run-*` directory at
this precise workspace-relative location, all 295 n=5 observations, the
unchanged public worker SHA, isolated/unoptimized Python with bytecode disabled,
the same interpreter/runtime projection, and a maximum 1,800-second native
replay. Therefore do not use `--resume`, run a smoke test in this canonical
directory, or combine partial campaigns there. A failed campaign is preserved;
select a fresh workspace for another complete run or introduce an explicitly
reviewed campaign-selector adapter.

**Current composition-platform scope:** the arithmetic worker is portable, but
the unchanged `n5_semantic_join.py` currently requires `system == 'Darwin'` in
its runtime observations. Its parent transport also records actual Darwin
observations. Linux execution can verify the numerical forests, but it does
not pass that composition reader without a separately reviewed transport
adaptation. Do not relabel another platform's observation as Darwin.

After the required n=5 source epoch is freshly prepared, its `counts` mode can
read this campaign with the same isolated interpreter. Full `join` additionally
needs all fresh parent executions and the source-cache activation step described
in the n=5 reproduction instructions. A standalone COUNT PASS is conditional
arithmetic, not the all-law theorem.
