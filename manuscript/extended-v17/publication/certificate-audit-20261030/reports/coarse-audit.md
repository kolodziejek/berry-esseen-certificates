# Audit of the two coarse passes (Condition D.3)

Audited checkout: `work/manuscript_revision_20261029`, HEAD
`77d7b4b2510a6ce5b2d8e162bd2a78ecbecec1b5`.
Audit date: 30 October 2026. No pinned program or manuscript was modified.

## Conclusion and scope

**The numerical obligations in Condition D.3 freshly pass.** A separate rational
reconstruction also reproduces all non-Fourier coefficients and all 48 pass
states on the complete 24-cell cover. The displayed manuscript maxima and the
minimum gap margin are exact matches. I found no defect in the audited coarse
moment bounds, sign handling, circle inversion, endpoint maximization,
raw/resource ordering, or coverage.

The mathematical implication has the following explicit scope. Assume an
attained fixed-target contact pair with `a>=0`, `n>=42`, the acquired support
bound `|X|<=96/25`, `1<=rho<=7361/4000`, the contact conservation identity,
the physical-defect inequality, and a valid complete Fourier enclosure
`E_n <= K_F+s_F|H|` with the pairs computed by the selected kernel. Then the
two coarse passes establish their stated raw and resource bounds, and every
cell acquires an actual central support gap. This audit derives the
non-Fourier part of that implication. It does **not** independently establish
the Fourier enclosure, attainment/contact reduction, or initial support
acquisition. Those are separate analytic dependencies, not consequences of
the PASS status.

| Result | Mathematical status | Execution status |
|---|---|---|
| Literal D.3 numerical inequalities and complete 24-cell cover | Locally checked exact arithmetic proposition | Fresh PASS |
| Non-Fourier coefficient and two-pass correspondence | Locally derived and checked, conditional on the stated analytic inputs | Fresh independent rational reconstruction PASS |
| Full Fourier enclosure used as `K_F,s_F` | Separate analytic input; shared by the two calculations here | Gates executed, not independently proved by this reconstruction |
| Full entry/local/global theorem | Outside this bounded audit | No conclusion from this audit alone |

## Reproduction evidence

Command, from the audited checkout:

```sh
python3 /Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/certificate_discharge_20261030/coarse_reconstruction.py
```

The script refuses an existing output directory. For a later replay, select a
new output directory in a disposable copy rather than overwrite this evidence.
It invokes the unchanged selected two-pass checker, independently rebuilds the
non-Fourier quantities, and checks equality of every returned pass field that
it reconstructs. The Fourier pair is explicitly a shared input, so this is
not claimed as independent Fourier verification.

Evidence directory:
`runs/certificate_discharge_20261030/coarse/`.

- `receipt.json`: exact command, working directory, return code, output hashes.
- `summary.json`: Python 3.9.6, optimization level 0, source/input hashes,
  observed elapsed time 0.92470325 seconds, all summaries and control results.
- `selected.json`: the unchanged selected checker's complete 24-by-2 output.
- `reconstructed.json`: the independently reconstructed coefficient gates and
  all 48 pass states.
- Adjacent `coarse.stdout.log`, `coarse.stderr.log`: stdout and empty stderr.

The process returned 0. This is measured fresh evidence, not inherited logs.

| Pass | Maximum raw T | Maximum resource U | Maximum defect d | Cells with actual gap |
|---|---:|---:|---:|---:|
| 1 | 13.2818901598 | 10.9330610254 | 3.9164138937 | 23 |
| 2 | 11.5164967977 | 9.9790315907 | 3.5746638454 | 24 |

The exact minimum second-pass gap margin is
`526024602543/1600000000000 > 0`. The first-pass minimum is negative,
`-20775474737/1600000000000`, so the second pass is genuinely necessary for
the stated all-cell acquisition.

## Selected call graph and absence of hidden numerical premises

The selected driver is
`mathematics/fixed-target-v6/2026-10-27/signed-two-pass-check.py`, SHA256
`a2b9309998191c2d7e4477a969cd55ecb516440f56dfa3cf97df5ccddac1e76d`.

Its `run()` freshly invokes v5 `cell_check.run()` on the literal JSON and
pinned source bytes. It uses v6 `signed-check.signed_cap()` and
`moment_check.circle_lower()`. It does **not** invoke the six-update schedule
in `moment_check.run()`, nor `signed-check.main()` (which reads an older
output file). Thus that old output and the six-update schedule are not
premises of this selected path. The v5 checker also evaluates legacy
comparison diagnostics, but those do not feed the selected two passes.

The selected `one_pass()` retains minima with an old first-cover raw bound
and prior pass quantities. The manuscript states these extra minima are
inactive. This statement is freshly confirmed in all 48 states. It also has
an elementary reason: old `K` is at least the new `K`, and old `A` uses
`8u^3/27` where the new expression uses `u^3/4`, a decrease of `5u^3/108`.
The second pass only lowers `A` and raises the quadratic coefficient. Its
new raw bound decreases, its phase price increases, and its resource bound
therefore decreases as well. Upward rounding preserves this ordering.

## Mathematical correspondence

Manuscript anchors below are in
`manuscript/compact-v16/appendices/entry-details.tex`, unless specified
otherwise. They are stable TeX labels rather than PDF-dependent numbers.

### 1. Domain, moments, and the actual event

At `v9:entry:moments`, the positive measure
`dmu_0=(|X|-1)^2(|X|+1/2)dP` has mass `rho-1`. The exact polynomial
identities give the fourth- and fifth-moment ratios printed there.
Both ratios increase on `x>=0`; their derivatives are respectively
`1-1/[4(x+1/2)^2]>=0` and
`2x+3/2-3/[8(x+1/2)^2]>=0`.
Consequently the code's bounds

```text
M=min(Ru, 1+(R+1)^2/(R+1/2)*(u-1)),
eta5=min(RM, 1+(R^3+2R^2+3R+3/2)/(R+1/2)*(u-1))
```

are valid. The additional code cap `M<=11.1` is inactive throughout this
cover. Pearson's square `E(X^2-1-gamma X)^2>=0` and `|gamma|<=rho` give
`g=min(u,sqrt_upper(M-1))`; the code's additional `1.85` cap is also inactive.

The sign-moment inequality
`rho >= (1+beta^2)/sqrt(1-beta^2)` gives
`beta^2 <= (rho*sqrt(rho^2+8)-rho^2-2)/2`.
The right side increases with `rho` (equivalently, the original function
strictly increases with `|beta|`). Nested upward square roots give the
code's `b`; its direct squared gate verifies the resulting enclosure and
`0<=b<1` on every cell.

The event at `v9:entry:event` is the actual event
`{(X-X')^2>=9/25}` for independent copies of this same marginal. Cauchy
gives `P(E)>=(2-9/25)^2/(2M+6)`, and its conditional second moment is at
most `2/alpha`. These are exactly `event_a`, `event_m`, and `event_d0` in
the v5 rows. No arbitrary characteristic-function replacement is made in
this input construction.

### 2. Gap coefficient Gamma and the constant coefficient A

At `v9:entry:Gamma`, define

```text
F(v)=-v^2/4+(R+l)v/3-Rl/2+l^3(2R-l)/(12v^2).
```

This is exactly `v^-2 int_l^v (R-x)x(x-l) dx`. On each of 64 closed
subintervals, the code maximizes the concave quadratic at its clipped
vertex and the nonnegative decreasing reciprocal term at the left endpoint.
It takes the largest of these bounds and zero. This encloses the complete
continuous interval, including shared endpoints. The alternative `5/2`
ceiling follows from monotonicity of the positive integral in `R,l` and
the polynomial check at `R=6,l=1` described in the manuscript. Its interior
critical points are `(7+-sqrt(5))/2`; both critical values are positive.
Taking the smaller of two complete upper bounds is sound.

For the negative part of the gap charge, discard the nonpositive integrand
where `|t|<rho`, put `x=-t`, and enlarge the remaining expression using
`l<=rho` and the support radius R. Tonelli yields the bound
`3 Gamma E X_-^3 = (3/2)Gamma(rho-gamma)`. The positive part uses
`t(rho-t)<=rho^2/4` and contributes at most `3rho^2 J/8`.
This explains `v9:entry:coarse-gap-charge`, including a gap crossing zero.

The elementary gap identities at `v9:entry:gap-free` give
`-M4/6<=J1<=M4/2`, `-3J2-M5/4<=0`, and `J<=rho+1`.
The nonnegative square
`E[|X|^3(|X|-rho)^2]=M5-2rho M4+rho^3`
gives `rho M4/2-M5/4<=rho^3/4`.
Thus the code's `constant(row,difference)` is precisely the minimum of
the two complete bounds `A1(Delta),A2` at `v9:entry:coarse-A`.
Its domain check `0<=Delta<=2u` is necessary and passes everywhere.

### 3. The three coarse bounds for K1

The radial identity printed before `v9:entry:signed-K` reduces the
integrand to

```text
f_rho(x)=x+3(1-rho)/2+3(rho-1)/(4(x+1/2)).
```

It is convex in `x>=0` and decreases in `rho`. Its positive part is
therefore bounded by the displayed endpoint value at `(R,l)`. Since
`rho<=37/20`, its negative part is at most `31/40`: indeed
`f_rho(x)+31/40 >= (x^2+31/80)/(x+1/2)>0`.
The code checks that its positive endpoint ceiling dominates `31/40`.
Integration against the positive measure of mass `rho-1`, plus the
`3rho|beta|` term, gives `K_rad`.

For `K_univ`, `||X|-3|<=3` on the acquired support gives
`|E[X|X|^3]-3gamma|<=3rho`. The remaining coefficient
`3-3rho/2` is nonnegative for `rho<=2`. The resulting
`6rho-3rho^2/2+3b` increases throughout the domain, so evaluation at u
is justified.

For `K_R`, use `0<=E X_+^4<=R(rho+gamma)/2` and
`0<=E X_-^4<=R(rho-gamma)/2`. Their difference gives
`|E[X|X|^3]-3rho gamma/2| <= Rrho/2+|R/2-3rho/2||gamma|`.
The absolute affine factor takes its maximum at an endpoint of `[l,u]`.
These are exactly the three alternatives in v5 `cell_check.py`.

### 4. The stronger signed K bound

This part was rederived without assuming signs for `beta*gamma` or
`K1*gamma`. For either `epsilon=+-1`, put
`h=1-epsilon beta>0`, `delta=rho-epsilon gamma`.
Signwise Cauchy and `m<=1/2` imply `delta>=h^2`.
An upper fourth-moment bound on one sign and the Cauchy lower bound on
the other give exactly

```text
epsilon K1 <= Rrho-3rho^2/2-3+3h+a(rho)delta-delta^2/(2h),
a(rho)=(3rho-R)/2.
```

Unconstrained maximization in delta yields `3h+h*a(rho)^2/2`, which
increases in h. Set `h*=1+b`. The resulting quadratic in rho is the
code's `unconstrained_cap`; endpoints plus an interior concave vertex
give its complete maximum.

With `delta>=h^2`, the piecewise maximum is the manuscript's `psi_a(h)`.
On its second branch, `d psi/dh=3+2ah-3h^2/2` is concave in h. The
code checks its value at h* with the smallest a, while its value at zero
is 3. Together with `h*>=a(u)`, this licenses substitution h=h*.
The final derivative in rho is `R-3rho+3h*^2/2`; the third code gate
licenses substitution rho=u. These exact three gates are reproduced
independently. Failed gates simply omit this optional stronger bound.

### 5. Normal coefficient and first quadratic pass

The gap-free J1 bounds imply
`Omega in [-1/2,2M4/3-1/2]`, hence
`|phi_z Omega| <= (2/5)max(1/2,2M/3-1/2)=v_H`.
The v5 code also retains an older alternative for v_H, but it is strictly
larger on every cell. Analytically, `M<=Ru=3.84u` bounds the displayed
v_H by `max(.2,1.024u-.2)`, whereas the other alternative is at least
`1.2(u+1)`. Thus the manuscript and actual code agree.

For the raw remainder formula `v9:core:R`, the first curvature lower
bound is `q(c)=cl-g/5`, because `phi_z<=2/5` and `gamma>=-g`.
The linear coefficient is `f(c)=cK+v_H+s_F>=0`, and the constant is
`K_F+cA`. For fixed `|H|`, the resulting quadratic is affine in c.
Maximize at the two c endpoints before completing its square. This gives
exactly `max(K_F+cA+f(c)^2/(4q(c)))`, with strict `q>0` checked first.

The raw gate `0<=T<Nc_-l` is checked before using it to infer a density
bound or phase price. Corollary `v9:core:phase-price` in
`sections/03-conservation.tex` then gives
`U<=R_c-eta H^2`, `eta=(c_-l-T/N)/2>0`.
Completing squares with `q+eta` gives the resource ceiling U. Since
`n phi(0)D/6<=U`, the rounded `d>=6U/(N phi_l)` gives `nD<=Nd`, hence
`D<=d` for every actual `n>=N`. It is the raw T, never U, that licenses
the density and phase corrections.

### 6. Circle inversion and the second quadratic pass

The moment circle and gap inequality yield
`D>=sqrt(10)rho-gamma-3sqrt(rho^2-gamma^2)`.
For `y=gamma/rho`, this requires
`y+3sqrt(1-y^2)>=sigma_l-d/l=a0`.
On `[-1,1/sqrt(10)]`, the left side increases from -1 to sqrt(10).
For `a0>-1`, its lower root is
`(a0-3sqrt(10-a0^2))/10`; for `a0<=-1`, retain the full lower endpoint -1.
Since `a0<=sigma_l<sqrt(10)`, the radical is in domain on the nontrivial
branch. Taking its square root upward gives a lower bound for y. If this
bound is negative, multiply by u; if nonnegative, multiply by l. The
code does exactly this and rounds downward afterward.

The further bound `gamma>=sigma_l*l-3-d` follows from `J<=rho+1`.
Intersecting these bounds with `gamma>=-g` gives the code's `gamma`.
The corresponding upper bounds on `rho-gamma` are `2u`,
`(1-sigma_l)l+3+d`, and `u-gamma_lower`; their minimum gives Delta.
An inconsistent gamma interval raises an error rather than silently
discarding a cell.

The licensed density lower bound is
`phi_-=phi_l(1-T/(Nc_-l))>0`. For all signs of `gamma_lower`,
`gamma phi_z>=min(phi_- gamma_lower,(2/5)gamma_lower)`.
This proves the second curvature alternative in the code. Its alternatives
have the same slope l in c, so their maximum is still affine in c.
The same endpoint/square-completion argument applies. Raw contraction
is established first, then the new phase price, then resource and defect
contraction. All quantities are associated with the same rho cell.

Finally, if zero belongs to the closed support, `J<=rho` and
`D>=(sqrt(10)-1)rho`. Every second-pass cell satisfies the strict
inequality `d<(sigma_l-1)l`, contradicting that consequence. Centering
and positive variance then give nonempty support on each side of zero,
so an actual central gap exists. No artificial Bernoulli event is inferred.

## Exact arithmetic, coverage, and negative controls

The selected code uses Python integer/Fraction arithmetic, integer square
roots with checked enclosure inequalities, and exact integer ceiling/floor
operations. All square-root enclosures used for coefficients are outward;
the inverse-circle expression uses the opposite sign of the upper square
root, followed by downward rounding. Decimal displays are rational ceilings,
not binary floating-point acceptances. Float arithmetic in the audit is used
only for elapsed-time metadata.

The 24 cells have literal endpoints `1+3361 i/96000`, `i=0,...,24`.
Their order, count, and both endpoints are checked exactly. Adjacent cells
overlap at their shared endpoint. The complete enclosing interval includes
the strict acquired rho domain. Both c endpoints and either sign of H are
covered by the affine and absolute-value arguments, not by sampling.
The original Fourier code checks N=42 and its all-index gates; the proof
that those gates imply an enclosure for every actual n remains part of
the separate Fourier audit.

The unchanged selected run rejects seven negative controls: missing,
duplicated, and reordered cells; broken shared endpoint; an unlicensed prior
raw bound; a false first-pass all-gap claim; and an understated final defect
target 3.5. Additional fresh controls exercise negative defect, reversed
rho interval, out-of-domain inverse, negative radicand, the wrong inverse
branch, and fabricated moments violating the circle. A rational actual law
with `beta>0,gamma<0` is also checked, so the audit does not rely on a false
same-sign assumption. These controls check implementation behavior; they
do not replace the continuous-domain arguments above.

## Remaining dependencies and safe manuscript action

This audit supports changing D.3's **finite arithmetic status** from an
unexecuted condition to a reproduced certificate theorem, provided the
coordinating audit verifies its complete Fourier input and preserves the
explicit upstream hypotheses. A precise proof can cite the selected source
hash, fresh receipt, exact cover, and the coefficient correspondence above.
It should not cite the PASS label as a proof of an analytic reduction.

Dependencies that this report does not discharge are:

1. The fixed-target attainment/contact theorem and the initial support
   theorem (including its external structural inequality).
2. The complete compensated LOW/HIGH Fourier bounds and their all-n
   monotonicity/gate correspondence. Their values are deliberately shared
   inputs to the independent reconstruction here.
3. The conservation identity itself; the use of its phase-price corollary
   has been checked, not its entire prior derivation.
4. The four signed passes (D.5), local comparison and finite base through
   699. A successful D.3 replay does not remove any of these hypotheses.

No claim about the full sharp iid conjecture, an unconditional all-n result,
or an independently verified finite base follows from this bounded audit.
