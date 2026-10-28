# A limit of probability screening by the binary defect alone

This bounded experiment removes no additional probability panel. It is retained
to prevent a tempting but unsuccessful simplification from being reported as a
proof. Mathematical status: locally derived necessary inequality, conditional
on the accepted source cover; not independently reviewed as a new theorem.
Execution status: fresh exact evaluation, no Fourier kernel execution.

The actual-law defect decomposition gives

\[
D\ge B_0=(6+2\sqrt{10})\frac{m^3}{p^2(1-p)^2}(p-p_*)^2,
\qquad p_*=(4-\sqrt{10})/2.
\]

For one signed moment cell intersecting a probability panel in `[l,u]`, put
`vmax=max p(1-p)` on that closed interval. With the recorded lower bound `ml`
and outward lower square-root constant `sigma_l`, a valid lower bound is

\[
b=(6+2\sigma_l)m_l^3
  \operatorname{dist}([l,u],[p_{*,l},p_{*,u}])^2/v_{\max}^2.
\]

The existing elementary panel floor is also valid, so the probe takes their
maximum. Since the same resource satisfies
`U >= n phi(0) D/6 >= 42*(997/15000)*b`, it subtracts this lower cost from
the signed phase ceiling. Each concave phase quadratic is maximized over
the entire acquired interval, including an interior vertex. Both signs and
all incident cells remain. No particular iid law is inferred from a cell.

All 28 surviving panels have a nonnegative residual upper bound for at least
one sign. In fact both sign maxima remain positive. Even panel25, the closest
left endpoint tested, retains upper bounds .07331886 and .173305518; panel52
retains .09641185 and .123034991. Thus this coarse subtraction cannot exclude
another complete panel. A positive upper bound is not an existence proof for
a witness and is not a counterexample to the conjecture.

`probability-probe.py` and `runs/fixed-target-v8-20261028/probability01/` preserve
all rational calculations, input hashes, command, return code and timing.
The script currently reads the frozen phase export in sibling `phase-entry-v8`;
integration changes this path to the identical in-repository export. The input
hash remains fixed. No certificate or existing driver is modified.
