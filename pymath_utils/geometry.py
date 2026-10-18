"""Geometry calculations for common shapes."""

import math


def circle_area(radius: float) -> float:
    """Area of a circle."""
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2


def circle_circumference(radius: float) -> float:
    """Circumference of a circle."""
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * radius


def rectangle_area(width: float, height: float) -> float:
    """Area of a rectangle."""
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return width * height


def triangle_area(base: float, height: float) -> float:
    """Area of a triangle."""
    if base < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return 0.5 * base * height


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
