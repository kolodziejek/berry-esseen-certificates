# Complete 104-Contract `n = 5` `B2` Band (`n5-b2-band`)

Self-contained portable verification package for the **complete 104-contract `n = 5`, `K = 0` `B2` band replacement** (`research/b2-band-20261106/n5-b2-band/`): all **104 original `n = 5`, `K = 0` `B2` contracts** (`320` nearest-integer threshold regions, replacing `25,970` legacy checked `COUNT` leaves) across the four `B2` sub-series `S0`, `S1`, `S2`, and `S3`, retaining all original contract hypotheses (centered sign-conditioned marginals, inward/outward support bounds, acquired mean/noise bounds, $\beta$/$\gamma$ signed-moment slabs, and threshold intervals).

## 1. Summary of Verified Results

- **Contracts verified:** **104 / 104** (100% of the `B2` band in `CENSUS_295.json`), partitioned across four sub-series:
  - **`S0` (`B2_S0_01_033..064`):** **32** contracts, **98** roots, $p \in [33/100, 13/20]$ (**31** contiguous probability joins), $\rho_{\text{lo}} = 23/20$, $\rho_{\text{hi}} \le 467/400$, $\beta_{\text{hi}} \le 1/5$; **374** all-Taylor leaves replacing **7,604** legacy `COUNT` leaves (**20.33x** reduction).
  - **`S1` (`B2_S1_01_033..050`):** **18** contracts, **55** roots, $p \in [33/100, 51/100]$ (**17** contiguous probability joins), $\rho \in [23/20, 467/400]$, $\beta_{\text{lo}} = 1/5$; **100** all-Taylor leaves replacing **2,477** legacy `COUNT` leaves (**24.77x** reduction).
  - **`S2` (`B2_S2_01_032..065`):** **34** contracts, **104** roots, $p \in [8/25, 33/50]$ (**33** contiguous probability joins), $\rho_{\text{lo}} = 467/400$, $\rho_{\text{hi}} \le 237/200$, $\beta_{\text{hi}} \le 1/5$; **563** all-Taylor leaves replacing **9,751** legacy `COUNT` leaves (**17.32x** reduction).
  - **`S3` (`B2_S3_endpoint02_032..034` + `B2_S3_01_035..051`):** **20** contracts, **63** roots, $p \in [8/25, 13/25]$ (**19** contiguous probability joins, including the cross-family join at $p = 7/20$ between `B2_S3_endpoint02_034` and `B2_S3_01_035`), $\rho \in [467/400, 237/200]$, $\beta_{\text{lo}} = 1/5$; **164** all-Taylor leaves replacing **6,138** legacy `COUNT` leaves (**37.43x** reduction).
- **Contiguous probability & $\beta = 1/5$ joins verified:** **100** contiguous probability joins (`31 + 17 + 33 + 19`) plus **38** exact $\beta = 1/5$ boundary joins (**18** between `S0` and `S1` on panels `33..50`, and **20** between `S2` and `S3` on panels `32..51`).
- **Nearest-integer roots verified:** **320** across all 104 `B2` contracts.
- **Total all-Taylor leaves:** **1,201** (vs. **25,970** legacy `COUNT` leaves — a **21.62x** leaf reduction across the entire `B2` band), with **0** baseline fallback leaves, **0** empty-domain leaves, and **0** raw-moment dual prices required.
- **Exact certificate checks replayed (`evidence/replay01/accepted/RESULT.json`):**
  - **14,412** univariate global Sturm ray checks on the compactified ray $[0, 1]$ (`12` per cell)
  - **37,231** curvature-corrected PSD Bernstein coefficients (`31` per cell: two degree-7 diagonal tests with 8 coefficients each and one degree-14 determinant test with 15 coefficients)
  - **1,048,200** bivariate degree-$(9, 4)$ score tensor Bernstein coefficients (`50` per vertex-corner across **20,964** vertex-corner combinations using the 4-endpoint-pair moment reduction)
- **Negative and corruption controls (`evidence/controls01/accepted/RESULT.json`):** **48** negative controls rejected (including broken `B2` probability and $\beta = 1/5$ joins, missing/swapped panels, legacy 9-pair method tags, ambiguous `(band, index)` selectors, and proof-tree mutations).

## 2. Mathematical Mechanisms (`gaussian_taylor_both_halves_4pair_v1`)

1. **Shifted Support-Square Affine Fourth-Moment Envelopes:**
   On a cell with variance-allocation polygon $V \subset \{x \ge 0, y \ge 0\}$, let $x_{\min} = \min_{(x,y)\in V} x$, $y_{\min} = \min_{(x,y)\in V} y$, and conditional variance floors $s_{0,\min} = \frac{x_{\min}}{1 - p_l}$, $s_{1,\min} = \frac{y_{\min}}{p_u}$. With inward support ceilings $(r_0, r_1)$ and Cauchy-Schwarz shifts
   $$d_{0,\text{out}} = \min\Big(A_0, \frac{s_{0,\min}}{A_0}\Big), \quad d_{0,\text{in}} = \min\Big(r_0, \frac{s_{0,\min}}{r_0}\Big), \quad d_{1,\text{out}} = \min\Big(A_1, \frac{s_{1,\min}}{A_1}\Big), \quad d_{1,\text{in}} = \min\Big(r_1, \frac{s_{1,\min}}{r_1}\Big),$$
   the skewness intervals are $\gamma_0 \in [g_{0,\text{lo}}, g_{0,\text{hi}}] = [-A_0 + d_{0,\text{out}},\, \max(g_{0,\text{lo}}, r_0 - d_{0,\text{in}})]$ and $\gamma_1 \in [g_{1,\text{lo}}, g_{1,\text{hi}}] = [\min(g_{1,\text{hi}}, -r_1 + d_{1,\text{in}}),\, A_1 - d_{1,\text{out}}]$.
   Since $(r_0 - U_0)(U_0 + A_0)(U_0 + d_{0,\text{in}})^2 \ge 0$ on $[-A_0, r_0]$ with $r_0 d_{0,\text{in}} \le s_{0,\min} \le s_0$, and $(A_1 - U_1)(U_1 + r_1)(U_1 - d_{1,\text{in}})^2 \ge 0$ on $[-r_1, A_1]$ with $r_1 d_{1,\text{in}} \le s_{1,\min} \le s_1$, taking expectations and dividing by $s_0, s_1 > 0$ yields the globally valid affine fourth-moment upper envelopes:
   $$\kappa_0 \le K_0(\gamma_0) := (r_0 - A_0 - 2d_{0,\text{in}})\gamma_0 + A_0 r_0 - (A_0 - 2r_0)d_{0,\text{in}} - d_{0,\text{in}}^2,$$
   $$\kappa_1 \le K_1(\gamma_1) := (A_1 - r_1 + 2d_{1,\text{in}})\gamma_1 + A_1 r_1 - (A_1 - 2r_1)d_{1,\text{in}} - d_{1,\text{in}}^2.$$
   When $d_{0,\text{in}} = 0$ and $d_{1,\text{in}} = 0$ (e.g., on the base noise slab), $K_0(\gamma_0)$ and $K_1(\gamma_1)$ reduce identically to $(r_0 - A_0)\gamma_0 + A_0 r_0$ and $(A_1 - r_1)\gamma_1 + A_1 r_1$.

2. **Four-Endpoint-Pair Moment Reduction (`moment_pairs = 4`):**
   Because $K_0(\gamma_0)$ and $K_1(\gamma_1)$ are affine in $\gamma_0$ and $\gamma_1$, substituting them into the upper-bounded fourth-order Taylor loss makes the score polynomial affine separately in $\gamma_0 \in [g_{0,\text{lo}}, g_{0,\text{hi}}]$ and $\gamma_1 \in [g_{1,\text{lo}}, g_{1,\text{hi}}]$. Consequently, the minimum over the moment rectangle $[g_{0,\text{lo}}, g_{0,\text{hi}}] \times [g_{1,\text{lo}}, g_{1,\text{hi}}]$ is attained at one of the **4 endpoint pairs**:
   $$c_0 = \big((g_{0,\text{lo}}, K_0(g_{0,\text{lo}})),\ (g_{0,\text{hi}}, K_0(g_{0,\text{hi}}))\big), \qquad c_1 = \big((g_{1,\text{hi}}, K_1(g_{1,\text{hi}})),\ (g_{1,\text{lo}}, K_1(g_{1,\text{lo}}))\big).$$

## 3. Portable Commands

```bash
# Verify byte inventory
python3 -I -B -S research/b2-band-20261106/n5-b2-band/portable.py verify

# Run single-root smoke test (B2_S2_01_050 k=3)
python3 -I -B -S research/b2-band-20261106/n5-b2-band/portable.py smoke --out /tmp/b2_smoke

# Run 48 negative and corruption controls
python3 -I -B -S research/b2-band-20261106/n5-b2-band/portable.py controls --out /tmp/b2_controls

# Replay all 104 B2 contracts (320 roots, 1,201 all-Taylor leaves)
python3 -I -B -S research/b2-band-20261106/n5-b2-band/portable.py replay --out /tmp/b2_replay
```
