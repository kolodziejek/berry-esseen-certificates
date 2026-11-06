# Additive Gaussian Taylor repair of the eleven unresolved BN39 cells

This epoch changes only the Gaussian lower bound at fixed variance-polygon
vertices. It leaves the external BN39 contract, p/noise domain, six-count
common-marginal moment bound, finite Cauchy correction, affine cubic price,
and original C_E/K=0 target unchanged. The completed portable01 remains frozen.

For every repaired cell, the reader checks p_hi<1/2,
a_max=k+u_hi−5p_lo≤0, and a_min²≤15v_min. Thus the actual function
Phi((k+u−5p)/sqrt(5pq+lambda)) is concave in lambda throughout the cell.
The actual upper loss (six-count majorant expectation minus the Gaussian and
fixed affine rho price) is convex in the one shared variance pair. Its
maximum lies at the exact fixed outer beta-polygon vertices, as in the
baseline proof. Only after that reduction is lambda fixed.

At each vertex, the isolated scalar routine constructs a quadratic lower
polynomial in p,u. Its center value is a rigorous lower normal-CDF enclosure;
its gradient intervals use an alternating exponential enclosure and directed
square roots; a uniform Hessian bound controls the entire closed rectangle.
The complete derivative/Taylor proof is in the separately reviewed
later/gaussian_taylor01/SOUNDNESS.md. The four scalar function bodies are copied
unchanged, with only their namespace dependencies routed to the same exact
native normal primitives used by this constructor. Provenance is explicit in
GAUSSIAN_SCALAR_PROVENANCE.json.

Multiplication by (pq)^2 gives degree at most6 in p and2 in u. Hence the
existing (9,4) tensor degree still suffices. One tensor lower bound per polygon
vertex is repeated for the nine COMMON gamma/inward corners in exactly the
same order as the original moment arrays. The affine rho improvement is
unchanged and is combined with the same fixed theta∈[0,1].

The lower Taylor polynomial need not be concave in lambda. No such assertion
is used: convexity is applied to the actual Gaussian before evaluation at a
vertex, and the polynomial only bounds its fixed-lambda value afterward.
There is no tangent cubic price or new variance-Hessian condition in this
n5 repair.

The discovery driver tries exactly the eleven failed cells in one pinned
partial object, without subdivision. A local successful construction is not
whole-row acceptance. A mixed reader must explicitly dispatch retained
baseline leaves to the baseline target and new leaves to this target, verify
every branch of the original full root domain, and freshly check all three
original nearest-count roots before claiming this row complete.
