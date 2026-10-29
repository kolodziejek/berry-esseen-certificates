# Independent review: direct acquisition and the one-strip join

**Outcome: no mathematical blocker found at the stated conditional scope.**
The scalar post-entry theorem does not need an inherited probability panel
or support radius. The amplitude `.6` conclusion does need the retained
fixed-target contact inequality and the genuine sharp predecessor. The
composition preserves those hypotheses and does not establish a finite base.

This review was performed on branch `research/acquisition-review-v16-20261029`
from baseline `fb9e918bef3b0a932fb44bf1dae8d3e4a589f932`. It imports or executes
no constructor. I constructed the unified five-count theorem, so I am **not**
claiming an independent review of that theorem here; its separate review is
in `unified-review-v16`. My independent tasks here are the acquisition
derivation, retained contact/heat interface, and exact theorem join.

| Item | Mathematical status | Execution status |
|---|---|---|
| Central/outer gap cost and budget-only localization | Independently rederived and checked | Fresh PASS: exact polynomial identities and scalar gates |
| One-sided cubic cost and λ bounds | Independently rederived for the same actual marginal | Fresh PASS: exact root licenses and coefficient identities on seven actual laws |
| Two whole-ray exclusions | Independently derived from the retained contact/heat inputs | Fresh PASS: negative shifted polynomial coefficients, both boundary tests, multiplier license |
| Local noise join, normalization, zero noise, reflection and least failure | Independently checked at the stated scope | Fresh PASS: exact interface checks and atom negative control |
| Coarse Fourier entry, attainment, fixed-target contact | Retained analytic/certificate inputs; not re-proved here | Source inspection only; no new execution claimed |
| Full iid conjecture or unconditional cutoff | Not established | Not claimed |

## Sources and reproduction

The reviewed sources in `mathematics/simplification-v16/2026-10-29/` are:

| Source | SHA-256 |
|---|---|
| `acquisition-direct.tex` | `c996f20f2202def6fb945f6e7c809a0517930a1a97402e1d11aedd840f88a6fd` |
| `composition.tex` | `76f4a3b591adf7ba6a03461f4fe28c9c5c0fb81d273a404bfe017c38676743fc` |
| `small-common.tex` | `da583ea6712fa159345aa22d402faaa5cd60c518aec51c8aff033c09df636e11` |
| `unified-comparison.tex` | `2be0dc58973a281accb66cf3c8dffd7209592e68278ef4c0c46805708e374938` |

`acquisition-review-sources.json` additionally pins the retained manuscript
sections 04, 06 and 07. The checker rejects a missing or changed source.
Hashes establish identity only. No theorem is inferred from a matching hash.

`runs/acquisition-review-v16-20261029/check01/receipt.json` records a fresh
standard-library Python run, versions, command, source pins, stdout, stderr,
return code and elapsed time. `acquisition-review.py` checks 61 strict
rational gates, three symbolic identities, seven exact actual-law identities,
both full-ray polynomial signs and the composition licenses. Its exact
actual-law arithmetic uses rational enclosures of sqrt(10), independently
of the constructor's quadratic-field implementation.

From an integrated worktree containing the pinned files:

```sh
python3 mathematics/simplification-v16/2026-10-29/acquisition-review.py --source-root .
```

No new LaTeX was written in this review. The reviewed constructor PDFs and
compilation remain constructor evidence, not an independently repeated build.

## Reconstructed gap cost

Let the actual central gap be `(-A-,A+)`, and put `q=1-p`, `v=pq`,
`m=EX+=EX-`, `ell=m/v`. The negative and positive conditional magnitudes
have means `ell p` and `ell q`. Write

\[
x=A_-/\ell=p-a_0,\qquad y=A_+/\ell=q-a_1,
\qquad d=a_0+a_1,\quad w=v\ell^2=1-\theta.
\]

For each positive outer gap, `(b-a)^2 <= 2 int_a^b(t-A+)dt`.
Multiplying by the constant tail weight on that gap and summing yields

\[
J_o^+\le E[X_+(X_+-A_+)^2].
\]

The corresponding negative-magnitude formula is identical. Endpoint atoms
are included by the tail convention; their integration-endpoint values have
zero Lebesgue measure. Countably many gaps are handled by monotone convergence,
since each contribution is nonnegative. Adding the central term
`m(A-+A+)²` and substituting in `D` gives positive residual kernels

\[
k_+(z)=(\sqrt{10}-1)(z+2\ell q)+6A_+,\qquad
k_-(z)=(\sqrt{10}+1)(z+2\ell p)+6A_-.
\]

The remaining deterministic expression, divided by `v ell³`, is

\[
(\sigma+1)p^2+(\sigma-1)q^2
 +6(qy+px-x^2-y^2-xy)
=Q(p)+6\{d(1-d)+a_0a_1\}.
\]

The independent polynomial-ring check verifies this identity exactly.
The residual moment identity follows from
`z³-M³-(z-M)²(z+2M)=3M²(z-M)` and the actual conditional mean `Ez=M`.
Consequently every discarded term in the displayed acquisition budget is
nonnegative. This is a property of the one actual marginal, not of a support
or moment relaxation.

If zero belongs to the support, all gaps lie on one side of zero and the
same tail integration with weight `|t|` gives `J<=rho`. Hence
`D>sqrt(10)-1>.047`. This excludes zero before the central-gap notation is
used. Centering and positive variance provide both signs. The weaker bound
`J<=rho+2m A-A+`, together with `rho>=1`, `gamma<=rho`, `m<=1/2`, gives
`A-A+>=z=(3.162277660-1-.047)/3`. Both bases in the ensuing squared tests
are positive; the checker explicitly verifies this.

The localization order is valid. First `D>=2 z^(3/2)Q` narrows p to
`(.36,.48)`. Positive residual prices give theta<.006 and ell>1.99.
The gap product gives d<.2. On that domain each direct-cost branch increases
in d, so setting d=0 is legitimate **before** removing theta. At d=0,
the derivative in theta has sign

\[
(2-3\theta)C-3(1-\theta)Q>0.
\]

Thus `D>=Q/sqrt(v)` is established with the variance normalization retained.
It is not obtained by deleting the denominator or ignoring noise. On the
left subinterval, Q decreases and v increases; on the right, the weaker
`sqrt(v)<=1/2` suffices. This yields `3/8<p<93/200`, then theta<.0036,
d<.004 and ell>1.996. The rho and beta statements follow from their exact
conditional second/third-moment identities; the signed beta endpoints are
`.066148` and `.2527` in the displayed orientation.

## Noise budget and its zero endpoints

For centered Z<=a with variance t,

\[
E[(a-Z)(Z+t/a)^2]\ge0
\quad\Longrightarrow\quad EZ^3\le at-t^2/a.
\]

The checker verifies the multiplied polynomial identity. If a=0, centering
forces Z=0, so its conditional variance and reciprocal term vanish; no zero
division is licensed. In count coordinates, the reciprocal costs are

\[
\frac{(\sigma+1)\lambda_0^2}{nq a_0},\qquad
\frac{(\sigma-1)\lambda_1^2}{np a_1}.
\]

Pair them respectively with `6nv(1-dbar)a0` and
`6nv(1-dbar)a1`. This produces exactly the two displayed square-root
prices `Y0,Y1`; their p and q factors are correctly assigned. The allocation
variables are the physical ones, `lambda0=nq EU0²`, `lambda1=np EU1²`,
and their sum is lambda. The argument permits either allocation endpoint.
The scalar root licenses give the common ceiling lambda<.35 and the
additional left ceiling lambda<.32. The selected composition needs only .35.

Seven rational three-point marginals independently test the entire
unsimplified gap budget. Each has at most one outer gap on either side,
so the bound is an equality in the coefficients of 1 and sqrt(10), which
the checker verifies. A tiny atom with U0=-.8 at p=.42 satisfies the actual
n=700 defect budget. It violates the proposed .6 amplitude if contact is
omitted. This is a counterexample to that omitted-premise strengthening,
not to the Berry–Esseen conjecture.

## Contact and the two infinite rays

The retained source is `manuscript/arxiv-v1/sections/04-fixed-entry.tex:70`
for closed-support contact and its exact Gaussian expression, and
`:98`–`:167` for the Gaussian expansion and derivative estimate. The general
all-threshold formulation is `07-fixed-confinement.tex:109`–`:183`.
It requires an attained fixed-target witness, nonnegative excess, the true
sharp predecessor `C_(n-1)<=CE`, and n>=42. It requires neither a probability
panel nor an incoming support strip. Thus its use here is not circular.

Dropping `-n a` requires a>=0. The rho replacement multiplies the positive
coefficient `3t²/2+e_n`. On the negative ray the directional beta price is
`-beta_lower`, and on the positive ray it is `beta_upper`. These are the
correct signs. The heat estimate retains `|t⁴-6t²+3|`; it does not assume
that Hermite polynomial positive at the new boundaries. Its four remainders
are uniform in H. The exact derivative estimate follows from a second-order
spatial Taylor bound for phi and the identity
`d_s[s phi(sy)]=-phi''(sy)`; it differentiates the Gaussian expression,
not the absolute-value majorant.

The review checks `c0=.4095<CE` directly via
`CE²=(19+6sqrt(10))/(72pi)` and pi<22/7. It also checks the n>=42 scaling
and e_n licenses. At the two boundaries `19461/10000` and `113273/50000`,
the upper heat/contact expressions are strictly negative. Independently
shifting Q and L to each boundary gives only negative coefficients, so
Q<0 and L<0 persist for every nonnegative ray displacement. This verifies
the entire unbounded ray, including its boundary, without a ray grid.
Since Q'<0, replacing CE by c0 in the derivative is also sign-correct.
Finally ell>1.996 and the strict acquired p interval give the stated
conditional support. No bound on H is required in this step.

## Exact composition and remaining conditional boundary

The two local theorems share literally the same probability interval,
amplitude, inward sum, n bound and raw threshold. Their intervals are
`0<lambda<=.01` and `.01<=lambda<=.35`, with the common endpoint included.
The small-noise anchor has phase `[-.3,.7]`, while the five-count proof uses
the floor. This causes no mismatch because both conclusions concern the
same actual signed excess. The first theorem holds for C>=0, so CE is
licensed; Schulz's strict binomial bound finishes that branch. At lambda=0,
`EU²=0` implies U=0 almost surely, and the binomial theorem is applied
directly rather than taking a limit of strict positive-noise estimates.

For the acquired law, `U=(X-m_B)/ell` gives
`1=v ell²+theta`, `s=theta/ell²`, `v+s=ell^-2` and
`X=(B+U-p)/sqrt(v+s)` exactly. Its raw threshold stays H, with count
threshold `np+H/ell`; no standardized argument is substituted for H.
The checker verifies these identities at all interface endpoints, and the
coarse ceiling `1.83605680<1.84` is strict.

Reflection uses the inequality, not an equality:

\[
P(-S\le-H)-\Phi(-H/\sqrt n)
=\Phi(H/\sqrt n)-P(S<H)
\ge\Phi(H/\sqrt n)-P(S\le H).
\]

The excess gap is the atom at H. An exact atom control rejects equality.
The signed D budget is not invariant under reflection; attainment and
coarse entry must be applied afresh to the selected orientation, as the
composition states.

With a genuine base through 41 and the retained implications at every least
failure, the first failure is confined to 42 through 699. This is a
conditional least-failure statement. An unresolved earlier failure prevents
using its conclusion as an unconditional later-index cutoff. A base through
699 or another proof of the remaining range is still required.

The permitted dependency removal is therefore confined to the **acquired
n>=700 route**: downstream probability panels, old numerical noise tables,
the separate left/right comparison union, Poisson-tail comparison and the
291-cell negative-inner certificate are absent from this join. The coarse
Fourier proof and its complete covers, contact, attainment, predecessor and
finite-base obligations remain. No existing object was deleted or weakened.
