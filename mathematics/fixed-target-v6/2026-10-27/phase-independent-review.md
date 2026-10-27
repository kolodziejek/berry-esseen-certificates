# Independent review: retaining the full phase correction

Reviewed the new `phase.tex` in the separate `phase-resource-v6` worktree. Its exact source hash is recorded in `runs/fixed-target-v6-20261027/phase-review01/receipt.json`. The reviewer did not construct this phase argument. No shared source was edited.

**Verdict:** the analytic implication is sound under its stated global quadratic-envelope gate. The finite-endpoint positive-part simplification and the elementary global concavity test are valid. There is one minor wording issue and one integration condition to preserve; neither requires weakening the lemma. The numerical claim about all 24 original cells is not independently accepted by this review.

| Item | Mathematical status | Execution status |
|---|---|---|
| Exact phase-resource bound | Independently derived from conservation and nonnegative excess/leakage | No numerical premise needed |
| Floor/infinite-index endpoint lemma | Independently differentiated and proved via a positive integral | Analytic proof, not grid inference |
| Finite endpoint positive part | Independently proved, including negative envelope values | Exact negative control for omitting the positive part |
| Taylor polynomial and global concavity gate | Independently rederived | 3,321 bounded exact polynomial checks pass |
| Affine coefficient endpoint cover | Independently checked at the proof level | Actual scalar coefficient gates not rerun |
| All-24-cell improvement or full acquisition | Outside this review's acceptance scope | No native or first-cover replay |

## Independent derivation

Write `d*=n phi(0)D/6`, `e=exp(-h^2/(2n))` and

`U=(n+h^2)a+d*+n^(3/2)L`.

The retained conservation identity is

`R=U+(1-e)(n c rho-d*)`.

Because `d*<=U` and `1-e>=0`,

`R>=e U+n(1-e)c rho>=e U+n(1-e)b`.

Division by e>0 proves `U<=n b+exp(h^2/(2n))(R-n b)`. This step needs no sign for `c rho-phi(0)D/6`, no small-defect bound and no prior Gaussian-weight license. The stated premises `a,D,L>=0` and `0<b<=c rho` are sufficient. Both signs of the raw H enter through h=|H|.

For h>0 put `a0=h^2/2`, `x=1/n` and

`f(x)=r exp(a0 x)-b(exp(a0 x)-1)/x`.

The removable value is `f(0)=r-b a0`. Direct differentiation gives

`f'(x)=a0 exp(a0 x)[r-b a0 j(a0 x)]`,

`j(z)=(z-1+exp(-z))/z^2=integral_0^1 (1-s)exp(-zs) ds`.

The integral is strictly decreasing in z>=0, since its derivative is the integral of `-s(1-s)exp(-zs)`. Therefore the derivative sign changes at most once, from negative to positive. There is no interior maximum. The h=0 case is constant and has no division issue. This proves the two-endpoint bound for every real n>=N, and hence uniformly for integers and varying laws.

The stronger finite-endpoint statement is also correct. If `f(0)>0`, then `r>b a0` and `j<=1/2`, so `f'>0`; the finite endpoint dominates. If `f(0)<=0`, the maximum of the two endpoints is at most `max(0,f(1/N))`. Thus the infinite-index branch is unnecessary for an upper bound on U once the finite endpoint's positive part is kept. This does not assert monotonicity on negative-valued branches.

Now assume the **selected envelope itself** satisfies

`R<=r(h)=A+Fh-qh^2<=T<Nb` for all h>=0,

with F>=0 and q>0. At the finite endpoint the multiplier `r(h)-Nb` is negative. Multiplying `exp(z)>=1+z+z^2/2` by this negative quantity reverses the inequality and yields

`P_N(h)=r(h)+(r(h)-Nb)(h^2/(2N)+h^4/(8N^2))`.

The positive-part map is increasing, so `U<=max(0,P_N(h))`. No upper Taylor approximation to the exponential can be substituted here. The polynomial coefficients, in increasing powers of h, are

`A, F, -q+(A-Nb)/(2N), F/(2N), -q/(2N)+(A-Nb)/(8N^2), F/(8N^2), -q/(8N^2)`.

The final coefficient is negative. The nonnegative conserved raw quantity R also means that a physical witness cannot have r(h)<0; using a certified finite interval containing all h>=0 with r(h)>=0 is sound.

For concavity let `v=h^2/(2N)+h^4/(8N^2)` and `z=F^2/(8q^2N)`. Direct differentiation gives

`P_N''=-2q(1+v)+2(F-2qh)v'+(r-Nb)v''`.

For h>=F/(2q), all three terms are nonpositive and the first is negative. Below that point, `h^2/(2N)<=z` and the maximum of `h(F-2qh)` is `F^2/(8q)`. As `v'=h/N*(1+h^2/(2N))`, the middle term is at most `F^2(1+z)/(4qN)`. Dropping the other negative contributions gives

`P_N''<=-2q(1-z-z^2)<0`.

Thus the stated scalar gate proves strict concavity on the entire half-line, not just on the tested h interval. If F>0 there is a unique positive stationary maximum because `P_N'(0)=F` and its leading derivative term is negative. If F=0 the maximum is **attained at h=0**, with value A.

If A,F,q,b are affine in one formal coefficient, P_N(h) is affine in that coefficient for each fixed h. The supremum over a fixed common h domain is convex; its positive part is another maximum with zero and remains convex. Hence the two coefficient endpoints suffice. The global raw gate and concavity gate must be verified at their stated scope; affine-coefficient reasoning does not waive them.

## Findings and integration cautions

1. **Minor wording:** the inspected phrase “its unique maximum is either zero (when F=0)” should say “its maximum is attained at h=0 when F=0.” The maximum *value* can be A=1, for example. This was reported to the constructor.
2. **Preserve the envelope gate.** A prior raw bound obtained by taking the minimum of several enclosures proves `R<=T`; it need not prove that a newly selected quadratic r satisfies `r(h)<=T`. Before reversing the exponential estimate, check `sup_h r(h)<Nb` for that quadratic, or explicitly handle `min(r(h),T)` piecewise. A first-pass T computed as the maximum of that same quadratic is valid. This is not a defect in the written theorem, which states the stronger premise explicitly.
3. **The improvement is on U.** The polynomial maximum must not be fed back as a raw ceiling for R. A subsequent density license still uses a valid raw bound, unless a separate argument proves a new one.
4. **Concavity is not automatic from the raw gate.** The example `N=q=1,A=0,F=20,b=101` has `sup r=100<101`, but `P_N''(5)=663/4>0`. The new scalar concavity gate is sufficient and useful; it must not be silently dropped. Its failure alone does not imply nonconcavity for every other parameter set.

The root's proposed finite-endpoint positive-part simplification is accepted as an analytic consequence. It can reduce the maximization to one sixth-degree polynomial without an infinite-index branch. That computational simplification does not establish any Fourier primitive, moment acquisition or complete local comparison.

## Checks actually executed

The new `phase_review_check.py` imports only standard-library fractions and JSON. It imports no constructor or inherited backend. Across 3,321 rational parameter/threshold cases it verifies the exact polynomial expansion, second-derivative identity and the negative second derivative under the sufficient gate. It also verifies three negative controls: unguarded global concavity, calling the maximum value zero at F=0, and dropping the positive part of the finite endpoint.

For the last control, take `h=2,N=2,r=0,b=1` and write `y=exp(1/2)>1`. The expression at n=4 minus its n=2 value is exactly `2(y-1)^2>0`, although both values are negative. This is why a plain finite-endpoint monotonicity claim would be false.

The run passed with return code 0; the receipt records source hashes, command, Python version and elapsed time. These are bounded diagnostics. The continuum proof is the derivation above, and the actual 24-cell numerical maximum and any downstream initialization result require their separate evidence and review.
