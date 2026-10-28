import pytest

from pymath_utils.statistics import percentile, weighted_mean


class TestWeightedMean:
    def test_basic(self):
        assert weighted_mean([1, 3], [1, 2]) == pytest.approx(7 / 3)

    def test_single_element(self):
        assert weighted_mean([5], [2]) == 5

    def test_uniform_weights(self):
        assert weighted_mean([2, 4, 6], [3, 3, 3]) == 4

    def test_mismatched_lengths_raises(self):
        with pytest.raises(ValueError):
            weighted_mean([1, 2], [1])

    def test_negative_weight_raises(self):
        with pytest.raises(ValueError):
            weighted_mean([1, 2], [1, -1])

    def test_zero_total_weight_raises(self):
        with pytest.raises(ValueError):
            weighted_mean([1, 2], [0, 0])


class TestPercentile:
    def test_single_element(self):
        assert percentile([7], 50) == 7

    def test_linear_interpolation(self):
        assert percentile([0, 10], 25) == 2.5

    def test_zero_percentile(self):
        assert percentile([4, 1, 3], 0) == 1

    def test_hundredth_percentile(self):
        assert percentile([4, 1, 3], 100) == 4

    def test_out_of_range_raises(self):
        with pytest.raises(ValueError):
            percentile([1, 2], -1)
        with pytest.raises(ValueError):
            percentile([1, 2], 101)

    def test_empty_values_raises(self):
        with pytest.raises(ValueError):
            percentile([], 50)
