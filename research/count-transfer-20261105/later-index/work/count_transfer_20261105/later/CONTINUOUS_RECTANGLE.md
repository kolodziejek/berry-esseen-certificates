# Exact sharp39 probability/phase rectangle

The source-bound sharp39 panel38 hypotheses imply the positive closed-score inequality at C_E whenever

    n=39, k=15,
    3849/10000 <= p <= 3851/10000,
    -1/1000 <= u <= 1/1000,
    0 <= lambda <= 37/200.

All other original row hypotheses remain in force. This is a small subrectangle of the selected p∈[.38,.39] row and one of its three licensed nearest-count roots. It is not the entire row, a new sharp39 theorem, or an acquisition replay. Both phase signs, zero noise and threshold atoms are included.

The actual original source, its schema and same-law acquisition join are listed in README.md and the source-bound DOMAIN.json. The forty quartics and common price blend are **unchanged from the fixed-point tangent pilot**. The new result is a continuous verification epoch, with a new full-domain reader and actual captures; it does not upgrade the old pointwise receipt by relabeling it.

## The new continuous obligations

Partition the probability interval into four closed equal strips of width1/20000. Retain the whole phase interval on every strip. The shared boundaries are included by both neighboring strips, so this covers the entire rectangle with no interior gap.

On a strip [l,h], use the fixed outer variance polygon

    x>=0, y>=0, x+y<=Lambda/39,
    [1/((1-l)A0)+39d0/Lambda]x
       +[1/(hA1)+39d0/Lambda]y <= d0,
    [g/((1-l)A0)+39e]x+[g/(hA1)+39e]y <= D-b.

Here the immutable row supplies A0=A1=471/1000, d0=233/10000,
Lambda=37/200, D=143/500, b=41/2000, g=2857/250 and e=2879/2000.
The smaller coefficients 1/(1-l) and1/h enlarge the necessary inequalities(5), so every actual variance pair at every p in the strip belongs to this polygon. All its vertices are computed exactly by pairwise line intersections and simultaneous satisfaction of every halfplane. The selected polygons have3 vertices each. This enlargement does not change the original noise intercept.

The inward caps a0,a1<=d0 are constant on these strips and are smaller than both p and q throughout. No pointwise endpoint is silently substituted into a whole-cell bound. The same nine common skew pairs are used as in GENERAL_N_SOUNDNESS.md.

For a fixed lambda>=0 and threshold coordinate t, differentiation gives

    d/dp [(t-np)/sqrt(npq+lambda)]
      = -n[np+t(1-2p)+2lambda]/[2(npq+lambda)^(3/2)].

If 0<=t<=n, the bracket is positive: when p<=1/2 its minimum over t is np, and when p>=1/2 it is nq. The normal CDF is therefore decreasing in p and increasing in t. On the entire strip/phase cell it is bounded below by

    G(lambda)=Phi((15-1/1000-39h)/sqrt(39h(1-h)+lambda)).

The numerator is negative, and its square is at most3*39*l(1-l), as checked exactly. In particular it is at most3*39*h(1-h). The curvature calculation in GENERAL_N_SOUNDNESS.md proves G concave throughout lambda>=0. Consequently -G(39(x+y)) is convex in(x,y). Its rigorous value at each polygon vertex is computed by the exact Gaussian enclosure, not by sampled numerical integration.

Put W=h(1-h)+Lambda/39 and choose the downward rational tangent-price coefficient c specified in TANGENT_PRICE.md. Actual w<=W, so the lower price remains valid on the entire strip. The proof of the nine skew/inward corners remains unchanged.

## Whole-cell expectation and convexity certificates

For each fixed vertex and corner, the reader constructs the **entire** translated forty-count quartic expectation as a polynomial in p,u after multiplication by v²=(pq)². It subtracts this from the rigorous Gaussian-plus-blended-cubic-price lower target. The resulting polynomial has bidegree at most(43,4). All220 tensor Bernstein coefficients are strictly positive on the strip/phase cell. The transform is reconstructed from exact power coefficients, not supplied by the discovery object.

Variance convexity must also hold for every p in the strip. For the quadratic objective excluding the favorable -G term, multiply the Hessian by v²>0. Its entries are

    A(p)=sum_j 6(38/39)b_j Q_(j,4)(39-j)²p²
                          +6theta*c*r0(p)*v²,
    B(p)=sum_j 6(38/39)b_j Q_(j,4)j(39-j)pq
                          +3theta*c*(r0(p)+r1(p))*v²,
    E(p)=sum_j 6(38/39)b_j Q_(j,4)j²q²
                          +6theta*c*r1(p)*v²,

with r0(p)=3p-gamma0 and r1(p)=3q+gamma1. These have degree at most41. The exact reader verifies nonnegative Bernstein coefficients for A,E and A*E-B² (degree at most82) on the entire p strip, for all nine common corners. Thus the full quadratic objective is convex in(x,y) for every p,u; its Hessian is independent of u. Adding the convex -G term preserves convexity. The maximum occurs at a polygon vertex, precisely the vertices used in the score tests. No fixed-point PSD check is being reused as a uniform one.

The original eighty strict compactified-ray Sturm checks are executed again on the unchanged forty quartics. They guarantee global CDF majorants and include the threshold atom at0. Together with the common-law moment proof, the vertex reduction, and the four closed strips, the new exact computations establish the stated rectangle implication.

## Execution, controls and limits

Selected public entry:

```sh
python3 -I -B -S analysis/accept_rectangle.py \
  analysis/N39_TANGENT_CANDIDATE.json /absolute/NEW_OUTPUT
```

The wrapper verifies the exact source/contract/object closure before and after invoking the unchanged full rectangle kernel. It strictly rejects bool/int/float coefficient encodings and noncanonical rational strings. The old pointwise kernels and their true historical captures are preserved; their selected objects were canonical, so the additional format guard does not change their mathematics.

The fresh source-bound full continuous capture is `runs/count_transfer_20261105/later_rectangle02/`: actual returncode0,24.701422500016633 seconds. The complete result and SOURCE_BINDING.json are in checked/. It verifies80 global rays,23,760 score coefficients and6,012 PSD coefficients across four strips. The first arithmetic capture later_rectangle01 is preserved separately. No old acquisition or whole finite-base campaign was rerun.

The independent control script reconstructs167 Bernstein power coefficients by inverse expansion, checks27 exact translated-mixture evaluations, and rejects10 malformed or ambiguous objects. Controls are at later_rectangle_controls01/checked/RESULT.json. These bounded checks audit the implementation; the algebra above proves the continuous implications.

A single unsplit use of the p_hi/u_lo Gaussian lower endpoint is too coarse: at p=.3849,u=0,lambda=0, even the larger of its two price branches plus that Gaussian lower value is strictly below the exact binomial CDF. The exact negative rational is preserved in the controls. Four probability strips repair this enclosure loss without changing the target or the forty quartics.

No other p/phase cell, nearest-count region or source row follows automatically. A general continuation needs complete source-bound closed covers and per-cell PSD licenses, not just the present local success.
