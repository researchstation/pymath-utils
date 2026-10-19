def _column_count(matrix: list[list[int | float]], name: str) -> int:
    if not matrix:
        raise ValueError(f"{name} must contain at least one row")

    column_count = len(matrix[0])
    if any(len(row) != column_count for row in matrix):
        raise ValueError(f"{name} must be rectangular")

    return column_count


def multiply(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]]:
    """Multiply two rectangular matrices."""
    a_columns = _column_count(a, "a")
    b_columns = _column_count(b, "b")
    if a_columns != len(b):
        raise ValueError(
            "the number of columns in a must match the number of rows in b"
        )

    return [
        [
            sum(a[row][inner] * b[inner][column] for inner in range(a_columns))
            for column in range(b_columns)
        ]
        for row in range(len(a))
    ]
