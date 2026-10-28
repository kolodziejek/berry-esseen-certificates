# A shorter argument: direct geometry and direct count comparison

The best route in the supplied comments is to simplify the mathematical
dependencies before shortening the exposition. We have adopted the direct
geometric cost and a count comparison adapted to the support strip already
available. Several replacements are proved below. The sharp conjecture,
the remaining count range and the finite base are still open.

This work starts at `00ba714897f2e09995d78354ac3c8931e257cd05`, preserves the
original baseline `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`, and is intended
for the existing draft PR5 in `kolodziejek/berry-esseen-certificates`.
The manuscript and all earlier certificates remain unchanged.

## What changed in the argument

The geometric defect pays for three departures from the extremal Bernoulli
law: the wrong sign probability, displacement of the inner support points,
and noise within each sign. The old proof repeatedly fed bounds for these
quantities into one another. The new proof keeps their common cost in one
inequality. Four quartics and two cubics give the global bounds; one direct
evaluation on each of the 30 existing probability panels then gives all
13 incoming strips and stronger central inputs. A balanced linear bound
retains the joint displacement/noise constraint, so this simplification
does not spend the same reserve twice.

For the count comparison, the binomial anchor need not be the nearest
integer. Choose it so that its phase lies in `[-.272,.728]`. That interval
fits the available conditional support `|U_j|<=.6` and inward displacement
`d<=.072`. The exact conditional-count identity is unchanged, including
strict outgoing and closed incoming events. Its curvature, variance and
normalization estimates are rederived on the larger phase interval.

There is now a complete direct comparison for `0<lambda<=1/50`, all
`n>=42`, `p in[.40,.53]`, and raw threshold `|H|<=1.84`. A quartic
minorant handles the own count near zero phase; Cantelli and the normal
increment handle the remaining phases. A quadratic Poisson theorem and
one geometric-series estimate control all incoming counts, including their
infinite tail. Four closed phase intervals suffice; no parameter grid is
needed. Every inner error is controlled relative to lambda. The conclusion is

`a + rho_B*(CE-C_B) < -lambda/100`.

This eliminates the half-amplitude confinement, fractional-part gain,
marked crossings and count curvature **on this domain**. On the smaller
interval `lambda<=1/500`, a separate elementary fourth-moment argument
also eliminates the Poisson input. Together with
the external strict Bernoulli theorem at lambda=0, it closes that part of
the count comparison. No limiting fixed-law argument is used.

The join uses the same original law: set `I=1_{X>0}` and
`U=(X-E[X|I])/ell`. Then `s=theta/ell^2` and `lambda=ns`, while the two
inward displacements are `a0=p-A/ell`, `a1=q-B/ell`, summing to the
geometric `d<.068<.072`. The thirteen closed panels and their outer support
rays give `|U_j|<.6`. The retained coarse threshold bound is
`|H|<=1.83605680<1.84`. Here p refers to the oriented positive closed-CDF
witness. Negative errors use the earlier reflection-and-attainment
reduction; one cannot simply replace p by q inside the acquisition.

## Proofs and checks

| Result | Mathematical status | Execution status |
|---|---|---|
| Direct common geometric cost | Complete local derivation for the stated compact actual law and central gap | 170 exact actual-law controls, including a false stronger-price control |
| Global theta<.056, d<.068, lambda<.616, rho<1.426 | Conditional only on stated coarse-entry inputs; radius needed for rho | 40 exact gates; independent reconstruction of four quartics and two cubics |
| One-pass entry-panel consequences | Derived whole-panel formulas; incoming strips retain heat/ray/contact/predecessor hypotheses | All30 panels checked, two excluded, all13 incoming .6 strips recovered; independent balanced-resource review |
| Direct count theorem through lambda=1/50 | Complete analytic comparison on its explicit actual-law domain; uses the external quadratic Poisson theorem | 62 exact gates, independent40-coefficient polynomial proof, 144 exact own-count tests and four new exact full-event controls |
| Elementary comparison through lambda=1/500 | Complete analytic comparison with no Poisson theorem | 46 exact gates, independent40-coefficient polynomial proof and five exact selected-event controls |
| Shifted-anchor curvature and gap criterion | Complete general inequalities at stated domains | Exact binomial, atom-collision, pathwise and all-p cubic controls; no full numerical count cover |
| Fifth-moment, first-moment and cosine replacements | Complete local proofs | Exact identity/inequality checks and false stronger-bound controls |
| Common all-n transfer and finite-base box | Transfer proved for finite third moment; compact box conditional on affine structural bound and attaining fixed-target contact | Exact controls; no finite-base acceptance |
| Whole sharp conjecture | Open | No complete LOCAL42 or BASE41 acceptance |

Read the short mathematical notes first:

- [Direct geometry](geometry.pdf), with source [geometry.tex](geometry.tex).
- [Direct count comparison through lambda=1/50](moderate-noise.pdf), with
  source [moderate-noise.tex](moderate-noise.tex).
- [Elementary comparison through lambda=1/500](small-noise-proof/main.pdf),
  with source [small-noise.tex](small-noise.tex).
- [Elementary replacements](primitives.pdf), with source [primitives.tex](primitives.tex).
- [Shifted count argument](counts.pdf) and [its review](counts-review.md).
- [External theorem checks](external-results.md): exact Bernoulli scope and
  the quadratic Poisson comparison, kept distinct from our deductions.

The main new derivations have separate reviews:
[direct-count review](moderate-noise-independent-review.md),
[elementary small-noise review](small-noise-independent-review.md) and
[geometry review](geometry-independent-review.md). Exact input/output receipts are under the four
component run directories. Compilation and visual inspection check the
documents, not their mathematical truth.

## Exact dependency removals

1. **Eight moment-update rounds.** Replace the recurrence in
   `mathematics/fixed-target-v8/2026-10-28/moment-entry-v8.py` by
   `geometry.tex` and the single evaluation in `geometry-panels.py`, for
   the named global bounds, probability exclusions, thirteen strips and
   central inputs. The new central resource triangle has intercepts
   `.069772925988` and `.551973904179`, both below the old
   `.0730144376` and `.5728987925`. The raw H and signed phase bounds
   still come from their separate v7/v8 ancestors. Unlisted old per-panel
   bounds require an individual comparison before replacement.
2. **Three fifth-moment penalties.** The new signed-plus-weighted loss
   `P_sign + (gamma-rho*beta)^2/(16m)` dominates the old three-way
   maximum in `sections/04-fixed-entry.tex` near line569. Its proof
   allocates the two signs separately. The stronger sum with denominator
   8 is false; an exact actual-law counterexample is retained.
3. **Eleven auxiliary first-moment choices.** Solve the same PSD
   determinant explicitly, including boundary cases. The resulting root
   is the infimum over all positive auxiliary choices in the old formula
   near `sections/04-fixed-entry.tex:561`. Other signwise PSD constraints
   remain. No revised Fourier cell cover has yet been generated from these
   stronger moment inputs.
4. **976 scalar cosine coefficients.** The unique maximizer solves
   `tan(y/2)=y`. Six Taylor terms, directed Machin bounds and monotonicity
   prove the same working constant4553/1000, with room to spare. This
   replaces the two scalar Bernstein certificates, not the other harmonic
   or convolution arguments.
5. **Low-noise confinement and count machinery.** After acquiring the .6
   strip, the direct theorem above bypasses the half-amplitude theorem,
   harmonic gain, marked crossings and count curvature for lambda<=1/50,
   p in[.40,.53], n>=42 and |H|<=1.84. It uses one external quadratic
   Poisson comparison, followed by two rational tail formulas; no Poisson
   table or truncation is required. The smaller lambda<=1/500 proof needs
   only a fourth moment. None of these removals applies at larger noise. The zero-noise endpoint
   follows from Schulz, without a new limiting certificate.
6. **Index-specific scalar transfer identities.** One sign-size-biased
   response formula works for every n. This replaces the scalar modulus
   and iid power-remainder part of the original-law four-summand appendix.
   Its reference law may have three atoms; it does not replace the signed
   Fourier information, bounded-support prices, or actual finite-base rows.

These are proposed dependency substitutions supported by new proofs, not
deletions from the repository. No runtime speedup or final manuscript page
count has been measured.

## How the whole proof should now be organized

1. Fix the target CE. Establish attainment and contact for a contrary
   witness. Keep the sharp-predecessor requirement explicit where it is
   used. A least contrary index cannot supply the still missing finite base.
2. Use the common conservation identity and the selected coarse Fourier
   entry. The existing11264-cell signed cover is still a dependency.
   The improved moment primitives may simplify that cover later, but this
   task has not claimed a smaller replacement for it.
3. Apply the direct geometric cost. Obtain the support strips with the
   existing contact/heat rays, using one set of panel formulas. Keep the
   shared displacement/noise reserve visible throughout.
4. Compare actual conditional counts directly with Bernoulli. For zero
   noise use Schulz; for the proved small-noise range use the direct
   quartic argument. For the rest, retain the binomial gap
   `2*CE*(min(p,q)-p*)^2/sqrt(pq)` where its theorem applies, instead of
   insisting that every error term be negative by itself.
5. Treat the finite base as a separate problem. The new common compact
   witness domain `rho<1.841, |X|<13, |H|<26` for n=1,...,41 needs no
   sharp predecessor, but it is only a localization. A genuine product-law
   argument or certified complete finite cover is still required.

The main unresolved large-n work is the count comparison above the proved
small-noise range and the left probability range below .4. The shifted
anchor makes a wider route possible; feasibility of its domains is not
itself a comparison theorem.

## Assessment of the supplied comments

Astra's direct cost and shifted anchor are the most useful structural
suggestions. We rederived them and followed their consequences, rather than
accepting the proposed60-page target as evidence. The geometry and the
small-noise count theorem now make concrete parts of the old chain
unnecessary.

The supplied Opus ZIP contains `README.md`, `experiments.py` and
`nearres.py`, not an additional written proof. The scripts are exploratory:
they use floating optimization and rounded convolution locations. We read
but did not execute or import them. Their rare-jump examples were recast
with exact rational atom locations and probabilities. The16 near-resonance
diagnostics lie outside the original lambda<=1/500 theorem's premises; their ordinary
floating CDF scores are labeled diagnostics. Five separate examples inside
the proved domain have exact selected-event checks with rational normal
enclosures. Four further controls in .002<lambda<=.02 pass the same exact
event arithmetic, with all hypotheses checked rationally. These reuse the
original evaluator and are not claimed as an independent implementation.
Discovery of the selected event was floating; the accepted
event comparison and distribution arithmetic were exact.

The unrestricted same-sign Bernoulli domination shortcut remains false,
as documented in the earlier audit. Rounded atom collisions and positive
sampled margins do not repair that defect. The accepted route preserves
the exact count identity and bounds its terms on an explicit domain.

The manuscript has deliberately not been revised in this task. The next
editorial pass should follow the new dependency graph after the remaining
comparison is settled, rather than obscure open steps by shortening prose.

## Reproduction

Run `python3 -I -B mathematics/simplification-v10/2026-10-28/run_checks.py NEWID`
from the repository root, using a fresh alphanumeric identifier. The driver
refuses an existing output directory and executes ten bounded component
checks without importing discovery or inherited mathematical kernels.
`runs/simplification-v10-20261028/integration01/receipt.json` records the
first eight-component PASS. The final ten-component PASS is
`runs/simplification-v10-20261028/integration02/receipt.json`, including the
moderate-noise proof and independent checker. Exact actual-law
event evidence is in `actual-laws01/` and `moderate-actual01/`; these controls
are not automatically rerun by the bounded driver.
The old coarse-entry/Fourier ancestry was not rerun in this task.
