# C15 - Simultaneous mastery inference with low-rank context effects

**Status:** candidate conjecture in a hypothetical model. No clinical or
empirical assertion about ADHD, intelligence, or real learners is made.

**Definitions.** Let $n$ learners and $r$ assessment contexts satisfy
$c\le n/r\le C$. Their mean-score matrix is
$$M=\theta{\bf1}_r^T+UV^T,\qquad V^T{\bf1}_r=0,$$
where $\theta_i$ is the model's context-averaged mastery parameter.
The rank of $M$ is a fixed $s\ge2$, its left and right singular-vector
matrices $L,R$ obey
$\max_i\|L_{i,*}\|^2\le\mu s/n$ and
$\max_j\|R_{j,*}\|^2\le\mu s/r$, and its nonzero singular values lie in
$[c\sqrt{nr},C\sqrt{nr}]$. Here $c,C,\mu$ are fixed positive constants.
Require ${\bf1}_r$ to belong to the row space of $M$.
Independently observe each entry with probability $p$, with independent
$N(0,\sigma^2)$ error, fixed $\sigma>0$, and
$p\min(n,r)/\log^{12}(n+r)\to\infty$.

**Proposal.** There is a polynomial-time estimator $\widehat\theta$, not given
$U,V$, for which the following holds uniformly over this matrix class.
Define $a_N=\sqrt{2\log N}$ and
$b_N=a_N-(\log\log N+\log(4\pi))/(2a_N)$. For every real $x$,
$$
\Pr\left[
a_{2n}\left(\max_{i\le n}
\frac{\sqrt{pr}\,|\widehat\theta_i-\theta_i|}{\sigma}-b_{2n}\right)
\le x\right]\longrightarrow \exp(-e^{-x}).
$$
This sharp simultaneous extreme-value law with unknown nuisance structure
is the target, not an elementary union-bound regret upper bound.

**Analytic checks performed.** Centering $V$ makes
$M{\bf1}_r/r=\theta$ identifiable under complete observation. For the
rank-$s$ tangent-space projection $P_T$,
$P_T(e_i{\bf1}_r^T/r)=e_i{\bf1}_r^T/r$ because ${\bf1}_r$ is in the row
space. Its squared Frobenius norm is $1/r$, supporting the proposed
efficient variance $\sigma^2/(pr)$ rather than a guessed noise scale.
At $p=1$, row averages have independent exact $N(0,\sigma^2/r)$ errors:
the absolute Gaussian maximum supplies the $2n$ normalization.

**Alignment/eventness.** An inferred ranking is compared only with
context-averaged mastery in this model. For any $1\le k<n$, a true top-$k$
gap exceeding
$2(1+\eta)\sigma b_{2n}/\sqrt{pr}$, fixed $\eta>0$, would give exact top-$k$
selection with probability tending to one under the proposal.
For $k=n$ selection is tautological and no lower bound or sharpness claim is
made. Ties do not define a unique high-achiever set.

**Interpretation/context/falsification.** In the user's hypothetical
attention-variable world, varied assessment contexts permit separation of
mastery from systematic context fit; the model does not diagnose anyone.
[Xia and Yuan](https://arxiv.org/abs/1909.00116) treat inference of individual
linear forms in noisy matrix completion. Their primary text was consulted;
it does not by itself certify this uniform maximum law. Check existing
simultaneous-inference results, debiasing remainder at extreme tails,
identifiability under missingness, and correlated errors. No missing-data
estimator experiment has been performed.

defines: main.conjectures.c15 hypothetical mastery inference with context nuisance
consumer: main.conjectures.evidence
