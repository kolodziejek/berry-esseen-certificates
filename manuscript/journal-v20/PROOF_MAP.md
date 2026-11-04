# Proof and certificate map

The manuscript continues the complete v17 argument and its v18/v19 consolidations. All analytic proofs needed for the chosen route remain in the PDF. V20 replaces the small-noise incoming-tail calculation by a same-law fourth-moment comparison and new exact polynomial certificates. The original acquisition, Fourier and larger-noise branches remain dependencies.

Mathematical status: locally derived and reviewed computer-assisted proof candidate, using the stated published inputs. Execution status: the new small-noise families have fresh exact checking and bounded independent reviews; unchanged selected numerical obligations retain the completed v17 evidence. Neither agent agreement nor arithmetic acceptance constitutes an independent human review of the complete manuscript.

## Logical order

1. Published affine bounds, strict finite-binomial comparison and the fixed-law Esseen limit have their hypotheses stated in Section 1.
2. Section 2 proves ratio attainment, reflection, contact on the closed support, the physical defect and conservation. Compactness uses uniform integrability only for the first two moments. Atom collisions are retained.
3. Section 3 proves a uniform one-step recurrence. At a first strict failure above 42, the excess is below `3003/10250`, the score is below `73/175`, the predecessor loss is zero, and both deleted predecessors are sharp.
4. Section 4 proves the common certificate soundness rules. Section 5 supplies compensated Fourier inversion, the closed-event majorant, and full finite and infinite frequency estimates.
5. Section 6 proves the finite base: quantitative 1–3, physical four-summand comparison, 5, then 6–38, a separate positive allowance at 39, sharp 39, and actual 40–42. Its acquisition and comparison tools are proved in Section 7. This forward reference is an exposition order, not a circular dependency: those tools are conditional statements for one law.
6. Section 7 establishes the two local exclusions. The finite calculation has actual range 42–48. The uniform calculation covers every index at least 47. The small-noise comparison uses the new joint-count certificates below; its acquired domains are unchanged. Each support/confinement update consumes already proved data for the same law. Each bound retains its signed threshold, complete probability cover and original joint resource.
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
| `j:local:uniform` | `uniform47` | Complete zero-barrier acquisition and the preserved larger-noise comparisons; new small-noise objects cover all 83 surviving rows and every phase down to arbitrary positive noise |

The `public_count_acceptance` node records acceptance of all 1,243 selected untrusted candidate objects through the complete original readers. It does not establish their applicability by itself; the corresponding acquisition and directed joins are separate obligations.

## New small-noise dependencies

The analytic edge is explicit:

`same-law inward-spaced coupled counts -> cutoff R -> G(R)<=-1{W_k>u}+R0*W_k^4/(c-u)^4 -> four outgoing/moment witnesses -> exact polynomial identities -> signed score gate`.

The strict outgoing event remains `W_k>u`; incoming count collisions are included. The near-phase rescaling `u=z*t`, with `t=E W_k^2`, gives a loss relative to noise even as `t` tends to zero. The finite negative-loss cases use `min(m*eta*omega_minus,eta*omega_plus)`, retaining both the mass upper bound and the variance upper bound.

| New family | Complete input domain | Target and unchanged premises |
|---|---|---|
| `certificates/joint-count/tiny` | 38 left + 45 central rows; n>=47; 0<lambda<=min(.05,row cap); all phases | Original strict target `rho_B(C-C_B)<-.001lambda`; acquired same-law support, C>=.4, normalization |
| `certificates/joint-count/finite` | 78 positive39,48 central40,49 left40–42,45 left42–48,47 central42–48 rows | Original sharp, positive-39, and finite-binomial-reserve targets; all signed score caps, actual index bands and row ceilings retained |

The common uniform object has four polynomials. The finite family has four for each of its 267 rows. Acceptance verifies complete ordered input inventories, regenerates the original normalization inequalities, checks exact Bernstein identities and final strict gates, and rejects corrupted objects. It does not prove acquisition or the inherited finite-binomial reserve. Those remain separately established ancestors from the preserved ledger.

The old small-noise proof objects remain preserved as earlier evidence, but their exponential-tail and relative-tail calculations are no longer required by this new route. The common Bennett/Poisson lemma remains necessary for intermediate-noise and whole-count comparisons. No such larger-noise branch was removed on the strength of a small-noise result.

## Why the second tail proof can be removed

The old `strict700` node and its separate fixed-target route are not needed in this revision. This deletion has a mathematical justification, rather than a page-count justification:

- Ratio attainment applies also when `C_n=C_E`.
- The native uniform initializer has barrier zero and lower score `.4095`; it includes equality. Its stored value 98 does not impose an upper sample-size limit.
- Conservation, raw sign licensing, acquisition and confinement use the excess only as a nonnegative term. There is no division by excess.
- Every selected positive-noise local comparison proves `rho_B(C-C_B)<-.001 lambda` with its original target. The estimates remain proportional to arbitrarily small positive noise.
- At zero noise the actual law is Bernoulli, and Schulz's finite theorem is strict.

After the weak bound is known at every index, equality at any `n>=47` meets the uniform exclusion's hypotheses and contradicts attainment. The new strictness claim is therefore `C_n<C_E` for `n>=47`. Strictness at 42–46 is not inferred from this audit.

The detailed boundary audit and independent review remain in [`../journal-v18/review/`](../journal-v18/review/), at commit `8d09d3e018c9ab11b137a6551bb1dde68c559b96`. The v19 changes remain reviewed in [`../journal-v19/review/`](../journal-v19/review/). The current `review/joint-count/` contains the new bounded derivations, source/interface reviews and fresh execution evidence. All prior manuscripts, reference files and history remain unchanged.

## Review boundary

The review checked the new analytic arguments and their interfaces; it did not repeat certificate discovery. Original acceptance, fresh review of the new exposition, compilation and visual inspection are distinct forms of evidence. The separate 114-command restoration recipe has not been executed as one newly relocated campaign. No claim of eventual exact two-point optimality is made.

## Optional experiments are outside this graph

`certificates/joint-count/mid/` is a fully checked conditional alternative on `[.05,.08]`: 200 phase cells, all-real polynomial majorants, exact enlarged normalization and complete source-bound applicability. Of the 83 uniform input rows,71 intersect this noise band and12 have lower acquired ceilings. Its theorem and acceptance are recorded, but it is not required for the PDF's chosen route; the original MID/LOW comparisons remain. Adding this separate proof to the PDF would not justify deleting the remaining larger-noise machinery.

The previous [`coefficient audit`](../journal-v19/research/coefficient-audit/) and [`conditional-count pilot`](../journal-v19/research/conditional-count/) remain available. Their failed shortening experiments and CDF nonidentification examples are not ancestors of the theorem. The new domination does not identify a joint process from its own-count distribution: it proves a pathwise upper bound using the actual coupled conditional laws.
