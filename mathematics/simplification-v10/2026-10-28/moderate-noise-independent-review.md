# Independent review of the moderate-noise comparison

No blocking defect was found in the stated comparison for every actual
integer n>=42, p in [2/5,53/100], incoming conditional amplitude at most
3/5, inward displacement at most 9/125, raw threshold |H|<=46/25, and
0<lambda<=1/50. The proof uses four complete closed phase intervals and
an infinite-tail bound. It does not infer coverage from discovery samples.

The conclusion is Delta_C<-lambda/100 for each C>=0, with Delta_C
defined in the constructor's theorem. For C=C_E, the sharp Bernoulli
theorem excludes a nonnegative fixed-target excess. This review does not
establish the incoming strip, raw-threshold restriction, remaining
probability panels, noise above 1/50, or the finite base. At lambda=0,
the conditional variances vanish and the marginal is Bernoulli; this
separate seam uses the Bernoulli theorem, not the strict positive-noise
comparison or a limiting argument.

| Item | Mathematical status | Execution status |
|---|---|---|
| Conditioning, normalization and moment repair | Independently rederived for the actual conditional laws | Source inspection and exact actual-law controls |
| Quadratic-hinge Poisson comparison | Published theorem at the stated variance-upper-bound scope | Primary-source hypotheses inspected; not formally verified here |
| Own-count quartic rectangles | Independently proved for the full rectangles by tensor Bernstein coefficients | Fresh exact PASS, 40 positive coefficients |
| Four phase regions and infinite incoming tail | Independently checked analytically, including all boundaries | Four terminal margins freshly reconstructed |
| Constructor's 62 scalar gates | Code and use of each constant reviewed | Constructor not imported or rerun as an independent implementation |
| Full Berry--Esseen theorem | Not established by this component | No complete acceptance or generation campaign |

The review branch is `research/smallnoise-review-v10-20261028`, created
from `00ba714897f2e09995d78354ac3c8931e257cd05`. All review files are new.

## Actual laws, normalizations and signs

Conditional centering gives Var(Y)=pq+s and hence the stated scaling
ell=(pq+s)^(-1/2). If the count is j, the noise sum has precisely j
copies of U_1 and n-j copies of U_0. Consequently the conditioning
identity retains strict outgoing events and closed incoming events.
Discarding all outgoing terms except j=k increases the comparison error.
The normal increment and variance repair in the master inequality have
the correct signs; the same fixed integer k is used throughout each
derivative calculation.

From s<=1/2100, sqrt(pq+s)<501/1000. Thus |delta|<33/20 globally,
|delta|<1 for |u|<=1/20, and |delta|<21/20 for 0<=u<=1/10.
These estimates imply 1<=k<=n-1. The segment between p and k/n is
contained in (9/25,23/40). On it r(1-r)>.23 and |1-2r|<.28,
which independently justify the entropy, logarithmic-prefactor and
finite-Stirling constants 6, 5/4 and 3/8. The Stirling estimate used
here is finite and uniform in the changing law and index.

In the logarithmic normal derivative, separate the variance terms at
delta from the spatial increment 2 delta t+t^2. This gives the stated
coefficient 1/(2v_*)+D^2/(2*42*v_*^2)<8/3, without losing an unrecorded
variance term. On positive phase, convexity of 2 delta t+t^2 on [0,u]
and delta=xi-u imply the sharper maximum max(0,2 Xi u-u^2).
The latter increases up to the stated upper phase because Xi>91/125.
This proves the improved positive derivative constant 9/10; the near
positive interval instead uses the absolute-log estimate and constant
19/20. There is no differentiation of a moving lattice anchor.

The upper mode mass and lower own-count mass give the global ratio
bound. In the inner interval, the first binomial ratio uses delta>=-1;
all subsequent ratios are <=1 since (n+1)p-k<153/100<2. These
arguments still apply for p above 1/2.

The inward assumptions ensure U_0<p and 1+U_1>p, so the absolute cubic
can be expanded with fixed signs. The two inequalities U_1^3>=-a_1 U_1^2
and U_0^3<=a_0 U_0^2 give the stated lower bound for E|Y-p|^3. Taylor's
upper bound for (1+x)^(3/2) has the right direction for x>=0; its third
derivative is negative. The resulting bracket is strictly positive
throughout the present domain. Therefore rho>=rho_B and discarding
C(rho_B-rho) is justified for every C>=0. The remaining normal repair
is bounded by (7/4) delta_+ lambda/n.

Writing s_j=E U_j^2 gives Var(W_k)=lambda+delta(s_1-s_0), with
|s_1-s_0|<=s/min(p,q). This proves the own-count interval
[79 lambda/84,89 lambda/84] on the inner phase and the global cap
11 lambda/10. For an incoming count,
Var(W_(k+i))<=lambda[1+(5/2)(D+i)/n]<=i V lambda.
Each conditional sum still consists of independent centered variables;
conditioning only changes how many variables of each of the two fixed
conditional laws occur.

## Poisson tails and the variance envelope

The constructor invokes Pinelis, *On the Bennett--Hoeffding inequality*,
[Proposition 2.8 and Corollary 2.11](https://arxiv.org/abs/0902.4058),
for the quadratic hinge. The comparison allows an upper bound on total
variance. An independent primary-source route appears in Bentkus,
[*On Hoeffding's inequalities*](https://arxiv.org/pdf/math/0410159),
the proof of Theorem 1.1, equations (3.8)--(3.10): quadratic-hinge
moments are dominated by the appropriate Bernoulli sum. Padding with
zeros and taking its Poisson limit yields the corresponding Poisson
comparison; bounded fourth moments justify convergence of quadratic
hinge moments. The Poisson tail transform is also explicitly recorded
in Bentkus--Juškevičius,
[Remark 1.6, equation (1.19)](https://arxiv.org/pdf/1111.6358).

Applying this theorem to -W is legitimate because |U_j|<=3/5.
Variance inflation is performed before selecting the hinge. This avoids
an unproved assertion that an arbitrary centered-Poisson hinge quotient
is monotone in its variance parameter. The threshold remains the actual
closed incoming threshold throughout the substitution.

For the first count, the anchor 1 is admissible on the two intervals
where it is used: h=0 and h=1/20. The exact numerator is
mu^2-mu+1-exp(-mu). Taylor's lower bound for exp(-mu) proves the stated
upper bound mu^2/2+mu^3/6. The anchor 1 is not admissible throughout
the positive outer interval; the proof correctly uses Cantelli there.

For i>=2 and integer r>=1, r^2<=C(i+r,i+1). At i=2 this reduces to
(r-1)(r-2)>=0; increasing i increases the binomial coefficient.
The Poisson factorial moment then gives the complete numerator bound.
Inflating variance to i V lambda yields denominator at least
i(b_h+mu)>0. The coefficient ratio in the remaining series is

`[i/(i+2)]*(1+1/i)^i < e < 3`.

Thus the displayed geometric remainder covers every i>=2, including
arbitrarily many legal incoming counts. Adding terms for illegal counts
only enlarges its upper bound. The denominator is positive even at the
largest phase, where b_h=3/50; also 3 mu_G=7/36<1.

For the inner interval, J/lambda increases because mu/(b_h+mu)
and 1/(1-3mu) increase. The first-tail quotient divided by lambda
increases on mu<=a_h: mu/(a_h+mu)^2 and 1/2+mu/6 both increase there.
The two required endpoint inequalities mu<a_h are verified. Accordingly
the final inner estimate remains proportional to actual lambda all the
way down to zero, with no fixed additive remainder.

## Own count and complete phase coverage

The quartic numerator factors as -x(x+alpha)^2(x-2alpha); it is
nonpositive for x<=0 and its positive maximum is below 5 alpha^4.
It is consequently a minorant for the strict event indicator, including
the atom at zero. Independence and centering give |E W^3|<=At and
E W^4<=A^2t+3t^2. Expansion after the signed shift produces exactly
the lower polynomial in the proof.

The own-count variance is positive whenever lambda>0, so dividing by
t is valid. The full scaled quartic extends continuously to t=0. The
independent check uses that full polynomial on both closed rectangles,
not the constructor's quadratic truncation. All 20 tensor Bernstein
coefficients in each rectangle are strictly positive after subtracting
the stated target. Their minimum margins are

- negative rectangle above 3/8: 72589549/5788125000;
- positive rectangle above 1: 5571/140000.

For negative phase after r=2t, the Cantelli-minus-linear derivative
first increases and then decreases. Its positive value at the switch
means any later zero is a maximum, so the minimum occurs at a boundary.
Both necessary boundaries, the initial slope and the switch location
are checked. The positive phase uses the quartic through r=3t/2 and
then the positive linear normal increment. These are bounds for the
actual own-count variance, not the incoming variance envelope.

The negative outer interval uses the same derivative-shape argument
with t replaced by 11 U_*/10. It does not falsely assert concavity
over that entire interval. On the positive near interval Cantelli is
evaluated at the worst threshold 9/10. On the positive far interval,
the retained linear term minus Cantelli is concave because
3(1-u)^2>7 U_*/6; both phase endpoints are included. The remaining
tail uses its worst h on each interval. All brackets are positive before
the lower bound for sqrt(n) pi_k is substituted.

The four closed intervals are [-34/125,-1/20], [-1/20,1/20],
[1/20,1/10] and [1/10,91/125]. Their union is the entire phase
interval, with overlap at every join. Independent terminal arithmetic
reproduces these margins after subtracting the requested lambda/100:

| Region | Exact margin |
|---|---:|
| Inner, divided by lambda | 113307367/16930513600 |
| Negative outer at U_* | 95575595137/4788968940000 |
| Positive near at U_* | 8209/4872000 |
| Positive far at U_* | 389390249/17290880250 |

For the outer regions, smaller lambda improves every incoming error
and repair, and the chosen own-count bound cannot deteriorate. The
absolute endpoint margins therefore imply the desired bound for all
smaller positive lambda.

## Fresh arithmetic and adversarial controls

`moderate_noise_independent.py` imports no constructor. Besides the
40 full-polynomial coefficients and four final margins, it checks 36
actual marginals: n=42 or 43, p=2/5 or 53/100, lambda=1/50, 1/500,
or 10^-8, with noise on both signs or either sign alone. Their conditional
laws are centered two-point laws with outer magnitude 3/5 and inward
endpoint determined exactly by the required variance. They respect the
actual signs and the inward budget. Exact finite convolution supplies
144 own-count tests, including exact threshold atoms. The code verifies
conditional centering, variance, third- and fourth-moment inequalities,
the own-count lower bound, and rho>=rho_B without floating-point roots.

Negative controls distinguish genuine false claims:

- The negative rectangle cannot support constant 1/2: at z=2 and
  t=89/4200 the full polynomial is 280392053/723515625<1/2.
- The factorial majorant used for anchors i>=2 fails for i=1, r=3.
- The exact first Poisson hinge exceeds mu^2/2 at mu=1/16; deleting
  its positive cubic correction would understate this expectation.
- At every constructed collision, strict and closed own-count events
  differ by a strictly positive atom. The strict convention is retained.

Fresh stdout, stderr, return code, interpreter version, elapsed time and
reviewed source hashes are in
`runs/moderate-noise-independent-20261028/check01/`. A preliminary
un-timed reproduction is separately retained in `preflight01/`.

Recommendation: accept the comparison on its stated domain after the
coordinator's integration checks. It removes the half-amplitude,
marked-crossing, harmonic and count-curvature dependencies there once
the incoming 3/5 strip and other premises have been acquired. It adds
the stated quadratic-hinge Poisson theorem. It authorizes no deletion
or replacement outside that domain.
