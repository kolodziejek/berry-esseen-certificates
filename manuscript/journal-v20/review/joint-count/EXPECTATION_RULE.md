# A common expectation rule from inward spacing

Status: locally derived theorem below. No assertion yet that its numerical gates cover every manuscript cell. The constructor is testing actual acquired central and left rows independently. The proposed change concerns probability comparison, not attainment or acquisition.

## 1. The coupled process and a deterministic enclosure

Let the actual iid marginal be `Y=B+U`, with `P(B=1)=p`, `E(U|B)=0`. Its actual conditional laws `U_0,U_1` are bounded by `A` in absolute value and satisfy `U_0<=a0`, `U_1>=-a1`, where `a0,a1>=0`, `a0+a1<=d0`, and `c=1-d0>1/2`.

Take all `2n` copies `U_{0,i},U_{1,i}` independently and define

\[
 W_j=\sum_{i\le j}U_{1,i}+\sum_{i>j}U_{0,i},\qquad 0\le j\le n.
\]

Extend constantly outside `[0,n]`. For a legal count `1<=k<=n-1` and `|u|<=1/2`, define `R=max{j:j+W_j<=k+u}-k`. Each increment of `j+W_j` is at least `c`. At the selected count, write `W=W_k`, `t=E W^2`.

The following deterministic enclosure uses the actual joint process:

\[
 \begin{cases}
 0\le R\le\lfloor(u-W)/c\rfloor,&W\le u,\\
 -\lceil(W-u)/c\rceil\le R\le-1,&W>u.
 \end{cases} \tag{1}
\]

Proof: `W<=u` means count `k` is in the closed event, so `R>=0`; reaching `k+R` consumes at least `cR` of the available distance `u-W`. If `W>u`, count `k` is outside, so `R=-h<=-1`. Count `k-h+1` is also outside, while its distance from count `k` is at least `c(h-1)`. Hence `W-u>c(h-1)`, or `h<=ceil((W-u)/c)`. This proof keeps the strict inequality on the outgoing side even when there are atoms.

For every real function `g` on the integers, any polynomial `P` satisfying

\[
 \begin{split}
 P(w)&\ge\max_{0\le r\le\lfloor(u-w)/c\rfloor}g(r),&&w\le u,\\
 P(w)&\ge\max_{-\lceil(w-u)/c\rceil\le r\le-1}g(r),&&w>u
 \end{split} \tag{2}
\]

therefore gives

\[
 E g(R)\le E P(W). \tag{3}
\]

All variables are bounded, so these expectations exist whenever `g` is finite on the possible cutoffs. Only the actual law of `W_k` is used in the last expectation; (1) is a domination statement about the entire coupled process, not an identification of that process from `W_k`.

## 2. A finite polynomial certificate interface for the binomial payoff

Write `pi_j` for the `Bin(n,p)` mass, `F_B` for its CDF, and

\[
 G(r)=\{F_B(k+r)-F_B(k)\}/\pi_k.
\]

Conditioning on an independent binomial selector gives the exact identity

\[
 P(\textstyle\sum Y_i\le k+u)-F_B(k)=\pi_k E G(R).
\]

Suppose `pi_(k+i)/pi_k<=R0` for every legal incoming count. Since `G` is increasing, `G(r)<=-1` for `r<=-1`, and `G(r)<=R0*r` for `r>=0`, (1) proves the pathwise inequality

\[
 G(R)\le -\mathbf1_{\{W>u\}}+
 R_0\left\lfloor\frac{u-W}{c}\right\rfloor_+. \tag{4}
\]

A polynomial `P(s)` majorizing the right side with `s=W-u` can be accepted on a finite set of real intervals. Choose a positive integer `M` and verify:

* `P(s)>=-1` for every `s>=0`, and `P(0)>=0`;
* `P(-cx)>=R0*m` on each closed interval `[m,m+1]`, `m=0,...,M-1`;
* `P(-cx)>=R0*x` for every `x>=M`.

These conditions imply the majorant on the whole real line. At an integer `x=m`, the interval beginning at `m` supplies the larger staircase value; at the last boundary the ray condition does. Thus no jump endpoint is omitted. Interval inequalities can be checked by rational Bernstein coefficients; ray inequalities can be checked by nonnegative coefficients after translation, or by a reciprocal transform to a compact interval. These are sufficient certificate formats, not assertions that every valid polynomial has such a certificate.

For `P(s)=sum b_j s^j`, its expectation is computed from one common conditional law:

\[
 E P(W-u)=\sum_j b_j\sum_{h=0}^j\binom jh(-u)^{j-h} E W^h. \tag{5}
\]

The moments of `W` are the coefficients, through the required finite degree, of

\[
 \left(\sum_{h\ge0}\frac{E U_1^h}{h!}z^h\right)^k
 \left(\sum_{h\ge0}\frac{E U_0^h}{h!}z^h\right)^{n-k}.
 \tag{6}
\]

Multiplying independent exponential-generating polynomials proves (6); it does not select independent moment optimizers at different counts. The source moments must come from the same marginal, or from a rigorously proved simultaneous feasible region containing it. Bounds with signed coefficients must use the corresponding direction of the moment bound.

## 3. A global quartic guard for the entire incoming count

For every integer `i>=1`, the function `i/(ci-u)^4` decreases as a function of real `i>=1`, because its derivative has the sign of `-3ci-u<0`. Its denominator is positive since `|u|<=1/2<c`. If `R=i>=1`, then `W<=u-ci<0`. Consequently

\[
 R_+\le\frac{W^4}{(c-u)^4}\qquad\text{on every path}. \tag{7}
\]

Thus any global polynomial minorant `h(s)<=1_{s>0}` gives the **single polynomial witness**

\[
 E G(R)\le -E h(W-u)+\frac{R_0 E W^4}{(c-u)^4}. \tag{8}
\]

This replaces the entire incoming conditional-count tail sum by one fourth moment. No Bennett or Poisson comparison, infinite-series remainder, incoming variance inflation, or relative-tail monotonicity is used. It is not assumed that `W_(k+i)` has the same law as `W_k`.

There is also a useful shifted version. For real `x>=0`, `floor(x)<=x^4` when `x>=1`, and `floor(x)=0` on `[0,1)`. Hence

\[
 E G(R)\le-Eh(W-u)+R_0E(W-u)^4/c^4. \tag{9}
\]

Either (8) or (9) may be selected by an exact certificate. They use the same process and moments. The unshifted version has no constant incoming charge when `t=0`.

## 4. Three explicit witnesses and one expectation formula

Let `a>0`, `K>=(9+6sqrt(3))/4`, and define

\[
 h_a(s)=\frac{-s^4+3a^2s^2+2a^3s}{Ka^4}.
\]

The factorization of the numerator as `s(2a-s)(s+a)^2` proves `h_a<=0` on `s<=0`. On the positive half-line, its derivative is `-2(s+a)(2s^2-2as-a^2)`; the positive maximum is attained at `s=a(1+sqrt(3))/2` and equals `(9+6sqrt(3))a^4/4`. Therefore `h_a(s)<=1_{s>0}` globally, including `s=0`.

Independence and centering give

\[
 |EW^3|\le At,\qquad EW^4\le A^2t+3t^2. \tag{10}
\]

Indeed `EW^3` is the sum of the third moments and each has absolute value at most `A` times its variance. The fourth moment is the sum of individual fourth moments plus six times the pairwise variance products; each individual fourth moment is at most `A^2` times its variance. Dropping the nonnegative diagonal correction gives (10). Zero conditional variances are allowed.

Suppose `f(0)=0` and `l_f<=f'(u)<=h_f` on the phase range, with both constants positive. Define `L_f(u)=l_f*u` for `u>=0`, and `L_f(u)=h_f*u` for `u<=0`; integration proves `f(u)>=L_f(u)` on either side. Equations (8) and (10) imply

\[
\begin{split}
 EG(R)-f(u)\le \mathcal B_4(t,u):={}&
 \frac{(A^2+4A|u|+6u^2-3a^2)t+3t^2
       +u^4-3a^2u^2+2a^3u}{Ka^4}\\
 &+\frac{R_0t(A^2+3t)}{(c-u)^4}-L_f(u).
\end{split} \tag{11}
\]

This is a direct expectation of one polynomial; its favorable second moment and unfavorable fourth moment are not separate tail estimates. If actual signed third moments or a stronger fourth moment are known, use them in (8) before taking (10).

Two further members of the same polynomial-witness family are useful away from zero phase:

* For `u=-r<0`, the quadratic `1-(W-t/r)^2/(r+t/r)^2` minorizes `1_{W>-r}`. Its expectation is `r^2/(t+r^2)`. Thus

\[
 \mathcal B_2(t,-r)=-\frac{r^2}{t+r^2}
       +\frac{R_0t(A^2+3t)}{(c+r)^4}+h_fr. \tag{12}
\]

* For `u=r>=0`, choose the zero minorant. Then

\[
 \mathcal B_0(t,r)=\frac{R_0t(A^2+3t)}{(c-r)^4}-l_fr. \tag{13}
\]

Every valid witness is an upper bound; taking their minimum is allowed. The quadratic is licensed only for `r>0`; no division by a zero phase is introduced.

## 5. Exact noise-relative verification

For `t>0`, put `u=zt`. Dividing (11) by `t` gives

\[
\begin{split}
 \frac{\mathcal B_4(t,zt)}t={}&
 \frac{A^2-3a^2+(3+4A|z|-3a^2z^2)t+6z^2t^2+z^4t^3}{Ka^4}\\
 &+\left(\frac2{Ka}-l_\sigma\right)z
 +\frac{R_0(A^2+3t)}{(c-zt)^4},
\end{split} \tag{14}
\]

where `l_sigma=l_f` for `z>=0`, `l_sigma=h_f` for `z<=0`. This expression extends continuously to `t=0`. On either signed rectangle where `c-zt>0`, multiplying by the positive denominator gives a polynomial. Rational Bernstein positivity can prove an upper bound `-eta` over the entire closed rectangle, including `t=0`. It then holds for arbitrarily small positive noise, with no additive error independent of `t`.

The same scaling turns (12) into

\[
 \mathcal B_2(t,-zt)/t=-\frac{z^2}{1+z^2t}
      +\frac{R_0(A^2+3t)}{(c+zt)^4}+h_fz\quad(z>0), \tag{15}
\]

and (13) into `R0(A^2+3t)/(c-zt)^4-l_f*z`. These are again rational functions with explicit positive denominators. Regions not touching `t=0` can instead be checked directly in `(t,u)` after clearing the positive denominators. Finite coverings must include every phase and noise boundary and retain the original same-law variance region.

To translate to the manuscript's strict score target, retain its exact identity

\[
 \rho_B(C-C_B)=b\{EG(R)-f(u)\}+\mathcal R,
 \qquad b=\sqrt n\pi_k.
\]

If `t>=omega_minus*lambda`, `b>=m>0`, `mathcal R<=kappa*lambda/n`, `n>=N`, and one valid witness proves `EG-f<=-eta*t`, where `eta>0`, `kappa>=0`, then

\[
 \rho_B(C-C_B)\le
 -\{m\,\eta\,\omega_- -\kappa/N\}\lambda. \tag{16}
\]

A strict rational gate `m eta omega_minus-kappa/N>.001` gives exactly the old target, with all original normalization and acquisition hypotheses retained. At `lambda=0`, both conditional noises vanish and the separate Bernoulli theorem is still used. A negative signed repair or finite positive allowance can be retained before this coarser nonnegative-repair specialization.

## 6. Scope of the prospective simplification

If actual cells pass (11)–(16), this rule replaces their nearest-count Poisson/Bennett tails and their vanishing-noise tail monotonicity proofs. If the same rules pass all cells previously assigned the whole-count witness, the marked-crossing, fractional-part and curvature calculations cease to be dependencies for those cells. That latter coverage is not asserted here.

The general polynomial rule (2)–(6) gives a common expectation/certificate interface beyond the previous scalar-majorant identity. The quartic guard (7) is the new analytic ingredient making it immediately executable with one actual conditional-count moment. It is a valid upper bound despite the earlier paired-law examples having equal own-count distributions and unequal full CDFs.

Still required: the acquired supports, the legal incoming binomial-ratio bound, exact normalization/phase bounds, the original simultaneous moment/variance region, full closed-cell coverage and the final strict score gate. No optimizer/contact property or Fourier remainder is proved by this rule.
