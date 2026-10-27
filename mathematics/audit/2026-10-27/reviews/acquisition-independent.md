# Independent review of acquisition and exclusion interfaces

Reviewed head: `ac7bd069c9d5afe6d0dfe5a9c86c9a095644ff99`.
Source baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
Review branch: `audit/review-acquisition-20261027` in
`kolodziejek/berry-esseen-certificates`. Date: 27 October 2026.

The reviewer did not author `acquisition-review.md`. This review treats that
report and `AUDIT.md` as claims to test, not as evidence of their conclusions.
It independently reads the source statements and selected native program
semantics. It does not independently establish the entire analytical LOCAL47
theorem or accept any of its numerical proof objects.

## Recommendation and findings

**Recommend merging the audit-only additions.** No blocking acquisition or
exclusion interface mismatch was found in the proposed conditional
least-counterexample substitution. This recommendation does not approve a
production assembly change, certificate removal, theorem weakening, or a claim
that LOCAL47 has been newly verified. The finite base and the complete
analytical/numerical acquisition and exclusion premises remain assumptions.

| Finding | Severity | Disposition |
|---|---|---|
| No new invalid dependency removal or missing scalar hypothesis found in the examined substitution | No blocking finding | The report correctly retains the support, resources, sign repairs, confinement and complete comparison cover |
| Baseline `paper/main.tex:163` misnames the normalized-score derivative as `rho I(y)` | P3, already reported | Independent differentiation confirms `I(y)` under lines 148–153; positivity of rho preserves every sign and zero-set inference. Preserve the separate proposed correction |
| The archive contains two different `global_route.tex` members, and its coverage object contains an older global-assembly scope string | Informational provenance caution | Use the exact root member identified below. The old assembly string does not override the explicitly all-index local theorem or license an old global run for a new assembly |
| Full analytic soundness and complete native acceptance remain outside this review | Retained proof obligations, not a new defect | The source reports must continue to be classified as supplied/conditional at this boundary |

No change to the audit's central verdict is requested. In particular its
strict-tail statement is valid only as a *separately stated conditional
composition*, using equality-compatible acquisition and exclusion. It is not
an automatic strengthening of the least-`>` argument.

## Source notation and integrity

`M` means `paper/main.tex`; `S` means `paper/analytic-supplement.txt`.
Numbers below are physical one-based file lines at the source baseline.
`Z` is `verification/finite-tail/sources/BE_cutoff49_20260930.zip`.
`R` means the archive prefix `BE_cutoff49_20260930/`.
`B` means the longer archive prefix
`BE_cutoff49_20260930/baseline/certificates/work/below50_20260929/`.

Fresh read-only identification reproduced:

- Z: `ecdb9acca0db29efc9fe2bf496c0bcc61b4881aecdcbc91a4eb6ad49b920c72e`;
- `R/paper/sections/global_route.tex`:
  `6c1715274ef031db7558070ea9f3540cd72df2e2a6a87282828cf04c75b6dfa2`;
- `R/paper_entry/resource_entry.tex`:
  `7912da195c21455eeb3fcb1a023c1fa597c7989e925a9599af83fe82bc3dd60a`.

These match the audited identifiers and establish byte identity only. A Git
comparison found no change from baseline in M, S or Z. The archive also contains
`R/baseline/paper/sections/global_route.tex`, an older four-loss/cutoff50 version.
It is not the root member above. Suffix-only file selection would be ambiguous.

## Independently checked interface chain

### Owner, orientation and scalar allowances

M:102–142 selects a fixed-index, positive closed maximizing pair, including
`C_n=C_E`. The compactness proof preserves first and second moments using
bounded third moments, applies closed-set Portmanteau at moving thresholds,
then derives equality of the limiting third moment from extremality. It does
not require unjustified third-moment uniform integrability. The positivity
needed for this argument is `C_n>0`, which holds also at `C_n=C_E`.

M:148–171 derives contact for the same law and raw threshold. Directly
differentiating `sqrt(n) v(epsilon)^(3/2) D(epsilon)/r(epsilon)` gives the
right side of M:148–151 divided by rho, namely `I(y)`. Thus the normalization
prose error at M:163 is real but does not affect contact's sign or equality
on closed support. No density approximation of the indicator is used.

M:173–196 defines `q_n(P,C)=n(R_(n-1)(P)-C)_+`. Therefore
`R_(n-1)(P)<=C_(n-1)<=C_E<=C_n` implies `q_n(P,C_n)=0`, as well as
the separate global decrement `n(C_(n-1)-C_n)_+=0`. This establishes no
zero-noise or zero-physical-defect claim, and requires no predecessor
optimizer or contact statement.

The root `global_route.tex:81–115` literally states exclusion for every
integer `n>=47` with `0<=C_n-C_E<=.7/n`, decrement at most `.19`, own cap
`C_n<.4247`, and both deleted caps `<.4253`. The root
`resource_entry.tex:402–420` uses the corresponding non-strict numerical
caps and expressly says there is no upper bound on n, conditional on the
support implications and checked schedule. Thus the first-counterexample
scalar caps are stronger than the stated entry hypotheses. At n=47 the two
deleted indices are 46 and 45, both inside a base through46.

### Support and initial resource license

S:583–602 obtains coarse moment information from published finite bounds and
the current condition `C_n>=C_E>.4095`, before quantitative bounded support
is used. S:642–650 has six radius-3.84 index bands, the last being
`[200,infinity)`. The infinite band sets the favorable `D_-` term to zero
(S:566–581). The complete radial cells and the exterior rays in S:631–640
remain necessary; the first-counterexample argument does not delete them.

S:719–757 requires the excess bound and decrement again in radius/strip
refinement. Its nonnegative remainder terms decrease with n, and the
first-counterexample `.3/n` excess meets its `.7/n` premise. S:765–774 also
requires a nonnegative beta lower bound and checks equal-endpoint singletons.
None of these requirements is replaced merely by zero predecessor loss.

The first unweighting license is strict: S:2238–2257 and
`R/paper_entry/resource_entry.tex:64–83` require a prior raw bound below
`2N/5`. Inspection of `B/entry/accept_initial47.py:22–61` confirms that its
recorded stage shape retains `0<raw<.4*47`, a complete signed count, ordered
feedback, and a complete 100-panel export. Those tests were not executed.
The raw bound is not licensed by assuming the desired improved defect.

### The apparent upper index 98

`B/entry/accept_initial47.py:12` fixes `n=47,nmax=98,barrier=0`.
Direct source inspection found precisely two occurrences of `nmax` in
`B/entry/local_signed_core.py`: line 22 checks the calculation-floor ordering;
line 29 forms `.4095+K/nmax`. Neither immediate imported module
`high_window_core.py` nor `kernel.py` contains `nmax`. At K=0 the second
expression is `.4095`; no actual-index upper endpoint survives there.

This confirms the audit's narrow claim, not all of its uniformity premises.
Every use of the fixed numerical floor still needs its analytic monotonicity
gates. Those remain explicit in `R/paper_entry/resource_entry.tex:304–338`
and :414–419. In particular :245–253 exports weighted `n theta`, `n d_Y`
and `lambda` from weighted `nD`. Multiplying an unweighted theta bound by47
would be invalid for an unbounded actual n.

A useful negative boundary check is K>0: a hypothesis
`C_n>=C_E+K/n` for n>98 does not imply `C_n>=C_E+K/98`.
Thus the same explanation cannot be reused unchanged for a positive-barrier
certificate. The audit explicitly preserves this distinction.

### Phase sign and ordered feedback

The early paired resource formula really needs its sign correction.
`R/legacy_phase/corrected_phase_callback_v2.py:15–25` changes curvature to

    C*rho + min(phi_low*g0, .4*g0)/2,
    g0 = 3.16*rho - 3 - d.

This is a valid lower bound for the gamma contribution for both signs of
g0: when g0 is negative, the upper density endpoint is required.
`accept_phase_corrected_v3.py:21–33` checks PREP and the complete complement
and compares every surviving resource, not just the number of exclusions.
These are still acquisition consumers even if strong46 is bypassed.

`R/legacy_phase/check_later_phase_premises.py:17–55` uses a signed-third-moment
lower bound on six preceding input families (302 domains), with common
support radius at most3.84, to license the later uncorrected lower-density
choice. If actual gamma is positive but g0 is negative, the bound remains
valid because `phi*gamma>=0>=phi_low*g0`; if g0 is nonnegative, the ordinary
product lower bound applies. This is separate from the Fourier-only
reflection in `resource_entry.tex:341–355`, which may bound absolute gamma
but may not reflect the actual contact and phase data independently.

The claimed C1/C2 dependency order is borne out by the actual inputs:

- `B/entry/accept_confined_feedback47.py:34–48,58–75` binds confinement to
  `conditional_input47.json`, then refines those original C rows.
- `B/local/sperner47_contract.py:8–35` and `accept_sperner47.py:19–37`
  bind the antichain confinement to that same original C table.
- `B/entry/accept_sperner_feedback47.py:34–49,59–76` separately binds the
  original C table, its antichain certificate and the C1 feedback table;
  only afterward does it compute C2.

This is acyclic. A stored hash or a shape check is not itself a proof of the
referenced confinement; its separate acceptance remains necessary. The root
schedule's optional further central S refinement is not required by its
selected C2 local comparison (`resource_entry.tex:397–400`).

### Confinement, strict resources and complete local cover

S:6533–6618 requires the actual conditional decomposition, inward endpoints,
the initial strip, `.4<C<=.4253`, simultaneous acquired panel fields, the
contact derivative, both deleted-convolution concentration estimates, and
one common strict resource budget. Earlier sharp suprema supply both score
caps; none of the other hypotheses follows from that fact alone.

The antichain branch at S:6621–6686 uses interval diameter **strictly** below
the conditional-label gap and the correct deleted floor `n-2>=45`.
The strictness matters even for a Bernoulli variable: the closed interval
containing both its atoms has probability one and is not bounded by its
largest atom. The examined `sperner47_kernel.py:23–41,57–77` retains strict
width, mode, denominator and resource gates; `accept_sperner47.py:23–33`
requires positive gates and complete sign/phase/noise coverage.

Strict resource export is a retained input, not a result of the scalar
argument. S:2579–2581 and root `resource_entry.tex:333–335` explicitly require
a strict Fourier or target gap before exporting strictness. S:7691–7710 and
root `resource_entry.tex:422–439` then permit exclusion at `G=0` because
`n d_Y<G` is strict. Replacing it by a non-strict resource bound would not
justify that boundary exclusion. The audit keeps this requirement.

The local interface at S:7107–7197 requires positive conditional probabilities,
centering, support amplitude, `d0<min(p,q)`, a legal interior nearest count,
positive binomial mass, and the signs of the chosen comparison witness.
The TINY normalizer explicitly checks interior counts and mass positivity
(`B/local/tiny47wide_normalization.py:25–35`); its scaled comparison has
positive-noise domain and explicit rescaling gates
(`tiny47wide_kernel.py:69–84`). It is not a fixed additive error argument.

S:7712–7755 does need the extra positive-left LOW domain in the fourth noise
band. `B/local/final_review/check_local47_coverage.py:81–120` preserves it,
clips each family to the acquired noise ceiling, checks the shared p=.38
seam, and includes zero-noise/ceiling singleton representatives. Its
`prove_cover` routine (:38–51) uses all rectangle endpoints and one point
per intervening open interval; for unions of closed rectangles this is a
finite partition argument, not sampled positivity. Its call at zero labels
the Bernoulli branch separately and does not apply TINY at lambda=0.
The fixed arithmetic acceptance of each component remains a separate
dependency, as the coverage module itself says at line1.

Finally, S:7757–7768 and root `global_route.tex:98–105` separately treat zero
noise. Since `lambda=n E U^2=0` and p,q>0, both conditional noises vanish.
The finite-binomial upper theorem then bounds the actual law directly.
For positive noise the signed comparison is with the same binomial law;
its signed score is bounded by that law's Kolmogorov score. This review
retains the external finite-binomial theorem at its stated strict scope;
it did not reverify the publication.

The coverage module's return at line127 still describes an older global
descent using47..98 and a prior99 tail. Its immediately preceding sentence
states the local comparisons hold for n>=47. The new root global-route
member separately supplies the all-index local statement. The historical
assembly string is not an additional local upper-index hypothesis, but must
not be used as a completed run receipt for a redesigned global assembly.

## Consequences and verification limits

The independently inspected interfaces support the two conclusions actually
claimed by the audit:

1. With a genuine weak sharp prefix, a first strict violation supplies all
   scalar gates of the retained full LOCAL47 implication, so the independent
   strong46/three-loss bootstrap is conditionally unnecessary for that new
   global *assembly*.
2. With the equality-inclusive interface, choosing the least `n>=47` with
   `C_n>=C_E` gives the separately named strict tail. Choosing the least
   `C_n>C_E` alone does not do so.

Neither conclusion identifies a physical certificate that can be deleted.
In particular none removes the corrected phase jobs, the full acquisition
schedule, strict resource bounds, confinement, normalization, TINY/MID/LOW
coverage, or the zero-noise theorem. The independent-tail theorem remains
an independent product with its original proof obligations.

| Reviewed claim | Mathematical status after this review | Execution status |
|---|---|---|
| First-counterexample hypotheses meet the literal acquisition/exclusion interfaces | Independently checked conditional applicability | Source inspected; no native acceptor run |
| Equality and n>=47 are allowed at the identified interfaces | Independently checked source scope, with retained uniformity/strictness gates | Source inspected; no native acceptor run |
| Complete LOCAL47, finite base, or global conjecture | Supplied/conditional here; not established by this review | Not run |
| Archive/source identity | Byte identity only | Fresh read-only hashes and Git comparison |

Actual work consisted of reading M/S, reading archive members with the Python
standard-library ZIP reader, inspecting the named script text without import
or execution, rederiving the interface implications above, and checking source
identity. No inherited driver, numerical certificate, mutation suite, package
installation, network operation, or campaign was run. No benchmark or measured
computation saving is claimed. Only this new review report is added.
