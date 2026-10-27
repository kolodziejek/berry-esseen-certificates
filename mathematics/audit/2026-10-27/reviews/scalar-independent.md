# Independent review of the scalar redesign

Reviewed commit: `ac7bd069c9d5afe6d0dfe5a9c86c9a095644ff99`.
Immutable research baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
Fork: `kolodziejek/berry-esseen-certificates`.
Review branch: `audit/review-scalar-20261027`; date: 27 October 2026.

**Recommendation: no blocking scalar defect found; suitable for review and
merge as an audit-only addition.** This is not a recommendation to remove
certificates, install the new assembly in the manuscript, or declare the
Berry–Esseen conjecture proved. The conditional acquisition/exclusion inputs
remain undischarged by this scalar review.

The reviewer did not construct the scalar proof or its checker. The independent
work below consists of direct mathematical rederivation, reading the literal
archive interfaces, and a separately written bounded diagnostic. Repeating
the submitted checker is recorded separately and is not called independent
verification of its implementation.

| Reviewed result | Mathematical status | Execution status |
|---|---|---|
| Support-free recurrence for all standardized iid real laws with finite third absolute moment, every integer `n>=2` | Independently rederived by conditioning and Gaussian calculus | Finite constants freshly checked; calculus is a written argument, not a program output |
| Scalar entry at `n>=47` from `C_(n-1),C_(n-2)<=C_E<=C_n` | Independently derived and checked, including `n=47` and equality | Exact independent integer/rational checks passed |
| Weak global assembly and separately stated strict tail from a weak prefix through46 | Correct conditional implications, with distinct contrary sets | No archived/native acquisition or exclusion checker run |
| Full LOCAL47 or all-index sharp upper theorem | Not established by this review | No full replay or certificate campaign |
| Eight finite-law recurrence diagnostics | Exploratory consistency checks, not proof | 325 tested same-law inequalities passed; Gaussian values are floating point |

## Reviewed files and source interfaces

The review read the whole of these three new files:

* `mathematics/audit/2026-10-27/scalar-review.md`;
* `mathematics/audit/2026-10-27/check_scalar.py`;
* `mathematics/audit/2026-10-27/scalar-proof/main.tex`.

The claims were also checked against `paper/analytic-supplement.txt:6479–6522`
(the recurrence), `paper/main.tex:102–139` (attainment, including equality),
and `paper/main.tex:173–190` (same-law predecessor allowance).

The source LOCAL47 interface was read directly from
`verification/finite-tail/sources/BE_cutoff49_20260930.zip`, without importing
or executing archived code:

* `BE_cutoff49_20260930/paper/sections/global_route.tex:81–115` says that no
  `n>=47` can simultaneously satisfy
  `0<=C_n-C_E<=.7/n`, `delta_n<=.19`, `C_n<.4247`, and
  `C_(n-1),C_(n-2)<.4253`.
* `BE_cutoff49_20260930/paper_entry/resource_entry.tex:402–420` states uniform
  acquired entry for an attained positive maximum under the corresponding
  non-strict caps, given the shared support/strip implications and exact
  ordered schedule. It explicitly has no upper bound on `n`.

These are equality-inclusive **supplied implications**, not independent
evidence that their numerical or analytic premises are all true. The new
scalar note correctly leaves that distinction explicit.

## Independent derivation and adversarial checks

Write `v=n-1>=1` and `G_v(H)=Phi(H/sqrt(v))`. For a fixed law `P`, let
`rho=E|X|^3`. Conditioning on its last summand gives

\[
|P(S_n\le H)-E G_v(H-X_n)|
\le \rho C_v/\sqrt v.
\]

The predecessor bound is applied to that same law at each threshold `H-X_n`.
It does not replace a convolution by a different marginal or differentiate an
atomic CDF. The defining global supremum is finite: `rho>=1` and
`Delta_v<=1` imply `C_v<=sqrt(v)`.

For the spatial Taylor step, the third derivative of `G_v` is
`v^(-3/2) phi''(H/sqrt(v))`. Its norm is `v^(-3/2) phi(0)`:
`abs((z^2-1)exp(-z^2/2))<=1`, with the exterior maximum attained at
`z^2=3` and equal to `2 exp(-3/2)<1`. Taylor expansion through degree two
and the actual mean/variance therefore leave an integrated error bounded by

\[
\phi(0)\rho/(6v^{3/2})<\rho/(15v^{3/2}).
\]

This is where the third absolute moment is used. No fourth moment, bounded
support, density, third-moment uniform integrability, or fixed-law limiting
argument is required. A rare atom arbitrarily far away is charged by its
actual contribution to `rho`.

Direct differentiation yields `partial_v G_v=G_v''/2` and
`partial_v^2 G_v=G_v^(4)/4`. The integral Taylor remainder over the variance
interval `[v,v+1]` has the factor `(1/4) integral_0^1(1-t)dt=1/8`.
Since `G_w^(4)=w^(-2)phi'''`, the heat error is at most
`norm(phi''')/(8v^2)`. Gaussian Fourier inversion has normalization
`1/(2 pi)`; differentiation is justified by absolute integrability of
`abs(t)^3 exp(-t^2/2)`. Its integral is `4`, so the norm bound is `2/pi`,
and the heat error is `1/(4 pi v^2)<2/(25v^2)`.

Adding these three inequalities and multiplying by `sqrt(n)/rho`, using
`rho>=1` only in the heat term, gives precisely

\[
C_n\le\sqrt{n/(n-1)}C_{n-1}
 +\sqrt n/[15(n-1)^{3/2}]+2\sqrt n/[25(n-1)^2].
\]

The argument works at `n=2`, where `v=1`. All estimates are uniform in the
raw threshold `H` and the law after dividing by `rho`; thus they cover varying
laws and thresholds. Closed events suffice for the stated `Delta_n`; their
left limits also cover strict events and reflected negative jump edges.

The new note's elementary constants were separately checked. Integrating
`1-t^2<1/(1+t^2)<1`, and placing `4 arctan(1/5)-arctan(1/239)` in
`(0,pi/2)`, makes its tangent-one calculation a valid Machin identity, with no
wrong-branch ambiguity. It yields `pi>281476/89625>157/50>25/8`.
Using `sqrt(10)<19/6` then gives
`C_E^2<1900/11304<1681/10000`. The last cross-product difference is `2024`.

For scalar entry set `s=sqrt(n/(n-1))`. Dividing
`s^2-1=1/(n-1)` by `s+1` gives

\[
n(C_n-C_E)\le {n\over n-1}
\left({C_E\over s+1}+{s\over15}+{2s\over25\sqrt{n-1}}\right).
\]

For `n>=47`, replace the nonnegative factors in their safe directions:
`n/(n-1)<=47/46`, `s>1`, `s<1011/1000`, `sqrt(n-1)>6`, and
`C_E<41/100`. The square-root upper gate has integer margin
`46*1011^2-47*1000^2=17566`. Clearing the inner denominator at `150000`
gives `30750+10110+2022=42882`, hence the bound is
`47*42882/(46*150000)=335909/1150000`. This is below `.3` with margin
`9091/1150000`. The own cap follows with margin `3909/470000`.
Both deleted caps follow from `.41<.4253`, and the predecessor loss is zero.

The proposed weak and strict assemblies correctly use different contrary
sets. A least index with `C_n>C_E` yields only the weak conclusion. The
constant numerical sequence `C_n=C_E` satisfies the scalar recurrence and
is not contradicted by a positive-excess-only exclusion. For strictness, the
least index with `C_n>=C_E` must be chosen **inside the tail `n>=47`**, since
the prefix is only weak. At `n=47` its two predecessors are 46 and45, both
in that prefix; at later indices they are either in the prefix or in the
already strict tail. Therefore both remain at most `C_E`. The archive's
literal equality-inclusive LOCAL47 and acquisition interfaces match this
argument, subject to all their retained premises.

The supplied attainment proof also handles equality without asking a weak
finite prefix to be strict. Its bound on third moments preserves first and
second moments under weak convergence, then Portmanteau at `H+epsilon`
handles moving thresholds. The inequality
`C_n>=R_n(P)>=C_n*b/rho(P)>=C_n` forces the missing third-moment equality
by extremality. This step does not assume third-moment uniform integrability.

## Executions actually performed

Fresh evidence is in `runs/least-counterexample-20261027/review-scalar01/`:
the diagnostic source, separate stdout/stderr files for each invocation, and
`metadata.json` containing commands, Python/platform version, return codes
and input hashes. Both commands returned zero under CPython 3.9.6:

```sh
python3 -I -B mathematics/audit/2026-10-27/check_scalar.py
python3 -I -B runs/least-counterexample-20261027/review-scalar01/independent_diagnostics.py
```

The submitted checker again passed its fixed rational comparisons and all
13 negative controls. Source inspection found that its normal invocation
uses integer/Fraction constants and checks strict comparisons in the required
directions. This review does **not** certify arbitrary external calls to its
internal `check(p)` function as a general proof-object API.

The separate diagnostic did not import that checker. It used integer
cross-products and the independently cleared denominator above. It also
confirmed that this particular square-root bound fails at `n=46` (margin
`-4555`) and that its rational total is greater than `.29`. Those are
limitations of this chosen envelope, not counterexamples to the recurrence
or to a different envelope.

For the finite-law diagnostic, all convolution probabilities and unnormalized
moments were rational. Normalization and Gaussian evaluations used ordinary
floating-point `sqrt` and `math.erfc`, so the displayed margins are **not
rigorous enclosures**. Both jump edges at every sum atom were evaluated.
The laws were symmetric/skew Bernoulli, near-endpoint Bernoulli and its
reflection, a tiny middle atom, a tiny remote atom, a four-point law with
collisions, and a nearby four-point perturbation. The first seven used all
indices 2–47; the last used 2–4, totaling 325 inequalities for the stronger
same-law recurrence with `R_(n-1)(P)` in place of `C_(n-1)`.
All passed. The smallest numerical margin was about `0.00174682`, for the
remote-atom law at `n=46`; tested standardized atom thresholds reached about
4847.68. These computations neither prove a continuous-law bound nor supply
any missing acquisition, uniform remainder, or certificate coverage.

## Findings and limitations

No blocking mathematical defect was found in the reviewed scalar recurrence,
constants, or the two conditional assemblies. No theorem statement needs to
be weakened to accept this audit-only addition. The assumptions cannot be
silently promoted to established numerical inputs.

The exact production consequences remain conditional: the scalar proof does
not remove support acquisition, signed phase repairs, confinement, noise
comparisons, or any finite43–48 consumer of a shared coarse computation.
It does not provide a full public `full_pass`. No archived/native checker,
external service, network request, expensive campaign, or source mutation was
performed in this review. No LaTeX was changed, so no new compilation is
claimed. Agent agreement is not used as a mathematical premise.
