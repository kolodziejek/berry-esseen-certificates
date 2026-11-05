# Tangent cubic price: a bounded sharp39 success

This additive result supersedes neither the original COUNT proof nor the earlier exact fixed-price obstruction. It changes the lower bound used for the same original C_E normalization, and supplies a necessary additional convexity check.

For 0<w<=W, convexity of f(w)=w^(-3/2) gives its tangent lower bound at W:

    w^(-3/2) >= (5W-3w)/(2W^(5/2)).

Let M=rho*w^(3/2) be the exact common cubic numerator in(6) of GENERAL_N_SOUNDNESS.md. For actual laws M>=0 and 5W-3w>=2W>0. Thus any rational

    0<c<=C_E/(2 sqrt(n) W² sqrt(W))

gives the valid lower price c*M*(5W-3w). A fixed convex blend theta of this price and the original constant rho floor is still a lower bound for C_E*rho/sqrt(n). The target itself has not changed.

For fixed x,y and one conditional support endpoint, the price is affine in the corresponding skew. Its inward-endpoint dependence on the extremal branch is also affine. Therefore the same nine common skew/inward corners remain sufficient: the only quadratic inward term is still the nonnegative quartic-leading moment term. There is no new assumption about the actual fourth moment.

The difficulty is variance convexity. At a fixed p and fixed shared pair gamma0,gamma1, write

    M=M0+r0*x+r1*y, r0=3p-gamma0, r1=3q+gamma1,
    w=v+x+y.

The negative tangent-price contribution to the objective is
-theta*c*(5W-3w)M. Its Hessian is

    3 theta c [[2r0,r0+r1],[r0+r1,2r1]].

The determinant of the displayed inner matrix is -(r0-r1)², so it must **not** be assumed positive semidefinite. Let z_j=((n-j)/q,j/p). The quartic mixture moment bound contributes the Hessian

    H_Q = sum_j 6(1-1/n)b_j Q_(j,4) z_j z_j^T.

For each of the nine shared pairs the exact reader checks that

    H_Q+3 theta c [[2r0,r0+r1],[r0+r1,2r1]]

is positive semidefinite, by its two diagonal entries and determinant. This matrix does not depend on x,y. The already gated concave Gaussian lower function contributes another positive semidefinite Hessian after subtraction, so it may safely be omitted from this sufficient matrix test. Once the test passes, the complete objective is convex on the original outer variance polygon and its maximum is attained at a vertex.

The new fixed-location experiment uses the unaltered sharp39 panel38 contract, p=77/200,k=15,u=0, lambda∈[0,37/200]. The polygon includes the independently derived necessary resource facets(5); it has3 vertices. Original outward supports and inward cap are retained, all40 mixture counts are present, and one shared moment pair is used across them. A floating LP proposed40 quartics and theta, with linear directional-curvature constraints used only for discovery. The exact reader checks all80 global rays by rational Sturm sequences, all9 full rational matrix tests, and all27 vertex/corner scalar score inequalities. It found a strict CDF reserve greater than .00077. The selected candidate is analysis/N39_TANGENT_CANDIDATE.json.

Fresh stdlib-only acceptance is `runs/count_transfer_20261105/later_tangent_exact01/checked/RESULT.json`. Controls independently expand the quadratic mixture objective at rational points and reproduce27 Hessian entries;4 malformed objects reject. A separate exact determinant shows why the PSD requirement cannot be dropped. The zero-noise obstruction for the earlier *constant* price remains true and is preserved.

This is a complete pointwise p/phase comparison over the entire acquired noise scope, not a nonzero-width p/u certificate or a full sharp39 row. The next proof obligation is continuous p/u coverage including a whole-cell PSD license. On a p-cell, after clearing positive denominators the scalar objective has degree at most max(n+4,10); for n39 that remains43. A proposed PSD enclosure must separately check its p-dependent principal minors. The existing nine pointwise matrix checks cannot be cited for a whole p interval.

The new price potentially unifies small- and larger-index normalization treatments; it does not itself remove a manuscript section. Original acquisition, positive39 prerequisite, support, phase domains and all remaining rows remain outside this bounded test.
