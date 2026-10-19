"""Trigonometric functions for angles in degrees."""

import math


def sin_deg(angle: float) -> float:
    """Sine of an angle in degrees."""
    return math.sin(math.radians(angle))


def cos_deg(angle: float) -> float:
    """Cosine of an angle in degrees."""
    return math.cos(math.radians(angle))


def tan_deg(angle: float) -> float:
    """Tangent of an angle in degrees."""
    return math.tan(math.radians(angle))
