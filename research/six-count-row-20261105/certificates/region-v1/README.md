# Exact closed-region pilot for n=5

This package proves the conditional positive closed-CDF comparison on
`p=[19/50,39/100]`, `k=2`, `u=[-1/100,1/100]`, with the original full
noise `[0,7687/25000]`, beta interval and `rho>=11/10`. It is a **partial
region**, not the complete original BN/p38 row and not a replacement for
the existing n=5 proof. Read `SOUNDNESS.md` for the mathematical reduction.

Use ordinary Python 3.12 or later; acceptance uses only its standard
library. Do not use `-O` or `-OO`. From this directory, with a fresh output
directory for each command:

```sh
python3 -I -B accept.py proof_object.json replay01 --k 2 --p 19/50 39/100 --u -0.01 0.01
python3 -I -B controls_v1.py proof_object.json controls01
```

The decimal command-line phase endpoints are converted exactly to
Fractions; the proof object contains canonical rational strings.
The reader requires the complete external rectangle, reconstructs its
dyadic cover, every common-moment expression, all tensor coefficients,
and twelve whole-ray targets per leaf. The bundled native files are
unaltered copies with fixed hashes and explicit provenance.

`discover.py` is optional SciPy/NumPy discovery. It is not needed for
acceptance. It can leave partial candidates; its successful exit code
does not itself imply complete coverage. The selected `proof_object.json`
has passed the separate `accept.py` process, as recorded under `evidence/`.
Those captures preserve original absolute runtime paths as historical
provenance; fresh commands above need no such workspace path.

Selected results: ten leaves, 120 ray checks, 18,000 exact tensor
coefficients; eighteen corrupt objects rejected, 57 inverse-transform
and 1,080 direct moment identities checked. Original acquisition remains
an inherited premise and has not been rerun in this package.
