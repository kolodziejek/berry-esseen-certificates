# Independent audit of the all-law window, tail and final comparison

Reviewer: counts component agent. Review worktree: `counts-window-review-v14`, branch `research/counts-window-review-v14-20261028`, baseline `656232ea8d9561a3f47aefa083ead4f6ba4206ca`.

This agent constructed the separate paired-kernel/two-point-family component, but did **not** construct the all-law characteristic-function/transport argument or its acceptance checker. The mass estimate below was derived independently and differs from the constructor's estimate. No constructor Python is imported or executed.

Reviewed source: `mathematics/simplification-v14/2026-10-28/large-index.tex`, SHA-256 `ad48f1eae57817b955016c6a12114e3929852a3e636afcfbb91646697b4c6509`.

| Item | Mathematical status | Execution status |
|---|---|---|
| Kernel support and bound | Independently derived; no blocker | Exact constants checked |
| Physical residual variance and fourth moment | Independently derived; no blocker | Exact check and actual-law negative control PASS |
| Complete discarded-window tail | Independently derived; no blocker | Exact rational coefficient PASS |
| Uniform binomial mass inside the window | Independently derived from finite Stirling with a different bound; no blocker | Exact rational gate and 27 actual binomial checks PASS |
| Weighted-loss normalization and final scalar | Independently derived; no blocker | Exact strict terminal margin PASS |
| Characteristic gain and phase/normal repair | Read and algebra rechecked; assigned formal ownership remains with the other review | Used as explicit premises below |
| Acquisition join and global theorem implications | Outside this review's acceptance scope | No global conjecture/cutoff claim |

## Precise inputs

The window result applies to `n>=6000`, `p in [.4,.53]`, centered conditional noises supported in `[-.6,a0]` and `[-a1,.6]`, `d=a0+a1<=min(.072,3/n)`, `lambda=ns in [.075,.36]`, and raw `|H|<=1.84`. Let `t=np+H sqrt(pq+s)`, `k=floor(t)`, `u=t-k in [0,1)`.

The retained crossing theorem supplies nonnegative `g_i=E h(R_i)`. For the final comparison this review takes the following separately justified inputs explicitly:

- `sum_i g_i >= lambda/5 - 13d`;
- normalized phase/normal repair `<5/n`;
- `rho>=rho_B`, so the cubic correction is nonpositive for every `C>=0`;
- the v13 signed-curvature theorem, with its actual conditional variances.

The proof below is uniform in the law, the sample size and the closed noise interval. It is not a fixed-law limit or a sampled-domain argument.

## 1. Kernel support and physical fourth moment

For `x<1-a1`, `h(x)=E(x-U0)_+`. It is zero for `x<=-.6` and increases to `1-a1<=1`, since `1-a1>a0`. For `x>=1-a1`, `h(x)=P(1+U1>x)-E(1+U1-x)_+`; it is nonnegative by the crossing theorem, at most one, and zero for `x>=1.6`. Thus `0<=h<=1` and it vanishes outside `[-.6,1.6]`, including the zero-valued extreme endpoints.

The residual `V_i=sum_(l<i) U1_l + sum_(l>i) U0_l` has variance at most `n max(v0,v1) <= lambda/min(p,q) <= (5/2)lambda`. This uses physical conditional variances; it does not replace them by a common own-count allocation. Independence and centering give

`E V_i^4 <= .36 Var(V_i) + 3 Var(V_i)^2 <= (153/20)lambda`,

because `lambda<=.36`. The coefficient is exactly `.36*(5/2)+3*(5/2)^2*.36=153/20`.

A negative control uses an actual admissible law at `n=6000,p=.4,lambda=.36`: `U0` centered on `{-3/5,1/6000}`, `U1=0`. At the first residual, `Var(V_1)=(n-1)/10000 > lambda`; its exact fourth moment also exceeds the false bound `.36lambda+3lambda^2`. The required allocation inflation is therefore substantive.

## 2. The entire discarded tail

For `i=k+j`, `j>=11`, nonzero kernel requires `V_i <=u+1-j+.6 <2.6-j`. For `i=k-j`, it requires `V_i>=u+j-.6>=j-.6`. These are implications for the actual residual; no independence with a selected index is invoked.

Markov and the kernel bound give the sum of both tails bounded by

`(153lambda/20) sum_(j>=11) [(j-13/5)^(-4)+(j-3/5)^(-4)]`.

For a decreasing nonnegative function, the entire sum is bounded by its first value plus the integral from that first integer to infinity. Thus the coefficient of `lambda` is at most

`(153/20)[(5/42)^4+(5/42)^3/3+(5/52)^4+(5/52)^3/3]`

`=5536030025/631986840576 <1/100`.

This is a complete infinite-tail bound, not a truncation or a finite test of small terms. Missing count indices near an endpoint only reduce the sum.

## 3. Independent uniform window mass estimate

From the domain, `|t-np|<.94`; hence `|i-k|<=10` implies `|i-np|<12`. Put `z=i/n`. Then `z` and every point between `z,p` lie in `[199/500,133/250]`, where the variance product exceeds `19/80`. Also `i,n-i>n/3`.

The finite Stirling inequalities yield

`sqrt(n) pi_i >= sqrt(2/pi) exp[-n D(z||p)-1/(12i)-1/(12(n-i))]`.

Taylor's integral formula for relative entropy and the preceding variance-product bound give `nD <24/475`. The two Stirling upper remainders sum to less than `1/(2n)<=1/12000`. With `pi<22/7` and `exp(-x)>=1-x`, it therefore suffices to check

`(7/11)(1-24/475-1/12000)^2 >9/16`.

This strict exact inequality holds. Consequently `sqrt(n)pi_i>3/4` throughout the complete window and all sample sizes in scope. The constructor uses the different valid entropy floor `.23` and its combined factorial remainder; this review does not reuse that gate.

The only external analytic input on this edge is the retained finite Stirling formula with explicit remainder. The source paragraph is in `manuscript/arxiv-v1/appendices/count-comparison.tex`, beginning “For completeness, the finite Stirling formula used here is”. No local central limit theorem or asymptotic error is substituted.

The additional 27 exact binomial checks use `n=6000,6001,10000`, `p=.4,.5,.53`, and indices `floor(np)-11,floor(np),floor(np)+11`. They are regression controls only. A genuine negative control verifies that the same lower bound fails at `n=6000,p=.5,i=np+50`; the window restriction matters.

## 4. Weighted loss and terminal scalar

The window's unweighted reserve is greater than

`(19/100)lambda -13d >= (19/100)lambda -39/n >0`.

Thus the normalized weighted loss is strictly greater than

`(3/4)[(19/100)lambda-39/n] = (57/400)lambda-117/(4n)`.

Here the square-root normalization is applied once: the mass bound is for `sqrt(n)pi_i`, whereas the `g_i` remain unnormalized. The finite window reserve is positive throughout the closed domain, including `n=6000,lambda=.075`.

The curvature parameter `c=(np-q-t)_+` is below `.46` because `q>=.47` and `1.84 sqrt(.25+.36/6000)<.93`. Hence the v13 lemma gives normalized curvature at most

`25lambda/(24sqrt(n)) +23sqrt(lambda)/(24sqrt(n+1))`.

Adding the `<5/n` phase/normal repair changes the constant `117/4` to `137/4`. Divide by `lambda` and use the smallest `n` and `lambda`, together with `sqrt(n),sqrt(n+1)>77` and `sqrt(lambda)>.27`. The exact residual after subtracting all adverse terms is

`57/400 -137/1800 -25/(24*77) -23/(24*77*(27/100))`

`=2411/356400 >1/200`.

The strict excess above the claimed rate is `629/356400`. Therefore, conditional on the listed input lemmas, the canonical all-law comparison satisfies `Delta_C<-lambda/200` on the entire stated domain.

## Outcome and reproduction

No blocker was found on the window, complete tail, mass or final comparison edges. This report does not certify the acquisition hypotheses or state a global numerical cutoff for the conjecture.

Run:

```sh
python3 mathematics/simplification-v14/2026-10-28/counts-window-review-check.py --source /absolute/path/to/large-index.tex
```

The checker rejects changed reviewed source bytes and imports no constructor. Three disposable mutation controls freshly rejected a missing required option, a missing source file, and changed source bytes; their logs are in `mutations01/`. Fresh stdout, stderr, source snapshot, Python version, elapsed time, return code and hashes are stored under `runs/counts-window-review-v14-20261028/check01/`. The reviewed proof is LaTeX owned and compiled by the coordinator; this component changes no theorem source.

## Final source-pin refresh

After the first committed review, the coordinator changed only two long source references from `texttt` to `path` and inserted paragraph breaks. The saved diff confirms no formula, hypothesis or mathematical prose changed. The old source remains preserved in `check01/`; the final source pin above is freshly checked in `check02/`. The independent arithmetic was rerun against the final bytes, and fresh malformed-source rejections are preserved in `mutations02/`.

## Explicit iid statement clarification

The final statement now explicitly defines `U_j` as the conditional noise given `B=j`, and states that `X_1,...,X_n` are independent copies of `X`. The diff from the preceding reviewed source contains exactly these two sentences. They make explicit the conditional-law and iid hypotheses already used throughout this audit; no bound, formula or arithmetic domain changes. The final pin above is bound by fresh `check03/`, which preserves the source, exact diff and successful quick checker replay. Earlier review snapshots remain unchanged.
