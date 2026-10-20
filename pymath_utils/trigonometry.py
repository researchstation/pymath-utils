"""Trigonometric utilities."""

import math


def sine_cosine(angle: float) -> tuple[float, float]:
    """Return the sine and cosine of an angle in radians."""
    return math.sin(angle), math.cos(angle)
