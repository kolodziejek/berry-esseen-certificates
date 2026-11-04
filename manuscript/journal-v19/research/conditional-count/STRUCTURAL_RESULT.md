# Conditional-count consolidation: proved lemma and bounded obstruction

## Result and recommendation

The nearest-count and whole-count witnesses are two upper bounds for the **same scalar binomial increment**. The lemma below is fully proved and preserves the actual iid marginal, every phase sign, and the strict outgoing/closed incoming convention at atoms. It provides a more conceptual explanation of their relationship.

It does **not** remove the separate estimates of those bounds. The current manuscript already shares the score identity, normalization, and moment inputs. Replacing its two short scalar tests by the generic test below would probably save no pages. Replacing the binomial-curvature explanation by the degree-elevation identity below could improve readability with essentially neutral length. No large shortening is established by this investigation.

A second, exact result explains one limit of the proposed unification: the own-count law, conditional variances, and the first four ordinary moments plus the absolute third moment do not determine the entire sum CDF. Two explicitly specified pairs of laws demonstrate this in the central and left normalization domains. These examples do **not** establish an obstruction for attained/contact laws or for laws passing the acquired resource conditions. In fact, their signed scores are below the manuscript's `.4` comparison floor. They are not counterexamples to the main theorem, nor do they preclude a useful upper bound based on the listed information.

No manuscript source or native numerical certificate was changed. This is a bounded research result, not a new proof dependency.

## 1. One conditional-count identity

Fix an integer `n>=2`, `0<p<1`, `q=1-p`, and `1<=k<=n-1`. Let

\[
Y=B+U,\qquad B\sim\operatorname{Bernoulli}(p),\qquad E(U\mid B)=0.
\]

The two actual conditional laws `U_0,U_1` are bounded and satisfy

\[
 U_0\le a_0,\quad U_1\ge-a_1,\quad a_0,a_1\ge0,
 \qquad d_0\ge a_0+a_1,\quad c=1-d_0>0.
\]

Take all `2n` variables `U_{0,i},U_{1,i}` independently, with their respective actual conditional laws, and define

\[
 W_j=\sum_{i\le j}U_{1,i}+\sum_{i>j}U_{0,i}\quad(0\le j\le n).
\]

Extend `W_j` constantly to each of the two exterior integer half-lines. Then `j+W_j` increases by at least `c` inside `[0,n]` and by exactly `1` outside. For every real `u`, put

\[
 R=\max\{j\in\mathbb Z:j+W_j\le k+u\}-k.
\]

The maximum is finite; boundedness also makes `R` bounded. Let `J~Bin(n,p)` be independent of these arrays. Conditional on `J=j`, `j+W_j` has exactly the distribution of the sum of `n` iid copies of `Y` conditional on its Bernoulli count. Monotonicity gives the pathwise equivalence

\[
 J+W_J\le k+u\quad\Longleftrightarrow\quad J\le k+R.
\]

Writing `F_B` for the binomial CDF and `pi_j` for its mass, zero outside `[0,n]`, this proves

\[
 P\Big(\sum_{i=1}^nY_i\le k+u\Big)-F_B(k)
   =E[F_B(k+R)-F_B(k)]=\pi_k E G(R),
 \qquad G(r)=\frac{F_B(k+r)-F_B(k)}{\pi_k}. \tag{1}
\]

Moreover, for legal indices,

\[
 \{R\ge i\}=\{W_{k+i}\le u-i\}\quad(i\ge1),\qquad
 \{R\le-i-1\}=\{W_{k-i}>u+i\}\quad(i\ge0). \tag{2}
\]

The strict inequality in the second formula is forced by the closed CDF event. No continuity assumption, independent-copy replacement of the marginal, or exclusion of phase collisions is used.

The nearest-count identity itself can also be obtained by conditioning without monotone coupling. The coupling is licensed here by the inward support bound, which every proposed joint application already supplies. It must not be silently dropped from a general unified statement.

## 2. Two pointwise majorants

For every integer `r`,

\[
 G(r)\le g_{\rm near}(r):=
 -\mathbf1_{\{r\le-1\}}+
 \sum_{i=1}^{n-k}\frac{\pi_{k+i}}{\pi_k}\mathbf1_{\{r\ge i\}}. \tag{3}
\]

For `r>=0`, this is equality. For `r<=-1`, `F_B(k+r)-F_B(k)<=-pi_k`; the remaining negative masses have simply been discarded. Equations (2) and (3) give exactly the native nearest outgoing count and the incoming tail sum, with their original atom conventions.

For the second majorant put `v=pq`, `chi=(n+1)p-k`, `m_B=max_j pi_j`, and assume `chi<2`. Set `r_+=max(r,0)`, `r_-=max(-r,0)` and take binomial coefficients of nonnegative integers, with `binom(h,l)=0` for `h<l`. Then

\[
 G(r)\le g_{\rm whole}(r):=r+
 \frac{m_B}{(n+1)v\pi_k}
 \left[(\chi-1)_+r_+
 +\chi_+\binom{r_-}{2}+\binom{r_-}{3}\right]. \tag{4}
\]

Here is a proof that also explains the boundary extension. Write `pi_j^(n+1)` for the `Bin(n+1,p)` mass. Direct factorial cancellation, including `j=0,n+1` and the exterior zero masses, gives

\[
 \pi_j-\pi_{j-1}
 =\frac{(n+1)p-j}{(n+1)v}\pi_j^{(n+1)},\qquad
 \pi_j^{(n+1)}=q\pi_j+p\pi_{j-1}\le m_B. \tag{5}
\]

For `r>0`, the numerator of `G(r)-r` is

\[
 \sum_{i=1}^r(r-i+1)(\pi_{k+i}-\pi_{k+i-1}).
\]

The positive part of the `i`th difference is at most `m_B(chi-i)_+/((n+1)v)`. Since `chi<2`, only `i=1` can contribute, proving the first correction in (4). For `r=-h<0`, the same numerator is

\[
 \sum_{i=0}^{h-2}(h-1-i)(\pi_{k-i}-\pi_{k-i-1}).
\]

Use `(chi+i)_+<=chi_++i`, and the identities

\[
 \sum_{i=0}^{h-2}(h-1-i)=\binom h2,\qquad
 \sum_{i=0}^{h-2}i(h-1-i)=\binom h3.
\]

This proves (4) for all integers, including cutoffs outside the legal count range. In particular, the coefficient of `binom(r_-,3)` is **one**. The inequality `chi<2` cannot simply be removed: the finite controls contain an explicit counterexample to that altered formula.

More generally any pointwise majorant `g>=G` on the possible integer cutoffs gives `Q/pi_k<=E g(R)`. A piecewise-polynomial `g` is therefore a legitimate common certificate interface. Its construction must come with a proved expectation bound under the **same joint conditional-count law**. The one-variable pointwise check alone does not supply that bound.

## 3. Shared score gate and preservation of small noise

Keep precisely the manuscript's quantities `rho_B,C,C_B,b=sqrt(n) pi_k,f(u),mathcal R`. Its exact identity becomes

\[
 \rho_B(C-C_B)=b\{EG(R)-f(u)\}+\mathcal R. \tag{6}
\]

Thus if `g>=G`, `E g(R)-f(u)<=X`, `mathcal R<=Y`, and `0<m<=b<=M`, then

\[
 \rho_B(C-C_B)\le\max\{mX,MX\}+Y. \tag{7}
\]

This is a sign-safe scalar interface, not a new probabilistic estimate. If a proved estimate has already regrouped terms as `b X+lambda I/n`, the same maximum applies, followed, for `N<=n<=L`, by

\[
 I/n\le\max\{I/N,I/L\},\qquad 1/\infty:=0. \tag{8}
\]

The native nearest witness is recovered with `X=-D<0`, `Y=kappa lambda/n`. The native whole witness is recovered from its already proved **regrouped** estimate with `X=lambda B<0`, `I>=0`; (7)–(8) become `lambda(mB+I/N)`. In the latter, `I` includes curvature and phase terms as well as repair terms. Identifying it with `mathcal R` alone would be incorrect. Positive allowance and finite-index sign variants remain separately charged exactly as in the manuscript.

There is no division by `lambda` in (1)–(8). Nevertheless, the desired strict improvement requires the final right side to be less than `-epsilon lambda` for **every** positive noise level. The new organization supplies no such uniform reserve by itself. The native TINY relative-tail argument and the whole-count fractional-part/marked-crossing estimate are still needed. At `lambda=0`, the actual conditional noises vanish and the manuscript uses its separate Bernoulli argument.

## 4. Exact central and left obstruction

Fix `a>0` and let independent elementary variables have laws

\[
 V=\begin{cases}-a&1/2,\\a&1/2,\end{cases}\qquad
 W=\begin{cases}-2a&1/8,\\0&3/4,\\2a&1/8.\end{cases}
\]

Both are centered and symmetric with variance `a^2`; their fourth moments are respectively `a^4` and `4a^4`. Choose positive integers `m0,m1`, an integer `k=np`, and require `qm0=pm1`. Define **entire iid marginals**, not independently chosen moment tables:

* Law A: `Y|B=0=sum_(1..m0) V`, and `Y|B=1=1+sum_(1..m1) W`.
* Law B: `Y|B=0=sum_(1..m0) W`, and `Y|B=1=1+sum_(1..m1) V`.

Every elementary copy is independent; `B~Bernoulli(p)` in either marginal. Each sum in the CDF consists of `n` independent copies of that entire marginal. Standardize both by

\[
 X=(Y-p)/\sqrt{v+s},\qquad s=(qm_0+pm_1)a^2.
\]

This specifies the full finite probability laws. Their raw noise supports are, respectively,

\[
 \begin{array}{c|cc}
 &U_0&U_1\\\hline
 A&[-m_0a,m_0a]&[-2m_1a,2m_1a]\\
 B&[-2m_0a,2m_0a]&[-m_1a,m_1a].
 \end{array}
\]

To obtain the standardized support, subtract `p` in the first column, add `q` in the second, and divide by `sqrt(v+s)`. The columns stay on their respective sides of zero in both examples below.

At count `k`, both laws give the **identical full distribution**

\[
 W_k\overset d=\sum_{1}^{m_0(n-k)}V+\sum_{1}^{m_1k}W,
 \qquad m_0(n-k)=m_1k. \tag{9}
\]

Equivalently its characteristic function is
`cos(at)^(m0(n-k)) ((3+cos(2at))/4)^(m1 k)`.
Both laws have the same conditional variances `s0=m0 a^2`, `s1=m1 a^2` and zero conditional third moments. They have the same first three ordinary moments. Their fourth moments also agree: for a sum of `m` elementary copies, the fourth moments are `(3m^2-2m)a^4` for `V` and `(3m^2+m)a^4` for `W`; the total fourth-moment difference is `3a^4(pm1-qm0)=0`. Finally

\[
 E|Y-p|^3=v(1-2v)+3v(s_0+s_1), \tag{10}
\]

so the standardized absolute third moments agree too. This does not assert equality of signed fourth moments or of every higher resource used by the manuscript.

The exact examples use `n=150`, `H=u=0`:

| Panel | `p` | `k` | `m0,m1` | `a` | `lambda=ns` | Common maximum `|U_j|` | Largest inward sum |
|---|---:|---:|---:|---:|---:|---:|---:|
| Central | `2/5` | `60` | `2,3` | `9/4000` | `729/400000` | `.0135` | `.018` |
| Left | `9/25` | `54` | `9,16` | `1/2500` | `108/390625` | `.0128` | `.0164` |

Both satisfy `n>=47`, `p in [.304,.47]`, `0<lambda<.05`, `theta=s/(v+s)<.0154`, inward sum `<.0181`, and amplitude `<.425`. These are global normalization-domain checks only. Neither example is claimed to pass the contact/acquisition hypotheses; the exact additional score classification in `details02/checked/RESULT.json` is below `.4` for both laws in both panels.

For these supports every count `j<=k-2` is surely inside the CDF event and every count `j>=k+2` is surely outside. The pilot verifies these finite support comparisons exactly. At the own count the laws agree. Consequently their full CDF difference is exactly

\[
 \pi_{k+1}\{P_A(W_{k+1}\le-1)-P_B(W_{k+1}\le-1)\}
 -\pi_{k-1}\{P_A(W_{k-1}>1)-P_B(W_{k-1}>1)\}. \tag{11}
\]

The exact fractions are positive and nonzero. Decimal diagnostics are approximately `1.39204378971792361e-133` centrally and `2.82935825400903872e-915` on the left; these decimals play no role in acceptance. The left example includes atoms at the transition value `1`. Replacing strict outgoing tails by closed tails would change the calculation.

The complete exact full CDFs, all four neighbor tails, the differences, the own-count atom and full law specifications are stored in `pilot01/checked/RESULT.json` and `details02/checked/RESULT.json`. Their fractions are large, so the machine-readable files are preferable to rounded or abbreviated display values.

The calculation is finite integer arithmetic. For `m` copies of `V` and `b` copies of `W`, write `c_l=[z^l](1+6z+z^2)^b`. Their lattice sum in units `a` is `2i-m+2l-2b` with weight `binom(m,i)c_l/(2^m 8^b)`. Summing exactly the indices above the appropriate integer threshold proves each fraction in (11). The independent controls also build small cases by direct rational convolution, with a different summation algorithm.

**Precisely excluded claim:** there is no function of just the own-count distribution and the listed normalization/moment information that equals this full CDF for every marginal satisfying those normalization conditions. The examples do not exclude a useful worst-case majorant, extra contact consequences, a sufficient finite moment package, or a different analytic proof of the theorem.

## 5. What still has to be proved in any shortening

| Obligation | Why the common majorant does not replace it |
|---|---|
| Actual iid reduction and inward support | They give the monotone coupling and the correct conditional marginals. A moment relaxation is not an iid realization. |
| Shared finite Stirling, phase and cubic repair bounds | They control the normalizing factor and `mathcal R` in (6); their signs matter. |
| Shifted quartic minorant and Bennett/Poisson bounds | They control the nearest outgoing loss and the entire incoming sum in (3). |
| Relative-tail monotonicity as `lambda` tends to zero | Endpoint values alone cannot prove a loss proportional to arbitrarily small noise. |
| Crossing moments and marked deletion | They estimate (4) using a coupling of neighboring counts; independence after deleting the marked pair is essential. |
| Fractional-part harmonic gain | It supplies the negative term in the whole-count linear expectation. It is not polynomial algebra in the supplied moments. |
| Same-law budget, signs and closed domain covers | They connect those estimates to every attained law, all signed phases and the selected numeric ranges. |

An ambitious future theorem could bound `E g(R)` for a finite family of piecewise-polynomial `g` using one explicitly defined **joint** conditional-count moment system and a common, proved relative-error envelope. Its exact missing input is a uniform expectation estimate retaining the marked deletion and harmonic information, or a new argument replacing them. No such theorem is established here, and no claim of a large page saving relies on it.

## 6. Reproduction and status

Mathematical status: (1)–(8) locally derived with proofs above; the explicit pairs (9)–(11) are exact finite constructions; no theorem about restricted attained laws has been added. Execution status: `pilot01`, `controls02`, and `details02` completed with actual return code zero. The controls verified 400 independent small convolution tails, 1,872 binomial identities, 50,000 nearest majorant values and 36,885 whole majorant values, and rejected four false variants. Those finite tests supplement rather than replace the symbolic proofs.

All earlier failed observations are preserved. `controls01` failed only because its small diagnostic grid ended at `n=15` and did not contain a counterexample to dropping `chi<2`; the next grid includes the explicit counterexample `n=21,p=9/25,k=5,r=3`. `details01` tested the stronger exploratory assertion that these examples have score above `.4`; that assertion failed. `details02` reports the actual classification and claims only the normalization-domain obstruction. No original source or result was rewritten.

The versioned sources and process captures are all in this directory. No Fourier integrations, finite-base campaign, all-index campaign, or fresh replay of the manuscript's numerical proof was run for this research note.
