# C21 - Analytic conditional response of global patterns to peak density

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** For uniform $\pi\in S_n$, let $K_n$ count interior peaks
$\pi_{i-1}<\pi_i>\pi_{i+1}$, and let $X_n$ count triples
$i<j<k$ with $\pi_i<\pi_k<\pi_j$ (132 patterns).
Set $\mu_n=\binom n3/6$.

**Proposal.** There is a real analytic, nonidentically-zero
$g:(0,1/2)\to\mathbb R$, with $g(1/3)=0$, such that for every interval
$K=[a,b]$ with $0<a<b<1/2$,
$$
\sup_{k:\,k/n\in K}
\left|n^{-2}(\mathbb E[X_n\mid K_n=k]-\mu_n)-g(k/n)\right|
\longrightarrow0.
$$
The scale, nonzero response, and analytic regularity are requirements,
not an unspecified function chosen separately at each $n$.

**Analytic checks performed.** Each triple has six equally likely relative
orders, giving exactly $\mathbb EX_n=\binom n3/6$, not $n^3/6$.
Each interior position is a peak with probability $1/3$, so
$\mathbb EK_n=(n-2)/3$. The typical peak density thus constrains the
candidate response; conditioning on rare densities is not justified by
an unconditioned CLT. Exact enumeration through $n=8$ is recorded in the
evidence artifact; it checks centering and gives finite conditional responses.
It does not establish the $n^2$ asymptotic scale.

**Alignment/eventness.** Compare a local-extrema constraint with the
global pattern response. The displayed uniform residual is misalignment;
the event is a prescribed atypical peak density.

**Context/falsification.** Permutation peak enumerators, local-interaction
tilting, and pattern cumulants are neighboring theory. Test whether the
leading $n^3$ coefficient changes under conditioning, whether $g$ vanishes
identically, or whether boundary effects create a nonanalytic response.
Any such finding would require replacement, not a caveat asserting success.

defines: main.conjectures.c21 analytic peak-conditioned pattern response
consumer: main.conjectures.evidence
