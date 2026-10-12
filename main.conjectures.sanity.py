"""Reproducible sanity checks; none proves an asymptotic conjecture."""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache, reduce
from itertools import combinations, permutations
import json
import hashlib
import math
from pathlib import Path
import platform

import numpy as np


def missing_probability(s, m, q):
    distance = min(s, 2 * m - 2 - s)
    return (1 - q * q) ** ((distance + 1) // 2) * (
        (1 - q) if distance % 2 == 0 else 1
    )


def energy(a, p):
    counts = Counter((x + y) % p for x in a for y in a)
    return sum(v * v for v in counts.values())


def increasing_counts(values):
    n = len(values)
    dp = [[0] * (n + 1) for _ in values]
    for i, value in enumerate(values):
        dp[i][1] = 1
        for j in range(i):
            if values[j] < value:
                for k in range(2, n + 1):
                    dp[i][k] += dp[j][k - 1]
    return [sum(row[k] for row in dp) for k in range(n + 1)]


def extension_data(values):
    n = len(values)
    predecessors = [
        sum(1 << j for j in range(i) if values[j] < values[i])
        for i in range(n)
    ]

    @lru_cache(None)
    def count(mask):
        if mask == (1 << n) - 1:
            return 1
        return sum(
            count(mask | (1 << i))
            for i in range(n)
            if not mask & (1 << i) and predecessors[i] & mask == predecessors[i]
        )

    levels = []
    for i in range(n):
        levels.append(1 + max(
            (levels[j] for j in range(i) if values[j] < values[i]), default=0
        ))
    layer_lower = math.prod(math.factorial(v) for v in Counter(levels).values())
    reverse_counts = increasing_counts([-v for v in values])
    width = max(k for k, value in enumerate(reverse_counts) if value)
    e = count(0)
    assert layer_lower <= e <= width ** n
    return e, width, max(levels), layer_lower


def run():
    rng = np.random.default_rng(20260701)
    result = {"seed": 20260701, "scope": "finite sanity checks, not proofs"}

    tribes = []
    for k in (3, 5, 8, 12):
        m = math.floor(math.log(2) * 2 ** k)
        b = 2 ** -k
        joint = b * 0.75 ** k
        covariance = (1 - 2 * b + joint) ** m - (1 - b) ** (2 * m)
        assert covariance >= 0
        tribes.append({"k": k, "m": m, "covariance_epsilon_half": covariance})
    result["C01"] = tribes
    result["C02"] = {"geometric_bounds": "order n <= shortest crossing <= order n^2"}
    result["C03"] = {
        "majority_three_covariance_at_zero": 3 / 16 + 1 / 16,
        "laplace_weights": [3 / 16, 1 / 16],
    }

    majority = []
    for n in (201, 10001, 100001):
        ratio = (1 - 4 / n) ** ((n - 1) // 2)
        majority.append({"n": n, "slope_ratio_at_one_window": ratio})
    assert abs(majority[-1]["slope_ratio_at_one_window"] - math.exp(-2)) < 1e-5
    result["C04"] = {"ratios": majority, "limit": math.exp(-2)}

    n = 12
    raw = rng.normal(size=(n, n))
    h = (raw + raw.T) / math.sqrt(2 * n)
    u = np.ones(n) / math.sqrt(n)

    def spike(w):
        values, vectors = np.linalg.eigh(h + (1 + w * n ** (-1 / 3)) * np.outer(u, u))
        return n ** (2 / 3) * (values[-1] - 2), vectors[:, -1]

    w, delta = 0.25, 1e-5
    _, vector = spike(w)
    derivative = (spike(w + delta)[0] - spike(w - delta)[0]) / (2 * delta)
    overlap = n ** (1 / 3) * float(u @ vector) ** 2
    assert abs(derivative - overlap) < 1e-6
    result["C05"] = {"finite_difference": derivative, "scaled_overlap": overlap}

    vectors = [vector]
    current = h.copy()
    dt = 0.2 * n ** (-1 / 3)
    for _ in range(2):
        raw = rng.normal(size=(n, n))
        innovation = (raw + raw.T) / math.sqrt(2 * n)
        current = math.exp(-dt / 2) * current + math.sqrt(1 - math.exp(-dt)) * innovation
        _, v = np.linalg.eigh(current + (1 + w * n ** (-1 / 3)) * np.outer(u, u))
        vectors.append(v[:, -1])
    fidelity = (np.array(vectors) @ np.array(vectors).T) ** 2
    assert np.allclose(np.diag(fidelity), 1) and np.max(fidelity) <= 1 + 1e-12
    result["C06"] = {"fidelity": fidelity.tolist()}

    adjacency = np.zeros((5, 5))
    for i, j in ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)):
        adjacency[i, j] = adjacency[j, i] = 1
    degrees = adjacency.sum(axis=1)
    normalized = adjacency / np.sqrt(np.outer(degrees, degrees))
    eigenvalues = np.linalg.eigvalsh(normalized)
    assert abs(eigenvalues[-1] - 1) < 1e-12
    assert np.allclose(normalized @ np.sqrt(degrees), np.sqrt(degrees))
    result["C07"] = {"degrees": degrees.tolist(), "eigenvalues": eigenvalues.tolist()}
    all_edges = list(combinations(range(6), 2))
    completions = defaultdict(Counter)
    regular_graphs = 0
    for edges in combinations(all_edges, 6):
        full_degrees = Counter(v for edge in edges for v in edge)
        if any(full_degrees[v] != 2 for v in range(6)):
            continue
        regular_graphs += 1
        inside = tuple(edge for edge in edges if edge[1] < 4)
        inside_degrees = tuple(sum(v in edge for edge in inside) for v in range(4))
        completions[inside_degrees][inside] += 1
    admissible_degree_classes = 0
    for degree_sequence, counts in completions.items():
        expected_graphs = set()
        for mask in range(1 << 6):
            inside_edges = list(combinations(range(4), 2))
            edges = tuple(edge for i, edge in enumerate(inside_edges) if mask & (1 << i))
            if tuple(sum(v in edge for edge in edges) for v in range(4)) == degree_sequence:
                expected_graphs.add(edges)
        assert set(counts) == expected_graphs
        assert len(set(counts.values())) == 1
        admissible_degree_classes += 1
    assert regular_graphs == 70
    result["C07"]["completion_check"] = {
        "n": 6, "regular_degree": 2, "retained_set": [0, 1, 2, 3],
        "regular_graphs": regular_graphs,
        "admissible_labeled_degree_classes": admissible_degree_classes,
        "all_completion_multiplicities_equal_within_class": True,
        "purpose": "reject tautological conditional-reference claim, not verify Tracy-Widom",
    }

    tangencies = []
    for r in (2, 3, 4):
        d = 10
        x = (math.factorial(r - 1) / d ** r) ** (1 / (r - 1))
        p = (r - 1) * x / r
        assert math.isclose(d ** r * x ** (r - 1) / math.factorial(r - 1), 1)
        assert math.isclose(p + (d * x) ** r / math.factorial(r), x)
        tangencies.append({"r": r, "d": d, "x": x, "p": p})
    assert math.isclose(tangencies[0]["p"], 0.005)
    result["C08"] = tangencies
    tree_count = round(np.linalg.det((4 * np.eye(4) - np.ones((4, 4)))[:3, :3]))
    assert tree_count == 16
    result["C09"] = {"K4_spanning_trees": tree_count}
    result["C10"] = {"d3_path_counts_t1_to_t4": [3 * 2 ** (t - 1) for t in range(1, 5)]}

    n = 12
    signs = [1] * (n // 2) + [-1] * (n // 2)
    rates = [F(0) for _ in range(n)]
    edge_rates = defaultdict(F)
    for edge in combinations(range(n), 3):
        weight = 1 + F(1, 4) * math.prod(signs[i] for i in edge)
        for i in edge:
            rates[i] += weight
        for pair in combinations(edge, 2):
            edge_rates[pair] += weight
    for i in range(n):
        assert rates[i] == math.comb(n - 1, 2) + F(1, 4) * signs[i] * (2 - n) / 2
    assert max(abs(rate - (n - 2)) for rate in edge_rates.values()) == F(1, 2)
    result["C11"] = {"n12_weighted_vertex_degrees": sorted(set(map(str, rates)))}
    result["C12"] = {"n12_weighted_edge_degrees": sorted(set(map(str, edge_rates.values())))}
    result["C13"] = {
        str(n): sum(len({(i + col) % n for i, col in enumerate(cols)}) == n
                    for cols in permutations(range(n)))
        for n in (3, 4)
    }
    assert result["C13"]["4"] == 0 and result["C13"]["3"] > 0

    arcs = [(i, j) for i in range(6) for j in range(6) if (i < 3) != (j < 3)]
    transition = np.zeros((18, 18))
    for a, (i, j) in enumerate(arcs):
        next_arcs = [b for b, (v, k) in enumerate(arcs) if v == j and k != i]
        for b in next_arcs:
            transition[a, b] = 1 / len(next_arcs)
    assert np.allclose(transition.sum(axis=0), 1)
    result["C14"] = {"K33_directed_arcs": 18, "stationary_column_sums": transition.sum(axis=0).tolist()}

    n, r = 20, 16
    theta = np.linspace(1, 2, n)
    left = np.cos(np.arange(n))
    right = np.cos(np.arange(r))
    right -= right.mean()
    matrix = theta[:, None] + np.outer(left, right)
    assert np.allclose(matrix.mean(axis=1), theta)
    l, singular, rt = np.linalg.svd(matrix, full_matrices=False)
    assert singular[1] > 1 and singular[2] < 1e-12
    pl = l[:, :2] @ l[:, :2].T
    pr = rt[:2].T @ rt[:2]
    functional = np.zeros((n, r))
    functional[3] = 1 / r
    projected = pl @ functional + functional @ pr - pl @ functional @ pr
    error = float(np.linalg.norm(projected - functional))
    assert error < 1e-12
    assert math.isclose(float(np.sum(functional ** 2)), 1 / r)
    result["C15"] = {"row_mean_max_error": float(np.max(abs(matrix.mean(axis=1) - theta))),
                     "tangent_projection_error": error, "functional_norm_squared": 1 / r,
                     "k_equals_n_regret": 0}

    m, q = 7, F(1, 4)
    missing = [F(0)] * (2 * m - 1)
    for mask in range(1 << m):
        a = [i for i in range(m) if mask & (1 << i)]
        sums = {i + j for i in a for j in a}
        weight = q ** len(a) * (1 - q) ** (m - len(a))
        for s in range(2 * m - 1):
            if s not in sums:
                missing[s] += weight
    assert all(value == missing_probability(s, m, q) for s, value in enumerate(missing))
    result["C16"] = {"m": m, "q": str(q), "exact_expected_deficit": str(sum(missing)),
                     "all_single_sum_probabilities_match": True}

    sumset_simulations = []
    repetitions = 600
    for q, m in ((0.2, 3000), (0.15, 3000), (0.1, 3000),
                 (0.05, 20000), (0.025, 80000)):
        fft_size = 1 << (2 * m - 1).bit_length()
        deficits = []
        for _ in range(repetitions):
            sampled = rng.random(m) < q
            transform = np.fft.rfft(sampled.astype(float), n=fft_size)
            counts = np.rint(np.fft.irfft(transform * transform, n=fft_size)[:2 * m - 1])
            deficits.append(int(np.sum(counts == 0)))
        expected = sum(missing_probability(s, m, q) for s in range(2 * m - 1))
        sumset_simulations.append({
            "q": q, "m": m, "repetitions": repetitions, "exact_mean": expected,
            "sample_mean": float(np.mean(deficits)),
            "q_cubed_sample_variance": q ** 3 * float(np.var(deficits, ddof=1)),
        })
    result["C17"] = {"experiments": sumset_simulations, "proposed_variance_limit": 8}

    p, size = 11, 5
    subsets = list(combinations(range(p), size))
    energies = [energy(a, p) for a in subsets]
    mean = F(sum(energies), len(energies))
    variance = sum((value - mean) ** 2 for value in energies) / len(energies)
    span = reduce(math.gcd, (abs(value - energies[0]) for value in energies), 0)
    assert variance > 0 and span > 0
    result["C18"] = {"p": p, "size": size, "subsets": len(subsets),
                     "mean": str(mean), "variance": str(variance), "lattice_span": span}

    p, q = 7, F(1, 3)
    by_size = Counter()
    absence = F(0)
    for mask in range(1 << p):
        a = {i for i in range(p) if mask & (1 << i)}
        independent = all(not (i in a and (i + 1) % p in a) for i in range(p))
        absent = 1 not in {(i - j) % p for i in a for j in a}
        assert independent == absent
        if absent:
            by_size[len(a)] += 1
            absence += q ** len(a) * (1 - q) ** (p - len(a))
    result["C19"] = {"p": p, "q": str(q), "cycle_independent_sets_by_size": dict(by_size),
                     "exact_absence_probability": str(absence), "unoriented_classes": 3}

    p, size = 11, 5
    samples = []
    for subset in subsets:
        a = set(subset)
        rd = [sum((i + d) % p in a for i in a) for d in range(1, p)]
        assert sum(rd) == size * (size - 1)
        assert all(rd[d - 1] == rd[p - d - 1] for d in range(1, p))
        samples.append(rd[0])
    pj = lambda j: F(math.prod(range(size - j + 1, size + 1)),
                     math.prod(range(p - j + 1, p + 1)))
    mean = p * pj(2)
    variance = p * pj(2) + 2 * p * pj(3) + p * (p - 3) * pj(4) - mean ** 2
    assert F(sum(samples), len(samples)) == mean
    assert sum((value - mean) ** 2 for value in samples) / len(samples) == variance
    result["C20"] = {"exact_mean": str(mean), "exact_variance": str(variance),
                     "formula_matches_all_462_subsets": True}

    conditional = {}
    increasing_triples_mean = None
    for n in (4, 6, 8):
        totals, sizes = defaultdict(int), Counter()
        inc_total = 0
        for values in permutations(range(n)):
            peaks = sum(values[i - 1] < values[i] > values[i + 1] for i in range(1, n - 1))
            patterns = sum(values[i] < values[k] < values[j]
                           for i, j, k in combinations(range(n), 3))
            totals[peaks] += patterns
            sizes[peaks] += 1
            if n == 6:
                inc = increasing_counts(values)
                lis = max(k for k, value in enumerate(inc) if value)
                assert all(inc[k] >= math.comb(lis, k) for k in range(1, lis + 1))
                inc_total += inc[3]
        unconditional = F(sum(totals.values()), math.factorial(n))
        assert unconditional == F(math.comb(n, 3), 6)
        conditional[str(n)] = {str(k): {"count": sizes[k], "mean": str(F(totals[k], sizes[k]))}
                               for k in sorted(sizes)}
        if n == 6:
            increasing_triples_mean = F(inc_total, math.factorial(n))
            assert increasing_triples_mean == F(math.comb(n, 3), math.factorial(3))
    result["C21"] = conditional

    differences = []
    for l, r, x, y in permutations(range(4)):
        hx = int(l > x) + int(x > r)
        hy = int(l > y) + int(y > r)
        differences.append((hy - hx) ** 2)
    single_variance = F(sum(differences), len(differences))
    assert single_variance == F(1, 3)
    n, m, repetitions = 2000, 100, 800
    times = np.array([0.25, 0.5, 1.0])
    indices = np.minimum(n - 1, (times * n).astype(int)) - 1
    changes = []
    for _ in range(repetitions):
        original = rng.permutation(n)
        shuffled = original.copy()
        chosen = rng.choice(n, m, replace=False)
        shuffled[chosen] = rng.permutation(original[chosen])
        delta = ((shuffled[:-1] > shuffled[1:]).astype(int)
                 - (original[:-1] > original[1:]).astype(int))
        changes.append(np.cumsum(delta)[indices] / math.sqrt(m))
    result["C22"] = {"exact_single_site_variance": str(single_variance),
                     "n": n, "m": m, "repetitions": repetitions,
                     "empirical_covariance": np.cov(np.array(changes).T).tolist(),
                     "proposed_covariance": (np.minimum.outer(times, times) / 3).tolist()}

    planar = []
    for _ in range(20):
        values = rng.permutation(8).tolist()
        e, width, height, lower = extension_data(values)
        planar.append({"permutation": values, "extensions": e, "width": width,
                       "height": height, "layer_lower": lower})
    result["C23"] = {"planar_examples": planar,
                     "rejected_width_bound": [
                         {"n": n, "normalized_log_extensions": math.lgamma(n // 2 + 1) / n - math.log(n)}
                         for n in (20, 100, 1000)
                     ]}

    gaps = []
    for n in (4, 6, 8, 10):
        states = [sum(1 << i for i in subset) for subset in combinations(range(n), n // 2)]
        lookup = {state: i for i, state in enumerate(states)}
        transition = np.eye(len(states))
        for i, state in enumerate(states):
            for j in range(n - 1):
                if bool(state & (1 << j)) != bool(state & (1 << (j + 1))):
                    target = state ^ (1 << j) ^ (1 << (j + 1))
                    transition[i, lookup[target]] += 1 / (2 * (n - 1))
                    transition[i, i] -= 1 / (2 * (n - 1))
        gap = 1 - np.linalg.eigvalsh(transition)[-2]
        formula = (1 - math.cos(math.pi / n)) / (n - 1)
        assert abs(gap - formula) < 1e-12
        gaps.append({"n": n, "states": len(states), "gap": float(gap),
                     "n_cubed_gap": float(n ** 3 * gap)})
    result["C24"] = gaps
    bounds = []
    for alpha in (0.5, 1, 1.5, 1.9):
        t = alpha / 2
        lower = -2 * (t * math.log(t) + (1 - t) * math.log(1 - t))
        upper = 2 * alpha * (1 - math.log(alpha))
        assert 0 < lower <= upper
        bounds.append({"alpha": alpha, "lower": lower, "upper": upper})
    assert increasing_triples_mean == F(10, 3)
    result["C25"] = {"bounds": bounds, "n6_increasing_triples_mean": str(increasing_triples_mean),
                     "all_720_LIS_witness_bounds_checked": True}
    result["checked_candidate_ids"] = [f"C{i:02}" for i in range(1, 26)]
    result["assertions_passed"] = True
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    results = run()
    source = Path(__file__).resolve()
    candidates = sorted(source.parent.glob("main.conjectures.c[0-9][0-9].*.current.md"))
    assert len(candidates) == 25
    assert [path.name.split(".")[2] for path in candidates] == [f"c{i:02}" for i in range(1, 26)]
    results["environment"] = {"python": platform.python_version(), "numpy": np.__version__}
    results["source_sha256"] = {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in [source, *candidates]
    }
    text = json.dumps(results, indent=2, allow_nan=False)
    if arguments.output:
        arguments.output.write_text(text + "\n", encoding="utf-8")
    print(text)
