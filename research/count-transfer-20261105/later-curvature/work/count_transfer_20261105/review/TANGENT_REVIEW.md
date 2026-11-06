# Independent review of the sharp-39 tangent-price rectangle

Mathematical status: **locally derived and checked conditional implication**. The selected original acquisition, support and resource hypotheses remain premises. Execution status: **fresh full constructor acceptance plus a fresh bounded independent algebra audit**. This is not a complete original row, an acquisition replay, or a new all-law sharp-39 proof.

The accepted scope is

\[
n=39,\quad k=15,\quad
3849/10000\le p\le3851/10000,\quad
-1/1000\le u\le1/1000,\quad0\le\lambda\le37/200.
\]

I read `later/GENERAL_N_SOUNDNESS.md`, `TANGENT_PRICE.md`, `CONTINUOUS_RECTANGLE.md`, the full base/tangent/rectangle kernels, their source-bound canonical entry points, and the original selected row. Paths in this note are relative to `work/count_transfer_20261105/` unless prefixed `runs/`. No mathematical defect was found at the stated scope.

## Independent derivation

Set \(q=1-p,v=pq,x=q\mathbb E U_0^2,y=p\mathbb E U_1^2,w=v+x+y\). The original row has outward caps \(A_0=A_1=471/1000\), inward sum cap \(d_0=233/10000\), and noise cap \(\Lambda=37/200\). Its exact raw absolute cube is

\[
R=v(1-2v)+(3p-\gamma_0)x+(3q+\gamma_1)y.
\]

This identity uses the original sign-conditioned supports. It does not follow for an arbitrary pair of centered residual distributions without those signs. On actual laws \(R=\rho w^{3/2}>0\).

Convexity of \(w^{-3/2}\) gives

\[
w^{-3/2}\ge\frac{5W-3w}{2W^{5/2}}.
\]

For \(0<w\le W\), the right numerator is positive. Hence any downward positive coefficient \(c\le C_{\rm E}/(2\sqrt n W^{5/2})\) gives the lower normalization price \(cR(5W-3w)\). Blending with the universal \(\rho\ge1\) floor by a fixed \(\theta\in[0,1]\) is valid. Artificial moment corners need not have \(R\ge0\): the lower bound is justified on actual laws first, and the resulting polynomial objective is then maximized over an outer domain.

For fixed variances, the price is affine in each conditional skew, and its inward-endpoint dependence is linear. The upper fourth-moment expression retains its nonnegative quadratic inward coefficient. Thus the existing nine **common** moment corners remain sufficient, including the zero-variance case without division. This does not assert an actual-law inequality \(\mathbb E U_i^4\le\gamma_i^2\mathbb E U_i^2\).

The essential new issue is convexity in \((x,y)\). If \(r_0=3p-\gamma_0,r_1=3q+\gamma_1\), the negative price contributes

\[
3c\theta
\begin{pmatrix}2r_0&r_0+r_1\\r_0+r_1&2r_1\end{pmatrix}
\]

to the Hessian. Its determinant before the positive prefactor is \(-(r_0-r_1)^2\), so the price is not automatically convex. The mixture contributes

\[
H_F=\sum_{j=0}^n6(1-1/n)b_jQ_{j,4}
\begin{pmatrix}(n-j)/q\\j/p\end{pmatrix}
\begin{pmatrix}(n-j)/q&j/p\end{pmatrix}.
\]

The implemented test checks the two diagonal entries and determinant of the **sum**, for every common corner and every probability in a strip. This is the correct sufficient matrix condition.

## Continuous-domain licenses

The following were checked directly against the fixed original row and the executable formulas.

- Both inward caps equal \(d_0\) throughout the full rectangle because \(d_0<\min(3849/10000,1-3851/10000)\). A pointwise inward cap is therefore not being substituted for a smaller cell-dependent cap.
- \(\operatorname{Var}U_i\le A_i a_i\) implies \(d\ge x/(qA_0)+y/(pA_1)\). Substitution into the two original resource inequalities gives the two polygon facets. Replacing \(q\) and \(p\) in their denominators by \(1-p_-\) and \(p_+\) reduces the positive coefficients, hence gives a safe fixed outer polygon. The original \(\Lambda\), rather than a smaller auxiliary cap, is retained in the joint-resource intercept.
- All polygon vertices come from pairwise intersections satisfying every halfplane. Nonnegativity and the finite noise triangle make the polygon bounded; the admitted examples have three vertices. The union of four closed probability strips covers the stated rectangle, with shared endpoints included.
- For a fixed noise, the Gaussian coordinate decreases in \(p\) and increases in \(k+u\) when the threshold lies in \([0,n]\). The lower endpoint function \(G(\lambda)=\Phi((15-1/1000-39p_+)/\sqrt{39p_+(1-p_+)+\lambda})\) is concave in \(\lambda\) under the checked negative-numerator and squared-coordinate guards. Thus \(-G(39(x+y))\) is convex and its vertex-specific directed enclosure is valid. There is no claim of this concavity on a sign-crossing cell.
- On each strip, \(W=p_+(1-p_+)+\Lambda/39\) bounds all actual \(w\), since this rectangle lies below \(1/2\). The price coefficient is fixed on the strip. Every division has a positive denominator.
- Multiplication by \(v^2>0\) gives moment/score bidegree at most \((43,4)\). The cleared Hessian entries have degree at most \(41\), and the determinant at most \(82\). The tangent term alone has probability degree at most \(10\), so it fits the stated score degree.
- All forty conditional counts share one conditional pair and one moment choice. The eighty global majorant rays include zero in the closed event. The result is for the acquired positive closed-score orientation; a negative CDF orientation requires its own reflected acquisition.

## Fresh independent executable evidence

Source: `review/check_tangent_rectangle_independent.py`, SHA-256
`7b3b71263c9b242ebccddd6418fba5a1240a726f759eedbbc755f17f52d7864a`.

Fresh capture:
`runs/count_transfer_20261105/review_tangent_rectangle01/PROCESS.json`.
Actual return code 0, 7.888978 seconds, ordinary Python 3.12.14, empty stderr, input/source hashes unchanged. The full selected source/contract/object closure is also checked before and after inside the review script.

Result:
`runs/count_transfer_20261105/review_tangent_rectangle01/checked/RESULT.json`, SHA-256
`f13c034e18586753c473566749a8cda895471fc678a22ffcc15a616f97debccd`.

The independent calculation uses sparse polynomial Taylor expansion of each translated quartic and the four common moment formulas. It extracts the Hessian by collecting quadratic \(x,y\) coefficients, rather than calling or copying the constructor's matrix formula. It verifies:

- 18 full Hessian polynomial triples: all nine common corners on the first and last probability strips;
- six complete moment/score polynomial tensors: outward, zero and inward choices at the three vertices on both strips;
- independent inverse expansion of 3,006 univariate Bernstein coefficients and 1,320 tensor coefficients, with exact positivity checks;
- 60 coefficient mutations, six actual-law semantic examples including four zero-variance components and rare-outlier cases, and explicit controls showing the bare price Hessian can be indefinite and the positive-factor license cannot be extrapolated beyond its range.

The actual-law examples test moment/price semantics, not all original contact or acquisition conditions. The last range control concerns positivity and downward-rounding use of the tangent factor; the underlying convex tangent inequality itself remains valid for all positive \(w\). These distinctions are part of the result's scope.

This audit shares the directed Gaussian primitive and does not independently replay the eighty global rays. The full source-bound constructor acceptance supplies all four strips, all vertices/corners and the global rays. The independent tests above are stronger algebraic checks on a precisely stated subset, not a second complete reader.

## Accepted execution identity and data handling

Selected complete constructor capture:
`runs/count_transfer_20261105/later_rectangle02/PROCESS.json`, actual return code 0, 24.701422500016633 seconds, empty stderr.

Its result is
`runs/count_transfer_20261105/later_rectangle02/checked/RESULT.json`, SHA-256
`2138f4faf71deac1e67d26dab584b610885ccf3208217189447e50f78cbc2069`.
It reconstructs 23,760 score coefficients, 6,012 PSD coefficients and eighty global rays.

The additive `accept_rectangle.py` wrapper checks canonical proof-object data and the complete `PUBLIC_SOURCE_PINS.json` closure before and after invoking the unchanged kernel. Its SOURCE_BINDING receipt has SHA-256
`e26b01745ef00366d7a103107b9027002d70739f8cd22d27f36eb1c460cc1109`.
The selected coefficient object has SHA-256
`dffec8eb618e7390905c7aa5c93a0126c252c6616e0118cdc90cea0df28d0502`.
The original source contract has SHA-256
`6e3ba2cef34cc577ef966ebe5708b83bccd33698b4388f8c0f652c239661f1c4`.

The first rectangle capture bound only its top-level script and is preserved as a historical epoch. The selected second capture closes that provenance limitation. Canonical data guards reject duplicate keys, booleans, integers, floats and noncanonical rational strings; the selected object was already canonical. Hashes establish byte identity, not the analytic result.

Two wording refinements were sent to the parent for the separate scalar note: specify the **fixed affine** price in the old convexity sentence, and distinguish exact first-order tangent contact from the extra downward rational rounding gap. Neither changes the accepted rectangle mathematics.

No manuscript sources or inherited proof objects were modified. The complete original probability/phase row, its other nearest-count domains, and every other sharp-39 row remain outside this new rectangle result.
