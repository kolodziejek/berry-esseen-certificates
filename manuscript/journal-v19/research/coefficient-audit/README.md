# Signed coefficient family: optional exact algebra audit

This package audits a substantial algebraic family from Section7.2 of the manuscript. It is **outside the manuscript proof dependency graph**. It does not accept the Fourier integrals, acquisition schedule, published numerical exports or the all-index theorem. The analytic proofs and old complete numerical evidence remain in force independently of this audit.

The shortening experiment retained the moment, conditional-expectation, central-gap integration and shared-budget explanations. Its complete replacement did not shorten the selected text. The recommendation is to retain this software as an independent audit, without making it a new trusted component of the proof solely to move algebra out of the paper. See `SCOPE.md` and the length-experiment record for the exact boundary and measured outcome.

## Portable commands

The acceptance and comparison code uses only the Python standard library. It was tested with physical CPython3.12.14, assertions enabled. Run from this directory, substituting an unused output path:

```
python3 -I -B accept_objects.py proof_objects.json
python3 -I -B controls.py /tmp/coefficient-controls-new
python3 -I -B compare_actual.py /tmp/coefficient-comparison-new
python3 -I -B capture_validation.py /tmp/coefficient-validation-new
```

The last command captures all three checks with exact commands, complete streams, actual return codes, runtime identity and source hashes. Output directories are create-only. Do not use Python `-O` or `-OO`. No installation, network access, compiler, Boost or numerical integration is needed for these commands.

`native/contracted_kernel.py` and `native/signed_resource47_table.json` are byte-identical copies of the pinned sources. The comparison extracts only seven named original functions, preserving their AST bodies; it never executes the original module or its Fourier routines. The83 rows are the entire selected signed-resource output table. Each row supplies an actual previously established probability/geometry domain. The comparison reruns only cheap central and conditional-coefficient formulas on those rows; it does not reaccept the preceding acquisition or all83 numerical exports.

The separate `native-prefix/` supplement, when present, documents a complete original signed-stage **prefix** on14 selected input states. Its scope is likewise algebraic: no Fourier call or feedback-state acceptance is claimed. Its independently captured87,963 row outputs are compared against the new PSD contraction map. Read its own instructions and scope before replaying it.

Historical capture files may contain absolute paths identifying their original executions. Those paths are evidence metadata, not requirements for the portable commands above.

## What is checked

`proof_objects.json` contains28 externally fixed polynomial/quotient identities, seven signwise Gram/localizing moment matrices, eight derivative factorizations, three positive-square witnesses and25 degree-four tensor Bernstein inverse identities. The targets and domains are fixed by `fixed_targets.py` and the printed analytic contract, not by candidate-supplied targets. `accept_objects.py` checks exact coefficient equality using sparse polynomials over Python `Fraction`. It verifies the Bernstein transform by expanding the basis and reconstructing each monomial, independently of the combinatorial formula used to propose its coefficients.

The conditional and matrix inequalities derive from integration of nonnegative weights and squares under the same marginal. Their meaning is explained in `soundness.tex`; coefficient agreement alone cannot prove that an arbitrary input box describes a law. The map retains both signs, different positive/negative radii, zero support-deficit denominators, signed multiplication by the common first moment, and one shared outer budget.

The fresh validation rejects75 malformed or corrupted proof objects and five invalid applicability domains. Seven boundary fixtures include symmetric/skew Bernoulli laws, unequal sign radii, zero conditional variance, zero PSD rows, negative central values and one-budget pricing. Invalid applicability means that this map cannot be used; it is **not** a proof that a law is impossible.

Actual native correspondence was also tested exhaustively on the83-row table:166 central-bound calls and83 conditional-K calls agree exactly with the original functions. The separate signed-stage prefix comparison agrees on87,963 rows. These are independent implementation comparisons, not replacements for the analytic derivations or proof of the input-state premises.

## Discovery and acceptance

`propose_objects.py` records explicit manuscript coefficients and proposes the finite basis table. It is not used during acceptance. The acceptance target factory derives the central polynomials by signed integration, derives the conditional coefficients by differentiation/expansion and reconstructs the full weighted Gram entries. The square witnesses must have positive weights; derivative factors have a fixed permitted meaning and order. Missing, duplicated, reordered or corrupted cases reject. A success string in a candidate is not an accepted field.

`coefficient_map.py` then evaluates the accepted polynomial family on exact rational intervals. The common-law hypotheses remain obligations of its caller. The full acquisition targets were not replayed through this new map, so there is no claim that changing the old program to use this implementation preserves all numerical margins.
