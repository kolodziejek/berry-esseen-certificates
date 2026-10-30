# Current publication record

The 30 October revision is recorded in [opus-20261030/](opus-20261030/README.md).
The following text and existing files describe the 29 October release; its
validation manifest and captures remain unchanged.

---

# Publication follow-up: source and execution record

This directory records the focused corrections made after review of the first
53-page revision. The complete revised proof and new scalar checkers are in
this manuscript directory. Historical `validation.json`, `checks-summary.json`
and `revision-validation.json` describe their respective earlier versions;
they are not the source manifest of this release.

The current manifest is `validation.json` in this directory. The immutable source snapshot is
[`b974df4ff28bf4876d98ca4a69ab31fb4e39d4e9`](https://github.com/kolodziejek/berry-esseen-certificates/tree/b974df4ff28bf4876d98ca4a69ab31fb4e39d4e9/manuscript/compact-v16).
The final release adds its source citation, release metadata and rebuilt PDF;
the mathematical arguments and checkers are unchanged. The PR body identifies
the exact final head commit too. No circular self-hash is claimed.

## Actual execution evidence

- `commands-copied-from-pdf.sh`: literal text extracted from the compiled PDF,
  parsed and matched to the three expected argv lists before execution.
- `copied-command-replay.json`: actual commands, return codes, times and hashes.
- `entry/`: fresh isolated 13-file retained-entry replay and its rejection controls.
- `bounded/`: all nine unchanged historical checks, source pins and output hashes.
- `scalar/`: all three new scalar checkers, current checker hashes and diagnostics.
- `followup-audit/`: independent signed-quotient diagnostics, CLI check and PDF
  command extraction. Those diagnostics supplement the four-endpoint proof.
- `build/`: final compiler captures and exact source/PDF hashes; `build-snapshot/` preserves the preceding source snapshot build.
- `final-layout-and-commands.json`: final rendered-page correspondence and unchanged copied command text.

Original captures can contain absolute paths recording the execution environment;
reproduce using the commands in the manuscript or parent README from your own
checkout. Every output directory must be new. Shell escape and Python optimization
are disabled. The full stdout/stderr are retained here; no PASS was inferred from
an earlier run or generated as a placeholder.

The entry uses retained mathematical kernels, not a second independent verifier.
Exact scalar checks do not prove the analytical reduction or finite base through699.
No theorem scope, threshold-atom convention or complete tail was weakened.
