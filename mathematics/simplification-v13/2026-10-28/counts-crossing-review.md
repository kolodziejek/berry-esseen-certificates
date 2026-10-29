# Independent review of the all-noise crossing identity

No blocker found in the coordinator's final `crossing.tex`, SHA256
`0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec`.
The result is an exact finite identity, a nonnegative unweighted crossing
loss, and an exact weighted decomposition. It is **not** yet the full
larger-noise Berry–Esseen comparison.

I independently derived the selected-noise bias, local crossing formula and
weighted summation by parts before reading the final canonical proof. The
final stop-loss telescoping proof is shorter and includes the same bias
without a stopping-time argument. This review concerns the new coordinator
proof; I constructed the previous v12 negative-inner comparison, which is
not being claimed as independently re-proved here.

| Claim | Mathematical status | Execution status |
|---|---|---|
| Existence and uniqueness of the closed/strict crossing | Independently rederived from positive increments and threshold bounds | All direct-product cases satisfy strict ordering |
| Local stop-loss cancellation and global nonnegative loss | Independently rederived, including endpoint atoms | 24 exact direct-product controls PASS |
| Clipped age reserve | Independently checked pointwise in both kernel regions | Same 24 controls PASS |
| Exact weighted CDF identity | Independently derived by summation by parts | 24 exact direct-product controls PASS |
| Selected noise is generally biased | Independently derived by deleting the coordinate from the crossing event | 9 controls have strictly positive selected noise mean |
| General weighted comparison at larger noise | Still open | No acceptance or certificate removal claimed |

## Analytic audit

The assumptions U0<=a0, U1>=−a1 and a0+a1<1 make every coupled
increment T_i−T_(i−1) at least1−a0−a1>0. The bounds
n*a0<=t<n*(1−a1) imply T0<=t<Tn on every sample. Consequently
K lies in {0,...,n−1}; no clipping or missing boundary term occurs.
The lower crossing event is closed and the upper event strict.

Write D=1+U1 and m=1−a1. The kernel

`h(x)=E(x−U0)_+−E(x−D)_+−P(D<=x)`

has the following two exact forms. For x<m it is E(x−U0)_+ because
both D terms vanish. For x>=m>a0, centering gives
h(x)=P(D>x)−E(D−x)_+. Since D<=1+A1, its positive overshoot is at
most (A1+a1)1{D>x}; therefore h is nonnegative when A1+a1<=1.
At x=m an atom at the lower endpoint of D belongs to P(D<=x), so the
second formula with strict survival is the correct one. The source handles
this endpoint explicitly.

Deleting both variables of pair i leaves R_i independent of that pair.
Thus E h(R_i) equals

`E(t−T_(i−1))_+ − E(t−T_i)_+ − P(T_i<=t)`.

The first two terms telescope, with endpoint expectations t and0.
Summing P(T_i<=t) gives E K. This proves g=t−E K=sum E h(R_i)>=0.
Integrability is sufficient for every term; no uniform integrability,
optional stopping, or fixed-law limit is used.

For the age refinement, conditional on R_i=x, the crossing event is
U0_i<=x<D_i. Below m, E(x−U0)_+ dominates the expected clipped age
on this event. Above m, U0_i<=a0<x surely, the age is at leastm−a0,
and h(x)>=(1−A1−a1)P(D>x). The stated minimum b is valid in both
regions. Summing over the unique crossing proves the clipped-age reserve.

The conditions hold throughout the stated acquired noise envelope:
right b>=.328, left b>=.232, and sqrt(1/4+.616/42)<.515 gives
|H|sqrt(v+s)<.948. The inequalities n(.25−.072)>.948 and
n(.928−.53)>.948 hold already at n=42. This is only the mapping of
acquired bounds into the crossing theorem, not a fresh acquisition proof.

## Weighted derivation and the exact missing inequality

Set A_j=E(t−T_j)_+, L_j=A_j−(t−j)_+>=0 and H_i=E h(R_i)>=0.
The local identity says F_i=A_(i−1)−A_i−H_i. Multiply by the actual
binomial masses pi_i and include pi_0 F_0=pi_0. Summation by parts gives

`F_actual=pi_0+pi_1*t+sum_(j=1)^(n−1)(pi_(j+1)−pi_j)A_j−sum_i pi_i H_i`.

Replacing A_j by (t−j)_+ yields the linear interpolation of the binomial
CDF at t. Hence the source's weighted identity and exact Delta_C formula
have the correct signs and normalizations. The count coupling is an
auxiliary representation preserving each conditional marginal. It makes
no assertion about the original joint law of its count and the auxiliary K.
The final prose states that distinction correctly.

The new gap is explicit: a quantitative lower bound on
sqrt(n)*sum pi_i H_i must absorb the signed curvature, phase, normal-variance
and cubic terms for the same law. The sign of sum H_i alone does not prove
that. In particular, the binomial masses cannot simply be replaced by one
constant without controlling the resulting error.

The companion `counts-tools.tex` proves a new uniform curvature bound and
an all-noise symmetric central subcase. Its four-moment obstruction shows
why a naive selected-term polynomial estimate is insufficient. These are
additional tools, not a completed general closure. The source correctly
retains the current count certificates until the missing joint inequality
is proved.

## Reproduction

The independent control program imports no constructor code and enumerates
the full product space of independent conditional pairs, rather than using
the constructor's conditional-sum recurrences. It checks 24 combinations
of laws, n=3 or4 and exact thresholds, including collisions and zero noise.
The source hash is verified before execution.

```
python3 -I -B mathematics/simplification-v13/2026-10-28/counts-crossing-review-check.py COORDINATOR_REPO_ROOT
```

Evidence: `runs/counts-v13-20261028/crossing-review01/`, with command,
interpreter, source pins, stdout, stderr and return code. These finite
controls support the analytic audit; they do not certify an unproved
weighted inequality or the external acquisition chain.
