# Fixed-target excess: independent derivation and dependency transport

Reference state: fork main `ca4943aae7a85ffa85d5d4d7166987dc055cb3e6`.
Immutable original baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
Work branch: `research/v4-fixed-excess-20261027`. The Astra attachment is
a proposal, not mathematical authority; its SHA-256 is
`88c4839385319086af01bee2e34d4fd80b5482b157f254c77328f1d3a9391cd1`.

## Verdict

The proposed fixed-target excess is mathematically sound at the core,
and permits a proved **conditional transport of zero-barrier acquisition
and local-comparison schedules**. It can remove the scalar recurrence
from the entry of a newly stated conditional tail theorem. This is more
than a change of notation, but less than acceptance of a complete LOCAL42
argument. No certificate or production file is changed here.

For `c>0`, define

\[
A_n(c)=\sup_{P,H}\{\sqrt n(F_{n,P}(H)-\Phi(H/\sqrt n))-c\rho(P)\}.
\]

`excess.tex` gives the full proofs as an inputtable section fragment;
`excess-main.tex` is its standalone wrapper. Its macros are `\E`, `\Pp`,
`\R`, `\CE`, `\ind`, `\supp` and standard AMS math, plus theorem/lemma/
corollary environments. Labels use the namespace `v4excess:*` to support combined input. The unchanged
compensated-inversion proof is referenced precisely rather than repeated.

| Result | Mathematical status | Execution status |
|---|---|---|
| Attainment for every fixed `n>=1,c>0`; closed-support contact and compact support for `n>=2` | Independently derived in the proof note; no UI3 assumption | Exact finite-law and atom-endpoint controls pass |
| Support inequality with `-n a` | Independently derived, conditional on the actual predecessor bound | Algebraic derivation; no support certificate rerun |
| Conserved coefficient `(n+H²)a` and fixed-c remainder | Independently derived from contact, zero-bias integration and the hinge identity | Independent Laurent-polynomial check passes; missing-`H²a` mutation rejected |
| Gaussian-weight removal and phase price | Derived given a valid first raw ceiling, defect positivity and listed sign gates | Exact coefficient checks, not acceptance of a raw ceiling |
| Scalar-schedule transport and new conditional global implication | Proved under explicit universal scalar, coverage, strictness and index hypotheses | No native acquisition/local check executed |
| BASE41, full uniform exclusion, all external analytic inputs | Not established by this work | No complete proof acceptance |

## What is proved, including the delicate points

**Attainment is stronger than proposed.** It holds for every positive
target, not only when `A_n(c)>=0`. Symmetric Bernoulli at raw threshold
`H=n` gives `A_n(c)>-c`. Along a maximizing sequence the discrepancy is
therefore bounded below by a positive constant, while
`c rho <= sqrt(n)-a` bounds third moments. Only the first two powers use
uniform integrability. Closed-event upper semicontinuity at moving
thresholds and lower semicontinuity of `rho` give a maximizer; maximality
then forces convergence of the third moments. The thresholds may be
negative. No density or continuity at the chosen atom is assumed.

The exact logical equivalences are `A_n(c)>0 iff C_n>c`, equality iff
equality, and `A_n(c)<0 iff C_n<c`. The equality case follows from a
bounded-moment sequence of scores approaching `c`; it does not require
the old ratio-attainment lemma. Thus excluding `a>=0` gives a strict
tail, whereas excluding `a>0` gives only the weak target.

**Raw contamination is essential.** After standardization the objective
is `sqrt(n)*(raw closed CDF - shifted Gaussian) - c*r_epsilon/v_epsilon^(3/2)`.
The derivative is exactly the proposal's `I_c`, with no division by `rho`.
Its expectation is zero. It is upper semicontinuous, not merely almost
everywhere nonpositive, so equality extends to the entire closed support.
The leading `-c|y|^3` excludes distant support points. The ordinary ratio
of this new maximizer is `C_act=c+a/rho`; it generally is not `C_n`.

**The support term is exactly `-n a`.** If `C_{n-1}<=c`, substitution in
the same-law contact equality gives

\[
0\le\mathcal H_n(H,y)
 +c\{-|y|^3+\tfrac32\rho y^2+3\beta y+\rho e_n\}-na.
\]

For `a>=0`, the old zero-loss support upper bounds remain valid after
dropping the last term. The universal structural moment bounds apply to
`C_act>=c`; they do not need the law to maximize the ratio. All later
moment caps must still be acquired before use. The all-real-H envelope,
both signs, frozen moment caps and negative-cubic-coefficient gate remain.

**The extra `H²a` is real.** Integrating the fixed-c contact polynomial
against the zero-bias density and using the truncated first-moment identity
gives

\[
P_0=H^2(c\rho+a+\gamma\phi(z)/2)
 -H\{cK_1+\phi(z)(M_4-3)/6\}+cK_q.
\]

The gap-slack calculation then gives, at `c=C_E`,

\[
(n+H^2)a+nc\rho(1-e^{-H^2/(2n)})
 +\frac{n\phi(0)e^{-H^2/(2n)}}6D+n^{3/2}L=\mathcal R_c(H).
\]

Here `H` is raw, so the coefficient is `n(1+z²)` in standardized units.
Compact support is proved before fourth and fifth moments are used. The
gap measure is `[u,v)`, not `[u,v]`. The retained compensated-inversion
lemma has no score coefficient and applies unchanged; obtaining a small
bound on its complete integral remains an independent input.

Weight removal still needs a first proved ceiling `R_c<=r0<2N/5`.
From conservation,

\[
\phi(z)(\gamma+3J)/6
=(1+H^2/n)a+c\rho+\sqrt nL-\mathcal R_c/n>0.
\]

This licenses the same Gaussian-weight removal and phase price. Omitting
the license would remain an error in the new formulation.

## Proof-level transport, not automatic acceptance

The key distinction is between three quantities: the **contact/remainder
multiplier** (now fixed `c`), the **actual score** (`c+a/rho`), and the two
**deleted-sum global constants**. The latter remain genuine predecessor
bounds. Formal scalar boxes for the multiplier do not need to enclose
the actual score once their proof has been generalized.

For the transport theorem fix `c=C_E` and `N>=3`. Suppose an old raw bound is proved for every parameter tuple in a domain,
with multiplier `t` in `[t0,t1]`, and `c` lies in that interval. Substitution
`t=c` proves the same bound for `R_c`. This applies to the reviewed atlas:
its bound on the explicit constant, linear and quadratic coefficients is
proved before conservation is used. A finite ordered schedule of such
bounds therefore transports by induction, provided its moment/support
inputs, sign gates, complete frequency ranges and index coverage all hold
for the new law. It is unnecessary to construct a fictitious ratio
maximizer with score `c`.

The two-interval charge does not obstruct reuse. Its old bound

\[
B_*=\max\{G(C_0),G(\chi),G(C_1)-N(C_1-\chi)\}
\]

still bounds `G(c)`, because `C0<c<chi<C1` and convexity gives
`G(c)<=max(G(C0),G(chi))<=B_*`. The high-score corner and its subtraction
are unnecessary for that conclusion. Likewise the six-corner charged
envelope contains `c<0.40974`, where the formal charge
`n(t-0.40974)_+` is zero. Future direct fixed-c evaluation can omit the
variable-score interpolation; an outward interval for the irrational
constant `c` may still be required. This is not a claimed sixfold runtime
saving or a new numerical PASS.

Actual-score feedback must be rederived, rather than transported as a
coefficient identity. After the raw license and nonnegativity give
`(n+H²)a<=R_c`, a strict bound `R_c/rho<V` implies, if the cell survives,

\[
C_{\rm act}=c+a/\rho<c+\frac{V}{n+H^2}\le c+\frac{V}{N}.
\]

Here `V>0` follows from survival and `a>=0`; `V<=0` excludes the cell.
Thus the old numerical shape of this optional output is available, but
its proof uses the new balance. It must not be fed back as an assertion
that the contact multiplier equals the actual score. A scalar coefficient
interval may use such a ceiling only after confirming that it contains c.

The local right side also transports. With the same count, phase, law and
Gaussian corrections, the new identity is

\[
a+\rho_B(c-C_B)
=\sqrt n\pi_k\{Q/\pi_k-f(u)\}+R_c^{\rm cmp}.
\]

The old strict negative nearest-count and whole-count witnesses therefore
still exclude `a>=0` when `C_B<=c`, if their **right-side** estimates are
universal at multiplier `c`. The signed cubic repair meets this test:
its proof uses only the multiplier interval, and `c` lies between `0.4`
and `0.4226`. A negative cubic gain still requires the upper multiplier;
fixing the target does not remove this sign rule. At zero noise a separate
strict finite-binomial result is required for the strict tail, and the
maximum over the threshold still occurs at a binomial atom.

The proposal's weaker inequality `E_c<=rho_B(c-C_B)` alone proves only
`a<=0`. It cannot exclude equality. A strict inequality, or an independently
strict binomial margin with an appropriate weaker envelope, is necessary.

## Exact current-source dependency table

All locations are relative to `manuscript/arxiv-v1/` at `ca4943a`.
These are ranges for review, not claims to have reverified every old
statement contained in the files.

| Edge / source location | What the proof uses | Fixed-target disposition |
|---|---|---|
| `sections/02-extremizers.tex:16–87` | Tightness, lower moment UI, moving closed event; ratio normalization | Replaced for the new branch by excess attainment proved here. No UI3 needed. Old theorem remains valid and preserved. |
| `sections/02-extremizers.tex:96–176` | Raw mixture derivative, support contact, positive cubic coefficient | Fixed-c derivative and majorant proved here; the actual score need not be extremal. |
| `sections/04-support.tex:8–34,119–158,232–240` | Contact, predecessor comparison, acquired moments, universal H envelopes and rays | Transfer to `c` with extra `-na`; all numerical support inequalities still require their stated moment inputs. No upper excess is used. |
| `sections/05b-conserved.tex:14–139,202–261` | Contact polynomial moments and two evaluations of slack | Replace the identity by the proved `(n+H²)a` identity. The pointwise raw remainder uses coefficient `c`. |
| `sections/05b-conserved.tex:143–200` | Compensated inversion, finite second moment of signed measure | Unchanged analytic lemma; its assumptions follow after compact support. It contains no contact coefficient. |
| `sections/05b-conserved.tex:290–365` | Raw ceiling license, defect sign, density floor and phase-price signs | Proved fixed-target versions keep these gates and the stronger excess charge. |
| `appendices/fourier-analysis.tex:775–786` | Formal profile, coefficient interval, positive barrier K and predecessor loss | New zero-barrier profile uses `K=0`, `c` in its coefficient box and sharp predecessors. Positive-K profiles do not transfer without a new lower-excess premise. |
| `appendices/fourier-analysis.tex:798–1470` | Complete low/high frequency, moment/support domains, signed cancellation, floor gates | Multiplier-independent analytic inputs remain. No decay at lattice frequencies is gained. This note does not independently validate every retained proof. |
| `appendices/fourier-analysis.tex:1477–1486,2411–2418` | A raw bound yields an actual-score upper bound | May be omitted if no consumer needs actual score; if retained it follows with `C_act=c+a/rho` and the stronger charge. A negative allowance excludes the cell. It is not a contact-coefficient identity. |
| `appendices/fourier-analysis.tex:1697–1747,2370–2440,2545–2586` | Universal coefficient bounds, separate convexity, positive curvature and finite ordered refinement | Scalar bounds transport at `t=c`. Coefficient boxes containing c can reuse old targets without requiring `C_act` in those boxes. First raw ceiling and all arithmetic/domain checks remain. |
| `sections/06-resources.tex:15–52,89–100`; `appendices/fourier-analysis.tex:2894–2941` | Score-corner interpolation and charged envelopes | Low formal interval already bounds `G(c)`. New evaluation can omit variable-score corners/charge; old larger envelope remains a valid bound if its scalar inputs are established. Its negative-cell consequences are not newly accepted here. |
| `appendices/fourier-analysis.tex:3103–3149,3298–3509` | Contact derivative coefficient, two separate deleted concentration caps, one strict budget | `c` lies in the coefficient interval `(0.4,0.4253]`. Sharp predecessors give the distinct deleted caps. Extra nonnegative excess can be dropped. All interval, slope, strictness and actual-floor gates remain. |
| `appendices/uniform-bridge.tex:67–93,126–177` | Floor42 deletion factors, strict-gap bounds, single strict resource and complete comparison | Retain all floor42 gates. In the transported statement the resource excess is `(n+H²)a`; its coefficient role is separated from deleted constants. Existing finite predicates are still inputs. |
| `sections/05c-counts.tex:52–117`; `appendices/fourier-analysis.tex:3544–3608` | Exact master identity, repair multiplier and strict negative count witnesses | Replace left side by `a+rho_B(c-C_B)` and repair multiplier by c. Same right-side proofs exclude nonnegative a. Zero-noise strictness remains separate. |
| `appendices/local42-refinements.tex:387–459` | Scalar multiplier in positive interval and negative-cubic sign rule | Universal repair bounds apply at c; no actual-score cap needed in this reformulated repair. Both multiplier positivity checks and zero clamp remain. |
| `sections/08-certificates.tex:17–28,49–74`; `sections/03-smoothing.tex:70–126` | Old LOCAL42 entry: ratio optimizer, upper excess, own-score caps, deleted caps | Replace by a new excess-maximizer exclusion under sharp predecessors. Then the recurrence is not an entry edge. The old LOCAL42 assumption itself is not proved or silently identified with the new one. |
| `appendices/finite-analysis.tex:3295–3342` | Independent 40–42 provider still derives U and uses `0.54 Q_+/m` in a Gaussian support bound | Real remaining consumer. This note does not redesign or discharge that finite-base provider. Recurrence removal is not repository-wide. |
| `appendices/finite-support.tex:427–444` | Positive-barrier support rows, including K=0.54 at46 | Outside the zero-barrier transport; preserve unless separately redesigned. |

The literal search and hashes for these dependencies are retained in
`runs/strategy-v4-20261027/excess01/dependency-search.*`. The upper
`n(C_n-c)<0.3` assertion appears in the recurrence and its introductory/
entry summaries; it is not used in the reviewed fixed-target raw atlas,
support proof or count RHS. A number `0.54` elsewhere is not automatically
the same premise: the explicit 40–42 support term above is a genuine
separate consumer.

## Resulting conditional DAG

```text
genuine BASE through N-1
  -> first index n>=N with C_n>=c
  -> predecessors <=c                         [no recurrence edge]
  -> attained fixed-target excess a>=0
  -> fixed-c contact -> compact support
  -> universal structural moment caps + predecessor comparison
  -> elementary support radii
  -> complete Fourier primitives + scalar boxes containing c
  -> raw ceiling license -> phase/defect/leakage resource
  -> ordered same-law moment/support/confinement schedule
  -> complete signed count cover + fixed-c repair bounds
  -> strict negative count RHS (positive noise)
     or strict finite-binomial bound (zero noise)
  -> contradiction
```

Every edge after the initial support has its original analytic, index and
numerical scope unless explicitly restated and proved above. There is no
fresh independent full check of the Fourier atlas or native root coverage.
The transport theorem states exactly the conditions under which their
proved scalar inequalities may be used; it does not grant them.

## What can actually become unnecessary

In the **new zero-barrier tail composition**, ratio attainment/contact as
the selected extremal problem, variable-score intervals in coefficient
bounds, their score-corner interpolation, two-interval score charging, and
the scalar recurrence used solely to acquire own-score/upper-excess entry
caps are no longer logically required. One may retain the old larger
scalar bounds containing c during a conservative transition.

The numerical predicates for support, moment/Fourier acquisition,
confinement and local comparison do not disappear just because their
multiplier is fixed. Their domains and ordered ancestors remain. The
finite-base provider, positive-barrier calculations, both deleted-sum
caps, strict zero-noise comparison, and the complete signed count cover
are not removed. No count of deleted native tasks or wall-time saving is
asserted. Original certificates are preserved; no production edit is
authorized by this note.

## Reproduction and adversarial evidence

`excess-check.py` uses only Python's standard library and exact rational
Laurent-polynomial algebra. The recorded run took about 0.39 seconds:
contact-polynomial moments, first/second slack and hinge elimination pass.
Its finite-law check covers eight standardized laws, 108 zero-bias/hinge
instances, and 324 raw-mixture CDF derivatives. Thresholds include both
signs, zero, atom collisions and boundary values. Ninety-eight collisions
reject replacing `[u,v)` by `[u,v]` in the gap mass. This is not a search
for an extremizer and does not claim any tested arbitrary law satisfies
contact.

Negative controls also show that an open-event contact function is not
upper semicontinuous at an atom, and that bounded third moments do not
imply UI3: the standardized tiny-far-atom family has third moment tending
to 2 while its weak Bernoulli limit has third moment 1. Dropping `H²a`
leaves exactly that nonzero symbolic residual. Replacing a strict target
comparison by a weak endpoint allows `a=0`.

`excess-transport-check.py` checks the modified count identity in 512 exact
rational instances, the explicit quadratic chord-gap identity at 101
rational points, and a negative-cubic multiplier control (about 0.03
seconds). General convexity and schedule induction are proved in the note,
not inferred from those finite samples. All streams, versions, commands,
return codes and source hashes are in `runs/strategy-v4-20261027/excess01/`.
No inherited/native checker, campaign, install or network mutation ran.

The final standalone PDF has eight pages. Compilation succeeded; there
are no unresolved references or overfull boxes. One nonfatal underfull-box
notice remains in the status table. All eight final pages were actually
inspected at 100 dpi, as well as in an overview, with no clipping or
overlapping equations. The final PDF SHA-256 is
`1b2052cbc5c62ac7cc2354f9e008c8c220d39dd47831c6eefe7034f4adaaf591`.
The first two compilation attempts failed on a missing script-font macro
and a blank paragraph inside displayed math; their exact input snapshots,
return codes and diagnostic streams are preserved. These were authoring
errors, not failed mathematical checks. The third build succeeded; the
fourth removed a largely empty final page. The final source is inputtable
without the original script-font macro.
