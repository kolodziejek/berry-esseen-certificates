# Equality in the uniform local comparison

Mathematical status: locally derived extension of the stated LOCAL47 interface,
subject to the same contact/Fourier/acquisition/confinement analytic results and
unchanged accepted numerical objects. Execution status: the existing complete
14+41 numerical campaign and readbacks are retained; no numerical target was
changed and no new integration campaign is claimed. This note audits the new
boundary case, not the entire earlier proof from first principles.

## Conclusion

The uniform local argument admits **0 <= n(C_n-C_E) <= 7/10**. With its other
hypotheses unchanged, an attained ratio maximizer is impossible even when
C_n=C_E. The separate compact fixed-target route is therefore unnecessary for
retaining the claimed strictness at n>=700. After the weak all-index theorem,
the same argument in fact gives strictness at every n>=47. Do not extend this
conclusion to n42–46 without a separate audit of LOCAL42.

This is not an argument by continuity in the optimum, nor does it replace a
positive certificate target by zero. The native local comparisons prove a
strict loss relative to the law's own Bernoulli count for every positive
noise. The zero-noise law is handled separately by the strict finite-binomial
theorem already cited in the manuscript.

## Boundary audit

All manuscript locations below are in `manuscript/extended-v17` in the revision
checkout. Native locations are relative to
`work/extension_20261030/bridge/original_tail/BE_cutoff49_20260930/baseline/certificates/work/below50_20260929`.

1. **Attainment and reflection.** At a fixed n, ratio attainment applies at
   C_n=C_E>0, not only above C_E. Reflection is the closed/left-limit reduction
   in the existing core theorem; it does not discard an atom. Use the attained
   positive closed-event pair. The contact coefficient is c=C_n and the
   fixed-target excess a is exactly zero. No positivity of C_n-C_E is required
   for contact or bounded support.
2. **Unrestricted support and strip.** `appendices/local-estimates.tex`, support
   polynomial and bounded-threshold sections, explicitly use C_n>=C_E. The
   selected initial support rows have K=0, lower score .4095, and loss .19.
   The support bands [45,49],[50,59],[60,89],[90,134],[135,199],[200,infinity)
   include every n>=47. The infinite row drops only a favorable fifth-order
   term. No bound involving 1/(C_n-C_E) occurs.
3. **Initial numerical domain.** `entry/accept_initial47.py` declares
   CE<=C_n<=.4247 and fixes `barrier=Fraction(0)`. In
   `entry/local_signed_core.py`, the lower score is
   `.4095+K/nmax`; nmax=98 occurs here with K=0. Thus 98 is not an upper limit
   on the actual sample size. The acceptance program evaluates the fixed
   floor 47; the analytic index comparison applies to every actual n>=47.
   The subtracted compulsory score charge is K*rho=0. Cells excluded by a
   negative score-update numerator are impossible because e>=0, including
   equality. A positive raw/defect *upper bound* is not a positive lower
   bound on the actual excess or defect.
4. **Raw sign license.** With w=H^2/(2n), the exact identity is

   `ne rho+n CE rho(1-exp(-w))+n phi(0)exp(-w)D/6+n^(3/2)L=R`.

   The first raw bound R<r<.4n implies
   `phi(H/sqrt(n))(gamma+3J)/6=C rho+sqrt(n)L-R/n>0`, since
   C rho>=CE>.4. This proves the unweighting license also at e=0.
   Thereafter `ne rho+kappa nD+n^(3/2)L<=B(H)` uses e only as a
   nonnegative summand. No division by e, D or L is made. The extra phase
   curvature uses the previous raw bound and is included once.
5. **Acquisition and confinement.** The uniform acquired-entry corollary
   already states CE<=C and 0<=n(C-CE)<=.7. The confinement budget explicitly
   retains e>=0. Strict budget inequalities originate in strict outward
   Fourier/target enclosures, not in e>0. A box with its residual G<=0 is
   excluded from the strict resource even at G=0. Every positive denominator
   is a separately checked probability, mean, support-gap, variance-envelope,
   slope or quadratic-curvature quantity. Their positivity is not inferred
   from e>0. The selected central and left tables remain 45+38 closed rows.
6. **Local comparison is score-independent near CE.**
   `shortloc:theorem` and the six selected TINY/MID/LOW variants require
   only C>=c_*=.4. The correction C(rho_B-rho) is bounded with this lower
   score after proving its coefficient has the correct sign. The normalizers
   (`local/tiny47wide_normalization.py`, `root/low47_normalization.py` and
   their MID counterparts) use .4, not a positive excess. Their positive
   mass/variance/entropy/count denominators are checked at the fixed floor.
   They prove `rho_B(C-C_B)<-.001 lambda` for every lambda>0 in the selected
   domain. Thus C=CE is already impossible at positive noise since C_B<CE.
7. **Arbitrarily small noise.** TINY covers 0<lambda<=.05 using the scaled
   quartic with t=E W_k^2 and r=zt. Its polynomial quotient extends to t=0;
   the positive-noise normalization has t>=omega_- lambda>0. The Poisson
   and Bennett bounds divided by lambda are monotone up to the positive
   endpoint. No fixed additive error is substituted for a noise-relative
   error. A deterministic one-sided conditional component is allowed.
8. **All phases/signs/counts.** The selected coverage reader
   `local/final_review/check_local47_coverage.py` checks the entire
   probability range [.304,.47], both H signs, the closed phase seams,
   all noise endpoints and ceilings, and entirely excluded LOW boxes.
   The exact conditional identity uses strict outgoing and closed incoming
   events. `k` and `delta=k-np` stay fixed in normal differentiation.
   The proof does not reflect a positive-phase estimate into an unproved
   negative-phase region.
9. **Zero noise, explicitly.** If lambda=n E U^2=0 then U=0 almost surely
   and X=(B-p)/sqrt(pq), with 0<p<1 from the acquired row. At any raw H,

   `sqrt(n)|P(sum X_i<=H)-Phi(H/sqrt(n))| < CE (p^2+q^2)/sqrt(pq)`.

   This is exactly Schulz (2016), Theorem 1, with its strict sign, verified
   against the original thesis page 1 (PDF page 11), not inferred from
   asymptotic sharpness. It applies for every finite positive integer n and
   all real thresholds. The old text's weaker invocation C_B<=CE was
   sufficient for strict first failure, but is not the full cited theorem.
   Source: https://d-nb.info/1197702695/34 ; existing bibliographic key
   `Schulz2016`. No new external theorem has been introduced.

## Consequence and implementation

After C_j<=CE has been proved for every j, suppose C_n=CE at n>=47. Its
predecessor loss is zero, its own score is below .4247, both deleted scores
are at most CE<.4253, and its scaled excess is zero. Apply the equality-
inclusive uniform local theorem; positive noise and zero noise are both
impossible. Hence C_n<CE. This uses attainment; merely proving that every
individual law has a strict bound would not rule out a nonattained supremum.

In journal-v18 state the local result with the closed lower excess endpoint,
prove the zero-noise branch using the exact strict Schulz statement, and
retain a named equality corollary after the weak all-index induction.
The old v17 theorem/proof and sealed evidence remain unchanged. The removal
of the separate compact route is contingent on the new chapter preserving
the whole analytic interface above; this note cannot compensate for a
missing analytic proof in that chapter. Numerical verification, independent
mathematical audit, and external peer review remain distinct.
