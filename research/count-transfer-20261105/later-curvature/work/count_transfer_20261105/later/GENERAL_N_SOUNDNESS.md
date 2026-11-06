# A general n+1 conditional-count quartic criterion

This is a self-contained extension of the fixed five-summand mechanism, not an assertion that a later complete row has been checked. The original same-law acquisition remains an input. The fresh n6 result below fixes both probability and phase. The sharp39 obstruction is to one explicitly named normalization gate only.

## One law and the exact score

Let X have mean0, variance1 and finite third absolute moment rho. Put p=P(X>0), q=1-p, v=pq and m=E X_+=E X_->0. With h=v/m and Y=p+hX, write Y=B+U, B=1{X>0}. Both U conditional on B=0 and U conditional on B=1 are centered. Zero atoms are in class0. Write their variances as s0,s1, their third moments as mu0,mu1, x=q*s0,y=p*s1, s=x+y and w=v+s=h². For the raw standardized-X sum threshold H, let

    z=np+hH=k+u.

The actual iid conditional-count identity is

    P(sum X_i <= H)=sum_(j=0)^n b_j P(W_j+j-k-u <= 0),
    b_j=binom(n,j)p^j q^(n-j),

where W_j sums n-j independent class0 residuals and j independent class1 residuals. The same two conditional laws occur in every j. All j=0,...,n are retained even when the threshold's nearest count k has a much smaller licensed range.

The Gaussian coordinate is (k+u-np)/sqrt(nw). In particular a certificate for target T>0 must prove

    sum b_j E Q_j(W_j+j-k-u)
      < Phi((k+u-np)/sqrt(nw)) + T*rho/sqrt(n),             (1)

with Q_j(t)>=1 for t<=0 and Q_j(t)>=0 for t>0. These are global inequalities, not inequalities only on a sampled support. Their shared boundary at0 includes atoms on the closed event. A negative CDF deviation is treated by the separately acquired reflected orientation; reflection turns a complementary closed event into an open event. No reflection of a signed contract is silently inferred.

For each quartic we require a strictly positive leading coefficient. Multiplying Q_j(-t/(1-t))-1 and Q_j(t/(1-t)) by (1-t)^4 gives two polynomials on [0,1]. Strict positivity of both compactified polynomials is sufficient for the two global inequalities. The inherited exact Sturm reader checks strict endpoints, a squarefree polynomial and zero interior root count. Its conservative rejection of other cases cannot create a false positive.

## A common nine-corner moment rule

Assume U0 in[-A0,a0] and U1 in[-a1,A1], with fixed positive outward caps and 0<=ai<=ri. These must be acquired for the same law. For centered Z in[-L,R], variance s, integrating Z²(Z+L)(R-Z)>=0 gives

    E Z^4 <= (R-L)E Z³+LRs.

If s>0, gamma=E Z³/s belongs to[-L,R], since E[Z² Z]/E Z² is an average of support points. If s=0 then Z=0 and all its terms vanish; no division is needed.

Fix x,y,p,u and all Q_j. The sum in(1) minus an affine function of mu0,mu1 is affine in each gamma at fixed inward endpoint after the fourth-moment upper bound. The coefficient of each fourth moment is nonnegative because b_j>=0 and Q_j has positive leading coefficient. For class0 its maximum is therefore at gamma0=-A0 or gamma0=a0. The former endpoint has fourth coefficient A0² independently of a0; the latter gives a0². The resulting expression on the latter branch is convex in a0, so a0=0 or r0 suffices. Class1 gives the analogous alternatives. Consequently nine common pairs suffice:

    gamma0 in{-A0,0,r0}, gamma1 in{A1,0,-r1}.              (2)

At these extremal evaluations the individual fourth-moment terms are gamma_i²*s_i. This is **not** the actual-law assertion E U_i^4<=gamma_i²*s_i. The nine pairs maximize an upper expression after successive convexity steps. One pair is shared across every conditional count and the normalization charge.

Let t_j=(n-j)x/q+j*y/p. The exact fourth moment of W_j is

    (n-j)E U0^4+j E U1^4
      +3[t_j²-(n-j)s0²-j*s1²].

Cauchy's inequality on the n individual variances gives

    (n-j)s0²+j*s1² >= t_j²/n.

Thus the upper fourth moment used at(2) is

    (n-j)gamma0²*x/q+j*gamma1²*y/p+3(1-1/n)t_j².         (3)

The other moments are E W_j=0, E W_j²=t_j and E W_j³=(n-j)gamma0*x/q+j*gamma1*y/p. Translation by j-k-u uses the exact binomial expansion. For fixed (2), the complete mixture expression is convex in(x,y): its only quadratic terms are nonnegative multiples of t_j². Keeping the exact negative diagonal correction instead of the Cauchy relaxation would not in general preserve this convexity.

## Necessary variance polygons, without substituting the noise intercept

Every actual x,y is nonnegative and x+y<=lambda_max/n. If a beta interval is actually acquired, the identity

    beta=[v(1-2p)-x+y]/[v+x+y]

gives the two halfplanes

    -(1+beta_u)x+(1-beta_u)y <= v(beta_u-1+2p),
      (1+beta_l)x-(1-beta_l)y <= v(1-2p-beta_l).           (4)

At fixed p these are rational. On a p-cell, taking rational cubic Bernstein upper bounds on their right sides supplies one outer polygon containing all actual variances. Missing beta data cannot be invented; sharp39 may use only the nonnegative noise triangle or independently proved facets.

There are useful additional facets from original joint resources. Support implies a0>=s0/A0 and a1>=s1/A1. Thus, if d=a0+a1 and the original acquired inequalities are

    d/d0+lambda/Lambda<=1,
    binary_charge+gap_charge*d+noise_charge*lambda<=D,

then, at fixed p,

    x/(q*A0)+y/(p*A1)+(n*d0/Lambda)(x+y)<=d0,
    gap_charge*x/(q*A0)+gap_charge*y/(p*A1)
        +n*noise_charge*(x+y)<=D-binary_charge.           (5)

Both follow by replacing d by a necessary lower bound. The independently smaller noise cap does not replace Lambda in(5). On p-cells, use smaller coefficients 1/(q_max*A0),1/(p_max*A1) to obtain an outer polygon. This is the same inward-noise price used in the large-index direct method, here retained as linear common-variance constraints.

## Cubic normalization and the Gaussian term

The exact identity is

    M:=rho*w^(3/2)=v(1-2v)+3p*x+3q*y-gamma0*x+gamma1*y. (6)

It follows by expanding q E(p-U0)^3+p E(q+U1)^3; the signs follow from the original sign-conditioned supports. For actual laws M>=0. Choose a rigorous lower constant c<=T/(sqrt(n)*w^(3/2)) throughout the cell and a rho floor r_l. Then both cM and T*r_l/sqrt(n) are lower bounds for the normalization term in(1). Any fixed blend theta in[0,1] remains a lower bound. Subtracting theta*cM preserves the affine gamma and convex variance steps above. At nonrealizable corners M need not be nonnegative; the affine extension remains part of the upper objective, not a new law assertion.

One may use a constant Gaussian lower bound. Alternatively at fixed p and a=k+u-np<=0, write D=npq+lambda. Direct differentiation gives

    d²/dlambda² Phi(a/sqrt(D))
       = a*phi(a/sqrt(D))*(3-a²/D)/(4*D^(5/2)).

If a²<=3npq, this is nonpositive for all lambda>=0. Hence subtracting the Gaussian is convex in(x,y), and the exact vertex-specific Gaussian lower enclosure may be used in(1). A rational lower enclosure at each vertex still yields a valid upper bound on the convex objective there. This is the correlated Gaussian rule used by the bounded pilot. No global concavity outside its sign/range gates is asserted.

At a fixed p/phase, maximizing over the compact variance polygon now reduces to its complete vertex set and the nine common pairs(2). Segments/points are valid mathematically but need explicit program handling; the current pilot only encounters polygons with at least3 vertices.

For a whole p/u cell, use fixed outer support and inward endpoints and a fixed polygon. After multiplying by v²>0, each translated expectation has bidegree at most(n+4,4): the binomial mass has degree n, the cleared zeroth moment degree4, the cleared linear variance terms degree3, and the squared-variance terms degree2. The cubic charge contributes degree8 after clearing, so a general statement uses degree max(n+4,8); this is n+4 for all indices considered here. An exact tensor Bernstein proof can therefore certify a whole cell. The n5 degree9 array must not be reused at n6(degree10) or n39(degree43).

## Fresh bounded result and exact limitation

The original n6.BN.p38 contract, at p=77/200,k=2,u=0, admits a seven-quartic exact certificate using the whole pointwise mean-licensed noise range

    0<=lambda<=21021472160667/81845776820000.

Every law satisfying the original row at this p has lambda in this range, by m>=447797/10^6 and lambda=6(v²/m²-v). The original uniform cap33259/125000 is not the intercept in the joint resource. The polygon has5 vertices; all45 common moment evaluations and14 global rays passed, with strict CDF reserve greater than .00599. The no-extra-resource-facet object is selected, so the result does not depend on(5). Fresh stdlib-only readback is `runs/count_transfer_20261105/later_exact_n6_01/checked/RESULT.json`.

At sharp39,p=77/200,k=15,u=0, the current full-noise constant c uses lambda_max=.185. Its zero-noise polygon vertex already makes the strongest permitted blend target minus the exact binomial CDF negative, less than-.0012217. In contrast, the exact Bernoulli normalization has positive margin greater than .0008592. At zero noise W_j=0, so every global CDF majorant has mixture expectation at least the exact binomial CDF. Therefore **no choice of quartics can pass this particular fixed-price gate on that whole noise interval**. Higher moments or facets that retain the zero-noise vertex cannot repair it. The exact inequality is checked in `later_controls01/checked/RESULT.json`. It is not an obstruction to the sharp39 theorem, the original COUNT proof, noise subdivision, or a stronger normalization.

Next test: split sharp39 noise into closed slabs (with a separately correct zero-width deterministic endpoint if needed), use the appropriate smaller upper w in each slab's price, and derive the p/u tensor rule at degree43. The next n6 test is a nonzero-width p/u rectangle around this fixed location, with the original three threshold roots eventually covered. Neither full-row task has been performed here.
