# How to pursue a complete manuscript near 60 pages

The present consolidation is still above the requested total length. This is not evidence that a 60-page proof is impossible. It shows that removing duplicated exposition and a redundant proof route is insufficient for this particular argument. Shrinking the type or omitting analytic licenses would not solve the mathematical presentation problem.

The best next approach is to make more of the *algebraic derivations* into explicit proof objects, while retaining the probability and analysis that justify their use. This implements the proposed architecture—human proofs of a few structural principles, computer proofs of precisely stated quantitative claims—more fully than the current checkers do. The current checkers already certify the final numerical inequalities. They do not yet provide a small common proof language for every formula feeding those inequalities.

## What has already been justified and implemented

- A direct proof of ratio attainment replaces the separate fixed-target optimization.
- The equality-inclusive uniform local exclusion replaces the separate strict tail argument from 700. It preserves that scope and proves strictness from 47.
- One sign normalization, one conservation identity, shared Fourier bounds, one acquisition invariant, and common nearest/whole-count comparisons replace repeated derivations.
- The four-summand physical argument has been condensed while retaining its common defect measure, singular-price licenses, quadrature and threshold errors, and both excess regimes.
- Coefficient arrays, subdivision data and execution metadata remain in the certificate package. Essential analytic arguments remain in the PDF.

These are completed improvements. The proposals below are not new proved replacements.

## Priority 1: a small algebraic certificate calculus

The main target is Section 7.2, with related formulas in Sections 5.3, 6.4–6.5 and 7.3. These derive numerous moment, gap, phase and resource coefficients from a much smaller set of principles. Preserve those principles in the paper and encode each particular derivation as data.

The checker should accept a typed directed acyclic graph of inequalities. Every node must state its variables, exact domain, hypotheses, conclusion and parent nodes. Initially allow only:

1. Exact polynomial identities, checked by coefficient comparison over integers or rationals.
2. Positivity on a closed rational box or simplex by a verified Bernstein expansion; the expansion identity is checked as well as coefficient signs.
3. Integration of a pointwise inequality against a named nonnegative measure, with explicitly specified moments. The measure identity is a mathematical input, not something inferred from its name.
4. Nonnegative linear combinations, interval intersection, division by an independently proved positive quantity, and a finite closed cover.
5. A proved conditional Taylor identity, signwise moment-matrix inequalities, and the shared resource-pricing lemma. Their analytic soundness remains in the paper.
6. A finite list of monotonicity and convexity rules, each with derivative or Hessian certificates and explicit domain guards. Do not permit a free-form assertion of convexity.

For example, conditional centering and the exact identity

`x^j-a^j-j*a^(j-1)*(x-a) = (x-a)^2 sum_{k=0}^{j-2}(k+1)*a^k*x^(j-2-k)`

give a positive-measure representation of the moment error. The particular fourth- and fifth-moment ceilings then reduce to polynomial identities and positivity on the acquired support interval. The same mechanism covers many signed Taylor coefficients, but their signs and the shared budget must be retained. A verifier must distinguish `E[W^2;X>0]`, `E[W^2;X<0]` and their sum; it must not spend one upper budget twice.

Concrete first milestone: cover every rule used by the signed initial acquisition and the paired Fourier coefficient rectangles. Export the *same* current tables, with exact directed containment of every scalar and phase polynomial. Do not change numerical targets to obtain acceptance. Then replace the corresponding formula catalogue in the paper by the common soundness theorem, a table of claimed interfaces and one worked derivation.

Required negative controls: altered coefficients, omitted and duplicated proof nodes, changed root domains, wrong inequality directions, missing denominator guards, incorrect sign classes, and a child domain not covering its parent. Each must reject. An independent implementation should verify a small set of nontrivial derivations before trusting a large library.

This is a concrete software-and-proof project. It is not already accomplished by the existing numerical PASS records, and it does not justify deleting the current derivations today.

A bounded pilot is supplied in [`research/polynomial-prototype/`](research/polynomial-prototype/). It checks the conditional identities at degrees 3–5 and two radial moment identities by exact rational coefficient arithmetic, with fixed targets and 23 malformed or corrupted objects that must reject. Fresh acceptance and control captures are included. This demonstrates a precise data/checker interface for five elementary cases only. It neither replaces the current manuscript proofs nor establishes the much larger signed, domain-aware calculus proposed above. For these simple examples, keeping the displayed factorizations may be clearer than outsourcing their verification.

## Priority 2: certify the finite collection of enclosure formulas uniformly

Section 5 and the finite refinements currently explain several scalar enclosures separately. Keep the compensated inversion proof, the closed-event Fourier majorant, the explicit infinite-frequency argument and the probabilistic construction of the HIGH event. They cannot be replaced by a check on a bounded grid.

For the bounded calculations, define one rigorously rounded calculus carrying a function and its first two derivatives. Prove its arithmetic and composition rules once. Supply polynomial/Taylor remainder certificates for the elementary primitives on their declared compact domains. Express each quadrature, support and phase calculation as an expression graph in this calculus.

The output obligation is exact: each graph must majorize the same integral or contact expression on the same closed domain as the existing program. A differentiated minimum is forbidden unless smoothness is proved; a branch may be fixed on a whole cell, or separate complete bounds may be minimized after integration. The law, moment variables, threshold and actual index must have persistent identities through the graph.

This could eliminate repeated derivations of interval endpoints, clipped quadratic vertices and differentiated Taylor tails. Whether it saves enough pages depends on the size and readability of the common soundness proof and worked examples. It should be measured on one complete family before rewriting the whole paper.

## Priority 3: unify the local comparison more deeply

Sections 7.4–7.7 still contain substantial probability, not just algebra. If the first two steps leave the manuscript over 60 pages, a further mathematical improvement is needed here.

A useful precise target is a single conditional-count comparison theorem. Its inputs should be the acquired interval for `p`, the actual bounded conditional supports, one joint defect/noise resource, both signed threshold ranges and the sharp deleted bounds. Its conclusion should be the same strict loss

`rho_B(C-C_B) <= -epsilon*lambda` for every positive `lambda`,

with an explicit uniform positive `epsilon`, and a separate exact Bernoulli branch at zero. It must cover every actual index and every parameter panel needed by finite 42–48 and uniform 47, using finite-index slack only in the domains where it is valid.

The present proof switches between a nearest outgoing count and a coupled random cutoff. A promising construction is a common polynomial or piecewise-polynomial witness for the exact conditional identity, evaluated with the same cubic moments and shared resource. Discovery may use optimization; acceptance must establish pointwise inequalities, exact common-marginal expectations and complete coverage. An error independent of `lambda` cannot handle its zero endpoint.

This is not a known convex-order consequence. Adding centered noise need not decrease a CDF at each threshold, and relaxed moment maximizers need not be iid convolution laws. Any proposed comparison must retain outgoing as well as incoming mass, the normal variance correction, threshold atoms and both phase signs. A proof using only a finite set of sampled laws would not establish it.

Start with one central panel and one difficult left panel, then test both phase signs, exact threshold collisions, deterministic conditional components and arbitrarily small noise. Only a complete analytic theorem plus a continuous-domain certificate cover can replace the current confinement and comparison proofs.

## A useful stop rule

After Priority 1, compile the full manuscript with unchanged readable typography and count *all* pages. If the small certificate calculus saves only a few pages or obscures the common ideas, retain the present exposition rather than building an opaque general system. After Priority 2, measure again. Do not promise 60 pages until a complete build reaches it.

A separate attempt to propagate the sharp bound directly from a much smaller finite base could save even more, but no such theorem is established here. The current one-step recurrence has a positive error and does not imply `C_n<=max(C_E,C_{n-1})`. It cannot be presented as that simplification.
