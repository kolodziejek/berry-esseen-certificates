# Complete 32-Contract `n = 5` `BN` Band (`n5-bn-band`)

Self-contained portable verification package for the **complete 32-contract `n = 5`, `K = 0` `BN` band replacement** (`research/bn-band-20261106/n5-bn-band/`): all **32 original `n = 5`, `K = 0` `BN` contracts** (`BN_034..BN_065`, 99 nearest-integer roots, 13,265 legacy checked leaves) across `gamma16_01`, `B0_BN_rest01`, and `pilots01`, covering the contiguous probability interval $p \in [17/50, 33/50]$ under the uniform moment slab $\rho \in [11/10, 23/20]$.

## 1. Summary of Verified Results

- **Contracts verified:** **32 / 32** (`BN_034..BN_065`, indices `34..65`, 100% of the `BN` band in `CENSUS_295.json`).
- **Contiguous probability coverage & joins:** **31** exact rational endpoint joins (`pu(index) == pl(index + 1)`) forming the gap-free closed interval $p \in [17/50, 33/50]$, including **5** cross-slab-family / half-boundary joins:
  - $p = 41/100$: `BN_040` (`gamma16_01`) $\to$ `BN_041` (`B0_BN_rest01`)
  - $p = 9/20$: `BN_044` (`B0_BN_rest01`) $\to$ `BN_045` (`pilots01`)
  - $p = 23/50$: `BN_045` (`pilots01`) $\to$ `BN_046` (`B0_BN_rest01`)
  - $p = 1/2$: `BN_049` (`B0_BN_rest01`, left probability half) $\to$ `BN_050` (`pilots01`, right probability half)
  - $p = 51/100$: `BN_050` (`pilots01`) $\to$ `BN_051` (`B0_BN_rest01`)
- **Nearest-integer roots verified:** **99** across `BN_034..BN_065`.
- **Total all-Taylor leaves:** **617** (vs. **13,265** legacy `COUNT` leaves — a **21.50x** leaf reduction across the entire `BN` band), with **0** baseline fallback leaves, **0** empty-domain leaves, and **0** raw-moment dual prices required.
- **Exact certificate checks replayed (`evidence/replay01/accepted/RESULT.json`):**
  - **7,404** global Sturm ray certificates on $[0, 1]^2$
  - **19,127** univariate degree-7/14 curvature-corrected PSD Bernstein coefficients
  - **1,239,300** bivariate degree-$(9, 4)$ score tensor Bernstein coefficients
- **Negative and corruption controls (`evidence/controls01/accepted/RESULT.json`):** **48** negative controls rejected (including broken `BN` band joins, missing panels, swapped panels, ambiguous `(band, index)` selectors, and proof-tree mutations).

## 2. Key Mathematical Mechanism: Elevated-Noise Variance Allocation (`alpha`) and Cauchy-Schwarz Support-Moment Tightening

On central `BN` panels (`BN_041..BN_057`) near $p = 1/2$, the acquired noise ceiling reaches $\Lambda \approx 0.403$, and legacy `COUNT` trees required hundreds of `EMPTY_RHO_BRANCH` and `EMPTY_SHARP_BOX` leaves per panel. In `model_all_taylor.py`:
1. Subdividing the variance-allocation ratio $\alpha = \frac{y}{x+y} \in [\alpha_l, \alpha_h] \subseteq [0, 1]$ on elevated noise slabs ($\text{lo} > 0$) adds the two exact linear cone halfplanes $\alpha_l x - (1 - \alpha_l) y \le 0$ and $-\alpha_h x + (1 - \alpha_h) y \le 0$ to the cell variance polygon $V$, yielding positive lower bounds $x_{\min} = \min_{(x,y)\in V} x$ and $y_{\min} = \min_{(x,y)\in V} y$ and hence conditional variance floors $s_{0,\min} = \frac{x_{\min}}{1 - p_l}$ and $s_{1,\min} = \frac{y_{\min}}{p_u}$.
2. For centered sign-conditioned marginals $U_0 \in [-A_0, a_0] \subseteq [-A_0, r_0]$ and $U_1 \in [-a_1, A_1] \subseteq [-r_1, A_1]$, the nonnegative support-square polynomials $(U_0 + A_0)(U_0 - s_0/A_0)^2 \ge 0$, $(a_0 - U_0)(U_0 + s_0/a_0)^2 \ge 0$, and $U_0^2(U_0 + A_0)(r_0 - U_0) \ge 0$ tighten the skewness intervals to $\gamma_0 \in [g_{0,\text{lo}}, g_{0,\text{hi}}] = [-A_0 + \min(A_0, s_{0,\min}/A_0),\, r_0 - \min(r_0, s_{0,\min}/r_0)]$ and $\gamma_1 \in [g_{1,\text{lo}}, g_{1,\text{hi}}] = [-r_1 + \min(r_1, s_{1,\min}/r_1),\, A_1 - \min(A_1, s_{1,\min}/A_1)]$, with exact affine fourth-moment upper envelopes $\kappa_0 \le K_0(\gamma_0) = (r_0 - A_0)\gamma_0 + A_0 r_0$ and $\kappa_1 \le K_1(\gamma_1) = (A_1 - r_1)\gamma_1 + A_1 r_1$.
3. The acquired normalized third-moment bounds $R \le R_+$ and $G \in [G_-, G_+]$ clip the outer variance polygon by three additional exact linear halfplanes in $(x, y)$. Because all tightened corner constants depend only on the cell, the Hessian $H_F(p)$ in $(x, y)$ and the score tensor bidegree $(9, 4)$ in $(p, u)$ are unchanged, and every cell with $\text{lo} = 0$ and $(\alpha_l, \alpha_h) = (0, 1)$ reduces identically to the `B0` model.

## 3. Portable Commands

```bash
# Verify byte inventory
python3 -I -B -S research/bn-band-20261106/n5-bn-band/portable.py verify

# Run single-leaf smoke test (BN_039 k=3)
python3 -I -B -S research/bn-band-20261106/n5-bn-band/portable.py smoke --out /tmp/bn_smoke

# Run 48 negative and corruption controls
python3 -I -B -S research/bn-band-20261106/n5-bn-band/portable.py controls --out /tmp/bn_controls

# Replay all 32 BN contracts (99 roots, 617 all-Taylor leaves)
python3 -I -B -S research/bn-band-20261106/n5-bn-band/portable.py replay --out /tmp/bn_replay
```
