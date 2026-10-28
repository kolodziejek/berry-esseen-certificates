# Current research status — v14, 28 October 2026

Existing sole review target: https://github.com/kolodziejek/berry-esseen-certificates/pull/5
Keep draft; no merge, main push, force-push, branch deletion or upstream change.
Original reference:6346fc1b4432bc5982822aa696eb566ed9e1e1ee.
V14 starts from reviewed/published656232ea8d9561a3f47aefa083ead4f6ba4206ca.

| Result | Mathematical status | Execution status |
|---|---|---|
| Right local comparison: n>=6000,p[.4,.53],.075<=lambda<=.36,d<=3/n,raw abs(H)<=1.84 | Locally derived all-law theorem, independent full review found no blocker; actual-gap budget supplies d<=3/n conditionally |39constructor gates; independent40gates/150small-product controls and27exact binomial controls PASS |
| Common independent noise, p[.25,.75], support width<=.2 | All-n/all-threshold sharp bound with margin3s/(1000v^(3/2)); independent coordinator derivation; external Schulz theorem retained |507checks,40moment,120product identities,156outwardCDF events,6negative controls PASS |
| Left geometric region: p[1/3,.4],nQ/sqrt(v)>=24 | Full signed excess<-1/(10n), conditional on stated budget/strip premises and Schulz middle-p theorem |28gates,5index endpoints,216curvature and15full signed events PASS; independent2638checks/72physical curvature cases PASS |
| Two central asymmetric families, n>=42,np integer,H0,lambda<=.36 | Complete restricted comparison; independently checked |28actual laws,68paired identities,2304hinge points,6bias controls PASS |
| General intermediate unequal-noise comparison,C4,BASE41,full conjecture | OPEN |No general acceptance claimed |

Main proof: mathematics/simplification-v14/2026-10-28/large-index.pdf (5pages).
Also loss-closure.pdf(3),geometry-slack.pdf(4),counts-pair.pdf(4).
Optional loss-common.pdf(3) is not an ancestor of independent-noise closure.
The89-page manuscript remains unchanged. No new overall paper length is claimed.

The high-index proof replaces larger-noise grids by a CF estimate, exact
selected-count transport, a21-count window and complete fourth-moment tails.
Together with v12 small-noise comparison, it closes the stated acquired right
strip at n>=6000. It does not establish acquisition or an unconditional cutoff.
On the left, an acquired contrary witness p<=.4 now has n<=2681;
p<1/3 still uses the earlier n<=168 bound. No count statement is added on(.53,.54].

Bounded reproduction: mathematics/simplification-v14/2026-10-28/run_checks.py NEWID.
Fresh integration:9bounded checks PASS, recorded in
runs/simplification-v14-20261028/integration01/receipt.json.
All2748baseline entries preserved:182materialized byte checks and2566sparse
bindings. All85tracked manuscript files unchanged. Publication is verified separately; do not infer a remote head
from this local status text. Prior state is preserved in stateBefore01.

Research worktree: work/fork_audit_20261027/simplification-v14.
Integration branch: manuscript/strategy-v4-20261027 in strategy-v4.
Baseline certificates/reference/history are preserved. Historical success labels
in startup files do not override this scope or constitute independent evidence.
