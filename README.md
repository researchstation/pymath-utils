# pymath-utils

Lightweight Python math utilities for common operations.

## Installation

```bash
pip install -e .
```

## Usage

```python
from pymath_utils import arithmetic, geometry, matrix

arithmetic.gcd(48, 18)       # 6
geometry.circle_area(5)      # 78.5398...
matrix.multiply([[1, 2]], [[3], [4]])  # [[11]]
```

## Modules

- **arithmetic** — GCD, LCM, prime checks, factorial
- **geometry** — Area and perimeter for common shapes
- **matrix** — Matrix multiplication
- **statistics** — Mean, median, mode, standard deviation

## Development

```bash
pip install -e ".[dev]"
python -m pytest tests/ -v
```

## License

MIT
