"""Reference formulas for the explicitly assumed models in the C15 note.

No parameter estimation, market data, or live investment recommendations.
consumer: main.conjectures.analysis.c15.full-observation
consumer: main.conjectures.analysis.c15.risk-screen
"""
from dataclasses import dataclass
import math
from statistics import NormalDist


def positive_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def probability(value, name):
    if not math.isfinite(value) or not 0 < value < 1:
        raise ValueError(f"{name} must be strictly between zero and one")


def gaussian_max_cdf(u, n):
    """P(max of n independent absolute standard normals <= u)."""
    positive_integer(n, "n")
    if math.isnan(u):
        raise ValueError("u must not be NaN")
    if u <= 0:
        return 0.0
    tail = math.erfc(u / math.sqrt(2))
    if tail >= 1:  # Very small u can round erfc to one.
        return 0.0
    return math.exp(n * math.log1p(-tail))


def simultaneous_quantile(n, alpha):
    """Exact Gaussian quantile, evaluated through the small upper tail."""
    positive_integer(n, "n")
    probability(alpha, "alpha")
    tail = -math.expm1(math.log1p(-alpha) / n) / 2
    if tail <= 0:
        raise ValueError("Requested tail is below floating-point resolution")
    return -NormalDist().inv_cdf(tail)


def simultaneous_radius(n, r, sigma, alpha):
    positive_integer(r, "r")
    if not math.isfinite(sigma) or sigma <= 0:
        raise ValueError("sigma must be finite and positive")
    return sigma / math.sqrt(r) * simultaneous_quantile(n, alpha)


def gumbel_normalizers(n):
    positive_integer(n, "n")
    a = math.sqrt(2 * math.log(2 * n))
    b = a - (math.log(math.log(2 * n)) + math.log(4 * math.pi)) / (2 * a)
    return a, b


def scheduled_alpha(alpha, t):
    """Predetermined look t in the countable alpha-spending schedule."""
    probability(alpha, "alpha")
    positive_integer(t, "t")
    return (6 * alpha / math.pi**2) / t / t


@dataclass(frozen=True)
class ModelScreen:
    lower_net_mean: float
    log_loss_probability_bound: float
    admissible_under_assumptions: bool


def model_screen(*, estimate, radius, transfer_bound, cost_bound,
                 tail_scale, loss_tolerance, beta):
    """Evaluate Proposition 3; the caller must justify every supplied bound.

    A result never verifies the assumptions. Missing bounds are not replaced
    by zero. Log probabilities avoid underflow to a purported zero risk.
    """
    probability(beta, "beta")
    values = (estimate, radius, transfer_bound, cost_bound, tail_scale, loss_tolerance)
    if not all(math.isfinite(v) for v in values):
        raise ValueError("All model inputs must be finite")
    if min(radius, transfer_bound, cost_bound, loss_tolerance) < 0 or tail_scale <= 0:
        raise ValueError("Bounds must be nonnegative and tail_scale positive")
    lower = estimate - radius - transfer_bound - cost_bound
    standardized_margin = (lower + loss_tolerance) / tail_scale
    if not math.isfinite(lower) or not math.isfinite(standardized_margin):
        raise ValueError("Arithmetic exceeds floating-point range")
    if standardized_margin > math.sqrt(float.fromhex('0x1.fffffffffffffp+1023')):
        raise ValueError("Log bound exceeds floating-point range")
    log_bound = -0.5 * max(0.0, standardized_margin)**2
    accepted = lower > 0 and standardized_margin >= math.sqrt(-2 * math.log(beta))
    return ModelScreen(lower, log_bound, accepted)
