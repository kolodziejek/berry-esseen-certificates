# Actual central-gap event beyond the sufficient D<2 regime

The source's genuine gap criterion is `D<(sqrt(10)-1)rho`; `D<2` is only a convenient uniform sufficient condition. The new proof fragment `central-gap.tex` proves a quantitative event interface directly from the moment-sensitive criterion. It does not acquire a numerical defect ceiling or assert complete coverage.

Let the same standardized actual law satisfy `rho in [l,u]`, `D<=d`, `d>=0`, and let `1<sigma_lower<sqrt(10)`. If

`P0=(sigma_lower-1)l-d>0`,

then zero is absent from its **closed** support, and its actual central gap `(-A,B)` obeys

`S=l-d/(sigma_lower-1)>0`,

`(A+B)^2 >= 2S+2P0/3 > 2S`.

Thus the question's proposed lower bound `2(l-d/(sigma_lower-1))` is valid, and the product estimate supplies the stronger bound used in the fragment. The two bounds concern the actual endpoints; no contact maximality, own-score cap, lattice approximation or D<2 assumption is used.

For independent copies, `E={XX'<0}` has

`P(E)>=alpha=1/(2u^2)`, `|X-X'|^2>=2S+2P0/3 on E`,

`E[(X-X')^2|E]<=2/alpha=4u^2`.

These are precisely the event inputs required by `high_window_core.one(N,alpha,event_m,d0,M,w)`, with `event_m=4u^2`, a **downward** rational square-root enclosure for d0, and a separately valid fourth-moment ceiling M. The field named `m` in that code is the conditional squared-distance ceiling; it is not the first positive moment m in the proof.

## Source hypotheses and independent derivation

At the task base `43f9f82`, `manuscript/arxiv-v1/sections/05-geometry-counts.tex:90–130` proves the physical gap criterion: if zero belongs to support, `J<=rho` and therefore `D>=sqrt(10)rho-gamma>=(sqrt(10)-1)rho`. Strict separation from that bound forces a genuine open component of the complement of closed support containing zero. Centering and nonzero variance ensure both endpoints are finite and positive in magnitude.

The same file, lines 148–180, gives the nonnegative decomposition

`D=m Q(A,B)+(sigma-1)T_plus+(sigma+1)T_minus+3(T_plus+T_minus-J_outer)`.

Here `T_plus=E X_plus^3-mB^2`, `T_minus=E X_minus^3-mA^2`, and the last difference is nonnegative by actual outer-gap integration. Thus `T_plus+T_minus<=D/(sigma-1)` and `m(A^2+B^2)>=S`. With `m<=1/2`, this already gives the requested `gap^2>=2S`.

The sharper product step is separate: `J<=rho+2mAB`, proved by summing the same signwise gap inequalities, gives `6mAB>=sigma*rho-gamma-D>=P0`. Adding `m(A^2+B^2)>=S` and `2mAB>=P0/3` before using `m<=1/2` yields `gap^2>=2S+2P0/3`. The source has the corresponding product argument in `appendices/fourier-analysis.tex:1877–1897`. If a separately established signed upper bound `gamma<=g_upper` is available, the product argument can use `max(P0,sigma_lower*l-g_upper-d)`; the submitted fragment uses only P0.

The probability and conditional moment need no small-defect theorem. Signwise conditional Cauchy gives `pq>=m^2`. Cauchy applied to `|X|^(1/2)` and `|X|^(3/2)` gives `1<=2m rho`, so `2pq>=1/(2rho^2)>=1/(2u^2)`. Finally the total independent-copy squared distance has mean two. All atoms at the actual inner endpoints are included. At the boundary `d=(sigma_lower-1)l`, the displayed quantitative distance collapses to zero and cannot be supplied to a kernel requiring `d0>0`.

The complete HIGH interface is in `appendices/fourier-analysis.tex:1198–1374` and `mathematics/fixed-target-v5/2026-10-27/cell-sources/high_window_core.py:9–38`. It assumes an actual event under the product of one marginal, not `D<2`. It also requires all six frequency pieces and their index/window gates. The older generic-event bundle at Fourier lines 2230–2284 additionally derives endpoint, J1 and moment ceilings under its own hypotheses, including D<2 and an alpha gate. Those extra conclusions are **not** automatically imported by the new event lemma.

## Read-only wrapper review

The root's revised `strategy-v4/mathematics/fixed-target-v6/2026-10-27/gap_check.py` was read together with its `combined_check.step`, the source `high_window_core` and the rational root helper. No wrapper or source kernel was executed by this reviewer.

The revised wrapper computes `gap2=prior.central_gap_squared_lower+2*prior.central_gap_margin/3`, which is exactly `2S+2P0/3`. It requires a positive prior gap margin before every use. The lower root enclosure is safe; if rounding produced zero, the source HIGH guard would reject it. The event parameters are the values proved above. It calls all six permitted windows, retaining all six positive terms in each candidate, and takes a minimum only of complete candidates.

`selected=min(original_HIGH,new_HIGH)` is valid because both bound the same integral for the same actual law. The low triple remains the original complete triple. `row.KF=min(previous_KF,new_KF)` is therefore also a minimum of valid bounds with the same H-slope; it is not a coordinatewise mixture of unrelated low triples. Keeping a previous KF even when the latest candidate is weaker is sound. The resulting smaller Fourier constant is passed to the existing ordered resource step; previous raw and resource ceilings remain distinct.

This wrapper uses a previous acquired gap, then obtains a new defect ceiling. It does not assume the desired new gap or D<2 in its own input. Its imports of the v6 moment, signed-coefficient and phase steps remain separate analytic prerequisites; this review does not re-prove or accept their full numerical computation. The wrapper's six-update results are recorded by the constructor as exploratory strengthening, not acceptance of the old INITIAL42 or LOCAL42 schedules.

## Status and checks

| Result | Mathematical status | Execution status |
|---|---|---|
| Moment-sensitive actual gap and distance floor | Independently derived from the actual support/gap identities | Bounded exact finite-law controls recorded separately |
| Opposite-sign HIGH event interface | Proved for the same actual marginal, no D<2 assumption | No HIGH integral evaluation in this review |
| Revised root wrapper's dependency order | Read-only semantic review; no mismatch found in the reviewed scope | Constructor runs not reproduced here |
| Full 24-cell acquisition / final exclusion | Not established by this report | No native or dense run |

The new standard-library `gap_event_check.py` checks normalized finite laws, actual gap sums and event moments. It includes a skew Bernoulli law with a valid chosen defect ceiling above 2, a gapped three-point law, a gapped law that fails this sufficient criterion, and a zero-atom law that must fail it. A separate rational check verifies the d0-independent HIGH monotonicity gates for the six fixed windows at the worst initial rho and M4 ceilings. None of this is an assertion that those test laws maximize fixed-target excess. Exact command, hashes, stdout, stderr and return code are recorded under `runs/fixed-target-v6-20261027/gap-review01` and `gap-review02`. Both passed; the second run records the final fragment after explicitly restricting the gap sum to bounded complementary intervals.
