"""Matrix utilities."""


def _column_count(matrix: list[list[int | float]]) -> int:
    if not matrix:
        return 0
    columns = len(matrix[0])
    if any(len(row) != columns for row in matrix):
        raise ValueError("Matrix rows must have the same number of columns")
    return columns


def matrix_multiply(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]]:
    """Multiply two matrices."""
    columns_a = _column_count(a)
    columns_b = _column_count(b)
    if columns_a != len(b):
        raise ValueError(
            "The number of columns in a must equal the number of rows in b"
        )
    return [
        [
            sum(a_value * b[row][column] for row, a_value in enumerate(a_row))
            for column in range(columns_b)
        ]
        for a_row in a
    ]


def matrix_transpose(matrix: list[list[int | float]]) -> list[list[int | float]]:
    """Return the transpose of a matrix."""
    columns = _column_count(matrix)
    return [[row[column] for row in matrix] for column in range(columns)]
