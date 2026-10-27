> Integration note, 27 October 2026: this is the original drafting contract. The
> Fourier, finite-index, retained support and signed local-comparison appendices
> have now been incorporated. See `manuscript-review.md` for the delivered
> coverage map and remaining scope gaps. Inclusion is not independent acceptance
> of the entire supplied analytic chain. The review of the new core is recorded
> separately in `core-review.md`.

# Analytic coverage for the first manuscript draft

Branch: `manuscript/analysis-20261027`. This is a map of the analytical
content, not an assertion that inclusion of a source proves its numerical
premises. The three new section files have no preamble and use only the
standard AMS theorem environments plus `\CE`, `\E`, `\Pp`, and `\R`.
All new labels begin `ms:`. There are no unverified external citations in
these sections. The coordinating manuscript must provide its definitions,
theorem environments, bibliography and compilation/visual inspection.

## New core proofs

| Statement | Manuscript location | Mathematical status | Execution status |
|---|---|---|---|
| Positive closed orientation, fixed-index attainment, equality included | `sections/02-extremizers.tex`, `ms:attainment` | Locally derived; ready for independent review | No certificate needed; no native program run |
| Raw contamination contact, all closed support points, compactness before higher moments | Same, `ms:contact`, `ms:contact-majorant` | Locally derived with atom-safe event and dominated moment derivative | As above |
| Gaussian transform/norm bounds, exact elementary bounds on `CE` | `sections/03-smoothing.tex`, `ms:gaussian-constants` | Full analytic derivation; finite rational comparisons explicitly specified | Uses the same exact constants previously checked in scalar/resource work; no new native run |
| Support-free one-step recurrence, all `n>=2` | Same, `ms:one-step` | Full spatial Taylor and variance-heat proof | No support or certificate input |
| First-failure42 bounds, weak predecessors, zero same-law decrement | Same, `ms:first-failure-entry`, `ms:least-contrary` | Proved scalar implication; global conclusion conditional on base and exclusion | No LOCAL42 arithmetic run |
| One-marginal sign split, conditional moments, physical/count units | `sections/05-geometry-counts.tex`, `ms:bernoulli-coordinates`, `ms:conditional-moments` | Exact identities; zero atom kept in nonpositive class | No numerical predicate |
| `tau`, nonnegative physical defect, central-gap license | Same, `ms:physical-defect` | Full signwise Tonelli and gap decomposition proof | No numerical predicate |
| Simultaneous binary/endpoint/noise resource | Same, `ms:simultaneous-gap` | Full conditional cubic expansion and square identity | No numerical predicate |
| Weighted `nD` joint plane, negative/zero residual branches | Same, `ms:joint-resource` | Proved conditional on explicitly stated same-law incoming bounds | Acquiring those incoming bounds remains separate |
| Count mixture, strict outgoing and closed incoming events, master score identity | Same, `ms:count-identity`, `ms:master-identity` | Exact same-marginal derivation, both probability halves | No numerical predicate |
| Nearest-count and whole-count final implications | Same, `ms:local-witnesses` | Explicitly conditional on analytic event/repair bounds; no hidden score acceptance | Numerical gates not run |
| Whole-count cutoff, discrete curvature and three crossing moments | Same, `ms:whole-count-cutoff`, `ms:crossing-curvature` | Full proofs; retains `chi<2`, gap, bounded residual and normalization conditions | No marked-count/LOW gates run |
| Common-marginal tensor expectation, Bernstein implication, finite closed-cover soundness | Same, `ms:certificate-expectation`, `ms:closed-cover` | General full proofs | Specific polynomials, coefficients and coverage predicates remain numerical inputs |

Notation is deliberately fixed: `rho=E|X|³`, `beta=EX|X|`, `gamma=EX³`,
`H` raw, `z=H/sqrt(n)`. The physical span `ell=m/(pq)` gives
`X=ell(B_0-p+U)`; the reciprocal `h=pq/m` used in some original sources is
not silently substituted for it. The count threshold is named `x`, not `z`.
Compactness in attainment uses uniform integrability only of first and
second moments. Third-moment convergence follows from extremality.

The contact proof is unconditional at the unrestricted fixed-index
maximizer; it is not introduced as an assumption. The physical defect
inequalities are proved for a compactly supported law. The numerical
radius and all upper budgets for this defect remain separately acquired.
The coordinator supplies the sharp third-moment and signed-second-moment
inequalities in a dedicated appendix, so they are not duplicated here.
The zero-noise reduction is proved, but the all-parameter Bernoulli bound
and its strictness are an external analytic input requiring exact source
verification. No citation is fabricated to fill that input.

## Analytic material still required in the manuscript

The following table identifies what must be included as mathematical
appendices if the article is to contain all analytical arguments of the
proposed route. These are **analytical proof obligations**, not clauses of
an opaque “all certificates pass” assumption. Source ranges are actual
one-based lines in the preserved `paper/analytic-supplement.txt`, rather
than the older `M...` numbers printed in its index.

| Retained analytic obligation | Candidate text to incorporate | Required treatment |
|---|---|---|
| Characteristic-function bounds, exact half-line/Prawitz interface and licensed smoothing | S1:92–211; S3:808–1218; A1:7913–8211 | Include definitions, frequency/domain restrictions, endpoint convention, scalar-cosine predicate and complete tails. Preserve external Prawitz/Shevtsova input status until the exact theorem is verified. |
| Conserved contact/defect identity and its Fourier error ledger | S3:1219–1507 | Essential for the resource phase inequality. Includes the two slack integrations, half-open leakage measure, compensated inversion and every term of the identity. The new main-text `D>=0` proof replaces only1253–1315, not the conserved identity. |
| Complete LOW/HIGH Fourier remainders | S3:1508–2236 | Include the entire small-frequency/large-frequency analysis and infinite tail, all positivity/damping domains, and the compensated supported variant. No numerical frequency truncation grants a Kolmogorov inequality. |
| Gaussian-weight removal, score update, conserved phase curvature | S3:2237–2287 | The resource inequality used by the score-excess reduction must be derived here from the conserved identity. Its initial sign license, `CE rho>2/5`, `phi(0)>997/2500`, weighted `nD`, and single use of the phase charge are essential. |
| General enclosure operator, coefficient atlas and signed phase feedback | S3:2485–3900, together with A3:8253–8298 where selected | Core main geometry replaces2289–2484. Keep required actual-moment, paired-domain, sign-corrected curvature and feedback ordering. Fixed schedule tables are numerical targets, not independent proofs of their truth. |
| Parameterized strict-gap confinement, both deleted laws, full exterior rays and one-resource error pricing | S8:6529–6946 plus the proved floor42 specialization in `mathematics/simplification/2026-10-27/uniform42.md` | The source literally begins `N=47`, strip `.55`. A LOCAL42 appendix must supply the actual substitutions, including LEFT strip `.575`, third-moment coefficient30, deleted floor40, strict interval widths and slope signs. Do not relabel the old statement unchanged. |
| Finite-binomial normalization, Gaussian/cubic repair, outgoing and incoming probability tools | S8:7197–7473; A0:7777–7904; selected finite42 signed refinements in the source ZIP | Prove all reciprocal-domain and sign gates. The main master identity and final conditional witness theorem do not establish these estimates. Include closed-event and strict outgoing conventions. |
| Marked crossing and harmonic/Poisson remainder leading to the actual LOW expression | S8:7512–7690 | The new main text supplies cutoff/discrete curvature/crossing moments at7474–7511, and the new curvature chapter supplies the exact supremum/clamp. The marked pair coupling, same deleted marginals, tail estimates, harmonic gain, repair and frozen-coefficient argument still require this appendix. |
| All-parameter zero-noise and Bernoulli reference comparison | Elementary reduction in new main text; external theorem cited in original S8:7758–7770 | Verify and state the exact external finite-binomial theorem, including its range and strictness. The old `n>=47` application is not the scope of a new theorem. |
| Exact finite42 phase/noise cover and signed refinements | `mathematics/simplification/2026-10-27/local-cover.md`, original ZIP `proofs/local42_improvements.tex`, `local42_signed_gaussian_v2.tex`, `signed_cubic_repair.tex`, contracts and numerical predicates | Include the mathematical sign/convexity/zero-noise arguments. Use the actual finite42 seams and any newly proved row-pruning contract, not the old tail47 table. |

The phase budget's incoming defect inequality and the whole-count local
estimate are explicitly conditional in the new core. To close those
conditions analytically, the appendices must supply the preceding chains.
The new support, exact curvature, retained-score resource and conditional
global composition chapters are owned by the coordinator and must be joined
to these inputs using their actual hypotheses.

## Material to omit or separate from the new all-index composition

- Do not import old S2 finite fifth-heat support schedules316–718 as if they
  remained needed by the new elementary support theorem. The contact proof
  at218–315 is now written out in the core. Retained strip tests719–803
  may still be needed by acquisition and must not be dropped merely because
  the radial support proof changed.
- Omit the obsolete strong46 assembly6947–7098 from the LOCAL42 propagation
  argument. Its proof is not a prerequisite of the new least-first-failure
  composition.
- Do not use the old tail47 selected cover and constants7691–7757 as the
  finite42 cover. They use different probability intervals, phase seams,
  amplitude profiles and floor. The Bernoulli endpoint argument after it
  remains relevant only at its separately verified analytic scope.
- S5's increasing induction and the old S7 tail assembly are replaced by
  the new equality-inclusive least-index proposition. The base premise is
  still a genuine sharp prefix, not its old positive-ceiling surrogate.

## Finite-base chapters: explicit candidate status

If the first manuscript is to present the prospective finite-base route as
well as the LOCAL42 propagation reduction, it needs the relevant analytic
reductions from S4:3996–4513 (conditional moment contractions, physical
halfplanes, strict outgoing bounds, incoming exponential and stop-loss
tools, common cubic moments) and S6:4666–6469 (two/three-summand certificates,
ROOT4 localization, one-free C5). The general expectation/Bernstein/forest
arguments are already in the new core, but they do not verify these
particular majorants or the full unrestricted fourth-index reduction.

The remaining currently selected finite-range adapters are A0, A1 and
A3–A18 as applicable to their named producer family. In particular A14–A18
contain weighted floor transport and active overrides; dropping them while
keeping the affected numerical predicates would leave an analytic gap.
A2's old far-ray Gaussian bound is not automatically retained if the new
support theorem supersedes the corresponding use. Inclusion of a source
candidate in an appendix must keep its literal hypotheses and any unresolved
proof or provider issue visible. No section title such as “an unrestricted
bound” is evidence that the sharp base is established.

## Review and typesetting boundary

These files form a coherent main-text analytic draft, with full proofs for
their stated propositions. They do not claim that the whole-manuscript
analytic coverage is complete until the required appendices above have
been incorporated and their hypotheses reconciled. No certificate or
expensive inherited driver was run during drafting. The coordinating
root owns the combined preamble, full compilation, equation/page inspection,
and subsequent independent review; this worker has not represented a
fragment-only compilation as a compiled complete article.
