# Opus review follow-up — 30 October 2026

The current source/PDF manifest is [validation.json](validation.json).
[OPUS_REVISION_NOTES.md](../../OPUS_REVISION_NOTES.md) records selective decisions.
The earlier publication directory and its manifest retain the 29 October stage.

- `checks/`: fresh complete entry, nine historical bounded checks and three scalar
  component checks; original stdout/stderr, versions, commands, return codes and
  input hashes are preserved. The mathematical programs and their pins are unchanged.
- `supplemental/`: exact comparisons and independent geometric/count diagnostics,
  with the component source hashes and scripts where available. Reports distinguish
  proofs from diagnostic examples. Local absolute paths record the actual run;
  adapt them to a fresh output location in another checkout.
- `build-snapshot/`: compiler evidence for the mathematical source snapshot.
- `build/`: final compiler evidence after adding the immutable source citation.
- `layout-and-commands.json`: rendered-page comparison, final visual review and
  matching of the PDF command text to the successfully executed CLI forms.

Exact execution does not establish an unperformed analytical or checker-semantic
proof. The entry conditions and structural premises remain explicit; the finite
base through 699 remains unproved. Every program ran without Python optimization;
LaTeX shell escape was disabled.

The mathematical source snapshot is [`df2dd2e4386a4e57f6b5194d0368fcae8b62f89b`](https://github.com/kolodziejek/berry-esseen-certificates/tree/df2dd2e4386a4e57f6b5194d0368fcae8b62f89b/manuscript/compact-v16). The final commit adds its citation and release metadata;
the PR body links the exact final commit. No self-referential commit hash is used.
