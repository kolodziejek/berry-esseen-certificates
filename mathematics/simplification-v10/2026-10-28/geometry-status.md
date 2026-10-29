# Direct geometric localization: result and dependency boundary

This component starts from fork commit `00ba714897f2e09995d78354ac3c8931e257cd05`
on the separate branch `research/geometry-v10-20261028`. It changes no manuscript,
existing proof source, certificate, acceptance program, baseline, reference or
history file. No external service was modified and no generation campaign ran.

## Result

The proposed direct geometric inequality is valid, with a complete derivation in
`geometry.tex` and a six-page compiled note `geometry.pdf`. For an actual compact,
centered variance-one law with central support gap, let `w=1-theta`, `v=pq`,
`ell=sqrt(w/v)` and `d=1-(A+B)/ell`. Then

`D >= ell [w Q(p) + 6w d(1-d) + theta min(C_plus-B_plus*d,C_minus-B_minus*d)]`,

where `Q=(6+2sqrt(10))(p-p*)^2`, `C_plus=3(sqrt(10)+1)q`,
`C_minus=3(sqrt(10)+3)p`, `B_plus=sqrt(10)+5`, `B_minus=sqrt(10)+7`.
The two noise costs are integrated against the two measures of the SAME law.
The inequality itself needs no contact or sharp-predecessor premise.

From the incoming coarse-entry bounds alone,

- `p in [.24,.54]`, `n>=42`, `nD<=32.20665378`;
- and, only for the rho conclusion, `|X|<=157/50`,

the proof gives `theta<.056`, `d<.068`, `lambda<.616`, `rho<1.426`, and `p>1/4`.
No output of the old eight-round contraction enters this argument.

The proof is shorter than the supplied numerical sketch: a coarse `theta<.2`
follows directly from the gap product and positive noise measure. Concavity in d
then leaves two endpoints; the maximal-d endpoint has a crude inward cost >1.38.
The remaining steps are four quartics with a lower second-derivative bound and
two cubics with an upper second-derivative bound. Exact tangent comparisons
replace interval grids. The scalar checker has 40 explicitly named gates.

## Stronger one-pass connection

One further direct evaluation per frozen v7 entry panel replaces the old eight
rounds for the currently used moment/strip conclusions. It reads the accepted
v7 input directly and does not read an old iteration output. Its input SHA256 is
`61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae`.
The named input, all 100 closed source panels, all 30 nonempty panels, maximum
incoming D and maximum surviving radius are checked explicitly.

- Panels 24 and 53 are excluded; panels 25 through 52 are retained.
- All 13 existing .6 strips on p[.40,.53] pass their complete boundary/ray tests.
- The central panel [.41,.42] gives:

| Quantity | New outward bound | Current central theorem's required bound |
|---|---:|---:|
| theta upper | .049086874003 | .054 |
| d upper | .066505471827 | .069 |
| rho upper | 1.204660335428 | 1.22 |
| lambda upper | .526219192656 | .6 |
| ell lower | 1.975749037978 | 1.9706 |
| ell upper | 2.033209198406 | 2.034 |
| beta lower | .103059226156 | .09736 |
| beta upper | .220251236683 | .234 |
| joint displacement intercept (balanced line) | .069772925988 | .0730144376 |
| joint noise intercept (balanced line) | .551973904179 | .5728987925 |

The last two reference values are the old central moment-stage resource
(`runs/fixed-target-v8-20261028/moment03/stdout.json`, panel 41), not independent
threshold caps. The smaller new intercepts imply containment in that old
resource triangle. The raw H bound and signed phase resource are unchanged
separate ancestors; this table does not re-establish them.

The direct formulas also retain the shared constraint
`aI*d + C_I*lambda/(42*vmax) <= J_I`, where
`aI=6(1-d_I)-Theta_I*(s_upper+7)/(1-Theta_I)>0`.
The zero-reserve case forces both quantities to zero. This keeps the joint
resource needed by later count estimates; its two intercepts cannot be spent
independently. The first line's central displacement intercept .07337803326
is slightly larger than the old .0730144376, although its noise intercept
is smaller. The balanced line averages it with the other valid linearization
of the same mixed cost; it improves BOTH old intercepts, as the table shows.
Both valid lines remain exported.

The new whole-panel outward bounds additionally give theta<=.053287161488,
lambda<=.561431508254 and ell>=1.960929043113. The independent global bounds
rho<1.426 and d<.068 remain available. These are useful improvements, but the
main simplification is removing the feedback iteration and exposing one cost.

## Mathematical versus execution status

| Component | Mathematical status | Execution status |
|---|---|---|
| Direct actual-law budget | Locally derived complete analytic proof | 170 exact actual-law controls passed |
| Four global improvements | Conditional theorem from stated coarse inputs | Fresh 40 exact rational gates passed |
| One-pass panel exports | Derived formulas for the same actual-law parameters | Fresh complete 30-panel evaluation passed |
| Incoming .6 strips | Conditional on retained all-threshold heat/ray/contact/predecessor theorem | Both rays passed on exactly 13 panels |
| Central-panel input connection | All listed premises strictly improved | Eight scalar joins and two joint-resource intercept joins checked |
| Remaining high-noise/count/BASE41 | Open, unchanged | Not accepted or executed here |

The negative control is a genuine law: centered atoms
`(-7/20,3/40),(-43/180,27/40),(3/4,1/4)` (node,mass).
It refutes replacing the minimum of the two sign prices by their maximum.
After clearing the positive variance factor, the false inequality's reserve is
`7/108000-(7/6000)sqrt(10)<0`; the valid reserve is
`(1+sqrt(10))/12000>0`. Thus noise on different signs cannot simply be charged
at the more expensive rate. The test suite also covers symmetric and skew
Bernoulli, reflections, nearby four-point laws, very small rare atoms,
large outward jumps, exact atom mergers, and an explicit zero-atom rejection
because the central-gap hypothesis excludes such an atom.

## Fresh evidence and reproduction

From the repository root:

```sh
python3 -I -B mathematics/simplification-v10/2026-10-28/geometry-run.py NEW_UNUSED_ID
```

The driver refuses an existing run directory and writes stdout, stderr,
source/proof hashes, Python version, durations and return codes. It runs only
three bounded pure-rational programs; no constructor/Fourier import or native
certificate campaign is involved. Assertions must remain enabled.

Selected result: `runs/geometry-v10-20261028/final05/`.
The initial floating-point discovery is separately labeled in `geometry-explore.py`
and `explore01/`; it is not used by acceptance. Earlier gated runs are preserved
without being relabeled as final. `build04` compiles the full proof in six pages,
with no final warnings; every rendered page was visually inspected. The final
PDF and source hashes are in its receipt and `visual-review.json`.

## Exact dependency removal

For these conclusions, the old `moment-entry-v8.py` eight-round recurrence and
its traces are unnecessary. Replace them by the direct global lemma and the
single evaluation specified here. Retain:

1. The selected v7 coarse entry, its complete cover, actual support gap,
   support radius and weighted nD output.
2. The actual-law outer-gap inequality and common residual measures, fully
   derived in the new note.
3. The all-threshold heat/ray theorem for the .6 strip, with its fixed-target
   contact, nonnegative excess, n>=42 and sharp-predecessor hypotheses.
4. The original separate raw-threshold and signed phase resource inputs to
   central-panel confinement.

An arbitrary old per-panel bound is not automatically dominated. Any later
phase/count program that reads an old individual moment interval needs an
input-by-input comparison or a rerun on the new interval. No old file or
certificate is deleted. This component does not remove half-amplitude
confinement, close the shifted-anchor count comparison, or prove BASE41.

The separate independent review found no blocker at the final source hashes.
Its commits are `8afb87ed8f9e89002d4ec67b740290e6594d036a` and
`f9ab4eebe4a1bea364b3d8d9a9d00471a517a744`. It reconstructed all four quartics
and both cubics, and checked the new joint constraints and central triangle
containment. The review and integration recommendation belong to the
coordinating agent; this constructor report is not independent acceptance.
