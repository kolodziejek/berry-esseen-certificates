# Final composition and scope review of the v11 simplification

**Outcome: no unresolved composition blocker found for the selected local
results.** They support the dependency replacements below. They do not prove
the whole sharp conjecture, a complete large-index exclusion, or `BASE41`.

This report checks the current integration README, the all-panel theorem,
left-strip construction, own-count local lemmas, and final right-panel `.03`
theorem against their actual domains. Source hashes and the README snapshot
are preserved in `runs/allpanel-review-v11-20261028/composition01/`.
The `.03` component's separate review is
`counts-v11-independent-review.md`, commit
`f0e306c` on `research/moderate-review-v11-20261028`.

This reviewer independently reviewed the all-panel **count** theorem and
read the complete own-count local proof and `.03` proof. The same reviewer
constructed the left-strip component; that is not an independent second
review of that component. The coordinator separately read the strip proof
and checker. This composition review does not repeat component executions.

## The three comparisons have different scopes

Every row assumes actual iid conditional laws, conditional mean zero,
`n>=42`, raw `|H|<=1.84`, and concludes the stated
`Delta_C<-lambda/100`.

| Comparison | Probability p | Conditional amplitude | Inward sum | Positive noise lambda | Coefficient C |
|---|---|---|---|---|---|
| New all-panel theorem | `[.25,.53]` | at most `.7` | at most `.068` | `(0,.002]` | `[0,.41]` |
| Retained v10 theorem | `[.4,.53]` | at most `.6` | at most `.072` | `(0,.02]` | every `C>=0` |
| New v11 right-panel theorem | `[.4,.53]` | at most `.6` | at most `.072` | `(0,.03]` | every `C>=.4` |

The new `.03` theorem extends the noise interval but does not supersede the
old theorem for `0<=C<.4`. The coefficient restriction is mathematically
used: the favorable cubic correction supplies `C(rho-rho_B)>s=lambda/n`.
It cannot be used on the left, where the adverse sign is realized by an exact
three-point law. The all-panel theorem instead retains an upper bound for
that adverse correction and consequently imposes `C<=.41`.

At `C=C_E`, all three coefficient requirements are satisfied. The all-panel
proof uses phase `[-.218,.782]`; the two right-panel comparisons use
`[-.272,.728]`. Their chosen anchors need not agree on an overlap. Each
theorem supplies an interior anchor, and the external Bernoulli bound applies
at every such anchor. Thus different phase conventions create no seam in the
conclusion for the actual law and raw threshold.

## The acquisition-to-count join

The selected coarse entry and direct geometry leave the closed panels
25 through 52. The left-strip result covers every panel 25--39, with
`-.6<U_0<=a_0`, `-a_1<=U_1<.7`; the previously acquired right strip covers
40--52 with the stronger common amplitude `.6`. Their closed intervals meet
at `.4`; there is no probability gap. The geometric theorem gives
`a_0+a_1=d<.068` on all these panels, stronger than the right theorem's
`.072` premise. Actual endpoint exclusions do not require deleting endpoints
from the sufficient count domains.

Both modules use one physical law and the same scale:

`U=(X-E[X|B])/ell`, `s=E U^2=theta/ell^2`,
`lambda=ns=n theta/ell^2`, `ell=(pq+s)^(-1/2)`.

The inward parameters are `a_0=p-A_-/ell`, `a_1=q-A_+/ell`; their sum is
the geometric displacement. The independent retained threshold bound
`|H|<=1.83605680` is stronger than `1.84`. This is a raw sum threshold,
not its normalized version `H/sqrt(n)`. No earlier signed phase resource
is needed to choose the new anchors.

The support-strip acquisition still requires an attained fixed-target
witness, nonnegative excess, actual `n>=42`, the sharp predecessor and the
retained heat/ray theorem. Its finite boundary checks extend along whole
rays. Neither the geometry arithmetic nor the local count theorem removes
those acquisition hypotheses. No completed count conclusion is fed back as
an input to its own support acquisition.

At `lambda=0`, conditional noise vanishes and the actual law is Bernoulli.
Schulz's strict finite-n theorem handles that endpoint directly. At positive
noise the count proofs remain uniform down to zero; no additive remainder
independent of noise is hidden at the join. Negative discrepancies retain
the original reflection-and-attainment argument. A signed ray of one law
must not be replaced by an unjustified symmetric acquisition for `1-p`.

## What the own-count lemmas add

The own-count moment bound keeps the two conditional variance totals in
`EW^4-kappa EW^3`. Its endpoint-maximization proof and the subsequent
quartic expansion are valid with the stated support caps. Combining the
marginal cubic before bounding it gives the correct two modified coefficients
and multiplicities. These are complete local inequalities.

The reduction of the variance-allocation coordinate to its endpoints requires
that the support caps, quartic and Chernoff tilt remain fixed while allocation
varies. The own bound is then concave and the incoming exponential sum convex.
The sufficient geometric-ratio condition is explicit. A pointwise minimum of
incoming bounds or insertion of the favorable finite-sum correction need not
preserve this argument. The optional fixed-variance majorant likewise requires
its own sign condition and a new curvature check before insertion.

The illustrative improvement at noise `.075` is realized by an actual law,
but is only one point. The normal-slope estimate through `.075` is also a
local ingredient, not a count exclusion. The current `.03` theorem does not
depend on these still-unclosed endpoint comparisons or on compound-Poisson
discovery. Keeping the local tools separate is correctly reflected in the
integration README.

## Exactly what can be omitted

For an acquired witness in one of the proved count domains, the direct
conditioning/quartic/tail proof replaces separate half-amplitude acquisition,
fractional-part or harmonic gain, marked crossings, and count curvature.
This is a domain-specific substitution. The first two tail probabilities may
be treated separately, and the remaining infinitely many scalar bounds are
summed analytically; no unverified finite tail truncation is introduced.

The quadratic-hinge Poisson comparison is still an explicit external input.
It is incorrect to describe the new comparison as removing all Poisson
arguments. Likewise, none of these substitutions removes the coarse Fourier
cover, actual-law/contact reduction, predecessor, attainment/reflection, or
the finite base. The earlier eight-round moment iteration was replaced only
for the named v10 exports and checked consumers; arbitrary unlisted old panel
bounds still require their own comparison.

The final `.03` proof explicitly requires positivity of the **unsquared**
hinge-domain parameter before dividing by its square. Its six closed phase
intervals meet at `-.075`, `0`, `.075`, `.1`, and `.2` and cover the whole
shifted interval. The stronger moment repair retains the essential `1/n`
factor. The final checker includes an explicit control rejecting omission
of that factor. These were the two wording points checked during integration;
both are resolved in the pinned final files.

## Explicit unresolved boundary at the sharp constant

At `C=C_E`, after acquisition:

- zero noise is covered by the external Bernoulli theorem;
- every retained probability is covered for `0<lambda<=.002`;
- the right range `[.4,.53]` is additionally covered through `.03`;
- the left range below `.4` above `.002` remains unclosed;
- the right range above `.03` remains unclosed.

The upper limits of those remaining intervals are the actual retained panel
budgets, not arbitrary new constants. The local variance-allocation tools do
not yet close them. The complete finite base below 42 is still an independent
obligation. Hence a least contrary index does not supply every missing premise,
and none of these results establishes `C_n<C_E` for every `n>=42` without
the remaining count and finite-base work.

## Status and recommendation

| Review item | Mathematical status | Execution status in this composition review |
|---|---|---|
| Same-law scaling and numerical premise joins | Checked directly | Exact rational joins and closed interval covers checked |
| All-panel count theorem | Independently reviewed earlier in this branch | Existing source-pinned review evidence retained; no rerun |
| Right-panel `.03` theorem | Read in full; separate independent review found no blocker | Its review and final source hashes read; no component rerun |
| Own-count local lemmas | Complete proof read; no scope mismatch found | Component evidence not relabeled as a new complete count cover |
| Global closure or `BASE41` | Not established | No acceptance claimed |

Recommendation: integrate these as scoped research reductions and retain the
old `.02` result at its broader coefficient scope. The README's selected
claims and dependency removals are consistent with this recommendation.
Compilation and actual-law controls support reviewability; they do not replace
the analytic implications or the identified external theorem inputs.
