import pytest

from pymath_utils.matrix import matrix_multiply, matrix_transpose


class TestMatrixMultiply:
    def test_identity_matrix(self):
        identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        matrix = [[1, 2, 3], [4, 5, 6]]
        assert matrix_multiply(matrix, identity) == matrix

    def test_rectangular_matrices(self):
        assert matrix_multiply([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]) == [
            [58, 64],
            [139, 154],
        ]

    def test_incompatible_dimensions(self):
        with pytest.raises(ValueError):
            matrix_multiply([[1, 2, 3]], [[1, 2], [3, 4]])

    def test_empty_matrices(self):
        assert matrix_multiply([], []) == []
        assert matrix_multiply([[], []], []) == [[], []]

    def test_negative_and_large_values(self):
        large_number = 10**100
        assert matrix_multiply([[-2, large_number]], [[4], [5]]) == [
            [-8 + 5 * large_number]
        ]

    def test_ragged_matrix(self):
        with pytest.raises(ValueError):
            matrix_multiply([[1, 2], [3]], [[1], [2]])


class TestMatrixTranspose:
    def test_rectangular_matrix(self):
        assert matrix_transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

    def test_empty_matrix(self):
        assert matrix_transpose([]) == []

    def test_ragged_matrix(self):
        with pytest.raises(ValueError):
            matrix_transpose([[1, 2], [3]])
