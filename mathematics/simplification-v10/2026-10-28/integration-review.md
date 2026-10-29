# Composition review of the direct geometry and small-noise comparison

## Extension through lambda=1/50

The final selected comparison is now `moderate-noise.tex`, proved for
every 0<lambda<=1/50 under the same actual-law, n, p, amplitude, inward and
threshold hypotheses. Its conclusion is Delta_C<-lambda/100 for every
C>=0, hence for C=CE. The independent report is
`moderate-noise-independent-review.md`; it rederives the full probability
argument, proves both quartic rectangles with40 tensor Bernstein
coefficients, reconstructs the four final margins and checks144 exact
own-count cases across36 actual marginals.

The coordinator independently read the proof and62-gate checker. In
particular, `(P-i)_+^2<=binom(P,i+1)` is valid for integer i>=2; its
Poisson factorial moment and the coefficient ratio
`[i/(i+2)]*(1+1/i)^i<3` bound the entire incoming tail. The first-count
anchor1 is used only where its denominator is positive; positive outer
phases use Cantelli. The refined positive Gaussian derivative holds with
the same fixed count throughout. All four closed phase intervals join
without a gap, and inner errors are proportional to actual lambda.

No blocker was found. Four additional exact selected-event comparisons
in .002<lambda<=.02 pass, at n42 and100 and p=.4,.42,.5,.53. They reuse
the earlier rational event evaluator and are not a second independent
implementation. Every domain premise in these new controls is checked
by rational arithmetic, including the raw-threshold inequality.

The extension replaces half-amplitude confinement, harmonic smoothing,
marked crossings and count curvature on this larger domain. It adds the
published quadratic-hinge Poisson theorem and uses elementary rational
tail bounds thereafter. The smaller theorem documented below remains
useful because it avoids the external Poisson input altogether. No old
proof is deleted and no claim is made beyond lambda=1/50.

The exact geometric parameter map and contact/predecessor qualifications
below are unchanged by this extension.

## Original small-noise composition review

The coordinating agent read the accepted component proofs and exact checkers.
A separate read-only review by the geometry agent checked the composition
and the external theorem statements. This agent constructed the geometry
component, so its composition report is **not** an additional independent
verification of that component. The separate geometry derivation review is
`geometry-independent-review.md`; the independent small-noise derivation is
`small-noise-independent-review.md`.

## Result and hypotheses

No blocking mismatch was found between the one-pass .6 strips and the
direct count theorem for n>=42, p in[.40,.53], |H|<=1.84 and
0<lambda<=1/500. The explicit parameter map is

`I=1_{X>0}, U=(X-E[X|I])/ell, s=theta/ell^2, lambda=ns`.

The inward bounds are `a0=p-A/ell`, `a1=q-B/ell`, with sum d. The direct
geometry gives d<.068<.072. Its thirteen closed panels cover the required
probability interval, including every shared endpoint; their outer rays
and inward bounds give |Uj|<.6. The unchanged coarse entry supplies
|H|<=1.83605680<1.84 independently of the old moment iteration.

The comparison theorem itself uses actual conditional iid laws, not contact
or a predecessor. The application to an acquired contrary witness retains
the contact, nonnegative excess, sharp-predecessor and earlier Fourier
hypotheses needed to obtain these premises. Reflection and attainment
precede oriented acquisition. No symmetry substitution p->q is made in the
signed geometry or phase calculation.

The new central scalar inputs and balanced resource triangle imply the
older central confinement inputs. The independent review checks all28
balanced exports and strict containment of the central triangle. The raw H
bound and signed phase coefficients remain separate dependencies. Reading
`phase_core.py` and `phase_region.py` confirms that these coefficients
come from the selected coarse signed entry, not the eight-round moment
contraction. Their old weaker moment inequalities remain valid; no new
Fourier cover or signed coefficient computation is claimed.

## Checks and artifact binding

- Eight bounded component checkers passed freshly in `integration01`.
  This confirms their integrated files and exact arithmetic; it is not
  a new independent proof of every written reduction.
- The original small-noise review source hash
  `3ff41e1f9be57b844915a07d02d699987ad696b7756e00b5c96d4a36441e6526`
  was recovered exactly by reversing three display-formatting changes.
  `cosmetic-binding01/receipt.json` records each old/new string and both
  hashes; `reviewed-source.tex` preserves the recovered original bytes.
  The read-only reviewer checked this transformation. Mathematical
  expressions, event inequalities and quantifiers did not change.
- The final small-noise note compiles in four pages without warnings;
  all four rendered pages were inspected. Earlier overfull displays and
  their logs remain in build01/02. Build04 makes the project self-contained;
  all four rendered pages are byte-identical to the inspected build03.
  The desktop editor also compiles the self-contained project successfully.
- Five actual rational-law selected-event comparisons pass using exact
  atom locations and probabilities and rigorous rational normal bounds.
  The floating choice of an event is explicitly discovery, not acceptance
  of the maximizing event or a proof of the universal theorem.
- Schulz's strict Bernoulli theorem and the restricted sharper p-dependent
  gap were checked against Theorem1 of the original dissertation. Pinelis's
  quadratic-hinge comparison was checked against Proposition2.8 and
  Corollary2.11 of the original paper. Neither complete external proof
  nor a third-party Lean project was rebuilt here.

## Final preservation and integration

The final ten-component check passes in
`runs/simplification-v10-20261028/integration02/receipt.json`.
`preservation01/` verifies all2748 original baseline entries:182 materialized
byte checks and2566 sparse tree/index bindings, with lazy fetching disabled.
All85 tracked manuscript files are unchanged, including the paper and its
source bundle. Raw supplied opinions remain identifiable by their input
hashes; no source in reference/ or history/ was edited.

## Limits and recommendation

The specified substitutions are ready for human mathematical review as
scoped research progress. The left probability panels, the remaining
noise range and a genuinely closed finite base remain open. The shifted
phase interval and the compact finite-base box are reductions, not solutions
of those problems. No old certificate, theorem statement or manuscript
source has been removed or weakened. Keep the existing PR draft; this is
not a recommendation to publish or merge a claim of the full sharp theorem.
