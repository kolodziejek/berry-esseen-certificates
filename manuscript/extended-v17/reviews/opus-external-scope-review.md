# External-input and theorem-scope review of the Opus plan

Review date: 30 October 2026. Baseline: commit `6339dda253238048aa75dcf1f2e8c4b73b7b6522`, `manuscript/compact-v16`. The external document is `/Users/bkolodziejek/Downloads/manuscript_revision_plan(1).md`. Its labels “JUSTIFIED” and reports of executions were treated as claims to check, not as evidence. This review changes no TeX and reruns no certificate. Source-reading evidence is recorded separately under `runs/manuscript_opus_20261030/external/` in the handoff workspace.

## Decisions that affect the revision

| Proposal | Mathematical status | Execution status / action |
|---|---|---|
| G8 / P3.6(c): delete the entry premises and promote Conditions D.3/D.5 to proved propositions | Not justified by the external plan or this bounded review | No new checker-semantic audit here. Retain the premises. |
| P3.2: finite-base-only main theorem | Stronger than the baseline theorem unless G8 is separately discharged | Do not implement in that form. |
| P3.2: introductory local theorem | Missing the essential noise restriction `0 < lambda <= 7/20` | Restore the full conditional-support, parameter and threshold domain; separate zero noise. |
| A1: lattice moment-span corollary | Locally derived from the manuscript's gap inequality; proof below | Pure mathematics; no numerical execution needed. |
| A2: conservation solved for excess | Algebraically valid at contact without assuming nonnegative excess | Pure mathematics; retain the definition and hypotheses of the remainder. |
| A7: non-strict binomial input suffices for the non-strict global conclusion | Valid, with every other baseline premise retained | A remark is safe; it does not establish strict `C_n < C_E`. |
| P6: precise external statements | Verified to the scope stated below | Source inspection, not independent reproduction of all cited proofs. |
| A9–A13: alternative proof routes | Partial or speculative | Do not convert into manuscript results or change constants without new proofs/checks. |

## 1. Why G8 is a substantive strengthening

The baseline acquired-witness theorem uses the predecessor bound, the external structural inequality and the complete entry conditions. The global theorem additionally requires the finite base and strict finite-binomial theorem. Conditions D.3 and D.5 include analytical validity, parameter domains, denominator positivity, complete coverage and correspondence between the inequalities and the finite checks; they are not merely a list of printed positive rational numbers.

An arithmetic replay can discharge its actual rational predicates. It does not by itself prove the Fourier estimates in Appendix A or the mapping from those estimates and a maximizing witness to every certified box. The external plan explicitly did not check that mapping or the constants of Propositions A.2–A.3. Its claim that deleting these assumptions leaves the theorem unchanged therefore lacks the necessary justification. This is not a finding that the certificates are false: it is a refusal to enlarge the proved scope on the strength of an unperformed audit.

Safe presentation: call them the *specified finite-verification conditions*, explain what their acceptance establishes, report fresh arithmetic executions separately, and retain the conditions in localization and composition. A later promotion requires a proof of each analytical reduction and coverage implication plus a semantic audit of the checker. A finite collection of checks may control all `n >= 42`, but that conclusion comes from the all-index analytical bounds. Avoid the blanket claim that every bound in Appendix A is decreasing in `n`.

The proposed introductory argument also needs two qualifications. A uniform upper bound on `R_c` is an output of the retained quantitative-entry argument, not of contact alone. To conclude `D = O(1/n)` from conservation one also needs a uniform positive lower bound for `e = exp(-H^2/(2n))`. A claim of distance `O(n^-1/2)` from the Esseen law needs a named distance or explicit coordinate estimates; a scalar defect estimate alone is not a metric statement.

## 2. Where the predecessor is used

For the selected route, the plan's claim that the numerical predecessor inequality is used for support control is accurate. In `sections/03-conservation.tex`, the measure `nu = Law(H-S_(n-1))` is positive and

`L = sum_g tau_g integral_[u,v) (t-u) dnu(t) >= 0`

holds directly. Neither its sign nor the gapwise contact identity uses `C_(n-1) <= C_E`. The half-open interval and endpoint atom rule must remain. The predecessor bound enters the initial support control in Appendix D and the later support strip in `sections/07-direct-acquisition.tex`. A safe sentence is: “The numerical bound at the preceding index is used in the support estimates; the conservation identity and nonnegativity of leakage hold independently of that bound.” This distinguishes use of the predecessor *distribution* from use of its Berry–Esseen *bound*.

## 3. Esseen: exact scope and an independent corollary

The original [Esseen 1945 paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5654-11511_2006_Article_BF02392223.pdf), Chapter IV, Theorem 3, printed p. 56, gives the lattice expansion for a fixed iid law of mean zero, nonzero variance and finite absolute third moment. The span is maximal (definition on printed p. 54). The periodic correction has magnitude at most one half. This is a fixed-law theorem; its remainder is not uniform over laws varying with `n`.

For standardized laws, that expansion implies

`lim_(n -> infinity) sqrt(n) Delta_n(P) = phi(0) (|gamma|/6 + h/2)`.

For completeness, the upper bound follows from `phi(x) <= phi(0)` and `|1-x^2| phi(x) <= phi(0)`. For the matching lower bound choose lattice points, or their one-sided limits, within `O(n^-1/2)` of zero, taking the sign of the periodic term that reinforces the skewness term. The uniform-in-threshold remainder for this fixed law tends to zero after multiplication by `sqrt(n)`. Closed-CDF conventions only determine which one-sided value occurs at a jump; both are available to the supremum. This derivation does not interchange a supremum over laws and a limit.

The [Esseen 1956 publisher record](https://doi.org/10.1080/03461238.1956.10414946) confirms the title, journal and pages 160–170. Its full moment-inequality proof was not obtained in this review. No dependence on that unavailable proof is needed for the proposed explanatory corollary:

1. A lattice support is countable and has Lebesgue measure zero. Each bounded complementary gap has length at least its maximal span `h`.
2. The density `tau` vanishes beyond the convex hull and is constant, with value `tau_g >= 0`, on each gap. Hence Tonelli and `integral tau = 1` give `sum_g tau_g |g| = 1`, including unbounded lattice supports.
3. Consequently `J = sum_g tau_g |g|^2 >= h`.
4. Reflect first if `gamma < 0`. Reflection preserves `rho`, `J` and `h`. The manuscript's gap inequality yields `|gamma| + 3h <= |gamma| + 3J <= (3+sqrt(10)) rho`.

Equality in the final moment-span inequality forces equality in the gap inequality and hence, by its existing rigidity result, the Esseen two-point law or its reflection. This is conditional only on the manuscript's previously proved gap lemma, not on a newly imported asymptotic theorem. The statement is valid for finite third moment without bounded support. Say `J=h` when every successive support gap has length `h`; do not require a two-sided infinite arithmetic progression.

## 4. Verified external inputs

### Structural Berry–Esseen bound

The primary [MathNet record for Shevtsova 2013](https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=ia&paperid=252&option_lang=rus) states the iid affine estimate with coefficients `0.3031` and `0.646` for all `n >= 1`. In its notation, standardization gives `ell_n = rho/sqrt(n)` and `tau_n = 1/sqrt(n)`, so the manuscript's input is precisely

`sqrt(n) Delta_n(P) <= 0.3031 (rho(P)+0.646)`.

The cited item is *Informatics and Applications* 7(1) (2013), 124–125. The full PDF retrieval redirected to the record; the proof of these constants has not been independently reproduced here. Retain the named external input. If a source uses strict-CDF probabilities, the same uniform bound holds for the closed CDF: let `t_k` decrease to `t`, use `P(S<t_k) -> P(S<=t)` and continuity of the normal CDF. This endpoint transfer is a direct argument.

The alternative coefficient pair `0.3322, 0.429` is also in that primary record, but changing to it enlarges the admitted moment interval. A10 remains a recertification proposal; it does not remove dependence on the same published source.

### Sharp third-moment relation

[Shevtsova, arXiv:1301.2783v3](https://arxiv.org/abs/1301.2783v3), Theorem 2 on p. 5 of the PDF, gives the equivalent relation for centered variance-one laws with prescribed absolute third moment. The v3 metadata explicitly records corrections to Theorem 2; cite that version. It matches the existing JMAA 418(1) (2014), 185–210, DOI `10.1016/j.jmaa.2014.03.075` bibliography.

Here is the algebraic equivalence independently: with `b=rho>=1` and `t=gamma^2`, the manuscript's inequality is

`t^2 + (4-b^2)t + 4-4b^2 <= 0`,

or `t <= (b^2-4+b sqrt(b^2+8))/2`. This is `|gamma| <= b A(b)` with the function in that theorem. Nonnegative sides justify squaring. The endpoint `b=1` forces `gamma=0`. Retain the manuscript's self-contained proof.

### Strict binomial theorem

[Schulz 2016, Theorem 1](https://d-nb.info/1197702695/34), printed p. 1 (PDF page 11), states, for every `n in N`, `0<p<1`, `q=1-p`,

`sup_x |F_(n,p)(x)-Phi((x-np)/sqrt(npq))| < C_E (p^2+q^2)/sqrt(npq)`.

The CDF is closed; printed p. 3 explicitly identifies the defining intervals as `(-infinity,x]`. Standardized Bernoulli third absolute moment is `(p^2+q^2)/sqrt(pq)`, exactly the manuscript's normalization. Its sharper result on `[1/3,2/3]` is also strict. Thus the existing strict finite-binomial invocation is supported. The whole-parameter proof uses Shevtsova (2013) outside `[1/6,5/6]` (printed p. 20); the two external inputs should not be described as dependency-independent. This review did not audit every step of the thesis or establish the absence of computational assistance throughout.

Independently, A7 is logically sound with the other premises retained. With only the non-strict binomial bound, positive noise still gives negative excess, and zero noise gives nonpositive excess. A least index violating `C_n <= C_E` has an attained *positive* excess and is excluded. This proves the non-strict upper statement, and the Bernoulli lower limit supplies the global supremum. It does not prove the strict finite-index statement.

## 5. Alternatives and reference hygiene

A9 requires a new floor-dependent proof and replay of all affected checks. The effective admissible threshold is at least the chosen verification floor and every revised acquisition/local-comparison threshold; it is not simply `B_*(N_1)/0.047`. A11's widened-noise proposal is not a substitute for the present local theorem. A12 needs uniform control near lattice laws, including moving laws and thresholds. A13 is not convolution with an independent noise law because the conditional noise distributions differ by Bernoulli class. Keep these speculative routes out of the theorem statements.

The numerical-computation precedent can be stated modestly. [Shevtsova 2011, Section 2](https://arxiv.org/pdf/1111.6554) reduces its bounds to finite numerical optimization using analytical monotonicity and large-index bounds. It does not document this manuscript's exact rational certificate format or furnish an independent verification of the present checker. Avoid equating numerical optimization, rigorous arithmetic acceptance and formal proof verification.

For P6/P9, the primary [He–Cheng v3 record](https://arxiv.org/abs/2609.06358v3) confirms the authors, title, 30 September 2026 version and claimed threshold `2 ceil(exp(10^17))`; this is a verified source statement, not a proof audit. [Hexagon v3](https://hexagonmath.org/2610.00147v3) is accessible and its history gives 17 October 2026, despite its header displaying the initial deposit date. Its stronger claims remain background and must not enter the dependency chain. The attempted BerryEsseenLean GitHub fetch returned a cache miss, which does not establish that the repository is absent or private. Removing an irrelevant context sentence is reasonable; asserting nonexistence is not.

Do not insert the plan's memory-based bibliography wholesale. Add only references actually used, after checking them. Neither a registry nor another LLM-generated proof supplies the mathematical justification for a replacement. The present scope decisions remain valid independently of the historical status claims in those sources.
