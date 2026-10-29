# Independent review of the comparison through noise .03

No blocking defect was found in the stated theorem: for actual n>=42,
p in [.4,.53], conditional amplitude at most .6, total inward displacement
at most .072, raw |H|<=1.84, 0<lambda<=.03 and **C>=.4**, the defined
comparison error satisfies Delta_C<-lambda/100. The lower bound on C is
essential to this argument. The preceding .02 theorem for every C>=0
remains a separate result.

The proof retains a positive marginal third-moment gain and uses different
incoming estimates for negative and positive inner phase. It covers six
closed phase intervals, with no noise grid. The remaining noise interval,
other probability panels and independent finite base are not established
by this component. At zero noise the original Bernoulli seam is still
required; the strict positive-noise conclusion is not asserted there.

Review branch: `research/moderate-review-v11-20261028`, from reference
`6027b27f85473780eaf90542f490168873de5986`. No constructor program was
imported or rerun as an independent verification.

| Item | Mathematical status | Execution status |
|---|---|---|
| Cubic gain and its lambda/n normalization | Independently rederived from actual conditional third moments | Exact scalar gain and 36 actual-law checks |
| Conditional counts, variances and Gaussian normalization | Independently checked at the new inner width and noise ceiling | Constructor source review and direct arithmetic |
| Two own-count rectangles | Independent proof using the full bivariate quartic | Fresh 40-coefficient tensor Bernstein PASS |
| Six phase regions and infinite incoming tails | Complete analytic coverage checked, including strict/closed events | All six terminal margins independently reconstructed |
| Constructor's retained normalization code | Explicit source-pinned dependency inspected | Direct source execution avoids cached-bytecode substitution |
| Full comparison above .03 or full sharp theorem | Not established here | No complete acceptance or generation campaign |

## Independent derivation of the new gain

Put v=pq, v_j=E U_j^2 and m_j=E U_j^3. The inward bounds imply
U0-p<0 and 1+U1-p>0. Conditional centering therefore gives exactly

`E|Y-p|^3 = v(1-2v)+3v(v0+v1)+p*m1-q*m0`.

On the actual supports, m1>=-a1*v1 and m0<=a0*v0. Since
s=q*v0+p*v1, this yields the lower bound
`v(1-2v)+(3 min(p,q)-d)s`. No arbitrary signed moment was substituted
for an actual conditional moment.

To compare with rho_B after variance normalization, Taylor's formula
gives `(1+x)^(3/2)<=1+3x/2+3x^2/8` for x>=0. Its third derivative
is negative. After subtraction, the coefficient of s is bounded below
using

`3 min(p,q)>=1.2`, `3(1-2v)/2<=.78`, and
`3(1-2v)/(8v)<=13/16`.

Consequently

`(v+s)^(3/2)(rho-rho_B) >= s[87/250-(13/16)s]`.

Here s<=.03/42, sqrt(v+s)<.501, and the exact positive margin is

`(2/5)[87/250-13*.03/(16*42)]-.501^3 = 92514493/7000000000`.

Thus C(rho-rho_B)>s=lambda/n for C>=.4. The normal variance term
is at most `(7/4)*delta_+*lambda/n`, by differentiating the normal
distribution with the count fixed. In the inner interval delta_+<1;
globally it is <33/20. Subtract the gain before enlarging 1/n to 1/42.
This gives the asserted repair bounds 3lambda/(4n) and 2lambda/n.
The coefficients remaining after subtraction are positive, so the
replacement by the smallest n has the correct direction.

There is no gain of order lambda without the factor 1/n. The independent
controls exhibit actual marginals for which .4(rho-rho_B)<lambda,
while also proving .4(rho-rho_B)>lambda/n. Nor does this proof imply
the gain for C=0. These distinctions are reflected in the theorem.

## Count normalization and own events

The master identity conditions on one common iid sign count. All outgoing
terms are strict, while incoming terms are closed. Keeping only the own
outgoing count increases the error, including at atoms.

The variance ceiling at the new noise endpoint still gives
sqrt(v+s)<.501. For |u|<=3/40, the actual count displacement is
less than `(1.84)(.501)+.075=.99684<1`. The global displacement stays
below 33/20. Both the count and the segment between p and k/n are
interior, with the latter in (9/25,23/40). The finite Stirling remainder
and entropy/prefactor constants retain their validated domains.

The logarithmic derivative keeps the actual delta fixed while its
integration variable runs between zero and u. Its variance coefficient
is bounded by 8/3; the spatial term has absolute bound
`(2D*b+b^2)/(2v_*)`. At D=1,b=3/40 these give
24/25<f'<26/25. The mass lower bound 73/100 and own-count ratio
53/50 still follow from |delta|<1. On positive phase up to .1 the
older 19/20 slope applies, and the signed increment calculation gives
9/10 on the remaining positive phase. These estimates do not assume
that p is below 1/2.

Conditional variance is exactly
`Var(W_k)=lambda+delta(v1-v0)`, with `|v1-v0|<=(5/2)s`.
This establishes the interval [79lambda/84,89lambda/84] and all
incoming variance envelopes. No independent conditional law is silently
chosen for different counts.

The quartic indicator minorant has value zero at zero and is nonpositive
on the negative half-line. Its expectation is consequently a lower bound
for the strict outgoing event. With alpha=13/25, the two full scaled
quartics are checked on `0<=z<=3/2`, `0<=t<=89/2800`.
All 20 tensor Bernstein coefficients in each rectangle are positive
after subtraction of the claimed constant. The minimum margins are

- above 37/100 on the negative rectangle:
  `82564663499/16050459443200`;
- above 19/20 on the positive rectangle:
  `2663081/159941600`.

This is a separate certificate for the original quartic. It does not
repeat the constructor's quadratic truncation and vertex calculation.
The edge t=0 is included by continuous extension, whereas division by
the actual own variance is performed only at lambda>0, where that
variance has a strictly positive lower bound.

After r=3t/2 the negative Cantelli-minus-linear derivative is positive
at the switch and first increases then decreases. Any later critical
point is a maximum; both endpoint minima are checked. For positive phase
the normal linear term alone suffices past that switch. The switch is
inside the inner phase interval for all admissible t.

## Incoming tails and phase joins

The external quadratic-hinge Poisson theorem and its variance-upper-bound
scope are unchanged; see the primary-source review linked in the v10
report. The first incoming term uses anchor 1 only where it is admissible.
For negative inner phase, u<=0 licenses **h=0**; for positive inner
phase, the uniform value is h=3/40. Treating both with the positive
value is a valid but too weak upper bound, not a mathematical
counterexample. The higher incoming counts are covered by the same
factorial-moment and infinite geometric-series argument.

At the new endpoint, mu_I=3/32 and mu_G=7/72. Every remainder
denominator and geometric ratio has the right sign. Q/lambda and
J/lambda are increasing on the used inner domains, so the inner errors
remain proportional to the actual lambda uniformly down to zero.
The negative outer first-tail bound is also valid: mu_G<1/3<2/3
ensures its denominator and required monotonicity.

On the negative outer phase, the Cantelli derivative-shape argument
is used instead of a false global concavity assertion. Positive outer
phase uses Cantelli for the first incoming event. The expression
`.9u-1.5*t_G/(t_G+(1-u)^2)` is concave on each of its two intervals
because `3(1-u)^2>t_G`. All brackets are positive before substituting
a lower count mass. The outer bounds worsen with increasing lambda;
their absolute endpoint margins therefore cover all smaller noise.

The six closed intervals, in order, are
[-34/125,-3/40], [-3/40,0], [0,3/40], [3/40,1/10],
[1/10,1/5] and [1/5,91/125]. They have no missing endpoint.
The independent arithmetic reproduces every terminal residual:

| Region | Residual after allowing lambda/100 |
|---|---:|
| Negative inner, divided by lambda | 19650157/2820720000 |
| Positive inner, divided by lambda | 40612185886957/129085181232000 |
| Negative outer | 12343549039/533914920000 |
| Positive near | 1221121/371280000 |
| Positive middle | 652372219/42906045000 |
| Positive far | 40879152773/857753190000 |

## Source binding, execution and limits

The constructor now reads the old normalization source as bytes, checks
its SHA256, and compiles those exact bytes into an isolated namespace.
The retained gates are explicit names. This repairs the initial use of
an import loader and a positional prefix, which could have read cached
bytecode or changed meaning after a gate reorder. The retained source
hash is `13c4c27a66cb692a5ac480a986e8240a8ab38b59c066cb3f24d81d9676a13f11`.
The new checker and review do not modify that source.

`counts_v11_independent.py` imports no constructor. Besides its 40
polynomial coefficients, gain check and six margins, it checks 36 actual
marginals and 144 own-count events, with p=.4 or .53, n=42 or 43,
noise .03, .002 or 10^-8, and either or both conditional noise signs
present. Exact convolution preserves atoms. A rational comparison after
sign-checked squaring verifies the actual cubic gain and rejects the
false unscaled gain on every law. A genuinely false stronger quartic
constant 1/2 is also rejected at an explicit rectangle corner.

Fresh source hashes, interpreter version, elapsed time, stdout, stderr
and return code are under `runs/counts-v11-independent-20261028/`.
The final checker accepts one positional repository-root argument for
integrated replay. Compilation of the constructor's proof remains
separate from this arithmetic review.

Recommendation: accept the stated .03 comparison after integration checks.
Its dependency removals apply on that domain after the original strip
and threshold premises have been acquired. This review neither deletes
the old certificates nor establishes their remaining parameter regions.
