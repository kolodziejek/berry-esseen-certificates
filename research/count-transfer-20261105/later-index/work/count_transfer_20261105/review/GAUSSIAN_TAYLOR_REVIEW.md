# Independent Gaussian Taylor lower-bound review

Mathematical status: **independently derived scalar enclosure**, with a source review of its bounded application. Execution status: the constructor has a **fresh exact broad-rectangle PASS**; this note does not claim an independent replay of that full rectangle.

The reviewed source is
`work/count_transfer_20261105/later/gaussian_taylor01/check_broad.py`, SHA-256
`01b169b84f1b5242fbaad9fd65ec54152a341a6f828caa9fb7b4d1d0eac65264`.
Its application is only \(n=39,k=15,p\in[3847/10000,39/100],u\in[-1/1000,1/1000],\lambda\in[0,37/200]\), under the selected original row hypotheses. I found no mathematical defect in the scalar function or its use in this domain.

## Derivation

Fix \(\lambda\ge0\), put \(t=k+u\), \(a=t-np\), \(D=np(1-p)+\lambda\), and \(z=aD^{-1/2}\). Then \(D'=n(1-2p)\), \(D''=-2n\), and direct differentiation gives

\[
\begin{aligned}
z_p&=-nD^{-1/2}-\tfrac12aD'D^{-3/2},&
z_t&=D^{-1/2},\\
z_{pp}&=n(D'+a)D^{-3/2}+\tfrac34a(D')^2D^{-5/2},&
z_{pt}&=-\tfrac12D'D^{-3/2},\qquad z_{tt}=0.
\end{aligned}
\]

For \(F(p,t)=\Phi(z)\),
\(F_{ij}=\phi(z)(z_{ij}-z z_i z_j)\). Let \(D\ge d>0\), \(|a|\le A\), \(|D'|\le B\), and choose a positive directed lower square root \(s\le\sqrt d\). The following are uniform upper bounds:

\[
\begin{aligned}
Z&=A/s,& Z_t&=1/s,& Z_p&=n/s+AB/(2ds),\\
Z_{pp}&=n(B+A)/(ds)+3AB^2/(4d^2s),&
Z_{pt}&=B/(2ds).
\end{aligned}
\]

Since \(\phi(z)\le\phi(0)<2/5\), valid absolute Hessian bounds are

\[
M_{pp}=\tfrac25(ZZ_p^2+Z_{pp}),\quad
M_{pt}=\tfrac25(ZZ_pZ_t+Z_{pt}),\quad
M_{tt}=\tfrac25ZZ_t^2,
\]

or any directed upper roundings of them. In particular the \(nA\) term in \(Z_{pp}\) has a positive sign; omitting it would be wrong.

At the center \((p_c,t_c)\), let \(F_c^-\le F(p_c,t_c)\), and let gradient intervals have midpoints \(g_p,g_t\) and radii \(e_p,e_t\). On half-widths \(h_p,h_t\), the gradient rounding budget is \(e_ph_p+e_th_t\). The integral Taylor remainder, with weight integral \(1/2\), yields

\[
F(p,t)\ge F_c^-+g_p\delta_p+g_t\delta_t-e_ph_p-e_th_t
-\tfrac12\{M_{pp}\delta_p^2+2M_{pt}|\delta_p\delta_t|+M_{tt}\delta_t^2\}.
\]

For any fixed \(\eta>0\), \(2|ab|\le\eta a^2+\eta^{-1}b^2\). Thus the displayed expression remains a lower bound after replacing its quadratic penalty by

\[
\tfrac12\{(M_{pp}+\eta M_{pt})\delta_p^2+
(M_{tt}+M_{pt}/\eta)\delta_t^2\}.
\]

The choice \(\eta=h_t/h_p\) minimizes this uniform rectangular cross-term allowance. Positive half-widths are required. No third-derivative remainder is needed.

## Source checks

The implementation's explicit \(0<p_-<p_+<1/2\) guard licenses \(d=np_-(1-p_-)+\lambda\). Its endpoint definitions of \(A\) and \(B\) bound the affine numerator and derivative over the complete rectangle. Both powers of the denominator and the square root are rounded in the safe direction.

At the center it encloses \(\phi(z_c)=\phi(0)e^{-a_c^2/(2D_c)}\) using even term 24 above and odd term 25 below. The explicit argument guard \(0\le a_c^2/(2D_c)\le1\) makes the alternating remainder direction immediate. The interval product for
\(z_p=D_c^{-1/2}[-n-a_cD'_c/(2D_c)]\) handles either sign; the derivative intervals and their midpoint radii are rounded outward. The center CDF value is already a rigorous lower enclosure, so it need not pay another rounding subtraction.

Expanding the centered quadratic gives exactly the code's constant, linear and quadratic power coefficients. The replacement has probability degree two and phase degree two; multiplication by \(v^2\) does not exceed the existing score degree \((43,4)\).

The argument is not that the Taylor polynomial is concave in variance. For each fixed \(p,u\), the genuine Gaussian is first known to be concave in \(\lambda\) throughout the selected negative-numerator domain. The quartic loss with the actual Gaussian is therefore convex in \((x,y)\), after the separate whole-probability PSD gate. Only at its variance vertices is the Gaussian replaced by the Taylor lower polynomial. This order is essential and is respected by the reader.

The larger interval \(p\in[.38,.39]\) crosses the Gaussian numerator sign for these phases and is not licensed by the same concavity argument. Nothing in this review asserts that extension.

The constructor capture is
`runs/count_transfer_20261105/later_gaussian_broad01/checked/RESULT.json`.
The reported exact scope comprises one closed probability/phase cell, eighty global rays, 5,940 score coefficients and 1,503 PSD coefficients. The full-row flag is false. The previous forty quartics and their target remain unchanged; only the sufficient Gaussian enclosure is strengthened. Original acquisition and the other probability/phase/count regions remain separate obligations.
