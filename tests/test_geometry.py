import math
import pytest
from pymath_utils.geometry import circle_area, rectangle_area, triangle_area, distance


class TestCircleArea:
    def test_basic(self):
        assert abs(circle_area(5) - 78.5398) < 0.001

    def test_zero(self):
        assert circle_area(0) == 0

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            circle_area(-1)


class TestRectangleArea:
    def test_basic(self):
        assert rectangle_area(3, 4) == 12

    def test_square(self):
        assert rectangle_area(5, 5) == 25


class TestTriangleArea:
    def test_basic(self):
        assert triangle_area(6, 4) == 12


class TestDistance:
    def test_basic(self):
        assert distance(0, 0, 3, 4) == 5.0

    def test_same_point(self):
        assert distance(2, 3, 2, 3) == 0.0
