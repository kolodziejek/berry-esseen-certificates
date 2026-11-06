# Next scope for the count-specific quartic method

The immediate next target is the other **294 selected five-summand contracts**,
with their original acquisition and signed-moment cover retained. Replacing
those contracts would simplify the numerical n=5 comparison. It would not yet
remove the manuscript's generic count argument, which is also used at later
indices, or its separate gap-free fifth-index corner. No page saving is claimed.

This is a read-only source/domain audit. Mathematical status: the proposed
extensions below still need their general analytic rules and accepted complete
covers. Execution status: the contract census passed freshly; no old numerical
campaign was rerun and no new comparison campaign was launched.

## What the other contracts actually contain

The selection is the immutable `files_sha256` map in
`work/cutoff5_20261020/root/final_composition_v2/C5_CHECKED.json`.
I rehashed all 295 selected contract files and their 295 old COUNT receipts.
Every contract has one row, actual n=5 and K=0, and exactly the same field set.
All contain the outward supports, rho interval, independent noise cap, beta,
mean, signed third moment, physical inward cap, scale, both threshold bounds,
and the `ACTUAL_SIGN_CONDITIONED_MARGINAL_V1` schema with centered conditional
laws and strictly positive closest-sign endpoint lower bounds.

| Original band | Selected contracts | Enclosing p range | Nominal rho region |
| --- | ---: | --- | --- |
| B0 | 24 | [.37,.61] | [1,1.1] |
| BN | 32 | [.34,.66] | [1.1,1.15] |
| B2 | 104 | [.32,.66] | [1.15,1.185] |
| B3 | 135 | [.31,.67] | [1.185,1.2] |

These enclosing ranges are not assertions that every p/rho combination is a
surviving contract. B2/B3 contain several distinct signed/moment slabs, and
some individual rho upper endpoints are smaller than the nominal band limit.
The exact tuple `(path, actual index, p interval, rho interval, signed domains)`
must identify a row; `(band,panel index)` alone is not always unique.

Of the 295 contracts, 195 end at or below p=1/2 and 100 start at or above it;
none straddles it in its interior. All physical inward caps lie strictly
between zero and one. Only 56 satisfy the stronger convenience guard
`inward < min(p_lo,1-p_hi)`. Thus the sign-conditioned derivation, rather than
that unnecessary guard, is essential to a general reader.

The raw bound `5p-Hminus*scale_upper <= z <= 5p+Hplus*scale_upper` gives the
following conservative nearest-count root sets without clamping:

| Threshold roots k | Number of contracts |
| --- | ---: |
| 1,2,3 | 177 |
| 2,3 | 5 |
| 2,3,4 | 88 |
| 1,2,3,4 | 24 |
| 1,2 | 1 |

All roots must keep both closed phase halves and all ties. The six mixture
counts j=0,...,5 are different objects. The original count capsules often use
the larger six-root cover; a replacement may use the smaller sets only with
this explicit raw-threshold derivation and whole-domain joining.

The historical `resource_verified=false` and `cutoff_proved=false` fields are
present in all 295 contracts. They remain unchanged. Their applicability comes
from the later complete n=5 acquisition/assembly, not from the contract flag,
an old COUNT marker, or this census. The selected v17 ledger records n5 as 31
parents, 326 frames, 12 regions, 70 closed signed arrangements, 295 forests and
75,178 leaves. Its final assembly record is
`runs/extension_20261104/coordinator/n5-v3-complete02/assembly/RESULT.json`.

The helper for the current BN row shows the provenance of the fields:
`contract_helpers.py` derives beta/mean/gamma/sign endpoints from the same
resource frame, derives the independent noise/scale cap from the mean, and
derives the physical inward cap from a gap price. It does not identify the
physical inward cap with the affine resource intercept `d0`. Retaining these
derived inputs retains their analytic gap/resource licenses.

## Three concrete next rows

The first row is a close transfer test. The second tests the probability-side
and low-rho changes. The third tests a higher signed-moment slab with weak sign
gaps. Their old leaf counts describe previous work, not expected difficulty of
the new method.

1. **BN panel 39**, old 809 leaves.
   Contract:
   `work/cutoff5_20261020/root/count5_prepare_v1/gamma16_01/n5/BN/panel039/contract.json`.
   SHA256 `8d2a6ec51bf43b45a7ce2de62d5ed734a90498924cb60c833a3976394eef3d9a`.
   Domains: p in [39/100,2/5], rho in [11/10,23/20],
   noise in [0,12941/40000], beta in [-12801/250000,59677/200000].
   Outward supports are 658801/10^6 and 724801/10^6;
   physical inward cap 207643/250000. The conservative threshold roots are
   k=1,2,3, each with u in [-1/2,1/2], or a proved clipped subdomain.

2. **B0 panel 50**, old 212 leaves.
   Contract:
   `work/cutoff5_20261020/root/count5_prepare_v1/pilots01/n5/B0/panel050/contract.json`.
   SHA256 `2939dcca05896e1c6393c50944df8dd5e872efb26076a7304df45d9f6d07a93f`.
   Domains: p in [1/2,51/100], rho in [1,11/10],
   noise in [0,32813/125000], beta in [-126629/10^6,159997/10^6].
   Outward supports are 600001/10^6 and 665001/10^6;
   physical inward cap 461037/10^6. Threshold roots k=2,3 suffice by the
   same source-bound calculation. This row includes p=1/2 and a rho floor of
   one, so the zero-noise and probability-boundary behavior must remain literal.

3. **B2 S3 endpoint panel 34**, old 731 leaves.
   Contract:
   `work/cutoff5_20261020/root/count5_prepare_v4/B2_S3_endpoint02/n5/B2/panel034/contract.json`.
   SHA256 `a9e2574fbb79e8d21d7bf6d5a9bc152ba6981878101c0dafd3eb7088233ba6d5`.
   Domains: p in [17/50,7/20], rho in [467/400,237/200],
   noise in [0,206391/10^6], beta in [1/5,8473/25000],
   signed third moment in [46599/125000,717493/10^6].
   Outward supports are 489501/10^6 and 155043/250000;
   physical inward cap 994857/10^6. The closest-sign gaps are only
   1857/500000 and 3571/500000. Threshold roots k=1,2,3 suffice.
   Its S3/endpoint identity must remain part of the selection; a generic
   unsplit B2 panel is not the same premise.

## General proofs and reader changes required first

* **Both probability sides.** The common-law moment and beta-polygon proof
  already works for any 0<p<1. V4's scalar enclosures use increasing pq on the
  left half, however. A general reader needs v_min from the two endpoints and
  v_max from the endpoints and 1/4 when the cell meets 1/2. The Gaussian
  numerator remains sign-sensitive; the negative-phase curvature test must use
  these general extrema. The mean/noise function is increasing in v when its
  explicit gate holds, not necessarily increasing in p. Derive these rules;
  do not simply remove the p-side restriction in code.
* **Original orientations.** Direct right-half evaluation is preferable to an
  unproved reflection shortcut. Reflection swaps conditional classes and
  signed moments and turns a closed CDF event into the complementary open
  event. The acquired frames are asymmetric. Reusing a left-half proof object
  requires a proved transformation of every field and endpoint convention.
* **Common resources and exact slab identity.** Read the row's own rho/beta/
  gamma/mean and sign endpoints, preserve their one-law provenance, and cover
  its original noise domain. A smaller cap follows only from a proved necessary
  constraint. The affine `Lambda` remains a resource intercept; substituting
  `acquired_lambda_upper` into its joint-budget denominator would change the
  hypothesis. Model V4 currently needs only a subset of these resources, which
  is a valid relaxation but may be too weak on another row.
* **Moment relaxations and degeneracies.** Keep one common vertex/gamma pair
  across all counts and the rho numerator. A slab with an empty/degenerate
  polygon cannot be silently skipped merely because the current reader rejects
  it. Handle segments, points, or a proved infeasibility certificate. Preserve
  zero conditional variance, zero total noise and event-plane atoms.
* **Whole-family applicability.** Parameterize external row identity and the
  complete root census, with duplicate/missing-row rejection and source-bound
  acquisition joins. An accepted cell does not establish the original band
  union. The remaining 294 contain multiple B2/B3 signed arrangements; all
  boundary overlaps and the separately handled fifth-index corner must survive.
* **Later n is another extension.** It needs n+1 count majorants, the coefficient
  3(1-1/n), and p degree n+4 rather than 9, as well as those indices' actual
  acquired inputs and weighted floors. No audit here establishes a common input
  schema or feasible certificates for n=6,...,39.

## Exactly what could change in journal-v21

Page numbers below refer to the actual 86-page release02 PDF, SHA256
`e15bf3de23795e3312b68fc08e97dc6d8bc9bdb835c0ede8647ec19f841fe0f7`.
They were read from its generated aux/toc, not estimated. The current v21
`sections/finite.tex` and `sections/local.tex` are byte-identical to that build.

| Current passage | Possible effect of a completed replacement | What must remain |
| --- | --- | --- |
| Section 6.5.1, p.41; (36)–(38), exact conditioning/common moments | Reuse and consolidate with the new common-variance proof | Same-law conditioning, closed events, support fourth-moment proof |
| Section 6.5.2, pp.41–43, outgoing quartic and Cantelli/MGF/Chernoff alternatives; (39) | Superseded only for consumers fully covered by the new count-specific global majorants | Remains for every old COUNT consumer still selected |
| Section 6.5.3, p.43, normalized-vertex (40), Proposition 6.8 | Replace by the beta-polygon/whole-cell criterion for replaced consumers | Complete finite cover, signed normal/rho normalization, threshold census |
| Sections 6.5.4–6.5.7, pp.43–46, cubic/physical-defect filters, noise floors and extra outgoing event | A count-only filter can disappear only when no retained proof consumes it | Mean, sign, physical-gap and resource lemmas still needed to acquire any new input; necessary exclusions still used by the domain cover |
| Section 6.6, pp.46–47, Proposition 6.9, signed fifth-index corner | No replacement established by the 295-contract program | Its separate gap-free positive signed rectangle and all-real-threshold proof |
| Section 6.7, pp.47–49, complete n=5,...,39 numerical assembly | Replace the selected n=5 COUNT edge after all 295 contracts and their joins pass | Support/Fourier complements, signed-corner union, original acquisition, predecessor induction and positive-39-before-sharp-39 |

In particular, even replacing all n=5 contracts leaves Section 6.5 in use by
the v21 ledger nodes `n6_14`, `n15_38`, and `sharp39`. Replacing n=5,...,38
still leaves the sharp-39 count consumers. The selected `public_count_acceptance`
node currently admits 1,243 original objects across those families; it cannot
be removed merely because one row or the n=5 subfamily has a new proof.

The six-support-row/Fourier complement at n=5 remains: its count region is
rho in [1,6/5], while the Fourier/affine parts cover the rest. The finite-sine
comparison for n=26,...,30 in Section 6.4 (pp.39–40) is a distinct surviving
region; replacing existing COUNT objects alone does not replace it. Section 7.2
acquisition (pp.56–72), including the simultaneous-resource theorem on p.59,
also remains an input, not a consequence of simpler comparisons. The new
large-index quartic route in Sections 7.4–7.10 is unaffected.

Fresh census evidence is
`runs/count_row_20261105/review_next_scope01/{PROCESS.json,checked/RESULT.json,checked/CENSUS.json}`.
It records exact source hashes and all row domains. This audit promises no net
page reduction: a manuscript deletion needs complete consumer replacement and
a new measured build after the essential general proof has been inserted.
