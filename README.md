# pymath-utils

Lightweight Python math utilities for common operations.

## Installation

```bash
pip install -e .
```

## Usage

```python
from pymath_utils import arithmetic, geometry, trigonometry

arithmetic.gcd(48, 18)       # 6
geometry.circle_area(5)      # 78.5398...
trigonometry.sine_cosine(0)  # (0.0, 1.0)
```

## Modules

- **arithmetic** — GCD, LCM, prime checks, factorial
- **geometry** — Area and perimeter for common shapes
- **trigonometry** — Sine and cosine
- **statistics** — Mean, median, mode, standard deviation

## Development

```bash
pip install -e ".[dev]"
python -m pytest tests/ -v
```

## License

MIT
