This directory contains an independent domain and algebra audit for the original n5 BN/panel38 contract. It contains no accepted full-row score forest.

From the workspace root, using ordinary unoptimized Python:

```sh
python3 -I -B -S work/count_row_20261105/domain/check_domain.py /absolute/path/to/NEW_OUTPUT
```

The output path must not exist. `domain.py` can create an exact source-bound domain JSON at a new file path; `check_domain.py` reads the frozen `domain.json` beside it. The scripts use only the standard library, verify the original contract/resource identity and preserve all original scalar fields. They read the listed historical acquisition artifacts without rerunning acquisition or accepting their flags as a proof.

Read `SOUNDNESS.md` for the independent coordinate/coverage proof, the six signed roots, reflection and atom conventions, and the precise fixed-polygon degree(9,4) conditions. The full mathematical hypotheses remain those of the original acquired row. Successful domain checks are not a successful score certificate.
