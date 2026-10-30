# Run from repository root; use fresh output paths.

python3 -I -B \
mathematics/fixed-target-v8/2026-10-28/isolated_entry_replay.py \
--output-dir runs/compact-v16-entry-review

python3 -I -B \
manuscript/compact-v16/tools/check_entry_claims.py \
mathematics/fixed-target-v7/2026-10-27/entry-proof.json

python3 -I -B \
manuscript/compact-v16/tools/recheck.py \
compact-v16-bounded-review

python3 -I -B \
manuscript/compact-v16/tools/check_revision_constants.py \
--output-dir runs/compact-v16-scalar-review
