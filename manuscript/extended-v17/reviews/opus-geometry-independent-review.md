# Independent review of geometry, conservation and acquisition edits

Date: 2026-10-30. Compared the working versions of `sections/03-conservation.tex`, `sections/05-geometry-counts.tex`, and `sections/07-direct-acquisition.tex` against `HEAD` (`6339dda253238048aa75dcf1f2e8c4b73b7b6522`). This review derives the new mathematical claims from their definitions; it does not rely on the constructor's report. No TeX was edited by this reviewer.

**Conclusion:** the new lattice consequence, moved normalization, solved excess identity, quantitative `1/n` explanation, and budget explanations are mathematically sound at their stated scope. No new substantive defect was found. Two small integration/editorial findings are listed below. This is a bounded review of the changes, not a new validation of every inherited localization estimate or external input.

| Result | Mathematical status | Execution status |
|---|---|---|
| Lattice `J>=h`, including unbounded support | Independently derived below | Finite lattice diagnostics freshly passed; diagnostics are not the proof |
| Reflection and lattice equality case | Independently derived from the existing equality lemma | Finite reflection diagnostics freshly passed |
| Canonical normalization and unchanged raw threshold | Independently derived algebraically | Source/cross-reference review; duplicate reported and removed by parent |
| Solved excess and uniform defect estimate | Independently derived from the retained conservation identity; assembly also checked | No numerical acceptance required |
| Joint budget and displacement/noise coupling | Independently expanded; exact polynomial identity checked | 81 rational interpolation-grid evaluations passed |
| Inherited numerical acquisition/ray estimates | Unchanged mathematics except explanatory additions | No fresh reproduction of every inherited constant claimed by this review |

## 1. Lattice gap functional, including unbounded support

Let the support `K` lie in `a+h Z`, with `h>0` its maximal span. This set is discrete and closed, so `K` has Lebesgue measure zero. Every bounded complementary component has endpoints in `K` and length `k_g h`, with integer `k_g>=1`.

The zero-bias density is nonnegative. Below the support it equals `E X=0`; above the support it is zero, apart from irrelevant endpoint values. Inside the convex hull, every point outside `K` belongs to a bounded gap. This remains true for support unbounded on one or both sides. Consequently the nonnegative gap integrals exhaust the whole integral:

`sum_g tau_g |g| = integral tau = E X^2 = 1`.

There is no exchange of signed or conditionally convergent sums: enumeration of the countable gaps and monotone convergence suffice. Define `omega_g=tau_g|g|`. Then

`J=sum_g omega_g |g| >= h sum_g omega_g = h`.

Finiteness follows independently from the existing general bound `J<=rho+2m`. If every successive gap has length `h`, equality follows. Missing lattice sites can make `J>h`; the proof does not assume full lattice occupancy.

For reflection, the new density at `t` is

`E[-X 1{-X>=t}] = E[X 1{X>-t}]`.

It equals `tau(-t)` except at the countable set of atom locations. Reflection therefore preserves gap weights, `J`, `rho`, and maximal span, and reverses `gamma`. Choose the orientation with third moment `|gamma|`. In that orientation,

`(3+sqrt(10))rho-|gamma|-3h = D_oriented+3(J-h)`.

Both terms are nonnegative. Equality forces `D_oriented=0`, whose existing equality characterization is the extremal Bernoulli law. Conversely, for that two-point law its maximal span is the distance between its two support points, and `J=h`; reflection gives the other equality law. The new corollary's exact equality statement is therefore justified.

An explicit unbounded check illustrates the missing-site issue. Take `P(Z=k)=P(Z=-k)=2^(-k-1)` for integers `k>=1`; then `E Z^2=6`. For `X=Z/sqrt(6)`, the maximal span is `h=1/sqrt(6)`, all outer gaps have length `h`, and the central gap has length `2h`. Its zero-bias mass is `1/3`, giving `J=(4/3)h`. No bounded-support hypothesis has slipped into the argument.

## 2. Normalization, units and orientation

With `B_0=1{X>0}`, `p=P(B_0=1)`, `q=1-p`, and `m=E X_+=E X_-`, the conditional means are `-m/q` and `m/p`. Setting `ell=m/(pq)` gives

`E[X|B_0]=ell(B_0-p)`, `W=X-E[X|B_0]`, `E[W|B_0]=0`.

Conditional orthogonality yields `1=pq ell^2+theta`, where `theta=E W^2`. With `U=W/ell`, `s=theta/ell^2`, one has `pq+s=ell^(-2)`. Thus

`X=ell(B_0+U-p)=(B_0+U-p)/sqrt(pq+s)`.

This is a pointwise identity for the original random variable, including a possible atom at zero assigned to the nonpositive class. It does not construct a new marginal or change the raw sum threshold `H`.

After acquisition there is a central gap, so zero is no longer in the support and the variance measures on `X>0` and `X<0` have total mass `theta`. The revised ending correctly refers to the same chosen law. The reflection step remains earlier in the fixed-target argument and composition: a signed defect or probability interval is not transferred from the opposite orientation. The lattice corollary's separate reflected inequality does not authorize such a transfer.

## 3. Conservation and the solved excess

The gap integration uses `h(t)=nu([t,infinity))`, hence `h(t)=h(v)+nu([t,v))` in a gap `(u,v)`. Contact kills the endpoint term. The resulting leakage has nonnegative measure and integrand; it enters the gapwise expression with a minus sign and, after rearrangement, the conservation identity with a plus sign. Its sign requires no predecessor theorem.

I checked the assembly: integration of `Q` against `tau` uses `integral t tau=gamma/2`, `integral t^2 tau=M_4/3`, and `integral |t|^3 tau=M_5/4`. Integration of `XQ` gives the stated first-moment formula. The identity for `q_z` then gives the displayed relation for `T-Phi(z)`. Collecting these expressions yields the retained general conservation identity with coefficient `n+H^2` on `a`.

At `c=CE`, substitute `phi_z=phi(0)e` and `gamma+3J=(3+sqrt(10))rho-D`. Rearranging gives exactly the new solved-excess formula. The specialization to `c=CE` is essential and is supplied by its surrounding text and reference to the positive conservation identity.

For `a>=0`, all four terms on the right of that identity are nonnegative. If `R_c<=T`, then `n phi(0)e D/6<=T`. The independent bounds `n>=N` and `|H|<=H_0` give `e>=exp(-H_0^2/(2N))`, proving

`D<=6T exp(H_0^2/(2N))/(n phi(0))`.

This is a uniform quantitative implication for every qualifying pair, so varying laws cause no fixed-law-limit issue. The later licensed improvement still starts with a bound on `R_c`, proves `M_c>0` and a density floor, and only then improves `mathcal U`. Its upper bound is not substituted back as a raw remainder bound.

## 4. Joint budget and acquisition

Independently expanding the outer-gap estimate gives

`D >= (sigma-1)M3,+ +(sigma+1)M3,- +6A_+ M2,+ +6A_- M2,- -6m(A_-^2+A_-A_++A_+^2)`.

On the positive class,

`M2,+=m barA_+ +E[W^2;X>0]`,

`M3,+=m barA_+^2 +E[(X+2barA_+)W^2;X>0]`.

The analogous negative identities use `-X` and `barA_-`. Substituting `A_-=ell(p-a0)`, `A_+=ell(q-a1)`, `m=pq ell`, and `w=pq ell^2` leaves deterministic part

`ell w [Q(p)+6{d(1-d)+a0 a1}]`.

The two residual expectations are exactly the two nonnegative noise kernels in the manuscript. Every expectation is integrable with a finite third moment; no new fourth-moment assumption is needed. The simultaneous-gap coefficients follow by evaluating these increasing kernels at the inner support endpoints.

The new explanation of dropping displacement terms is valid: for either branch, the combined change from `d=0` is

`d[6w(1-d)-theta b_pm]`.

The available bounds `w>.994`, `d<.004`, `theta<.006`, and `b_pm<=sqrt(10)+7` make the bracket positive. It would be wrong to drop the positive displacement term while retaining its negative noise correction separately; the revision explicitly keeps them together.

For the count variance, the one-sided cubic inequality follows from the nonnegative polynomial `(a-Z)(Z+t/a)^2` for centered `Z<=a`. Its variance-squared term paired with `6n v(1-dbar)a_j` gives the displayed AM–GM term. If `a_j=0`, centered one-sided noise vanishes and that term is absent, so the argument makes no illicit division by zero. The refined bound controls `n theta/ell^2` and not merely `theta`, exactly as the new explanation claims.

## 5. Findings and evidence

1. **Resolved integration finding:** `revision:canonical-decomposition` was briefly duplicated in the guide and geometry. Parent removed the guide equation and replaced it with a reference; the intended normalization labels now belong to geometry.
2. **Resolved minor wording finding:** acquisition step 5 said “before bounding these two cubics” immediately before a display already containing the reciprocal terms obtained from those cubic bounds. The constructor changed this to “with these two cubic bounds inserted, gives”, and I verified the correction in the source. This is an explanatory correction, not a defect in the displayed inequality.

Fresh independent evidence is in `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_opus_20261030/geometry-independent/`: `check.py`, `check.stdout.json`, `check.stderr.txt`, and `receipt.json`.

The check uses exact `Fraction` arithmetic. It verifies the budget polynomial on a tensor interpolation grid with enough distinct values for every variable degree, which proves that polynomial identity. Finite lattice examples with two atoms, an atom at zero, and a missing lattice site verify the stated gap-weight calculations and reflection invariance as diagnostics. The general unbounded-support proof is the argument above, not those examples. Source hashes at the time of the exact check are recorded in the output; the later cubic-wording correction does not alter its mathematics. No TeX compilation is claimed by this independent review; the constructor and parent own rendering/integration.
