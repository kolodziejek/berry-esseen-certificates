# Handoff: continue the complete five-summand row

The selected manuscript remains journal-v21, 86 pages. This research package
does not justify deleting any part of its earlier finite proof.

## Completed and reproducible

1. A continuous score certificate for n=5, p in [19/50,39/100], k=2,
   u in [-1/100,1/100], full noise [0,7687/25000]. Its exact target is C_E,
   with rho>=11/10 and the original acquired beta/support bounds.
   Object: certificates/region-v1/proof_object.json.
   Separate original acceptance result SHA256:
   8f4f9c28d0493858cda50f2da5269b9ddbe70b2dc905252b1d6ebfc99949d760.
2. The original threshold/domain projection. The Bernoulli sum threshold is
   h=5p+sqrt(w)H, with H the raw sum threshold of standardized X. Its bounds
   are [777741882751/10^12,3072258117249/10^12]. Only nearest k=1,2,3 occur.
   Every mixture count j=0,...,5 remains.
3. A general cell criterion and the negative-numerator Gaussian refinement
   in six_count_reduction.tex/pdf. Source and original execution boundaries
   are explicit.

## Next complete coverage target

Use the exact original domain, not just favorable points:

| Nearest k | Required closed phase interval |
|---:|---|
| 1 | [-222258117249/10^12,1/2] |
| 2 | [-1/2,1/2] |
| 3 | [-1/2,72258117249/10^12] |

Probability is [19/50,39/100] throughout; retain all noise and common moments.
The intervals may be split at zero and into closed dyadic cells. A complete
row must accept every root or exclude it by a proved original condition.
Missing leaves, altered targets or sampled feasibility are not acceptance.

## What the wider attempt exposed

The basic constant Gaussian target combines noise zero with a quartic
expectation potentially maximized at large noise. It gave negative floating
discovery margins near u=-1/2. More subdivision alone did not repair that
loss; this is not an exact impossibility certificate or a counterexample.

For a=k+u-5p<=0, a^2<=15pq, the function
g(lambda)=Phi(a/sqrt(5pq+lambda)) is concave. Therefore the quartic bound minus
g is convex on the variance polygon. Each vertex may use its own noise
lambda=5(x+y). Proposition 3 proves the rule; use the precise closed-cell
guards. Positive or crossing numerator cells may use the original safe target.

A further candidate keeps the exact common absolute third-moment numerator:
R=pq(1-2pq)+3(px+qy)-gamma0*x+gamma1*y,
rho=R/(pq+x+y)^(3/2).
For a fixed noise slab and an upper bound W for pq+x+y, actual R is positive,
so rho>=R/W^(3/2). Blend this with rho>=11/10 using a fixed rational
theta in [0,1]. The resulting correction is affine in x,y at fixed
p/gamma and preserves the corner convexity. This strengthening is being
developed in the local work directory; this initial checkpoint does not
claim its complete acceptance.

## Local work and preservation

Local root: /Users/bkolodziejek/Downloads/BE_Codex_Handoff.
Active additive sources: work/count_row_20261105/construct/model_v2.py,
model_v3.py and corresponding discovery/readers, if present.
Domain and complete-row assembly: work/count_row_20261105/domain/ and
work/count_row_20261105/assembly/.
Independent review: work/count_row_20261105/review/.
Actual captures: runs/count_row_20261105/.

The V1 numerical sources and proof object in this PR are frozen. Use a new
epoch for mathematical changes and keep unsuccessful searches/captures.
Before accepting a wider result: independently review the formula, replay
the entire object with exact arithmetic, run meaningful rejection controls,
and bind the full original root census. Then package unchanged readers and
fresh relocation evidence. Completing one row still does not replace all
295 original five-summand count forests or the later finite families.

