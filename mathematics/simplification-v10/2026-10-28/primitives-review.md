# Elementary primitives: independent derivation and bounded checks

Worktree: `primitives-v10`, branch `research/primitives-v10-20261028`,
starting at `00ba714897f2e09995d78354ac3c8931e257cd05`. This component adds
only new research proofs/checks and their evidence. The current manuscript,
old certificates and old acceptance programs are unchanged.

## Results and exact dependency removals

| Result | Mathematical status | Execution status |
|---|---|---|
| Combined fifth-moment bound | Independently derived for every centered variance-one law with finite fifth moment; zero atoms allowed | Exact controls on 56 actual laws; 41 strict improvements over the old three-way maximum |
| Closed first-moment bound | Independently derived PSD root, including R=rho, R=1 and monotonicity on parameter rectangles | Exact determinant, discriminant, root and all 11 old auxiliary comparisons checked on every fixture |
| Cosine constant 4553/1000 | Complete calculus proof on [0,1], with rational Taylor/Machin checks | Exact six-term derivative lower bound >.000015 and final constant margin >.0001 |
| Common sign-size-biased transfer | Independently derived for all n>=1 with finite third moment, without bounded support; explicit zero-defect and zero-atom treatment | 672 exact polynomial coefficient identities, 14 zero-defect fixtures and 252 complex power-remainder cases |
| Uniform finite-base witness box | Locally proved implication conditional on the explicitly stated universal affine structural inequality and fixed-target maximizing contact; no predecessor | Exact target/density/contact-ray/threshold constants checked; no finite-base acceptance |

The proofs are all in `primitives.tex`; the six-page `primitives.pdf` was
compiled and visually inspected. `primitives_check.py` imports no inherited
mathematical kernels or discovery code. Exact arithmetic checks finite
identities and fixed fixtures; the written arguments establish generality.

### One loss instead of three

The old source `manuscript/arxiv-v1/sections/04-fixed-entry.tex:569` takes
the maximum of a signed loss, a quartic loss and a full weighted loss.
Proposition1 here proves

`rho M4/2 - M5/4 <= rho^3/4 - P_sign - delta^2/(16m)`.

Its proof splits the underlying square by sign. Weighted Cauchy gives
`V_s>=d_s^2/m` on each sign. On the sign where `d_s>=0`, log-convexity of
the moments yields the stronger `V_s>=b_s d_s^2/a_s^2`. The new extra term
belongs to the other sign, so it may be added without charging one square
twice. The new loss dominates all three former losses. Their separate
proofs and maximum-selection expression are therefore unnecessary if this
new inequality is used. Signwise matrix constraints unrelated to those
three losses remain necessary inputs where used.

A tempting stronger sum is false: the explicitly displayed rational
four-atom law violates `P_sign+delta^2/(8m)` by more than .0267, while the
correct combined inequality has margin greater than .0201. This is a
counterexample to an intermediate bound, not to Berry–Esseen.

### One determinant instead of eleven auxiliary values

The old source at `sections/04-fixed-entry.tex:561` applies the same
nonnegative cubic at eleven positive auxiliary values. Proposition2 solves
the equivalent two-by-two PSD determinant and proves that its upper root
equals the infimum over every positive auxiliary value. This is a genuine
analytic optimization, including its limiting boundary cases.

The upper root increases with R and decreases with rho. A cell may use
`U(R_upper,rho_lower)`, with an outward square root, and this bound is no
larger than any of the old eleven values at the same endpoints. There is
no need to search for an auxiliary parameter. The stronger signwise PSD
information and other row-cover obligations are not eliminated.

### One scalar calculus argument instead of 976 coefficients

Proposition3 finds the unique maximizer through
`tan(y*/2)=y*`. Six terms show `y*>23311/10000`; then the decreasing
function `y/(1+y^2)` and `pi<355/113` give the stronger working constant
4553/1000. Machin's formula with 8 and 2 arctangent terms supplies the
directed pi interval. This replaces both old Bernstein positivity
certificates (80+896 coefficients), while preserving the stronger constant.

The scalar inequality alone does not widen a harmonic span or count
normalization domain. At x=3/8 the value `(8+4sqrt(2))/3` disproves K=9/2;
the checker verifies this negative control with rational squares.

### One transfer formula for all n

Proposition4 represents the same original law through its two sign-size-biased
measures. The defect is the sum of their variances, multiplied by m.
The function `(exp(i sign t y)-1)/y` has a continuous integral representation
and a second derivative bounded by |t|^3/3. Taylor's formula gives the
original-law response without dividing by a defect or omitting contact
atoms. The same two measures work at every frequency. The full iid power
remainder follows from the unit disk, for every integer n>=1.

This simplifies only the scalar defect/response/remainder mechanism in
`appendices/original-law-four.tex:1–95` and its n=4 power extension. It does
not reproduce the stronger mass radius, signed Fourier prices or the
genuine whole-cell bounds needed by that finite-base route. Those may not
be deleted merely because the simpler modulus estimate exists.

In particular Q may have three atoms. Neither the Bernoulli theorem nor
the modulus estimate proves a finite-base inequality for Q or P. The
coefficient 1/6 in the modulus bound is sharp: a fixed rational four-atom
law has a one-sign defect, and an explicit fourth-order remainder disproves
the proposed coefficient1/7 at a specified nonzero rational frequency.

### One finite-index compact domain

Proposition6 uses the existing fixed-target contact calculation directly,
without any predecessor. The external affine structural bound first gives
rho<7361/4000. For 1<=n<=41, the support contact is at most

`P(u)=266.5+1.944715 u^2+17.63 u-.4095 u^3`, for u>=1.

P and its first two derivatives are strictly negative at13, and P'''<0.
This proves support strictly inside(-13,13). Chebyshev on the negative
threshold side and the same second-moment estimate for the normal tail
on the positive side give |H|<26. The n=1 contamination formula uses the
deterministic deleted sum S0=0; the attainment proof also extends to n=1.

This is one bounded problem for a future finite-base argument. It does
not prove any new finite row by itself, and it need not be numerically
sharper than separately proved support bounds for particular indices.
The all-n structural input is kept explicit and is not proved here.

## Checks actually performed

The final checker uses exact `fractions.Fraction` arithmetic. The actual-law
fixtures comprise symmetric and skew Bernoulli laws, zero atoms, reflected
laws, rational mixtures with weight10^-8, and distant atoms of size20.
Every law is checked to have total mass one, mean zero and variance one.
The scalar proof controls all real x analytically; no sampled trigonometric
positivity claim is used. The characteristic-function proof likewise uses
Taylor's integral remainder; moment coefficient checks do not masquerade
as a continuous Fourier certificate.

Negative controls verify:

1. the false sum of the full weighted fifth-moment loss and signed loss;
2. the false cosine constant9/2;
3. the false characteristic coefficient1/7, with an explicit rational
   frequency and a rigorous fourth-moment remainder;
4. a missing factor in the n=2 power remainder.

Execution evidence is under `runs/primitives-v10-20261028/`.
`check01` records the initial four primitives on Python3.9.6. `check02`
adds the conditional finite-base box on Python3.12.14. `check03` records
the final script and proof bytes. The later check changes only the report's
scope wording; numerical targets and inequalities are unchanged.
`build02` preserves two layout warnings; these were repaired by splitting
two displays. `build03` is the clean six-page build; all six rendered pages
were inspected and no clipping or overlap was found. Compilation is a
document check, not proof acceptance.

Reproduce the bounded arithmetic from the repository root:

```sh
python3 -I -B mathematics/simplification-v10/2026-10-28/primitives_check.py
```

The recommendation is to adopt these analytic replacements at the named
edges, with an independent review of this derivation. They need no dense
generation campaign. The full entry/count/finite-base composition and any
changed interval enclosures remain separate obligations.
