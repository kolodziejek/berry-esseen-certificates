# Removing the sign restriction from the variance-vertex argument

Mathematical status: **locally derived and independently checked curvature lemma**. Execution status: **fresh exact failure of the requested final score tensor**, after the curvature-corrected PSD gates passed. There is no new accepted rectangle, and no statement about the complete original row.

This is an additive epoch. The earlier portable package and its accepted narrower rectangles are unchanged.

## Uniform curvature bound

Fix a probability and phase, write

\[
a=k+u-np,\qquad D=np(1-p)+\lambda,\qquad
g(\lambda)=\Phi(a/\sqrt D).
\]

Differentiating with respect to noise gives

\[
g'(\lambda)=-\frac{a\phi(a/\sqrt D)}{2D^{3/2}},\qquad
g''(\lambda)=\frac{a(3D-a^2)\phi(a/\sqrt D)}{4D^{7/2}}.
\]

Let a closed domain satisfy \(D\ge d>0\), \(a_-\le a\le a_+\), and
\(\min(a_-,0)^2\le3d\). Choose \(0<s\le\sqrt d\) and a rigorous upper bound \(\phi_+\ge\phi(0)\). Then

\[
g''(\lambda)\le M:=\frac{3\max(a_+,0)\phi_+}{4d^2s}.
\]

For negative \(a\), the square guard gives \(3D-a^2\ge0\), so \(g''\le0\). For nonnegative \(a\), discard the negative \(-a^3\) term in the numerator and use \(a\le a_+\), \(\phi\le\phi_+\) and \(D^{5/2}\ge d^2s\). The bound includes \(a=0\) and \(\lambda=0\). It is constant on the whole cell.

Here \(n=39,k=15,p\in[19/50,39/100],u\in[-1/100,1/100]\) and \(0\le\lambda\le37/200\). Hence

\[
a\in[-11/50,19/100],\qquad d=39(19/50)(31/50)=22971/2500,
\]

and \((11/50)^2<3d\). The lower directed square root and \(\phi_+\) are the original exact native enclosures. All signs and denominators are checked explicitly.

## Corrected Hessian and common-moment reduction

Retain the original coupled conditional law, variance coordinates \(x=q s_0,y=p s_1\), and \(\lambda=n(x+y)\). At each fixed probability, phase and shared moment corner, let \(H_0\) be the Hessian of the quartic expectation minus the tangent cubic price. The true loss, including the Gaussian term, has Hessian

\[
H_{\rm true}=H_0-n^2g''(\lambda)J,
\qquad J=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

If \(H_0-n^2MJ\) is positive semidefinite, then

\[
H_{\rm true}=(H_0-n^2MJ)+n^2(M-g'')J\succeq0.
\]

This proves convexity on the complete fixed outer variance polygon and licenses its vertex reduction even when the Gaussian numerator changes sign. The Gaussian does not depend on either conditional skew, so the earlier nine common-moment endpoint choices remain valid. No separate marginal is chosen for different count terms.

The existing Hessian polynomials are cleared by \(v^2\), \(v=p(1-p)>0\). Consequently the new exact test subtracts \(n^2Mv^2\) from **both diagonal entries and the off-diagonal entry** before computing the determinant. It tests both diagonals and the determinant on the complete probability interval. The degrees remain at most 41 for the entries and 82 for the determinant. Subtracting the correction only from the diagonals would not implement this argument.

Only after convexity of the actual loss is proved are the exact Gaussian values at polygon vertices replaced by the quadratic lower polynomials from `../gaussian_taylor01/SOUNDNESS.md`. These polynomials need not themselves be concave in noise. The quartic coefficient object, same-law resource polygon, tangent price, target constant, inward supports, global closed-event majorants and noise ceiling are unchanged.

## The one bounded experiment

`check_full_p.py` reconstructs this exact argument with the unchanged forty quartics. It verifies source and object hashes before and after successful acceptance; the outer capture verifies that the same complete closure stayed unchanged even on failure. The ordinary unoptimized command was

```sh
python3 -I -B -S check_full_p.py /absolute/NEW_OUTPUT
```

The actual stopped capture is `runs/count_transfer_20261105/later_gaussian_curvature01/`: return code 1 in 5.248639083001763 seconds. The 80 global rays and all nine curvature-corrected PSD corners passed. The smallest corrected PSD principal-minor Bernstein coefficient was approximately 3.6054062. However, the minimum score Bernstein coefficient was approximately \(-6.9031559\cdot10^{-6}\); its exact rational is preserved in `checked/FAILED.json`.

This negative coefficient rejects the selected sufficient one-cell tensor test. It does **not** prove a negative value of the polynomial or disprove the mathematical score inequality. No new discovery, coefficient tuning, subdivision, target change or original acquisition replay was performed. The full probability/narrow-phase implication remains unproved by this experiment. The curvature lemma itself remains available for another explicitly named certificate.
