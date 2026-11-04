# Independent joint-count derivation

This derivation was written before reading the new analytic proof or constructor's polynomial implementation. The existing v19 Sections 7.5–7.7 and the previous structural pilot were read. The selected-row metadata and proposed constants were then supplied by the constructor. Mathematical status: the implications below are locally derived under their stated hypotheses. Execution status: separate finite controls support the derivation; they do not replace its universal argument or accept a full numerical cover.

## Information that must survive

One actual iid marginal supplies two centered conditional laws `U0,U1`. All counts must use these same laws. Conditional noises need not have equal distributions or variances. Independently couple the entire arrays and set `W_j=sum_(i<=j)U1_i+sum_(i>j)U0_i`. The inward bound `U0<=a0`, `U1>=-a1` gives count increments at least `c=1-a0-a1>0`. Exterior extension is constant for `W_j`, so the count-plus-noise increases by one there. An independent binomial selector recovers the actual iid sum law.

The closed CDF forces strict outgoing events. In particular `R<=-1` is equivalent to `W_k>u`, not `W_k>=u`. The phase, count, mass ratio, normal correction, third absolute moment and all conditional moments must refer to this same law. An input giving only unrelated countwise moment bounds cannot assert this coupling. The final bound must be proportional to positive noise uniformly down to zero; zero noise itself remains a Bernoulli case.

## A majorant depending on the one own-count variable

Write `G(r)=(F_B(k+r)-F_B(k))/pi_k`, where the binomial CDF is extended by zero and one. Suppose every legal incoming ratio is at most `R0`. For the monotone cutoff `R`,

`G(R) <= -1{W_k>u} + R0 floor((u-W_k)/c)_+`.                 (1)

For `R<0`, the exact increment is at most `-1`. For `R>=1`, the telescoped increments imply `W_k<=u-cR`, hence `R<=floor((u-W_k)/c)`. The binomial increment has at most `R` positive masses, each at most `R0*pi_k`; this stays valid when the cutoff exceeds the legal range. If `R=0`, both the exact increment and the outgoing indicator vanish, and the remaining right side is nonnegative. These three cases prove (1), including threshold collisions. The floor's positive part is taken after flooring; at a positive integer boundary the incoming count is included.

Assume now `u<c` and `|u|<=c`. If `r=floor((u-w)/c)_+>=1`, then `w<=u-cr<0`, and

`(cr-u)^2-r(c-u)^2=(r-1)(c^2 r-u^2)>=0`.

Consequently, for every real `w`,

`floor((u-w)/c)_+ <= w^2/(c-u)^2`,

`floor((u-w)/c)_+ <= w^4/(c-u)^4`.                          (2)

The fourth-power bound follows by squaring the first lower bound on `w^2`, then using `r^2>=r`. Both polynomial majorants vanish at `w=0`. In the manuscript's actual phase domain `|u|<=1/2<c`, all denominators and both guards hold. The guard `|u|<=c` cannot be silently removed from this proof. In contrast, the shifted bound `((u-w)_+/c)^4` is also valid but loses a zero constant after replacing its expectation by the full shifted fourth moment when the phase is fixed.

## Expectation and four useful branches

Let `W=W_k` be a sum of independent centered variables with `|U_j|<=A`, and let `t=E W^2`. Direct expansion gives

`|E W^3|<=A t`,

`E W^4=sum E Z_i^4+6 sum_(i<j) Var(Z_i)Var(Z_j)<=A^2 t+3t^2`.

For any `a>0`, choose `K0>=(9+6 sqrt(3))/4` and let

`h_a(z)=(-z^4+3a^2 z^2+2a^3 z)/(K0 a^4)`.

Factoring its numerator as `-z(z-2a)(z+a)^2` proves nonpositivity for `z<=0`; its positive maximum is at `z/a=(1+sqrt(3))/2` and is at most one. Thus `h_a(W-u)<=1{W>u}`, with equality zero at the threshold. Combining (1) with the fourth majorant in (2) gives a single expectation inequality, rather than unrelated estimates for neighboring counts:

`E G(R) <= E[-h_a(W-u)+R0 W^4/(c-u)^4]`.                   (3)

Suppose `lf<=f'<=hf`, `f(0)=0`. For `r>=0`, define

`P(t,r)=(3a^2-A^2)t-3t^2-4Art-6r^2t-r^4+3a^2r^2`.

The loss `f(u)-E G(R)` is at least each applicable expression:

- Negative near phase `u=-r`: `(P(t,r)+2a^3 r)/(K0a^4)-hf r-R0 t(A^2+3t)/(c+r)^4`.
- Positive near phase `u=r`: `(P(t,r)-2a^3 r)/(K0a^4)+lf r-R0 t(A^2+3t)/(c-r)^4`.
- Negative far phase `u=-r`, `r>0`: `r^2/(t+r^2)-hf r-R0 t(A^2+3t)/(c+r)^4`.
- Positive far phase `u=r`: `lf r-R0 t(A^2+3t)/(c-r)^4`.

The negative far branch uses Cantelli on the **closed** event `W<=-r`; its complement is the required strict outgoing event. The positive far branch discards a nonnegative outgoing probability. The combined fourth moment in (3) has one negative coefficient in the loss, `-1/(K0a^4)-R0/(c-u)^4`, so bounding it once by the upper fourth moment yields exactly the displayed near formulas. No independent choice of incompatible fourth moments and no duplicate resource subtraction is made. The third moment coefficient has sign determined by the phase; its lower contribution is `-4Art/(K0a^4)`.

Set `r=z t` in the near branches. Dividing by `t>0` gives rational functions extending continuously to `t=0`. On the far wedges, write `r=z0 t+(1/2-z0 t)v`, `0<=v<=1`, provided `z0 t<=1/2`. At the single limiting corner `t=r=0`, the negative-far quotient must be cancelled algebraically or controlled by a valid polynomial extension: an unqualified division by `t+r^2` there is invalid. A cleared polynomial numerator may vanish at that corner; strict loss at every positive `t` does not require strict positivity at the artificial zero-noise corner.

If the four closed-domain proofs show loss `>eta*t` for positive `t`, and `t>=omega_lo*lambda`, `sqrt(n)*pi_k>=m`, and the existing signed repair gives `Rcal<=kappa*lambda/n`, then for `kappa>=0`, `n>=N`,

`rho_B(C-C_B)<-(m eta omega_lo-kappa/N)lambda`.              (4)

In fact the constructor needs only loss `>=eta*t`: then (4) is non-strict, and a strictly positive excess of `m eta omega_lo-kappa/N` over the requested `1/1000` supplies the final strict comparison. Thus nonnegative Bernstein coefficients, including zeros at the artificial zero-noise corner, are sufficient. No strictness may be inferred solely from a nonnegative coefficient array.

For negative `kappa` a different endpoint rule is needed; one may safely replace `kappa/n` by zero. The constructor's supplied `kappa` is positive. No normal-discrepancy or acquisition input is generated by the polynomial proof itself.

## Optional quadratic improvement, not needed by the selected proposal

If additionally `t<=c^2-u^2`, choose `a=t/(c-u)`. The same square calculation with phase `u-a` proves

`floor((u-w)/c)_+ <= (w-a)^2/(c-u+a)^2`.

Centering then gives the expectation bound `t/(t+(c-u)^2)`. This is an optional stronger quadratic estimate; it is not assumed by the proposed four-family fourth-moment proof.

## What this can replace, and what it cannot

If the four exact polynomial families pass on the whole claimed domain, this argument can replace the tiny-noise incoming Bennett/Poisson estimates and their relative-tail monotonicity argument on precisely that domain. It uses only one count's centered third/fourth moment bounds after the monotone coupling is proved. It does not remove acquisition, the inward support gap, finite mass/phase/repair normalization, the `C>=.4` premise, or the separate zero-noise case. A tiny-noise success alone does not replace the larger-noise whole-count crossing/fractional-part proof. The previous below-.4 structural examples do not obstruct this upper bound.
