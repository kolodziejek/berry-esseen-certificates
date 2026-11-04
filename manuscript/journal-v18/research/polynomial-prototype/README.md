# Five exact polynomial objects: shortening feasibility demonstration

This is a **demonstration only**, outside the current manuscript dependency graph. It does not replace any analytic proof or accepted numerical object, and it establishes no Berry–Esseen theorem by itself. The current manuscript retains the corresponding derivations.

The proposed saving is modest: a manuscript could state these explicit identities and their mathematical consequences once, while distributing their expansion checks as declarative rational objects. This prototype shows how to make that step precise; it does not claim that the resulting presentation would necessarily be shorter or clearer than the elementary displayed factorizations.

## Fixed scope and schema

`proof_objects.json` contains exactly five ordered cases: conditional3, conditional4, conditional5, radial4 and radial5. Extra, missing, duplicate or reordered cases reject. The format, scope and variable order `[x,a]` are fixed. Every polynomial is an ordered list `[exponent_x, exponent_a, rational_string]`, with unique nonnegative integer exponent pairs and canonical nonzero rational coefficients. Unknown fields, duplicate JSON keys, floating-point coefficients and noncanonical fractions reject.

The conditional cases supply only a quotient Q_j. The radial cases supply N_j, its derivative numerator and its moment difference. The checker reconstructs each target from its fixed mathematical case, rather than trusting a submitted target or success flag. Its sparse polynomial ring uses only Python integers and `Fraction`, without a symbolic algebra system. It checks coefficient identities, not point evaluations.

## Soundness of the five cases

For j=3,4,5 the accepted coefficient identity is

`x^j-a^j-j*a^(j-1)*(x-a) = (x-a)^2 Q_j(x,a)`.

Every coefficient of Q_j is positive and every exponent nonnegative. Thus Q_j>=0 and is coordinatewise nondecreasing for x,a>=0. In particular, if0<=x<=R and0<=a<=v, then Q_j(x,a)<=Q_j(R,v). The displayed polynomials are Q3=x+2a, Q4=x²+2ax+3a², Q5=x³+2ax²+3a²x+4a³. At x=a the polynomial identity still holds; no division is used. For a conditional sign class, a=E[x|class], so the linear term has conditional expectation zero. Since W²=(x-a)² on either class, integration yields the conditional moment identity used in `j:local:re:conditional`. The analytic conditional-expectation step and bounded-moment assumptions remain in the manuscript.

For j=4,5, the denominator is d(x)=x+1/2>0 on x>=0. The checker fixes N4=(x+1)² and N5=x³+2x²+3x+3/2, and checks

`d N4' - N4 = x²+x`,

`d N5' - N5 = 2x³+(7/2)x²+2x`.

Their coefficients are nonnegative, so (N_j/d)' is nonnegative on the entire half-line; its denominator is d²>0. This proves the radial quotient monotonicity without a finite mesh or a tail truncation. The additional factor identities checked are

`(x-1)^2 N_j(x) = x^j-(j/2)x²+j/2-1`.

For x=|X| and E x²=1, their expectations are M_j-1. The positive measure dmu=(x-1)²(x+1/2)dP has mass rho-1. Hence under x<=R, M_j<=1+[N_j(R)/(R+1/2)](rho-1). This expectation argument is analytical and is not replaced by the coefficient checker.

## Acceptance and evidence

Run the physical unoptimized Python interpreter with `-I -B`; do not use `-O`. The acceptance command is

```
python3.12 -I -B check_polynomial_objects.py proof_objects.json
```

The independent control driver makes23 corrupt copies in a new disposable directory, including one corrupt polynomial in each of the five cases and corruption of each radial field. It also tests missing, duplicated and reordered cases and duplicate JSON keys. The supplied object is never rewritten.

The fresh process captures, complete stdout/stderr, executable/source/input identities and mutation files are under `runs/journal_v18_20261104/prototype01`. These bounded checks are separate from the complete native numerical executions supporting the existing manuscript.

For this published copy, those same records are included in [`evidence/`](evidence/). Their recorded paths identify the original run; the checker and capture driver use paths relative to their own location and can be run from this directory. This explanatory addition changes only this README, not the checker, input, control driver or preserved run records.

## Limits of this approach

Only finitely many polynomial equalities have been moved into data. Compactness, contact, conditional expectation, Fourier inversion, uniform tails and domain coverage remain mathematical proofs. This small checker would become a new trusted component if its output were ever promoted into the manuscript dependency graph; such promotion is neither performed nor implied here. For these elementary examples, keeping their one-line factorizations may remain the most readable choice. The prototype is a precise option for future repeated algebra, not a requirement to certificate every calculation.
