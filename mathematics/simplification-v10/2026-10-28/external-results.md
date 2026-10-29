# External results checked against their original statements

## The Bernoulli endpoint and the available gap

Jona Schulz, *The optimal Berry–Esseen constant in the binomial case*,
Trier dissertation (2016), Theorem 1, printed p.15 (PDF page25),
[original dissertation](https://d-nb.info/1197702695/34).
Equation (4) is strict for each finite n>=1 and every p in (0,1).
Equation (5) gives the sharper strict bound, for p in [1/3,2/3],

`C_B < c(p) = phi(0)*(3+|1-2p|)/(6*(p^2+q^2))`.

Here C_B can be any one-sided binomial discrepancy, since the theorem bounds
the full Kolmogorov distance. Thus the zero-noise endpoint requires no new
certificate. Direct algebra gives, with r=min(p,q) and p*=(4-sqrt(10))/2,

`rho_B*(CE-c(p)) = 2*CE*(r-p*)^2/sqrt(pq)`.

This gap is nonnegative, vanishes at p* and its reflection, and must not be
replaced by a positive uniform constant on an interval containing either.
Outside [1/3,2/3], use only the global bound, hence gap zero. These are
external theorems; this task checked the hypotheses and formulas, not the
dissertation's complete proof. No new Lean build was performed.

## Quadratic Poisson comparison

Iosif Pinelis, *On the Bennett–Hoeffding inequality*, arXiv:0902.4058,
Proposition 2.8 and Corollary 2.11, printed p.9,
[original paper](https://arxiv.org/pdf/0902.4058).
For independent variables Xi with EXi<=0, Xi<=A>0, and sum EXi^2<=V,
the stated comparison applies to every quadratic hinge `(x-t)_+^2`:

`E(S-t)_+^2 <= E[A*(Pois(V/A^2)-V/A^2)-t]_+^2`.

This supplies a variance-envelope comparison and needs no lower support
bound. For b>0, t<b, Markov also covers the closed event S>=b. Taking the
infimum gives its quadratic Poisson tail bound P2. At V=0 the original
sum is deterministic and is handled separately. This is an external
comparison theorem, not a claim that an arbitrary rounded numerical
evaluation of its infimum is certified.

### Evaluation and dominance: direct deductions

Write mu=V/A^2 and x=mu+b/A. For any real j<x one may use

`P2 <= E(Pois(mu)-j)_+^2/(x-j)^2`.

For j=0 its numerator is mu+mu^2. For j=1 it is
mu^2-mu+1-exp(-mu). For an integer j>=0 the numerator follows from
the full second moment minus the finite sum over Poisson values <=j.
Every such choice is an upper bound; optimizing is optional. Directed
enclosures for the exponential and nonnegative denominators remain proof
obligations for a numerical certificate.

The optimized P2 is no larger than Cantelli: choose the physical hinge
t=-V/b and bound its truncated square by the full square. It is also no
larger than the usual cubic Poisson and Bennett bounds. To see the latter
claims without comparing numerical tables, use the positive mixtures

`(y-t)_+^3 = 3 integral_t^infinity (y-s)_+^2 ds`,

`exp(k*y) = (k^3/2) integral_-infinity^infinity exp(k*s)*(y-s)_+^2 ds`.

If r is the infimum of the hinge ratios at b, then each expected hinge
is at least r times its value at b. Integrating against either positive
measure proves the comparison of optimized bounds. This direction does
not say that a particular integer-hinge candidate dominates the other
tail bounds. For a finite implementation it is safe to retain their minimum.

The extension work records its actual certified choices separately. No
global count cover follows merely from this dominance observation.
