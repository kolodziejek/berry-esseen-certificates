# Independent review of the 267 finite small-noise comparisons

Date: 2026-11-04. Reviewer: `/root/resume_finite`.

This review accepts the new joint-count moment argument and its finite numerical application at the scopes below. It does not establish acquisition, Fourier estimates, the finite binomial reserves, or the complete theorem by running a polynomial checker. Those remain explicit, previously established dependencies.

| Mathematical status | Execution status |
|---|---|
| Joint-count inequality independently derived; finite normalization, signs, domains, and application reviewed | Fresh exact acceptance and independent controls passed; actual return code 0 |
| Original acquired row interfaces and finite binomial reserves retained as dependencies | Native normalization gates freshly evaluated; selected original files byte-matched; no new acquisition, Fourier, or binomial probability campaign |

## Files and exact scope

The reviewed implementation is under `work/joint_count_20261104/construction/`:

| File | SHA-256 |
|---|---|
| `finite_native.py` | `eecdb515ea27ee352afcaf5e79acbf0c0f6ac0ca4ffe10e1d680c02639077557` |
| `finite_targets.py` | `32e33beed0a890dbba1818f6e9a1117cd768079ff24a5d48ec1d5d8bb9bdc417` |
| `accept_finite.py` | `666640187b85699283cc24652769dca353cd4519fea9e5bbbd3282605a39f268` |
| `finite_proof_objects.json` | `e9e792cc74107e865e521d27989e8e27e580894eb1f64850896c795ba21f2609` |
| `FINITE_NATIVE_SOURCES.json` | `59681199b6341107bf24b9be7c258e4ef96c1a23a1c45e52399f7019636b21fc` |
| `FINITE_INPUTS.json` | `c648ff9f317844c0eb2792cb8ef5781fc65bddcced1abd55659b62977650324d` |

| Family | Closed p cover | Actual integer indices | Rows | Score cap used by normalization | Conclusion |
|---|---|---|---:|---|---|
| positive39 | [151/500,229/500] | 39 | 78 | 2113/5000 | Positive allowance K/39, K=741/4000 |
| central40 | [190/500,238/500] | 40–42 | 48 | 4247/10000 | Original sharp local comparison |
| left40_42 | [141/500,190/500] | 40–42 | 49 | 4247/10000 | Comparison using the original finite-binomial reserve |
| left42_48 | [145/500,190/500] | 42–48 | 45 | 2113/5000 | Original sharp local comparison |
| central42_48 | [190/500,237/500] | 42–48 | 47 | No cap needed by this positive-raw repair | Original sharp local comparison |

Each cover consists of consecutive closed intervals of width 1/500. Each actual noise domain is `0 < lambda <= min(1/20, row Lambda)` and each phase domain is the full closed interval `[-1/2,1/2]`. Both signed third-moment bounds are retained. The premises still require score at least 2/5, the actual common conditional laws, their centering and acquired support/moment interfaces. These numerical rows do not themselves prove those analytic premises.

The normalization uses amplitude 11/25 for positive39 (conservative relative to its acquired 43/100), 43/100 for central40, the maximum of 87/200 and the original row amplitude for left40_42, and 17/40 for finite42–48. The exact original target and allowance fields are retained.

## Independent analytic checks

The coupled-array derivation was obtained before reading the constructor's argument; see `INDEPENDENT_DERIVATION.md`. With coupled count increments at least c>1/2, the exact cutoff payoff satisfies

\[
G(R)\le-\mathbf1_{\{W_k>u\}}+R_0\lfloor(u-W_k)/c\rfloor_+.
\]

The outgoing event is strict; the incoming staircase includes endpoint collisions. For |u|<=c and u<c, the staircase is bounded by `W_k^4/(c-u)^4`. This follows for each integer r>=1 from

\[
(cr-u)^2-r(c-u)^2=(r-1)(c^2r-u^2)\ge0,
\]

and then squaring the nonnegative bound. Thus all incoming counts can be bounded using the same own-count variable W_k; no equality of neighboring-count laws is assumed. Its shifted fourth-moment outgoing minorant, the bounds `|E W_k^3| <= A t`, `E W_k^4 <= A^2 t+3t^2`, and the one-sided normal increments give the four fixed near/far, positive/negative phase targets. Closed rectangle maps cover every phase and every positive noise level, including arbitrarily small positive noise. The artificial t=0 polynomial boundary is used only after clearing denominators, not by dividing by zero.

### Negative eta and the finite score gate

The polynomial conclusion is `E G-f <= -eta t`, also when eta is negative. With

\[
m\le b=\sqrt n\pi_k\le1,
\qquad \omega_-\lambda\le t\le\omega_+\lambda,
\]

the valid lower bound for `b eta t/lambda` is

\[
J_\eta=\min\{m\eta\omega_-,\eta\omega_+\}.
\]

For negative eta the second endpoint is needed. Independent minimization over all four rectangle corners agrees with this formula in every row. The normalization yields

\[
\rho_B(C-C_B)\le\lambda(\kappa/n-J_\eta).
\]

The final acceptor explicitly requires nonnegative repair kappa, `0<m<=1`, and `0<omega_-<=omega_+`. Consequently `kappa/n<=kappa/N` for the declared actual indices. It also rejects optimized Python. These are analytic sign requirements, not optional numerical conveniences.

The native gate `1-zeta/N>0` together with `v(1-zeta/N)^2>(2/5)^2` verifies the existing mass upper-bound argument `b<=1`. Every signed-cubic repair retains its score cap and the minimum of the lower- and upper-multiplier products. Thus a negative raw cubic coefficient uses the upper multiplier, rather than silently multiplying it by the lower bound. The selected native source variants and their positive denominator/mass/variance guards were read, including the piecewise finite42 normalizer.

Writing `reserve=J_eta-kappa/N`, the three applications are:

* The sharp rows require `reserve-1/1000>0`, giving the unchanged strict local margin.
* Positive39 requires `reserve+K/(39 max(1/20,Lambda))>0`. Multiplication by the actual positive lambda gives a bound strictly below K/39. Since rho_B>=1, this proves `C<C_B+K/39`. It does not use a sharp39 theorem.
* The left40–42 rows require `reserve+epsilon rhoB_lower/U>0`, where `U=min(1/20,Lambda)` and epsilon is the minimum of the unchanged binomial reserves for actual n=40,41,42 on this same p interval. When reserve<0, lambda<=U and rho_B>=rhoB_lower imply `C-C_B<epsilon`; when reserve>=0 the comparison is immediate. The lower bound for rho_B is independently checked using the exact square inequality at the upper endpoint of v=p(1-p).

The finite-binomial reserve is an inherited numerical theorem. This review checks its original file bytes, integer/index/p matching, and the minimum used in the gate; it does not recompute or independently prove those binomial probabilities.

### Polynomial target changes

The parameterized finite targets retain a=299/625, `K0=(9/4)/(4641/10000)`, negative near-phase cutoff 5/3, and positive cutoff 6/5. Relative to the reviewed eta=1/10 target, they add `(1/10-eta)` times the corresponding cleared-denominator factor:

* near phases: `(c-u)^4`;
* far positive: `t(c-u)^4`;
* far negative: `t(t+r^2)(c+r)^4`.

These signs agree with subtracting eta t from the moment loss. All denominators used for the positive-noise argument are positive. Nonnegative exact Bernstein coefficients establish the target on the entire closed rectangle; the final strict scalar gate supplies the strict comparison. The finite row eta census is 244 at 1/10, 12 at zero, and 11 at -1/20. The 23 nonpositive rows are all left40–42 rows and retain their original binomial reserve.

## Fresh execution and adversarial controls

Independent driver: `work/joint_count_20261104/audit/check_finite.py`.

Actual capture: `runs/joint_count_20261104/audit_finite01/RESULT.json`, `stdout.txt`, and `stderr.txt`. The result records the exact command, runtime path, return code, elapsed time, and all source/input hashes before and after execution. Actual return code: 0; elapsed time: 5.832228792016394 seconds; all inputs unchanged; stderr empty.

The fresh run checked:

* 267 complete actual-domain row joins and all 18 native source files against their cited original paths, byte for byte;
* 17,115 regenerated native normalization gates and 65,148 exact inverse-Bernstein coefficients;
* 12,816 direct exact formula comparisons, covering every row, every phase family, eta signs, phase endpoints, an arbitrarily small rational positive noise point, interior points, and the cleared t=0 boundary;
* exact agreement with the final constructor acceptance output, after separately checking its proof-object hash;
* all allowance and signed-product formulas above, independently computed from the row values.

The direct formula comparisons are bounded adversarial checks of the separately derived formulas; they are not a substitute for polynomial identity or continuum positivity. The acceptor's exact inverse-Bernstein reconstruction and the reviewed derivation are the corresponding proof obligations.

Eleven negative controls rejected: missing row, reordered families, Boolean index, changed original score target, missing phase branch, negative coefficient, changed eta with old coefficients, negative eta relabelled zero, negative repair, mass above one, and nonpositive variance lower bound.

An exact counterexample to the incorrect negative-eta endpoint rule is recorded: at eta=-1/20 the declared interval minimum is `-6859/125000`, whereas using the lower endpoints gives `-419165787/12500000000`. This refutes that interval multiplication rule; no iid realization of that extremal endpoint pair is asserted.

The earlier direct finite-law/path controls are separately preserved in `runs/joint_count_20261104/audit_paths01/` and described in `REVIEW.md`; they exercise skew and symmetric Bernoulli cases, tiny atoms/noise, both signs, and exact collisions. No expensive native integration was repeated for this audit.

## Manuscript correspondence and one correction

Reviewed manuscript: `work/manuscript_revision_20261029/manuscript/journal-v20/sections/local.tex`, SHA-256 `5f4e691861900f30a8b0946ea82ff322d63f81860bead3b59fa68f70501511d0` at the final text readback.

The new joint-count moment lemma, four-region polynomial rule, signed reserve formula, uniform application, and finite positive-allowance application were read. Strict outgoing events, closed incoming collisions, the same conditional laws, the complete phase cover, and the signed finite reserve are retained. The whole-count LOW and intermediate-noise arguments remain distinct dependencies.

One concrete text mismatch was detected and corrected by the manuscript owner: positive39 normalizes the polynomial rectangle at U=1/20 even on the 18 rows whose actual Lambda is smaller. The final text now states `T=omega_+ U`, with U=1/20 for positive39 and `U=min(1/20,Lambda)` otherwise, while the actual noise always obeys `lambda<=min(1/20,Lambda)`. This matches the accepted coefficients without changing them or enlarging the claimed actual noise domain.

No further defect was found in this bounded review. This finding licenses replacement of the old finite small-noise argument at the exact inherited scopes; it is not a separate all-index proof and does not claim that the manuscript became shorter.
