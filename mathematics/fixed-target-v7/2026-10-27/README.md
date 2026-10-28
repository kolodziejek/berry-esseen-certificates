# A shorter coarse acquisition, with a proved Fourier bound

This continuation closes a substantial intermediate task, not the sharp conjecture. Starting from the fixed-target contact/support entry and the two simple quadratic passes from v6, four signed passes meet all five numerical targets of the older coarse initialization. The selected route does not use an unknown-score cap, the degree-six phase routine, or the six intervening v6 HIGH updates.

The new object is named **INITIAL42_FIXED_TARGET_COARSE_V7**. It does not impersonate the older INITIAL42 acceptance contract. The original certificates, targets and drivers remain unchanged. BASE41 and a complete ordered confinement/count exclusion are still separate obligations.

## What makes the reduction work

The physical defect already implies `m >= (sqrt(10)*rho-gamma-D)/6`, where `m=E X_+`. Combining this with `4m^2+beta^2<=1` contracts both the first moment and the signed second moment in each same-law box. The earlier signed calculation used the defect only to restrict an upper envelope and missed this lower-mean feedback. Feeding it back removes the artificial freedom that kept high-rho boxes alive. Per-cell support radii are acquired by the existing contact/heat proof before being used in moment and Fourier bounds.

`signed-transport.tex` gives the scalar argument, including the fixed coefficient, density license, phase price, weighted nD bound, signed roots, gap distance and coverage order. The selected proof uses four signed passes after the two coarse quadratic passes. The last two signed passes in the discovery trace are optional and not required for the acceptance targets.

## Quantitative result

After the selected four passes:

- raw remainder <= 2.1995174 < 2.24;
- floor-scaled defect <= .76682509 < .784, hence `nD <= 42*.76682509` for all `n>=42`;
- rho <= 71527/48000 = 1.490145833... < 1.526;
- |beta| <= .50549963 < .523;
- |H| < 1.83605680 < 1.947.

There are 14 surviving rho cells out of the original closed 24-cell cover. The four signed passes evaluate 11264 nominal boxes in total, with at most 3072 per pass. The 100 closed probability panels retain all incidences and simultaneous resource/moment bounds. A discarded cell requires a recorded necessary-condition contradiction.

The optional six-pass discovery result is raw <= 2.14458615 and D <= .74519531, with the same rho ceiling. These stronger figures are not necessary for the selected proof.

The original `accept_initial42.py` prescribes twelve 18432-box stages and one further 18432-box export evaluation, or 239616 signed boxes. The new named coarse component requires 11264 signed boxes plus its separate small initial quadratic calculation. This is a comparison of specified box evaluations for the coarse component, not a measured runtime ratio or a claim that the full proof is 95% shorter. Subsequent confinement and local certificates have not disappeared.

## Analytic closure and limitations

`fourier-closure.tex` independently proves compensated quadratic-hinge inversion, the triangle sixth-order LOW estimate, and the complete six-piece HIGH estimate, including all-index evaluation at the floor, actual event hypotheses and the Gaussian comparator. It applies to varying laws and moving raw thresholds. It closes precisely the Fourier route used here; paired/Mills alternatives elsewhere remain outside that review.

`exclusion-proof/exclusion.tex` proves that the harmonic argument permits conditional span below one, improving its former below-one-half restriction. It also constructs actual standardized iid laws with arbitrarily small defect and noise but span exactly one and zero fractional-part gain. This rules out a tempting moment-only shortcut around confinement. Those laws are not claimed to satisfy maximizing contact or nonnegative excess.

`base-audit.md` identifies the unresolved finite-prefix dependencies. In particular a historical C5 composition assumes C4 and therefore cannot supply that missing parent. The sparse/partial checkout limitation is stated explicitly; missing checkout files are not treated as absent repository objects. The small conditional n4 support refinement does not close ROOT4 or BASE41.

| Result | Mathematical status | Execution status |
|---|---|---|
| Complete triangle LOW / six-piece HIGH / inversion | Independently derived at stated moment/event scope | Fresh exact algebra, domain and negative controls pass |
| Mean/beta contraction and fixed-c scalar transport | Derived and independently reviewed with actual-law hypotheses | Exact bounded discovery completed; separate named acceptance replay recorded under accept01/accept02 |
| Four-pass coarse entry and 100p export | Conditional on the explicit contact, conservation, support and moment/gap inputs | Fresh exact accept02 PASS: 11264 boxes, 100 probability panels (30 nonempty), 19 rejected controls |
| Harmonic span extension and resonance obstruction | Proved, including an actual-law obstruction | Exact laws and mutation controls pass |
| Full finite base, confinement/count composition, sharp conjecture | Not established by this continuation | No complete native/Lean acceptance |

## Reproduction

Run from the repository root with ordinary, unoptimized Python:

```sh
python3 -B mathematics/fixed-target-v7/2026-10-27/accept_entry.py mathematics/fixed-target-v7/2026-10-27/entry-proof.json
```

`export_entry.py` is discovery-output conversion; it is not acceptance. The acceptor pins reviewed sources, reconstructs the two-quadratic ancestor, proves each selected support-radius gate, replays every signed box, checks complete coverage and all probability incidences, and rejects malformed or understated proof data. It is an exact rational replay of the stated implementation, not an independent implementation of all its analytic inequalities.

Independent reviews: `signed-independent-review.md` and `fourier-signed-review.md`, with source hashes and exact scope. `signed_review_structure.py` is independent accounting only; it must not be described as a numerical leaf reimplementation. `runs/fixed-target-v7-20261027/signed01` through `signed07` preserve the bounded exploratory history and source snapshots. No earlier result is overwritten.

The selected dependency removals are specific: no full exponential/degree-six phase ancestor, no six coarse actual-gap HIGH updates, no unknown-score cap for this initialization, and no legacy twelve-stage signed initialization in the new composition. The moment inequalities, two coarse quadratic passes, complete Fourier terms, contact and finite-base obligations remain. Existing alternatives remain available in the repository.
