# After coarse entry: moment contraction and one complete confinement panel

The new result is **conditional half-amplitude confinement on the entire panel
p in[.41,.42], for every actual n>=42**. If an attained fixed-target witness
has nonnegative excess, satisfies the sharp predecessor bound, and meets the
retained contact, gap and accepted-entry hypotheses, its normalized conditional
noise obeys `|U|<1/2` and its inward displacement obeys `d<.069<1/4`.
This is one complete panel, not the whole local comparison or the conjecture.

The proof has a simple division. Small noise makes the third moment and signed
second moment close enough to their two-point values that two direct contact
inequalities exclude the exterior rays, uniformly in the threshold. Larger
noise consumes part of the same conserved resource that pays for the other
errors. Keeping the sign of the threshold in that resource closes the
remaining finite bounds. No extra phase or noise subdivision is needed.

A further reduction now handles small noise on **all thirteen acquired panels
p in[.40,.53] without a new probability grid**. Both physical support rays
reduce to one quintic polynomial on[1.7928,2.1912]. Its third derivative is
negative, its first derivative is concave with positive endpoint values, and
its right endpoint is below−.1779. A few accompanying monotonicity inequalities
give the whole exterior rays. Start with the short
[continuous proof PDF](low-noise-continuous-proof/main.pdf); its
[portable TeX source](source-low-noise-v8.zip) reproduces all five pages.

## Results and evidence

| Result | Mathematical status | Execution status |
|---|---|---|
| Attainment/contact and full conservation, including support residual | Derived under stated fixed-target hypotheses; independent review | Exact finite-law, atom and residual controls pass; see conservation-audit.md |
| Elementary contraction of every entry probability panel | Derived from the actual-law outer-gap inequality and accepted entry | All30 panels evaluated exactly; panels24 and53 excluded,28 survive |
| Signed phase resource | Independently derived conditional same-law bound | Complete2048-box last-pass replay;682 active cells,1364 endpoint quadratics independently reconstructed |
| Small-noise half amplitude on acquired p in[.40,.53], lambda<=.075 | Continuous analytic implication, independently derived; all H and n>=42 |28 exact endpoint/domain gates, no new grid; independent polynomial reconstruction passes |
| Complete half amplitude on p in[.41,.42] | Conditional composition of the preceding entry and retained confinement inequalities | All128 closed boxes covered:16 direct heat,84 excluded by resource,28 pass both rays |
| ROOT4 original-law to central-threshold bridge | Conditional proof of the scoped bridge | Exact Hermite/moment/count/atom controls; no native ROOT4 acceptance |
| Complete confinement on other panels, strict count comparison, BASE41 | Still required | No complete acceptance claimed |

The elementary all-panel result gives

\[
p\in[.25,.53],\quad\theta\le.0594425514,\quad
d\le.0719539227,\quad\rho\le1.4547288545,\quad
\lambda\le.6314459997.
\]

Its direct `.6` strip test passes on panels40--52. The positive boundary
estimate fails on panels25--39; the proof does not discard these panels.
A separate binary-cost/phase screening experiment excludes no additional
whole panel. Those unsuccessful bounds are preserved, not turned into claims.

## Read the arguments

- [moment-entry-v8-proof/main.tex](moment-entry-v8-proof/main.tex): the all-panel
  defect decomposition, ordered iteration, moment turnover and signed beta bounds.
- [phase-proof/main.pdf](phase-proof/main.pdf) and
  [phase-proof/main.tex](phase-proof/main.tex): the three-page signed resource
  argument and its exact closed-region consequences.
- [small-noise.tex](small-noise.tex): an independent three-page proof of the
  small-noise step using simple rational constants, with the heat remainder
  and whole-ray derivative estimate derived explicitly.
- [low-noise-continuous-proof/main.tex](low-noise-continuous-proof/main.tex):
  the shorter uniform low-noise argument. Its abstract premise allows
  p in[.4,.6]; the actually acquired strip permits application only to[.4,.53].
  The independent derivation is in
  [reviews/low-noise-proof/main.tex](reviews/low-noise-proof/main.tex).
- [phase-confinement-proof/main.tex](phase-confinement-proof/main.tex): the
  complete five-page panel join. The previously derived parameterized
  confinement inequalities remain in
  [confinement-proof/confinement.tex](confinement-proof/confinement.tex).
- [root4-bridge.tex](root4-bridge.tex): the original-law response, midpoint and
  threshold interpolation bridge. Genuine whole-cell rows, complete numerical
  coverage and the closed Prawitz theorem remain inputs. The central interval
  must actually meet the certified tail ranges before claiming all thresholds.
- [reviews/phase-accept-independent.md](reviews/phase-accept-independent.md):
  executable review, reproduced acceptance defect, repair and isolated ancestry.

The long manuscript remains a research draft. These notes supply the new
analytical arguments without promoting the unresolved global statement.

## Exactly which dependencies can change

1. **Panel moment acquisition can use elementary algebra after v7 entry.**
   The proof of the common defect budget in `moment-entry-v8-proof/main.tex`
   pays the binary asymmetry cost first, then bounds displacement and noise
   from its nonnegative residual. The eight iterations use only previously
   established bounds. No further Fourier-kernel execution is needed for
   those exported moment bounds. The outer-gap inequality and initial entry
   remain necessary; this does not remove their ancestors.

2. **The downstream scalar resource need not be a global absolute-phase cap.**
   Proposition1 in `phase-proof/main.tex` retains both signed slopes in each
   accepted cell. Convexity in the fixed target justifies its two endpoints;
   the separately proved raw ceiling precedes the extra phase price. All682
   active cells remain. These envelopes can therefore replace the looser
   global ceiling when the consumer uses the same actual-law resource.

3. **The lowest-noise confinement band on this panel needs no phase table.**
   The theorem in `small-noise.tex` covers all raw thresholds and the entire
   closed lambda interval[0,.075], including zero. The already acquired `.6`
   strip controls the conditional cubic moment before the `.5` strip is
   inferred. Two boundary values and12 ray signs replace the sixteen
   phase/sign boxes of that lowest band. The shared `.075` endpoint is
   included in both proofs. The remaining seven noise bands still require
   the retained finite resource/ray gates.

   The later continuous proof replaces the additional thirteen-panel
   low-noise boundary table as well. With common bounds
   theta<.0074, ell>1.992, rho<1.105, set z=p on the negative ray and z=1−p
   on the positive ray of the same law. Substitution gives one quintic
   family; its endpoint/derivative signs prove the entire continuous range.
   These are physical rays, not a CDF reflection. The incoming thirteen-panel
   `.6` strip remains required. The26 boundary checks and156 derivative signs
   from discovery are preserved, but are unnecessary for this new low-noise
   step. The final integrated check uses the continuous argument and binds
   its incoming strip to the fresh elementary moment output.

4. **No complete repository certificate family is deleted by these results.**
   Half amplitude on one panel is not a strict iid count comparison. The
   other27 surviving probability panels, marked/phase/count repairs,
   zero-noise comparison, finite base and any remaining analytic joins
   still have to be established at their full scopes. ROOT4's conditional
   physical bridge is not a complete C4 certificate. C5 cannot supply C4
   by assuming it. Existing certificates, targets and drivers are preserved.

## Acceptance defect and repair

The review found that `python -B` still reads valid cached bytecode. The old
phase checker could accept an altered export even with every `.py` hash
unchanged; import search order admitted a second shadow-module route.
The repaired checker executes explicitly named source bytes and uses an
isolated child with a fresh cache. Adversarial replay now rejects the altered
object and reproduces the genuine export byte-for-byte.

The old v7 source is unchanged. `isolated_entry_replay.py` copies exactly13
pinned files into a fresh private tree and replays its two-quadratic ancestor
and all four selected signed passes. The fresh output is byte-identical to
the earlier accepted output:11264 signed cells,100 probability panels,
30 nonempty panels and19 rejecting controls, plus5 wrapper controls.
This closes a source-execution evidence gap; it does not prove an analytic
premise merely by repeating arithmetic. Original failure and success logs remain.

## Reproduce bounded checks

```
python3 -I -B mathematics/fixed-target-v8/2026-10-28/run_checks.py new-unused-id
```

The integration driver runs eleven small analytic/scalar checks and the complete
128-box confinement join, binds the separately recorded isolated ancestry
and repaired phase replay, and verifies preservation of all2748 baseline
entries. It does not launch a native certificate-generation campaign.
For a new complete isolated entry replay, use:

```
python3 -I -B mathematics/fixed-target-v8/2026-10-28/isolated_entry_replay.py --output-dir runs/fixed-target-v8-20261028/new-entry-id
```

Commands, versions, return codes, exact outputs, source hashes, malformed-object
controls and document builds are under `runs/fixed-target-v8-20261028/`.
The immutable reference commit is `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
All work is submitted to the existing fork draft PR#5; no merge is performed.
