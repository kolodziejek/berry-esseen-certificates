# Independent audit of the complete conditional confinement panel

28 October 2026. Review on `research/v8-small-noise-20261028`, following the independent low-noise proof commit `1172d87ad3a662a179035a2fc84074929dd87fc6`. Only new research/review evidence and the explicit inward-endpoint clarification described below are changed. No inherited numerical program was executed by this review.

**Verdict:** the high-noise implication is valid under the named contact, acquired-entry, and same-cell resource premises. Together with the separately proved all-threshold low-noise lemma it yields `|U|<1/2`, `d<.069` on the single oriented probability panel `p∈[.41,.42]`, uniformly for actual integers `n≥42`. I found no additional analytic obstruction in the signed-deletion, concentration, slope, or common-resource step. This is a conditional panel theorem, not proof of the accepted entry ancestors, all probability panels, the eventual count comparison, a finite base, or the global conjecture.

| Component | Mathematical status | Execution status in this review |
|---|---|---|
| Same-law endpoint moment cost, interval deletion, strict-gap concentration, slope bounds and common-resource implication | Independently derived below, conditional on contact/entry/resource | Algebra and domains checked; no inherited execution |
| Exact 128 closed rectangles and incident-cell resource maxima | Correct finite cover of the acquired phase/noise rectangle | Fresh independent rational reconstruction from the frozen export |
| High-noise complement | Conditional confinement implication established | All 56 required strict ray margins freshly reconstructed; 84 other boxes excluded by necessary conditions |
| Low-noise band | Independently proved in `small-noise.tex` | Earlier independent two-boundary/twelve-ray PASS; no rerun needed for the arithmetic |
| Complete four-pass entry, Fourier acquisition, original producer semantics | Ancestor premises, outside this final review's reproof scope | Not rerun here; B's separate producer evidence is not relabelled as my execution |
| Global sharp Berry–Esseen statement | Not established by this component | Not run |

## Exact reviewed sources

Paths in this paragraph are relative to sibling worktree `phase-confinement-v8`. The source hashes distinguish the inspected snapshot from subsequent edits.

- `mathematics/fixed-target-v8/2026-10-28/confinement-proof/confinement.tex`: SHA256 `080fe7915bd5cfd569c208ce057a7078f6aae7a787ceca1cde14cb45acf25ee2`. Its first three sections establish the preceding `.6` strip; its failed subsequent diagnostic remains correctly labelled historical research in that note.
- `mathematics/fixed-target-v8/2026-10-28/phase-confinement-proof/main.tex`: SHA256 `6bff5f927dd53da6574c8c9ecd9d096f298806c26987d26c7906e4365aef11c9`. The retained-confinement section and complete conditional panel proposition are the new composition under review.
- `mathematics/fixed-target-v8/2026-10-28/phase-confinement.py`: SHA256 `8f5260920d73d1ef8bf63f192a2adcbc0cfc67ab1fc87368c8764dee3689186d`; relevant functions `rectangle_resource`, `diagnostic`, and `compose_heat`.
- `mathematics/fixed-target-v8/2026-10-28/confinement_check.py`: SHA256 `2ef7e9c9eb28482af904ad502ebd5044e612d364a449e42f89a44a7586ff4bce`; literal panel constants and `moment_chain`.
- `manuscript/arxiv-v1/appendices/fourier-analysis.tex`: SHA256 `0274a491a12fec13d87a391ce88184cc7229210168fc72bc88974e5382670a1f`; lines 3058–3468 contain the full retained confinement derivation. The original displayed floor 47 and strip .55 are not automatically reused: the changes to 42 and .6 are checked explicitly here.

The exported phase coefficients have SHA256 `b18599468c975032f4078e7a5f734fd6430b2b7da583789de58d9537d323f690`, the same bytes independently reconstructed in the earlier `phase-review.md` (commit `261776a9dc570f41ac16348ecc3b61009779ba11`). The final recorded calculation `runs/fixed-target-v8-20261028/phase-confinement05/stdout.json` has SHA256 `e5dd725d31b2e67a634a8ae7b6cd630e899457a96280a2f2ee3b3612eed9ba90`.

## Premises and one-law normalization

Fix an actual standardized fixed-target maximizing law at an actual integer `n≥42`, nonnegative excess over `c=CE`, and a raw threshold H. The true predecessor bound `C_(n−1)≤c` supplies the retained closed-support contact majorant. Assume the accepted four-pass acquisition and its all-law cell cover supply the named same-law raw/resource bounds and the preceding panel theorem. In particular,

`p∈[l,h]=[.41,.42]`, `X=ell(Y−p)`, `Y=B+U`, `E(U|B)=0`,

`theta<.054`, `d<.069`, `rho<1.22`, `.09736≤beta≤.234`, `1.9706<ell<2.034`, `lambda=n E U²<.6`, `|H|<1.814`,

and the acquired closed support lies strictly inside `Y∈(−.6,1.6)`, with `|U|<.6`. Here `B=1_(X>0)`. Write the inner Y-endpoints as `a,b`, so `0≤a≤d`, `1−d≤b≤1`, `b−a=1−d`. The actual inward statements are **weak**, `U_0≤d`, `U_1≥−d`; strictness comes from `d<.069`. The earlier independent low-noise note unnecessarily stated strict inner inequalities. Its proof only uses the weak version, which is corrected in this review commit; no boundary arithmetic changes.

The probability panel belongs to the oriented law on which contact is applied. Both signs of raw H are covered. This is not an assertion that reflection preserves that same p-panel, nor a statement for arbitrary laws satisfying only a moment box.

## 1. One physical resource really controls all three costs

Let the physical central gap be `(−A,B)` and use distinct notation `J_leak=∫_[a,b)(y−a) nu(dy)` for the confinement leakage. Put

`M_+=E[X−B;X>0]=m−pB`, `M_−=E[−X−A;X<0]=m−qA`.

These quantities are nonnegative and concern the same marginal. The endpoint expansion of the physical defect gives

`D≥m(√(sigma+1)A−√(sigma−1)B)² + 2(sigma+2)B² M_+ + 2(sigma+4)A² M_− + 3(sigma+1)B theta_+ + 3(sigma+3)A theta_−`,

where `sigma=√10`. This follows directly by setting `Z=X−B≥0` on the positive class: `T_+=2B²M_++3B E[Z²;X>0]+E[Z³;X>0]` and `R_+=BM_++E[Z²;X>0]`. Thus `(sigma−1)T_++6BR_+` has the stated M and variance coefficients. The negative class has the corresponding `sigma+1` expansion. The squared term is valid since `2√((sigma+1)(sigma−1))=6`. Discarding that nonnegative square is legitimate here.

Using `A≥E(l−d0)`, `B≥E(1−h−d0)`, with `E=1.9706,d0=.069`, proves exactly

`D≥c_+M_++c_−M_−+b_*theta`,

where the code's `c_+=2(5.16)E²(1−h−d0)²`, `c_−=2(7.16)E²(l−d0)²`, and `b_*=min(3(4.16)E(1−h−d0),3(6.16)E(l−d0))`. Also

`d=(M_+/p+M_−/q)/ell`, `epsilon=E|U|≤2(M_++M_−)/ell`.

The last inequality uses the elementary bound that mean absolute deviation about a conditional mean is at most twice mean distance from its inner support endpoint. It does not introduce an independent marginal or a relaxation optimizer.

The fixed-target resource is

`Ucal=(n+H²)a_excess+n phi(0)D/6+n^(3/2)L_leak≤S`,

and `L_leak≥(1−theta)J_leak`. All terms are nonnegative. With `kappa=997/15000<phi(0)/6`, a closed noise band `[lambda_0,lambda_1]` therefore gives the **single** simplex

`n c_+M_+ + n c_−M_− + n^(3/2)L_leak/kappa ≤ R`,

`R=S/kappa−b_*E²lambda_0`.

Here `n theta=ell²lambda≥E²lambda_0`; the lower noise endpoint is used in the correct direction. `R<0` excludes a law, whereas `R=0` is retained. This also proves `nd≤G=R/alpha`, `alpha=min(c_+lE,c_−(1−h)E)`. There is no separate expenditure of the same defect resource in these steps.

## 2. Both deleted indices, strict widths and atoms

Conditional noises can be coupled independently and sampled with an independent Bernoulli label without changing the actual one-coordinate law. Each conditioned Bernoulli increment is at least `b−a=1−d`. A sum falling in an interval of diameter **strictly less** than that increment selects an antichain. The random-chain/LYM argument bounds its Bernoulli mass by the largest binomial atom; conditioning on an additional independent noise preserves the bound. This is a proof about the actual iid convolution, not a claim that every feasible conditional-moment relaxation is iid realizable.

For every deleted index `j≥n−2≥40`, a binomial mode satisfies `(j+1)p−1≤k≤(j+1)p`. Thus `r=k/j` lies in `[rL,rR]`, where `rL=l−(1−l)/40` and `rR=h+h/40`. Both endpoints lie strictly inside `(0,1)`. The usual finite Stirling inequalities yield

`√j max_k P(Bin(j,p)=k) < .4/[√v_* (1−1/480)] < M`,

`v_*=min(rL(1−rL),rR(1−rR))`.

The relative-entropy term is nonpositive in the exponent and may be discarded. This standard finite Stirling theorem is an explicit external analytic input, not a numerical observation. The exact outward square root M and `Fd=1.037` satisfy `Fd²>max((42/41)³,42/40)`. The first factor bounds the directed-distance term from `n−1` summands; the second bounds both the signed-noise and pair-event terms from `n−2` summands. No `C_(n−2)` hypothesis is used.

For the lower ray take `I=[a−r,a−d−tau−eta]`, `tau=.2`, `eta=10^−5`, with `.5≤r≤.6+d0`. Then `I^+=[a−r+1−d,b−eta]`. Its width is `r−eta≤.669−eta<.931≤1−d`, and the width of I is smaller still. Moreover `I^+⊂[a+g,b)`, `g=1−.6−2d0=.262>0`. The intervals are disjoint. For the upper ray take `I=[a,a+tau]`, `I^+=[b,a+1+2tau]`. Their widths are at most `.2` and `.469`, both strictly below `.931`. The strict gate `d0+2tau=.469<.5` places `I^+⊂[b,y)` for every putative support point `y≥1.5`. All comparisons remain strict at every cell seam.

Contact and the central leakage give the needed lower/upper interval inequalities without dropping atoms: `g(y)=nu([y,infinity))`, so differences at contacting endpoints equal `nu([u,v))`. Closed intervals used for upper concentration contain these half-open intervals. In particular the upper estimate includes the atom at b, while its outer comparison interval excludes the contacting y. The lower interval may be enlarged to a closed interval for concentration. No CDF continuity is assumed.

## 3. Signed deletion and contact slopes

Let `m=n−1`, `Z=x−sum_(i≤m)Y_i`, `mu=p+H/ell`, and K be the count of labels. Exchangeability and `mp−K=Z−mu+sum U_i` give exactly

`nu(I)−T_1(I)=E[(Z−mu+sum U_i)1_I(Z)]/(mp)`,

`T_0(I)−nu(I)=E[(Z−mu+sum U_i)1_I(Z)]/(mq)`.

For each removed full pair, the remaining conditional interval probability f lies in `[0,M/√(n−2)]`; since `E U=0`, `E[Uf]≤(epsilon/2)M/√(n−2)`. This is why the error coefficient is `a_e=Fd M(1/l+1/(1−h))/2`, not an unsigned bound for the sum of noises.

For independently coupled conditional noises `Delta=U_1−U_0`, the actual gap gives `Delta≥−d`, while `E Delta=0` and `Var Delta≤s/p` since `p<q`. Mapping the label-one point by `1+Delta` yields

`T_1(I)≤T_0(I^+)+M/√(n−2) P(Delta>tau)`,

`P(Delta>tau)≤min(lambda_1/(lambda_1+N l tau²),G/(N tau+G))`.

The exceptional inequality is strict, so collisions at `Delta=tau` are in the good event. This accounts for the actual atom convention.

The contact derivative is unchanged by the additive fixed-target excess:

`√n(−Q_c'(y))=ell phi(H/√n)+(ell/n)[3c beta+(H phi(H/√n)+3c rho)t−3ct|t|]`, `t=ell(y−p)`.

For a phase band `[h0,h1]`, `phi_- = .39886(1−h1²/(2N))>0` is valid uniformly in `n≥N`. The signed upper bound on `H phi` is `.4h1` for positive H and `−phi_-h0` for negative H. On `t≤0`, completing the upward quadratic gives the negative-side cost in B's code; its linear coefficient is checked positive before squaring the upper bound. On the central positive half-line, `t≤B_*=1.2`, and `rho≥1`, `B_*²>(1−l)/l` make the lower bound valid. On the whole positive half-line, completing the downward quadratic gives the upper slope `Uplus`. All uses of `ell/n≤FL/N` multiply a nonpositive correction in a lower bound, or a nonnegative correction in an upper bound.

For the sharper lower ray, `t≤t_*=-E(l+tau+eta)<0`. Write `B(t)=beta_-+rho_*t+t²`. The code first bounds its possible negative part by its clipped minimum, then varies `c∈[cl,cu]`:

`3c(beta+rho t+t²)+H phi t ≥3cl B(t)+v_+t+3(cu−cl)min(0,min_(t≤t_*)B(t))`.

Both clipped minima used in the code are the actual minima of upward quadratics. This verifies the sign-sensitive term, including negative H. The frozen cap `rho_*=min(1.22,rho_B(l)+24lambda_1/N)` follows from the already acquired `.6` strip, as independently proved in `small-noise.tex`. It does not use the desired `.5` conclusion. The resulting slopes L,Lg,Uplus are all strictly positive.

## 4. The two error bounds and full rays

The preceding inequalities reduce either putative ray to an error bounded by

`a_d d+a_e epsilon+a_J√n J_leak+A/n+B P(Delta>tau)`.

The lower side uses `a_d=L`, `a_J=1/g`, contact side `L(.5−tau−eta)`; the upper side uses `a_d=Lg+Uplus`, `a_J=1/tau`, contact side `Lg−.6Uplus`. Directed distances A in the code are the respective upper interval endpoints minus `mu`, with positive parts and outward probability denominators. On the lower side they are independent of r; strict-gap concentration is also independent of r. Thus L>0 extends the lower contradiction from r=.5 to every r in the acquired strip. The upper inequality already applies to every putative y≥1.5 in that strip. No extrapolation outside the proved strip is needed.

For the common simplex of Section 1, the three per-unit linear costs are

`z_+=(a_d/l+2a_e)/(E c_+)`, `z_−=(a_d/(1−h)+2a_e)/(E c_−)`, `z_J=kappa a_J/(1−Theta)`.

Hence `E0=(max(z_i)R+A)/N+B min(lambda_1/(lambda_1+N l tau²),G/(N tau+G))` is valid. The positive inverse-index coefficient is explicitly checked, including nonexcluded `R=0` cases.

At each simplex vertex, `(v_i,w_i)` is the linear cost and upper displacement `nd`: namely `v_i=z_i R/N`, `w_+=R/(E c_+ l)`, `w_−=R/(E c_−(1−h))`, `w_J=0`. The nonnegative origin is harmless. Concavity gives, for every `t≥0,x≥0`,

`x/(N tau+x) ≤ [N tau/(N tau+t)²]x+t²/(N tau+t)²`.

Subtracting the left side gives the explicit nonnegative rational `N tau (x−t)²/[(N tau+x)(N tau+t)²]`. Therefore the eleven tangent-vertex error bounds in the code are individually valid on the same simplex. Their minimum with E0 is valid; it does not assume that individually optimized resource allocations coexist. This is the essential common-resource issue, and the implemented signs and scalings match it.

## 5. Fresh bounded exact check and closed composition

The independent `high-noise-review.py` imports no B module and executes no source producer. It reads only the two pinned JSON artifacts above, reconstructs all incident-cell filters and whole-phase concave maxima using a clipped vertex, and independently recomputes all slope/simplex-error formulas in all nonexcluded boxes. It checks exact equality to every stored resource, left side, error and margin. Thus its evidence is stronger than counting stored PASS flags, while still not being a fresh Fourier/producer replay.

The exact Cartesian order is both signs, eight closed phase bands of width `907/4000`, and eight closed noise bands of width `3/40`. Missing, duplicate and reversed box arrays are rejected. Both original unassisted diagnostics remain failures where reported; the independent check recovers eight failed gates, all in the first noise band.

On the 112 boxes complementary to that band the exact results are:

| Outcome | Boxes |
|---|---:|
| No incident acquired moment cell | 14 |
| Negative whole-rectangle joint resource | 5 |
| Noise lower endpoint costs more than the resource | 65 |
| Both strict contact-ray gates pass | 28 |

All 56 retained strict margins exceed `0.00892011917`. The 16 first-band boxes are supplied by the independent low-noise theorem on the entire closed `[0,3/40]` band, for all H. The seven complementary closed noise bands cover `[3/40,3/5]`. Their common endpoint is covered twice, and the acquired `lambda<3/5`, `|H|<1.814` fit inside the closed cover. At H=0 both signed phase branches are included. No cell is added, no failed gate is relabelled, and no assertion for an omitted endpoint is needed.

The full retained conclusion follows: no support point lies below `a−1/2` or above `1+1/2`; since `a≥0`, `b≥1−d` and `d<.069<1/2`, both conditional noises satisfy `|U|<1/2`. Support atoms are included in the contradiction, so this is strict confinement.

The run receipt and exact stdout/stderr are in `runs/fixed-target-v8-20261028/high-noise-review01`. This review adds no native or dense campaign. Earlier entry/conservation/Fourier proofs, their actual complete-domain acceptance, and the true sharp predecessor remain the specified ancestors. The resulting theorem can replace this panel's old failed confinement invocation in a new composition, but does not authorize deleting any certificate or claiming full INITIAL42/LOCAL42 acceptance.

The inward-endpoint clarification was compiled separately in `small-noise-build03`, with return code 0, no warnings, and all three rendered pages visually inspected. No clipping or equation-layout issue was found. The exact low-noise arithmetic is unchanged.
