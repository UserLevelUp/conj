# C18 - A lattice local limit for fixed-cardinality additive energy

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Fix $\alpha\in(0,1)$, and take $A$ uniformly among
$m=\lfloor\alpha p\rfloor$ element subsets of $\mathbb F_p$, through odd
primes. Let
$E(A)=|\{(a,b,c,d)\in A^4:a+b=c+d\}|$.
Write $\mu_p=\mathbb EE$, $\sigma_p^2=\operatorname{Var}E$.
For sufficiently large $p$, define $h_p$ as the gcd of all nonzero
differences between attainable energy values; let $b_p$ be any attainable
value.

**Proposal.** $\sigma_p^2=\Theta_\alpha(p^3)$ and
$$
\sup_{\ell\in b_p+h_p\mathbb Z}
\left|\frac{\sigma_p}{h_p}\Pr(E=\ell)
-\phi((\ell-\mu_p)/\sigma_p)\right|\longrightarrow0,
$$
where $\phi$ is the standard normal density.
The lattice-corrected local limit is stronger than an ordinary CLT.

**Analytic checks performed.** With
$r_s=|\{(a,b)\in A^2:a+b=s\}|$, exactly
$E=\sum_sr_s^2$ and $\sum_sr_s=m^2$.
Fixing $m$ removes the leading random-cardinality fluctuation of the
Bernoulli model. Repeated indices contribute different terms and cannot
be dropped when determining the lattice span. The arithmetic-geometric
baseline $E\ge m^4/p$ is compatible with fluctuations on the proposed
$p^{3/2}$ scale about the exact mean; it does not prove that variance scale.

**Alignment/eventness.** Compare a discrete collision statistic with
Gaussian point probabilities on its actual attainable lattice.
Misalignment is the supremum displayed above; unusually high collision
energy is the detected structural event.

**Context/falsification.** Degenerate U-statistics, random Fourier fourth
moments, and additive-energy identities are neighboring theory. The claim
must survive conditioning on cardinality, arithmetic contractions, and
possible persistent support holes. Exact small-prime enumeration in the
evidence script checks the observable and lattice definition, not the
asymptotic local limit.

defines: main.conjectures.c18 fixed-cardinality additive-energy lattice local limit
consumer: main.conjectures.evidence
