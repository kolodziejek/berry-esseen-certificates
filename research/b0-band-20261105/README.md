# Complete 24-Contract `n = 5` `B0` Band (`research/b0-band-20261105/`)

Additive continuation on top of commit `8517231` (`research/argon-audit-20261105/`). Both `research/count-transfer-20261105/` (`FILES.json` SHA-256 `9c7cf55a7611c51c9a264c5c428e6a69010b60038833c06db60ed14516038b0c`) and `research/argon-audit-20261105/` remain **100% byte-for-byte unchanged**.

This package completes the **first full `n = 5` band replacement**: all **24 contracts of the `B0` band** (`B0_037..B0_060`, 67 nearest-integer roots, 5,040 legacy `COUNT` leaves) across `gamma16_01`, `pilots01`, and `B0_BN_rest01`, covering the gap-free contiguous probability interval $p \in [37/100, 61/100]$ under $\rho_{\text{lower}} = 1$ and $\rho_{\text{upper}} \le 11/10$ at the original Berry–Esseen constant $C_E = \frac{3 + \sqrt{10}}{6 \sqrt{2 \pi}}$.

## 1. Summary of Verified Results

| Metric | Value |
| --- | --- |
| Original `n = 5`, `K = 0` `B0` contracts verified | **24 / 24** (`B0_037..B0_060`, indices `37..60`, 100% of `B0` in the 295-contract census `B0=24, BN=32, B2=104, B3=135`) |
| Contiguous rational probability interval joins | **23** (`pu(i) == pl(i + 1)` across $p \in [37/100, 61/100]$) |
| Cross-slab-family / half-boundary joins verified | **3** ($p = 23/50$: `gamma16_01` $\to$ `B0_BN_rest01`; $p = 1/2$: `B0_BN_rest01` $\to$ `pilots01`; $p = 51/100$: `pilots01` $\to$ `B0_BN_rest01`) |
| Complete derived nearest-integer roots verified | **67** (`k in {1, 2, 3}` on `037..047`, `k in {2, 3}` on `048..052`, `k in {2, 3, 4}` on `053..060`) |
| All-Taylor curvature-corrected leaves (`gaussian_taylor_both_halves_v1`) | **222** (vs. **5,040** legacy `COUNT` leaves — **22.70x** reduction) |
| Baseline fallback leaves / dual-priced leaves | **0** baseline leaves, **0** priced leaves (`prices` omitted on all 222 leaves) |
| Numerator sign partition across the 222 leaves | **143** nonpositive-numerator ($a_{\max} \le 0, M = 0$), **37** sign-crossing ($a_{\min} < 0 < a_{\max}, M > 0$), **42** purely positive-numerator ($a_{\min} \ge 0, M > 0$) |
| Global Sturm ray checks on $[0, 1]^2$ | **2,664** ($222 \times 12$) |
| Univariate curvature-corrected PSD Bernstein coefficients | **6,882** ($222 \times 31$) |
| Bivariate degree-$(9, 4)$ score tensor Bernstein coefficients | **456,300** |
| Negative and corruption controls (`controls01`) | **48** (including isolated positive-curvature PSD failure using globally valid quartics $2 + 10^{-12} x^4$ that pass all 12 Sturm rays, plus `B0` band-join corruption controls) |

## 2. Per-Contract Breakdown (`B0_037..B0_060`)

| Row ID | Slab family | $p$ interval | $\rho$ interval | Roots $k$ | All-Taylor leaves | Legacy `COUNT` leaves |
| --- | --- | --- | --- | --- | ---: | ---: |
| `B0_037` | `gamma16_01` | `[37/100, 19/50]` | `[1, 11/10]` | `1, 2, 3` | 7 | 159 |
| `B0_038` | `gamma16_01` | `[19/50, 39/100]` | `[1, 11/10]` | `1, 2, 3` | 8 | 200 |
| `B0_039` | `gamma16_01` | `[39/100, 2/5]` | `[1, 11/10]` | `1, 2, 3` | 10 | 235 |
| `B0_040` | `gamma16_01` | `[2/5, 41/100]` | `[1, 11/10]` | `1, 2, 3` | 14 | 317 |
| `B0_041` | `gamma16_01` | `[41/100, 21/50]` | `[1, 11/10]` | `1, 2, 3` | 14 | 360 |
| `B0_042` | `gamma16_01` | `[21/50, 43/100]` | `[1, 11/10]` | `1, 2, 3` | 21 | 439 |
| `B0_043` | `gamma16_01` | `[43/100, 11/25]` | `[1, 11/10]` | `1, 2, 3` | 17 | 561 |
| `B0_044` | `gamma16_01` | `[11/25, 9/20]` | `[1, 11/10]` | `1, 2, 3` | 28 | 439 |
| `B0_045` | `gamma16_01` | `[9/20, 23/50]` | `[1, 11/10]` | `1, 2, 3` | 12 | 411 |
| `B0_046` | `B0_BN_rest01` | `[23/50, 47/100]` | `[1, 11/10]` | `1, 2, 3` | 12 | 343 |
| `B0_047` | `B0_BN_rest01` | `[47/100, 12/25]` | `[1, 11/10]` | `1, 2, 3` | 12 | 318 |
| `B0_048` | `B0_BN_rest01` | `[12/25, 49/100]` | `[1, 11/10]` | `2, 3` | 10 | 260 |
| `B0_049` | `B0_BN_rest01` | `[49/100, 1/2]` | `[1, 11/10]` | `2, 3` | 9 | 234 |
| `B0_050` | `pilots01` | `[1/2, 51/100]` | `[1, 11/10]` | `2, 3` | 8 | 212 |
| `B0_051` | `B0_BN_rest01` | `[51/100, 13/25]` | `[1, 11/10]` | `2, 3` | 5 | 142 |
| `B0_052` | `B0_BN_rest01` | `[13/25, 53/100]` | `[1, 11/10]` | `2, 3` | 5 | 101 |
| `B0_053` | `B0_BN_rest01` | `[53/100, 27/50]` | `[1, 11/10]` | `2, 3, 4` | 5 | 96 |
| `B0_054` | `B0_BN_rest01` | `[27/50, 11/20]` | `[1, 11/10]` | `2, 3, 4` | 5 | 49 |
| `B0_055` | `B0_BN_rest01` | `[11/20, 14/25]` | `[1, 11/10]` | `2, 3, 4` | 5 | 35 |
| `B0_056` | `B0_BN_rest01` | `[14/25, 57/100]` | `[1, 11/10]` | `2, 3, 4` | 3 | 35 |
| `B0_057` | `B0_BN_rest01` | `[57/100, 29/50]` | `[1, 11/10]` | `2, 3, 4` | 3 | 29 |
| `B0_058` | `B0_BN_rest01` | `[29/50, 59/100]` | `[1, 219361/200000]` | `2, 3, 4` | 3 | 29 |
| `B0_059` | `B0_BN_rest01` | `[59/100, 3/5]` | `[1, 273431/250000]` | `2, 3, 4` | 3 | 24 |
| `B0_060` | `B0_BN_rest01` | `[3/5, 61/100]` | `[1, 1086953/1000000]` | `2, 3, 4` | 3 | 12 |
| **Total (24 contracts)** | | **`[37/100, 61/100]`** | | **67 roots** | **222** | **5,040** |

Combined with the 5 additional non-`B0` contracts verified in `../count-transfer-20261105/n5-all-taylor/` (`BN39`, `B2_S3_34`, `BN38`, `B3_S0_59`, `B3_S2_59`), **29 distinct original `n = 5` contracts** (**81 roots**, **269 all-Taylor leaves** vs. **7,468 legacy `COUNT` leaves**) now have complete all-Taylor curvature-corrected replacements; 266 of the 295 `n = 5` contracts remain.

## 3. Reproduction Commands

```bash
# Verify top-level publication inventory
python3 -I -B -S research/b0-band-20261105/verify_inventory.py

# Verify portable package manifest (191 files, 24 rows)
python3 -I -B -S research/b0-band-20261105/n5-b0-band/portable.py verify

# Replay all 24 B0 contracts in stdlib Python
python3 -I -B -S research/b0-band-20261105/n5-b0-band/portable.py replay --out /tmp/b0_band_replay

# Run 48 negative and corruption controls
python3 -I -B -S research/b0-band-20261105/n5-b0-band/portable.py controls --out /tmp/b0_band_controls

# Run independent polynomial and band-join audit
python3 -I -B -S research/b0-band-20261105/review/check_b0_band_v2.py \
  research/b0-band-20261105/n5-b0-band /tmp/b0_band_audit
```
