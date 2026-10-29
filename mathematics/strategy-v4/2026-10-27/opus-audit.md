# Audit of the Opus discrete experiments and proposed shortcuts

The attachment supplies exploratory programs, not a proof of skeleton domination
or global optimality. **Universal domination by the same-sign-probability
Bernoulli skeleton is false, including at index 42.** The counterexamples below
are actual iid laws, with exact rational probabilities and certified normal
bounds. They are far below the Esseen constant and outside the small-moment
local-comparison region. No existing certificate dependency can be removed on
the strength of these experiments.

Worktree branch: `research/v4-discrete-audit-20261027`; starting commit
`ca4943aae7a85ffa85d5d4d7166987dc055cb3e6`. The immutable original project
baseline remains unchanged. Only this new audit directory and its run directory
were written. The four allowlisted members of `/Users/bkolodziejek/Downloads/files.zip`
were copied byte-for-byte to `opus-supplied/`; its `provenance.json` records
archive and member hashes. The supplied programs were read, not imported or run.

| Result | Mathematical status | Execution status |
|---|---|---|
| Universal same-sign-p skeleton domination | Refuted by the explicit iid laws below | Fresh bounded rational checks, exit 0 |
| Near-collision merging as an exact CDF calculation | Refuted: a 1/4 CDF error is possible | Fresh exact rational control, exit 0 |
| Small deterministic score screen | Numerical exploration only | 171 laws at each of eight indices; exit 0 |
| Bernoulli, three/four-atom, collision and remote-atom controls | Numerical scores; exact convolution and mass identities | 15 fixed law/index controls; exit 0 |
| Finite candidate set for a fixed discrete contact function | Locally derived analytic reduction below | No continuum contact acceptance program implemented |
| Moment-preserving second variation | Locally derived necessary condition below | One exact four-atom direction checked |
| Full sharp bound, extremizer reduction or certificate replacement | Not established by this audit | No native certificate or random campaign executed |

## 1. What the programs actually compute

The source locations here refer to the unchanged copied files in
`mathematics/strategy-v4/2026-10-27/opus-supplied/`.

* `README.md:3–5` calls the discrete scores exact while simultaneously specifying
  double precision and disclaiming certification. Count-vector enumeration is
  exhaustive **combinatorially**, but the resulting arithmetic is not exact.
  `experiments.py:13–20` uses floating `gammaln`, logarithms, exponentials and
  matrix products, then rounds every sum location to ten decimal places.
  `experiments.py:31–36` does correctly consider both the positive closed edge
  and the reflected open edge, subject to that inaccurate sum law and `ndtr`.
* The advertised `n=1..41` search actually tests the twelve indices explicitly
  listed at `experiments.py:120`. The Bernoulli comparison samples only the
  grid `[0.02,0.98]` at lines 97–105. The three-point search is local
  Nelder–Mead, rejects weights below `1e-6`, and has finitely many starts
  (lines 108–123). Failure to find a better law is not an upper bound.
* `noise_test`, lines 43–78, compares particular conditional-noise shapes at a
  rounded phase with an unproved first-order prediction. Its intermediate
  convolutions are also rounded (lines 66,73). The `+1e-12` inside `floor`
  at line 74 can even make the numerical fractional part negative immediately
  below an integer. No uniform remainder bound accompanies the prediction.
* `skeleton_test.py:8–11` uses the sign probability after centering, with the
  numerical cutoff `x>1e-12`. This differs from the exact `P(X>0)` when a
  small positive atom is present. It does not use the Bernoulli law matching
  the signed third moment. Lines 13–25 give bounded random exploration, not
  a complete family. Line 3 executes a text prefix from another source file;
  our checks do not use that mechanism.
* `contact_test.py:13–15` uses a grid and bounded scalar minimization, so
  “best two-point law” is a numerical candidate. Lines 25–29 sample 24,001
  points of `[-6,6]`, plus points displaced by `1e-9` from jumps. They do
  not enclose all real y, stationary points between grid nodes, or the tails.
  The `floor(x+1e-12)` at line 21 is not exact closed-event evaluation.
  The printed `ysup` is the grid maximizer even if the reported supremum
  came from `extra`. Only fifteen n values are used (line 32), not every
  n from 1 to 100. The cited manuscript contact lemma is stated for n>=2;
  the n=1 experiment is outside that literal statement.

The attachment records no rigorous errors for these arithmetic operations.
The README's rough runtime description is inherited, not a measured cost here.

## 2. Exact counterexamples to unconditional skeleton domination

For a raw law Y, write mu=EY, v=Var(Y), r=E|Y-mu|^3, and standardize
X=(Y-mu)/sqrt(v). Its score at a raw n-sum threshold t is

\[
 {\sqrt n\,v^{3/2}\over r}
 \left\{\mathbb P\Bigl(\sum Y_i\le t\Bigr)
       -\Phi\Bigl({t-n\mu\over\sqrt{nv}}\Bigr)\right\}.
\]

The skeleton used here has p=P(Y>mu), atoms
`-sqrt(p/(1-p))`, `sqrt((1-p)/p)`, and probabilities `1-p,p`.
This is the standardized sign-conditional-mean skeleton of manuscript
`sections/05-geometry-counts.tex:12–36`, including its zero-atom convention.
It is **not** the signed-third-moment matching law.

The following decimal bounds are outward rational bounds, not floating estimates.
The actual column is a lower bound from one specified event; the skeleton
column bounds its entire two-sided Kolmogorov score.

| Law, index and raw threshold | Actual score at least | Skeleton score at most | Strict positive gap at least |
|---|---:|---:|---:|
| Y=-1,0,1 with weights 1/20,9/10,1/20; n=2,t=0 | 0.182239540166 | 0.180402292891 | 0.001837247275 |
| Y=-1,1/1000,1 with the same weights; n=2,t=1/500 | 0.182159555015 | 0.180402292891 | 0.001757262124 |
| X=-20,0,20 with weights 1/800,399/400,1/800; n=42,H=0 | 0.146244707299 | 0.123845652650 | 0.022399054649 |

The first law has v=1/10, r=1/10 and event probability 363/400.
The second has mu=9/10000 and the same event probability; after centering
none of its three atoms is zero, and p=19/20. Thus the failure is not an
artifact that requires assigning a zero atom to one class.
The last law is already centered and standardized, with rho=20, p=1/800.
By symmetry its closed discrepancy at zero is half its zero-sum atom:

\[
 \mathbb P(S_{42}=0)=
 \sum_{j=0}^{21}{42!\over j!^2(42-2j)!}
       (1/800)^{2j}(399/400)^{42-2j}.
\]

For the skeleton, with v_B=p(1-p), each of its n+1 sum atoms corresponds
to K=k for K~Bin(n,p). At that atom the two discrepancies are

\[
 \mathbb P(K\le k)-\Phi((k-np)/\sqrt{nv_B}),\qquad
 \Phi((k-np)/\sqrt{nv_B})-\mathbb P(K<k).
\]

Multiplication by `sqrt(n v_B)/(1-2 v_B)` gives the normalized score.
Between atoms the distribution function is constant and Phi is increasing;
therefore checking these two edges at every atom bounds the full supremum.
The exact checker does this, including both extreme atoms.

### Why this obstruction occurs at every fixed index

Let P_a have mass a at each of `+/-1/sqrt(2a)` and mass 1-2a at zero.
It has variance 1 and rho=(2a)^(-1/2). For each fixed n,
P_a^{*n}({0}) tends to 1 as a decreases to zero. Symmetry gives
Delta_n(P_a)<=1/2 and Delta_n(P_a)>=P_a^{*n}({0})/2, so Delta_n(P_a)->1/2.
For the sign skeleton p=a, the first standardized binomial atom is
`-sqrt(na/(1-a))`, tending to zero, and its mass `(1-a)^n` tends to one.
Below that atom the discrepancy is bounded by its normal CDF; above it,
absolute discrepancy is at most the larger of `1-P(K=0)` and
`1-Phi(-sqrt(na/(1-a)))`. These bounds and the closed first edge imply
Delta_n(B_a)->1/2. Since rho(B_a)~a^(-1/2),

\[
 \frac{C_n(P_a)}{C_n(B_a)}\longrightarrow\sqrt2>1.
\]

Thus an unconditional own-sign-skeleton theorem fails for every fixed n.
The explicit n=42 example supplies finite rational evidence without an
asymptotic threshold claim. None of these examples violates C_E. The n=42
law has rho=20 and |X|=20; the two n=2 laws have rho approximately sqrt(10).
They do not meet the acquired small-rho/bounded-support hypotheses of the
retained local packages. They cannot invalidate a correctly delimited local
comparison or justify deleting its hypotheses.

## 3. Normal enclosures and exact execution scope

`opus_exact_checks.py:14–31` uses integer square roots and the Machin identity
`pi=16 atan(1/5)-4 atan(1/239)`. The identity follows from tangent addition
and the angle range. Alternating arctangent partial sums enclose pi;
35-decimal rational square-root endpoints enclose every required radical.
For nonnegative rational x<=8, lines 34–55 integrate the odd/even Taylor
bounds for `exp(-t^2/2)`:

\[
 \sum_{k=0}^{159}{(-1)^k x^{2k+1}\over 2^k k!(2k+1)}
 \le \int_0^x e^{-t^2/2}\,dt
 \le
 \sum_{k=0}^{160}{(-1)^k x^{2k+1}\over 2^k k!(2k+1)}.
\]

Taylor's remainder has the stated sign for every nonnegative argument;
no small-argument or monotonic-term assumption is used. The checker asserts
positivity of the lower integral at each actual input. Negative x uses normal
symmetry; x>8 uses monotonicity and the trivial upper bound 1. Normal
monotonicity propagates the square-root intervals. All acceptance comparisons
are between `Fraction` values. Floating CDFs occur only in the separate
exploratory programs.

Lines 70–95 compute the skeleton upper and witness lower in the directions
required above; lines 97–105 enumerate exact multinomial event probabilities.
The three fixed cases and strict comparisons are at lines 108–124. This is a
bounded checker for these inputs, not a generic proof-object acceptance API.
It validates neither unrestricted optimization nor all analytic prerequisites
of existing certificates. Normal symmetry and a rational enclosure at 1 are
regression checks, not independent implementations. Reversing the established
comparison is rejected; the substantive adversarial control is the collision
example below.

## 4. A small location tolerance is not a small CDF error

Let epsilon=10^-12 and let raw Y have nodes `-1,1,1+epsilon` with weights
`1/2,1/4,1/4`. Then mu=epsilon/4. For n=2 the two middle centered sums are
`-epsilon/2` and `+epsilon/2`, each with probability 1/4. Standardizing by
its positive standard deviation preserves their signs and keeps their
magnitudes below 10^-10/2. The true centered/standardized CDF at zero is
1/2. Rounding both locations to zero makes it 3/4: an exact error of 1/4.

`opus_exact_checks.py:132–140` verifies the exact event probability. This
refutes interpreting `experiments.py:18–20` as an exact discrete law or as
having a CDF error of order 10^-10. It does not assert that this particular
rounding changes the *global maximum score* by 1/4; the maximum may occur
elsewhere, as the separate diagnostic demonstrates. A valid approximation
must preserve separate ordered atoms or prove a coupling/threshold-shift
bound, not silently identify near collisions.

## 5. Contact tests: a finite exact check is possible, but it is necessary only

The source expression in `contact_test.py:23–24` matches the manuscript
contact formula `sections/02-extremizers.tex:96–105`, after inserting the
candidate's actual positive closed score C, threshold H, rho and beta.
The manuscript theorem obtains I<=0 from **global attainment**
(lines 107–142); its logical implication cannot be reversed from sampled I.
Equality on closed support is a separate conclusion (lines 144–153).
For example, the symmetric Bernoulli law at n=2, H=0 has
C=sqrt(2)/4, rho=1, beta=0 and F=3/4. At y=1 its calibrated derivative is
`I(1)=2 phi(0)-1/sqrt(2)>0`, because pi<4. A correct contact test rejects
this nonstationary candidate despite its legitimate Bernoulli score.

There is a useful exact alternative to the 24,001-point y grid **for one
fixed finite law**, without promoting the test to a proof of optimality.
Let J be the finite set of jumps of `F_{n-1,P}(H-y)`, and assume C>0.
Set a=n phi(z)+3C beta and b=H phi(z)/2+3C rho/2. Between J and zero,
`rho I(y)` has the form

\[
 d+a y+b y^2-C|y|^3,
\]

where d is constant on that interval. Its derivative is
`a+2by-3C y^2` for y>0 and `a+2by+3C y^2` for y<0. Therefore its global
supremum is attained among zero, the *closed* jump values, and the at most
four real roots of these two quadratics that lie in their appropriate open
pieces. The cubic tends to minus infinity on both rays. At each jump the
CDF term drops as y increases, and the closed value is the larger, left
value, so no omitted right-hand limit can increase the supremum. Smooth
pieces have only their stationary points and endpoints as candidates.
For a Bernoulli law J has n points; this gives at most n+5 candidates
before coincident points are identified, and covers all real y.

This is a proved finite-candidate reduction conditional on knowing the exact
law and its calibrated parameters. It still needs rigorous root and normal
bounds, exact jump arithmetic, and treatment of parameters defined by an
optimizer. The attachment supplies none of those enclosures. Even a successful
continuum contact verification yields a first-order necessary condition; it
does not provide the missing concavity/global-comparison argument for
P -> P^{*n}. No converse theorem is established here.

## 6. What second variation could add

Fix a standardized P, fixed raw event A={S_n<=H}, and bounded real h with
`Eh=E[Xh]=E[X^2h]=0`. For sufficiently small positive and negative epsilon,
`dP_epsilon=(1+epsilon h)dP` is a probability law with the same first two
moments. Write `r=E[|X|^3 h]`, `D=F-Phi(H/sqrt(n))`. Then

\[
 F'_0=nE[h(X_1)1_A],\quad
 F''_0=n(n-1)E[h(X_1)h(X_2)1_A],\quad
 \rho_\epsilon=\rho+\epsilon r.
\]

These identities follow by multiplying the finite product densities; no
indicator is differentiated. At a maximizing pair the two-sided score
variation `G(epsilon)=sqrt(n)(F_epsilon-Phi)/rho_epsilon` has G'_0=0,
so `F'_0 rho=D r`. Direct quotient differentiation then cancels both
r-dependent terms and gives

\[
 G''_0={\sqrt n\over\rho}n(n-1)
       E[h(X_1)h(X_2)1_A]\le0.
\]

This is a genuine additional necessary condition with exact moment constraints,
not a universal sign inequality for arbitrary P. For r distinct fixed nodes,
the mass tangent space satisfying the three moment equations has dimension
r-3. It is zero for three nodes. Imposing absolute-third-moment preservation
as an extra constraint would unnecessarily remove another direction; the
cancellation above makes that restriction unnecessary at a stationary pair.
Location variations and new atoms remain outside this fixed-support test and
require separate treatment, especially at event collisions.

The bounded four-node control uses raw nodes `-3,-1,1,3`, uniform masses and
mass derivative `(-1,3,-3,1)`. It preserves moments 0,1,2 and the absolute
third moment, and is feasible for |epsilon|<1/12. At n=2,H=0 the event
polynomial is `5/8-10 epsilon^2`: F'=0 and F''=-20 exactly
(`opus_adversarial.py:49–55`). Standardization is constant along this line.
Thus this law is a strict maximum on its entire allowed moment line, while
its normalized score `5 sqrt(10)/112` is below the symmetric Bernoulli score
`sqrt(2)/4`. This explicitly shows why a successful fixed-moment curvature
test alone is not a global optimization certificate. It does not claim that
this four-node law also passes the full continuum contact inequalities.

## 7. Reproduction and what remains

All commands use the system Python 3.9.6, without `-O` or third-party packages:

```sh
python3 mathematics/strategy-v4/2026-10-27/opus_discovery.py
python3 mathematics/strategy-v4/2026-10-27/opus_exact_checks.py
python3 mathematics/strategy-v4/2026-10-27/opus_adversarial.py
```

Separate captured stdout, stderr, input hashes, interpreter/version, command,
return code and UTC timestamps are in `runs/strategy-v4-20261027/opus01/`.
The deterministic discovery covers 171 weight triples on raw {-1,0,1} at
n in {1,2,3,4,5,10,20,42}. It is a small screen, not a parameter cover. The
15 independent fixed controls include symmetric and skew Bernoulli, rational
p=419/1000 near p*, three/four-atom laws, exact/near collisions and a remote
atom at 1000 with mass 2*10^-12. All three bounded processes exited zero.
A short six-denominator diagnostic suggested the final n=42 witness; it was
not used for acceptance and is superseded by the preserved rational case.

The viable next analytic question is a contact- and resource-constrained
comparison on the exact acquired local domain, or a rigorous continuum contact
checker for a specified candidate. The supplied sampled tests do not establish
that all global maximizing laws belong to a tested finite family, do not bound
all remaining n, and do not justify any certificate deletion. A complete
second-variation exclusion would also need to cover every admissible law and
all relevant perturbations; the one-dimensional control above is not such a
cover.
