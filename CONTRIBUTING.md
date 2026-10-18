# Contributing

Thanks for your interest in contributing to pymath-utils!

## Getting Started

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Install dev dependencies: `pip install -e ".[dev]"`
4. Make your changes
5. Run tests: `python -m pytest tests/ -v`
6. Open a pull request

## Code Style

- Follow PEP 8 naming conventions
- Use type hints for all public functions
- Raise `ValueError` for invalid inputs
- Keep functions focused and well-documented

## Testing

Every new function needs tests covering:
- Normal inputs
- Edge cases (zero, negative, empty)
- Invalid inputs (type errors, domain errors)
