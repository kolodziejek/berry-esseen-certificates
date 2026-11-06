# Gaussian Taylor lower polynomial and the broad sharp39 rectangle

This additive epoch proves the original sharp39 panel38 positive closed-score implication on

    n=39, k=15,
    p∈[3847/10000,39/100], u∈[-1/1000,1/1000],
    0<=lambda<=37/200.

The original same-law acquisition remains a premise. There is one whole p/phase cell, using the **same forty quartics and price blend as the earlier fixed-point object**. No new optimization or numerical discovery was run. This is not the entire original p/phase row: the lower-p region, most phases and the other nearest-count roots remain outside this test.

The moment, tangent-price, variance-polygon and PSD arguments are unchanged from ../GENERAL_N_SOUNDNESS.md, ../TANGENT_PRICE.md and ../CONTINUOUS_RECTANGLE.md. Here a quadratic lower polynomial replaces the coarse constant Gaussian endpoint. It is applied only after reduction to the exact variance vertices; it need not be concave as a function of lambda.

## Derivation of the Gaussian polynomial

Fix a polygon vertex and therefore a nonnegative lambda. Write t=k+u,
D=np(1-p)+lambda, a=t-np and z=a/sqrt(D). On the closed p/u rectangle,

    z_t=D^(-1/2),  z_tt=0,
    z_p=-n D^(-1/2)-a D'/(2D^(3/2)),
    z_pt=-D'/(2D^(3/2)),
    z_pp=n(D'+a)/D^(3/2)+3a(D')²/(4D^(5/2)),
    D'=n(1-2p).

These follow by differentiation with t fixed; p and the standardized raw threshold H are not conflated. For G=Phi(z),

    G_ij=phi(z)[z_ij-z z_i z_j].

The verified universal bound phi(z)<=phi(0)<2/5 therefore implies
|G_ij|<=(2/5)(|z_ij|+|z||z_i||z_j|).

Let l,h be the p endpoints, u_l,u_h the phase endpoints, D_min=n l(1-l)+lambda,
A=max|k+u-np| at the four corners, B=n max(|1-2l|,|1-2h|), and choose a positive
rational s_min<=sqrt(D_min). Since this whole cell lies below1/2, D>=D_min.
Valid rational derivative bounds are

    Z=A/s_min, Zt=1/s_min,
    Zp=n/s_min+A B/(2D_min s_min),
    Zpp=n(B+A)/(D_min s_min)+3A B²/(4D_min² s_min),
    Zpt=B/(2D_min s_min).

Choose outward-rounded rational

    Mpp >=(2/5)(Z Zp²+Zpp),
    Mpt >=(2/5)(Z Zp Zt+Zpt),
    Mtt >=(2/5)Z Zt².

These bound the Hessian on the *entire* rectangle, not just at evaluated grid points.

At its center (p_c,u_c), a_c²/(2D_c)<=1 is checked exactly. The even degree24 and odd degree25 alternating partial sums enclose exp(-a_c²/(2D_c)), since the term magnitudes decrease on[0,1]. Together with the existing exact phi(0) and square-root enclosures, this gives rigorous intervals for the two center derivatives. Let g_p,g_t be their rational midpoints and epsilon_p,epsilon_t their halfwidths. The existing exact Gaussian routine gives G_c^lo<=G(p_c,u_c). Set Delta_p=(h-l)/2, Delta_t=(u_h-u_l)/2 and eta=Delta_t/Delta_p>0.

The integral Taylor remainder and 2|delta_p delta_t|<=eta delta_p²+eta^(-1)delta_t² imply the lower polynomial

    G_c^lo+g_p delta_p+g_t delta_t
      -epsilon_p Delta_p-epsilon_t Delta_t
      -1/2[(Mpp+eta Mpt)delta_p²+(Mtt+Mpt/eta)delta_t²]. (T)

The center CDF value is already a lower bound, so no missing center-error subtraction is assumed. Rounding of derivatives and Hessian bounds is explicitly directed. Formula(T) is then expanded in p,u with exact rational arithmetic.

## Why the original variance vertex reduction still applies

Throughout the chosen wider cell, k+u-np<0: its maximum is15.001-39*.3847=-.0023. Its squared magnitude is at most3n p_min(1-p_min). The **actual** Gaussian is therefore concave in lambda for every fixed p,u, by the prior derivative proof. With the exact tangent-price PSD tests, the full objective is convex in the variance pair. It suffices to bound it at each vertex. At a vertex lambda is fixed, and(T) is a valid whole-p/u lower bound for the Gaussian there. Replacing these vertex values by lower bounds preserves the desired upper score estimate. No concavity of(T) in lambda is needed or asserted.

The original variance polygon is enlarged with the same safe whole-cell coefficients 1/(q_max A0) and1/(p_max A1). Its three vertices are reconstructed exactly. At all nine shared skew/inward corners the reader checks the degree41 diagonal and degree82 determinant Bernstein coefficients of the cleared Hessian over the whole wider p interval. The Gaussian quadratic adds at most degree6 after multiplication by(pq)², so the score remains degree(43,4). All its tensor Bernstein coefficients are strictly positive. The eighty global ray checks are also executed again.

## Actual result and limits

The fresh source-bound exact check returned0 in5.947907624999061 seconds at
`runs/count_transfer_20261105/later_gaussian_broad01/`.
It checked80 global rays,5,940 whole-cell score coefficients and1,503 PSD coefficients.
The source/object closure is bound before and after execution. The broad p width .0053 is26.5 times that of the prior .0002 rectangle, and it now needs one cell rather than four; these are bounded test comparisons, not a forecast of complete-row cost or manuscript page savings.

Separate controls check rigorous Gaussian lower enclosures, exact centered polynomial expansion and independently derived inverse-square-root two-jets at105 rational points, and reject four invalid scalar domains. The grid checks are implementation tests, not the continuous proof. The continuous conclusion comes from the displayed analytic derivative bounds and exact complete polynomial certificates.

The lower part of the original p interval has positive raw-threshold cases. There the simple Gaussian concavity-in-noise premise can fail. This result does not cross that boundary. A general row extension needs a separately proved mixed-sign normalization/curvature rule or a suitable closed split; it must also cover the much larger phase interval and other nearest-count regions. No such campaign was run here.
