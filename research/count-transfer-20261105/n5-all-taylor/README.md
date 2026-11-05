# All-Taylor Curvature-Corrected $n=5$ Count-Transfer Package (`n5-all-taylor`)

This additive package upgrades the $n=5$ six-count transfer model to an **all-Taylor, curvature-corrected, both-half** formulation with an unambiguous **295-contract external selector**, and proves the positive closed-score implication across **7 complete original $n=5$ acquired contracts** in **63 total leaves** (versus **2,736** leaves in the old `COUNT` certificates, a **43.4x** reduction; and **49** leaves across `BN39`, `B0_50`, `B2_S3_34`, `BN38` versus **2,296** leaves in the baseline/mixed six-count packages, a **46.9x** reduction).

The target constant $C_E = 9199/25000$ and $K = 0$ are unchanged. Original acquisition remains a premise; this is not a full 295-row $n=5$ sweep or a manuscript-deletion claim.

## 1. Mathematical & Architectural Upgrades

1. **Both-Half Quadratic Gaussian Taylor Scalar (`code/gaussian_scalar.py`):**
   - Extends `gaussian(n, k, pl, pu, ul, uh, lam)` from `0 < pl < pu <= 1/2` to all `0 < pl < pu < 1` by replacing the left-half monotonicity shortcut $v_{\min} = p_l(1 - p_l)$ with the general concave endpoint minimum
     $$v_{\min} = \min\bigl(p_l(1 - p_l),\, p_u(1 - p_u)\bigr), \qquad d_{\min} = n v_{\min} + \lambda > 0.$$
   - Adds `curvature(n, k, pl, pu, ul, uh, lo=0)` implementing the uniform second-derivative bound on $g(\lambda) = \Phi(a/\sqrt{d_0 + \lambda})$:
     $$g''(\lambda) \le M := \frac{3\max(a_{\max}, 0)\,\Phi_{\mathrm{HI}}}{4\,d_{\min}^2\,s_{\min}}, \qquad d_{\min} = n v_{\min} + \mathrm{lo}, \qquad s_{\min} = \sqrt{d_{\min}},$$
     whenever $\min(a_{\min}, 0)^2 \le 3 d_{\min}$ (enforced by exact assertion). When $a_{\max} \le 0$, $g$ is concave on $[\mathrm{lo}, \infty)$ and $M = 0$.

2. **All-Taylor Curvature-Corrected Leaf Acceptance (`code/model_all_taylor.py`):**
   - Every leaf uses `method == "taylor"` with the cleared degree-7/14 univariate Bernstein certificate
     $$v^2\bigl(H_F(p) - n^2 M J\bigr) = v^2\bigl(H_F(p) - 25 M J\bigr) \succeq 0 \quad \text{on } [p_l, p_u].$$
   - Because $F(p, u, x, y) - \Phi\bigl((k+u-5p)/\sqrt{5pq + 5(x+y)}\bigr)$ is thereby convex in $(x, y)$ across the entire mean-noise polygon (both for $a_{\max} \le 0$ where $M = 0$ and across $a = 0$ where $M > 0$), the quadratic Gaussian Taylor lower polynomial in $(p, u)$ is evaluated directly at each polygon vertex's exact noise $\lambda = 5(x + y)$.
   - Supports optional non-negative dual raw-moment prices $(a, b, c, d) \ge 0$ (`raw_moment_prices` in leaf JSON, defaulting to $(0, 0, 0, 0)$) for the cell-wide raw cubic bounds $F_{\mathrm{lo}} \le F(x, y, f_0, f_1) \le F_{\mathrm{hi}}$ and $G_{\mathrm{lo}} \le G(x, y, g_0, g_1) \le G_{\mathrm{hi}}$, verified identically at every $(p, u)$ Bernstein coefficient before testing the 50 degree-$(9, 4)$ score tensor coefficients per polygon vertex and moment corner.

3. **General External Contract Selector Across All 295 Original $n=5$ Contracts (`code/selector.py`, `contracts/CENSUS_295.json`):**
   - Inventories all 295 original $n=5$ contracts across `B0` (29), `BN` (30), `B2` (92 across `S0..S3`), and `B3` (144 across `S0..S3`), handling right-half probability cells ($p \ge 1/2$), the fourth active root $k = 4$, and $\rho$ floor $1$.
   - Resolves contracts unambiguously by `row_id`, canonical `path`, `sha256`, or structured query (`band`, `slab_family`, `index`, `p`, `rho`, `beta`), and explicitly rejects ambiguous `(band, index)` queries when multiple signed slabs share the same band and panel index (68 such pairs exist across `B2` and `B3`).
   - Conservatively derives the complete active nearest-count root family $k \in \{1, 2, 3, 4\}$ from `contract["raw"]` and verifies exact interval equality against `contract["derived"]["roots"]`.

## 2. Verified Rows Summary

| Row ID | Original Contract Path | Band / Slab | $p$ | $\rho$ | Roots ($k$) | Old `COUNT` Leaves | Prior Six-Count Leaves | All-Taylor Leaves |
|---|---|---|---|---|---|---:|---:|---:|
| `BN39` | `.../gamma16_01/n5/BN/panel039/contract.json` | `BN` / `gamma16_01` | $[39/100, 2/5]$ | $[11/10, 23/20]$ | $1, 2, 3$ | 809 | 1,126 (mixed) | **18** (`5+12+1`) |
| `B0_50` | `.../pilots01/n5/B0/panel050/contract.json` | `B0` / `pilots01` | $[1/2, 51/100]$ | $[1, 11/10]$ | $2, 3$ | 212 | 383 (baseline) | **11** (`9+2`) |
| `B2_S3_34` | `.../B2_S3_endpoint02/n5/B2/panel034/contract.json` | `B2` / `B2_S3_endpoint02` | $[17/50, 7/20]$ | $[467/400, 237/200]$ | $1, 2, 3$ | 731 | 54 (baseline) | **7** (`4+2+1`) |
| `BN38` | `.../gamma16_01/n5/BN/panel038/contract.json` | `BN` / `gamma16_01` | $[19/50, 39/100]$ | $[11/10, 23/20]$ | $1, 2, 3$ | 822 | 733 (baseline) | **13** (`6+6+1`) |
| `B0_53` | `.../B0_BN_rest01/n5/B0/panel053/contract.json` | `B0` / `B0_BN_rest01` | $[53/100, 27/50]$ | $[1, 11/10]$ | $2, 3, 4$ | 96 | — | **5** (`2+2+1`) |
| `B3_S0_59` | `.../B3_S0_01/n5/B3/panel059/contract.json` | `B3` / `B3_S0_01` | $[59/100, 3/5]$ | $[237/200, 477/400]$ | $2, 3, 4$ | 32 | — | **4** (`1+2+1`) |
| `B3_S2_59` | `.../B3_S2_01/n5/B3/panel059/contract.json` | `B3` / `B3_S2_01` | $[59/100, 3/5]$ | $[477/400, 6/5]$ | $2, 3, 4$ | 34 | — | **5** (`2+2+1`) |
| **Total (7 rows)** | | | | | **19 roots** | **2,736** | **2,296** (4 rows) | **63** (**49** on 4 rows) |

## 3. Reproduction (Python 3.12+, standard library only)

Run from this directory (or pass paths relative to repository root). Never use `-O` or `-OO`. Choose fresh output paths outside this package:

```sh
python3 -I -B -S portable.py verify
python3 -I -B -S portable.py smoke --out /tmp/n5-all-taylor-smoke
python3 -I -B -S portable.py controls --out /tmp/n5-all-taylor-controls
python3 -I -B -S portable.py replay --out /tmp/n5-all-taylor-replay
```

- `verify` checks the SHA-256 byte manifest in `FILES.json`.
- `smoke` runs a fast (< 1 s) exact positive closed-region acceptance check on the single-leaf `BN39` `k=3` root.
- `controls` runs 43 exact negative and corruption controls (< 1 s), including selector disambiguation across all 68 ambiguous `(band, index)` pairs, incomplete root covers (dropping `k=4` on `B0_53`), invalid dual prices, curvature PSD failures ($c_{j,4} = 10^{-9}$ when $M > 0$), excessive negative numerators ($\min(a_{\min}, 0)^2 > 3 d_{\min}$), and coefficient mutations.
- `replay` resolves all 7 contracts through `code/selector.py` and freshly verifies all 19 roots (63 all-Taylor leaves, 756 Sturm rays, 1,953 univariate PSD Bernstein coefficients, and 121,500 bivariate score tensor coefficients) in ~29 seconds.
