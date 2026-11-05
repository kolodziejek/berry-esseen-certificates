# Continuous six-count comparison: research checkpoint

This is a partial step toward shortening the 86-page manuscript in
[journal-v21](../../manuscript/journal-v21/README.md). It changes no selected
manuscript theorem or proof dependency and claims no page saving yet.

The previous pilot fixed both probability and phase. The new exact result
covers **n=5, p in [0.38,0.39], nearest threshold k=2, phase u in
[-0.01,0.01]**, and the **entire acquired noise interval [0,7687/25000]**.
It retains the original beta bounds, support ceilings and rho floor 11/10.
This is a conditional implication under the selected BN/panel38 acquisition.

| Result | Mathematical status | Execution status |
|---|---|---|
| Continuous narrow-phase score bound | Proved by the supplied common-moment reduction and exact certificate | Separate complete replay: 10 leaves, 120 global rays, 18,000 tensor coefficients |
| Complete threshold domain | Source-bound conditional reduction to nearest k=1,2,3; all six mixture counts retained | Original and relocated exact domain checks, 20 rejected mutations |
| Same-noise Gaussian refinement | Analytic convexity criterion proved in Proposition 3 | Independently differentiated and reviewed; no complete-row claim |
| Complete BN/panel38 row | Not proved by this checkpoint | Other phase regions remain unresolved here |
| Further manuscript shortening | Not yet established | journal-v21 remains 86 pages |

Read [the four-page analytic note](six_count_reduction.pdf).
The fixed outer variance polygon, nine shared skew choices and the
finite-sample fourth-moment bound reduce each probability/phase cell to
degree-(9,4) polynomial inequalities. All conditional counts use one common
pair of marginal laws. The certificate includes closed-event collisions and
both infinite rays; it is not a sample of probability laws.

The complete acquired threshold domain and its original source boundaries
are in [the domain proof](domain-package/work/count_row_20261105/domain/SOUNDNESS.md).
The old conditional flags in the contract are preserved. No acquisition
campaign is rerun or certified merely by a successful new arithmetic check.

## Reproduction

Use unoptimized Python 3, with the standard library only:

```sh
python3 -I -B -S reproduce.py /absolute/path/to/NEW_OUTPUT
```

This freshly runs the complete narrow-region reader, its 18 corruption
controls and the independent source-domain checker. Every output directory
must be new. NumPy and SciPy are needed only for coefficient discovery,
whose code is supplied separately.

The reader checks all 10 leaves, including every closed child face. The
controls additionally test 57 inverse Bernstein identities and 1,080 direct
moment-tensor identities. Domain controls include 972 independently expanded
polynomial identities and 104 exact atom collisions. These tests exercise
implementations; the continuous mathematical reasoning is in the proof note.

Preserved discovery and actual acceptance captures are in
`certificates/region-v1/evidence/`. Historical absolute paths describe those
actual executions. The local portable rerun is recorded separately under
`verification/`. Read [HANDOFF.md](HANDOFF.md) before extending the method.

