# Portable $n = 5$ `B3`-Band Curvature-Corrected All-Taylor Certificate Package

This directory is a self-contained portable certificate package for the complete **135-contract $n = 5, K = 0$ `B3` band** across all six original series (`S0`: 35, `S2`: 36, `T0`: 22, `T1`: 9, `T2`: 22, `T3lower`: 11), closing all **417** nearest-integer threshold roots with **1,633** curvature-corrected all-Taylor leaves (`gaussian_taylor_both_halves_4pair_v1`) in place of **30,903** legacy `COUNT` leaves (**18.92x** reduction).

## 1. Summary of Verified Scope

- **Contracts verified:** **135 / 135** original `B3` contracts across six series:
  - `S0` (`B3_S0_01_031..B3_S0_01_065`, 35 contracts, 107 roots): $p \in [31/100, 33/50]$, $\rho \in [237/200, 477/400]$, $-1 < \beta_{\text{lo}} < \beta_{\text{hi}} < 1$; **557** all-Taylor leaves replacing **9,808** legacy `COUNT` leaves (**17.61x** reduction).
  - `S2` (`B3_S2_01_031..B3_S2_01_066`, 36 contracts, 112 roots): $p \in [31/100, 67/100]$, $\rho \in [477/400, 6/5]$, $-1 < \beta_{\text{lo}} < \beta_{\text{hi}} < 1$; **684** all-Taylor leaves replacing **10,694** legacy `COUNT` leaves (**15.63x** reduction).
  - `T0` (`B3_T0_01_031..B3_T0_01_052`, 22 contracts, 69 roots): $p \in [31/100, 53/100]$, $\rho \in [237/200, 477/400]$, $\beta_{\text{lo}} = 1/5$; **142** all-Taylor leaves replacing **3,978** legacy `COUNT` leaves (**28.01x** reduction).
  - `T1` (`B3_T1_01_032..B3_T1_01_040`, 9 contracts, 27 roots): $p \in [8/25, 41/100]$, $\rho \in [237/200, 477/400]$, $\beta_{\text{lo}}(T_1) = \beta_{\text{hi}}(T_0)$; **35** all-Taylor leaves replacing **668** legacy `COUNT` leaves (**19.09x** reduction).
  - `T2` (`B3_T2_01_031..B3_T2_01_052`, 22 contracts, 69 roots): $p \in [31/100, 53/100]$, $\rho \in [477/400, 6/5]$, $\beta_{\text{lo}} = 1/5$; **167** all-Taylor leaves replacing **4,823** legacy `COUNT` leaves (**28.88x** reduction).
  - `T3lower` (`B3_T3lower_01_031..B3_T3lower_01_041`, 11 contracts, 33 roots): $p \in [31/100, 21/50]$, $\rho \in [477/400, 6/5]$, $\beta_{\text{lo}}(T_{3,\text{lower}}) = \beta_{\text{hi}}(T_2)$; **48** all-Taylor leaves replacing **932** legacy `COUNT` leaves (**19.42x** reduction).
- **Contiguous probability & $\beta$ boundary joins verified:** **129** contiguous probability joins (`34 + 35 + 21 + 8 + 21 + 10`) plus **64** exact $\beta$ boundary joins (**22** between `S0` and `T0` at $\beta = 1/5$ on panels `31..52`, **9** between `T0` and `T1` on panels `32..40`, **22** between `S2` and `T2` at $\beta = 1/5$ on panels `31..52`, and **11** between `T2` and `T3lower` on panels `31..41`).
- **Nearest-integer roots verified:** **417** across all 135 `B3` contracts.
- **Total all-Taylor leaves:** **1,633** (vs. **30,903** legacy `COUNT` leaves — an **18.92x** leaf reduction across the entire `B3` band), with **0** baseline fallback leaves, **0** empty-domain leaves, and **0** raw-moment dual prices required.
- **Exact certificate checks replayed (`evidence/replay01/accepted/RESULT.json`):**
  - **19,596** univariate global Sturm ray checks on the compactified ray $[0, 1]$ (`12` per cell)
  - **50,623** curvature-corrected PSD Bernstein coefficients (`31` per cell: two degree-7 diagonal tests with 8 coefficients each and one degree-14 determinant test with 15 coefficients)
  - **1,404,400** bivariate degree-$(9, 4)$ score tensor Bernstein coefficients (`50` per vertex-corner across **28,088** vertex-corner combinations using the 4-endpoint-pair moment reduction)
- **Negative and corruption controls (`evidence/controls01/accepted/RESULT.json`):** **48** negative controls rejected (including broken `B3` probability and $\beta$ joins, missing/swapped panels, legacy 9-pair method tags, ambiguous `(band, index)` selectors, and proof-tree mutations).

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

3. **Exact $\beta$-Forced Noise and Variance-Allocation Floors (`beta_floors` / `map_slab`):**
   On panels where $M_{\beta,\text{lo}} = \max_{p \in [p_l, p_u]} \text{Bernstein}_3(v(p)(1 - \beta_{\text{lo}} - 2p)) < 0$ (`T0` and `T2` panels `41..52` with $\beta_{\text{lo}} = 1/5$ and $p > 2/5$), every $(x, y) \ge 0$ satisfying $(1 + \beta_{\text{lo}}) x - (1 - \beta_{\text{lo}}) y \le M_{\beta,\text{lo}} < 0$ satisfies
   $$5(x + y) \ge 5y \ge \text{lo}_b := \min\Big(\Lambda,\ \frac{-5 M_{\beta,\text{lo}}}{1 - \beta_{\text{lo}}}\Big) > 0, \qquad \frac{y}{x + y} > \alpha_b := \frac{1 + \beta_{\text{lo}}}{2} = \frac{3}{5}.$$
   When `noise` is subdivided (`(lo, hi) != (0, LAMBDA)`) or `alpha` is subdivided (`(al, ah) != (0, 1)`), mapping `[lo, hi]` affinely from `[0, LAMBDA]` onto `[lo_b, LAMBDA]` and `[al, ah]` affinely from `[0, 1]` onto `[al_b, 1]` preserves the exact partition of the feasible polygon while ensuring non-empty child cells.

## 3. Portable Commands

```bash
# Verify byte inventory
python3 -I -B -S research/b3-band-20261106/n5-b3-band/portable.py verify

# Run single-root smoke test (B3_S2_01_050 k=3)
python3 -I -B -S research/b3-band-20261106/n5-b3-band/portable.py smoke --out /tmp/b3_smoke

# Run 48 negative and corruption controls
python3 -I -B -S research/b3-band-20261106/n5-b3-band/portable.py controls --out /tmp/b3_controls

# Replay all 135 B3 contracts (417 roots, 1,633 all-Taylor leaves)
python3 -I -B -S research/b3-band-20261106/n5-b3-band/portable.py replay --out /tmp/b3_replay
```
