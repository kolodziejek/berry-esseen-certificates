# Shifted count anchor: analytic audit and replacement

Starting state: `00ba714897f2e09995d78354ac3c8931e257cd05`.
Worktree: `counts-v10`, branch `research/counts-v10-20261028`.
No manuscript, inherited proof object, production program or external service
was changed. This report concerns Astra's sections 3–4, treated as proposals.

## Result

**Mathematical status:** the proposed shifted anchor, extended curvature,
third-crossing coefficient and Bernoulli-slack criterion are valid with the
additional domain bookkeeping proved in `counts.tex`. The general curvature
argument remains valid on any phase interval inside `(-zeta,zeta)` for
`0<zeta<=1`; the old `|u|<=1/2` and `chi<2` restrictions can both be removed.

**Execution status:** fresh exact bounded controls passed. They do not
constitute a complete count-comparison cover. The same-law support premises
and all quantitative comparison inequalities are still necessary.

With amplitude `A=3/5`, inward displacement `d0=9/125` and increment
`zeta=116/125`, choose phase `[-34/125,91/125]`. The individual mark distances
are at least `16/125`; optional common-mark distances at least `7/125`;
conditional spans are at most `84/125`; fourth-moment tail denominators are
`124/125` and `181/125`. Thus a `.6` strip suffices for those domains.

The exact cubic-crossing coefficient is `1953125/7739786`. It is attained
at integer `j=3`, after checking `j=2,3`; using only `j=2` would be wrong.

## Hypotheses behind each replacement

| Existing source | Replacement and reason | Still required |
|---|---|---|
| `sections/05c-counts.tex`, exact count/master identities | Any integer anchor; the algebra never uses nearest-integer optimality | Legal/interior count, actual common marginal, strict outgoing and closed incoming events |
| Same source, discrete curvature, `chi<2` | Replace `(chi-1)+` by `T(chi)=sum_{j>=1}(chi-j)+`; double-sum weights are bounded by total displacement | Actual binomial mass/normalization and zero extension |
| Same source, three crossing moments | Extend phase to `(-zeta,zeta)`; retain correct lower endpoint in the cubic coefficient | Positive denominators, independent centered conditional summands, absolute amplitude bound |
| `sections/07-curvature.tex`, three-candidate phase supremum | The same candidates work for general T: active positive-crossing terms are convex; below zeta/3 the other second derivative is positive whenever T>0 | `0<zeta<=1`, phase interval strictly inside `(-zeta,zeta)` |
| `appendices/count-comparison.tex`, marked crossing | The pathwise floor argument uses no half-phase or half-amplitude assumption; both deletion conventions rederived | Individual tail distances positive; optional shared-deleted-sum method needs its stronger distances |
| Same appendix, tiny-noise negative phase | Replace the far-end `r=1/2` gate by the actual negative endpoint magnitude | Quartic, switch derivative, endpoint and own-count variance gates |
| Same appendix and `local42-refinements.tex`, Gaussian bounds | Derivative estimates hold for any finite phase interval when the actual count is fixed | Recomputed displacement/phase constants and positive derivative bounds |
| Same appendices, binomial ratio | Old `p_++Delta<2` shortcut may fail after the shift; use mode-mass/own-mass ratio or a new product bound | Positive lower own mass and valid upper mode mass |
| Same appendices, probability below one half | Replace p by min(p,q) in variance and cubic lower bounds; use absolute Stirling derivatives across one half | Sign separation `d0<min(p,q)`, signed multiplier direction for a negative cubic bracket |
| `sections/05c-counts.tex`, strict negative RHS witness | Allow comparison error up to the explicit strict Bernoulli gap | Schulz Theorem 1 with its exact probability domain; complete new scalar cover |

The first-mark condition for the centered shifted interval is
`A+2d0<1`. The optional common-mark shortcut needs `A+4d0<1`; it is not a
consequence of the first condition alone. Both hold for `.6,.072`.
The first condition also ensures harmonic span below one. This changes the
analytic interface but does not assert favorable numerical constants.

The whole-count mark choice `eta=z*lambda` and its bound
`G^2<c_v*N*L` still require a positive lower noise endpoint. A quartic or
another genuinely relative-noise argument remains necessary at zero.
The coordinator is independently pursuing such an argument.

Schulz's primary source is
[The optimal Berry–Esseen constant in the binomial case](https://d-nb.info/1197702695/34),
Theorem 1, printed page 15, equations (4)–(5). The coordinator checked that
source in this research turn. Its strict finite-index conclusion removes
the manuscript's separately unresolved Bernoulli strictness premise. It
does not resolve the non-Bernoulli comparison or finite all-law base.

## Fresh checks

`counts_check.py` uses exact fractions and no constructor imports:

- 6,025 discrete-curvature cases, including 1,956 with `chi>=2` and counts
  extending outside the legal range;
- 720 actual conditional-law cases at `n=3,4`, including probabilities above
  one half, deterministic components, tiny inward displacement and rare
  outward atoms;
- 37,044 pathwise marked inequalities and 894 own-count atom collisions;
- exact equality of the original iid convolution and coupled binomial CDF;
- all-p cubic lower bounds and the three crossing moments;
- 24,600 rational-grid regression points for the independently proved
  three-candidate supremum. These sampled points are explicitly not a
  continuous-domain certificate.

Four negative controls expose the old nearest-phase mark obstruction,
the false single-j cubic coefficient, invalid use of `(chi-1)+` at general
chi, and a changed closed/open atom convention. No claim that an arbitrary
feasible moment vector is an iid law is made.

Evidence: `runs/counts-v10-20261028/check01/`, with stdout, stderr, command,
return code, Python version and source hash. The full proof fragment was
compiled with TeX Live; its five-page standalone review build has no warnings
and all five rendered pages were inspected. Evidence is in `build01/`.

## Decision

Proceed with shifted-anchor comparison and Bernoulli slack before extending
the harder half-amplitude proof. It can remove that support target from a
domain-complete comparison once the corresponding scalar inequalities are
proved. At this checkpoint it removes the domain obstruction, not the
remaining whole-domain comparison obligation. Existing confinement results
and certificates should remain preserved.
