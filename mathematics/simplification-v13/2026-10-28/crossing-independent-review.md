# Independent review of the all-count crossing identity

Reviewed source: `crossing.tex`, SHA-256
`b0f2e15ff41aaeb843b8b8e0619c89cdc15f07a427f71adba4ea7c151dfd0aec`.
The source belongs to the separate `simplification-v13` constructor worktree.
This review imports none of its checker or discovery code.

| Claim | Mathematical status | Execution status |
|---|---|---|
| Exact crossing, local-kernel and actual iid-mixture identities | Independently rederived; no blocker found | Fresh PASS, 366 actual-law/threshold cases |
| Nonnegative unweighted loss and the truncated-age reserve | Independently rederived under all stated support, centering and endpoint premises | Fresh exact controls, including equality and atom cases |
| Weighted binomial summation by parts and displayed Delta identity | Independently rederived; extra normalized-moment premises are now explicit | Fresh exact count-part reconstruction |
| Acquired-range applicability of the crossing theorem | Verified conditional on the retained acquisition bounds | Six exact rational range/reserve checks |
| Full comparison, positive defect-proportional reserve, or removal of count certificates | Not established by this result | Not claimed or tested as a theorem |

## Independent derivation

Write `D=1+U1`, `m=1-a1`, and `L_j(t)=E(t-T_j)_+`. The increment
`T_i-T_(i-1)=D_i-U0_i` is at least `1-a0-a1>0`. Thus the assumed
`n*a0<=t<n*m` gives one and only one closed-lower/strict-upper crossing
`T_K<=t<T_(K+1)`, with `0<=K<n`. In particular

`E K = sum_(i=1)^n P(T_i<=t)`.

For the leave-pair variable `R_i`, independence gives separately

`E(R_i-U0_i)_+ = L_(i-1)(t)`,
`E(R_i-D_i)_+ = L_i(t)`, and
`P(D_i<=R_i)=P(T_i<=t)`.

Therefore the kernel

`h(x)=E(x-U0)_+ - E(x-D)_+ - P(D<=x)`

satisfies `E h(R_i)=L_(i-1)-L_i-P(T_i<=t)`. Summation telescopes.
The endpoint conditions and centering give `L_0=t` and `L_n=0`, so the
sum is exactly `t-E K`. Every sum is finite; integrability suffices.

To check its sign without any stopping argument, split at `m`:

- If `x<m`, both D terms vanish. Thus `h(x)=E(x-U0)_+>=0`.
- If `x>=m>a0`, then `E(x-U0)_+=x`. Since `E D=1`, positive-part
  subtraction yields `h(x)=P(D>x)-E(D-x)_+`. The positive residual is
  bounded by `A1+a1` on its event, hence
  `h(x)>=(1-A1-a1)P(D>x)>=0`.

The second case includes `x=m`. The strict survival probability is essential
there: an atom at the lower endpoint of D is included in `P(D<=x)`.

Conditionally at crossing i, its age is `x-U0_i`. Below m, the kernel is
at least the expectation of `min(x-U0_i,b)` on `U0_i<=x` and the D crossing
is automatic. At or above m, every U0 crosses the lower boundary; its age
is at least `m-a0>=b`, and the preceding survival bound is at least b times
the crossing probability. Unique crossing and summation prove the stated
truncated-age reserve, with no strict or variance-proportional conclusion.

For comparison, the older conditional expression is exactly the same kernel:

`F0(x)[P(D>x)-E(D-x)_+] - E[U0 1_(U0<=x)]`.

Below m it becomes `x F0-M0`; above m the first support is already entirely
to the left and `F0=1,M0=0`. The checker independently evaluates both forms.

## Actual mixture and weighted identity

An actual iid sample from the mixture `(1-p)Law(U0)+p Law(1+U1)`, conditional
on j labels of the second type, has precisely the distribution of T_j.
The common monotone coupling only changes how these conditional sums are
placed together. Consequently

`P(sum Y_i<=t)=sum_j pi_j P(T_j<=t)=E F_B(K)`.

This is an identity for the common original marginal, not a relaxation of
its different conditional counts. No inference about a stopping-time
filtration is used.

Multiplying the exact local identity by pi_i yields

`P(sum Y_i<=t)=pi_0+pi_1*t + sum_(j=1)^(n-1)(pi_(j+1)-pi_j)L_j - sum_(i=1)^n pi_i g_i`.

For `k=floor(t)` and `u=t-k`, the same first three terms with `L_j` replaced
by `(t-j)_+` equal `F_B(k)+u*pi_(k+1)`. Since `E T_j=j`, Jensen proves
`B_j=L_j-(t-j)_+>=0`. This gives exactly the weighted formula in the source.
The unfavorable coefficients are precisely the positive differences of
consecutive binomial masses. The displayed Delta formula follows by
subtracting the two Gaussian terms and `C(rho-rho_B)`; no inequality is hidden
in that subtraction.

The main theorem only needs integrability. The normalized Delta additionally
needs `0<p<1` and finite third absolute noise moment. This was raised in review
and is explicit in the pinned source. Conditional centering then gives
`E Y=p`, `Var(Y)=p(1-p)+E U^2`, and the stated Bernoulli rho formula.

## Range and boundary audit

For the acquired right strip, `a1<=.072`, so the two candidate reserves are
at least `.328` and `.928`; `.328` is legal. For the left strip, `.232` is
legal by the same calculation with A1=.7 and inward sum .068.

For n>=42, `ns<=.616` gives
`1/4+s <= 1/4+.616/42 < .515^2`; multiplying by `1.84` gives displacement
strictly below `.948`. The inequalities
`(.25-.072)*42>.948` and `(.928-.53)*42>.948` verify both endpoint premises
uniformly thereafter. This mapping retains the acquisition's predecessor,
contact and support obligations; it does not establish acquisition itself.

The upper threshold is strict. For zero noise and t=n no crossing in
`{0,...,n-1}` exists. The lower threshold may be attained. For zero noise
and integer t<n, the crossing uses K=t and has zero age and zero gain.
The theorem correctly allows equality.

The selected-noise mean need not vanish. Direct path enumeration confirms
`E W_(K+1)=-sum_i E[U0_i 1_(T_(i-1)<=t)]>=0`, with strict positivity in
242 test cases. This is why an unqualified optional-stopping shortcut is
invalid even though the telescoping proof is valid.

## Reproduction and adversarial controls

Run from an integrated checkout containing the constructor source:

```sh
python3 -I -B mathematics/simplification-v13/2026-10-28/crossing-independent-run.py fresh-crossing-review
```

For a separate review worktree, append `--source /absolute/path/to/crossing.tex`.
`runs/finite-v13-20261028/crossing02` records the final independent replay.
The checker constructs conditional convolutions, full coupled paths, and the
actual iid mixture product distribution separately. It checks n=1,2,3,4,
all admissible conditional-sum atom thresholds and intermediate thresholds
for eight noise configurations: zero noise, both small symmetric groups,
both right-strip groups, either right group alone, both left-strip groups,
width equality with zero reserve, and a rare large negative U0 atom.
This gives 366 exact actual-law/threshold cases and 9,192 rational checks.

Six negative controls reject omitted width, omitted centering, omitted
selected-noise bias, replacement of the closed lower crossing by a strict
one, inclusion of the forbidden upper endpoint, and reversal of the curvature
coefficient. In particular, the source's actual width counterexample has
`U0=0`, `D=9/10,39/20` with masses `19/21,2/21`. At n=2, t=9/10,
`E K-t=1/210>0`; all other stated centering/separation/threshold conditions
hold, but `A1+a1=21/20>1`.

The checker uses Python integer/Fraction arithmetic and records versions,
return codes and source hashes. This supports the enumerated identities,
while the general proof above supplies their continuous-law scope.
No Poisson comparator, infinite-tail estimate, coefficient grid, or constructor
acceptance implementation is used by this review.

## Remaining obligation

The sign of `sum g_i` is not the sign of Delta. The weighted loss still has
to absorb the positive binomial curvature, the phase term and the normal and
third-moment repairs. There is no established defect-proportional lower bound
here, and zero-noise endpoint cases force non-strictness in the present theorem.
The retained regional comparison certificates therefore remain active.
