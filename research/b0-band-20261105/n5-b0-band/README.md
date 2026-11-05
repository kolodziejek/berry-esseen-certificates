# Complete 24-Contract `n = 5` `B0` Band (`n5-b0-band`)

Self-contained portable verification package for the **first complete `n = 5` band replacement** (`research/b0-band-20261105/n5-b0-band/`): all **24 original `n = 5`, `K = 0` `B0` contracts** (`B0_037..B0_060`, 67 nearest-integer roots, 5,040 legacy checked leaves) across `gamma16_01`, `pilots01`, and `B0_BN_rest01`, covering the contiguous probability interval $p \in [37/100, 61/100]$ under $\rho_{\text{lower}} = 1$ and $\rho_{\text{upper}} \le 11/10$.

## 1. Summary of Verified Results

- **Contracts verified:** **24 / 24** (`B0_037..B0_060`, indices `37..60`, 100% of the `B0` band in `CENSUS_295.json`).
- **Contiguous probability coverage & joins:** **23** exact rational endpoint joins (`pu(index) == pl(index + 1)`) forming the gap-free closed interval $p \in [37/100, 61/100]$, including **3** cross-slab-family / half-boundary joins:
  - $p = 23/50$: `B0_045` (`gamma16_01`) $\to$ `B0_046` (`B0_BN_rest01`)
  - $p = 1/2$: `B0_049` (`B0_BN_rest01`, left probability half) $\to$ `B0_050` (`pilots01`, right probability half)
  - $p = 51/100$: `B0_050` (`pilots01`) $\to$ `B0_051` (`B0_BN_rest01`)
- **Nearest-integer roots verified:** **67** (`k in {1, 2, 3}` on `B0_037..B0_047`, `k in {2, 3}` on `B0_048..B0_052`, and `k in {2, 3, 4}` on `B0_053..B0_060`).
- **Total all-Taylor leaves:** **222** (vs. **5,040** legacy `COUNT` leaves — a **22.70x** leaf reduction across the entire `B0` band), with **0** baseline fallback leaves and **0** raw-moment dual prices required.
- **Exact certificate checks replayed (`evidence/replay01/accepted/RESULT.json`):**
  - **2,664** global Sturm ray certificates on $[0, 1]^2$
  - **6,882** univariate degree-7 curvature-corrected PSD Bernstein coefficients
  - **456,300** bivariate degree-$(9, 4)$ score tensor Bernstein coefficients
- **Negative and corruption controls (`evidence/controls01/accepted/RESULT.json`):** **48** negative controls rejected (including broken `B0` band joins, missing panels, swapped panels, ambiguous `(band, index)` selectors, and proof-tree mutations).

## 2. Key Mathematical Mechanism: Bernoulli-Endpoint Noise Peeling (`lo == 0`)

On the left probability half ($p < 1/2$) of the `B0` band ($\rho_{\text{lower}} = 1$), the constant target term $\text{lower} = \frac{c_{\text{CE}} \rho_{\text{lower}}}{\sqrt{5}} v^{3/2}$ uses $\rho_{\text{lower}} = 1$, whereas at the Bernoulli vertex $(x, y) = (0, 0)$ the true normalized third absolute moment is $\rho_{\text{Bernoulli}}(p) = \frac{1 - 2v}{\sqrt{v}} > 1$. To unlock the third-moment improvement $\theta (c R - \text{lower})$ at $(x, y) = (0, 0)$ where $c = \frac{c_{\text{CE}}}{\sqrt{5} \, w_{\max}^{3/2}}$ and $w_{\max} = v_{\max} + \text{hi}_{\text{eff}}/5$, `discover_b0_band.py` peels the noise interval $[0, \text{hi}]$ at $\text{lo} = 0$ down to $\Lambda / 16$ when $\delta_u \le 1/8$, aligning $w_{\max}$ with $v$ near $\text{lo} = 0$ while keeping upper noise slabs ($\text{lo} > 0$) unsplit.

## 3. Portable Commands

```bash
# Verify byte inventory (191 tracked files)
python3 -I -B -S research/b0-band-20261105/n5-b0-band/portable.py verify

# Run single-leaf smoke test (B0_043 k=3)
python3 -I -B -S research/b0-band-20261105/n5-b0-band/portable.py smoke --out /tmp/b0_smoke

# Run 48 negative and corruption controls
python3 -I -B -S research/b0-band-20261105/n5-b0-band/portable.py controls --out /tmp/b0_controls

# Replay all 24 B0 contracts (67 roots, 222 all-Taylor leaves)
python3 -I -B -S research/b0-band-20261105/n5-b0-band/portable.py replay --out /tmp/b0_replay
```
