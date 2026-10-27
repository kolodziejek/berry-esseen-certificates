# Independent review of the combined v6 scalar acquisition

**Recommendation:** accept the recorded calculation as a conditional scalar
acquisition result. No blocking integration defect was found. The first pass
covers all 24 initial rho cells, has `raw<13.281891`, `U<10.796596`, and
`D<3.867530<4`, and satisfies the strict scalar gate for an actual central gap
on every cell. The contact/support and complete Fourier estimates remain
premises. This is not acceptance of `INITIAL42`, `LOCAL42`, a finite base, or
a global theorem.

I independently reviewed the coordinator's `combined_check.py` and phase
argument. I previously authored the v5 first-cover and v6 circle component;
this is an independent check of the **combination and new phase application**,
not a claim of independent authorship review of my own earlier work. C's signed
coefficients were separately reviewed in `signed-independent-review.md`.
The actual-gap implication is reviewed separately by A; this report checks
its input inequalities and exact coverage.

| Item | Mathematical status | Execution status |
|---|---|---|
| Combining the same-law signed cap, quarter constant, circle bounds and corrected curvature | Independently checked coefficient and hypothesis match | Every coefficient reconstructed for 24 cells and 7 passes |
| Phase inequality, formal-coefficient endpoints and all-index reduction | Independently derived from conservation with nonnegative excess/loss/defect | Exact gates checked on every selected polynomial |
| Degree-six resource maxima | Independently certified on their full continuous threshold domains | 336 fresh Bernstein certificates and stationary-bracket checks; no shared checker execution |
| First-pass `D<4` and all actual-gap scalar gates | Verified conditional conclusions | Fresh independent exact check, exit 0 |
| Subsequent high-frequency event, complete initial/local exclusion, global theorem | Separate analytic/computational obligations | Not accepted or run here |

## Exact outcome

The first-pass maxima are

\[
 T_{\max}=66409450799/5000000000=13.2818901598,
\]
\[
 U_{\max}=21593190521/2000000000=10.7965952605,
 \quad d_{\max}=2417205917/625000000=3.8675294672.
\]

For each cell `[l,u]`, the recorded `d` satisfies
`d<(sigma_lower-1)*l`, where `sigma_lower=3.162277660`. The minimum margin is

\[
 57439607663/1600000000000=0.035899754789375>0.
\]

Thus these data meet the separately proved central-gap theorem's sufficient
condition throughout the initial moment range. The recorded squared gap lower
bound `2*(l-d/(sigma_lower-1))` is also positive and reconstructed exactly.
It does not import the more restrictive `D<2` package or its other geometry
hypotheses. After six optional circle updates the largest recorded defect
ceiling is `3.3579256801`. The first-pass conclusion does not require those
updates.

## Conservation and the chosen polynomial's own raw gate

Write `e=exp(-h^2/(2n))`, `h=|H|`, and

\[
 R=U+n(1-e)(c\rho-\phi(0)D/6),\qquad
 U=(n+h^2)a+n\phi(0)D/6+n^{3/2}L,
\]

with `a,D,L>=0`, actual fixed target `c=CE`, and `n>=N=42`.
For any positive `b<=c*rho`, `n*phi(0)*D/6<=U` gives

\[
 R\ge eU+n(1-e)b,\qquad
 U\le nb+e^{h^2/(2n)}(R-nb).
\]

This derivation does not require a small defect or an actual-score upper cap.
The proof in `phase.tex:18–45` then reduces the last expression, for fixed
`h` and raw value `r`, to the finite index `N` and the infinite-index limit.
I checked its derivative: with `x=1/n` and `a0=h^2/2`, the sign is that of

\[
 r-ba_0j(a_0x),\qquad
 j(z)=\int_0^1(1-s)e^{-zs}\,ds.
\]

The function `j` decreases, so the derivative can change only from negative
to positive; an interior maximum cannot occur. The case `h=0` is separate
and immediate. If the infinite-index endpoint `r-bh^2/2` is positive, the
finite endpoint dominates it; otherwise the positive part of the finite
endpoint bounds the nonnegative resource. This justifies the positive part
at `phase.tex:47–70`.

For the chosen polynomial `r(h)=A+f*h-q*h^2`, the check must establish
`A+f^2/(4q)<N*b` **for that polynomial**. Then `r(h)-N*b<0` for every real h,
so the lower Taylor polynomial `exp(z)>=1+z+z^2/2` produces an upper bound
when multiplied by this negative quantity. An unrelated smaller prior raw
ceiling cannot justify that sign. The implementation at
`combined_check.py:51–59` calls the phase verifier before intersecting with
prior raw/resource minima, and `phase_check.py:22–28` checks the polynomial's
own maximum. I separately verified that gate for all 336 endpoint polynomials.
The rejection control with selected polynomial `43-h^2`, `N*b=42`, fails
regardless of any unrelated excellent prior bound.

The physical conservation identity is used only at `c=CE`. At formal
coefficient endpoints the calculation evaluates affine polynomial enclosures;
it does not assert that a physical defect identity holds at another target.
The constant, linear, curvature and `b=c*l` terms are affine in the formal c
when all previously acquired moment bounds are held fixed. The corrected
curvature is the maximum of two affine expressions with the same slope l,
so it remains affine. Thus the raw and phase polynomials are affine before
threshold maximization, and the two endpoints of the interval enclosing CE
suffice. The strict raw gate holds throughout that interval because its
supremum over h, minus `N*b`, is convex and negative at both endpoints.

## Independent polynomial acceptance, not a repeated producer run

My checker imports none of `combined_check.py`, `phase_check.py`,
`signed-check.py`, `moment_check.py`, or the Fourier kernels. It expands

\[
 P(h)=r(h)+(r(h)-Nb)\{h^2/(2N)+h^4/(8N^2)\}
\]

by polynomial convolution and compares every coefficient with the recorded
one. It verifies that the recorded threshold cap lies beyond the nonnegative
raw region by `r(cap)<=0` and `r'(cap)<0`; concavity of r then excludes the
whole exterior ray for a nonnegative conserved raw quantity.

Instead of rerunning the producer's concavity scalar test and bisection, the
review check converts `-P''` to the Bernstein basis on `[0,cap]`. In every
one of the 336 cases, **all coefficients are strictly positive on the entire
interval**, with no subdivision needed. This proves strict concavity there.
The recorded derivative signs bracket its unique maximum. A second Bernstein
conversion on that narrow stationary interval supplies an independent upper
bound for P, and this bound is no larger than the recorded resource ceiling.
The endpoint values and the infinite-index quadratic maximum are checked too.

The transform used is explicit: after `h=l+(u-l)s`, the power coefficient is
`alpha_j=(u-l)^j*sum_{k>=j}p_k*binom(k,j)*l^(k-j)`, and the degree-n Bernstein
coefficient is `sum_{j<=i}alpha_j*binom(i,j)/binom(n,j)`. Nonnegative Bernstein
basis functions sum to one on the closed unit interval. This establishes
continuous coverage; these are not sampled polynomial values.

## Coefficients, ordering and source scope

For every row and pass, I reconstructed the new quarter constant from the
pinned initial moment/gap data, took the independently reviewed signed K1 cap,
and rebuilt both formal endpoint polynomials. In later passes the previous
raw ceiling alone supplies the density floor; the previous defect supplies
the same-law gamma constraint. Raw and resource ceilings are then computed
separately, rounded upward, and intersected with their own prior values.
Only the resource supplies the new `D` and weighted `nD` bounds. No new defect
is used to prove itself, no resource replaces a raw license, and no threshold
or sign class is discarded.

All 24 indices and both endpoints of every cell match the fixed partition
`[1+3361i/96000,1+3361(i+1)/96000]`, `0<=i<24`. Each row has exactly one
initial pass plus six updates. No smaller support radius, actual-score cap,
new Fourier norm, or later-stage local hypothesis is silently substituted.
The inherited low/high Fourier values and Gamma are explicit input premises;
reading their pinned values does not independently prove their analytic
validity. The coordinator's fresh run recomputed them through the first-cover
constructor, while this independent reviewer intentionally avoided a repeat
of that shared implementation.

The combination's code snapshot is SHA256
`f22a0506d8301fb5c747650443980363b6bc06b47ce8fa6c35fb7eab0bc19d18`.
Its `combined01/stdout.json` is
`200cc178bed6400f4a6043aac7f136e38a5cfa02a390c4d3a02971caf5c78dca`.
The exact phase proof/checker, signed table/checker, circle checker and retained
v5 input hashes are bound in `combined_review_check.py` and copied into the
review output. The combined output's own source hashes agree with the files
read. This is a review of that fixed invocation, not a generic external receipt
acceptance API.

## Fresh evidence and limits

Command actually run from this separate worktree:

```sh
python3 mathematics/fixed-target-v6/2026-10-27/combined_review_check.py ../strategy-v4
```

The recorded run is `runs/fixed-target-v6-20261027/combined-review01/`.
It returned zero with Python 3.9.6 and optimization 0; exact stdout, empty
stderr, timestamps, command, script and output hashes are preserved.
Six controls reject a missing cell, altered signed coefficient, changed phase
polynomial, understated resource, false gap margin, and unlicensed selected
polynomial. The check reconstructs the first-pass scalar targets independently
of the producer's summary fields.

No dense/native program was executed, no certificate changed, and no dependency
was deleted. The supported result is a compact conditional initial scalar
acquisition and positive gap gate. A new high-frequency use of that gap must
apply its own complete event theorem and all frequency-piece gates; a local
exclusion still requires its full hypotheses and numerical predicates.
