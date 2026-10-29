# ROOT4 original-law bridge: bounded analytic closure

Date: 28 October 2026. Branch `research/v8-root4-bridge-20261028`, task base `4f5bbbfebb82b3a4749ec9fa17cbd0dd995bb270`; original reference baseline `6346fc1b4432bc5982822aa696eb566ed9e1e1ee` is untouched. Only new research/evidence files are added. No native ROOT4 job, historical self-test, imported mathematical module, network fetch, or certificate generation was run.

The deliverable is the theorem in `root4-bridge.tex`: **genuine whole-cell center/response/remainder enclosures, together with the stated closed-CDF Prawitz majorant, imply the desired bound for every original iid law and every central threshold.** The proof derives the two physical reserves, the original-law defect representation, and the closed count/reflection joins. It requires neither finite original support nor ratio/contact optimality. This closes an analytic implication, not the entire `c4.physical_bridge` obligation: that obligation also requires complete implementation-to-enclosure correspondence for every selected portfolio.

| Result | Mathematical status | Execution status here |
|---|---|---|
| Actual law to one common tagged defect measure, including zero/contact atoms and eta=0 | Locally derived exact theorem | 65 exact polynomial response identities over the positive-excess test laws passed |
| Original-law quadrature and continuous-threshold interpolation factors | Locally derived from the explicitly retained closed Prawitz input | Exact sharp quadratic factor controls and kernel-weight integrals passed |
| Valid complete nodal rows to every threshold and every law in a cell | Locally derived conditional theorem; finite bounds remain premises | No ROOT4 terminal row evaluated |
| Actual iid law to five-count conditional moments, Cantelli and reflected-law coverage | Locally derived, including zero conditional variances and closed events | 45 moment pairs and 1,105 closed conditional events passed |
| Three-point reference alone dominates every original CDF | Refuted; explicit actual-law counterexample below | Exact convolution reproduced |
| Full selected ROOT4 arithmetic/source closure, unrestricted C4, BASE41 | Not established by this task | Native run and full portfolio audit not performed |

## 1. Exact analytic contract

Let P be any standardized marginal with `|X| <= 17/4` and `rho < 46/25`; all four summands are independent copies of P. Its canonical contacts are `a=E X_-^2/u`, `b=E X_+^2/u`, where `u=E X_+=E X_->0`. The reference Q has masses `u/a, 1-u/a-u/b, u/b` at `-a,0,b`. Put `eta=rho(P)-rho(Q)`.

For each actual P in a declared geometry/excess cell, the finite input contract requires:

1. Whole-geometry, node-specific bounds `M_H >= C_H(Q)-T rho(Q)` for the **actual** reference characteristic function, with the original raw phase and factor 2.
2. A valid signed whole-domain common-measure bound `Gamma_H(eta)` for the sum of all linear frequency responses, using one fixed price tuple before the tagged supremum.
3. A complete nonnegative remainder bound `R2_H(eta)` for the weighted complex fourth-power remainder. An affine radius must be nonnegative over its entire closed excess cell. The theorem proves a basic convex-quadratic remainder; sharper disk/lens producers are separate premises unless independently proved.
4. Whole-cell actual-reference moduli and actual-law difference radii, sufficient for continuous-frequency characteristic-function bounds, not just midpoint values.
5. Both endpoints of each convex complete row `M_H+Q_H+E_H+2 Gamma_H+2 R2_H-T eta` are nonpositive at every threshold node. Complete rows may be selected independently at different nodes. No coefficientwise portfolio selection is licensed.

The raw midpoint reserve is `Q_H = min(687/(8 N^2), F2_H/(12 N^2))`, where `F2_H=42 sqrt(D2)+108 D2+24 sqrt(D2 D4)`. The threshold reserve is `E_H=h^2(B+1/4)/16`, with `B=36 sum d_j P_j^4` and `P_j=min(1,a_j+e_j+3/(2N))`. Each is used once. The first belongs to the original-law integral at the node. The second belongs to the smooth function `2(J_P(H/2)-Phi(H/2))` on the full interval between nodes. It is not a curvature claim for the CDF or for a pointwise minimum of candidate numerical envelopes.

For N=256 and h=1/8 this is precisely the normalization in the retained source. The analytic statement is more general in N and h. The all-threshold conclusion additionally uses the independently proved actual-law tails at H<=-4 and H>=25/8. The note proves the elementary normal-tail comparison with a rational lower bound using pi<22/7, rather than accepting a recorded floating-point value.

## 2. Why the bridge contains every original iid law

For eta>0, the same probability `nu=W dP/eta`, `W=|X|(|X|-c)^2`, supplies every frequency. The exact mass budget is `eta integral k0 = 1-w-P{0}`, and the signwise inverse-square budget is `eta integral_sigma k2 = u-c_sigma P{sigma c_sigma}`. Contact masses cannot be omitted from these identities. The signed inverse-distance integral is zero. All singular integrals are justified by cancellation and Cauchy; no integral is defined at a zero-denominator atom. When eta=0, P=Q directly and nu is unnecessary.

Hermite interpolation matches the first two tagged moments. Its constant terms match only after both tags and the zero atoms are added. This supplies an exact characteristic-function difference for P itself. Maximizing a priced response over a relaxation of nu is safe because every actual nu is in that relaxation; the proof does not infer a law or an iid convolution from a relaxation optimizer.

The characteristic-function fourth power and the conditional binomial probabilities both require iid copies. In the count route, zero is in the nonnegative group. Under reflection the new probability is `P(X<=0)=1-p+P{0}`, not `1-p`. Conditional means and variances are computed from the same tagged moments. Cantelli is applied to the closed event, using value 1 at its mean, even when the conditional variance is zero. A complete upper bound for the binomial mixture may relax the means/variances further; it must still cover every feasible p and retain the same mixture probabilities.

The reflected characteristic function is conjugated while the phase at its own raw H remains `exp(-i q H)`. Positive closed bounds for P and -P cover negative CDF errors by `Phi(x)-F_Z(x) <= Phi(x)-F_Z(x-) = F_{-Z}(-x)-Phi(-x)`. Equality at an atom is not required.

## 3. Source edges and scoped implementation correspondence

The immutable source text used here is `paper/analytic-supplement.txt` at the task base. These are inspected source arguments, not theorem labels accepted on authority.

| Edge | Source location | Result of independent derivation |
|---|---|---|
| Canonical reference, cubic/fourth moment defect identities | 5350–5406 | Verified by the two pointwise polynomial identities in the note; no three-point restriction on P |
| Common measure, mass/contact budgets, signed prices | 5515–5577 | Verified including contact subtraction, common-frequency dependence and eta=0 |
| Fourth-power linear/remainder separation | 5580–5592 | Exact algebra and the primary convex quadratic proved; all selected sharper lens implementations not audited here |
| Prawitz normalization and original-law integrand | 5645–5693 | Closed Prawitz remains an explicit smoothing input; regularized derivative factors42/108/24 derived |
| Same-law moment bound and midpoint normalization | 5694–5727 | Verified from support and moments before quadrature; raw factor1/(12N^2) retained |
| Continuous-frequency fill and H interpolation | 5729–5765 | Verified on all frequency cells and the smooth majorant; single factor h^2(B+1/4)/16 |
| Low-excess complete row and eta endpoints | 5774–5813 | Conditional original-law implication proved; no acceptance inferred from symbolic form |
| Count/Cantelli and high/low cutoff joins | 5880–5930 | Actual iid conditional moment formulas and reflection proved; numerical high-cell envelopes and external large-rho bound remain inputs |
| Parent/child/all-threshold cover | 5932–6019 | Set-theoretic implication sound with all closed cells, complete selected child covers, both actual orientations and both tails; counts are not acceptance evidence |
| Global owner localization before this bounded class | 5408–5511 | Separate dependency; not re-proved here. The earlier v7 localization proof remains separately scoped |

The local files were available in `work/end2end25_audit_20261024/remote/vendor/root4_75a9470`; no Git object was fetched. Availability here does not assert complete repository or archive availability. Exact file SHA256 values are saved in the run receipts. These sources were read, never imported or executed:

- `n4_local_physical_moment_quadrature_2026_10_09.py:83–134`: same-law rho/kappa/M4 bounds, physical contact min with R, outward square root and one scalar minimum of the two complete midpoint reserves. All match the derived formulas.
- `n4_frequency_local_physical_H_curvature_2026_10_09.py:129–277`: the selected radius is a whole-cell nonnegative affine model, frozen by its endpoint maximum; all N frequency cells get the `3/(2N)` fill; two complete positive integral weights are intersected cellwise; curvature and raw-H reserve use the factors in the proof.
- `n4_Q3_H_curvature_low_eta_box_leaf_2026_10_09.py:54–76`: actual-reference moduli enter the curvature helper; its two outward ceilings enlarge the analytic reserve.
- `n4_fresh_signed_common_nu_quartic_ledger_2026_10_09.py:139–229`: inequality prices have the proper sign; one complete primary quadratic/disk constant is used; the raw row has exactly `2 Gamma+2 R2` and one copy of each reserve. The sign-safe normalized score retains both denominator faces. Its disk formula and broader producer graph are not fully audited here.
- `n4_cpu_time_signed_CDF_consumer_2026_10_09.py:87–221`: same-H assembly of all three complete routes, all16 excess cells and both orientations, original baseline radii for H curvature, and per-H physical midpoint reserve are visible in the call path. The helper inputs still need their complete mathematical provenance. No whole producer graph is claimed checked by these five reads.

The active implementation therefore agrees with the focused analytic bridge at these calls. The remaining implementation requirement in `source/original/proof/obligations.json:271–287` is broader: every selected CF/reference/radius/price/lens producer and whole-domain enclosure must be justified and bound to the actual completed arithmetic. Earlier review reports may help locate them; this task does not use their PASS wording as proof.

The dependency graph has no C4-to-C4 edge in the reviewed mathematics:

```text
actual standardized bounded iid P -> canonical Q / common nu / actual moments
closed Prawitz + those moments -> original-law nodal midpoint bound
genuine finite center/price/remainder inputs -> complete nodal row bound
actual CF cell bounds -> smooth-majorant curvature -> every central H
actual iid count bound OR independent all-law large-rho theorem -> high eta
closed geometry/eta joins + both tails + actual reflection -> bounded-law C4 bound
G3 + all-law rho envelope + attainment/contact -> unrestricted owner in bounded class
bounded-law bound + owner localization -> unrestricted C4 conclusion
```

The first six edges never require C4, C5, or a later tail theorem. The last two remain separately scoped here. A native Boolean is not a replacement for the genuine finite-input node.

## 4. Exact controls and concrete false shortcuts

`root4-check.py` is independent standard-library rational code. It executes no original kernel. It covers nine standardized finite laws, including both skew orientations, an atom at zero, exact reference contacts, and a four-point law. It verifies 65 polynomial Hermite-response identities,45 conditional moment pairs,1,105 conditional closed-event Cantelli inequalities, and103 actual sum-atom thresholds. Four laws have zero excess and use the direct P=Q case.

For the actual four-point law

`P(±1/2)=5/16, P(±3/2)=3/16`,

one has `rho=43/32`, contacts `a=b=8/7`, and `eta=45/224`. At raw H=-4,

`P(S4<=-4)=2511/65536 > 5764801/268435456=Q^4((−infinity,−4])`.

This is inside the bounded-law class and at a central threshold endpoint. It refutes Q-only CDF domination, not the active physical bridge and not the Berry–Esseen conjecture. The active bridge retains the linear response, nonlinear remainder and original normalization that the shortcut discards.

Other rejecting controls are the false complementary reflected sign mass (seven laws have zero atoms), substituting iid weights for four perfectly correlated symmetric signs (CDF1/2 versus5/16 at H=-2), half-sized raw midpoint/threshold reserves (sharp quadratic controls), and a lower-only denominator for a negative numerator. Exact cell-integral weight totals and the rational Gaussian tail lower bound also pass.

Runs `root4-bridge01` and `root4-bridge02` contain actual stdout, stderr, command, interpreter, return code, timing and input hashes. Run02 strengthens the Q-only control by requiring its witness threshold to lie in the central range. These tests check algebra, scales and endpoints; they do not turn finite laws or sampled parameters into the all-law theorem. The continuous arguments are in the TeX note.

## 5. Consequence and remaining boundary

No new analytic defect or circularity was found in this physical bridge. The new proof can discharge the original-law-to-enclosed-row implication under its explicit closed Prawitz and whole-cell input contract. It also explains exactly why the apparent three-point reduction is not such a reduction.

It does **not** discharge the complete `c4.physical_bridge` flag, `c4.native_root4`, or `c4.complete_root`: complete selected input-producer validity and the actual qualified finite arithmetic still need binding/review. The old status fields do not prove no later run exists, and this task neither denies nor reissues a historical native acceptance. No certificate or producer can be deleted on this result alone; the numerical cells are still the hypotheses of the theorem. The finite-base obstruction is narrower analytically, but BASE41 and the global theorem remain unproved here.

The final five-page note in `root4-build02/root4-main.pdf` compiled without warnings or overfull/underfull boxes. All five rendered pages were visually inspected at full page size; no clipping or overlapping equations was found. This checks presentation only.
