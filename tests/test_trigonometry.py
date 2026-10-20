import math

from pymath_utils.trigonometry import sine_cosine


class TestSineCosine:
    def test_zero_angle(self):
        assert sine_cosine(0) == (0.0, 1.0)

    def test_quarter_turn(self):
        sine, cosine = sine_cosine(math.pi / 2)
        assert math.isclose(sine, 1.0)
        assert math.isclose(cosine, 0.0, abs_tol=1e-15)

    def test_negative_and_large_angles(self):
        sine, cosine = sine_cosine(-math.pi / 2)
        assert math.isclose(sine, -1.0)
        assert math.isclose(cosine, 0.0, abs_tol=1e-15)

        sine, cosine = sine_cosine(1e100)
        assert math.isfinite(sine)
        assert math.isfinite(cosine)
