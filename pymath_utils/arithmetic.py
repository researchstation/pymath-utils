"""Basic arithmetic utilities."""

import math


def gcd(a: int, b: int) -> int:
    """Greatest common divisor using Euclidean algorithm."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Arguments must be integers")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Least common multiple."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_prime(n: int) -> bool:
    """Check if n is a prime number."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def factorial(n: int) -> int:
    """Factorial of a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return math.factorial(n)


def fibonacci(n: int) -> list[int]:
    """Return first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq
