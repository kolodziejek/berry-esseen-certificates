# Independent coverage and selector audit of the Argon continuation

The selected package has **seven complete original-row candidates, twenty threshold roots and sixty-three leaves**. The reported nineteen-root total is wrong; it is a counting error in the prose, not a missing selected root. I found no false-acceptance path in the reviewed source-selection or closed-tree rules at the selected scope. Several documentation claims need correction before publication, especially the displayed target constant.

External source, read-only throughout:
`/Users/bkolodziejek/Documents/BerryEsseen/research/count-transfer-20261105/n5-all-taylor/`.

| Item | Mathematical status | Execution status |
| --- | --- | --- |
| Original contract identity and selected closed cover | Independently audited against all original 295 contracts and the exact trees | Fresh own JSON/hash/rational-domain audit passed; no external code imported |
| Sixty-three leaf inequalities | Original acquired-row implications, subject to the separate analytic/model audit | External historical replay preserved; coordinator freshly replayed the copied reader successfully |
| All 295 rows or acquisition | Not established by this seven-row package | No new all-295 or acquisition campaign |

This review concerns coverage, identity, rejection behavior and executable scope. It does not represent another independent implementation of the complete numerical score checker.

## 1. Catalogue and original provenance

The external `contracts/CENSUS_295.json` is **byte-identical** to the previously independently constructed `runs/count_row_20261105/review_next_scope01/checked/CENSUS.json`. Both have SHA-256
`33193caa1a214ac84f938990c61468f269fdc1fb02cf7ed1781922bc2ccd4812`.

My fresh audit additionally opened every original workspace contract named in this catalogue. All 295 complete file hashes match; every embedded `row` equals the original contract's entire single row. There are 24 B0, 32 BN, 104 B2 and 135 B3 contracts. The 68 ambiguous `(band,index)` pairs are real.

The selector has more than seven metadata stubs: its catalogue embeds all fields consumed by `model_all_taylor.Row` for every original contract. Therefore path/hash/structured selection can instantiate those original row domains without a separately bundled full JSON file for each one. Seven aliases also bind seven bundled complete original contract files. This **does not** supply a new numerical certificate for the other 288 rows.

The catalogue's old `resource_verified` and `cutoff_proved` fields remain false for all 295 entries. The package correctly keeps original acquisition as a premise. These historical fields are not silently changed into new acquisition evidence.

`selector.py:26–30` first derives the complete integer-center range from the acquired threshold bounds, then rejects invalid/degenerate results. It does not clamp or discard centers. Independent derivation gives the catalogue root sets:

| Root set | Number of original contracts |
| --- | ---: |
| `(1,2,3)` | 177 |
| `(2,3)` | 5 |
| `(2,3,4)` | 88 |
| `(1,2,3,4)` | 24 |
| `(1,2)` | 1 |

No selected or catalogue threshold root zero is being omitted. The six mixture counts `j=0,...,5` are a separate family and remain present in every leaf. Half-integer threshold ties are included by both adjacent closed phase roots.

## 2. Exact selected coverage

| Row | Probability interval | Threshold roots | Leaves by root | Total |
| --- | --- | --- | --- | ---: |
| BN39 | `[39/100,2/5]` | 1,2,3 | 5,12,1 | 18 |
| B0_50 | `[1/2,51/100]` | 2,3 | 9,2 | 11 |
| B2_S3_34 | `[17/50,7/20]` | 1,2,3 | 4,2,1 | 7 |
| BN38 | `[19/50,39/100]` | 1,2,3 | 6,6,1 | 13 |
| B0_53 | `[53/100,27/50]` | 2,3,4 | 2,2,1 | 5 |
| B3_S0_59 | `[59/100,3/5]` | 2,3,4 | 1,2,1 | 4 |
| B3_S2_59 | `[59/100,3/5]` | 2,3,4 | 2,2,1 | 5 |
| **Total** | | **20 roots** | | **63** |

Every target object matches its declared hash, original path and contract hash. The object header fixes literal integer `n=5` and `k`, the complete original probability/noise intervals and either the exact clipped phase root or the permitted larger `[-1/2,1/2]`. No narrower phase root is accepted.

The sixty-three trees have 39 phase splits and four probability splits; no selected noise split occurs. The acceptor supports exact midpoint noise splits as well, with both children required. My independent traversal reconstructs the closed child domains rather than trusting stored leaf success records. All node shapes, canonical rational coefficients, positive quartic leading coefficients, common method tags and leaf counts agree. Exact leaf volumes sum to the full root domains; more importantly, each recursive split has both closed children, so endpoint coverage is explicit and does not rely on a measure-zero argument.

All leaf path lists also match the supplied historical per-root acceptance outputs. There is exactly one nonzero dual-price leaf: B2_S3_34, root 1, tree path `11`, with upper-raw-absolute-cube price `2124448403/10000000000`; the other three prices are zero. Its original acquired upper-rho premise remains part of that row's domain.

The aggregate arithmetic counts are internally consistent: 756 global ray checks, 1,953 univariate PSD coefficients and 121,500 score tensor coefficients. The old selected COUNT total is 2,736 leaves. Ratios of leaf counts are not automatically ratios of proof length or verification work.

## 3. Acceptance and ambiguity rules

I read `selector.py`, `accept_all_taylor.py`, `portable.py`, `controls_all_taylor.py`, `model_all_taylor.py`, `gaussian_scalar.py`, `algebra.py` and the capture supervisor before any package execution by this reviewer. The numerical native modules match the previously pinned source identities.

- Structured selector fields are conjunctive; unsupported fields and noncanonical intervals reject. The final unique-match requirement rejects ambiguity. Path/hash identities are canonical catalogue identities, not an inference from a filename. The four integer/type guards distinguish booleans from actual indices where proof input determines them.
- `admit_row_selection` requires exactly the complete ordered root census. The three source identity fields are checked against the resolved original row. The explicit phase enlargement cannot drop any part of the original phase domain.
- Each root object has an exact schema and is checked against its **external** domain. Leaves require the exact method tag. Unknown tags, old PASS/failure markers, omitted children and extra target fields reject. The shared endpoints of dyadic splits are included.
- All six countwise quartics, common moment choices, original target and original orientation remain in force. A right-half probability cell is not silently reflected into a different signed contract. Closed-event majorants retain threshold atoms.
- Multi-row replay permits a requested nonempty batch; it does not assert all 295 rows. Duplicate row identifiers reject, and each identifier must match the canonical resolved row. The fixed portable target here is precisely the seven-row batch listed above.
- Source and selected input hashes are checked after replay, and the capture records the actual return code. A printed PASS line alone is insufficient if the final stability check fails.

`portable.py verify` is a byte-inventory check, not a semantic proof replay. Its `catalogue_sha256` target field is not directly compared in that function, and its row test is only `len==7`; the actual exact reader independently pins the catalogue and validates row/root identities. This is a documentation/API distinction, not a found false-acceptance path in the selected replay. An optional hardening change would validate those semantic target fields already in `verify`, while retaining the full reader as the authority.

The 43 controls comprise twelve selector tests, twenty-six proof/tree mutations and five analytic/selection/parser guards. They include three representative ambiguous `(band,index)` queries, not an executable loop over all 68 ambiguous pairs. The selector's unique-match rule covers the general case; the empirical coverage claim should still be stated accurately.

## 4. Required documentation corrections

1. **Target constant — `n5-all-taylor/README.md:5`.** `C_E=9199/25000` is false for this reader. Replace it by
   `C_E=(3+sqrt(10))/(6*sqrt(2*pi))` and explain that acceptance uses its rigorously directed lower enclosure `normal.CE_LO`. The native source still uses the original constant; the certificates do not prove the stronger displayed rational target.
2. **Root total — `README.md:38,54`, `COMPLETION.json:355`, and the parent `count-transfer-20261105/README.md:62`.** Replace nineteen by **twenty**. Keep the true historical files unchanged; put corrections in an additive revised delivery or erratum.
3. **Catalogue bands — `README.md:23`.** Replace `(29,30,92,144)` by **B0 24, BN 32, B2 104, B3 135**.
4. **Proof schema — `README.md:17,20`.** The method is `gaussian_taylor_both_halves_v1`, not `taylor`; the optional field is `prices`, not `raw_moment_prices`. The four fixed nonnegative prices multiply necessary raw-moment slacks. The reader does not assert those slacks at every artificial corner; it uses them after their actual-law justification.
5. **Threshold derivation — `README.md:25`.** There are no `contract["raw"]` / `contract["derived"]["roots"]` interfaces here. Describe derivation from `p`, `acquired_scale_upper`, `Hminus`, `Hplus`, and comparison to the catalogue's `nearest_roots` list.
6. **Control scope — `README.md:53`.** Say that 43 controls include representative ambiguous queries and that the catalogue contains 68 ambiguous pairs. Do not say all 68 were exercised by this control script.

None of these corrections requires weakening the code's target or replacing a proof object. The target-constant error is the most consequential presentation issue; it should be corrected before readers rely on the stated theorem.

## 5. Evidence and limits

New work directory was created using `python tools/prepare_worktree.py --destination work/argon_audit_20261105/coverage`. The inherited reference copies created by that helper were not executed or edited.

Fresh own source: `work/argon_audit_20261105/coverage/audit_data.py`, SHA-256 `adddffb6a1157f857d1dbae3eb1dbc0f47a2c1f893db92fa20e3a701343ff431`.

Fresh own run: `runs/argon_audit_20261105/coverage_data01/`, actual return code 0 in 0.13986706733703613 seconds, empty stderr. Result SHA-256:
`aaaf5c7f9cadff81645fd105d1499a6aeb660161d5e4a3c25ad3488bb05ad4a8`.
`checked/LEAF_DOMAINS.json` gives the independently reconstructed sixty-three closed domains. All 88 external package files and all 295 original contracts were unchanged before/after the audit. This code imports **no external package module**.

The supplied historical replay reports return code 0 in 28.73209462495288 seconds; its stream hashes and source/object identities were checked. Separately, the coordinator's copied replay at `runs/argon_audit_20261105/replay01/` now reports actual return code 0 in 23.741375041019637 seconds with unchanged inputs and empty stderr. I did not repeat that numerical campaign.

The seven-row source/coverage rules are ready to use with the independently reviewed analytic reduction and fresh numerical replay. This review does not establish original acquisition, all 295 n5 rows, a complete manuscript replacement, or any claimed page saving.
