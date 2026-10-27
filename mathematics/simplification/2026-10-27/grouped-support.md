# A 14-interval replacement for the zero-loss support arithmetic

This strengthens the alternative support-lift proof in `zero-loss-support.md`.
For the **new zero-loss theorem only**, the old finite42–48 polynomial sign
predicates can be replaced by 672 exact Bernstein coefficients on 14 single
intervals and 14 whole-ray checks. Every coefficient is strictly greater than
1/4. The initial support radius3.84 and all64 LEFT contraction radii are
unchanged. This is a new certificate, not a change to any old acceptance target.

| Result | Mathematical status | Execution status |
|---|---|---|
| Polynomial signs for all65 support calls, for every n>=42 at zero predecessor loss | Locally derived exact finite certificate, conditional on the analytic fifth-order contact envelope | Fresh PASS:672 coefficients,84 ray signs,14 closed intervals,9 rejection controls |
| Each support radius for an actual maximizing law | Conditional on retained attainment/contact/heat analysis and previously acquired moment ceilings | No native resource/acquisition program run |
| Uniform LOCAL42 or the sharp conjecture | Requires the other acquisition/comparison premises and a genuine sharp finite base | Not accepted by this checker |

## Fixed objects and source binding

Use N=42, c=819/2000, ell=6403124237432/10^12,
S=202424330939/200000000000. Thus ell^2<41 and S^2>42/41. With
A,J,H4,W,B2,E,Q as in `zero-loss-support.md`, set

    G=[A/2-3J/(120*41)-H4/(12ell)]W+B2,
    P=(2/5)S^3[AW+B2]+S^3 EW+cQW.

These are the infinite-upper-index, zero-loss polynomials: no favorable
finite48 term and no positive predecessor-loss term remain. The seven
polynomials checked are A,H4,J,W,G,-Q,-P. Their degrees are respectively
3,4,5,5,10,3,11, hence48 Bernstein coefficients per interval.

`check_grouped_support.py:TABLE` fixes14 rational rows (R,r,b,multiplicity).
Thirteen radii group all64 LEFT support invocations. At each radius r and b
are the componentwise maxima of the original preceding-resource ceilings.
The remaining row is initial R=96/25 with r=7361/4000 and
b=641562334877/10^12. The two published moment bounds giving initial r and
the moment relation giving b remain analytic inputs; the initial outward
rounding inequality is checked independently.

Grouping is sound even if the two maxima occur in different rows. For u>0,
Q is increasing separately in r,b. Once W>0, P has derivatives

    dP/dr = cW[(3/2)u^2+.384/42] > 0,
    dP/db = 3cuW > 0.

Thus the group polynomial upper-bounds every individual call. The other five
polynomials are independent of r,b. The same majorization applies to Q'
and to the derivative ray bound. It does not assert any group maximum is
attained by a common law.

Binding uses the immutable backend archive SHA256
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`,
and LEFT proof member
`finite61/blobs/419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393`.
The new source-binding helper verifies first-bridge maxima, every later
predecessor resource, all55 ordered probability cells and all64 invocations.
The analytic/source locations and exact baseline hashes are given in
`zero-loss-support.md`, Section1; the contact derivation is the original
`paper/analytic-supplement.txt:455–640`, and its derivative bound is :350–410.
No archived module is imported or executed.

## Continuous intervals, Bernstein transformation and whole rays

Each LEFT interval is [R,39/10]; the initial interval is [96/25,21/5].
There is one closed interval per group; endpoints are included. For
p(u)=sum(a_i u^i), degree d, set u=l+(h-l)t. Its transformed power coefficients
are

    q_j=(h-l)^j sum_(i=j)^d a_i binom(i,j) l^(i-j).

The Bernstein coefficients are

    B_k=sum_(j=0)^k q_j binom(k,j)/binom(d,j).

Indeed t^j equals sum_(k=j)^d [binom(k,j)/binom(d,j)]
*binom(d,k)t^k(1-t)^(d-k): cancel binomial factors and apply the binomial
theorem. Consequently p is a convex combination of its B_k on0<=t<=1.
The program additionally reconstructs every q_j by the inverse identity

    q_j=binom(d,j) sum_(k=0)^j (-1)^(j-k) binom(j,k) B_k,

obtained by expanding the Bernstein basis in powers of t. All672 B_k are
strictly greater than1/4, which proves all seven signs everywhere on their
closed intervals, without sampling or asymptotic inference. The fresh log
contains every exact coefficient and each group's minima. Its global minimum is

    168770300272604270966158879019623858439411520950319456559 /
    650737668933625093816320000000000000000000000000000000000 > 1/4.

For each group, at its splice U check Q,Q',Q'',L,L',L''<0, where

    L(u)=(2/5)(u^2/2+1/2+.384/42)+cQ'(u).

Q'''=-6 and L''=2/5-6c<0 extend these signs along the whole ray. The direct
Gaussian derivative bound in `zero-loss-support.md`, Section3, then makes
the contact envelope strictly decrease from its already negative value at U.
This treats both exterior signs and every real raw threshold H. The exact
scale polynomial check gives e_n<.384/n for every n>=42.

## Evidence, smallness and remaining premises

Run from repository root:

    python3 -B mathematics/simplification/2026-10-27/check_grouped_support.py

`runs/grouped-support-20261027/accept01/` records interpreter, input hashes,
stdout, stderr, return code0 and measured runtime about0.12seconds on this
machine. This timing concerns only the new672-coefficient certificate.
Nine negative controls reject a missing, duplicate or reordered group, a
lowered moment ceiling, omitted radial prefix, corrupt or missing coefficient,
negative polynomial and false ray cap. A quadratic and a constant are direct
transform controls. The new checker constructs the polynomial expressions
separately from the binding helper; independent source review is still needed
to ensure those expressions encode the analytic envelope correctly.

The separate bounded diagnostic `discover_grouped_support.py` tried partitions
from a fixed list up to32; every group succeeded at the first one-interval
choice. Its stdout/stderr are retained in `discovery01/`; only the subsequent
fixed acceptance has a full timed receipt. No expensive discovery or native
certificate campaign occurred.

The old finite polynomial sign predicates are no longer premises of this
**alternative** support proof. Their stored JSON serves only to identify the
moment parameters and ordered call graph. Actual resource inequalities,
attainment, moment bounds, Gaussian contact/heat reduction, later CENTRAL
contractions, confinement, profiles, TINY/MID/LOW comparisons, strict Bernoulli,
and BASE41 remain separate. In particular, this does not remove64 resource
acquisitions or the152 LOW rows. The old certificates remain intact.
