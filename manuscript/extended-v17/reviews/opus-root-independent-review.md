# Independent review of the coordinator's manuscript edits

Date: 30 October 2026. Reviewed the working diff against `6339dda` in `main.tex`, Sections 1, 2, the moment-domain subsection, Sections 5, 8 and 9, and Appendices `normalization.tex` and `fixed-fourier.tex`. Paths, rather than section numbers, are authoritative during reorganization. The pending agent-owned conservation, geometry, acquisition and local-comparison edits were excluded from this review. No TeX was changed by this reviewer.

## Result

No mathematical or theorem-scope defect was found in the reviewed changes. The new predecessor-support lemma and solved-excess display are exact consequences of the existing contact and conservation identities. The finite-verification premises remain present in localization and composition. Eight exact scalar comparisons passed freshly; this is not a certificate replay or an audit of the Fourier reduction.

Two minor presentation adjustments would make the scope and notation more precise:

1. `appendices/fixed-fourier.tex`, opening paragraph: “Appendix D verifies these inputs for the maximizers to which the bound is applied” is best qualified by “under its stated entry conditions.” The theorem statements retain those conditions, so this is a cross-reference clarification rather than a missing theorem hypothesis.
2. `sections/04-fixed-entry.tex`, new predecessor-support lemma: `eta_n` is the same scalar called `e_n` in Appendix D's initial-support proof. Either add “the quantity denoted by `e_n` in Appendix D” or coordinate a rename there. The new notation avoids confusing this quantity with the Gaussian factor `e`, but leaving two names without an identification makes the derivation harder to trace.

## Independent derivation: predecessor support

Let `s=sqrt(n/(n-1))`. At a support point `t`, the baseline contact identity is

`0 = n^(3/2)(h(t)-F) + nt phi + H phi (t^2-1)/2 + 3c rho (t^2-1)/2 - c(|t|^3-rho-3t beta)`.

The predecessor inequality supplies

`h(t) <= F^G_(n-1)(H-t) + c rho/sqrt(n-1)`.

The excess definition gives `F=F^G_n(H)+(c rho+a)/sqrt(n)`. Substitute these expressions into the right side of contact. Because the coefficient of `h` is positive, the resulting expression is an upper bound on zero, as required. Its Gaussian terms are

`n^(3/2)[F^G_(n-1)(H-t)-F^G_n(H)] + nt phi + H phi(t^2-1)/2`.

Since `(F^G_n)'(H)=phi/sqrt(n)` and `(F^G_n)''(H)=-H phi/n^(3/2)`, these are exactly the newly defined `H_n(H,t)`. The non-Gaussian terms simplify to

`c[-|t|^3 + 3rho t^2/2 + 3beta t + rho{n(s-1)-1/2}] - na`.

Thus the new formula, all signs, its normalization, and the coefficient `-na` are correct. Both probabilities use the same closed event at `H-t`; no atom convention is changed. The argument actually needs only `n>=2`, the contact identity and the predecessor bound, but retaining `n>=42`, `c=C_E`, `a>=0` gives a valid narrower statement matching its use.

## Independent derivation: excess and signs

The retained positive conservation identity is

`R_c=(n+H^2)a + nc rho(1-e) + n phi(0)e D/6 + n^(3/2)L`, with `c=C_E`.

Here `n+H^2>0`, `rho>=1`, `0<e<=1`, `D>=0` and `L>=0`. Solving for `a` yields precisely the introductory display, without requiring `a>=0`. If `a>=0`, discarding the other nonnegative contributions proves `n phi(0)eD/6<=R_c`. A uniform upper bound for `R_c` plus a uniform bound for `|H|` at `n>=42` bounds `nD`, because `e` then has a positive uniform lower bound. The new prose expressly assigns these uniform estimates to quantitative localization and does not invoke a fixed-law limit. This is the needed scope.

## Notation and theorem scope

The replacement of the supremum symbol `A` by `a^*` is complete in the reviewed fixed-target file. The proof still obtains lower-moment uniform integrability from the third-moment ceiling, uses lower semicontinuity of the third moment, and deduces equality of limiting third moments from maximality. It does not infer third-moment uniform integrability from bounded third moments. “Along this maximizing sequence” refers to the subsequence selected immediately above; “along the chosen subsequence” would be slightly more explicit but is not needed for validity.

The sign equivalence remains correct. For `C_n<c`, the inequality `rho>=1` gives `rho(r-c)<=C_n-c<0`. For `C_n=c`, scores approaching `c` have `rho<=2sqrt(n)/c` eventually, so their excesses tend to zero. Reflection retains its closed/strict endpoint distinction. Moving the definition of `Q` earlier does not alter its formula; expanding `-I/n^(3/2)` gives exactly `Q-h`.

The moment proof's `c` to `c_gamma` change is consistent in the definition, polynomial and expectation identity. No coefficient or integrability hypothesis changed. The introductory local-result summary includes the noise cap and points to the complete conditional-support domain. The global implication retains the structural, binomial and entry premises as well as the missing finite base. The discussion correctly says that improving localization alone cannot lower a threshold also used in the local comparison.

## Fresh exact scalar checks

Using Python 3 `Fraction`, the following strict comparisons were checked by exact rational arithmetic:

- `pi_- > 333/106 > (4431/2500)^2`, where `pi_-` is the displayed finite Machin sum.
- `pi_+ < 22/7 < 2(251/200)^2`, with the displayed `pi_+`.
- `(0.39886)^2 < 7/44`.
- `32.20665378/700 < 0.047`.
- `1.83605680 < 46/25`.
- `71527/48000 < 3/2`.

All eight comparisons passed. Exact positive numerator/denominator margins, Python version and hashes of the reviewed inputs are saved in `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_opus_20261030/external/root-edit-scalar-checks.json`. The command returned exit code 0 and stdout `Fresh PASS: 8 exact rational comparisons.` No floating-point approximation entered acceptance. The existing alternating-series proof supplies `pi_-<pi<pi_+`; combining it with the new comparisons gives both claimed square-root enclosures in their required directions.

## External-source status and limits

The primary-source verification is recorded in `opus-external-scope-review.md`. The current edits do not introduce a new theorem dependent on the unread parts of a reference. Schulz's strict finite-binomial statement and Shevtsova's moment statement were checked; the structural coefficients were checked in their primary publication record, without independently reproducing their full numerical proof. The recent reported results remain background, explicitly outside the proof's dependency chain.

This review establishes correctness of the listed changes relative to the retained identities and hypotheses. It does not independently establish the complete finite base, audit every analytical Fourier constant or prove the semantic equivalence of all certificate checks to Appendix D. Accordingly, retaining the entry premises remains necessary at the present audit scope.
