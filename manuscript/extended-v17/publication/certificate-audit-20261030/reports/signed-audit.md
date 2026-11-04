# Signed entry audit: Condition D.5

Date: 30 October 2026. Reviewed checkout:
`work/manuscript_revision_20261029`, commit
`77d7b4b2510a6ce5b2d8e162bd2a78ecbecec1b5`.
No manuscript, retained proof object, or pinned acceptance source was changed.

## Conclusion and scope

I found no defect in the signed-stage translation of Appendix D to
`mathematics/fixed-target-v7/2026-10-27/signed_core.py` and
`accept_entry.py`. The delicate sign choices, zero denominators, independent
gamma slices, actual opposite-sign event, and closed-panel intersections have
valid necessary-condition interpretations. This is an audit of the signed
transition, not an independent proof of the contact/conservation theorem,
support theorem, coarse ancestor, or Fourier theorem.

The signed transition can discharge Condition D.5 once the coordinator has
combined (i) fresh exact replay of its fixed object, (ii) the coarse Condition
D.3 audit, (iii) the support/contact and Fourier premises, and (iv) this
code-to-mathematics correspondence. A generic `PASS` alone is insufficient:
the acceptor's hard numerical targets are weaker than the manuscript's
reported maxima. The independent exact check below verifies the sharper
fixed-object targets explicitly.

| Result | Mathematical status | Execution status |
|---|---|---|
| Signed moment and gap enclosure transition | Locally derived and checked, under the specified incoming contact, support, Fourier, raw and weighted-defect invariants | Source audited; complete replay belongs to coordinator's retained-entry run |
| Printed D.5 constants and census from the fixed JSON object | Exact arithmetic checked; actual enclosure requires successful replay and the transition proof | Fresh PASS |
| Delicate product signs, shared endpoints and zero-denominator cases | Proved below, with independent rational diagnostics | Fresh PASS |
| Contact existence, compactness, initial support, all-index Fourier estimates, and D.3 ancestor | Inputs to this bounded audit, not established by its diagnostic program | Separate audits/runs required |
| Independent finite base / full sharp iid conjecture | Not proved here | Not attempted here |

## Fresh independent evidence

The diagnostic program imports only Python's standard library and does not
import any retained acceptance kernel:

`runs/certificate_discharge_20261030/signed/independent_semantics.py`.

Its stdout, stderr and run metadata are respectively
`independent.stdout.json`, `independent.stderr.txt`, and `independent.meta.json`
in that directory. Python 3.12.12 ran without optimization; exit status was 0.
The object SHA-256 is
`61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae`.

The check obtains:

| Quantity | Exact checked value |
|---|---:|
| Maximum final raw ceiling | `10997587/5000000` = 2.1995174 |
| Maximum final D ceiling | `76682509/100000000` = 0.76682509 |
| Weighted nD ceiling | `1610332689/50000000` = 32.20665378 |
| Maximum surviving original rho endpoint | `71527/48000` |
| Maximum beta ceiling | `50549963/100000000` = 0.50549963 |
| Maximum phase ceiling | `2295071/1250000` = 1.83605680 |
| Maximum final support radius | `157/50` |
| Processed rho rows per pass | 24, 24, 24, 16 |
| Surviving rho rows per pass | 24, 24, 16, 14 |
| Nominal signed boxes | `(24+24+24+16)*128 = 11264` |
| Nonempty probability panels | 30 of 100 |
| Stored final panel incidences | 7235 |

All nonempty panels satisfy the stated resource, beta and phase ceilings.
The exact rho bound needs a small but important explanation: the JSON panel
maximum is `18626823/12500000 = 1.49014584`, because panel coordinates are
rounded upward to 1e-8. That number is slightly larger than `71527/48000`.
The sharper theorem bound follows from the identities of the surviving
original rho rows (indices 0 through 13) and their exact closed right endpoints
`1 + 3361*(i+1)/96000`. Thus the printed rho bound is justified by the original
cover, not by comparing it directly with the rounded JSON panel field.

The support conclusion is open, `supp P subset (-157/50,157/50)`, only because
the support theorem excludes the entire closed outer rays starting at each
selected radius. The JSON maximum by itself would establish only a radius
value, not strict exclusion of its endpoints.

## Audited dependency edges

### 1. Already proved support enters before higher moments

`accept_entry.py:113–116` independently recomputes `cell_radius(rho_upper)`,
requires equality with the stored radius, and passes it into the stage.
`signed_core.py:21–28` sets `kernel.RADIUS`, recomputes K4 and K5, and calls
the exact constant checks before evaluating any moment or Fourier bound.
There is no stale radius left from a different rho cell. The support helper
checks the heat/ray expressions A, h4, Q, Q', Q'', L, L', L'' and P with
strict inequalities. Their implication from the contact law is a separate
analytic premise; this audit does not infer it from their being negative.

### 2. Sign moments, beta coverage and common first moment

Write `a_s=E X_s^2`, `b_s=E X_s^3`, and
`m=E X_+=E X_-`. Cauchy gives
`a_s^2 <= m b_s` and `m^2 <= a_+ a_-`. These imply the displayed gamma
enclosure and `m >= (1+beta^2)/(2rho)`. Combining the latter with
`2m <= sqrt(1-beta^2)` gives the beta inversion used by the code:

`beta^2 <= (rho*sqrt(rho^2+8)-rho^2-2)/2`.

Its upper endpoint is outward, using upper roots and the upper rho endpoint.
The signwise gamma functions are increasing in beta on (-1,1), so their
chosen beta endpoints and downward roots have the required directions.
The fourth-moment projection follows by minimizing
`E(X|X|-uX-v|X|)^2`; the Gram matrix is positive definite because `|beta|<1`.
The implementation uses all corners of `gamma-rho*beta`, the distance of
this interval from zero, and the upper denominator `1-min|beta|^2`.

The compulsory mean `max(0,(sigma_l*rho_l-gamma_u-d)/6)` is applied separately
on each gamma cell. Lines 51–54 explicitly save the original beta interval
and restore it before every gamma subdivision; dependent semimoments are
recomputed after intersection. A contraction in one gamma slice therefore
cannot remove a law in another slice.

### 3. Localizing matrices and degenerate denominators

On each sign the PSD matrix with weight `(R-|X|)` gives

`(R p_s-m)(R a_s-b_s) >= (R m-a_s)^2`.

Summing gives the first-moment necessary inequality in the manuscript,
with `p_++p_- <= 1` also allowing a zero atom. Extra factors `|X|` and
`|X|^2` give respectively

`(R m-a_s)(R b_s-c_s) >= (R a_s-b_s)^2`,

`(R a_s-b_s)(R c_s-f_s) >= (R b_s-c_s)^2`.

The interval denominators DU and denm are upper bounds for the true
nonnegative denominators; DL is a nonnegative lower numerator bound.
Consequently subtracting `DL^2/denm` gives an upper moment enclosure.
A negative upper denominator, or zero upper denominator with strictly
positive lower numerator, contradicts the PSD inequality. A zero/zero
correction is dropped. For the first- and fifth-moment estimates the code
also harmlessly drops a correction when its upper denominator is zero.
It never divides before this case distinction.

The bisection function replaces each actual correction by
`max(0,Rt-a_upper)^2/DU`; it is nondecreasing for `t>=0` and is a lower
bound for the necessary expression at any actual `m>=t`. A value above R
therefore excludes that t and all larger values. The code keeps the upper
bisection endpoint and rounds it upward, so this operation preserves all
possible means. Negative rounded means cannot arise because the explicit
rounded-mean domain gate rejects them.

### 4. Actual event and conditional moment

This edge requires the incoming D.3 strict gap inequality. It first excludes
an atom at zero and supplies actual support endpoints `-A<0<B`; it is not
a moment-realizability assertion. Then `p=P(X>0)`, `q=1-p`, Cauchy gives
the code's p interval, and variance decomposition gives `pq>=m^2`.
Thus both lower bounds used for the event probability `2pq` are valid.
The first is `(1+beta^2)^2/(2rho^2)`, and the second minimizes the concave
function `2p(1-p)` at the p endpoints. Their maximum is still a lower bound.

The gap decomposition gives
`T<=D/(sigma-1)` and `6mAB>=(sigma-1)rho-D`, hence the code's lower bound
for `(A+B)^2`. It divides a lower numerator by an upper m endpoint and
takes a downward square root. The exact conditional second moment is

`(1+4m^2+beta)/(2p) + (1+4m^2-beta)/(2(1-p))`.

Its numerators are positive on `|beta|<1`; it increases with m, is affine
in beta and convex in p. The chosen corner maximum is an upper bound.
The independent bound `2/alpha` is also valid because
`E(X-X')^2=2`. Their minimum is valid. These values enter one complete
HIGH evaluation; its minimum with the complete universal-event evaluation
does not mix terms from incompatible events. The all-index HIGH theorem
and its analytic gates are covered by the Fourier audit.

### 5. Central and outer integral costs

The endpoint lower bound is the positive root of a downward quadratic
lying below the actual necessary endpoint expression. Positive
coefficients use lower endpoints, the negative quadratic coefficient uses
the upper endpoint, and the root is rounded down. The lower bound for
`Q=(sqrt(sigma+1)A-sqrt(sigma-1)B)^2` is the squared distance of zero from
an outward interval. The remaining outer budget is `d-m_lower*Q_lower`,
not d alone.

For the central charge, maximizing first in B gives the displayed G(A,rho).
Its derivative in A is `(rho-A)^2(rho+2A)/6>=0`; its second derivative in
rho is `rho^2+rho*A>=0`. Also G is nonnegative since G(0,rho)>0 and it
increases in A. Thus multiplication by the upper m endpoint is valid.
The outer charge is bounded both by the weighted residual budget and by
the separate T-plus/T-minus ceilings. The code takes the minimum of two
complete valid bounds.

For `P1(A,B)=B^3/3+AB^2/2-A^3/6`, its B derivative is `B(A+B)>=0`;
its A derivative is `(B^2-A^2)/2`, and it is concave in A. The minimum is
therefore at B_lower and an A endpoint; the maximum is at B_upper with
A clipped to B_upper. Multiplication by m must change endpoint when P1
is negative, exactly as lines 132–133 do. In the exact binary example
`A=3/2, B=2/3`, P1 is `-169/1296`; blindly multiplying its upper bound by
m_upper would give a false upper product. The diagnostic checks this
negative control and 2916 rational product samples. The derivative argument,
not the samples, establishes the continuous rectangle bound.

### 6. Signed coefficients and ordered feedback

The beta charge is maximized over the full beta/J/gamma rectangle. The
signed rho*gamma product uses both its minimum and maximum as required.
The K1 interval intersects valid fourth-semimoment bounds. The three
fifth-moment losses follow separately from square completion/projection,
signwise Cauchy, and weighted Cauchy; the code subtracts their maximum,
not their sum. Each denominator is replaced in the direction appropriate
for a lower loss.

The signed rectangle maximum `|c K1+phi Omega|` retains the common density
factor and handles negative lower gamma by the upper density endpoint.
The incoming raw gate licenses the density lower bound. The new raw bound
is completed first and intersects the old raw bound; only then is the new
positive phase price formed. The resource square uses that price, and
`15000/(997*N)=6/(N*phi_l)` updates the weighted invariant `nD<=N d`.
The actual sample size is not set equal to 42. For c between its two
endpoints the unreduced quadratic is convex in c at each fixed |H|, so
the endpoint maxima are valid even when the constant A is negative.
The phase root uses `max(0,B)` and an upward square root, enlarging the
allowed root whenever necessary.

### 7. Closed coverage and acceptance

Each closed rho/beta/gamma/m rectangle is subdivided without holes.
Inconsistent outer cells count every descendant. Cardinality alone is not
a proof of coverage, but here it accompanies explicit closed subdivision
and valid necessary exclusions. `accept_entry.py` checks original row
identities/endpoints, four passes, persistence of excluded rows, each
128-leaf census, and monotone outward scalar ceilings. The final panel
incidence count is checked against recomputation.

At lines 161–162 an intersection is skipped only when lower>upper.
Singleton intersections are retained, including both neighbors of a shared
panel boundary. The diagnostic interval `{1/2}` belongs to panels 49 and
50; the deliberately wrong strict intersection loses both. The p-variance
maximum includes 1/4 exactly when the closed intersection contains 1/2.
It is positive because actual p intervals lie strictly inside (0,1).
This yields the correct upper theta bound from the lower m endpoint.

## Remaining obligations and recommended manuscript change

There is no newly found signed-stage defect to repair. Preserve all pinned
objects and checker semantics. If the companion coarse, support and Fourier
audits and the full replay succeed, Condition D.5 can be replaced by an
exact-verification proposition citing the object hash and reproducible run.
Its proof should retain the preceding analytic enclosure and coverage
argument. Add one sentence explaining that the exact rho endpoint comes
from the surviving original rows, since the panel serialization rounds it
upward. Keep the strict support conclusion tied to the whole-ray support
theorem.

This conclusion does not eliminate an independent finite-base hypothesis,
prove compactness or existence of a contact witness, or establish any
unexamined analytic premise. An unconditional downstream theorem is
warranted only after the coordinator checks every edge in that theorem's
dependency graph, rather than treating this bounded audit or agent agreement
as an independent theorem.
