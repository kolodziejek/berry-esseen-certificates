# Proof and certificate map

The manuscript is a consolidation of the complete v17 argument. Its analytic proofs are included in the PDF; the companion repository supplies the finite proof objects and acceptance programs. The old manuscript is not being cited as a substitute for an omitted analytic proof.

Mathematical status: locally derived and reviewed computer-assisted manuscript proof, using the stated published inputs. This is not proof-assistant certification or external referee acceptance. Execution status: the selected numerical obligations and their same-law domain joins were completed for v17; this revision changes neither their bytes nor their acceptance targets. It does not claim a new execution of the entire numerical campaign.

## Logical order

1. Published affine bounds, strict finite-binomial comparison and the fixed-law Esseen limit have their hypotheses stated in Section 1.
2. Section 2 proves ratio attainment, reflection, contact on the closed support, the physical defect and conservation. Compactness uses uniform integrability only for the first two moments. Atom collisions are retained.
3. Section 3 proves a uniform one-step recurrence. At a first strict failure above 42, the excess is below `3003/10250`, the score is below `73/175`, the predecessor loss is zero, and both deleted predecessors are sharp.
4. Section 4 proves the common certificate soundness rules. Section 5 supplies compensated Fourier inversion, the closed-event majorant, and full finite and infinite frequency estimates.
5. Section 6 proves the finite base: quantitative 1–3, physical four-summand comparison, 5, then 6–38, a separate positive allowance at 39, sharp 39, and actual 40–42. Its acquisition and comparison tools are proved in Section 7. This forward reference is an exposition order, not a circular dependency: those tools are conditional statements for one law.
6. Section 7 establishes the two local exclusions. The finite calculation has actual range 42–48. The uniform calculation covers every index at least 47. Each support/confinement update consumes already proved data for the same law. Each bound retains its signed threshold, complete probability cover and original joint resource.
7. Section 8 excludes a least strict failure and then excludes equality from 47 onward. One fixed Bernoulli law supplies the sharp lower limit.

## Numerical assertions and preserved evidence

The immutable evidence index is [`extended-v17/reproduction/COMPLETION_LEDGER.json`](../extended-v17/reproduction/COMPLETION_LEDGER.json) at commit `c31d0cbe2af867d26871fbae37a3a7f4066f4a55`. Each node below identifies its full source/candidate inventories, execution records, hypotheses and domain joins. Restoration and acceptance commands are in [`REPRODUCE.md`](../extended-v17/reproduction/REPRODUCE.md). A result hash is an integrity check, not a mathematical proof.

| New manuscript interface | Preserved ledger node(s) | Meaning of the finite check |
|---|---|---|
| `j:fourier:scalar-cosine`, compatible modulus profile | `scalar_fourier` | Exact scalar polynomial positivity and profile gates |
| `j:finite:n123` | `n1_3` | Closed threshold covers, pointwise majorants and same-iid expectation inequalities |
| `j:finite:n4numerical` | `n4` | Complete 260-parent physical comparison; all parent/child alternatives, threshold joins and tails |
| Fifth-index part of `j:finite:numerical539` | `n5`, `public_count_acceptance` | Full signed moment cover, count forests, positive corner and Fourier complements |
| Actual-index support and indices 6–14 | `n6_14`, `sign_mass`, `public_count_acceptance` | All 51 support rows, score/Fourier inputs, 2,200 probability panels and complete count objects |
| Indices 15–38 and weighted uses of 25/31 | `n15_38`, `weighted_transfer`, `public_count_acceptance` | Actual-index support and counts, full moment complements, weighted resource and directed domain containment |
| Positive-39 prerequisite | `positive39` | Separate local comparison establishes the own-score cap before sharp-39 acquisition |
| Sharp 39 | `sharp39`, `public_count_acceptance` | Actual-index resources and sharp count comparisons consuming that cap |
| `j:finite:numerical4042` | `actual40_42` | Actual 40, 41 and 42; weighted floor, two-endpoint support, finite binomial slack and all signed local branches |
| `j:local:finite42` | `local42_48` | Complete acquisition and local comparison on actual 42–48, including 184 probability cells and the separate finite amplitude profiles |
| `j:local:uniform` | `uniform47` | Complete zero-barrier acquisition and six local comparisons, including all 83 surviving probability rows, all phases and arbitrarily small positive noise |

The `public_count_acceptance` node records acceptance of all 1,243 selected untrusted candidate objects through the complete original readers. It does not establish their applicability by itself; the corresponding acquisition and directed joins are separate obligations.

## Why the second tail proof can be removed

The old `strict700` node and its separate fixed-target route are not needed in this revision. This deletion has a mathematical justification, rather than a page-count justification:

- Ratio attainment applies also when `C_n=C_E`.
- The native uniform initializer has barrier zero and lower score `.4095`; it includes equality. Its stored value 98 does not impose an upper sample-size limit.
- Conservation, raw sign licensing, acquisition and confinement use the excess only as a nonnegative term. There is no division by excess.
- Every selected positive-noise local comparison proves `rho_B(C-C_B)<-.001 lambda` with its original target. The estimates remain proportional to arbitrarily small positive noise.
- At zero noise the actual law is Bernoulli, and Schulz's finite theorem is strict.

After the weak bound is known at every index, equality at any `n>=47` meets the uniform exclusion's hypotheses and contradicts attainment. The new strictness claim is therefore `C_n<C_E` for `n>=47`. Strictness at 42–46 is not inferred from this audit.

The detailed boundary audit and independent review are included in `review/`. The old v17 theorem, evidence and history remain unchanged.

## Review boundary

The review checked the new analytic arguments and their interfaces; it did not repeat certificate discovery. Original acceptance, fresh review of the new exposition, compilation and visual inspection are distinct forms of evidence. The separate 114-command restoration recipe has not been executed as one newly relocated campaign. No claim of eventual exact two-point optimality is made.
