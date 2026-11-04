# Final scope review: promotion of D.3 and D.5

Date: 30 October 2026. Reviewed worktree:
`work/manuscript_revision_20261029`, with pre-edit HEAD
`77d7b4b2510a6ce5b2d8e162bd2a78ecbecec1b5`.
This review changes no manuscript or pinned numerical source.

## Finding

**The promotion of D.3 and D.5 from numerical conditions to
computer-assisted propositions is supported by the combined analytic
arguments, code correspondence audits, and fresh exact replay.** I found
no circular dependency or remaining unproved numerical gate in the
promotion's scope. The altered localization theorem retains its actual
law hypotheses, attained contact, sharp predecessor, and external
structural inequality. The global statement retains the independent
finite base through 699.

This is a review of the certificate discharge and its dependency
composition. It is not a new independent review of the later local
binomial theorem or the cited external literature. It does not assert the
finite base, the full conjecture, or a proof-assistant verification.

| Claim | Mathematical status after this review | Execution status |
|---|---|---|
| D.3 numerical table and strict gap margins | Exact checked proposition; continuous use follows from the proved coarse bounds and Fourier enclosure | Fresh replay plus separate 48-state reconstruction PASS |
| D.5 cover, gates, and printed constants | Exact checked proposition; valid necessary exclusions and ordered enclosures preserve every actual witness | Fresh isolated replay and separate printed-claims check PASS |
| Localization for attained witnesses at every n>=42 | Computer-assisted theorem under its displayed predecessor and structural hypotheses | Numerical inputs freshly reproduced |
| Global finite-base implication | Certificate premises removed; BASE699 and the stated external inputs remain | No finite-base computation supplied |

## Material reviewed

- Current TeX diff in `main.tex`, `sections/01-introduction.tex`,
  `sections/04-fixed-entry.tex`, `sections/09-composition.tex`,
  `sections/10-discussion.tex`, `appendices/entry-details.tex`, and
  `appendices/reproducibility.tex`.
- All three saved reports: `coarse-audit.md`, `fourier-audit.md`, and
  `signed-audit.md` in this directory.
- The actual support/contact proof in Appendix D, its imported contact
  formula, the conservation derivation and phase-price corollary, the
  signed step and coverage argument, and the relevant selected source
  paths in `signed_core.py`, `accept_entry.py`, and `signed_support.py`.
- `support_audit.py` and the fresh
  `runs/certificate_discharge_20261030/root01/support.stdout.json`.
- Fresh isolated-replay command/return-code receipt and stdout in
  `runs/certificate_discharge_20261030/root01/`, together with
  `claims.stdout.json`.

The selected proof object's hash is
`61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae`.
The isolated replay returned 0, with
`PASS_ISOLATED_REPRODUCTION_FIXED_ENTRY_V7`, 11,264 nominal signed
boxes, 100 probability panels, 30 nonempty panels, 19 acceptor controls,
and five wrapper controls. Its recorded elapsed time is
26.935194832999997 seconds. No completed calculation was rerun for this
review.

## Dependency order and absence of circularity

The mathematical dependencies can be ordered as follows.

1. **Fixed-target attainment and contact.** The preceding fixed-target
   proposition supplies a compactly supported maximizing witness and
   equality of the contact expression on its entire closed support.
   Its proof uses tightness, lower-order moment uniform integrability,
   closed-CDF upper semicontinuity, and a one-point contamination. It
   does not use entry bounds, certificates, or a bounded-support moment
   assumption. For localization, an attained pair is also an explicit
   hypothesis; no numerical routine is being used to prove attainment.

2. **Conservation and nonnegative defect.** Conservation is obtained
   from the contact identity by gap integration, zero-bias integration,
   and the first-moment identity. The gap sums are finite under the
   compactness already proved. The moment-circle/gap lemma proves
   D>=0 for the actual law without either certificate or a presumed
   central gap. Its placement later in the paper is a forward reference,
   not a logical dependence on localization. The brief statement in
   Section 3 that localization will provide numerical bounds is not
   used in the conservation proof.

3. **Initial support and moments.** The structural inequality bounds
   rho; the sign-moment inequality bounds beta. The sharp predecessor
   gives the contact upper bound with the favorable term `-n*a`, which
   is discarded using a>=0. The Gaussian heat/ray estimate then gives
   the entire support bound. Only after that bound are M4, M5, M6 and
   the Fourier event introduced. Thus no higher moment or Fourier
   estimate is used to justify the first support acquisition.

4. **First complete Fourier enclosure and D.3.** The universal event
   under two iid copies exists before a central gap is known. Appendix
   A bounds the complete Fourier integral using this event and the
   acquired support/moments. Coarse coefficients produce a raw T
   before the density and phase-price corollary is applied. U then
   produces the weighted invariant `nD<=42d`; the second coarse pass
   acquires the actual central support gap by a strict contradiction
   with the zero-in-support bound.

5. **Support refinement and D.5.** Per-rho radii are acquired again by
   the independent contact/heat/ray argument, before recomputing higher
   moments. The signed pass enters with a licensed raw T and the
   weighted defect invariant from D.3. Its actual opposite-sign event
   is permitted by the already acquired gap. Every signed step proves
   its new raw bound before repricing the phase and updating U and d.
   No U or d is treated as a raw bound. Pooling may weaken bounds but
   cannot remove an actual law; all closed incidences are retained.

6. **Localization and composition.** The finite soundness proposition
   is a generic induction on valid enclosure/exclusion rules and closed
   subdivisions. Its proof does not assume either numerical table.
   D.3/D.5 instantiate those rules with verified inequalities. The
   localization theorem then invokes those proved propositions. The
   global argument uses localization only at a least failure above
   699, where BASE699 and minimality supply the predecessor.

In particular, D.3's invocation of the soundness proposition is not
circular: that proposition assumes valid elementary rules and a passing
evaluation, not D.3 or D.5 as mathematical hypotheses. The text could
make this ordering even more explicit by calling its inputs the
"analytical enclosure and exclusion rules," but this is an editorial
clarification, not a missing proof.

## Independent checks of the support and phase interfaces

I checked the potentially delicate analytic support interface against
the formulas, rather than infer it from the root script's PASS label.
With v=n-1 and s=sqrt(n/v), Taylor expansion of the Gaussian CDF and
the heat equation give the cubic coefficient `(-t^3+3t)/6`, the quartic
coefficient `(t^4-6t^2+3)/24`, and the four displayed uniform remainders.
After division by s^3, their denominators are respectively v,
v^(3/2), v, and v^(3/2). The manuscript's bound E(u) follows using
v>=41, sqrt(v)>6, `||phi^(4)||<=3phi(0)<6/5`, and
`||phi^(5)||<=8/pi<51/20`.

For the leading polynomial, the `B<=A/4` gate handles the reflected sign
and the exterior normal thresholds; on |z|<=1, completing
`-Az^2+3B|z|` yields `9B^2/(4A)`. The exact radial derivative is
`n phi(z)+Ht phi(z)-ns phi(sy)`. Taylor expansion in y and the identity
`d_s[s phi(sy)]=-phi''(sy)` bound its absolute value by
`phi(0)(t^2/2+1/2+eta_n)`. Consequently the negative Q/Q'/Q'' and
L/L'/L'' gates extend the strict boundary exclusion over both entire
closed exterior rays. The sign Q<0 is established before c is replaced
by its lower bound. This justifies the open support conclusion and the
same test at each stored radius.

The import-free support check independently encloses beta by monotone
rational bisection and verifies the initial radius and all 24 stored
radii. The original acceptor separately recomputes the actual selected
radius using its own helper and rejects disagreement with the stored
one. Hence the support check is supplemental evidence; it is not
silently substituting a smaller beta cap into the retained acceptor.

For the phase interface, set `M_c=c*rho-phi(0)D/6`. Conservation gives
`e M_c >= c*rho-T/n>0`, while D>=0 gives `M_c<=c*rho`.
Thus the incoming raw gate licenses both the density interval and
`R_c-U=n(1-e)M_c >= H^2(c_-l-T/N)/2`. This establishes the exact phase
price used in both programs. The implication holds separately at each
actual n>=42; setting the scalar floor to 42 is not setting the law's
sample size to 42. The Fourier audit supplies the independent all-index
majorant argument needed for its constants.

## Printed values and theorem scope

The new proofs correctly distinguish the acceptor's generic target limits
from the sharper values in the fixed accepted object. The exact
printed-claims check establishes the latter, including:

```text
max raw          = 10997587/5000000 = 2.1995174
max D            = 76682509/100000000 = 0.76682509
max weighted nD  = 1610332689/50000000 = 32.20665378
max original rho = 71527/48000
max |beta|       = 50549963/100000000
max |H|          = 2295071/1250000
max radius       = 157/50
```

The rho statement correctly comes from the last surviving original row
index 13, rather than the slightly larger rounded panel field
1.49014584. The open support interval correctly comes from the strict
whole-ray argument, rather than from the radius value alone.

The main theorem edits remove only the now-discharged certificate
premises. The abstract states that a base through 699 implies all sample
sizes, and explicitly says that base is not proved here. The composition
theorem is appropriately renamed "Finite-base implication." This is a
stronger justified result than an implication also assuming D.3/D.5,
but is not an unconditional solution of the full conjecture.

The frozen acceptor's historical conditional status string is consistent
with this promotion: the acceptor establishes a modular arithmetic
claim, and the manuscript supplies its analytic inputs. It need not be
rewritten or have its semantics weakened. Lack of a Lean formalization
is not a residual theorem hypothesis.

## Publication consistency

The first diff inspected still had only the 29-October replay description
in Appendix E. The later diff reviewed here adds the 30-October replay,
correspondence reports, separate printed-claims command, fixed-object
hash, and explanation of the unchanged conditional status strings.
That resolves the textual mismatch with the new proposition proofs.

The final release should include the referenced audit/evidence directory
and manifest and complete normal TeX compilation and layout checks.
Those are packaging/verification tasks for the coordinator, not an
identified mathematical obstruction. No manuscript edit was made by
this reviewer, and no additional mathematical gate was found to block
the promotion.
