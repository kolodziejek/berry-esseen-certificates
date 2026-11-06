# Unified Complete 295-Contract `n = 5` All-Taylor Package (`research/n5-complete-20261106/`)

Additive continuation on top of commit `9dd7d0a` (`research/b3-band-20261106/`). All prior publication directories (`research/count-transfer-20261105/`, `research/argon-audit-20261105/`, `research/b0-band-20261105/`, `research/bn-band-20261106/`, `research/b2-band-20261106/`, and `research/b3-band-20261106/`) remain **100% byte-for-byte unchanged**.

This package unifies **all 295 original acquired `n = 5`, `K = 0` contracts** (`B0`: 24, `BN`: 32, `B2`: 104, `B3`: 135; `903` derived nearest-integer threshold regions, replacing all `75,178` legacy checked `COUNT` leaves across `1,770` six-root `COUNT` trees) into a **single portable 4-pair curvature-corrected all-Taylor package** (`n5-all-295/`, `gaussian_taylor_both_halves_4pair_v1`) with **3,589 terminal leaves** (**20.95x** reduction), **0 baseline fallback leaves**, **0 empty-domain leaves**, and **0 raw-moment dual prices** (`prices` omitted on all 3,589 leaves).

In addition to upgrading `BN` (`32` contracts) from the 9-pair model (`617` leaves in `bn-band-20261106`) to the shifted support-square 4-pair model (**535 leaves**, **24.79x** reduction vs. `13,265` legacy `COUNT` leaves) and unifying `B2_S3_01_045` (`9` leaves vs. `11` in `b2-band-20261106`) under the exact $\beta$-forced slab rescaling (`map_slab`), this package performs:
1. **Complete 4-Band & 12-Series Domain Join Verification (`accept_n5_all.py`):** Verifies all **283** intra-series contiguous probability joins (including **10** half-boundary joins at $p = 1/2$), all **102** cross-series $\beta$ boundary joins (`82` at $\beta = 1/5$ and `20` at $\beta = 3/10$), and all **244** cross-band and cross-slab $\rho$ boundary joins (`21` at $\rho = 11/10$, `48` at $\rho = 23/20$, `48` at $\rho = 467/400$, `62` at $\rho = 237/200$, and `65` at $\rho = 477/400$, plus the `8` right-edge panels whose $\rho_{\text{hi}}$ is capped below the nominal band ceiling by the outer support/Fourier envelope).
2. **Full-Corner Independent Polynomial, Cell-Geometry, and 4-Band Join Audit (`review/check_n5_complete_v3.py`):** Independently reconstructs every cell’s variance-allocation polygon and 4-pair shifted moment corners (**3,589** geometry checks) and verifies all 4 inverse Bernstein identities (`target`, `imp`, `ep`, `direct`) across **all 62,964 vertex-corner combinations** (**3,148,200** score Bernstein coefficients and **251,856** exact inverse identities), remediating the corner-0-only audit limitation of the frozen `b0-band-20261105` and `bn-band-20261106` checkers across all 295 contracts simultaneously.

---

## 1. Summary of Verified Results (`295 / 295` Contracts)

| Metric | Value |
| --- | --- |
| Original `n = 5`, `K = 0` contracts verified | **295 / 295** (100% of all `n = 5` contracts: `B0 = 24, BN = 32, B2 = 104, B3 = 135`) |
| Complete derived nearest-integer threshold regions (`k in {1, 2, 3, 4}`) | **903 / 903** (`B0: 67, BN: 99, B2: 320, B3: 417`; replaces `1,770` six-root `COUNT` trees) |
| Unified 4-pair all-Taylor leaves (`gaussian_taylor_both_halves_4pair_v1`) | **3,589** (vs. **75,178** legacy `COUNT` leaves — **20.95x** reduction) |
| Band leaf breakdown (`B0`, `BN`, `B2`, `B3`) | **`B0`**: 24 contracts, 67 roots, **222** leaves vs. 5,040 legacy (**22.70x**)<br>**`BN`**: 32 contracts, 99 roots, **535** leaves vs. 13,265 legacy (**24.79x**, down from 617 in `bn-band`)<br>**`B2`**: 104 contracts, 320 roots, **1,199** leaves vs. 25,970 legacy (**21.66x**, down from 1,201 in `b2-band`)<br>**`B3`**: 135 contracts, 417 roots, **1,633** leaves vs. 30,903 legacy (**18.92x**) |
| Baseline fallback / empty-domain / dual-priced leaves | **0** baseline leaves, **0** empty-domain leaves, **0** priced leaves (`prices` omitted on all 3,589 leaves) |
| Numerator sign partition across the 3,589 leaves | **2,390** nonpositive-numerator ($a_{\max} \le 0, M = 0$), **549** sign-crossing ($a_{\min} < 0 < a_{\max}, M > 0$), **650** purely positive-numerator ($a_{\min} \ge 0, M > 0$) |
| Dyadic internal subdivision nodes (`noise`, `alpha`) | **679** `noise` split nodes, **696** `alpha` split nodes (`6,275` total tree nodes) |
| Univariate global Sturm ray checks on compactified $[0, 1]$ | **43,068** ($3,589 \times 12$) |
| Curvature-corrected PSD Bernstein coefficients | **111,259** ($3,589 \times 31$: two degree-7 diagonal tests of 8 coefficients each + one degree-14 determinant test of 15 coefficients) |
| Full-corner independent geometry & polynomial audit (`review03`) | **3,589** independent cell-geometry checks, **62,964** vertex-corner combinations ($4V$ per leaf), **3,148,200** score Bernstein coefficients, **251,856** exact inverse identities |
| Negative and corruption controls (`controls01`) | **50** (including isolated positive-curvature PSD failure after passing 12 Sturm rays, legacy 9-pair method rejection, and probability/$\beta$/$\rho$ cross-band join corruption controls) |

---

## 2. Complete 4-Band & 12-Series Domain Join Census

| Series Key | Band | Series | Contracts | Panel Range | $p$ Union | $\rho$ Interval (Nominal) | $\beta$ Interval | Prob. Joins | Roots | All-Taylor Leaves | Legacy `COUNT` Leaves | Reduction |
| --- | --- | --- | ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `B0_B0` | `B0` | `B0` | 24 | `037..060` | `[37/100, 61/100]` | `[1, 11/10]` (3 right-edge capped) | `[-b, b]` | 23 | 67 | 222 | 5,040 | 22.70x |
| `BN_BN` | `BN` | `BN` | 32 | `034..065` | `[17/50, 33/50]` | `[11/10, 23/20]` | `[-b, b]` | 31 | 99 | 535 | 13,265 | 24.79x |
| `B2_S0` | `B2` | `S0` | 32 | `033..064` | `[33/100, 13/20]` | `[23/20, 467/400]` (2 right-edge capped) | `[beta_lo, 1/5]` or `[beta_lo, beta_hi]` | 31 | 98 | 374 | 7,604 | 20.33x |
| `B2_S1` | `B2` | `S1` | 18 | `033..050` | `[33/100, 51/100]` | `[23/20, 467/400]` | `[1/5, beta_hi]` | 17 | 55 | 100 | 2,477 | 24.77x |
| `B2_S2` | `B2` | `S2` | 34 | `032..065` | `[8/25, 33/50]` | `[467/400, 237/200]` (1 right-edge capped) | `[beta_lo, 1/5]` or `[beta_lo, beta_hi]` | 33 | 104 | 563 | 9,751 | 17.32x |
| `B2_S3` | `B2` | `S3` | 20 | `032..051` | `[8/25, 13/25]` | `[467/400, 237/200]` | `[1/5, beta_hi]` | 19 | 63 | 162 | 6,138 | 37.89x |
| `B3_S0` | `B3` | `S0` | 35 | `031..065` | `[31/100, 33/50]` | `[237/200, 477/400]` (1 right-edge capped) | `[beta_lo, 1/5]` or `[beta_lo, beta_hi]` | 34 | 107 | 557 | 9,808 | 17.61x |
| `B3_S2` | `B3` | `S2` | 36 | `031..066` | `[31/100, 67/100]` | `[477/400, 6/5]` (1 right-edge capped) | `[beta_lo, 1/5]` or `[beta_lo, beta_hi]` | 35 | 112 | 684 | 10,694 | 15.63x |
| `B3_T0` | `B3` | `T0` | 22 | `031..052` | `[31/100, 53/100]` | `[237/200, 477/400]` | `[1/5, 3/10]` or `[1/5, beta_hi]` | 21 | 69 | 142 | 3,978 | 28.01x |
| `B3_T1` | `B3` | `T1` | 9 | `032..040` | `[8/25, 41/100]` | `[237/200, 477/400]` | `[3/10, beta_hi]` | 8 | 27 | 35 | 668 | 19.09x |
| `B3_T2` | `B3` | `T2` | 22 | `031..052` | `[31/100, 53/100]` | `[477/400, 6/5]` | `[1/5, 3/10]` or `[1/5, beta_hi]` | 21 | 69 | 167 | 4,823 | 28.88x |
| `B3_T3lower` | `B3` | `T3lower` | 11 | `031..041` | `[31/100, 21/50]` | `[477/400, 6/5]` | `[3/10, beta_hi]` | 10 | 33 | 48 | 932 | 19.42x |
| **Total (12 series)** | **4 bands** | **12 series** | **295** | **`031..066`** | **`[31/100, 67/100]`** | **`[1, 6/5]` (244 $\rho$ joins)** | **102 $\beta$ joins** | **283** | **903** | **3,589** | **75,178** | **20.95x** |

### Boundary Join Breakdown (`verify_n5_all_join`)
- **283 Contiguous Probability Joins:** Exact rational equality $p_u(i) = p_l(i+1)$ across consecutive panel indices within all 12 series (`23 + 31 + 31 + 17 + 33 + 19 + 34 + 35 + 21 + 8 + 21 + 10`), including **10 half-boundary joins** at $p = 1/2$ (`049 -> 050` in `B0_B0, BN_BN, B2_S0, B2_S1, B2_S2, B2_S3, B3_S0, B3_S2, B3_T0, B3_T2`).
- **102 Cross-Series $\beta$ Boundary Joins:**
  - `B2_S0 <-> B2_S1` at $\beta = 1/5$ on `033..050`: **18** joins
  - `B2_S2 <-> B2_S3` at $\beta = 1/5$ on `032..051`: **20** joins
  - `B3_S0 <-> B3_T0` at $\beta = 1/5$ on `031..052`: **22** joins
  - `B3_T0 <-> B3_T1` at $\beta = 3/10$ on `032..040`: **9** joins
  - `B3_S2 <-> B3_T2` at $\beta = 1/5$ on `031..052`: **22** joins
  - `B3_T2 <-> B3_T3lower` at $\beta = 3/10$ on `031..041`: **11** joins
- **244 Cross-Band & Cross-Slab $\rho$ Boundary Joins (+ 8 Support/Fourier-Capped Right-Edge Panels):**
  - `B0_B0 <-> BN_BN` at $\rho = 11/10$ on `037..057`: **21** joins (`B0_058..060` have $\rho_{\text{hi}} < 11/10$ capped by the $B_0$ support/Fourier envelope)
  - `BN_BN <-> B2_S0` at $\rho = 23/20$ on `034..064`: **31** joins
  - `BN_BN <-> B2_S1` at $\rho = 23/20$ on `034..050`: **17** joins
  - `B2_S0 <-> B2_S2` at $\rho = 467/400$ on `033..062`: **30** joins (`B2_S0_01_063..064` have $\rho_{\text{hi}} < 467/400$ capped by the $B_2$ support/Fourier envelope)
  - `B2_S1 <-> B2_S3` at $\rho = 467/400$ on `033..050`: **18** joins
  - `B2_S2 <-> B3_S0` at $\rho = 237/200$ on `032..064`: **33** joins (`B2_S2_01_065` has $\rho_{\text{hi}} < 237/200$)
  - `B2_S3 <-> B3_T0` at $\rho = 237/200$ on `032..051`: **20** joins
  - `B2_S3 <-> B3_T1` at $\rho = 237/200$ on `032..040`: **9** joins
  - `B3_S0 <-> B3_S2` at $\rho = 477/400$ on `031..064`: **34** joins (`B3_S0_01_065` has $\rho_{\text{hi}} < 477/400$ and `B3_S2_01_066` has $\rho_{\text{hi}} < 6/5$)
  - `B3_T0 <-> B3_T2` at $\rho = 477/400$ on `031..052`: **22** joins
  - `B3_T1 <-> B3_T3lower` at $\rho = 477/400$ on `032..040`: **9** joins

---

## 3. Manuscript & `COMPLETION_LEDGER.json` Replacement Map for Logical Node `n5`

In `manuscript/extended-v17/reproduction/COMPLETION_LEDGER.json` (`logical_nodes[id="n5"]`, `evidence_sets["n5"]`) and Proposition `ext:five-assembly-criterion` (`manuscript/extended-v17/sections/06i-five-summand-assembly.tex`, lines 82–90):

1. **Replaced Certificate Component on `n = 5`:**
   - **Legacy Proof Object (`runs/extension_20261104/coordinator/n5-v3-complete02`):** Across the 12 signed-moment regions of $1 \le \rho \le 6/5$ (`1,200` probability-panel instances, of which `905` are excluded by physical resource inequalities), the remaining **295 probability-panel contracts** were covered by **295 six-root `COUNT` forests** (`1,770` roots, **75,178 terminal leaves**) against the fixed count target $4097/10000 < C_E$, using 9-corner conditional-moment tables and raw/signed moment dual prices.
   - **Unified All-Taylor Replacement (`research/n5-complete-20261106/n5-all-295/`):** Covers the exact same **295 acquired `contract.json` domains** (`SHA-256` pinned in `contracts/CENSUS_295.json`) using **903 derived nearest-integer threshold roots** ($k \in \{1, 2, 3, 4\}$) and **3,589 curvature-corrected 4-pair all-Taylor leaves** (`20.95x` fewer cells) directly against the dynamic Berry–Esseen target $\Phi(u_{\min}(x)) + \frac{C_E}{\sqrt{5}} \rho(w)$, with **0 baseline fallback leaves** and **0 raw-moment dual prices**.
2. **Retained Upstream & Complementary `n = 5` Dependencies (Not Replaced Here):**
   - Predecessor bound $C_4 \le C_E$ (`logical_node` `n4`) and closed-event attainment/contact (`logical_node` `attainment_contact`).
   - Actual-$n=5$ support radius bounds (`Appendix ext:n5-support`, jobs `support` and `n5-high-support01`).
   - Auxiliary and supported Fourier own-score and compensated `HIGH` caps (`jobs high` and `owncaps`).
   - The 12 unseeded finite initializers `initial.{B0, BN, B2.S0..S3, B3.S0..T3lower}` and 15 physical resource jobs `resource.{B0, BN, B2, B3}.*` (`Section ext:physical-count-domain`) that exclude the `905` infeasible panel instances and export the `295` surviving `contract.json` files.
   - The whole-line elementary corner estimate on $[477/400, 6/5] \times [17/50, b_3]$ (`Appendix ext:gapfree5`, job `gapfree5-01`).
   - The 6 supported Fourier bands on $\rho \in [6/5, 7361/4000]$ (`job complement`) and the affine tail bound on $\rho \ge 7361/4000$.
3. **Why the 86-Page Manuscript Remains Unchanged at This Stage:**
   - While `n = 5` (`logical_node` `n5`) no longer requires the legacy `COUNT` forest certificates or raw-moment dual pricing, the shared `COUNT` comparison framework in `manuscript/extended-v17/sections/06b-finite-counts.tex` and `06c-count-domain.tex` is still used by `logical_node` `n6_14` ($6 \le n \le 14$) and `logical_node` `n15_38` ($15 \le n \le 38$). The manuscript therefore remains at 86 pages.

---

## 4. Reproduction Commands

```bash
# Verify top-level publication inventory (2,145 files)
python3 -I -B -S research/n5-complete-20261106/verify_inventory.py

# Verify portable package manifest (2,133 files, 295 rows)
python3 -I -B -S research/n5-complete-20261106/n5-all-295/portable.py verify

# Replay a single root smoke check
python3 -I -B -S research/n5-complete-20261106/n5-all-295/portable.py smoke --out /tmp/n5_all_smoke

# Run all 50 negative and corruption controls
python3 -I -B -S research/n5-complete-20261106/n5-all-295/portable.py controls --out /tmp/n5_all_controls

# Replay all 295 contracts (903 roots, 3,589 leaves) and 4-band domain join in stdlib Python
python3 -I -B -S research/n5-complete-20261106/n5-all-295/portable.py replay --out /tmp/n5_all_replay

# Run full-corner independent polynomial, cell-geometry, and 4-band domain-join audit
python3 -I -B -S research/n5-complete-20261106/review/check_n5_complete_v3.py \
  research/n5-complete-20261106/n5-all-295 /tmp/n5_all_audit
```
