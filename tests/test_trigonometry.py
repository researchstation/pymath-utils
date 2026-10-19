import math

import pytest

from pymath_utils.trigonometry import cos_deg, sin_deg, tan_deg


class TestSinDeg:
    def test_cardinal_angles(self):
        assert sin_deg(0) == pytest.approx(0)
        assert sin_deg(90) == pytest.approx(1)
        assert sin_deg(180) == pytest.approx(0)

    def test_negative_angle(self):
        assert sin_deg(-30) == pytest.approx(-0.5)

    def test_large_angle(self):
        assert sin_deg(1e12) == pytest.approx(math.sin(math.radians(1e12)))


class TestCosDeg:
    def test_cardinal_angles(self):
        assert cos_deg(0) == pytest.approx(1)
        assert cos_deg(90) == pytest.approx(0)
        assert cos_deg(180) == pytest.approx(-1)

    def test_negative_angle(self):
        assert cos_deg(-60) == pytest.approx(0.5)


class TestTanDeg:
    def test_common_angles(self):
        assert tan_deg(0) == pytest.approx(0)
        assert tan_deg(45) == pytest.approx(1)

    def test_negative_angle(self):
        assert tan_deg(-45) == pytest.approx(-1)
