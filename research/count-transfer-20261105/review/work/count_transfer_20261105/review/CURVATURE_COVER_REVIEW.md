# Independent review of the two-cell Gaussian-curvature cover

Mathematical status: **locally derived and checked conditional implication**. Execution status: **fresh full two-cell constructor acceptance and fresh independent corrected-Hessian audit**. Original acquisition remains a premise. The accepted new scope is

\[
n=39,\quad k=15,\quad p\in[19/50,39/100],\quad
u\in[-1/100,1/100],\quad0\le\lambda\le37/200.
\]

This covers the complete probability interval of the selected sharp-39 row only on the stated narrow phase interval and one threshold root. It does not cover the complete original row. I read the complete single-cell and two-cell readers, their analytic notes, scalar controls and closed-cover/body controls. No mathematical defect was found.

## Uniform curvature derivation

At fixed \(p,u\), let \(a=k+u-np\), \(D=np(1-p)+\lambda\), and \(g(\lambda)=\Phi(a/\sqrt D)\). Direct differentiation gives

\[
g''(\lambda)=\frac{a(3D-a^2)\phi(a/\sqrt D)}{4D^{7/2}}.
\]

For a cell with \(D\ge d>0\), \(a\in[a_-,a_+]\),
\(\min(a_-,0)^2\le3d\), a positive lower square root \(s\le\sqrt d\), and \(\phi_+\ge\phi(0)\),

\[
g''(\lambda)\le M:=\frac{3\max(a_+,0)\phi_+}{4d^2s}.
\]

For negative \(a\), the square guard makes \(3D-a^2\ge0\), so the curvature is nonpositive. For positive \(a\), drop the negative cubic term and bound the remaining positive expression by the displayed constant. This argument includes zero numerator and zero noise. It does not assume concavity on a sign-crossing cell.

For the full requested rectangle, \(a\in[-.22,.19]\) and \(d=39(.38)(.62)\), so the negative-numerator guard holds. On the selected left cell \([.38,.385]\), \(M>0\); on the right cell \([.385,.39]\), \(a_+<0\) and \(M=0\).

Let \(H_0\) be the variance Hessian of the common quartic upper expectation minus the tangent cubic price. Since \(\lambda=n(x+y)\), the true loss has Hessian

\[
H_{\rm true}=H_0-n^2g''(\lambda)J
=(H_0-n^2MJ)+n^2(M-g'')J,
\qquad J=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

Thus \(H_0-n^2MJ\succeq0\) suffices. After the original positive clearing factor \(v^2\), the code must subtract \(n^2Mv^2\) from **all three matrix entries**, including the off-diagonal, before testing the determinant. That is what the implementation does. The entries retain degree at most 41 and the determinant at most 82. The Gaussian is independent of the two conditional skews, so the earlier common-corner reduction is unchanged.

Only after convexity of the true variance objective is proved are the Gaussian values at variance vertices replaced by their reviewed Taylor lower polynomials. No curvature property of those lower polynomials in variance is required.

## Closed coverage and preserved failure

`gaussian_curvature01/check_two_cells.py`, SHA-256
`bc656fcd874e2e866fb2bd47e36b35a7dd76cb5374d27d58528b0ba78461cf47`, validates exactly
\([19/50,77/200]\cup[77/200,39/100]\), with the shared boundary included twice. Its analytic checking body is identical to the earlier single-cell body, except that cell endpoints are explicit arguments. It reconstructs every inequality and does not accept stored success flags. All forty quartics, original target, resource assumptions, common conditional laws and noise ceiling are unchanged.

The single-cell attempt is preserved at `runs/count_transfer_20261105/later_gaussian_curvature01/checked/FAILED.json`, SHA-256 `2d01987140b6759e185aa80a1d456ada69c2395ddfd5432711b2c681ed705d8f`. Its actual return code was 1. All corrected PSD tests passed, but one score Bernstein coefficient was negative. That rejects the sufficient one-cell test; it does not show that the polynomial itself is negative or disprove the score inequality.

The selected two-cell complete result is `runs/count_transfer_20261105/later_gaussian_curvature_two01/checked/RESULT.json`, SHA-256 `e6495b16fc3f7fadc236951f94e05142219d1e778f9aacdeafd7d125d8d8f8d4`. The captured command returned 0 in 10.114259499998298 seconds, with empty stderr and unchanged source closure. It verifies 11,880 score coefficients and 3,006 PSD coefficients. The same eighty global ray conditions are checked in each cell, for 160 actual ray checks. This is a new accepted cover, not a relabeling of the failed attempt.

I reviewed `check_controls_v2.py`: exact second-derivative identities, both numerator signs and zero, the rank-one correction and five invalid domains are correctly tested. Its fresh result is `later_gaussian_curvature_controls02/checked/RESULT.json`. The earlier control harness's result-path serialization failure remains preserved. I also reviewed `check_cover_controls.py`: it compares analytic function bodies and rejects eight malformed, missing, duplicated, reordered or gapped fixed covers. These bounded controls support the implementation audit; the derivation above supplies the continuous argument.

## Fresh independent array audit

My additive source is `review/check_curvature_cover.py`, SHA-256
`14d9534362734544dc6dffc559cbd48e6532ce9de682580ca380dffdcf957d4f`.
It uses the already frozen independent sparse variance-quadratic expansion in `review/check_tangent_rectangle_independent.py`, then independently applies the Gaussian curvature correction. It checks:

- all 54 complete corrected Hessian entry arrays: three entries, nine common corners, two cells;
- independent inverse reconstruction of all 3,006 PSD Bernstein coefficients, exact positivity, and equality to the captured minima;
- 54 scalar endpoint/sign/noise cases;
- 18 mutations reversing the correction sign or dropping one chain-rule factor of \(n\).

Fresh capture: `runs/count_transfer_20261105/review_curvature_cover01/PROCESS.json`, actual return code 0, 3.2603766918182373 seconds, empty stderr and stable source closure. Result SHA-256:
`1a003c9a38e7b57ddd0d787f181004245c79028676c43640cdb2d7485f03f64e`.

This independent audit shares the scalar constants and does not independently repeat the complete score or global-ray reader. Its exact scope is stated in the result. No prior campaign, original acquisition or manuscript source was changed.
