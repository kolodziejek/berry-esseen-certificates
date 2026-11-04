# Complete algebra-prefix comparison

This optional audit is outside the manuscript's theorem dependency graph.
It compares the newly derived moment-matrix contraction with every reached
algebraic cell in the original INITIAL47 grid, before any Fourier evaluation.
It does **not** rerun the full INITIAL47 acceptor or validate its feedback
states, exported remainder, resource bounds or Berry–Esseen conclusion.

`native/` contains byte-identical copies of the five required original inputs.
Their fixed hashes are checked before use. `capture_prefix.py` parses the
original `stage` function and retains its exact AST prefix, initialization,
four nested grids and rejection gates. It stops immediately before the first
`k.sixth` call. Tripwires reject any numerical Fourier call. Its input states
are the initial state and the 13 stored feedback states; these are inputs to
this comparison, not newly verified outputs.

The complete prefix visits 258,048 grid cells and captures 87,963 reached
rows in 14 stages. `compare_psd.py` recomputes the fourth/fifth/sixth moment
contractions from primitive moments and support bounds, using the separate
coefficient map. It compares all four outputs exactly: `c4u`, `Mc`, `etac`
and `corrections`. Each row is interpreted under the same-law analytic
premises proved in the manuscript. Finite equality tests cannot establish
those premises.

## Reproduce

Use unoptimized Python 3.12; no third-party Python package is required.
From this directory, choose two nonexistent output directories:

```sh
python3.12 -I -B capture_prefix.py /tmp/be-prefix-new
python3.12 -I -B compare_psd.py /tmp/be-prefix-new /tmp/be-psd-new
```

The capture refuses an existing destination. The comparison can also use the
supplied `evidence/` directory as its first argument. Both write input hashes,
runtime identity and a result. For an outer process receipt, redirect stdout
and stderr and record the real exit code; the included evidence preserves
the actual captured process records verbatim.

The fresh packaged capture reproduced the earlier compressed row stream
byte for byte: SHA-256
`6b66b6b53dc928a42e783ea2005fed04b38aab8b4a377c5cc41dc9f51d04b134`.
`CAPTURE_MANIFEST.json` inventories that capture and its native inputs.
The surrounding package manifest covers the final audit, including the
subsequent exact comparison evidence.

Historical absolute paths in receipts identify the actual machine and run.
They are not needed by these portable commands. Do not run
`native/accept_initial47.py` as a substitute for the full manuscript
reproduction recipe: this small capsule intentionally contains only the
files needed for the prefix audit.
