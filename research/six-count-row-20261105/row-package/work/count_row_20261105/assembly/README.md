# Complete-row exact acceptance protocol

The selected epoch is V4. `complete.py` and `READER_SOURCES.json` preserve the earlier V3 protocol; V3 full-root candidates were partial and must not be selected as V4 evidence. The new mathematics and its exact scope are in `MATHEMATICAL_REVIEW.md` and `../domain/SOUNDNESS.md`.

Once the three V4 objects exist, run from the workspace root:

```sh
python3 -I -B -S work/count_row_20261105/assembly/select_v4.py \
  runs/count_row_20261105/SELECTED_COMPLETE_V4.json \
  --k1 runs/count_row_20261105/construct_k1_v4_repair01/objects/proof_object.json \
  --k2 runs/count_row_20261105/construct_k2_v4_repair01/objects/proof_object.json \
  --k3 runs/count_row_20261105/construct_k3_v4_campaign01/objects/proof_object.json

python3 -I -B -S work/count_row_20261105/assembly/complete_v4.py \
  runs/count_row_20261105/SELECTED_COMPLETE_V4.json \
  runs/count_row_20261105/analytic_complete_row_v4_01
```

Both outputs are create-only. The selection records candidate bytes and validates their external root headers; it is not numerical acceptance. The second command actually invokes the unchanged V4 reader on all three whole objects, including a fresh k3 replay. It needs only the standard library. It does not execute discovery or import SciPy/NumPy.

Use a fresh selection/output name for another attempt. An unfinished candidate is preserved and rejected, not treated as acceptance. A failed native root gets a full observation and FAILED.json; no full-row RESULT.json is written. A successful RESULT identifies every actual root, object/result/stream/source hash and the complete census. It proves only the displayed conditional original-row score implication. Source integrity and process success do not themselves establish analytic acquisition.

The exact reader closure is frozen by READER_SOURCES_V4.json, SHA256:

    ffa814c525fceaafe39e47e9352b544557ffb83d3225f5329ceba55180474589

If a mathematical reader changes, create an explicitly new epoch and review it; do not edit the pinned reader or relax these gates. Historical absolute paths in captures describe actual executions.

Bounded controls can be repeated at a fresh workspace output:

```sh
python3 -I -B -S work/count_row_20261105/assembly/check_assembly_v4.py \
  runs/count_row_20261105/OTHER_NEW_ASSEMBLY_CONTROLS
```

Those controls exercise deliberately invalid synthetic objects, not real row certificates. They prove rejection behavior and include one actual unchanged native failure. No whole-row completion is implied by their successful status.
