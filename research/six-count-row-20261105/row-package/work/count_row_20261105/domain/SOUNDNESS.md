# The complete source domain of n=5, BN, panel38

Mathematical status: locally derived exact domain and expectation-interface implications, conditional on the original acquired same-law row. Execution status: fresh rational domain, atom, convolution, polynomial-identity and rejection controls. This file does **not** establish a new score bound on the whole row. The original manuscript and certificates are unchanged.

## 1. The original input and the meaning of a complete row

The original contract is
`work/cutoff5_20261020/root/count5_prepare_v1/gamma16_01/n5/BN/panel038/contract.json`,
SHA256 `2b3f626ba3a9e954e4700bf206cf7a364f44958bb901b463198249dda2f37e48`.
Its entire row is retained, without altered values, in `domain.json` under
`all_original_hypotheses`. In particular:

| Quantity | Exact licensed enclosure |
|---|---|
| Actual index and target | n=5, K=0 |
| p=P(X>0) | [19/50,39/100] |
| ρ=E|X|³ | [11/10,23/20] |
| β=E[X|X|] | [−15293/500000,307221/1000000] |
| γ=EX³ | [−14467/125000,636273/1000000] |
| m=EX₊=EX₋ | [217391/500000,24569/50000] |
| Raw standardized-X sum threshold | −2051019/10⁶ ≤ H ≤ 2051019/10⁶ |
| Negative/positive standardized support radii | 19/10,12/5 |
| Conditional outward bounds A₀,A₁ | 82453/125000,703209/10⁶ |
| Acquired noise cap λ | 7687/25000 |
| Acquired scale cap √w | 547171/10⁶ |
| Acquired actual inward sum d | at most471533/500000 |

Both physical inner endpoints are strictly positive: the negative support endpoint has magnitude at least29529/10⁶, and the positive endpoint at least9459/200000. The source also retains the shared gap/defect, signed phase resources, and original affine intercepts. The latter are d₀=7691481/10⁶ and Λ=965647/125000. Neither is to be replaced inside its original affine constraint by the much smaller independently acquired inward/noise cap. In particular, d₀ is **not** a usable count spacing.

The same-law resource gives a scalar D upper bound, the joint plane

    binary_charge + gap_charge*d + noise_charge*λ ≤ D,

and the six signed phase quadratics. In their declared orientation, these give

    D ≤ min(D_row,15000/(997n) max_i[A_i+F_i,sign |H|−Q_i H²]).

The whole list, including all six quadratics and the independent physical gap, remains part of the input. A new upper-bound proof may drop a restriction, thereby proving an implication on a larger domain, but may not substitute unrelated or independently optimized moment data.

The contract's `resource_verified:false` and `cutoff_proved:false` are preserved. They describe the original conditional artifact. The exact exported resource is
`root/signed_gamma_paired5_v1/BN/panel038.json`, SHA
`7e1d1303ce8ec4888484ac52ec77af45972b77456d2ddb7d74f862d19384c8ab`.
The original `audit/resource5_readback_v4/BN_READBACK.json` selects those same bytes as a retained gamma row, with actual index5, N=5,Q=K=0 and full rho band. Its `check.py` checks the INITIAL seed, both support rays, successive exact resource updates and the entire exported row. The subsequent `audit/count5_readback_v1/check.py` checks that precise source selection and all directed contract interfaces before joining the original count forest. The new domain checker verifies this selection and the relevant scalar projections; it does not rerun those acquisitions or infer their truth from a status string.

Thus a complete new **row** result means: every actual oriented law and threshold satisfying this original simultaneous acquired row has positive closed-event score below the fixed K=0 target. It is not all n=5 laws, all probability panels, all rho bands, or a fresh proof of the acquisition. In the original global argument the row is reached after attainment, contact, the adopted predecessor bound, support, Fourier/INITIAL and resource acquisition. Thresholds beyond the acquired H interval are excluded by those antecedents for the putative witness; this row calculation alone makes no statement about every threshold of every unrelated law.

## 2. Derive the coordinate rather than guessing a count range

Let EX=0, EX²=1, p=P(X>0), q=1−p and m=EX₊=EX₋. Assign a zero atom to the nonpositive class. Set B=1{X>0}. Its two conditional means are −m/q and m/p. With ℓ=m/(pq), define centered conditional residual U by

    X=ℓ(B+U−p),       E[U|B]=0.

Writing v=pq, s=E U²=q E U₀²+p E U₁² and w=v+s, the variance identity gives ℓ²w=1. Hence

    √w = v/m,     λ=ns=n(v²/m²−v),     Y=B+U=p+√w X.

For the **raw sum threshold** H in P(ΣX_i≤H), the exact Bernoulli coordinate is therefore

    h=np+√w H,       P(ΣX_i≤H)=P(ΣY_i≤h).

If h=k+u then the normal argument is

    H/√n=(k+u−np)/√(nw).

There is no extra √n multiplying H in the first formula. In particular, sign(u) and sign(H) need not coincide.

For this row, v lies in [589/2500,2379/10000]. The actual lower mean m_l=217391/500000 gives √w≤v_max/m_l. Since v²/m_l²−v is convex in v, its maximum on this interval is at an endpoint. These exact rational inequalities independently yield the outward caps stated in the contract:

    √w≤547171/10⁶,    λ≤7687/25000.

This justifies removing the portion above the acquired noise cap from a new actual-law comparison, even though the old affine budget retains its much larger Λ. It does not change that affine plane.

Combining both signed H bounds with the full p interval gives

    777741882751/10¹² ≤ h ≤ 3072258117249/10¹².

The left endpoint is strictly above1/2 and the right endpoint strictly below7/2. Every nearest integer is consequently in {1,2,3}. No inference is made from the six mixture counts. A complete sufficient closed phase cover is:

| Nearest k | Negative phase | Positive phase |
|---:|---|---|
|1|[−222258117249/10¹²,0]|[0,1/2]|
|2|[−1/2,0]|[0,1/2]|
|3|[−1/2,0]|[0,72258117249/10¹²]|

At h=3/2 the pairs (k,u)=(1,1/2),(2,−1/2) both occur; at h=5/2 the corresponding pair is (2,1/2),(3,−1/2). Shared faces and u=0 are retained. These boxes enlarge the actual domain by ignoring some correlations with p,H and λ, which is harmless for an upper bound. Using three whole phase intervals [−1/2,1/2] is also a valid further enlargement.

## 3. All six mixture counts remain; atoms and reflection

For every j=0,…,5 let W_j be the sum of j independent copies of U₁ and5−j independent copies of U₀, using the same two actual conditional laws throughout. Then, for every real h, including values outside the licensed row interval,

    P(ΣY_i≤h)=Σ_{j=0}^5 binom(5,j)p^j q^(5−j) P(W_j≤h−j).

The representation with h=k+u changes only the argument to u+k−j. It does not remove any j and does not require a positive spacing. A majorant for the closed CDF must be at least1 at a collision W_j=h−j. The six-polynomial method can therefore cover zero noise and atoms without an outgoing/incoming approximation or division by a small gap.

This row has the original orientation p∈[.38,.39]. Reflection does not leave it invariant. Precisely,

    Φ(H/√n)−P(S_n≤H)
      = P(−S_n<−H)−Φ(−H/√n).

The event on the right is strict; using a reflected closed CDF adds the atom at −H. It is a safe upper bound, not an equality. With no zero atom the reflected positive probability is1−p, so it lies in[.61,.62], and β changes sign. The acquired positive inner gap excludes a zero atom on this row; without that premise the reflected positive probability is1−p−P(X=0). The original attainment/reflection reduction must supply the correctly oriented row. A positive-score certificate on this single p panel is not an absolute-discrepancy theorem for that panel by itself.

## 4. Fixed outer beta polygon and degree(9,4)

Put x=q E U₀² and y=p E U₁². The actual sign condition gives exactly

    β=[v(q−p)−x+y]/[v+x+y].

The denominator is positive. Therefore, with the original β limits b_l,b_u,

    −(1+b_u)x+(1−b_u)y ≤ v(b_u−1+2p),
     (1+b_l)x−(1−b_l)y ≤ v(1−2p−b_l).

Together with x,y≥0 and x+y≤Λ_acquired/5 these define the actual variance restriction. On a fixed p-cell [l,h], replace each cubic right side by a rational **upper** bound valid throughout the cell. Degree-three Bernstein coefficients after p=l+(h−l)t supply such a bound by their maximum. The resulting rational polygon contains every actual pair for every p on the cell. Its vertices are fixed constants, independent of p,u,skew and inward endpoints. Complete intersection of the five closed halfplanes computes them; no sampled feasibility criterion is used.

Let fixed inward caps be r₀=min(d,h), r₁=min(d,1−l), and keep the original fixed outward A₀,A₁. For any fixed p,x,y, the actual fourth-moment inequalities follow by integrating (U₀+A₀)(a₀−U₀)U₀²≥0 and its class-one counterpart. Maximizing the mixture expectation with nonnegative quartic leading coefficients first over the two actual skew ratios and then over inward endpoints leaves the nine shared pairs

    γ₀∈{−A₀,0,r₀},       γ₁∈{A₁,0,−r₁}.

Both classes retain one common moment choice across all counts. At these extremal evaluations the support part of the fourth moment has price γ_i²s_i; this is not the false actual-law assertion E U_i⁴≤γ_i²s_i. If a variance is zero its terms vanish, without dividing by it. Dropping the shared inward-simplex restriction enlarges the domain safely.

For fixed γ₀,γ₁, at count j put

    t_j=(5−j)x/q+j y/p,
    M₃,j=(5−j)γ₀x/q+jγ₁y/p,
    M₄,j≤(5−j)γ₀²x/q+jγ₁²y/p+(12/5)t_j².

Indeed, independence gives the exact correction −3ΣVar(Z_i)², and Cauchy gives ΣVar(Z_i)²≥t_j²/5. This positive-square bound makes the full mixture expectation convex in (x,y), so it is enough to test each vertex of the fixed outer polygon and each of the nine shared pairs. Retaining the exact negative diagonal correction instead would not, in general, preserve this convexity.

For fixed rational quartics P_j and the shift j−k−u, each resulting expectation is rational in p and polynomial in u. Its only possible denominators are p²q². Multiplication by the strictly positive (pq)² produces a polynomial of degree at most9 in p and4 in u: the mass is degree5, the clearing factor degree4, the fixed-vertex moment numerators add no higher degree, and each shift has degree at most4 in u. More explicitly, linear moment factors have cleared p powers p^(j+2)q^(6−j) or p^(j+1)q^(7−j), and squared-variance factors have total degree7. The constant-moment term has total degree9.

This degree claim depends on using **fixed cell endpoint** inward caps, not pointwise γ₀=p or γ₁=−q. The latter choices can raise the naïvely cleared fourth-moment degree to10. The constructor has explicitly selected the fixed-endpoint convention.

A safe scalar target can be held constant on each cell. If a=k+u_l−5p_h, w_l=v_l and w_h=v_h+Λ_acquired/5, then the normal argument is at least a/√(5w_h) for a≥0, and at least a/√(5w_l) for a<0. An outward lower Gaussian bound there, plus c_*ρ_l/√5_upper for a positive rational c_*≤C_E, gives a sufficient target for the mixture CDF. This treats the actual sign of the normal numerator and does not confuse it with phase sign. A strict polynomial reserve against that constant implies the desired positive score bound.

## 5. What has run and what remains

`domain.json` is the exact source-bound census, not a score certificate. Its checker returned actual exit0 in `runs/count_row_20261105/analytic_domain01/PROCESS.json`. The result pins every source and records:

-38 threshold test points and45 exact coordinate checks;
-128 same-marginal mixture equalities,128 strict-reflection equalities and104 exact atom collisions;
-9 signed-beta actual-law checks;
-108 independently expanded cleared moment polynomials,972 direct rational evaluation identities, maximum degrees(9,4);
-20 rejected corrupt domain objects, including a missing root, omitted atom face, nearest/mixture confusion, changed target, replaced original affine Λ, altered source hash and duplicate JSON keys.

The continuous assertions are proved above; the finite checks exercise their implementation. Some test laws intentionally include a zero atom or do not satisfy all acquired scalar restrictions, solely to test the general algebra and event convention. They are not reported as acquired maximizing laws.

Remaining: exact global majorants and complete closed score acceptance on the declared p/phase roots (with all noise and common moments), plus the unchanged original acquisition boundary. No complete new row, manuscript deletion, whole n=5 improvement or overall theorem is inferred from these domain checks.
