# C04 - Differentiable near-critical crossing profiles

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Use site percolation on the triangular lattice of mesh $1/n$
inside the unit square, with free boundary and left-right occupied crossing
indicator $f_n$. Let $\alpha_4(n)$ be the critical alternating four-arm
probability from lattice distance 1 to $n$ in the plane. Set
$a_n=(n^2\alpha_4(n))^{-1}$ and
$F_n(\lambda)=\mathbb E_{1/2+\lambda a_n}f_n$.

**Proposal.** There is a nonconstant $F\in C^2(\mathbb R)$ with
$F'(\lambda)>0$ everywhere such that, for every compact $K\subset\mathbb R$,
$$
\max_{j=0,1,2}\sup_{\lambda\in K}|F_n^{(j)}(\lambda)-F^{(j)}(\lambda)|
\longrightarrow0.
$$
The differentiability and convergence of derivatives, not just convergence
of crossing probabilities, are the proposed target.

**Analytic check performed.** For majority on $2m+1$ bits,
$\mu'(p)=(2m+1)\binom{2m}{m}p^m(1-p)^m$.
Thus the logarithmic slope derivative at $1/2$ is zero, yet
$\mu'(1/2+c/\sqrt{2m+1})/\mu'(1/2)\to e^{-2c^2}$.
This explicitly rejects the previous implication from a derivative at one
point to constant slope over a whole window. C04 no longer asserts flatness.

**Alignment/eventness.** Compare the discrete probability, pivotal intensity,
and curvature profiles with one common continuum profile. The displayed
$C^2$ discrepancy is misalignment; the event is crossing emergence.

**Context and falsification.** Garban, Pete, and Schramm establish
[near-critical scaling limits](https://arxiv.org/abs/1305.5526).
That baseline alone does not justify interchanging limits and derivatives.
Investigate second-order pivotal correlations and possible curvature
singularities. No percolation simulation or proof of this strengthening has
been performed. See the portfolio evidence artifact for the majority check.

defines: main.conjectures.c04 differentiable near-critical crossing profile
consumer: main.conjectures.evidence
