# Acquisition and local-exclusion audit

Audit date: 27 October 2026. Repository: `kolodziejek/berry-esseen-certificates`.
Reference commit: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
Working branch: `audit/acquisition-20261027`.

This is a bounded dependency/interface audit, not a fresh certification of the
analytic or numerical tail theorem. No inherited driver was executed, no
certificate was changed, and no proof obligation was removed. The historical
reviews were used as finding aids, not as authorities for their conclusions.

| Result | Mathematical status | Execution status |
|---|---|---|
| The first-counterexample scalar hypotheses fit the literal acquisition and local-exclusion statements, including the equality case | Locally checked conditional implication | Exact source inspection; no inherited numerical acceptance run |
| Uniform acquired entry and complete LOCAL47 | Supplied analytic/certificate implications; retained premises | Historical acceptance records exist; not freshly rerun here |
| Complete conjecture, unconditional LOCAL47, or certificate deletion | Not established by this audit | Not attempted |

## Source convention and a material omission in the short supplement

Line numbers below refer to the files at the reference commit, not to the
original manuscript's `M...` numbering. `S` means
`paper/analytic-supplement.txt`. `Z` means the checked-in archive
`verification/finite-tail/sources/BE_cutoff49_20260930.zip`; paths following
`Z:` are archive members, read directly without importing their code.

The supplement index maps S7 to original M7458–7506 and S8 to M7647–8887.
The intervening global/entry assembly is not imported there. The short
`paper/main.tex:465–476` description therefore does not suffice for an exact
acquisition audit. The actual uniform statement and its ordered schedule are
present in:

* `Z:BE_cutoff49_20260930/paper_entry/resource_entry.tex:375–420`;
* `Z:BE_cutoff49_20260930/paper/sections/global_route.tex:81–115`.

Fresh read-only SHA-256 identification of Z:
`ecdb9acca0db29efc9fe2bf496c0bcc61b4881aecdcbc91a4eb6ad49b920c72e`.
The first member above has SHA-256
`7912da195c21455eeb3fcb1a023c1fa597c7989e925a9599af83fe82bc3dd60a`;
the second has
`6c1715274ef031db7558070ea9f3540cd72df2e2a6a87282828cf04c75b6dfa2`.
These hashes identify bytes; they do not establish the lemmas.

## The literal local interface

The archive's Proposition `global:local` states that no integer `n>=47` can
satisfy all of

\[
0\le C_n-C_E\le .7/n,\qquad
\delta_n=n(C_{n-1}-C_n)_+\le .19,\qquad
C_n<.4247,\quad C_{n-1},C_{n-2}<.4253.
\]

It explicitly includes `C_n=C_E`. Its proof invokes attained positive closed
contact, initial radius 3.84, the complete 83-panel acquisition, and the local
comparison. The corollary `re:acquired` in the first archive member states the
same conditions with non-strict numerical caps `C<=.4247` and deleted caps
`<=.4253`. It has no upper bound on `n`, **given** the shared support/strip
implications and the checked finite schedule. Thus the stricter scalar caps
from a first counterexample satisfy this acquisition interface.

Here `delta_n` is a global predecessor decrement. It is not the physical
Esseen defect `D`, the inward gap `d_Y`, or the noise `lambda=n E U^2`.
For the selected law, its same-law allowance is no larger than `delta_n`.
None of these other quantities becomes zero because `delta_n=0`.

## Hypothesis-by-hypothesis dependency table

Every conditional numerical row below must retain its complete source-bound
acceptance obligation. The table checks applicability and ordering; it does
not assert that the corresponding arithmetic has freshly passed.

| Edge | Exact premises and conclusion | Source and first-counterexample disposition |
|---|---|---|
| Attainment and orientation | Fixed integer `n`; standardized law class with finite third absolute moment; unrestricted supremum. Produces a positive **closed** maximizing pair, including `C_n=C_E`. Moving thresholds and weak products are handled before support. | `paper/main.tex:102–139`, S:218–288. Retain. The source proves lower-order uniform integrability and obtains third-moment equality from extremality; it does not infer third-moment uniform integrability merely from bounded moments. |
| Same-law predecessor | `R_(n-1)(P)<=C_(n-1)<=C_E<=C_n` implies `q_n(P,C_n)=0`; globally `delta_n=0`. No predecessor contact or optimizer is needed. | `paper/main.tex:173–193`. Locally checked direct implication. Sharp predecessors supply exactly this edge. |
| Contact on the whole support | The same maximizing law and raw threshold remain fixed; contamination is standardized while the raw event is held fixed. Contact is nonpositive everywhere and zero on closed support. | `paper/main.tex:142–171`, S:290–348. Retain. Atoms and reflected negative discrepancy cannot be replaced by a smooth density argument. |
| Coarse moment caps before bounded support | `C_n>=C_E>.4095`, published finite structural bounds, exact sign-moment inequality. They supply `rho<1.85` and an admissible `abs(beta)` bound. | S:583–605; `Z:.../paper/sections/overview.tex:48–60`. Retain the structural inequalities. Sharp predecessor bounds do not imply moment caps on their own. |
| Initial support 3.84 | Nonnegative excess (`K=0`), decrement `<=.19`, attained contact, the just-acquired moment caps. Six index bands `[45,49]`, `[50,59]`, `[60,89]`, `[90,134]`, `[135,199]`, `[200,infinity)`; only `n>=47` is applied. Full radial cells and both far rays must pass. | S:566–651. The first-counterexample assumptions fit, but support computations remain necessary. In the infinite band the favorable `D_-` term is set to zero. This is separate from every finite-base support row in S:652–668. |
| Fourier/resource initialization I | `n>=47`, actual `abs(X)<=3.84`, `C_E<=C<=.4247`. Complete signed cover; a first raw bound below `.4*47` must license Gaussian-weight removal before defect feedback. | S:2238–2287, 2550–2585; `Z:.../paper_entry/resource_entry.tex:64–83,375–382`. Retain full LOW/HIGH and initialization. Its selected outputs are raw `<1.885`, weighted `nD<47*.590`, and 100 closed probability cells, 35 surviving. |
| Central preparation C | Consumes I, first computes 10 broad cells `[.38,.48]`, excludes the last, proves radius 2.5 by contact from the **preceding** row, then refines 45 cells `[.38,.47]`. | S:719–785; `Z:.../baseline/certificates/work/below50_20260929/entry/accept_central47.py:22–81`. The own/excess/decrement inputs fit. Retain both preparation and contraction. |
| Complement L | I plus complete 125-cell cover `[.25,.38] union [.48,.60]`; all other INITIAL probability cells are already excluded. Surviving left laws are contracted to radius 3 using acquired `rho<=1.390`, `abs(beta)<=.430`, then refined to 39 panels `[.302,.38]`. | S:786–794; `Z:.../baseline/certificates/work/below50_20260929/entry/ENTRY47_DAG.md:16–38`; resource enclosure proof S:2550 onward. Keep complete complementary exclusions and their signed phase repair. |
| Coordinate strips | `n>=47`, `0<=C-C_E<=.7/n`, decrement `<=.19`, previously acquired radius and simultaneous `rho,beta,H` bounds with nonnegative beta lower endpoint. Contact is checked on every forbidden closed coordinate cell, including singletons, yielding `-.55<Y<1.55`. | S:719–794. This is a real consumer of the excess cap. The stronger `.3/n` suffices but does not remove the strip certificate. |
| First confinement C1 | Original canonical C row and strip; `Y=B+U`, conditional centering, `p<1/2`; panel `theta,d,rho,beta,lambda,H` bounds; `.4<C<=.4253`; actual contact derivative; **both** deleted-convolution concentration caps; one common strict resource budget. | S:6533–6620, 6683–6945. First-counterexample predecessors supply the two deleted caps; conditional support/resources still come from C. Retain the confinement certificate and signed deletion. |
| Antichain confinement and C2 | Strict interval diameter `<1-d`, conditional-label gap, both full/deleted indices `j>=n-2>=45`, finite binomial mode bounds; original C input, then intersection with C1 and resource feedback. | S:6621–6686, 6935–6945; `Z:.../paper_entry/resource_entry.tex:387–400`. C2's confinement consumes **C, not C2**, so the declared schedule is acyclic. Sharp predecessors do not eliminate antichain or moment gates. |
| Separate sign resource S and left L2 | C2 plus L; preserve weighted `nD<=47d`, separate sign-variance prices and all coherent quadratics. S removes one left cell; left acquired `rho<=1.2563`, `abs(beta)<=.3926` permits contact radius 2.7, then 38 left panels `[.304,.38]`. | S:786–794, 3547–3894; `Z:.../paper_entry/resource_entry.tex:391–420`; `Z:.../entry/ENTRY47_DAG.md:61–102` under the long baseline prefix. Retain. Unweighted `theta` cannot be multiplied by 47 to bound noise at arbitrary n. |
| Common acquired local input | 45 central plus 38 left panels, common endpoint `.38`; each has its own `Theta,d0,Lambda`, signed `H` bounds, amplitude and four coherent budget quadratics. Current law and threshold are unchanged. | S:7691–7710; `Z:.../paper_entry/resource_entry.tex:402–439`. This is the complete target of acquisition, not a consequence of scalar bounds alone. |
| Parameterized comparison | Actual same-law count identity; conditional centering; support `abs(U_j)<=A`, inward `d0<min(p,q)`, `d0<=A`; legal nearest count, both ties; positive binomial mass lower bound; sign gates on outgoing loss or whole-count coefficients. | S:7107–7201. Retain all count, mass, normalization and repair inequalities. The global predecessor zero does not make the conditional noises vanish. |
| TINY | `N=47`, `p in [.304,.47]`, `abs(H)<=1.393`, `Theta=.0154`, `d0=.0181`, `A=.425`, `0<lambda<=.05`; every nearest phase. Bounds are relative to lambda. | S:7732–7745 and scaled-witness derivation preceding it. Retain. A fixed additive error cannot replace this branch near zero. |
| MID and LOW | Noise/phase cover in S:7712–7755; central MID complements at `.09,.13,.18,.29`; left `.09,.14,.19`, then negative-only `u<=-.29` on `[.10,.12]`; a separate positive-left LOW covers `[.29,.5]` there. All intervals clip to each row's Lambda and include shared endpoints. | S:7691–7755. Retain all six comparison families and coverage. In particular ordinary left MID does not cover the positive fourth-band complement. |
| Zero noise and Bernoulli comparison | Conditional centering plus `lambda=0` implies both noises vanish. The actual law is Bernoulli. At an attained positive closed maximum its threshold is an atom. Schulz's separate all-parameter strict finite-binomial theorem excludes it; the same theorem also closes positive noise. | S:7757–7768; `Z:.../paper/sections/global_route.tex:98–105`. Retain external binomial theorem; do not reintroduce the superseded finite `47..98` binomial restriction. |

The archive member abbreviations `Z:.../paper...` in this table all start at
`BE_cutoff49_20260930/`. For `ENTRY47_DAG.md`, the full prefix is
`BE_cutoff49_20260930/baseline/certificates/work/below50_20260929/`.
That DAG is only a locator/summary; the mathematical enclosure and confinement
arguments, with their hypotheses, were read separately above.

## Two executable semantics that must survive any redesign

1. **The apparent upper index 98 is not a tail cutoff.** The native acceptor
   `Z:BE_cutoff49_20260930/baseline/certificates/work/below50_20260929/entry/accept_initial47.py:12`
   sets `n=47,nmax=98,barrier=0`. Its imported `local_signed_core.py:22,29`
   uses `nmax` only in the floor-order guard and `.4095+K/nmax`. At `K=0`
   the latter has no upper-index content. This inspection supports the precise
   explanation in `resource_entry.tex:414–417`; it does not prove every
   index-dependent Fourier bound, which remains a retained analytic/gate
   obligation. A generic `nmax=98` label must neither truncate the theorem nor
   be silently ignored in a positive-barrier application.

2. **The phase repair is shared with acquisition.**
   `Z:BE_cutoff49_20260930/legacy_phase/corrected_phase_callback_v2.py:3–25`
   replaces curvature by
   `C*rho+min(phi_low*g0,.4*g0)/2`, where `g0=3.16*rho-3-d`.
   `accept_phase_corrected_v3.py:21–36` rechecks all PREP targets and all
   125 complement cells, including every survivor's numerical resource;
   merely preserving exclusion counts would be insufficient.
   `check_later_phase_premises.py:21–55` covers 302 later input domains
   across six named jobs to license the old positive-skewness phase formula.
   These checks remain consumers even if the separate strong46 barrier is
   removed from a new global proof. Their historical common directory is not
   a mathematical reason to delete them.

## What the first-counterexample argument can replace

Conditional on the same numerical and analytic acquisition/exclusion premises,
suppose all indices through 46 have the weak sharp bound. For a least violating
index `n>=47`, all earlier indices give `C_(n-1),C_(n-2)<=C_E` and `delta_n=0`.
The support-free recurrence yields the roadmap's exact scalar estimate

\[
n(C_n-C_E)<\frac{335909}{1150000}<.3,
\qquad C_n<.41+.3/47<.4247.
\]

This fills every **scalar** input of `re:acquired` and `global:local`. The
acquisition/support/resource/count premises remain exactly those in the table.
No edge from strong46, the three-loss step, or an independent global positive
ceiling to those conditional lemmas was found in their stated proofs. The
legacy entry DAG's use of the `.7/n` ceiling from index45 is a provider of
these scalar inputs, not an additional premise such as attainment at index45.

This supports a proposed replacement of the independent tail **assembly** by
a conditional first-counterexample assembly. It does not yet support deletion
of files or of all coarse-cap computations: the finite 43–48 proof has its own
consumers, and a whole-program dependency/certificate inventory is separate.
In particular:

| Proposed removal | Interface-audit verdict and reason |
|---|---|
| Strong46 support/barrier and the three-loss bootstrap as premises of the *new global upper proof* | Conditionally unnecessary once the weak sharp finite base and retained LOCAL47 are supplied: no strong46 premise occurs in the entry/local statements; least failure supplies their scalar inputs directly. Preserve the original independent tail theorem and its proof objects. |
| Independent `.7/j` ceilings as *providers of the new tail's scalar caps* | Conditionally unnecessary for this specific consumer. Earlier sharp bounds plus smoothing replace them. They may remain required by retained finite43–48 or other theorem consumers. |
| Finite47/48 as mathematical base obligations | Potentially unnecessary if the complete sharp base through46 is available independently of 47/48 and the retained local theorem is supplied. Do not infer that a fixed 43–48 certificate bundle may be truncated without a new declared composition and coverage audit. |
| Initial3.84 support, central/left contractions, strip, resources, phase repairs, confinement, TINY/MID/LOW | Still necessary on the examined route. Zero predecessor decrement supplies no replacement inequalities for these laws. |
| Reserve `.001*lambda` | Not needed merely to deduce `C<C_E` if an independently established weaker local comparison suffices, but changing that target would be a new theorem/certificate task. This audit authorizes no weakening. |

There is a useful strictness correction to the proposal: choosing the least
index with `C_n>C_E` proves only the weak global result. Here the actual local
and acquisition statements **also cover equality**. With a weak base through46,
one may instead choose the least `n>=47` with `C_n>=C_E`. All earlier tail
indices are strict and both relevant predecessors are at most `C_E`; the same
scalar computation applies. Conditional on the retained local theorem, this
proves the strict tail `C_n<C_E` for `n>=47`. It does not make the finite base
strict, and it does not establish a standalone tail independent of that base.

## Negative controls and remaining verification boundary

A literal normalization transcription in `paper/main.tex:163` should be
corrected in a separately reviewed edit: the derivative of the normalized
score is **`I(y)`**, not `rho I(y)`. This agrees with S:297 and follows
independently by writing the varied score as
`sqrt(n) v_epsilon^(3/2) D_epsilon / r_epsilon`. At zero,
`v'=y^2-1`, `r'=abs(y)^3-rho-3 beta y`, and
`sqrt(n) D'=n^(3/2)(F_(n-1)(H-y)-F)+n y phi(z)+H phi(z)(y^2-1)/2`.
Its derivative is therefore the right side of the defining equation
`paper/main.tex:148–151` divided by `rho`, namely `I(y)`. Since `rho>=1`,
the sign and zero-set arguments, contact majorant and ensuing support
conclusions are unchanged. This is a transcription issue, **not** a failed
contact lemma or a new counterexample. The original source was not edited.

The following boundary checks were analytical source checks, not new runs of
the inherited acceptance code:

* Equality at `C_n=C_E` is permitted by attainment, entry and exclusion.
* `n=47` leaves the two deleted indices 46 and 45, both inside the proposed
  finite base; the concentration proof uses `n-2>=45` explicitly.
* Zero noise has its own Bernoulli argument; positive noise can be arbitrarily
  small and uses the scaled TINY witness.
* Exact count ties and probability/noise/phase boundaries belong to the closed
  cover; the positive-left fourth-band exception has a separate LOW consumer.
* A tiny atom outside a proposed radius is not discarded: contact must exclude
  every support point and the complete far rays before moment refinement.
* Confinement is established from a preceding resource row and only then used
  for feedback; replacing that input by its own improved output would be circular.

No new acceptance run, mutation run, full public `full_pass`, or independent
rederivation of every Fourier estimate is claimed. The analytic proofs and
native gates below these interfaces remain explicitly retained. This audit
finds a conditional dependency simplification, not an unconditional proof or
a counterexample to Berry–Esseen. The next reviewable step is a new assembly
statement with the retained local predicate list and a separate inventory of
all finite43–48 consumers; existing statements and certificates should stay
unchanged until that proposal is reviewed.
