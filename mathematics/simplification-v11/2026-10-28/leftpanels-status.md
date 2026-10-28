# Wider support strips on the left probability panels

Base commit: `6027b27f85473780eaf90542f490168873de5986`.
Branch: `research/leftpanels-v11-20261028`.
This component changes only its new proof, checker and evidence. It does not
edit the manuscript, prior certificates, reference baseline or external services.

## Result and exact scope

The retained contact and heat/ray argument proves, on every closed panel
25 through 39, the asymmetric conditional support bounds

`-.6 < U_0 <= a_0`, `-a_1 <= U_1 < .7`, `a_0+a_1=d<.068`.

Thus `|U_j|<.7` holds on the whole left probability interval `[.25,.40]`.
Combined with the existing `.6` strip on panels 40 through 52, a common `.7`
amplitude is now available on every retained panel 25 through 52. The actual
left endpoint is already excluded by the strict geometric `p>1/4` result;
keeping the closed endpoint in a sufficient domain creates no gap.

The hypotheses remain the selected v7 coarse entry, the direct v10 geometry
export, an attained fixed-target witness with nonnegative excess, actual
index `n>=42`, sharp predecessor, and the retained all-threshold heat/ray
lemma. Moment bounds alone do not imply these support exclusions.

The positive-ray boundary margin exceeds `.27` on every left panel, and the
negative-ray margin exceeds `.3`. All continuation and `t>sqrt(3)` gates
are strict. Whole rays, not only the boundary points, are excluded.

## Consequences for the count route

For common amplitude `A=.7` and displacement ceiling `d_0=.068`,

- `A+2d_0=.836<1`;
- the shifted phase interval is `[-.218,.782]`;
- crossing separation is `.932` and the amplitude slack is `.082`;
- the retained `|H|<=1.83605680` and scale bounds ensure legal interior
  counts for every `n>=42` on all left panels;
- `s=theta/ell^2` and `lambda=ns=n*theta/ell^2`, as in the count theorem.

This supplies a missing support premise. It does **not** prove the count
inequality, nor authorize reuse of the earlier `p>=.4` normalization constants.

Schulz's sharper Bernoulli theorem yields a uniform weighted reserve
`rho_B*(CE-C_B)>.00059` on `[1/3,.4]`. Below `1/3` this component retains
only the global strict Bernoulli theorem, with no claimed positive uniform
reserve. Panel 33 crosses `1/3` and must be split before applying the sharper
formula. No gap formula is extrapolated beyond its theorem's scope.

An exact actual-law control shows why the left extension needs a new repair
estimate: take `p=13/50`, `U_1=0`, and `U_0=+/-1/1000` with equal conditional
probabilities. Its standardized third moment satisfies `rho<rho_B`, although
`d=.001` and `lambda=.00003108` at `n=42`. Thus the favorable moment repair
used for `p>=.4` cannot simply be discarded on the enlarged domain. This law
is not claimed to satisfy contact and is not a counterexample to a count theorem.

## Mathematical and execution status

| Component | Mathematical status | Execution status |
|---|---|---|
| Left asymmetric strip | Locally derived implication under the retained entry/contact/predecessor hypotheses | Fresh exact checks of both rays on all 15 closed panels |
| Whole-ray continuation | Proved from the retained heat derivative bound and polynomial signs | Eight strict gates on each of 30 rays |
| Shifted-anchor feasibility and legality | Complete domain calculation | Exact rational PASS |
| Bernoulli reserve on `[1/3,.4]` | Deduction from the external Schulz theorem at its stated scope | Rational lower bound PASS |
| Favorable moment repair on all left panels | Refuted for arbitrary laws in the proposed count domain | Exact three-point counterexample PASS |
| Count comparison on the enlarged domain | Not proved by this component | Not claimed or run |
| Full sharp conjecture and `BASE41` | Unchanged | Not accepted here |

## Evidence and reproduction

The frozen input is
`runs/geometry-v10-20261028/final05/geometry-panels.py.stdout.json`, SHA256
`2980009e801c9bc7bb1ab15edca2edd6782241e5151986ed269a961fefb8dcd4`.
Its exact panel values are outputs of the already proved one-pass geometry
formulas. This component does not reaccept the earlier Fourier cover.

Exploration tested only `.65` and `.7` from the permitted five-value list,
then stopped at the first common success: 30 positive-ray evaluations.
At `.65`, panels 29--33 fail only the sufficient boundary estimate. The first
obstruction, on `[.29,.30]`, lies strictly between `.010460` and `.010461`.
This is a failure of that bound, not a counterexample to a `.65` strip.

The acceptance checker reconstructs all selected boundary and continuation
expressions directly. It uses 31 ray evaluations, including the first failed
`.65` control. Missing, duplicate, reordered and corrupted-endpoint cover
mutations are rejected. The rho counterexample uses exact rational moments;
no rounded atom locations or floating event probabilities enter acceptance.

From the repository root, run:

```sh
python3 -I -B mathematics/simplification-v11/2026-10-28/leftpanels-run.py NEW_UNUSED_ID
```

The driver refuses an existing run directory and records commands, source
hashes, Python version, duration, return code, stdout and stderr. Assertions
must remain enabled. Selected evidence is under
`runs/leftpanels-v11-20261028/{discover01,check01,build02}`.
The four-page proof compiles without warnings; all four final pages were visually
inspected. The first build is retained as a historical layout check. No
constructor campaign or Fourier rerun was launched.

## Dependency change

The left-panel support gap in the proposed direct count route is removed:
replace “only the negative ray passes on panels 25--39” by the complete
asymmetric strip above. The original `.6` positive-ray test genuinely remains
insufficient there; no old target is relabeled. On the new count route a
separate half-amplitude acquisition is unnecessary **as a support premise**
once its count estimates have been established for `.7` amplitude.

The count estimates themselves, the selected coarse entry and its certificates,
the actual contact and heat/ray hypotheses, and a genuine finite base remain
obligations. No existing proof component is deleted.
