# Independent Review of the 7-Row All-Taylor Curvature-Corrected $n=5$ Package and 295-Contract Selector

Mathematical status: **locally derived and checked conditional positive closed-score implication across 7 complete original $n=5$ acquired contracts (`BN39`, `B0_50`, `B2_S3_34`, `BN38`, `B0_53`, `B3_S0_59`, `B3_S2_59`, 19 roots, 63 all-Taylor leaves)**.
Execution status: **fresh complete 7-row replay (`n5-all-taylor/evidence/replay01/`), 43 exact negative and corruption controls (`n5-all-taylor/evidence/controls01/`), and fresh independent PSD Hessian, bivariate Bernstein inverse, and 295-contract selector audit (`review/runs/count_transfer_20261105/review_all_taylor01/`)**.
Original acquisition remains a premise; no all-295 $n=5$ theorem or manuscript deletion is claimed.

## 1. Mathematical Audit

1. **Both-Half Quadratic Gaussian Taylor Scalar (`code/gaussian_scalar.py`):**
   - For any closed cell $[p_l, p_u] \times [u_l, u_h]$ with $0 < p_l < p_u < 1$ and fixed noise $\lambda \ge 0$, concavity of $p(1-p)$ implies
     $$p(1-p) \ge v_{\min} := \min\bigl(p_l(1-p_l),\, p_u(1-p_u)\bigr) > 0, \qquad D = 5p(1-p) + \lambda \ge d_{\min} := 5 v_{\min} + \lambda > 0.$$
   - Using $v_{\min}$ in place of the left-half formula $p_l(1-p_l)$ preserves all gradient and uniform Hessian bounds on $(p, u) \mapsto \Phi\bigl((k+u-5p)/\sqrt{5p(1-p)+\lambda}\bigr)$ across both probability halves ($p \le 1/2$, $p \ge 1/2$, and cells crossing $1/2$).

2. **Uniform Noise-Curvature Correction (`curvature` and `psd_check`):**
   - With $a = k + u - 5p \in [a_{\min}, a_{\max}]$ and $D = 5p(1-p) + \lambda \ge d_{\min} = 5 v_{\min} + \mathrm{lo} > 0$,
     $$g''(\lambda) = \frac{a(3D - a^2)\phi(a/\sqrt{D})}{4 D^{7/2}}.$$
   - The exact guard $\min(a_{\min}, 0)^2 \le 3 d_{\min}$ guarantees $3D - a^2 \ge 0$ for all $a \le 0$ on the cell, so $g''(\lambda) \le 0$ whenever $a \le 0$. When $a_{\max} \le 0$, $M = 0$; when $a_{\max} > 0$, dropping $-a^3 \le 0$ yields
     $$g''(\lambda) \le M := \frac{3\max(a_{\max}, 0)\,\Phi_{\mathrm{HI}}}{4\,d_{\min}^2\,s_{\min}}, \qquad 0 < s_{\min} \le \sqrt{d_{\min}}.$$
   - Because $\lambda = 5(x+y)$, the true variance loss has Hessian $H_F(p) - 25 g''(\lambda) J \succeq H_F(p) - 25 M J$. Multiplying by the positive clearing factor $v^2 = p^2(1-p)^2$ gives three degree-7 entries $v^2(H_{ab}(p) - 25 M)$ and a degree-14 determinant. Non-negativity of their univariate Bernstein expansions on $[p_l, p_u]$ (7+1, 7+1, and 14+1 = 31 coefficients per leaf) certifies convexity in $(x, y)$ across the entire mean-noise polygon, licensing evaluation of the quadratic Gaussian Taylor lower polynomial at each polygon vertex's exact noise $\lambda = 5(x+y)$.
   - Across the 63 accepted leaves, 40 have $a_{\max} \le 0$ ($M = 0$) and 23 cross $a = 0$ ($M > 0$).

3. **295-Contract External Selector (`code/selector.py`, `contracts/CENSUS_295.json`):**
   - Verified all 295 original $n=5$ contracts: 100 lie in the right half ($p_l \ge 1/2$), 112 activate the fourth threshold root $k = 4$, and 24 have $\rho_{\mathrm{lower}} = 1$.
   - Partitioned all `(band, index)` pairs into 58 unique pairs and 68 ambiguous multi-slab pairs (in `B2` and `B3`), confirming that `select_contract({'band': band, 'index': idx})` rejects every ambiguous pair and resolves every pair uniquely once `slab_family` is supplied.

## 2. Independent Reconstruction Receipt

- **Review script:** `work/count_transfer_20261105/review/check_all_taylor.py` (SHA-256 `8004ce48ec293ca88952f70324f6785eb050c886d3b37231414f61adaf32e0fd`).
- **Capture receipt:** `runs/count_transfer_20261105/review_all_taylor01/PROCESS.json` (SHA-256 `1985e783064fe99feac9a8d2c7ecd38634ab7b02467c257c964a5462a0cf9d7d`, return code `0`, `71.886` seconds, empty stderr, unchanged source closure).
- **Result receipt:** `runs/count_transfer_20261105/review_all_taylor01/checked/RESULT.json` (SHA-256 `de48c0eac95091a7f8fa5f165c5a3518a823ff212e98d46bd7076df81d76202d`):
  - 7 rows, 19 roots, 63 all-Taylor leaves independently verified;
  - 1,953 univariate PSD Bernstein coefficients independently inverted and checked;
  - 121,500 bivariate degree-(9,4) score tensor coefficients independently inverted and checked against direct polynomial expansions;
  - 68 ambiguous `(band, index)` selector queries rejected and 63 target-tensor mutations rejected.
