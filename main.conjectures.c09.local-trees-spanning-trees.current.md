# C09 - Gaussian spanning-tree residual after growing-cycle conditioning

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Let $G_n$ be uniform among connected simple $d$-regular
graphs, fixed $d\ge3$, $nd$ even. Let $C_j$ count unoriented simple
$j$-cycles, and let $\mathcal C_n=\sigma(C_3,\ldots,C_{r_n})$ with
$r_n=\lfloor\log\log n\rfloor$. Put
$T_n=\log\tau(G_n)$,
$m_n=\mathbb E[T_n\mid\mathcal C_n]$, and
$v_n=\operatorname{Var}(T_n\mid\mathcal C_n)$.

**Proposal.** With probability tending to one $v_n>0$, and
$$
d_{\rm BL}\left(\mathcal L((T_n-m_n)/\sqrt{v_n}\mid\mathcal C_n),
N(0,1)\right)\longrightarrow0
$$
in probability. Here $d_{\rm BL}$ tests functions bounded by 1 with
Lipschitz constant at most 1. Conditioning, centering, and scale are exact:
this is a quenched residual law, not a guessed $\sqrt n$ normalization.

**Analytic checks performed.** Since $r_n=o(\log n)$,
$(d-1)^{2r_n}/n\to0$; a simultaneous positive limit for that expression is
impossible. Cycle counts near $r_n$ nevertheless have diverging heuristic
means $(d-1)^{r_n}/(2r_n)$, so removing an increasing initial cycle segment
can plausibly leave many individually small contributions. A vanishing
unscaled residual would not prove its standardized Gaussian law.
For $K_4$, the matrix-tree cofactor determinant is 16, checking the
spanning-tree observable independently of cycle heuristics.

**Alignment/eventness.** Short-cycle information is aligned with the part
of global tree entropy it explains. Conditional Gaussianity tests the
remaining misalignment; cycle discovery changes the available evidence.

**Context/falsification.** [Greenhill, Kwan, and Wind](https://arxiv.org/abs/1309.6710)
study spanning trees and small-subgraph conditioning. Their primary
cycle-interaction section was consulted; no unverified cycle coefficient
from a search summary is used here. Check quantitative residual errors,
conditional variance, and whether known growing-cycle results already imply
the claim. No random-graph residual experiment has been performed.

defines: main.conjectures.c09 growing-cycle conditional tree-entropy residual
consumer: main.conjectures.evidence
