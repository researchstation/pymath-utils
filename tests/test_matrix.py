import pytest

from pymath_utils.matrix import multiply


class TestMultiply:
    def test_rectangular_matrices(self):
        assert multiply([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]) == [
            [58, 64],
            [139, 154],
        ]

    def test_zero_values(self):
        assert multiply([[0, 2], [3, 0]], [[4, 0], [0, 5]]) == [[0, 10], [12, 0]]

    def test_incompatible_dimensions_raise_value_error(self):
        with pytest.raises(ValueError):
            multiply([[1, 2]], [[1, 2]])

    def test_ragged_matrix_raises_value_error(self):
        with pytest.raises(ValueError):
            multiply([[1, 2], [3]], [[1], [2]])

    def test_empty_matrix_raises_value_error(self):
        with pytest.raises(ValueError):
            multiply([], [])
