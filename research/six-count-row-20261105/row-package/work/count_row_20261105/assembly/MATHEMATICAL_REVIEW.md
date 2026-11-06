# Independent review of V3 and additive V4 scope

This review concerns the exact six-count expectation criterion and its whole-row assembly. It does not prove acquisition or admit an unfinished numerical tree. V3 full-root candidates remained partial; V4 is the separately pinned selected reader epoch. The original V3 wrapper/source manifest are retained as an unexecuted predecessor protocol.

## Fixed-domain and moment interfaces

The original n5 BN/p38 contract and domain projection are unchanged. The probability interval is [19/50,39/100], full acquired noise interval [0,7687/25000], beta interval [−15293/500000,307221/1000000], rho lower11/10, and fixed target K=0. Exact original raw-threshold bounds imply nearest k=1,2,3. Every conditional mixture still includes j=0,…,5 and the same two actual conditional laws. The independently derived proof is `../domain/SOUNDNESS.md`, with all source pins in `../domain/domain.json`.

The quartics are fixed on each closed p/u leaf, have positive fourth coefficient and majorize the closed count CDF on both whole rays. The native reader reconstructs these global targets and applies the exact strict Sturm reader. Its conservative rejection of zero endpoints or repeated roots cannot create acceptance. The six polynomials may differ by count; their expectation must use one shared moment tuple.

For actual x=q Var(U0), y=p Var(U1), the support fourth-moment bounds and Cauchy's finite-n correction give the earlier nine shared skew/inward evaluations. At such an evaluation, the quartic expectation has the form affine(x,y)+nonnegative multiples of t_j², t_j=(5−j)x/q+jy/p. This is a convex extension of an upper expectation bound. It is not a claim that the actual fourth moment is at most gamma² times variance. Zero variance contributes zero without division.

The beta halfplanes and noise slab define a fixed rational outer polygon for each p cell. Its right-hand cubic maxima are bounded by exact degree3 Bernstein coefficients. All vertices are retained. The native criterion rejects rather than accepts a degenerate or unproved empty polygon.

## V3: correlated Gaussian and the same-law absolute cube

Let a=k+u−np and D=npq+lambda. For fixed p,u,

    g(lambda)=Phi(a/sqrt(D)),
    g''(lambda)=a*phi(a/sqrt(D))/(4 D^(5/2))*(3−a²/D).

The native guard uses a_max=k+u_hi−n*p_lo≤0 and a_min²≤3n*p_lo*(1−p_lo). These imply a≤0 and a²≤3npq throughout the whole leaf. Therefore g is concave throughout the noise interval. The quartic upper expectation minus g is convex in x,y. At a polygon vertex, replacing g by a directed lower bound with numerator a_min and denominator n*p_lo*(1−p_lo)+n(x+y) is valid for the whole p/u leaf. When the guard fails, the reader uses a constant lower Gaussian bound on the entire leaf instead. For negative a_min it uses the lower denominator; for nonnegative a_min it uses the upper denominator. Phase sign is not substituted for numerator sign.

The additional exact absolute-cube numerator is

    M=E|Y−p|³ = v(1−2v)+3p*x+3q*y−gamma0*x+gamma1*y,
    rho=M/w^(3/2),   w=v+x+y.

For actual laws M≥0. With a positive outward upper w_max and positive lower C_E enclosure, the reader chooses

    c=C_E,lo/(sqrt(n)_hi * w_max * sqrt(w_max)_hi),
    f=C_E,lo*rho_lower/sqrt(n)_hi.

Both cM and f are lower bounds on C_E*rho/sqrt(n) for the actual law. Hence, for any *fixed leaf coefficient* theta∈[0,1],

    (1−theta)f + theta*cM ≤ C_E*rho/sqrt(n).

The complete deficit tested is Gaussian + this price − quartic upper expectation. Equivalently, maximize expectation minus Gaussian minus this price. The new M term is affine in each gamma_i and in x,y. It leaves the previous skew endpoint reduction valid, leaves the inward objective convex (its added dependence is only linear), and leaves the x,y objective convex. The same nine shared moment pairs and every fixed polygon vertex therefore suffice. If M is negative at a relaxed, unrealizable corner, the test simply becomes harder; no sign assumption on M at the artificial corners is used in the proof.

After multiplication by positive p²q², the cube-price term has degree at most8 in p. The original expectation degree bounds remain(9,4). The vertex Gaussian value is a fixed rational lower bound, not a p-dependent nonpolynomial substituted into a Bernstein transform.

The native exact CLI calls `m.admit` without the optional precomputed `rows` argument. It therefore reconstructs all moment targets. Discovery's cached matrices and success flags are not acceptance authorities.

## V4: additional original mean and inner-endpoint restrictions

No new law assumptions are introduced. The original row already supplies m≥m_lo and positive physical inner endpoint bounds A_neg,B_pos. Independently,

    sqrt(w)=v/m,    lambda/n=v²/m²−v.

The derivative of v²/m_lo²−v is2v/m_lo²−1. The native guard2p_lo(1−p_lo)>m_lo² is sufficient to make it positive across this p cell (which lies below1/2). Thus the exact mean cap at p_hi bounds every actual lambda on the cell. Intersecting it with the declared noise upper endpoint retains all actual points. The reader's rejection when this intersection cannot provide a nondegenerate polygon is not an empty-domain proof.

For an actual negative support point, X≤−A_neg gives U0≤p−A_neg*sqrt(w); the positive support bound gives −U1≤q−B_pos*sqrt(w). Consequently, with r a directed lower square root of p_lo(1−p_lo)+noise_lo/n,

    a0≤min(d, p_hi−A_neg*r),
    a1≤min(d, 1−p_lo−B_pos*r).

These are fixed rational upper endpoints for that leaf. Using them in the shared moment-corner argument retains its quantifiers and polynomial degree. The new w_max uses the proved mean/noise intersection consistently in the cubic denominator and noncorrelated Gaussian bound. These changes agree with `model_v4.py`; the V4 acceptance tree code differs from V3 only by the model/schema/source-epoch names.

No defect was found in this bounded derivation/source comparison. Original acquired support, sign, rho, beta, mean and threshold licenses remain necessary premises. This statement does not assert a fresh full-row score acceptance.

## Whole-row assembly contract

`complete_v4.py` fixes all of p, full noise, contract hash, original domain hash and seven-file exact reader closure externally to the candidate. It permits only these complete roots, or the explicitly larger full phase intervals for k1/k3:

- k1: [−222258117249/10^12,1/2];
- k2: [−1/2,1/2];
- k3: [−1/2,72258117249/10^12].

No count can be missing, duplicated or substituted. Selection order is immaterial and is normalized by k. The selector merely prepares a source/object inventory and does not accept a tree.

For each root the wrapper stages exact candidate bytes, launches the unchanged native CLI in a fresh unoptimized isolated interpreter, saves actual exit and full streams, and checks the complete result against stdout, object bytes, exact source closure and fixed p/u/noise declaration. Each child is an actual arithmetic execution; a stored RESULT or construction status is ignored. Original sources, selector, wrapper and objects are rehashed before/after. A partial tree fails in the native reader. Nonzero actual exit cannot create the final RESULT.

Only after all three actual returns are zero does the wrapper issue
`PASS_FRESH_COMPLETE_ORIGINAL_N5_BN38_ROW_COMPARISON_V4`.
That conclusion is a conditional positive closed-score implication for this one complete original acquired row. It does not establish the original acquisition, all probability panels, reflected row, n5 as a whole, or the full Berry–Esseen theorem.

The bounded controls deliberately use incomplete synthetic leaves; they are not score witnesses. They verify21 rejection conditions, including a real fresh native rejection despite a neighboring fake success artifact, and a real optimized-Python rejection. No live candidate or source was changed.
