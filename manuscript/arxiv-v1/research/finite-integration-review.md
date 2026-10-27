# Focused independent review of the finite and local interfaces

Date: 27 October 2026. Review worktree/branch:
`manuscript-review-core`, `manuscript/review-core-20261027`.

The primary reviewed artifact is `finite-analysis.tex` at commit
`559e898ffebc9c697e7db3d4197fbcdecd444021`, SHA-256
`1e33d456c855cac70097adaa84c3cb4b4773874b9b0616fdce85c038b5e4322a`.
This is a bounded adversarial integration review, **not verification of all
50 pages**. It reads the selected statements, their immediate proofs and
dependency conditions. It neither edits the constructor's worktree nor
accepts any inherited numerical certificate.

The supplementary source review covers the complete three short files
`local42_improvements.tex`, `local42_signed_gaussian_v2.tex`, and
`signed_cubic_repair.tex`, supplied read-only under `/private/tmp` for the
coordinator's new `local42-refinements.tex`. Their hashes are recorded in
`runs/manuscript-20261027/finite-integration01/local42-source-hashes.json`.
This review is primarily of their source mathematics, not of the native
implementations consuming them. A final focused read of the coordinator's
`local42-refinements.tex` at commit `f5aaa8e` confirmed the positivity
hypotheses and conditional numerical presentation described below.

**Recommendation:** suitable for integration as conditional analytic
material. No blocking algebraic error was found in the requested finite
interfaces. The source mass-localization statement omitted explicit
$v_->0$; the coordinator's final copy now states this and also requires
$n\ge N\ge2$, an interior legal count and $\pi_k>0$. This finding is
resolved. Numerical coefficient, quadrature and complete-cover
acceptance must remain conditions. The new manuscript still does not have
an accepted finite base or a complete all-index theorem from these texts.

| Reviewed item | Mathematical status | Execution status |
|---|---|---|
| N1 cubic-dual implication and tails | Independently checked, conditional on the whole-line dual cover | Selected rational tail comparisons passed; 150-cell native acceptance not run |
| G3 condition and G4 dependency | Correct explicit conditional dependency in the inspected statements | Scalar target comparisons passed; tensor/ROOT4 predicates not run |
| Fifth-index support/cutoff entry | Correct conditional composition with actual-index support still required | Both beta caps and exact structural-tail endpoint passed |
| Weighted invariant and floor noise scaling | Independently rederived as a finite same-law implication | No saved resource sequence or finite floor producer executed |
| Signed Gaussian and cubic repairs | Independently rederived with the listed sign/domain gates | No local kernel or normalization checker run |
| Harmonic constant | Bernstein-to-continuum implication and outward directions checked; coefficient positivity remains conditional | No 896-coefficient acceptance run |

## Finite appendix review

### N1: lines 796--828

The dual condition is
$L_a-v+ux+vx^2+(2/5)|x|^3-\mathbf1_{x\le b}\ge0$ on the entire real
line. Its expectation is
$L_a+(2/5)\rho-F_X(b)\ge0$, since $EX=0$ and $EX^2=1$.
The signs of the constant $-v$ and quadratic $vx^2$ are correct. For
$t\in[a,b]$, the chain
$F_X(t)-\Phi(t)\le F_X(b)-L_a$ has the correct directions.

Cantelli gives the left tail $F_X(t)\le1/5$ for $t\le-2$.
The right-tail proof gives $\Phi(1)>13/16$, so the discrepancy is below
$3/16<2/5\le(2/5)\rho$. The elementary input $\phi(0)>3/8$ follows,
for example, from the already available upper bound $\pi<22/7$.
Reflection uses $F_X(t-)$ and therefore retains atoms correctly.
The statement does not claim the dual coefficients exist or that all 150
cells pass. Whole-line inequalities, both rays, closed boundaries and
complete coverage are all in the condition.

### G3 and G4: lines 1119--1163, 1276--1289, 1356--1390, 1492--1608, 2092--2169

G3 uses the explicit constant $\Lambda=59/250$. Its continuous-domain
condition requires both the pointwise majorant on the full cube and the
same-law expectation bound on the outer moment domain; it does not accept
an optimizer's status or sampled positivity. The cube includes the
localized witness support and the threshold partition is closed. This
review checked the implication and scope, not the full 59-feature
construction or its continuous-domain predicates.

G4 explicitly assumes the G3 theorem's conclusion before using
$C_3\le59\sqrt3/250$ in the unrestricted witness localization. The exact
identity
$c_0^2-K_3^2=1069/1562500>0$, with $c_0=256/625<T=4097/10000$, checks.
Thus G3 numerical completion cannot disappear behind G4's theorem label.
The three-point law is described as a reference law rather than an
extreme-point reduction. ROOT4's terminal proposition explicitly requires
all parent/child inequalities, closed joins and both tails. It states no
successful completion count. The canonical moment calculations and all
physical smoothing arguments within ROOT4 were not independently audited
in this focused review.

### Fifth index: lines 2174--2310 and 2497--2618

The zero allowance is valid under the two stated premises
$C_4\le C_E<C_5$: for the same attained marginal,
$R_4(P)\le C_4<C_5$. This proves only $q_5=0$; it does not assert that
noise or defect vanishes. Compact support follows from generic contact,
but the listed **quantitative** radii remain separate actual-$n=5$
obligations. In particular the new support result for $n\ge42$ cannot be
substituted. The opening analytic-input item and the fifth-index text both
preserve this distinction.

The moment cover joins at $\rho=6/5$ and has closed signed-beta seams.
For $0\le b<1$, the function $(1+b^2)^2/(1-b^2)$ increases with $b$.
The exact squared comparisons therefore verify the two outward caps
$b_2\ge b(237/200)$ and $b_3\ge b(6/5)$ without a floating-point radical.

At the structural cutoff the exact value is

$$
\frac{3031}{10000}\left(1+
 \frac{323}{500(7361/4000)}\right)=\frac{819}{2000}.
$$

The cutoff has **zero reserve against $819/2000$**, so the source's
“at most” is the correct relation. There remains a strict reserve against
$c_0=4097/10000$, and the structural majorant decreases with $\rho$.
The Fourier strips must first acquire their own support and must include
all four smoothing terms and the infinite normal tail. None is marked as
accepted. The resource route explicitly starts without a central-gap seed;
the six original count roots and thresholds beyond them still need complete
coverage. The final theorem concludes the weak bound $C_5\le C_E$ from
strict contrary witnesses, as its proof requires.

### Weighted reuse: lines 3185--3228 and 3351--3509

The invariant is $\mathcal R_{\rm actual}\le r$ and
$mD_{\rm actual}\le Nd$, where $m$ is the actual index. It does not
replace the weighted bound by $D\le d$. Indeed the latter alone is
insufficient whenever $m>N$; the diagnostic includes a simple exact
negative control.

From the stated affine resource
$D\ge b+g d_{\rm in}+(N/m)h_N\lambda_m$, multiplication by $m$ gives

$$
Nd\ge mD\ge mb+mgd_{\rm in}+Nh_N\lambda_m
       \ge N(b+gd_{\rm in}+h_N\lambda_m).
$$

Every replacement is licensed by nonnegative coefficients and $m\ge N$.
It yields the joint actual-noise bound without identifying $ms$ with the
floor noise $Ns$. Negative budgets are excluded before division, while
zero cases must retain their original endpoint handling.

The floor25, floor31 and literal floor40--42 contracts remain distinct.
Actual support callbacks, own caps, deleted-index domains, signed inverse
corrections and complete local joins remain explicit prerequisites. In
particular $I/m\le\max(I/40,I/42)$ is used only on that finite range,
and the saved support primitive retaining favorable Gaussian terms is not
treated as monotone without its separate indexed proof. This review
checks the stated invariant and scope discipline, not every source
callback or implementation binding in those contracts.

## Local42 source review

### Positive and negative Gaussian phases

Keep the actual $k$ and $\delta=k-np=h-u$ fixed while the integration
variable $t$ moves. With the stated Stirling remainder, the exact formula is

$$
\log f'(t)=-\tfrac12\log(1+s/v)+\frac{\delta^2}{2nv}
               -\frac{(\delta+t)^2}{2n(v+s)}-\zeta.
$$

For positive phase, replacing the denominator of the **nonnegative square**
$(\delta+t)^2$ by $v$ bounds this expression from below. Together with
$\log(1+s/v)\le s/v$, it gives exactly
$\log f'(t)\ge-(\lambda+2\delta t+t^2)/(2nv)-\zeta$.
This step does not need $2\delta t+t^2\ge0$; replacing the denominator
directly on that signed expression would be an invalid alternative proof.
The convex quadratic on $0\le t\le u$ is bounded by
$\max(0,2hu-u^2)$, then by the stated projected maximum $G_+\ge0$.
The replacement $v\mapsto v_-$ is performed only after this nonnegative
upper numerator is available. The resulting signed correction has the
claimed upper bound and the claimed $A+B/\lambda$ form for $\lambda>0$.

For negative phase $u=-r$, the first two terms cancel in the required
direction because
$\log(1+s/v)\ge s/(v+s)$ and $\delta^2\le D^2\le Nv_-\le nv$.
The remaining quadratic is bounded by its maximum on $[0,b]$ at the
projection of $h_*+b$. This gives $G_-\ge0$ and
$\eta_-=G_-/(2v_-)+Z\ge0$. The strict gate $\eta_-<N$ is essential
before $e^x\le(1-x)^{-1}$ is used. Finally
$u-f(u)=\int_0^r(f'(-t)-1)dt$ has the source's sign. Both formulas work
for either sign of $h$; neither reflects the marginal or changes the count.
Positive own-count mass, the global Stirling segment, all denominator
gates, nonnegative inverse-correction checks and the separate zero-noise
endpoint remain necessary.

The mass-localization proof is correct once $v_->0$ is explicit. Its
logarithmic bound implies
$\sqrt n\pi_k\ge(.39886/q_+)e^{-A_*/n}$ with
$A_*=D^2/(2v_-)+Z_N(D)\ge0$. The linear exponential lower bound is valid
even when its final bracket is negative; a previously proved positive
mass lower bound can then be retained. The smaller $D$ does not license
shrinking the original domain on which the Stirling constants were proved.

### Cubic multiplier and repair sign

The sign-class support assumptions give
$pEU_1^3-qEU_0^3\ge-ds$ and
$3pq(s_0+s_1)\ge3ps$ for $p<1/2$. Subtracting the quadratic Taylor upper
bound for $(1+s/v)^{3/2}$ yields the source bracket $Q$ exactly. Its
lower bound $Q_*$ has the correct directions: the first term increases
with $p$, $(1-2v)/v$ decreases with $v$, and $s\le\Lambda/N$.

For $A=C/(v+s)^{3/2}\in[m_-,m_+]$ and $Q\ge Q_*$, positivity of $A$
first yields $AQ\ge AQ_*$. If $Q_*<0$, the latter is bounded below by
**$m_+Q_*$**, not $m_-Q_*$. The minimum of the two endpoint products
therefore gives the correct signed gain. The normal variance term is
nonpositive at $\delta\le0$ and otherwise is bounded using $\delta_+$.
Clamping its combined coefficient at zero before replacing $n$ by $N$
is correct and necessary. The squared multiplier checks additionally need
positivity; the source says so explicitly.

### Harmonic and joint-resource refinements

The interval resource substitution $d\le d_*(1-L/\Lambda)$ follows from
one joint plane, not from independent marginal caps. The amplitude-plus-gap
span bound and the monotonicity of the curvature denominators are correct
on their positive domains. Cache reuse in increasing noise bands also
requires that actual execution order and all other dependencies be fixed;
the source argument does not justify arbitrary caching.

For the harmonic lemma, the degree-14 alternating upper polynomial has
the stated remainder sign on $[0,2/K]$. Positive coefficients use $\pi_+$
and negative coefficients use $\pi_-$, so each replacement raises that
polynomial. Division by $x$ is removable at zero. The displayed
degree-13 Bernstein transform and 64 closed subintervals are correct.
**Positivity of all 896 coefficients, the claimed smallest coefficient,
and the directed $\pi$ endpoints were not executed in this review.** They
must be conditions in the new appendix unless separately accepted. Given
those premises, the factor $1000/4553$ and half-factor $500/4553$ follow
correctly in the fractional-part gain. A historical PASS cannot replace
that premise.

## Evidence and limitations

`check_finite_integration.py` is a new standard-library rational diagnostic.
Run `finite-integration01` completed in 0.020 seconds with exit 0 and 14
selected scalar/negative-control checks. Its stdout, stderr, source hash,
Python version and reviewed appendix hash are retained. Reproduce with:

```sh
python3 manuscript/arxiv-v1/research/check_finite_integration.py
```

No native checker, harmonic acceptance program, tensor positivity program,
ROOT4 cover, fifth-index campaign or saved resource sequence was run.
No claims are made about the remaining 50-page analytic content, full
implementation coverage, or source-provider provenance beyond the recorded
bytes. This focused review strengthens the inspected implications and
identifies their boundaries; it does not supply BASE41, eliminate a
certificate, or authorize an unconditional theorem.
