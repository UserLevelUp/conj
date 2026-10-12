"""Deterministic tests of formulas, boundaries, and assumption failures.

trigger: main.conjectures.analysis.c15.full-observation
trigger: main.conjectures.analysis.c15.risk-screen
"""
import math
from statistics import NormalDist
import unittest

from tools.c15_bounds import (
    gaussian_max_cdf, gumbel_normalizers, model_screen, scheduled_alpha,
    simultaneous_quantile, simultaneous_radius,
)


class C15Tests(unittest.TestCase):
    def test_exact_coverage(self):
        for n in (1, 2, 100, 10**6, 10**12):
            for alpha in (0.001, 0.05, 0.5):
                with self.subTest(n=n, alpha=alpha):
                    q = simultaneous_quantile(n, alpha)
                    self.assertAlmostEqual(gaussian_max_cdf(q, n), 1-alpha, places=12)

    def test_small_tail_quantile_is_finite(self):
        q = simultaneous_quantile(10**12, 1e-8)
        self.assertTrue(math.isfinite(q))
        self.assertGreater(q, 9)

    def test_row_centering_cancels_without_fitting(self):
        theta = [2, 4, -1, 3]
        left, right = [1, -1, 1, -1], [1, 1, -1, -1]
        errors = [[1, 2, 3, 4], [0, 0, 0, 0], [-4, 3, 1, 0], [2, 2, 0, 0]]
        for i in range(4):
            row = [theta[i] + left[i]*right[j] + errors[i][j] for j in range(4)]
            self.assertEqual(sum(row)/4 - theta[i], sum(errors[i])/4)

    def test_missing_raw_mean_does_not_cancel_context(self):
        # Only the first of two centered contexts is observed, with no noise.
        theta, contexts = 3, [7, -7]
        observed = theta + contexts[0]
        self.assertNotEqual(observed, theta)
        self.assertEqual(observed-contexts[0], theta)  # Oracle subtraction.

    def test_context_correlation_breaks_claimed_radius(self):
        # All r context errors are the same N(0,1) within each independent row.
        n, r = 10, 25
        incorrect_radius = simultaneous_radius(n, r, 1, 0.05)
        self.assertLess(gaussian_max_cdf(incorrect_radius, n), 0.01)

    def test_finite_gumbel_cdf_against_direct_formula(self):
        n, x = 32, 0.5
        a, b = gumbel_normalizers(n)
        u = b + x/a
        direct = (2*NormalDist().cdf(u)-1)**n
        self.assertAlmostEqual(gaussian_max_cdf(u, n), direct, places=13)

    def test_radius_search_penalty_and_sample_scaling(self):
        self.assertGreater(simultaneous_radius(100, 25, 1, 0.05),
                           simultaneous_radius(1, 25, 1, 0.05))
        self.assertAlmostEqual(simultaneous_radius(10, 100, 1, 0.05)*2,
                               simultaneous_radius(10, 25, 1, 0.05))

    def screen(self, **changes):
        args = dict(estimate=4.0, radius=0.25, transfer_bound=0.25,
                    cost_bound=0.5, tail_scale=1.0, loss_tolerance=0.0, beta=0.05)
        args.update(changes)
        return model_screen(**args)

    def test_both_criteria_required(self):
        self.assertTrue(self.screen().admissible_under_assumptions)
        # Positive mean bound alone is insufficient for the tail criterion.
        self.assertFalse(self.screen(estimate=1.1).admissible_under_assumptions)
        # A large tolerated loss can satisfy the tail criterion with negative mean.
        result = self.screen(estimate=0.5, loss_tolerance=10)
        self.assertLess(result.log_loss_probability_bound, math.log(0.05))
        self.assertFalse(result.admissible_under_assumptions)
        self.assertFalse(self.screen(estimate=1).admissible_under_assumptions)

    def test_gaussian_actual_tail_below_chernoff_bound(self):
        for estimate in (2, 3, 4, 5):
            result = self.screen(estimate=estimate)
            exact = 0.5*math.erfc(result.lower_net_mean/math.sqrt(2))
            self.assertLessEqual(exact, math.exp(result.log_loss_probability_bound))

    def test_invalid_inputs_rejected(self):
        for n in (0, -1, 2.5, True):
            with self.assertRaises(ValueError):
                simultaneous_quantile(n, 0.05)
        for alpha in (0, 1, float('nan')):
            with self.assertRaises(ValueError):
                simultaneous_quantile(2, alpha)
        for changes in ({'radius': -1}, {'tail_scale': 0}, {'estimate': float('inf')},
                        {'cost_bound': -1}, {'beta': 1}, {'transfer_bound': float('nan')}):
            with self.assertRaises(ValueError):
                self.screen(**changes)

    def test_schedule_spends_at_most_budget(self):
        alpha, steps = 0.05, 10000
        total = math.fsum(scheduled_alpha(alpha, t) for t in range(1, steps+1))
        self.assertLess(total, alpha)
        self.assertLess(alpha-total, 6*alpha/(math.pi**2*steps))

    def test_cdf_boundaries(self):
        self.assertEqual(gaussian_max_cdf(-1, 2), 0)
        self.assertEqual(gaussian_max_cdf(0, 2), 0)
        self.assertEqual(gaussian_max_cdf(float('inf'), 2), 1)
        with self.assertRaises(ValueError):
            gaussian_max_cdf(float('nan'), 2)


if __name__ == '__main__':
    unittest.main()
