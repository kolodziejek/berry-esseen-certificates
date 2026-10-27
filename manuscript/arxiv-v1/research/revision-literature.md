# Literature audit for the proposed manuscript revision

Checked 27 October 2026 in branch `manuscript/v2-literature-20261027`, starting
from `ec370aa`. The supplied revision files are proposals, not source authority.
This review changes only the selected additional bibliography and this report;
it does not alter the introduction, author information, or theorem statements.

| Result type | Mathematical status | Execution status |
|---|---|---|
| Cited theorems below | External results; stated scope checked to the extent recorded | No external proof computation or formal development replayed |
| Zero-bias identification and biased-antichain implication | Elementary implications independently derived below | No numerical experiment needed |
| Historical bounds | Distinguish a directly inspected theorem/abstract from a later author's historical attribution | Metadata and available primary text read; inaccessible original text identified |

## Selected additions and exact provenance

Six entries are supplied in `references-added.bib`. They identify methods
actually used or a concise historical milestone. The three optional background
items discussed later are not added merely to expand the bibliography.

| Key | Primary evidence and scope | Editorial decision |
|---|---|---|
| `Shiganov1986` | [Springer article record](https://link.springer.com/article/10.1007/BF01121471) gives I. S. Shiganov, the supplied title, volume 35, pp. 2545–2550, November 1986, and DOI `10.1007/BF01121471`; it identifies the 1982 Russian original, pp. 109–115. Its navigation names the historical journal *Journal of Soviet Mathematics*, although its generated citation uses the later journal name. | Keep one English citation. Do not add the proposed `Shiganov1982` as a second English article. The original theorem text was paywalled; numerical attribution has the separate status below. Optional issue number omitted. |
| `HippMattner2008` | [SIAM publisher record](https://epubs.siam.org/doi/10.1137/S0040585X97983213) gives 52(3), 516–523, **2008**, and DOI. [MathNet's original/translation record](https://www.mathnet.ru/php/archive.phtml?jrnid=tvp&option_lang=rus&paperid=82&wshow=paper) gives original edition 52(3), 610–617, 2007. [Author manuscript](https://www.math.uni-trier.de/~mattner/Papers/NormBin20050401.pdf), introductory text retrieved through the search index, identifies Christian Hipp and Lutz Mattner and states the exact symmetric-Bernoulli supremum. Repeated direct PDF fetches timed out. | Replace the proposal's key `HippMattner2007` by `HippMattner2008`. The theorem is for symmetric Bernoulli sums; it does not establish the all-parameter binomial result. |
| `GoldsteinReinert1997` | [Author-submitted arXiv record](https://arxiv.org/abs/math/0510619v1) supplies title, authors, journal reference and DOI. Its [paper](https://arxiv.org/pdf/math/0510619v1), Definition 1.1 and Lemma 2.1(2), introduces the transform and gives its density. The [author-hosted copy](https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/zertr.pdf) has the same definitions; its typesetting date 2014 is not the publication year. | Cite the 1997 journal article for the density identity. Neither the 2005 arXiv upload nor the later typesetting date is a separate result. |
| `Lubell1966` | [Original one-page article scan](https://sites.math.rutgers.edu/~zeilberg/akherim/lubell1966.pdf), p. 299, contains the full chain-counting proof. [Publisher record](https://www.sciencedirect.com/science/article/pii/S0021980066800352), retrieved through its indexed text, supplies volume 1(2), September 1966, p. 299, and DOI. | This is the direct methodological reference for the manuscript's random-chain argument. Use the original signature D. Lubell rather than guessing an expanded name. |
| `Erdos1945` | [Rényi archive of the original article](https://www.renyi.hu/~p_erdos/1945-04.pdf), pp. 898–902, particularly Theorem 1 and proof on p. 898; [AMS issue listing](https://doi.org/10.1090/S0002-9904-1945-08488-2) gives the article DOI ending `08454-7`. | Useful in one sentence explaining the Littlewood–Offord antecedent. It is not the source of a general biased-product theorem. |
| `Tyurin2010` | [MathNet journal record](https://www.mathnet.ru/eng/rm9337) and indexed [published first page](https://www.mathnet.ru/links/3f8261e0e428180fb7d3b53331a406f3/rm9337_eng.pdf): RMS 65(3), 586–588, DOI `10.1070/RM2010v065n03ABEH004688`. Its theorem states 0.4785 for iid summands and 0.5606 for independent summands. | Prefer this published short announcement for the historical number; use existing `Tyurin2009` when discussing the detailed argument. Do not present the two as independent improvements. |

## Actual methodological connections

**Zero bias.** For a centered variable with variance one, Goldstein–Reinert
give a density `t -> E[X 1{X>t}]`. The manuscript uses `>=` in
`sections/05-geometry-counts.tex:69` and
`appendices/fourier-analysis.tex:805`. These versions agree Lebesgue almost
everywhere, not necessarily at an atom. For an absolutely continuous test
function with bounded derivative, independently splitting at zero and applying
Fubini gives

\[
 \int_{\mathbb R} f'(t)\tau(t)\,dt
 =\mathbb E[X(f(X)-f(0))]=\mathbb E[Xf(X)].
\]

Finite second moment justifies the integral; taking `f(t)=t` gives mass one.
Thus the manuscript's `tau` is a version of the zero-bias density. This
identification does not prove the later gap or Fourier inequalities. Proposed
wording should say “a version of this density” and should not imply that the
zero-bias literature already supplies the new conserved-resource inequality.

**Antichains.** Lubell proves
\(\sum_{A\in\mathcal F}\binom{N}{|A|}^{-1}\le1\) for an antichain.
Independently, if `a_k` counts its sets of size `k`, then for `0<p<1`,

\[
 \mathbb P_p(\mathcal F)
 =\sum_k\frac{a_k}{\binom Nk}\binom Nk p^k(1-p)^{N-k}
 \le\max_k\binom Nk p^k(1-p)^{N-k}.
\]

This is precisely the implication at
`appendices/fourier-analysis.tex:3568–3595`. Positive weights bounded below by
`c` make an interval event an antichain when its diameter is strictly less than
`c`; equality of the diameter needs endpoint care. Erdős's Theorem 1 concerns
real coefficients of absolute value at least one and **open** intervals of
length two, with equiprobable signs after division by `2^N`. Cite him for the
antecedent, and Lubell for the weighted-cardinality argument actually used.

**Symmetric binomial laws.** Hipp–Mattner identify
\(\sup_{n\ge1}\sqrt n\,\Delta_n=1/\sqrt{2\pi}\) for a standardized symmetric
Bernoulli law. Their introductory description points to exact distances in
Corollary 1.4 and the sharp constant in Corollary 1.5 of the author manuscript.
The inspected abstract/introduction supports the weak bound and optimal
uniform constant. I do not supply a finite-`n` strictness locator from a full
original proof that was not retrieved. This is a separate special case from
Schulz's all-binomial theorem. Strict and closed CDF conventions have the same
Kolmogorov supremum against a continuous Gaussian CDF; that observation alone
does not settle attainment at a specified atom.

## Historical claims: keep the scope and the edition together

The proposed full chronology is unnecessary. The following is a bounded
selection suitable for a short paragraph or carefully labelled table.

| Claim | Evidence inspected | Recommendation |
|---|---|---|
| Berry 1.88; Esseen 7.59 | These numbers occur in later presentations, but the relevant original statements and normalizations were not directly verified here. Tyurin's historical account instead cites Esseen 7.5. | Do not certify the proposed early numerical entries from this audit. Cite the foundational papers without numerical values. |
| Zolotarev 0.9051 | [Tyurin's original research manuscript](https://arxiv.org/pdf/0912.0726v1), p. 2, distinguishes the general value 0.9051 from the iid value 0.8197. | 0.9051 is a valid inherited bound for iid laws but is misleading as the best iid milestone. Omit the row rather than guess the original theorem locator. |
| van Beek 0.7975; Shiganov 0.7915 general / 0.7655 iid; Shevtsova 0.7056 iid | Same historical account, p. 2. This is a later primary research account, **not** direct inspection of each earlier theorem. | If retained, distinguish the classes. Cite Shiganov's English 1986 edition once, noting original 1982 if desired. |
| Tyurin 0.4785 iid / 0.5606 general | Published theorem on p. 586 of the [2010 paper](https://www.mathnet.ru/links/3f8261e0e428180fb7d3b53331a406f3/rm9337_eng.pdf). The [longer 2009 preprint](https://arxiv.org/abs/0912.0726v1) explains a convex moment reduction and zero-bias estimates feeding characteristic-function bounds. | Replace “introduced zero-bias transformations” by “used zero-bias estimates and characteristic-function bounds.” Do not describe it as avoiding Fourier analysis. |
| Korolev–Shevtsova 0.5129 iid | The [publisher abstract](https://epubs.siam.org/doi/abs/10.1137/S0040585X97984449) explicitly states the scope and number. | Supported; existing English citation year 2010 is correct (original 2009). |
| Shevtsova 0.4748 iid | [Original 2011 arXiv abstract](https://arxiv.org/abs/1111.6554v1) states all `n>=1` and derives this from 0.33554(`rho`+0.415). | Supported as a structural improvement; no numerical replay performed. |
| Shevtsova 0.4690 iid | [Two-page original](https://www.mathnet.ru/php/getFT.phtml?jrnid=ia&option_lang=eng&paperid=252&what=fullt), pp. 124–125, gives the iid minimum with coefficients 0.4690, 0.3322, 0.3031. | In standardized iid notation retain **0.4690 rho**, not 0.4690 or a separate `rho` term. General independent bound is 0.5583. |

The fixed-law asymptotic formula must not be substituted for a uniform
triangular-array result. [Shevtsova 2012](https://publikacio.uni-eszterhazy.hu/3231/1/AMI_39_from241to307.pdf),
printed pp. 243–244, explicitly fixes the law in the Esseen expansion and
records the lattice/skewness formula and extremal two-point weights. Its
Corollary 4.7 and Remark 4.9 (pp. 284–286) discuss a *different* optimal
two-term structure: in the iid case the leading terms are
`2 rho/(3 sqrt(2 pi n)) + E|X|/(2 sqrt(2 pi n))`, with a quadratic
Lyapunov-ratio remainder. “Asymptotically optimal” must identify which
statement and quantifiers are intended. The valid weights sum to one:
`p=(4-sqrt(10))/2`, `q=(sqrt(10)-2)/2`; the proposed abstract's paired
`(4∓sqrt(10))/2` expression is false.

## Proposals not added, and other corrections

- **Goldstein 2010:** [Original published paper](https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/3pt-1.pdf),
  pp. 1672–1674, verifies the supplied metadata and DOI `10.1214/10-AOP527`.
  Theorem 1.1 gives the upper constant **one** for integrated absolute CDF
  distance; it does not prove this to be the sharp finite-sample mean-CLT
  constant. Its displayed lower bound is about 0.535377. The proposal's
  “sharp constants in related problems” is too imprecise. Omit the citation
  unless a specific mean-distance comparison is added.
- **Chen–Goldstein–Shao 2011:** the [publisher record](https://link.springer.com/book/10.1007/978-3-642-15007-4)
  verifies the authors, title, *Probability and Its Applications*, Springer
  Berlin Heidelberg, 2011, DOI `10.1007/978-3-642-15007-4`. Sound background
  reference, but unnecessary when the manuscript only needs the specific
  original zero-bias identity. No book theorem has been used as a proof input.
- **Bhattacharya–Ranga Rao 1976:** the [SIAM reprint's copyright page and preface](https://epubs.siam.org/doi/pdf/10.1137/1.9780898719895.fm)
  confirm the Wiley 1976 original, followed by corrected editions in 1986 and
  2010; [Korolev–Shevtsova's bibliography](https://epubs.siam.org/doi/abs/10.1137/S0040585X97984449)
  confirms Wiley, New York. The proposed original-edition entry is sound.
  If citing the 2010 edition actually inspected, use SIAM, Philadelphia,
  *Classics in Applied Mathematics* 64 and DOI `10.1137/1.9780898719895`.
  Do not attach that DOI to a 1976 Wiley entry. No full Edgeworth theorem from
  the book was inspected; it should not replace the direct classical source.
- The revision instructions' `Shiganov1982` entry has the wrong English DOI
  `10.1007/BF01099124` and wrong terminal page 2551. Its duplicate English
  record should not be created. The proposed Tyurin title is not the
  publisher's English title; `references-added.bib` uses the verified title.
- The normalized recurrence in the supplied introduction has a substantive
  transcription error: `sqrt(n)/(n-1)^(3/2)` is of order `1/n`, not
  `n^(-3/2)`. The latter order is the unnormalized smoothing error. The parent
  editor was notified and is using the exact recurrence instead.
- Later numerical or formal claims remain attributed to the inspected
  external manuscripts and versions. None of this bibliography work upgrades
  their execution status or the present conditional finite-base/local suite.

## Suggested concise prose

For insertion with the indicated keys, without inflating the historical list:

> For symmetric Bernoulli summands, Hipp and Mattner determined the optimal
> uniform constant `1/sqrt(2 pi)` (`HippMattner2008`). The all-binomial
> theorem used below is the separate result of Schulz (`Schulz2016`).

> The function `tau` is a version of the zero-bias density introduced by
> Goldstein and Reinert (`GoldsteinReinert1997`, Lemma 2.1(2)). We use its
> integral identity together with the contact inequality to derive the
> resource relation below.

> The concentration step uses the antichain principle behind the real
> Littlewood–Offord inequality of Erdős (`Erdos1945`). Lubell's chain-counting
> inequality (`Lubell1966`) gives the biased Bernoulli bound required here.

These are proposed summaries, not quotations from the sources. Source text
was read through publisher pages, original scans or author manuscripts;
search-index-only access is explicitly marked. No external service was
modified, no paid access obtained, and no external proof computation run.
