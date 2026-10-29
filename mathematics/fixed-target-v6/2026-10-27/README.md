# From fixed-target excess to an actual support gap

This continuation closes the initial `D < 4` and actual-central-gap gates on the complete initial third-moment interval. It does **not** establish the full INITIAL42/LOCAL42 contracts, all retained Fourier premises, or BASE41. The reference commit remains `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`; no certificate, production driver or target is changed.

## Selected short proof

Use the sign-coherent K1 estimate and fifth-moment square in `signed-proof/signed.tex`, the same-law circle/inversion in `moment-core.tex`, then the two elementary quadratic passes in `simple-route.tex`. This acquires an actual central support gap on every one of 24 closed rho cells. The new degree-six phase lemma is **optional**; it is not required by the selected route.

Assumptions: an attained fixed-target witness with nonnegative excess, sharp predecessors, support radius 96/25 and rho in [1,7361/4000], the fixed-target conservation identity, and the retained complete low/high-frequency scalar inequalities, uniformly for n >= 42. All moments refer to one actual marginal. Initial contact/support/structural arguments are supplied in v4/v5; exact arithmetic here does not prove their entire dependency graph.

| Result | Mathematical status | Execution status |
|---|---|---|
| Signwise bound for K1, including reflection and zero atoms | Proved for any centered variance-one law with the specified bounded support | Exact 24-cell and actual-law checks; independent reconstruction passes |
| Fifth-moment quarter constant | Proved by a nonnegative square; already present in later signed code | Sharp zero-atom control and exact coefficient reconstruction pass |
| Two-pass central-gap entry | Conditional on the listed contact/support/Fourier premises | Fresh exact 48 cell passes; separate independent review |
| Full-phase one-pass entry | Conditional on the same premises; selected quadratic has its own strict raw gate | Fresh 24-cell check; independent 336-polynomial review including optional updates |
| Actual-gap event and distance | Proved from actual gap sums and same-law moments | Exact actual-law and complete-window domain controls |
| Six optional actual-gap HIGH updates | Conditional on the full six-piece HIGH theorem and initial acquisition | Fresh exact 24-cell cover; all frequency pieces retained |
| Full acquisition, count exclusion, finite base, sharp conjecture | Not established by this continuation | No complete native/Lean acceptance or heavy generation campaign |

## Exact quantitative outcomes

The selected simple route uses no degree-six maximization:

- Pass 1: raw <= 13.2818901598, resource <= 10.9330610254, D <= 3.9164138937; all 24 cells satisfy D < 4,23 have the actual-gap scalar gate.
- Pass 2: raw <= 11.5164967977, resource <= 9.9790315907, D <= 3.5746638454, nD <= 150.1358815051. All 24 satisfy `d<(sqrt(10)_lower−1)*rho_lower`, with minimum margin 526024602543/1600000000000 > 0. No central-gap premise is used in these passes.

The optional full phase calculation acquires all 24 gaps in one pass: U <= 10.7965952605,D <= 3.8675294672. Six optional circle updates give D <= 3.3579256801. Six optional updates using the acquired actual-gap event instead give U <= 8.3681296416,D <= 2.9976105609,nD <= 125.8996435547. Only 16/24 cells then satisfy D < 2. These are upper bounds, not values of an optimizer.

The actual-gap criterion is `D < (sqrt(10)−1)*rho`; the stronger sufficient uniform condition D < 2 is unnecessary for this conclusion. This does not license the other conclusions of any lemma whose hypotheses specifically require D < 2.

## Proof shortening

`compression-map.md` gives source locations, measured page spans and a dependency-removal audit. The selected route replaces score-cap feedback **to the initial support-gap conclusion** with two coarse scalar passes. The manuscript already uses first failure; its earlier savings cannot be counted again. Full Fourier estimates, later physical/noise acquisition, confinement, strict count comparison and the finite base remain. There is no supported percentage reduction or claim that 24 cells replace the outputs of a complete 18432-cell stage.

The v6 note is intended to replace the relevant derivations in a future consolidated manuscript, not to be appended to all earlier notes as mandatory reading. Choose the elementary route for exposition, keeping stronger phase/event estimates available when their quantitative gain is needed.

## Reproduction and review

From the repository root:

```sh
python3 -B mathematics/fixed-target-v6/2026-10-27/run_checks.py another-unused-run-id
```

The driver refuses an existing run directory, records streams/versions/hashes/return codes and verifies preservation of all original baseline entries, including sparse tree/index objects. It runs only bounded exact checks. Component evidence, independent review reports and negative controls are in this directory and `runs/fixed-target-v6-20261027/`.

`main.pdf` is the compiled proof note; `source-fixed-target-v6.zip` contains portable TeX. Review reports separate mathematical scope from execution status. Existing draft PR #5 is the only review target. No merge is authorized.
