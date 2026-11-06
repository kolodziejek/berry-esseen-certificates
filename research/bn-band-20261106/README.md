# Complete 32-Contract `n = 5` `BN` Band (`research/bn-band-20261106/`)

Additive continuation on top of commit `ae5d80d` (`research/b0-band-20261105/`). All prior publication directories (`research/count-transfer-20261105/`, `research/argon-audit-20261105/`, and `research/b0-band-20261105/`) remain **100% byte-for-byte unchanged**.

This package completes the **second full `n = 5` band replacement**: all **32 contracts of the `BN` band** (`BN_034..BN_065`, 99 nearest-integer roots, 13,265 legacy `COUNT` leaves) across `gamma16_01`, `B0_BN_rest01`, and `pilots01`, covering the gap-free contiguous probability interval $p \in [17/50, 33/50]$ under the uniform moment slab $\rho \in [11/10, 23/20]$ at the original Berry–Esseen constant $C_E = \frac{3 + \sqrt{10}}{6 \sqrt{2 \pi}}$. Together with `research/b0-band-20261105/` (`B0_037..B0_060`, 24 contracts), both unique-panel-index `n = 5` bands (`B0` and `BN`, **56 contracts**, **166 roots**, **839 all-Taylor leaves** vs. **18,305 legacy `COUNT` leaves**) are now 100% replaced by all-Taylor curvature-corrected certificates.

## 1. Summary of Verified Results

| Metric | Value |
| --- | --- |
| Original `n = 5`, `K = 0` `BN` contracts verified | **32 / 32** (`BN_034..BN_065`, indices `34..65`, 100% of `BN` in the 295-contract census `B0=24, BN=32, B2=104, B3=135`) |
| Contiguous rational probability interval joins | **31** (`pu(i) == pl(i + 1)` across $p \in [17/50, 33/50]$) |
| Cross-slab-family / half-boundary joins verified | **5** ($p = 41/100$: `gamma16_01` $\to$ `B0_BN_rest01`; $p = 9/20$: `B0_BN_rest01` $\to$ `pilots01`; $p = 23/50$: `pilots01` $\to$ `B0_BN_rest01`; $p = 1/2$: `B0_BN_rest01` $\to$ `pilots01`; $p = 51/100$: `pilots01` $\to$ `B0_BN_rest01`) |
| Complete derived nearest-integer roots verified | **99** across `BN_034..BN_065` |
| All-Taylor curvature-corrected leaves (`gaussian_taylor_both_halves_v1`) | **617** (vs. **13,265** legacy `COUNT` leaves — **21.50x** reduction) |
| Baseline fallback leaves / empty-domain leaves / dual-priced leaves | **0** baseline leaves, **0** empty-domain leaves, **0** priced leaves (`prices` omitted on all 617 leaves) |
| Numerator sign partition across the 617 leaves | **424** nonpositive-numerator ($a_{\max} \le 0, M = 0$), **97** sign-crossing ($a_{\min} < 0 < a_{\max}, M > 0$), **96** purely positive-numerator ($a_{\min} \ge 0, M > 0$) |
| Global Sturm ray checks on $[0, 1]^2$ | **7,404** ($617 \times 12$) |
| Univariate curvature-corrected PSD Bernstein coefficients | **19,127** ($617 \times 31$) |
| Bivariate degree-$(9, 4)$ score tensor Bernstein coefficients | **1,239,300** |
| Negative and corruption controls (`controls01`) | **48** (including isolated positive-curvature PSD failure using globally valid quartics $2 + 10^{-12} x^4$ that pass all 12 Sturm rays, plus `BN` band-join corruption controls) |

## 2. Per-Contract Breakdown (`BN_034..BN_065`)

| Row ID | Slab family | $p$ interval | $\rho$ interval | Roots $k$ | All-Taylor leaves | Legacy `COUNT` leaves |
| --- | --- | --- | --- | --- | ---: | ---: |
| `BN_034` | `gamma16_01` | `[17/50, 7/20]` | `[11/10, 23/20]` | `1, 2, 3` | 9 | 389 |
| `BN_035` | `gamma16_01` | `[7/20, 9/25]` | `[11/10, 23/20]` | `1, 2, 3` | 10 | 583 |
| `BN_036` | `gamma16_01` | `[9/25, 37/100]` | `[11/10, 23/20]` | `1, 2, 3` | 10 | 693 |
| `BN_037` | `gamma16_01` | `[37/100, 19/50]` | `[11/10, 23/20]` | `1, 2, 3` | 12 | 784 |
| `BN_038` | `gamma16_01` | `[19/50, 39/100]` | `[11/10, 23/20]` | `1, 2, 3` | 13 | 822 |
| `BN_039` | `gamma16_01` | `[39/100, 2/5]` | `[11/10, 23/20]` | `1, 2, 3` | 16 | 809 |
| `BN_040` | `gamma16_01` | `[2/5, 41/100]` | `[11/10, 23/20]` | `1, 2, 3` | 19 | 784 |
| `BN_041` | `B0_BN_rest01` | `[41/100, 21/50]` | `[11/10, 23/20]` | `1, 2, 3` | 21 | 648 |
| `BN_042` | `B0_BN_rest01` | `[21/50, 43/100]` | `[11/10, 23/20]` | `1, 2, 3` | 28 | 665 |
| `BN_043` | `B0_BN_rest01` | `[43/100, 11/25]` | `[11/10, 23/20]` | `1, 2, 3` | 28 | 635 |
| `BN_044` | `B0_BN_rest01` | `[11/25, 9/20]` | `[11/10, 23/20]` | `1, 2, 3` | 32 | 647 |
| `BN_045` | `pilots01` | `[9/20, 23/50]` | `[11/10, 23/20]` | `1, 2, 3` | 41 | 660 |
| `BN_046` | `B0_BN_rest01` | `[23/50, 47/100]` | `[11/10, 23/20]` | `1, 2, 3` | 46 | 681 |
| `BN_047` | `B0_BN_rest01` | `[47/100, 12/25]` | `[11/10, 23/20]` | `1, 2, 3` | 61 | 681 |
| `BN_048` | `B0_BN_rest01` | `[12/25, 49/100]` | `[11/10, 23/20]` | `1, 2, 3, 4` | 45 | 614 |
| `BN_049` | `B0_BN_rest01` | `[49/100, 1/2]` | `[11/10, 23/20]` | `1, 2, 3, 4` | 30 | 527 |
| `BN_050` | `pilots01` | `[1/2, 51/100]` | `[11/10, 23/20]` | `1, 2, 3, 4` | 30 | 500 |
| `BN_051` | `B0_BN_rest01` | `[51/100, 13/25]` | `[11/10, 23/20]` | `2, 3, 4` | 27 | 397 |
| `BN_052` | `B0_BN_rest01` | `[13/25, 53/100]` | `[11/10, 23/20]` | `2, 3, 4` | 26 | 408 |
| `BN_053` | `B0_BN_rest01` | `[53/100, 27/50]` | `[11/10, 23/20]` | `2, 3, 4` | 23 | 331 |
| `BN_054` | `B0_BN_rest01` | `[27/50, 11/20]` | `[11/10, 23/20]` | `2, 3, 4` | 20 | 243 |
| `BN_055` | `B0_BN_rest01` | `[11/20, 14/25]` | `[11/10, 23/20]` | `2, 3, 4` | 18 | 224 |
| `BN_056` | `B0_BN_rest01` | `[14/25, 57/100]` | `[11/10, 23/20]` | `2, 3, 4` | 15 | 194 |
| `BN_057` | `B0_BN_rest01` | `[57/100, 29/50]` | `[11/10, 23/20]` | `2, 3, 4` | 7 | 94 |
| `BN_058` | `B0_BN_rest01` | `[29/50, 59/100]` | `[11/10, 23/20]` | `2, 3, 4` | 6 | 79 |
| `BN_059` | `B0_BN_rest01` | `[59/100, 3/5]` | `[11/10, 23/20]` | `2, 3, 4` | 6 | 68 |
| `BN_060` | `B0_BN_rest01` | `[3/5, 61/100]` | `[11/10, 23/20]` | `2, 3, 4` | 3 | 18 |
| `BN_061` | `B0_BN_rest01` | `[61/100, 31/50]` | `[11/10, 23/20]` | `2, 3, 4` | 3 | 26 |
| `BN_062` | `B0_BN_rest01` | `[31/50, 63/100]` | `[11/10, 23/20]` | `2, 3, 4` | 3 | 26 |
| `BN_063` | `B0_BN_rest01` | `[63/100, 16/25]` | `[11/10, 23/20]` | `2, 3, 4` | 3 | 15 |
| `BN_064` | `B0_BN_rest01` | `[16/25, 13/20]` | `[11/10, 23/20]` | `2, 3, 4` | 3 | 12 |
| `BN_065` | `B0_BN_rest01` | `[13/20, 33/50]` | `[11/10, 23/20]` | `2, 3, 4` | 3 | 8 |
| **Total (32 contracts)** | | **`[17/50, 33/50]`** | **`[11/10, 23/20]`** | **99 roots** | **617** | **13,265** |

Combined with the 24 `B0` contracts in `../b0-band-20261105/n5-b0-band/` (`B0_037..B0_060`, 67 roots, 222 leaves vs. 5,040 old leaves) and the 3 additional `B2`/`B3` contracts in `../count-transfer-20261105/n5-all-taylor/` (`B2_S3_34`, `B3_S0_59`, `B3_S2_59`, 9 roots, 17 leaves vs. 853 old leaves), **59 distinct original `n = 5` contracts** (**175 roots**, **856 all-Taylor leaves** vs. **19,158 legacy `COUNT` leaves** — a **22.38x** cumulative leaf reduction) now have complete all-Taylor curvature-corrected replacements; 236 of the 295 `n = 5` contracts remain (103 in `B2` and 133 in `B3`).

## 3. Reproduction Commands

```bash
# Verify top-level publication inventory
python3 -I -B -S research/bn-band-20261106/verify_inventory.py

# Verify portable package manifest (262 files, 32 rows)
python3 -I -B -S research/bn-band-20261106/n5-bn-band/portable.py verify

# Replay all 32 BN contracts in stdlib Python
python3 -I -B -S research/bn-band-20261106/n5-bn-band/portable.py replay --out /tmp/bn_band_replay

# Run 48 negative and corruption controls
python3 -I -B -S research/bn-band-20261106/n5-bn-band/portable.py controls --out /tmp/bn_band_controls

# Run independent polynomial and band-join audit
python3 -I -B -S research/bn-band-20261106/review/check_bn_band_v2.py \
  research/bn-band-20261106/n5-bn-band /tmp/bn_band_audit
```
