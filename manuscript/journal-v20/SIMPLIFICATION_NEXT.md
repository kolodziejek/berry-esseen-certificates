# What the new certificates do, and the next experiment

The new small-noise proof is a mathematical simplification, but the measured
complete draft has 100 pages, compared with 98 in v19. It removes the
small-noise relative-tail arguments and replaces them with a coupled-count
fourth-moment bound, four polynomial domains and their soundness explanation.
The added certificates do not by themselves shorten the full paper.

## Completed result

For the actual coupled conditional sums and `c=1-d0>1/2`,

`G(R) <= -1{W_k>u} + R0 W_k^4/(c-u)^4`.

This bounds all incoming counts using the same own-count random variable.
It is a domination theorem; it does not identify the full CDF from that
variable. The exact polynomial cover works on all 83 uniform inputs and all 267
finite small-noise inputs. The finite sign and allowance rules are retained.
Thus the old small-noise tail proof really can be deleted, rather than being
moved to an uncounted analytic supplement.

An optional stronger certificate uses a quartic majorant of the entire
staircase payoff on each phase cell. It proves the original strict comparison
on the full uniform band `.05<=lambda<=.08`. All finite intervals, both
infinite rays, the enlarged normalization and actual row ceilings were checked.
It is outside the main proof graph because it does not remove the remaining
MID/LOW machinery. Its complete mathematical argument and portable objects
are in `certificates/joint-count/mid/`.

## Why repeating this operation will not reach sixty pages

In the current layout, the finite-index argument occupies approximately
pages 27–50, acquisition and confinement pages 50–82, and final local comparisons
pages 82–98. The small-noise proof was only about one page of the old argument.
Even eliminating every final local-comparison page would not save the roughly
40 pages needed. A large reduction must also simplify acquisition/confinement
or the finite-index argument. These ranges describe occupied pages, not
additive estimates of savings: boundary pages are shared.

The earlier broad coefficient-calculus experiment also saved zero pages.
Its failure and the present 98-to-100 measurement argue against converting
more algebra into certificates without first identifying a removable
mathematical dependency.

## Next bounded mathematical experiment

Try a higher-moment polynomial comparison on the **coarser acquired support**,
before the noise-dependent confinement profiles. Success could remove both
the separate marked-crossing/harmonic calculation and some confinement steps.
This is a research proposal, not a proved replacement.

1. Start with the original central row near `p=.4` and difficult left row near
   the lower endpoint. Record their complete acquired domain before
   confinement: same-law conditional supports, inward distance, variance,
   signed threshold, actual noise ceiling and score bounds. Do not substitute
   an improved amplitude supplied by the theorem one hopes to remove.
2. Seek degree-six or degree-eight polynomial majorants of the coupled-count
   payoff. Begin with the already proved staircase majorant, whose all-real
   checking interface is available. If it is too weak, derive a stronger
   pathwise or expectation inequality before constructing its certificate.
   A candidate upper bound for a different joint process is not sufficient.
3. Derive moments from one common pair of conditional laws. For example the
   coefficient of `z^r/r!` in
   `M_1(z)^k M_0(z)^(n-k)` is the actual r-th moment of `W_k`, where the
   `M_j` are the conditional exponential-generating moment polynomials.
   Use the acquired bounded support to justify these moments, and retain
   simultaneous moment feasibility and inward-support constraints.
4. Keep `t=E W_k^2` distinct from `lambda`; retain the actual integer `k`,
   `n`, signed phase and normalization repair. A relaxation in `1/n` must
   contain every licensed integer and preserve all denominator signs.
5. Prove complete phase/noise coverage, retaining the scaled small-noise
   charts. Use the original strict target on uniform inputs and the original
   allowances/reserves on finite inputs. Do not change a target to obtain
   acceptance. Negative controls must include omitted rays, threshold atoms,
   wrong moment signs, a changed marginal between factors, and the
   arbitrarily-small-noise boundary.
6. Before extending beyond two panels, measure a literal full manuscript
   replacement including its analytic soundness proof. A valid certificate
   that leaves every old analytic dependency in place is an optional result,
   not a shortening step.

The fourth-moment envelope alone already fails for some larger-noise targets;
the saved exact failures concern those sufficient witnesses, not the
Berry--Esseen conjecture. Higher moments may also fail. In that event preserve
the failure or a rigorous relaxation obstruction, and redirect effort toward
a stronger structural/contact inequality. No numerical cutoff, propagation
theorem, eventual exact two-point optimality or sixty-page feasibility is
established by this proposal.
