# Final composition: independent statement-level review

**Mathematical status:** the proposed composition follows from its named
analytic results and complete numerical/interface premises. No new
composition gap was found. **Execution status:** several finite-base
ancestors remain unfinished. The proposed final introduction and theorem
must remain inactive until those gates close. This review does not announce
the all-law theorem and reruns no numerical certificate campaign.

The main objects reviewed are the inactive `01-introduction.tex`,
`09-composition.tex`, and `reproducibility-extension.tex`, against the active
fixed-target, smoothing, finite-induction, LOCAL42/47, fixed-entry, geometry,
and count-comparison statements. The checks below use those statements and
their mathematical derivations, rather than historical success summaries.

## 1. Re-derivation of the first-failure entry

Fix a standardized law with third absolute moment rho and a raw threshold H.
Let v=n-1 and G_v(H)=Phi(H/sqrt(v)). Conditioning on the final summand gives

`|P(S_n<=H)-E G_v(H-X)| <= C_(n-1)*rho/sqrt(v)`.

This is valid at atoms because the predecessor inequality concerns the
closed CDF at every real threshold. Taylor expansion in X uses only E X=0,
E X²=1 and E|X|³=rho; its remainder is bounded by
`phi(0)*rho/(6*v^(3/2)) < rho/(15*v^(3/2))`.

For the Gaussian variance change,

`G_(v+1)-G_v-G_v''/2 = (1/4) integral_0^1 (1-t)G_(v+t)^(4) dt`.

Since `||phi'''|| <= 2/pi`, its absolute value is at most
`1/(4*pi*v²) < 2/(25*v²)`. Multiplication by sqrt(n)/rho and rho>=1 gives
exactly the active one-step recurrence. The estimates are uniform in both
the law and H; taking the two suprema does not require a fixed-law limit.
The factors 1/4 and the integral of (1-t), namely 1/2, are both necessary.

If `C_(n-1)<=CE<=C_n`, put `s=sqrt(n/(n-1))`. Rearranging yields

`n(C_n-CE) <= n/(n-1) * [CE/(s+1) + s/15 + 2s/(25sqrt(n-1))]`.

For n>=42, the valid simultaneous bounds are
`n/(n-1)<=42/41`, `1<s<81/80`, `sqrt(n-1)>6`, and `CE<41/100`.
The square comparison for s is `41*81²-42*80²=201>0`. Consequently

`n(C_n-CE) < (42/41)*(41/200+27/400+27/2000)
             =3003/10250 <3/10`.

This is a strict uniform rational bound, not an unjustified passage of
pointwise strict inequalities through a supremum. It implies
`C_n<41/100+(3/10)/42=73/175<4226/10000<4247/10000`.

For every one of the original laws,
`sqrt(n-1)*Delta_(n-1)(P)/rho(P)<=C_(n-1)<=CE<=C_n`.
Thus its same-law positive predecessor loss is zero. The corresponding
loss using the global predecessor constant is also zero. Nothing here
asserts monotonicity of C_n or replaces the marginal between indices.

## 2. Why a weak base through 42 is sufficient

Assume the sharp weak inequalities at 1,...,42 and suppose the set
`{n:C_n>CE}` is nonempty. Its least element satisfies n>=43. Minimality
supplies both `C_(n-1)<=CE` and `C_(n-2)<=CE`, including the endpoint n=43,
where the two deleted indices are 42 and 41. Since `CE<.41<.4253`, these
are stronger than both deleted-predecessor ceilings in LOCAL42 and LOCAL47.

The exact hypothesis check is:

| Requirement | First strict failure | Finite local domain | Uniform local domain |
|---|---|---|---|
| index | n>=43 | use 43<=n<=48 | use n>=49, which is inside n>=47 |
| positive scaled excess | 0<n(C_n-CE)<3003/10250<.3 | at most .54 | at most .7 |
| predecessor loss | zero | at most .19 | at most .19 |
| own score | below 73/175 | below .4226 | below .4247 |
| both deleted constants | at most CE<.41 | below .4253 | below .4253 |

The two chosen index cases partition every possible first failure.
LOCAL42 is used only within its proved finite band 42--48. The uniform
result is used within its actual all-n>=47 domain, not extrapolated from a
saved finite upper-index field. The two-index deletion at 49 does not need
an independent tail premise: indices 47 and 48 are smaller than the
hypothetical least failure and therefore already satisfy the weak bound.

A ratio maximizer exists at each of these fixed indices by
`ext:ratio-attainment`. Its contact coefficient is c=C_n, its positive
closed score equals C_n, and its support is compact. These are exactly the
local-engine premises. The engine treats both threshold signs, derives all
moment/support restrictions for that same law, and retains actual n in
conditional binomial probabilities. Positive noise gives C<C_B^+<=CE;
zero noise gives the Bernoulli law and C<=CE. Both contradict a *strict*
failure. No strict base and no nonnegative-excess equality exclusion at
small indices is needed for this part.

## 3. Reflection, atoms, and attainment at equality

For every raw H,

`P(-S_n<=-H)-Phi(-H/sqrt(n))
 =Phi(H/sqrt(n))-P(S_n<H)
 >=Phi(H/sqrt(n))-P(S_n<=H)`.

Thus reflection dominates a negative closed-CDF error by a positive closed
error while preserving standardization and rho. Equality of the two
errors at atoms is neither asserted nor needed. This justifies reducing
the absolute discrepancy supremum to positive closed scores.

The fixed-target attainment proof does not assume uniform integrability
of third moments from a bound on those moments. That bound gives uniform
integrability of the first two moments, preserving mean and variance under
weak convergence. Third moments initially satisfy only lower
semicontinuity. The closed-set inequality at moving thresholds gives
`limsup F_j(H_j)<=F_P(H)`; maximizing the penalized objective then forces
the lost third-moment mass to be zero. Compact support follows later from
the contact inequality's negative cubic term. Thus the order does not
use higher moments before bounded support.

For c>0 write `a=rho*(r-c)` and a* for its maximum. If C_n=c, choose
positive scores r_j increasing to c with r_j>=c/2. Since
`rho_j*r_j<=sqrt(n)`, one has `rho_j<=2sqrt(n)/c`; hence a_j tends to zero.
Every excess is nonpositive, so a*=0 and fixed-target attainment produces
an actual maximizer with a=0. If C_n>c, some excess is positive and its
maximum is positive. Therefore `C_n>=c` supplies an attained nonnegative
excess. This is the required equality argument; merely proving every
individual law has score below c would not establish C_n<c.

## 4. Strictness includes n=700

After the weak all-index bound is established, `C_(n-1)<=CE` holds for each
fixed n>=700, including the predecessor 699. Choose an attained
fixed-target maximizer at c=CE if C_n>=CE. This is a different optimization
problem from the finite-index ratio maximizer; the final text correctly
keeps them distinct.

The compact localization theorem applies at actual n>=42 under a>=0,
the sharp predecessor, and the published affine structural estimate. It
gives the simultaneous `nD<=32.20665378` and `|H|<=1.83605680` bounds for
the same compact law. Its constants are uniform for varying laws and
thresholds; no triangular-array conclusion is inferred from a fixed-law
asymptotic expansion.

At n=700 already, `700*.047=32.9>32.20665378`, so the direct geometry
argument gives the strict probability, displacement, and noise bounds.
The two contact rays give the actual conditional supports. The resulting
inclusion in the common-strip theorem is exact:

- p in (3/8,93/200) lies in its closed probability interval;
- a_0,a_1>=0 and a_0+a_1<1/250 meet its inward limits;
- the strict acquired outer endpoints lie in its closed +/-3/5 bounds;
- lambda<7/20 and |H|<=1.83605680<46/25 meet its full noise/threshold domain;
- B is the actual indicator of X>0 and the centered conditional noise
  decomposition reconstructs the original marginal, not a relaxed optimizer.

For positive lambda the theorem gives a<-lambda/100<0. At lambda=0,
conditional centering and zero variance imply U=0 almost surely, so the
law is Bernoulli. The finite-binomial strict bound gives a<0 there too.
Both contradict a>=0. No lower bound on positive lambda and no uniform
negative margin over all laws is required, because the fixed-target
maximum is attained. Thus the proposed deduction is C_n<CE for every
integer n>=700, not only n>700. No strictness at 1--699 is claimed.

## 5. External theorem hypotheses and global sharpness

The inspected primary statement in [Shevtsova (2013), pp.124--125](https://www.mathnet.ru/php/getFT.phtml?jrnid=ia&option_lang=eng&paperid=252&what=fullt)
gives the iid bound `Delta_n<=.3031*(ell_n+.646*tau_n)` for every n>=1.
Taking summands X_i/sqrt(n) gives `ell_n=rho/sqrt(n)` and
`tau_n=1/sqrt(n)`, exactly the manuscript's affine structural inequality.
The hypotheses are independent identically distributed centered summands,
total variance one, and finite third absolute moments. The paper's strict
CDF convention has the same supremum distance from continuous Phi as the
closed convention, by approaching each threshold from either side.

[Schulz (2016), Theorem1, printed p.1](https://d-nb.info/1197702695/34)
states a strict bound for the full binomial Kolmogorov distance, every
0<p<1 and every finite positive integer n. It therefore implies the signed
closed-threshold inequality used here. The same thesis's Remarks4.1--4.2,
printed p.15, explicitly state the Esseen full fixed-p limit and its
specialization at p*=(4-sqrt(10))/2. The required distribution is
nondegenerate, standardized, and has all moments.

For that one fixed Bernoulli law, the third absolute standardized moment
is `(p*²+q*²)/sqrt(p*q*)`; its signed third moment is
`(q*-p*)/sqrt(p*q*)` and its lattice span is `1/sqrt(p*q*)`.
The normalized limit is therefore
`(3+q*-p*)/[6sqrt(2pi)(p*²+q*²)]`.
Direct algebra gives `q*-p*=sqrt(10)-3`,
`p*²+q*²=10-3sqrt(10)`, and the quotient of the two numerators is
`sqrt(10)/(10-3sqrt(10))=3+sqrt(10)`. Thus the limit equals CE.
Since C_n dominates this law's score at every n, `sup_n C_n>=CE`.
The weak upper bound supplies the reverse inequality. There is no
interchange of law and sample-size suprema with a limit, and no assertion
that a finite-index maximizer must be Bernoulli.

## 6. Numerical ancestors still required before promotion

These are execution obligations, not omitted hypotheses that the displayed
composition somehow proves:

1. ROOT4's complete fresh 260-parent/1300-HIGH replay and full acceptance;
   the interrupted producer is not an accepted process. This is an ancestor
   of C4 and hence of the finite induction, even though C5's modular
   31-parent/326-frame numerical assembly is complete.
2. The remaining foundation support/Fourier complements, actual
   7--9 resources, 10--14 cores/families, and complete foundation semantic
   and acquisition joins. All13 INITIALs and owncaps344-row readback alone
   do not discharge these gates. The repaired serial resources79 routing
   is transport preparation, not a numerical pass.
3. The remaining actual35--39 INITIAL/resource calculations and their full
   current resource-to-COUNT traversal. Positive39 is a separate completed
   prerequisite of sharp39; assuming the later sharp39 conclusion to obtain
   its own-score ceiling would be circular.
4. Final source/capture binding of every selected result to the manuscript
   dependency graph and the retained compact entry/scalar checks.

The foundation owner reports the N6 chain now complete with41parents and54
source-derived edges; its final manuscript-level evidence binding is still
part of the coordinating readback. The finite owner reports all selected15--34 families complete, including
the whole high-rho14--19 complement, and identifies only35--39 as remaining
in that lane. The selected bridge roots now include complete actual40--42,
all171 LOCAL42 tasks, and the full14+41 uniform47 suite with their joins.
These reports delimit outstanding gates; they are not substituted for the
continuous argument above or for the coordinating final evidence readback.

## 7. Editorial findings and proposed changes

No theorem-level change to the proposed final composition is required.
Two small wording/status changes are useful:

- In the inactive reproduction text replace **"independent exact acceptance
  follows that planning step"** by **"complete exact acceptance follows
  that planning step"**. Shared arithmetic routines are exact replay, not
  an independent implementation. The introduction already states this
  distinction correctly.
- Refresh the working dependency table: LOCAL42's last binder and the
  high-rho14--19 complement have completed. Keep ROOT4, the remaining
  foundation gates, and35--39 pending. Do not convert the proposed all-law
  theorem into active text merely because this composition review passed.

For readability, the first sentence of the upper-bound proof could cite the
specific finite assembly labels in addition to the reproduction appendix:
`ext:n123`, the four-summand physical theorem, the fifth-index assembly,
`ext:finite-five-fourteen-assembly`, `ext:finite1539-assembly`, and
`ext:floor40`. This is an exposition improvement, not a new mathematical
premise. Retain the explicit equality/attainment paragraph and the
zero-noise Bernoulli branch; both do real logical work.
