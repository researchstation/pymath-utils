"""Basic statistics functions."""

import math
from collections import Counter


def mean(values: list[float]) -> float:
    """Arithmetic mean."""
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


def weighted_mean(values: list[float], weights: list[float]) -> float:
    """Weighted arithmetic mean."""
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length")
    if not values:
        raise ValueError("Cannot compute weighted mean of empty lists")
    if any(weight < 0 for weight in weights):
        raise ValueError("Weights cannot be negative")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Sum of weights must be greater than zero")
    return sum(value * weight for value, weight in zip(values, weights)) / total_weight


def median(values: list[float]) -> float:
    """Median value."""
    if not values:
        raise ValueError("Cannot compute median of empty list")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


def percentile(values: list[float], p: float) -> float:
    """Return the p-th percentile using linear interpolation."""
    if not values:
        raise ValueError("Cannot compute percentile of empty list")
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")
    sorted_vals = sorted(values)
    position = p / 100 * (len(sorted_vals) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    return sorted_vals[lower] + (position - lower) * (
        sorted_vals[upper] - sorted_vals[lower]
    )


def mode(values: list) -> list:
    """Mode (most frequent values). Returns list for multi-modal data."""
    if not values:
        raise ValueError("Cannot compute mode of empty list")
    counts = Counter(values)
    max_count = max(counts.values())
    return sorted(v for v, c in counts.items() if c == max_count)


def std_dev(values: list[float]) -> float:
    """Population standard deviation."""
    if len(values) < 2:
        raise ValueError("Need at least 2 values")
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return math.sqrt(variance)
