# Joint-count certificates

The mathematical reduction is in Section 7.5 of the manuscript. A monotone
coupling of the actual conditional laws bounds every incoming count by
`W_k^4/(c-u)^4`. Combining this with a quartic, Cantelli, or zero minorant
gives four polynomial inequalities on complete unit squares. The near-phase
coordinates scale with the variance, so verification covers every positive
noise level, including arbitrarily small noise. Zero noise is Bernoulli.

The coefficients are exact rational data. Acceptance reconstructs each target
from the stated formulas, expands the Bernstein basis back into power
coefficients, and checks every coefficient sign. Checking complete native
input inventories and normalization inequalities supplies the quantitative
premises. The acquired same-law domains themselves remain conclusions of the
earlier manuscript argument and its preserved numerical families.

`tiny/` contains the uniform `n>=47` family. Its four polynomial arrays have
244 coefficients altogether and apply to all 83 acquired rows after the
complete input census. The target is unchanged:
`rho_B(C-C_B)<-lambda/1000`, for `0<lambda<=min(.05,row ceiling)`.

`finite/` contains the five complete finite families, 267 input rows in all.
The 65,148 coefficients retain the original sharp targets, positive-39
allowance and finite-binomial reserves. Read its `FINITE_RESULT.md` for
the exact actual-index, probability, score, support and noise premises.
Its normalization uses 17,115 freshly evaluated original rational gates.

Run with standard-library Python, assertions enabled, and a fresh output path:

```sh
python3 -I -B tiny/capture_all 83.py /tmp/joint-count-uniform-new
python3 -I -B finite/capture_finite.py /tmp/joint-count-finite-new
```

The capture saves actual return codes, stdout, stderr, input hashes and runtime
identities. It also runs corrupted-object and domain-substitution controls.
Never use `-O` or `-OO`. Hashes identify bytes; the mathematical argument and
checker semantics establish what their successful verification means.

The original acquisition, Fourier, finite-binomial reserve and larger-noise
evidence is indexed in
[`extended-v17/reproduction`](../../../extended-v17/reproduction/).
It is not rerun by these commands. The intermediate-noise `mid/`
staircase-quartic experiment is outside the manuscript's required dependency
graph. Its README supplies separate commands, proof, scope and exact controls.
It uses `tiny/` as a sibling for the unchanged acquired-input census.
