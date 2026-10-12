# C03 - An exact long-time amplitude for critical crossing memory

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Let $f_n$ be the critical triangular-lattice left-right
crossing indicator in the unit square. Each site is resampled at rate
$a_n=(n^2\alpha_4(n))^{-1}$, with $\alpha_4$ the critical alternating
four-arm probability to distance $n$. Start the dynamics in equilibrium.
Define
$C_n(t)=\operatorname{Cov}(f_n(\omega(0)),f_n(\omega(t)))$.

**Proposal.** Writing $C(t)=\lim_{n\to\infty}C_n(t)$, there is
$c_{\square}\in(0,\infty)$ such that
$$\lim_{t\to\infty}t^{2/3}C(t)=c_{\square}.$$
The order of limits and four-arm normalization are fixed. An exact finite
positive amplitude, rather than an exponent up to unspecified factors, is
the proposed strengthening.

**Analytic checks performed.** Under fair-product measure the Fourier
expansion gives
$C_n(t)=\sum_{S\ne\varnothing}\widehat f_n(S)^2e^{-a_n t|S|}$.
Consequently $C_n\ge0$ and every derivative alternates sign; this is a
Laplace transform, not an arbitrary covariance profile. If the scaled
spectral-sample mass near zero were $b u^{2/3}(1+o(1))$, integration by parts
would give $c_{\square}=b\Gamma(5/3)$. Obtaining that exact lower-tail
amplitude is an unresolved step, not evidence already established here.

**Alignment/eventness.** Compare long-time event memory with the
spectral-sample lower tail. Drift of $t^{2/3}C(t)$ is misalignment.

**Context/falsification.** The Fourier spectrum and dynamical scaling limits
of critical percolation are established neighboring work of Garban, Pete,
and Schramm ([scaling-limit source](https://arxiv.org/abs/1305.5526)).
Check whether stronger spectral-tail results already establish the exact
amplitude, or instead produce slowly varying corrections. No percolation
experiment has been performed.

defines: main.conjectures.c03 exact dynamical crossing-memory amplitude
consumer: main.conjectures.evidence
