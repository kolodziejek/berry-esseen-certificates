# Direct-comparison certificates

Extract each archive into its own new directory and run its commands from
that package root. Preserve its internal `work/` and `runs/` hierarchy.
Use unoptimized Python 3 with the standard library and `-I -B`; never use
`-O` or `-OO`. Recorded exact runtimes are CPython 3.12.12 or 3.12.14.
NumPy and SciPy are used for coefficient discovery, not these acceptance
commands. Every output destination must be new. Replace `/fresh/...` or
the relative `runs/reproduce-...` names with suitable fresh destinations.

| Archive | Conditional numerical implication | Archive SHA-256 |
|---|---|---|
| `left.zip` | All 39 raw left rows, every `n >= 47`: exact index caps and 3,385 retained comparisons | `b74b0b5fbccd774a0729cdc7b4666ddcd9b248b203dbb254ec45e09a8b085397` |
| `earlier.zip` | 78 positive-39, 291 actual 40–42 and 368 actual 43–46 comparisons | `53dc19350d841290835bce2fc8dc0d5ab2e433bbafc49eebd52df004d26b292f` |
| `central.zip` | 45 original central rows: 25,908 pairs at 47–999, plus the explicit tail for all `n >= 1000` | `2dabdd6d9d8c5840a194ad71f78b7f5fff90c27d8d2b8e0a75463c18b14090f1` |

All three hashes above match the published archive bytes. A ZIP digest and internal file inventory establish byte
integrity. Exact replay establishes the reader's finite inequalities.
The manuscript proves why the reader's targets cover the same iid law;
attainment, contact, Fourier bounds and original acquisition are not proved
by a file hash or an arithmetic success message.

## Left package

Run the complete gap/cap and comparison replays, followed by their controls:

```sh
python3 -I -B tools/capture.py /fresh/left-gaps gaps/accept_gaps.py all '{output}/accepted' gaps/proof_object.json
python3 -I -B tools/capture.py /fresh/left-gap-controls gaps/controls.py '{output}/accepted'
python3 -I -B tools/capture.py /fresh/left-comparison \
  work/finite_left_replacement_20261104/audit/complete_strong_campaign.py \
  --input runs/finite_left_replacement_20261104/root_strong_shard0_01/objects \
  --input runs/finite_left_replacement_20261104/root_strong_shard1_01/objects \
  --input runs/finite_left_replacement_20261104/root_strong_shard2_01/objects \
  --input runs/finite_left_replacement_20261104/root_strong_shard3_01/objects \
  --discovery-result runs/finite_left_replacement_20261104/root_strong_shard0_01/objects/RESULT.json \
  --discovery-result runs/finite_left_replacement_20261104/root_strong_shard1_01/objects/RESULT.json \
  --discovery-result runs/finite_left_replacement_20261104/root_strong_shard2_01/objects/RESULT.json \
  --discovery-result runs/finite_left_replacement_20261104/root_strong_shard3_01/objects/RESULT.json \
  --output '{output}/accepted'
python3 -I -B tools/capture.py /fresh/left-comparison-controls tools/comparison_controls.py '{output}/accepted'
```

The regenerated gap result must have SHA-256
`d6b53cc0f4ec90d48105ea0d59b75819a704285504769ca592252ec1b0ccfce4`.
The comparison requires all 3,385 pairs and checks every leaf; its status is
`PASS_EXACT_COMPLETE_STRONG_RESOURCE_3385_RAW_LEFT_PAIRS`. A census-only
check is not acceptance. `COMPLETION.json` records the completed workspace
and full portable replays and their controls. The preserved discovery
outputs supply proposed objects, not trusted mathematical conclusions.

## Earlier package

```sh
python3 -I -B replay.py /fresh/earlier-comparison
```

This verifies the complete package inventory and freshly accepts all 737
objects with `--complete`. It checks the original source projections,
finite binary bounds, global quartics, signed 48-corner inequalities and
complete count/phase covers. The positive-39 target is
`C_E + 741/(4000*39)` throughout, including the cubic correction and reserve.
The other cases use `C_E` and retain their acquisition floors 40 or 42.

The preserved full workspace acceptance has result SHA-256
`92c9f2f231292289b20205434e66f6f67b3985c9be1f9bf3ce7bfee9bb2e0c08`.
The recorded relocation verified every packaged byte and accepted six
selected cases. It was **not** a full relocated 737-object replay. The
command above performs that full check for the reader. Do not rerun the
archived `run_complete01.py`, whose output paths belong to the original
campaign. The 25 upstream source/interface files bind the acquisition
inputs; this replay does not re-execute their acquisition ancestors.

## Central package

From its extracted root, first select an unoptimized interpreter:

```sh
BE_PY=/absolute/path/to/python3
```

To recompute every finite binary gap and compare the mathematical table
with the fixed input consumed by the comparison:

```sh
"$BE_PY" -I -B work/central_comparison_20261104/finite/campaign/launch_gap_shards.py \
  runs/reproduce-central-gaps
"$BE_PY" -I -B work/central_comparison_20261104/finite/campaign/collect_gaps.py \
  --input runs/reproduce-central-gaps/shard0/accept \
  --input runs/reproduce-central-gaps/shard1/accept \
  --input runs/reproduce-central-gaps/shard2/accept \
  --input runs/reproduce-central-gaps/shard3/accept \
  --output runs/reproduce-central-gap-union
"$BE_PY" -I -B - <<'PY'
from pathlib import Path
import json
old = json.loads(Path('work/central_comparison_20261104/finite/campaign/native/gaps_campaign.json').read_text())
new = json.loads(Path('runs/reproduce-central-gap-union/RESULT.json').read_text())
for key in ('status', 'row_n_pairs', 'count_pairs', 'closed_branch_cells',
            'minimum_epsilon', 'gaps', 'sources'):
    if old[key] != new[key]:
        raise SystemExit('Reproduced mathematical gap table differs: ' + key)
print('Exact finite gap table and source identities agree.')
PY
```

Execution-path metadata changes after relocation, so whole-file hash
equality is not required here. Do not replace the pinned table or rerun
the one-time data binder. Recheck every finite comparison object with:

```sh
"$BE_PY" -I -B work/central_comparison_20261104/finite/campaign/launch_cover_replays.py \
  proof_objects/cover runs/reproduce-central-covers
"$BE_PY" -I -B work/central_comparison_20261104/finite/campaign/collect_cover_replays.py \
  --input runs/reproduce-central-covers/shard0 \
  --input runs/reproduce-central-covers/shard1 \
  --input runs/reproduce-central-covers/shard2 \
  --input runs/reproduce-central-covers/shard3 \
  --output runs/reproduce-central-union
```

The complete table contains 25,908 retained pairs; all remaining row/index
pairs in 47–999 are excluded by the exact defect budget. The required
comparison status is `PASS_EXACT_COMPLETE_CENTRAL_FINITE_COMPARISON`.
It must come from the complete replay and join, not from discovery alone.

The portable tail supervisor runs the unchanged numerical readers, using a
system temporary directory and recording both actual child executions:

```sh
"$BE_PY" -I -B replay_tail.py /fresh/central-tail
```

It checks all 45 row premises, the serialized object, 21 rejection controls
and the common four-quartic envelope. The fresh relocated tail result matches
the original exact accepted result byte-for-byte.

The finite comparison's full relocated four-shard replay and coverage join
passed, with final result SHA-256 `edbc026fc8f4052a343787852c38a2376b103e028babbd95ffaaf96d69295132`. It accepts all
25,908 pairs and 112,438 quartics; all 24 new cover-capture
controls reject their malformed inputs. The finite binary gaps were fully
replayed in the original workspace; relocation verified their bytes and one
complete critical panel, without a second full gap campaign.

The archive roundtrip verifies every file by path, size and digest. It is
an integrity check, not another numerical replay. `COMPLETION.json` records
the precise execution boundaries and source/result joins. Preserved analytic
drafts inside the archive retain their historical pending labels; the final
manuscript and completion record state the completed scope.

## Relation to the original evidence

The original selected proof data and execution ledger remain in
`manuscript/extended-v17/reproduction` at commit
`c31d0cbe2af867d26871fbae37a3a7f4066f4a55`. They supply the unchanged
1–38/sharp-39 counts and acquisition ancestors. No new run of that entire
campaign, or of its separate 114-command relocated recipe, is claimed.
Historical absolute paths in archived receipts describe their actual
executions; new captures retain their own command, runtime, source hashes,
streams and exit code. Old confinement, MID/LOW and Poisson comparison
calculations may remain preserved or byte-pinned without being selected
mathematical ancestors of the new direct comparison.
