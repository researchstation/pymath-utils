"""Basic statistics functions."""

import math
from collections import Counter


def mean(values: list[float]) -> float:
    """Arithmetic mean."""
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


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
