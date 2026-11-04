# Preserved execution evidence

These archives preserve selected completed execution records and their native
working files. They include actual commands, source/input identities, stdout,
stderr, process observations, candidate objects and complete results needed
by the relevant readers. They preserve original relative paths and recorded
absolute paths. They do not rerun the numerical checkers.

The three packs below preserve the complete selected execution evidence.
The [completion ledger](COMPLETION.md) maps their numerical scopes to the
manuscript. Archive completeness establishes preservation; the theorem also
requires the mathematical arguments and complete native acceptance.

## Existing packs and exact identities

| Pack | Selected scope | Files | Compressed bytes | Restored logical bytes |
|---|---|---:|---:|---:|
| `assets/evidence-base01` | Frozen completed foundation, coordinator and bridge captures identified by its selection inventories | 136,969 | 148,012,777 | 6,407,910,368 |
| `assets/evidence-finite01` | The 23 completed finite component roles, including original and explicitly continued executions | 107,148 | 109,376,824 | 13,634,739,006 |
| `assets/evidence-final01` | Final foundations, independent complete interface readbacks, controls and bounded publication records | 51,439 | 75,296,737 | 3,033,211,481 |

The base and finite archives each have two chunks named
`captures.tar.gz.part0000` and `captures.tar.gz.part0001`. The final archive
has only `captures.tar.gz.part0000`. Keep each pack’s complete chunk sequence and `PACK.json` together in the
named directory. The complete `CAPTURE_MANIFEST.json` is embedded in the
compressed stream and is verified by the restorer. The publication package
does not duplicate the large uncompressed manifest beside the chunks, and
no external manifest copy is required for restoration. The hashes below are
SHA256 hashes of the actual `PACK.json` files, not of the compressed streams:

```text
evidence-base01/PACK.json
70a93bf2d51fdba55c4bd4ed353f80f1fe011d7e5e9e86cc39445b3d7d3137d3

evidence-finite01/PACK.json
e46d1622b8c4cbe4d43566d22d3af4c5a4cdee4888a7f91b156cc6f2d0ebc3d9
```

The corresponding embedded capture-manifest hashes are:

```text
base:   3efcaf318a5ccd055bc71c1885db6aa330933a5a5cad81641c0c4d00dc2748b5
finite: 6455e8c5f9c889f57b84b54983310410c6d869718cd15c5d938fd133c99c2b8d
```

Each manifest maps every preserved relative file path to its byte count and
SHA256 and explains the selection. Identical contents are stored once in the
compressed archive but restored at every original path. Thus the three separate
restores together require about 23.08 GB of logical file contents, plus
filesystem overhead and temporary compressed streams; their compressed sizes
are not estimates of the required free disk space.

## Restore into separate fresh directories

Use the supplied [evidence_pack_v2.py](tools/evidence_pack_v2.py). Its reviewed
source SHA256 is
`58ad9d8a3ebd909729b3ddbd074e51d992138adf6049bfd6270d5b40b584fc63`.
It uses the Python standard library; the recorded restores used unoptimized
CPython 3.12.14. These restore commands do not need NumPy, Boost or a compiler.

Replace the three values below with actual physical absolute paths. Avoid
symbolic-link ancestors; on macOS, for example, use `/private/tmp` instead of
the `/tmp` alias. Choose a fresh parent location. The `base`, `finite` and `final`
destination directories must not exist, and should not be created in advance.
They must be separate from source or numerical-reproduction workspaces.

```bash
BE_PY=/absolute/physical/path/to/python3.12
BE_RELEASE=/absolute/physical/path/to/release
BE_EVIDENCE_PARENT=/absolute/physical/path/to/new-evidence-parent

env -u PYTHONOPTIMIZE "$BE_PY" -I -B \
  "$BE_RELEASE/tools/evidence_pack_v2.py" restore \
  --pack "$BE_RELEASE/assets/evidence-base01/PACK.json" \
  --pack-sha256 70a93bf2d51fdba55c4bd4ed353f80f1fe011d7e5e9e86cc39445b3d7d3137d3 \
  --workspace "$BE_EVIDENCE_PARENT/base"

env -u PYTHONOPTIMIZE "$BE_PY" -I -B \
  "$BE_RELEASE/tools/evidence_pack_v2.py" restore \
  --pack "$BE_RELEASE/assets/evidence-finite01/PACK.json" \
  --pack-sha256 e46d1622b8c4cbe4d43566d22d3af4c5a4cdee4888a7f91b156cc6f2d0ebc3d9 \
  --workspace "$BE_EVIDENCE_PARENT/finite"
```

The restorer checks the pinned PACK description, complete ordered chunk list,
every chunk, the whole compressed stream, embedded manifest, closed blob
namespace, blob lengths and hashes, and complete file counts. It rejects
symbolic-link ancestors, nonregular archive members, duplicate or undeclared
blobs, missing data and existing destination workspaces. It writes files with
exclusive creation and does not merge packs into an existing tree. Its success
message is `PASS_BYTE_PRESERVATION_ONLY`.

A rejected restore can leave a partial destination after archive validation
has begun. Preserve that failed attempt and use a different absent destination
for a corrected retry. Do not interpret partially written files as a completed
restore. Do not rewrite embedded old paths or runtime identities to make them
look current; they record the original execution environment.

Complete restores of all three published packs have been performed, followed
by explicit checks of every restored path, size and hash. The final archive
preserves these earlier receipts, at paths relative to its restored root:

- `runs/extension_20261104/coordinator/evidence-base-restore01/RESULT.json`;
- `runs/extension_20261104/finite/evidence-pack02/RESULT.json`.

The corresponding finite packaging commands, source identities and actual
process streams are also preserved under the second receipt's directory.
The final archive's own build and restore receipts necessarily sit outside
that archive. They are published under
[`publication/extension-20261104`](../publication/extension-20261104/), in
`final-evidence-build/` and `final-evidence-restore/`.

The publication package has no top-level restored `workspace/` directory.
Restore each archive into its own fresh destination to inspect its full
records. These preservation receipts are separate from mathematical acceptance.

## Three different checks

1. **Byte integrity.** An archive restore establishes that the selected files
   have the recorded bytes and paths. Hashes and successful extraction do not
   establish the correctness of the checkers or their mathematical claims.
2. **Native arithmetic and its scope.** Actual checker executions, complete
   outputs and source/domain readers establish their stated finite arithmetic
   obligations under the documented trusted implementation and runtime. Read
   the entire required evidence chain, including coverage, interfaces and
   adverse controls. An old `PASS` string, a summary alone or a preserved failed
   attempt is insufficient. Explicit continuations retain their old and new
   execution identities; they are not relabeled as one fresh run.
3. **Continuous mathematics.** Applying a finite inequality to the original
   class of probability laws requires the manuscript's analytic reductions,
   attainment/contact arguments, predecessor and own-score hypotheses, and
   complete same-law interfaces. Preservation and arithmetic do not discharge
   those obligations automatically.

For fresh numerical work, use [REPRODUCE.md](REPRODUCE.md) and the separately
pinned source assets and command maps. The 114-node reproduction index is a
dependency and command plan. It has not been executed in full as one fresh
relocated campaign. Static command validation, selected actual executions,
continued executions and byte-restoration checks are distinct evidence; this
guide makes no claim that all 114 commands freshly passed together.

## Deliberate symlink fixture excluded from the finite archive

Finite packaging selection06 excludes precisely this disposable negative-test
subtree from archive traversal:

```text
runs/extension_20261104/finite/scalar-relocation02/symlink-source
```

The scalar-preparation test deliberately placed a symbolic link there to check
that the preparer rejects it. The first evidence inventory also correctly
rejected this link. Neither process followed it as an ordinary accepted input.
The original fixture was not modified or deleted.

The preserved descriptor is
`work/extension_20261030/finite/SCALAR_SYMLINK_FIXTURE_PRESERVATION_20261104.json`
inside the finite restore. Its SHA256 is
`ed0ac1afa8d4cc2a881fd7325f3560fb9f7fd4f758f21cfe7e533215fb5f0580`.
It records the literal link target without following it and the identities of
the four ordinary duplicate fixture files. The successful scalar workspace,
actual commands and streams, negative-control outcome, selection adapter and
first rejected inventory capture are preserved. No numerical acceptance input
was removed. The link itself is not recreated when restoring the archive.

## Final supplement and its restoration

The final pack closes the formerly pending foundation records and includes
complete independent semantic69, semantic1014 and acquisition614 readbacks.
Its explicit selection also includes bounded review, source-restoration,
prior-pack preservation and final manuscript-build records. No live numerical
tree or already restored workspace was recursively archived.

The `assets/evidence-final01/PACK.json` SHA256 is
`2f37b3754679b774a7caba1f5deb52b98a607057c25eb4d33fe3f1983e04cca1`.
The embedded manifest SHA256 is
`05e880d6e562da1cb0545cd4bfeb1982c40ca6c591f75c107d20b3f73f9edc14`.
Its single chunk is 75,296,737 bytes, SHA256
`e164584e6c34877596294c811dd3970d5546662f1290b4362e53ed2687575389`.

Run the final restore into a third absent directory:

```bash
env -u PYTHONOPTIMIZE "$BE_PY" -I -B \
  "$BE_RELEASE/tools/evidence_pack_v2.py" restore \
  --pack "$BE_RELEASE/assets/evidence-final01/PACK.json" \
  --pack-sha256 2f37b3754679b774a7caba1f5deb52b98a607057c25eb4d33fe3f1983e04cca1 \
  --workspace "$BE_EVIDENCE_PARENT/final"
```

The build and complete restore exited 0. All 51,439 restored paths, sizes and
hashes were then checked again against the selected inventory. The bounded
actual records are published separately under
[`publication/extension-20261104`](../publication/extension-20261104/), in
`final-evidence-build/` and `final-evidence-restore/`; their restored workspace
is not duplicated in the repository. The source inventory, constituent
selection manifests and full native records are inside the archive.

One additional deliberately rejected packaging-control symlink is preserved
as a literal descriptor instead of being recreated. In the final restore,
`runs/extension_20261104/foundations/evidence-final-selection01/SYMLINK_FIXTURES.json`
records its exact original path, literal target and `lstat` metadata. The link
was never followed during packaging; all ordinary control files and its
rejection result remain included. This affects no numerical acceptance input.

Original execution paths and runtime identities remain literal evidence.
Restoring packs separately is intended for inspection. To rerun numerical
work in one new workspace, use the source package and fresh command recipe;
do not overlay these preserved execution trees onto it.
