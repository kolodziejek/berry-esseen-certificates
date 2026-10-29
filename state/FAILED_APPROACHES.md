# Failed strengthenings and cautions — v16, 29 October 2026

Earlier records remain in runs/simplification-v16-20261029/stateBefore01 and
all prior versioned proof notes. These are failures of intermediate claims,
not counterexamples to Berry–Esseen.

- Budget alone does not give amplitude.6. An actual n700,p.42 law with rare
  U0=-.8 and lambda10^-6 meets nD<=32.20665378 and the old radius3.14.
  acquisition-check.py and acquisition-review.py independently verify it.
- Removing n>=700 from narrow probability acquisition fails: n42,p.3
  Bernoulli meets the same budget. The signed budget also fails under naive
  reflection at p.58. Reacquire the chosen positive witness.
- The small-noise incoming tail requires(1-u)^-4 for positive u. At n700,
  p3/8,lambda.01,U0 in{-.6,1/26250},U1=0,u.7, the first incoming probability
  exceeds357259/13057579>.43*.01. small-review-check.py supplies the exact
  Bonferroni control. Do not omit that factor.
- Bounding all incoming variances by a count-independent maximum is too coarse
  for the new small-noise margin. Preserve actual linear count dependence.
  Extending the same outer positive phase bound to.75 also fails.
- The old sqrt(lambda)<=lambda+1/4 tangent cannot certify rightlambda.03
  at n200. The new tangent(5/3)lambda+3/20 works, but its criterion does not
  extend to zero noise or n100. The corresponding negative endpoints are
  retained by counts-check.py/unified-check.py.
- Uniform cubic favorability outside the displayed probability domain is false;
  the independent generic review has an actual p.26 control. The cosine3
  lower bound also fails at diameter.75, so the wider Left row uses7/5.
- A universal floor anchor at tiny noise remains refuted by v15 counts-phase.
  The selected small-noise proof uses a shifted interval of length1.
- BASE41 plus conditional acquired exclusion at n>=700 does not give an
  unconditional cutoff. An earlier failure destroys the predecessor premise.

Review corrections were descriptive/typographical only: explicit conditional
noise notation and integer n, a missing TeX backslash, one overflow phrase,
and correct odd/even fold atom wording in a test comment. No theorem was
weakened. Old failed compile/development runs remain preserved.
