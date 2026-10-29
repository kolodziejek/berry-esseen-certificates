# Decision audit of the Argon unification proposals

Date: 2026-10-27. Source revision: `ca4943a` on the user's fork. The preserved
original research baseline is `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
All source locations below refer to `ca4943a`, except where explicitly marked
as the changed smoothing chapter. Paths are relative to the repository;
`M` abbreviates `manuscript/arxiv-v1`.

The two supplied proposals are referred to as **P** (the 170-line
`MANUSCRIPT_REVISION_INSTRUCTIONS.md`) and **A** (the pasted accompanying
analysis). Their byte hashes are in the run metadata. Statements described
as mandatory author instructions inside those files are proposals, not
authorization. No page budget justifies deleting an unverified dependency.

## Result and scope

The general sharp-predecessor and least-failure argument is valid, with an
explicit index-dependent excess bound, equality handling, and no second
deleted index at `n=2`. That is the only manuscript change made here:
`M/sections/03-smoothing.tex`, preserving its existing theorem labels and
the full one-step derivation and floor-42 conclusion.

Two proposed algebraic identifications are false. The deletion-factor
comparison has the opposite sign for **every** integer `N>=3`; the shifted
quartic is the `c=2` case, not `c=1+sqrt(3)`. A third proposed replacement
loses the actual strict margin in the retained `n=4` support calculation.
None is a counterexample to the Berry--Esseen conjecture.

| Result | Mathematical status | Execution status |
|---|---|---|
| Parameterized predecessor entry and least failure | Locally derived from the unchanged smoothing recurrence and attainment lemma | Exact scalar checks fresh PASS; changed TeX compiled; see receipt |
| Reversed deletion comparison and unsafe replacement factor | Refuted proposal by exact universal algebra and rational examples | Fresh PASS of rejection checks |
| Proposed quartic specialization | Refuted proposal by coefficient comparison | Fresh PASS of multiplication checks |
| Universal cubic substitution in the retained n=4 endpoint proof | Does not close that proof; exact positive residual after substitution | Fresh PASS |
| New floor 20/25, direct exact-binomial finite closure, or complete global proof | Conditional research proposals, not established by this audit | No native certificate or cover run |
| Existing finite/Fourier/count predicates | Retained at their original scope | Not rerun; no execution upgrade |

## 1. Valid general first-failure reduction

P55--65 has a correct scalar core. Write `c=CE`,
`s_n=sqrt(n/(n-1))`. The unchanged recurrence at
`M/sections/03-smoothing.tex:21--68` gives, for every `n>=2` such that
`C_{n-1}<=c<=C_n`,

\[
0\le n(C_n-c)\le\varepsilon_n,
\qquad
\varepsilon_n=\frac n{n-1}
 \left\{\frac c{s_n+1}+\frac{s_n}{15}
                  +\frac{2s_n}{25\sqrt{n-1}}\right\}.
\]

Indeed `n(s_n-1)=n/((n-1)(s_n+1))`; multiplying the other two terms
of the recurrence by `n` gives `s_n^3/15` and
`2s_n^3/(25 sqrt(n-1))`. Also
`R_{n-1}(P)<=C_{n-1}<=c<=C_n` for **each** marginal, so both positive
predecessor losses vanish. No optimizer-specific comparison is inferred
from a comparison of unrelated optimizing laws.

The bound decreases with the index. Express it as

\[
 c\frac{s^2}{s+1}+\frac{s^3}{15}
       +\frac{2s^3\sqrt{s^2-1}}{25},\qquad s=s_n>1.
\]

All three terms increase with `s`; the derivative of `s^2/(s+1)` is
`s(s+2)/(s+1)^2>0`, and `s_n` decreases. Thus `epsilon_n<=epsilon_N`
for `n>=N>=2`. This is an analytic proof of monotonicity, not an inference
from the finite list of checked indices.

The existing floor-42 rational proof is unchanged:
`s_n<81/80`, `sqrt(n-1)>6`, `c<41/100`, and therefore

\[
 \varepsilon_n<\frac{42}{41}
 (41/200+27/400+27/2000)=3003/10250<3/10.
\]

It still gives `C_n<73/175<2113/5000`. At floor 40, the simpler bounds
`s_n<40/39`, `sqrt(n-1)>6` give
`epsilon_n<2239/7605<61/200=0.305`. This extra scalar specialization
does not verify a floor-40 resource or support calculation. At index 5,
`C_4<=c<=C_5` suffices for zero loss, independently of any floor-42 proof.

For a general integer `N0>=2`, assume the sharp weak prefix `C_j<=c`
for `1<=j<N0`. If the strict conclusion fails above that prefix, choose
the least `n>=N0` with `C_n>=c`. Earlier tail indices satisfy `<c`, and
the prefix satisfies `<=c`. Hence the entry lemma applies. When `n>=3`
both `C_{n-1}` and `C_{n-2}` are defined and at most `c`. At `n=2`
only `C_1` is used. Fixed-index attainment supplies the extremal pair
to an independently established exclusion theorem at this **actual** index.

Choosing the least `C_n>c` instead establishes only a weak bound, even if
all those violations are excluded: an abstract sequence with a term equal
to `c` is a countermodel to the logical inference of strictness. A59--60
must not turn zero loss *at a selected least failure* into zero loss for
every index of an arbitrary sequence. Likewise a sharp prefix is a premise,
not an output of this scalar lemma. In particular A58's statement
`C_1=2/5 is trivial` is unsupported by the manuscript: the actual result
is a conditional **upper bound**, with a 150-cell premise at
`M/appendices/finite-analysis.tex:777--808`. This audit does not purport to
refute that equality by identifying the actual exact value of `C_1`.

**Dependency-removal consequence.** The scalar positive-loss premise at
a least failure may be replaced by zero in a **new** composition, after
checking the downstream hypotheses. The separate support, moment, Fourier,
phase and count implications remain. The old n=2 and n=3 targets
`2 sqrt(2)/7` and `59 sqrt(3)/250` are strictly below `CE`; a sharp
least-failure exclusion at `CE` alone does not establish those stronger
targets or license their existing finite consumers. The zero-loss part of
the fifth-index lemma (`finite-analysis.tex:2091--2108`) is a direct
specialization, but its attained-pair and compact-support conclusions still
need attainment and contact. No historical proof or certificate is removed.

## 2. Refuted deletion-scale comparison

P116 claims `(N/(N-1))^3 < N/(N-2)` for all `N>=3`. Direct subtraction gives

\[
 \left(\frac N{N-1}\right)^3-\frac N{N-2}
 =\frac{N(N^2-3N+1)}{(N-1)^3(N-2)}>0.
\]

For integer `N>=3`, `N^2-3N+1=N(N-3)+1>=1`. Thus the proposed
direction is always wrong. At `N=3`, it says `27/8<3`. Moreover the
error changes the accepted parameter domain: `Fd=9/5` satisfies
`Fd^2>3` but not `Fd^2>27/8`. At the manuscript's floor 42, `Fd=103/100`
satisfies `Fd^2>42/40` but `Fd^2<(42/41)^3`.

The retained requirements are explicit at
`M/appendices/uniform-bridge.tex:85--93`,
`M/appendices/fourier-analysis.tex:3417--3421`, and
`M/appendices/finite-analysis.tex:3337--3340`. A genuinely general
version could replace their maximum by the **larger** first term:
`Fd>0` and `Fd^2>(N/(N-1))^3` for `N>=3`.
It must still retain both deleted-score caps, same-law concentration,
strict interval widths and every confinement gate. This is a valid scalar
simplification, not a proof of confinement at floor 25.

## 3. Universal Gaussian estimate versus a quantitative support theorem

The universal cubic estimate in P70--73 is already proved at
`M/appendices/finite-support.tex:278--326`; the derivative bound is proved
at lines 86--102. Its scale identity can be checked directly:
`n=s^2/(s^2-1)` gives

\[
 ne_n=\frac{s^2(2s+1)}{2(s+1)^2}.
\]

These estimates are legitimate common analytic building blocks. They are
not by themselves support theorems: contact, a positive score floor,
actual moment bounds, predecessor allowance, and negative boundary/ray
polynomials are explicit at `finite-support.tex:51--113`.

There is a concrete obstruction to P75's claimed immediate replacement of
the n=4 proof. The n=4 estimate at
`M/appendices/finite-analysis.tex:1527--1551` has constant remainder
`1/15`, whereas the proposed universal replacement has `1/2`.
The retained endpoint polynomial at radius `101/25` has value
`-51557/9765625` (lines 1572--1580). Replacing only this remainder yields

\[
 -51557/9765625+1/2-1/15=25081283/58593750>0.
\]

Thus this direct common-bound substitution loses the strict endpoint
needed to prove the acquired radius. This does not refute the true radius
or rule out a new sharper common estimate; it refutes the asserted immediate
proof replacement. The existing n=4 proof must remain unless the lost
margin is repaired rigorously. The n=2 and n=3 support proofs also carry
their own score/predecessor and moment caps (`finite-analysis.tex:893--914`
and `1153--1185`), which are not supplied just by a bound on `H_n`.

P76's all-index exterior-ray assertion lacks these parameters. For example,
the actual direct-contact theorem has a term `r S q`; an arbitrary positive
predecessor allowance cannot be discarded. A Gaussian estimate alone
cannot exclude support of all standardized laws (a standardized Gaussian
has unbounded support). Under an extremal-pair interpretation, its listed
moment and ray gates, not that example, are the missing premises.

Nor are the finite fifth-order bounds merely a dispensable repeated
fourth-order proof. `finite-support.tex:163--277,328--345` retains a
favorable term `-3D_-` with `D_-=(u^5-15u)/(120(L-1))`; at an infinite
upper index this becomes zero. The denominator gate `W_*>0`, the
second envelope gate, the finite remainder and threshold series need
their full derivations. Its positive-budget index-27 invocation
(lines 146--161) also has a different target and explicit endpoint cells.
The new zero-loss N42 support theorem does not replace these ancestors
without a new composition and complete coverage proof.

## 4. Quartic family: useful unification, wrong proposed parameter

P123 states that `c=1+sqrt(3)` in `Q_{a,c}=x(ca-x)(x+a)^2` gives the
shifted quartic. In fact

\[
 Q_{a,c}=-x^4+(c-2)ax^3+(2c-1)a^2x^2+ca^3x.
\]

The shifted quartic is `-x^4+3a^2x^2+2a^3x`, hence exactly `c=2`.
At `a=x=1`, the proposed specialization gives `4 sqrt(3)` instead of `4`.
The source already identifies `c=2` at
`M/appendices/finite-analysis.tex:314--345,2485`; the shifted version and
its independent-sum moment substitutions are at
`M/appendices/fourier-analysis.tex:3721--3738`.

One may prove the family once and retain the shifted result as a corollary,
but must preserve independence and centering for
`|E W^3|<=A t`, `E W^4<=A^2 t+3t^2`, the strict outgoing event,
`a>0`, and the normalization `K0>=(9+6sqrt(3))/4`. Tiny positive noise
does not permit division by zero at zero noise; the Bernoulli boundary
has its own comparison.

## 5. Decisions on the remaining proposed deletions

| Proposal | Decision and exact hypothesis boundary |
|---|---|
| P81--99: defect and weighted-joint reprints | Genuine deduplication candidates. The displayed joint theorem at `fourier-analysis.tex:1615--1649` already applies main `ms:joint-resource` with the same `nD<=Nd_D`, positive endpoint floors, `Theta<1`, nonnegative offset and positive coefficients. Move its label to the main theorem or keep a short exact application; retain negative/zero residual cases and outward intercept directions. The central-gap decomposition at lines1534--1560 can likewise cite the same main formula with a genuine central gap. |
| P85: resources joint-plane application | A valid short application of the main theorem can replace the repeated weighted calculation. Preserve `d_new=min(d_old,B*/(kappa N))`, actual weighted bound, rational lower `b*,K`, positive `A+B`, upper `v*`, and all three signs of the residual. Do not delete the displayed numeric coefficients used by later consumers. |
| P94--95/A68--69: one Fourier transfer | Shared Taylor algebra can be stated once. The triangle finite-window majorants have nonnegative weights and may be integrated over the larger Gaussian domain to produce corresponding triangle bounds. This is **not** a theorem obtained by taking the Taylor-validity interval to infinity. Both proofs restrict the expansion and modulus comparison to `[0,1/2]`. The signed cancellation triple uses the actual `(z,c)` rectangle and the exact `J` norm; replacing it by the triangle triple generally weakens it. Preserve the two complete coefficient triples and their consumers. Source: `fourier-analysis.tex:798--1040,1059--1145`; sign-aware finite rectangle: `finite-analysis.tex:2542--2654`. The finite-window version also acquires its own sixth moment from bounded support and Pearson residual; the signed transfer allows any correctly acquired sixth-moment bound. |
| P98: second propagation theorem duplicates enclosure theorem | Not verbatim duplication. `fourier-analysis.tex:1713--1748` proves a within-schedule enclosure implication. Lines3023--3069 additionally prove pooling by interval hulls, empty active-family handling, retention of earlier exclusions, and simultaneous signed fields before another cover. A merged theorem must include those operations and their proof. Merely deleting the second theorem loses those interfaces. |
| P84/P99: move positive-measure prices and atlas | Moving definitions and proofs is editorially possible. Their common residual cannot be spent separately and added. Conditional Taylor, signwise Gram, signed-moment penalties, acquired endpoint floors, positive divisors, and coherent corner formulas are different tools, not eliminated by a defect positivity theorem. Their unique proofs have not become unnecessary. |
| P111--113: marked crossing plus harmonic gain makes local witness self-contained | Insufficient as stated. The mark sum still needs the deleted-tail and common-center bounds, positive denominators, `G^2<c_v N L`, `L>0`, `zU<=1` and correct variance-envelope directions at `fourier-analysis.tex:3951--4003`. Normalization, phase derivatives, cubic repair and mass lower bounds are separate at lines3545--3717. Main `05c-counts.tex:91--106,198--209` requires the strict signs before mass substitution and clamps an inverse-index term at zero. `1000/4553>5/23` is correct, but its scalar trigonometric majorant and amplitude gates remain conditions. |
| P115--117/A71--72: all confinement floors differ only by J0,Fd | Rejected. Besides the false Fd comparison, the N42 bridge checks strip23/40, initial moment coefficient30 (not24), interior mode endpoints and both deleted indices at `uniform-bridge.tex:14--93`; interval widths, signed phase resource, positive slopes and inverse numerators are at lines95--154. The old floor40 contract is only `m in {40,41,42}` (`finite-analysis.tex:3293--3423`). No all-N25 theorem follows from replacing two parameters. |
| P129: delete all analytic-input assumption items | Replace only an item whose full domain and hypotheses have been proved at its consumer. `finite-analysis.tex:29--82` includes original index restrictions, strict support/confinement, same-law signed fields, positive divisors, directed elementary enclosures and numerical conditions. A reference can document a discharge; a heading change cannot discharge it. |
| P131--147: aggressively compress finite proofs | Some shared definitions and exact majorant expectation algebra can be cited. The n=1 dual condition, n=2 tensor features and n=3 independence-null features have distinct predicates; n=4 uses a canonical three-point/Hermite measure and lens remainder; n=5 needs six acquired support radii and a complete moment-domain cover. Those proof components have not been shown redundant. The intermediate finite sources contain sign-aware and weighted-interface refinements, not just parameter repetitions. |
| P155/A80--81: lower the tail to20/25 | A research question, not an established monotonicity result. Support formulas `04-support.tex:104--122` freeze 41 and other floor42 constants. The floor25/31 contracts at `finite-analysis.tex:3265--3291` explicitly require their own support states, complete resource/local covers and counts. Zero predecessor loss does not prove those predicates or transfer favorable finite upper-endpoint terms. |
| P156/A83--85: exact binomial polynomials close4..24 | Exactness of `binom(n,k)p^kq^(n-k)` gives a valid representation, not a sign for the target difference. Actual conditional tails, count admissibility, support acquisition, joint resources, both event orientations and closed boundaries must still be covered. No claimed regional closure or removal of n4/n5 methods is justified by an executed or supplied covering proof here. |
| P14--40,163--170: exact page/line budgets and naming | Editorial targets only. Numerical block labels can be mapped to mathematical descriptions, but removing them without a coverage map would hide the index/row boundary. There is no established 60-page proof preserving all current unique analytic arguments. No reduction in certificate jobs or arithmetic output contract is claimed. |

## 6. Fresh checks and limits

Run `python3 mathematics/strategy-v4/2026-10-27/argon-audit.py` from the
repository root. It uses only the Python standard library, exact `Fraction`
arithmetic and integer square roots. `runs/argon-audit-20261027/exact01/`
contains stdout, empty stderr, versions, return code and hashes. The tests
include the scale identity at eight indices, two unsafe accepted-by-proposal
factors, independent quartic multiplication, the n4 endpoint margin,
floor40/42 bounds, and exact root enclosures at nine indices. Negative
controls reject the incorrect quartic parameter, n=1 recurrence substitution,
strictness from a `>`-only argument and zero loss without the predecessor
premise. The last two are logical countermodels, **not probability laws**.

The universal claims above are justified by the written algebra and proof;
checking finitely many indices alone would be insufficient. The script does
not verify Fourier inversion, the source's analytic reductions, certificate
semantics or domain coverage. It runs no inherited program, changes no
certificate or sourceoriginal file, and performs no numerical generation.
The edited smoothing chapter retains the atom-safe support-free recurrence;
its new conclusion does not acquire bounded support or higher moments.

The compile/visual receipt records the changed chapter check. This is a
reviewable scalar/generalization contribution and a decision audit. It is
not acceptance of the full conjecture, the finite base, or LOCAL42.
