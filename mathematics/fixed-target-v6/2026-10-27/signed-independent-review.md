# Independent review of signed K1 and the quarter constant

**Recommendation:** accept the two moment inequalities and their fixed 24-cell
coefficient table for integration, with the existing support and gap/Fourier
premises kept explicit. I found no blocking defect. This review does not accept
a combined raw/resource acquisition, `D<4`, a local exclusion, or any certificate
removal.

Reviewed constructor commit:
`c159b80fc0f781b5452c46b8ff22ba29e73818c5` in the separate
`signed-response-v6` worktree. I did not author its signed-coefficient proof or
checker. I did author the earlier v5 raw cover and the v6 circle-feedback
component; this report does not describe their reinspection as independent
review. I independently derived the new signed inequalities and wrote a separate
small table check which imports no constructor or Fourier code.

| Item | Mathematical status | Execution status |
|---|---|---|
| Signed Cauchy enclosure for K1, both reflections | Independently derived and checked under one centered, variance-one, bounded-support marginal | Direct exact controls on six laws |
| Strong closed-cell cap and its three monotonicity gates | Independently checked over the complete continuous domain | Fresh exact verification of all 24 rows, with a Bernstein derivative check |
| Quarter constant from the nonnegative fifth-moment square | Independently derived; actual same-law identity | Fresh reconstruction of all 24 new constants, conditional on the retained Gamma charge |
| Complete raw/resource bound or global theorem | Outside this review | No constructor checker, Fourier integral, dense stage or native acceptor executed |

## 1. Sign Cauchy and reflection

The definitions at `signed-proof/signed.tex:3–18` are consistent with the
raw coefficient in `manuscript/arxiv-v1/appendices/fourier-analysis.tex:1940–1943`
and `2022–2027`:

\[
 K_1=c_+-c_--3\beta-\tfrac32\rho\gamma,
 \quad a_\pm=(1\pm\beta)/2,
 \quad b_\pm=(\rho\pm\gamma)/2.
\]

For a centered nondegenerate law both sign second moments are positive.
Cauchy gives `a_-^2<=m*b_-` and `b_-^2<=a_-*c_-`; the support bound gives
`c_+<=R*b_+`. With `h=1-beta=2a_->0`, `delta=rho-gamma=2b_-`, and
`m<=1/2`, these imply

\[
 \delta\ge h^2,\qquad c_-\ge\delta^2/(2h),\qquad
 c_+\le R(\rho+\gamma)/2.
\]

Substitution, with no independent choice of moments from different laws, yields

\[
 K_1\le R\rho-\tfrac32\rho^2-3+3h
 +(\tfrac32\rho-R/2)\delta-\delta^2/(2h).
\]

This matches the displayed formula at `signed.tex:24–50`. Under `X->-X`,
`beta,gamma,c_+-c_-` change sign, `rho,R` do not, and therefore `K1` changes
sign. Applying exactly the same proof bounds `-K1` with `h=1+beta` and
`delta=rho+gamma`. A zero atom contributes nothing to any of these moments;
no strict nonzero-support or central-gap condition was introduced. The divisor
`h` is positive for an actual centered variance-one law.

The source beta cap at `signed.tex:52–63` is also in the correct direction.
The function `(1+b^2)/sqrt(1-b^2)` strictly increases for `b∈[0,1)`. Thus
its value at the proposed cap being at least `u` bounds every actual `|beta|`
when `rho<=u`. The polynomial gate tested in the code is equivalent because
both sides and the denominator are nonnegative.

## 2. Continuous maximization, including failed gates

Write `a(r)=3r/2-R/2`, `C(r)=Rr-3r^2/2-3`. For fixed positive `h`, the
concave delta quadratic has vertex `delta=a*h`. On the constrained interval
`delta>=h^2`, the exact maximum is

\[
 \psi_a(h)=\begin{cases}
 h(3+a^2/2),&0<h\le a,\\
 3h+ah^2-h^3/2,&h\ge a.
 \end{cases}
\]

The first branch is empty when `a<=0`. The formulas and their derivatives
agree at `h=a` when it is positive. The derivative of the second branch is
`3+2a*h-3h^2/2`, a concave quadratic. The minimum-endpoint argument in
`signed.tex:98–119` is valid on the entire interval `[0,h_*]`, including when
it crosses the branch boundary: the derivative is at least the analogous
quadratic at `a(l)`, whose endpoints are nonnegative by gate 2. Gate 1 places
`h_*` in the second branch for every rho in the cell. Finally the derivative
in rho at fixed `h_*` is `R-3rho+3h_*^2/2`, bounded below by gate 3.
No interior h or rho maximum is omitted.

My independent arithmetic check additionally writes the h-derivative in the
quadratic Bernstein basis on `[0,h_*]`, with coefficients

\[
 3,\qquad 3+a(l)h_*,\qquad 3+2a(l)h_*-\tfrac32h_*^2.
\]

All three are nonnegative in each row where the strong theorem is used.
This gives a separate finite positivity certificate for the continuous
derivative, rather than sampling it.

Where these gates fail, the unconstrained delta maximum remains valid and is
quadratic in rho. I independently checked its two endpoints and, for a concave
quadratic, its interior vertex when present. The table uses the strong bound
exactly on rows `0,10,...,23`; rows `1,...,9` retain the valid fallback. The
code never extrapolates the stronger formula through a failed gate. Every
reported lower/upper rho endpoint matches the fixed 24-cell partition of
`[1,7361/4000]`, in order and with shared closed boundaries.

The last exact new cap is

\[
 991066736835152656509887/250000000000000000000000
 <3.964267<3.97.
\]

The last five safe decimal caps are `3.558417, 3.661560, 3.763656, 3.864593,
3.964267`. These concern all laws in their cells under the support assumption,
not only contact optimizers or laws satisfying a small-defect premise.

## 3. Quarter constant and exact consumer

The identity at `signed.tex:139–155` follows by direct expansion:

\[
 \mathbb E[|X|^3(|X|-\rho)^2]
 =M_5-2\rho M_4+\rho^3\ge0.
\]

Thus `rho*M4/2-M5/4<=rho^3/4`. Finite fifth moment follows from the already
assumed bounded support. The standardized three-point law on `{-rho,0,rho}`
with nonzero masses `1/(2rho^2)` gives equality, so zero atoms must remain
admissible. The inequality itself is an existing ingredient, not newly claimed.

Crucially, this is the precise combination in
`Kq=M5/4-rho*M4/2-3beta*gamma/2+rho/2`, at
`fourier-analysis.tex:2099–2108`. Therefore its replacement in the unsigned
constant leaves `3beta*gamma/2-rho/2` untouched. The gap charge also remains
unchanged. Since `8/27-1/4=5/108`, subtracting `5u^3/108` from the old first
branch is exactly the valid substitution after taking the cell upper rho
endpoint. The second branch is independently retained. I reconstructed all
24 new A values from this quarter formula; I did not merely check that they
are smaller than the old values.

The last new A is
`1380955788771400317346292272927/132701452507702886400000000000`, approximately
`10.4064858573514`, with safe upper decimal `10.406486`. Its gap coefficient
Gamma is still a retained analytic input, as the constructor states at
`signed-check.py:132–139`. This review does not promote its hash into a proof
of that gap estimate.

## 4. Code, controls and evidence

I read the entire final `signed-check.py` and `signed.tex`. The fixed table
checker reconstructs its moment caps, gates, endpoints and coefficient
formulas; it reads the old pinned output only for explicitly retained data.
No archived numerical module is imported. The final helper also checks actual
support before evaluating its literal laws (`signed-check.py:85–99`).
That support guard was added during review; the prior four controls already
satisfied the support bound, so its addition changes no coefficient row.
I independently confirmed exact parsed equality of all 24 `signed01` and
`signed02` row objects.

My own check reads pinned source bytes and the fixed table, but never imports
or executes the constructor. It freshly validates all 24 new signed caps and
quarter constants, six actual-law controls (including an additional four-point
law and a tiny-far-atom law using its own radius 20), and six table mutations.
Missing, reordered and duplicated cells, an understated final cap, a forced
failed monotonicity gate, and an invalid beta cap are rejected. The far-atom
case tests only the universal moment inequality; it is not admitted to the
radius-3.84 acquisition table. The constructor's explicit opposite-sign
moment counterexample also passes direct verification and excludes the
unjustified shortcuts `beta*gamma>=0` and `K1*gamma<=0`.

Final source pins:

- `signed-proof/signed.tex`: `43dc933883f313b26a6b4a0a99b57369f98a3ec2093707818e63dda5a1f9ef56`.
- `signed-check.py`: `c827917d18b241d7e6255b3c15184ca719044cc3b7ffb8c7474ea5482dd7a847`.
- Constructor `signed02/stdout.json`: `3376557f83874f571ed1c7cfad10b82930e736427ba597b5c8ed76b3c46b1944`.
- Retained v5 row source: `7525713bd06a30b9c13693d01949d4f186890128eed3432771953ef9eafef082`.

Command actually run from this review worktree:

```sh
python3 mathematics/fixed-target-v6/2026-10-27/signed_review_check.py ../signed-response-v6
```

The first attempt, `signed-review01`, rejected the source hash because the
constructor added its support guard concurrently. Its failed stdout/stderr,
receipt and reviewer-code snapshot are preserved. After reading that change
and updating the pins, `signed-review02` returned zero. Python was 3.9.6 without
optimization. Exact review output, stderr, versions, timestamps, code/output
hashes and the table-equality record are preserved in that run directory.

This is an independent review of the new signed coefficients, not a rerun of
all v5/v6 analytic dependencies. Integration must still keep the actual support,
fixed-target transfer, full Fourier remainder and correct raw/resource order.
Those coefficient improvements alone do not certify any final initial resource
budget or permit removing existing certificates.
