# One small-noise argument across the acquired probability range

This checkpoint extends the direct count argument to the left probability
panels. It also develops an estimate that keeps the conditional variance
allocation in both the outgoing and incoming terms. The full sharp theorem,
the remaining larger-noise exclusion and `BASE41` remain open.

Research starts at `6027b27f85473780eaf90542f490168873de5986`.
The immutable reference remains `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
All work is for the existing draft PR5 in the user's fork. The manuscript,
existing certificates and original theorem targets are unchanged.

## The simpler route

Condition on the number of positive summands. At the Bernoulli anchor, retain
the outgoing probability from that one count. Bound the incoming probabilities
by a complete Poisson tail. Compare their difference with the normal and
third-moment corrections. This uses actual independent conditional noises from
one common marginal, including their atoms.

The new point is that this argument works across every probability panel left
by the geometric acquisition, provided `0<lambda<=.002`. The left panels admit
a slightly larger amplitude, `.7`. The third-moment correction can be unfavorable
there, but a direct uniform bound pays for it. There is no need to infer a
favorable sign that fails for admissible laws.

Read [the five-page proof](allpanel-proof/main.pdf), with canonical source
[allpanel.tex](allpanel.tex). Its theorem is:

`n>=42`, `p in [.25,.53]`, `Y=B+U`, `E(U|B)=0`, `|U_j|<=.7`,
`U_0<=a_0`, `U_1>=-a_1`, `a_0+a_1<=.068`, `0<lambda=n E U^2<=.002`,
and raw `|H|<=1.84` imply `Delta_C < -lambda/100` for `0<=C<=.41`.
Here `Delta_C` is the fully specified same-law Bernoulli comparison in the
theorem. The shifted phase is `[-.218,.782]`; its anchor is always interior.

The local comparison has no contact or predecessor premise. Its application
to an extremal witness retains those premises in the acquisition. The same-law
join is `U=(X-E[X|sign])/ell`, `s=theta/ell^2`, `lambda=ns`, and
`ell=(pq+s)^(-1/2)`. Zero noise is handled separately by the external strict
Bernoulli theorem of Schulz. The right-panel comparison now extends through `lambda=.03` when `C>=.4`, as described below. The previously proved theorem through `.02` remains stronger in coefficient scope: it allows every `C>=0`.

## A further extension on the right panels

[The next count theorem](counts-v11.tex) proves the same strict comparison for
`n>=42`, `p in [.4,.53]`, amplitude `.6`, inward sum at most `.072`, raw
`|H|<=1.84`, and **every `0<lambda<=.03`, provided `C>=.4`**. This includes
`C=C_E`. Its proof needs no grid over noise, probability or sample size.

The new ingredient is a favorable moment gain: the same conditional cubic
expansion gives `C(rho-rho_B)>s=lambda/n`. It pays for most of the normal
variance correction. The first incoming tail is bounded separately on positive
and negative inner phases. A quartic, Cantelli and an infinite factorial tail
then close six intervals covering every phase, with estimates uniform as
positive noise tends to zero. All70 rational gates pass. The [independent review](counts-v11-independent-review.md) reconstructs the original quartics with40 positive Bernstein
coefficients and rederives all six margins; it imports no constructor.

Four further exact selected full-event comparisons in `.02<lambda<=.03` pass with rational normal enclosures (`extended_actual.py`). The constructor also checks18 rare-jump laws at72 events, including collisions and examples with no neighboring outgoing contribution; its `.075` controls lie outside the theorem.

The variance-aware own-count lemma below is a separate advance for the next
range. The `.03` theorem does not depend on the still-unfinished compound-Poisson
construction. Keeping those two routes distinct avoids introducing an
unproved dependency into the completed extension.

## What can be omitted, and why

| Dependency | Precisely justified change | Source and retained assumptions |
|---|---|---|
| Separate half-amplitude acquisition for the new small-noise domain | Not needed: the count theorem accepts amplitude `.7` directly | `leftpanels.tex`, Proposition1 and whole-ray proof; all retained contact, heat and sharp-predecessor premises still apply |
| Missing positive support bound on panels25–39 | Replaced by a proved `.7` positive ray, together with the old `.6` negative ray | `leftpanels.tex`, first proof; eight strict gates at each of30 boundaries plus whole-ray continuation |
| Harmonic smoothing, marked crossings and count curvature within the new domain | Not needed by this comparison: exact conditioning, one quartic minorant, Cantelli and the full incoming Poisson tail prove it directly | `allpanel.tex`, conditioning identity through three closed phase intervals |
| A favorable third-moment repair on the entire left range | Cannot be assumed; the new proof retains and bounds its adverse part | `allpanel.tex`, third-moment subsection; exact three-point law at `p=.26` refutes the shortcut |
| Infinite incoming count truncation or a count grid | Not needed: factorial moments and a geometric series bound every remaining incoming count | `allpanel.tex`, `J_2` and `J_3`; first two counts treated separately on the outer positive phase |
| Fourier coarse entry, contact/attainment/reflection and finite base | No removal justified | These remain ancestors of the acquired support domain or of the first-failure global argument |
| Count comparison on right panels through `.03` at `C>=.4` | The direct route extends, with the same omitted half-amplitude/harmonic/crossing components | `counts-v11.tex`; retain the positive cubic gain and all six phase intervals |
| Count comparison above the proved noise ranges | No removal justified | Variance-aware inequalities and diagnostics do not yet constitute a complete replacement |

These are dependency changes within stated domains. No old file is deleted.
The five-page length is a component-note length, not a claimed length for the
complete proof or a numerical estimate of total pages saved.

## Evidence and limitations

- [Left-panel proof and scope](leftpanels-status.md):15 closed panels, both
  signed whole rays. Only30 exploration ray evaluations and31 acceptance
  evaluations, including a failed `.65` negative control. Missing, duplicate,
  reordered and corrupted-endpoint covers are rejected.
- [All-panel checker](allpanel_check.py):52 exact rational scalar gates, exact
  phase identities, and three rejected shortcuts. These check arithmetic;
  analytic implications are supplied by the proof.
- [Actual-law checks](allpanel_actual.py):five exact iid event comparisons,
  with rational atom keys and probabilities and rigorous normal enclosures.
  The old anchor is explicitly replaced by the new one. Floating maximizer
  discovery is not certified. The source-pinned v10 evaluator is reused and
  is not an independent implementation.
- `runs/simplification-v11-20261028/allpanel01/receipt.json`:fresh arithmetic
  and event evidence, including source hashes, versions, return codes and logs.
- `allpanel-build02`:five-page TeX Live build, with all five rendered pages
  inspected. The dedicated editor project contains a byte-identical proof copy.
- [Independent review](allpanel-review.md) found no mathematical blocker. It rederived the original quartics with40 positive tensor Bernstein coefficients, the normalization and adverse repairs, the entire tail, and10 exact convolution/conditioning events. The report must be read at its exact scope.
  Agreement between reviewers is not an additional mathematical premise.

[The variance-aware own-count note](owncount.pdf) and [coordinator review](owncount-coordinator-review.md) establish a separate local moment inequality and a conditional allocation-endpoint reduction. They retain the same third moments in the own count and marginal repair. Their360 moment,360 strict event and360 cubic controls concern36actual laws; these are controls, not a proof of a continuous larger-noise count domain.

The larger-noise exploration is separated from acceptance. A more flexible
quartic improves some sampled bounds but still fails at `.05` and `.075` when
conditional third moments and incoming tails are bounded independently. These
are failures of sufficient estimates, not counterexamples to the conjecture.
The next step retains the same variance allocation and third moments in both
parts of the comparison. Any finite grid of promising values remains discovery
until a closed-domain proof is supplied.

Reproduce the small-noise arithmetic and actual-law controls with a new run id:

```sh
python3 -I -B mathematics/simplification-v11/2026-10-28/allpanel_run.py NEWID
```

Reproduce the support-strip acceptance using `leftpanels-run.py NEWID`.
Both drivers refuse existing run directories. No expensive certificate
generation or full ancestor replay is included.


For the complete bounded v11 suite, run:

```sh
python3 -I -B mathematics/simplification-v11/2026-10-28/run_checks.py NEWID
```

The suite binds both reviewed proof versions, runs the new component controls
and checks the original baseline and manuscript bytes. It includes the
independent programs, not merely second invocations of the constructors.
The earlier Fourier ancestry and external probability theorems are retained
inputs, not freshly reproved by this suite.
