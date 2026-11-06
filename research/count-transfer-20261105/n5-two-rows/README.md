# Two complete n=5 transfer comparisons

The exact reader has freshly checked the entire original B0/p50 row and the
B2 S3 endpoint/p34 row, conditional on their original same-law acquisition.
B0/p50 has 383 leaves; B2 has 54. These are positive closed-CDF comparison
implications at the original C_E target (K=0). They are not a fresh proof of
acquisition, all n=5 cases, or the full conjecture. See COMPLETION.json for the
exact source contracts, complete root census, selected object/result hashes,
and actual arithmetic counts.

`proof/SOUNDNESS.md`, `proof/THEORY_V4.md` and `proof/TRANSFER_PROOF.md` give the
mathematical argument and its extensions. The code retains one common pair
of conditional laws across all six binomial counts. Each selected leaf
checks quartic majorants on both complete real rays and a positive tensor
Bernstein expansion on the full closed probability/phase cell. The original
noise, rho, beta, support, mean and threshold premises are unchanged.

## Reproduce with Python 3.12 and its standard library

Run from the package directory (do not use -O or -OO). Outputs must be new
paths outside this immutable directory. These commands need no NumPy/SciPy:

```sh
python3 -I -B portable.py verify
python3 -I -B portable.py controls --out ../transfer-controls-new
python3 -I -B portable.py smoke --out ../transfer-smoke-new
python3 -I -B portable.py replay --row B0_50 --out ../B0-replay-new
python3 -I -B portable.py replay --row B2_S3_34 --out ../B2-replay-new
```

The last two commands freshly recompute every selected leaf. The smoke checks
only the small complete B2 k=3 root. Discovery required NumPy/SciPy; acceptance
does not. There is no claim of an independently written second full reader:
the separate exact replay uses the reviewed same acceptance implementation.
Independent derivations and coefficient/endpoint tests are preserved under
evidence/review_*. The current reviewer source snapshot is separate; historical
records retain their original hashes, including earlier prose versions. These
review receipts are not advertised as portable runnable review closures. Historical capture argv retain original absolute paths as
provenance; the portable commands generate new selectors using this location.
Hashes establish byte identity, not mathematical truth.

## Unfinished BN39 transfer

The package does not claim the BN39 row complete. Its bounded construction,
including initial failures, complete k1/k3 candidate objects and the final
bounded k2 object, is preserved under research/. A negative discovery margin
on a coarse box was not a law or relaxation obstruction: a finer exact cell
passed. Failed leaves remain unresolved; no success marker admits them.

Inspect COMPLETION.json and the candidate RESULT before continuing. To
replay a complete root candidate separately:

```sh
python3 -I -B code/accept.py research/construct_BN39_k1_refined01/objects/proof_object.json ../BN39-k1-new --row BN39 --k 1
python3 -I -B code/accept.py research/construct_BN39_k3_refined01/objects/proof_object.json ../BN39-k3-new --row BN39 --k 3
```

The root reader's fixed domain comes from the unchanged original contract.
For a partial k2 tree, code/repair.py can attempt bounded further discovery;
a fixed resumable command (requires NumPy/SciPy) is:

```sh
python3 -I -B code/repair.py research/construct_BN39_k2_refined01/objects/proof_object.json ../BN39-k2-repair-new --row BN39 --k 2 --extra-depth 2
```

This rechecks retained leaves before attempting only failed cells. It does not
guarantee completion; run a separate exact reader afterward. No further brute refinement
is recommended without assessing the new polynomial Gaussian bound being
investigated separately. Discovery is not required to reproduce the two
completed rows.

The package preserves the actual complete captures and controls. Relocated
byte verification, small-root replay and controls are recorded outside this
package; they do not imply another relocated full B0/B2 replay. FILES.json
covers every included file except itself. No frozen original or historical
capture was rewritten.
