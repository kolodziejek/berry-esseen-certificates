# Closed-cell six-count comparison: the accepted V1 region

This is a conditional local implication, outside the manuscript proof DAG.
It does not replace the original five-summand proof. Its accepted domain is

\[
n=5,\quad p\in[19/50,39/100],\quad k=2,\quad
u\in[-1/100,1/100],\quad 0\le\lambda\le7687/25000.
\]

The original BN/p38 contract is included unchanged and pinned. In
particular, the actual sign-conditioned centered variables have

\[
-A_0\le U_0\le a_0,\quad -a_1\le U_1\le A_1,
\quad A_0=82453/125000,\quad A_1=703209/10^6,
\]

\[
0\le a_0\le\min(d,p),\quad0\le a_1\le\min(d,1-p),
\quad d=471533/500000,
\]

and the same original law satisfies
\(\rho\ge11/10\) and
\(b_-\le\beta\le b_+\), with
\(b_-=-15293/500000\), \(b_+=307221/10^6\).
All other original acquired premises remain available; this sufficient
test simply does not use them. It does not certify their acquisition.

Write \(q=1-p\), \(s_i=E U_i^2\), \(x=qs_0\), \(y=ps_1\),
\(v=pq\), and \(\lambda=5(x+y)\). If \(B\) has Bernoulli parameter
\(p\), the raw coordinate is \(Y=B+U_B\), and
\(X=(Y-p)/\sqrt{v+x+y}\). For the actual same conditional marginals,
let \(W_j\) be the sum of \(5-j\) independent copies of \(U_0\) and
\(j\) independent copies of \(U_1\). Then

\[
P\{\textstyle\sum Y_i\le k+u\}
=\sum_{j=0}^{5}{5\choose j}p^jq^{5-j}
 P\{W_j+j-k-u\le0\}.
\]

There are six mixture counts, not six licensed threshold centers. Each
quartic \(P_j\) satisfies \(P_j(z)>1\) on \(z\le0\) and
\(P_j(z)>0\) on \(z\ge0\). Thus its expectation bounds the closed
CDF, including every atom at the threshold.

## A fixed outer polygon for the whole probability cell

The signed second moment is exactly

\[
\beta=\frac{v(q-p)-x+y}{v+x+y}.
\]

Its denominator is positive. Consequently the common pair \((x,y)\)
obeys \(x,y\ge0\), \(x+y\le\Lambda/5\), and

\[
-(1+b_+)x+(1-b_+)y\le v(b_+-(1-2p)),
\]
\[
(1+b_-)x-(1-b_-)y\le v((1-2p)-b_-).
\]

For a fixed closed probability cell, each right-hand side is a cubic.
The maximum of its exact degree-three Bernstein coefficients is an upper
bound throughout the cell. Replacing the two right-hand sides by these
bounds enlarges the domain to one fixed compact rational polygon.
The checker enumerates every pairwise boundary intersection and retains
exactly all intersections satisfying every halfplane. These are all
vertices of this bounded two-dimensional polygon; nonemptiness and at
least three vertices are required. The lower coordinate bounds and the
sum upper bound prove compactness independently of the candidate.

## Common moment reduction

For fixed \((x,y)\), support gives

\[
EU_0^4\le(a_0-A_0)EU_0^3+A_0a_0s_0,
\quad
EU_1^4\le(A_1-a_1)EU_1^3+A_1a_1s_1.
\]

These follow by integrating the nonnegative polynomials
\((U_0+A_0)(a_0-U_0)U_0^2\) and
\((U_1+a_1)(A_1-U_1)U_1^2\).
When \(s_i>0\), put \(\gamma_i=EU_i^3/s_i\). Weighted averaging
by \(U_i^2\) bounds \(\gamma_i\) by the same support endpoints.
If \(s_i=0\), every corresponding centered moment is zero and no
division by \(s_i\) is used.

After summing all six weighted quartic expectations, the support upper
bound is affine in each \(\gamma_i\). At the outward endpoint the
linear fourth-moment price is \(A_i^2s_i\), independently of \(a_i\).
At the inward endpoint it is \(a_i^2s_i\); the resulting expression is
a convex quadratic in \(a_i\), because every quartic leading
coefficient and binomial mass is nonnegative. It is therefore enough to
use the nine COMMON pairs

\[
\gamma_0\in\{-A_0,0,\min(d,p_{hi})\},\quad
\gamma_1\in\{A_1,0,-\min(d,1-p_{lo})\}.
\]

These constant inward caps contain every actual inward endpoint in the
cell. The corresponding fourth-moment prices are \(\gamma_i^2s_i\)
at these extremal evaluations only. No assertion that
\(EU_i^4\le\gamma_i^2s_i\) for an arbitrary actual law is made.

Independence gives, with \(t_j=(5-j)x/q+jy/p\),

\[
EW_j^3=(5-j)\gamma_0x/q+j\gamma_1y/p,
\]
\[
EW_j^4=(5-j)EU_0^4+jEU_1^4+3t_j^2
-3((5-j)s_0^2+js_1^2).
\]

Cauchy on the five individual variances implies
\((5-j)s_0^2+js_1^2\ge t_j^2/5\). Thus the retained upper fourth
moment is

\[
(5-j)\gamma_0^2x/q+j\gamma_1^2y/p+(12/5)t_j^2.
\]

For a fixed common gamma pair, the full mixture expectation is convex
in \((x,y)\): its only quadratic terms are nonnegative multiples of
\(t_j^2\). Hence its maximum over the fixed outer polygon occurs at
a vertex. This argument preserves one marginal pair across every count.

## Gaussian target and exact polynomial checks

The normal argument is
\((k+u-5p)/\sqrt{5pq+\lambda}\). On a cell let
\(a=k+u_{lo}-5p_{hi}\). If \(a<0\), use denominator
\(5p_{lo}(1-p_{lo})\); if \(a\ge0\), use denominator
\(5p_{hi}(1-p_{hi})+\Lambda\). In either case the resulting ratio
is a lower bound for the actual normal argument. This sign test uses
the numerator, not the sign of the phase. The lower CDF enclosure plus
\(C_{E,lo}(11/10)/\sqrt{5}_{hi}\) is a sufficient constant target.
The unchanged native Gaussian routine uses rational square-root brackets,
a finite Taylor integral with explicit remainder, and directed integer
rounding; it does not infer rigor from arbitrary precision alone.

For every polygon vertex and common gamma pair, multiply target minus
the six-count expectation by \(v^2=p^2q^2>0\). The denominator-cleared
moments are

\[
v^2 M_0=v^2,\quad v^2 M_1=0,\quad
v^2 M_2=(5-j)xp^2q+jypq^2,
\]

and analogously for \(M_3\) with gamma factors. For \(M_4\), add
the squared term
\((12/5)((5-j)xp+j yq)^2\) to the two gamma-squared linear terms.
Translate each moment by \(j-k-u\) using the binomial formula, and
multiply by the actual mass \({5\choose j}p^jq^{5-j}\).
This is a polynomial of degree at most nine in \(p\), four in \(u\).
The fixed tensor Bernstein transform is recomputed from the thirty
quartic coefficients. Strictly positive coefficients prove a strict
inequality on the whole closed cell. No coefficient table or success
marker is accepted from discovery.

For the global CDF rays, substitute \(z=\pm t/(1-t)\), multiply
by \((1-t)^4\), and check \(P_j-1\) on the negative ray and
\(P_j\) on the positive ray. The pinned exact rational Sturm reader
requires strict endpoints and no root on \([0,1]\), including the
infinite-ray endpoint supplied by the positive leading coefficient.

Every tree split bisects an externally specified p or u interval, and
both closed children are mandatory. Thus the final ten leaves cover the
complete stated rectangle, including all seams. No other phase interval
or threshold center is admitted by this object.

## Evidence and limits

Construction returned zero in 8.562 seconds. A separate stdlib-only exact
replay returned zero in 3.208 seconds, accepting 120 global rays and
18,000 tensor coefficients. This is a fresh replay of the same exact
implementation, not an independent software implementation. Eighteen
mutations reject; 57 independently expanded inverse-transform identities
and 1,080 direct moment/tensor identities pass. Independent mathematical
review is recorded separately by the coordinating agent.

The original full phase domain and the other licensed centers remain
outside this accepted object. Floating discovery failures elsewhere are
not impossibility certificates. No manuscript deletion or page saving is
justified by this partial region alone.
