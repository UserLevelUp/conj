# C06 - Dynamic critical spike fidelity universality

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Start a matrix Ornstein-Uhlenbeck process $H_n(t)$ from
the Wigner ensemble of C05. Each independent upper-triangular entry solves
$dh=-h\,dt/2+\sqrt{\nu/n}\,dB$, with $\nu=1$ off the diagonal and
$\nu=2$ on it. Fix $w\in\mathbb R$, a delocalized unit $u_n$ as in C05,
and let $v_n(s)$ be the top eigenvector of
$H_n(sn^{-1/3})+(1+wn^{-1/3})u_nu_n^T$.
Its sign is irrelevant in the fidelity
$Q_n(s,t)=|\langle v_n(s),v_n(t)\rangle|^2$.
Define the Gaussian-reference $Q_n^{\mathrm G}$ by starting from GOE.

**Proposal.** For every $S<\infty$, the bounded-Lipschitz distance between
the laws of $Q_n$ and $Q_n^{\mathrm G}$ in $C([0,S]^2)$ tends to zero.
The statement includes $s=0$ and compares a whole two-time field, not only
stationary one-time eigenvalues.

**Analytic checks performed.** The OU variance remains $1/n$ off-diagonal
and $2/n$ diagonal. Exactly $Q_n(s,s)=1$, $0\le Q_n\le1$, and $Q_n$ is
symmetric. The perturbative ratio of a typical increment coupling
$\sqrt{t/n}$ to an edge gap $n^{-2/3}$ is order
$\sqrt t\,n^{1/6}$, singling out $t=n^{-1/3}$.
This is a scale calculation, not a proof of fidelity universality.

**Alignment/eventness.** Two-time eigendirections are aligned by squared
overlap; their loss of memory is a mathematical event. The proposed
cross-ensemble field-law discrepancy measures model misalignment.

**Context/falsification.** Dyson Brownian motion, eigenvector dynamics, and
critical finite-rank deformation are neighboring theories. Check short-time
non-Gaussian memory and tiny-gap effects. The previous fault-gap bound is
withdrawn: normalized matrix perturbation already gives an $O(\rho)$ bound
under its local degree cap, stronger than that draft's $O(\sqrt\rho)$.
No dynamic-matrix simulation has been performed.

defines: main.conjectures.c06 dynamic critical spike fidelity universality
consumer: main.conjectures.evidence
