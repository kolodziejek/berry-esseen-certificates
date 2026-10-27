# Independent scalar and smoothing review — 27 October 2026

Baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`, fork
`kolodziejek/berry-esseen-certificates`, branch `audit/scalar-20261027`.
This review adds no theorem to the manuscript and authorizes no removal.
It audits the supplied recurrence and two explicitly distinct assembly lemmas.

| Result | Mathematical status | Execution status |
|---|---|---|
| Support-free smoothing recurrence, every integer n >= 2 | Locally derived and checked below, using ordinary calculus and the Gaussian Fourier identity | Finite constants checked by `check_scalar.py`; analytic statement is not a program output |
| First strict violation implies scalar entry gates at n >= 47 | Locally derived and checked | Fresh exact-arithmetic evidence recorded in `runs/least-counterexample-20261027/scalar01/` |
| Weak global assembly from those gates | Conditional on complete acquisition and exclusion for the selected owner | No acquisition/exclusion drivers run here |
| Separately named strict tail assembly from a weak prefix | Conditional on the equality-inclusive versions of acquisition/exclusion | No acquisition/exclusion drivers run here |

## Source boundary

All locations refer to the baseline above, not later changes or historical
success reports. Links below target the user's fork at the frozen commit.

- Definitions: [paper/main.tex, lines 40–54](https://github.com/kolodziejek/berry-esseen-certificates/blob/6346fc1b4432bc5982822aa696eb566ed9e1e1ee/paper/main.tex#L40-L54).
- Recurrence and its complete short proof: [paper/analytic-supplement.txt,
  lines 6479–6522](https://github.com/kolodziejek/berry-esseen-certificates/blob/6346fc1b4432bc5982822aa696eb566ed9e1e1ee/paper/analytic-supplement.txt#L6479-L6522),
  label `cut49:global:smoothing`; the supplement identifies original source
  lines M7458–7506. Physical supplement lines differ from those original lines.
- Current tail assembly: [paper/main.tex, lines 460–510](https://github.com/kolodziejek/berry-esseen-certificates/blob/6346fc1b4432bc5982822aa696eb566ed9e1e1ee/paper/main.tex#L460-L510).
- Equality is expressly included by the supplied attainment proof:
  [paper/main.tex, lines 107–136](https://github.com/kolodziejek/berry-esseen-certificates/blob/6346fc1b4432bc5982822aa696eb566ed9e1e1ee/paper/main.tex#L107-L136).
- A support refinement explicitly permits `0 <= C-C_E <= .7/n`:
  [supplement, lines 719–755](https://github.com/kolodziejek/berry-esseen-certificates/blob/6346fc1b4432bc5982822aa696eb566ed9e1e1ee/paper/analytic-supplement.txt#L719-L755).
- The parameterized local comparison still needs all of its support,
  normalization, sign and witness hypotheses:
  [supplement, lines 7153–7197](https://github.com/kolodziejek/berry-esseen-certificates/blob/6346fc1b4432bc5982822aa696eb566ed9e1e1ee/paper/analytic-supplement.txt#L7153-L7197).
  Its positive- and zero-noise conclusions invoke the separate binomial
  theorem: [lines 7748–7768](https://github.com/kolodziejek/berry-esseen-certificates/blob/6346fc1b4432bc5982822aa696eb566ed9e1e1ee/paper/analytic-supplement.txt#L7748-L7768).

The last three references identify equality-compatible parts of the interface;
they do not by themselves establish the entire acquisition chain. The main
audit must verify all intervening edges and numerical predicates.

## 1. Independent derivation of the recurrence

Let P be any mean-zero, variance-one real probability law with finite
rho = E|X|^3, and let X_1,...,X_n be iid with law P. No support restriction,
maximality, attainment, fourth moment or density is assumed. Lyapunov's
inequality gives rho >= 1. Set v = n-1 >= 1 and F_v(t) = Phi(t/sqrt(v)).

For every raw threshold H, independence and the defining uniform bound for
the same marginal P at index v give

\[
\left|P(S_n\le H)-E F_v(H-X_n)\right|
\le C_v\rho/\sqrt v.
\]

This use of C_v is legitimate before taking any supremum at index n.
The CDF of S_v is not differentiated or approximated by a density.

Taylor's theorem applied only to the smooth normal CDF, with its global
remainder, gives for every real y

\[
\left|F_v(H-y)-F_v(H)+yF'_v(H)-\tfrac12y^2F''_v(H)\right|
\le \frac{\|\phi''\|_\infty}{6v^{3/2}}|y|^3.
\]

Now phi''(z) = (z^2-1)phi(z). On z^2 <= 1 its absolute value is at most
phi(0). On u = z^2 >= 1, (u-1)e^{-u/2} is maximized at u=3, with value
2e^{-3/2}<1 (indeed e^{3/2}>1+3/2>2). Thus the norm is exactly phi(0).
Taking expectation uses only EX=0, EX^2=1 and E|X|^3=rho, and yields

\[
\left|E F_v(H-X)-F_v(H)-\tfrac12F_v''(H)\right|
\le \frac{\phi(0)\rho}{6v^{3/2}}
<\frac{\rho}{15v^{3/2}}.
\]

Direct differentiation in v shows the heat identity
partial_v F_v = F_v''/2 and partial_v^2 F_v = F_v^{(4)}/4. Here primes
differentiate the raw argument H, not the variance. Therefore

\[
F_{v+1}(H)-F_v(H)-\tfrac12 F_v''(H)
=\int_0^1(1-t)\tfrac14F_{v+t}^{(4)}(H)\,dt.
\]

Since F_w^{(4)}(H) = w^{-2}phi'''(H/sqrt(w)), the absolute value is at most
||phi'''||_infty/(8v^2). Gaussian Fourier inversion and differentiation
under its absolutely convergent integral give

\[
\|\phi'''\|_\infty
\le\frac1{2\pi}\int_{\mathbb R}|t|^3e^{-t^2/2}\,dt
=\frac2\pi.
\]

The integral on the positive half-line is 2, by u=t^2/2 and
integral_0^infty u e^{-u}du=1. In particular, the heat error is at most
1/(4 pi v^2) < 2/(25v^2). The Gaussian Fourier identity used here follows
from the elementary Gaussian transform; differentiating is justified by
integrability of |t|^3 exp(-t^2/2). It is a standard analytic identity, not
a numerical claim derived from this checker.

Combining the three bounds, multiplying by sqrt(n)/rho and using rho>=1
proves, uniformly in H and P,

\[
C_n\le\sqrt{\frac n{n-1}}C_{n-1}
+\frac{\sqrt n}{15(n-1)^{3/2}}
+\frac{2\sqrt n}{25(n-1)^2}. \tag{S}
\]

The exact same constants work for every n>=2, including n=2. Arbitrarily
remote rare atoms cause no change: the only integrated remainder is a
constant times |X|^3. Moving thresholds and atom collisions are harmless
because the estimate holds for every real H. For strict events, take
H_j increasing to H; the CDF has the requisite left limit and Phi is
continuous. Thus both jump edges and reflected branches are included.
No fixed-law limit, uniform-integrability assertion or optimizer exists
inside this argument.

## 2. Elementary bounds for pi and C_E

For completeness, no floating-point value of C_E is an input. Let
a=arctan(1/5), b=arctan(1/239). Tangent addition gives tan(2a)=5/12,
tan(4a)=120/119 and tan(4a-b)=1. Also

\[
0<4(1/5-1/(3\cdot5^3))-1/239<4a-b<4/5<1<\pi/2.
\]

The arctangent bounds follow by integrating 1-t^2 < 1/(1+t^2) < 1
on positive intervals. The final pi/2>1 follows from
arctan(1)>1/2. Hence 4a-b=pi/4, and

\[
\pi>16(1/5-1/(3\cdot5^3))-4/239
=281476/89625>157/50>25/8.
\]

This proves phi(0)<2/5 and 1/(4pi)<2/25 used above. Moreover,
sqrt(10)<19/6 because 361>360. Therefore

\[
C_E^2=\frac{19+6\sqrt{10}}{72\pi}
<\frac{1900}{11304}<\frac{1681}{10000},
\]

the last difference having numerator 2024 over 113040000. Positivity
then gives 0<C_E<41/100.

## 3. First strict violation: weak global conclusion

Assume C_j<=c=C_E for 1<=j<=46. If the set of n with C_n>c is nonempty,
choose its least member n; then n>=47 and C_{n-1},C_{n-2}<=c. In
particular d_n=n(C_{n-1}-C_n)_+=0. Put s=sqrt(n/(n-1)). By (S),

\[
n(C_n-c)\le\frac n{n-1}
\left(\frac c{s+1}+\frac s{15}+\frac{2s}{25\sqrt{n-1}}\right).
\]

For n>=47, n/(n-1)<=47/46, s>1, sqrt(n-1)>6 and s<1011/1000;
the last assertion follows from 46*1011^2-47*1000^2=17566>0. Thus

\[
0<n(C_n-c)<\frac{47}{46}
\left(\frac{41}{200}+\frac{1011}{15000}+\frac{1011}{75000}\right)
=\frac{335909}{1150000}<\frac3{10}<\frac7{10}.
\]

The margin below 3/10 is 9091/1150000. Also

\[
C_n<\frac{41}{100}+\frac3{470}
=\frac{1957}{4700}<\frac{4247}{10000},\qquad
C_{n-1},C_{n-2}<\frac{4253}{10000}.
\]

The own-cap margin is 3909/470000. These inequalities include n=47.
They establish every scalar gate displayed in the roadmap. If complete
acquisition and local exclusion apply to such an attained contrary owner,
they contradict its existence. That yields C_n<=c for all n. It proves
no strict inequality by itself: the constant sequence C_n=c obeys (S).

## 4. Separately named equality-inclusive tail lemma

Assume the same weak prefix through 46. In addition assume that fixed-index
attainment, acquisition and local exclusion apply to every selected owner
with n>=47, **0<=C_n-c<=.7/n**, d_n<=.19, C_n<.4247 and
C_{n-1},C_{n-2}<.4253, and exclude that owner including at C_n=c.
Every support, resource, probability, moment, sign, normalization and
certificate hypothesis is part of this extra input.

If some n>=47 has C_n>=c, choose the least such n **within that tail**.
All earlier tail values are <c and all prefix values are <=c. Thus both
predecessors are <=c, d_n=0, and the calculation above gives
0<=n(C_n-c)<3/10 and the required caps. Equality-inclusive acquisition
and exclusion contradict this choice. Hence C_n<c for every n>=47.

The original > argument has not been silently relabeled as strict. This
separate lemma exploits a different contrary set and a stronger interface
whose equality case must survive every acquisition edge. A weak finite
prefix is enough; the first >= violation among *all* indices would be the
wrong choice because equality might occur inside the prefix.

## Evidence, limits and permitted dependency conclusions

Run `python3 -B mathematics/audit/2026-10-27/check_scalar.py` from the
worktree root. The checker uses only standard-library integer/Fraction
arithmetic and checks the finite rational comparisons after the written
analytic reductions. It does not prove Taylor's theorem, Gaussian inversion,
attainment, acquisition, local comparison or certificate coverage. Its
negative controls reject invalid constants, the n=46 endpoint under this
particular rational square-root envelope, n=1, a claimed .29 bound, and
missing/unexpected input fields. Rejection at n=46 says nothing against
the recurrence or an independently chosen envelope there.

The recurrence itself has no strong46, three-loss, support, local certificate
or finite 47/48 dependency. Thus **the scalar entry step** can replace an
independent computation of precisely these scalar caps when the consumer
has the preceding sharp bound and n>=47. Removing the strong46/three-loss
*assembly branch* from a global proof is conditional on complete acquisition
and exclusion having no dependency back into that branch. Removal of any
physical certificate, including finite 47/48 or coarse caps shared by other
consumers, is not justified by this review. No existing files were changed.
