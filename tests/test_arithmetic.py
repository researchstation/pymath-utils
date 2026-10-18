import pytest
from pymath_utils.arithmetic import gcd, lcm, is_prime, factorial, fibonacci


class TestGCD:
    def test_basic(self):
        assert gcd(48, 18) == 6

    def test_coprime(self):
        assert gcd(17, 13) == 1

    def test_zero(self):
        assert gcd(0, 5) == 5
        assert gcd(5, 0) == 5

    def test_negative(self):
        assert gcd(-12, 8) == 4


class TestLCM:
    def test_basic(self):
        assert lcm(4, 6) == 12

    def test_zero(self):
        assert lcm(0, 5) == 0


class TestIsPrime:
    def test_primes(self):
        for p in [2, 3, 5, 7, 11, 13, 97]:
            assert is_prime(p) is True

    def test_non_primes(self):
        for n in [0, 1, 4, 9, 15, 100]:
            assert is_prime(n) is False


class TestFactorial:
    def test_basic(self):
        assert factorial(5) == 120
        assert factorial(0) == 1

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)


class TestFibonacci:
    def test_basic(self):
        assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

    def test_empty(self):
        assert fibonacci(0) == []

    def test_one(self):
        assert fibonacci(1) == [0]
