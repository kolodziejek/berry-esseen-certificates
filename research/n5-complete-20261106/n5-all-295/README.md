# Portable Complete 295-Contract `n = 5` All-Taylor Package (`n5-all-295`)

Self-contained stdlib-only (`python3 -I -B -S`) verification package for **all 295 original acquired `n = 5`, `K = 0` contracts** (`B0`: 24, `BN`: 32, `B2`: 104, `B3`: 135; `903` nearest-integer threshold regions, `3,589` curvature-corrected 4-pair all-Taylor leaves vs. `75,178` legacy `COUNT` leaves — **20.95x** reduction).

## Commands

```bash
# Verify byte inventory (FILES.json + TARGET.json)
python3 -I -B -S research/n5-complete-20261106/n5-all-295/portable.py verify

# Replay a single root smoke check
python3 -I -B -S research/n5-complete-20261106/n5-all-295/portable.py smoke --out /tmp/n5_all_smoke

# Run all 50 negative and corruption controls
python3 -I -B -S research/n5-complete-20261106/n5-all-295/portable.py controls --out /tmp/n5_all_controls

# Replay all 295 contracts (903 roots, 3,589 leaves) and 4-band domain join
python3 -I -B -S research/n5-complete-20261106/n5-all-295/portable.py replay --out /tmp/n5_all_replay
```
