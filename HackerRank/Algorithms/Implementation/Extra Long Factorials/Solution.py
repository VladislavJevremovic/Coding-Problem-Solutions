# https://www.hackerrank.com/challenges/extra-long-factorials/problem
# HackerRank: Extra Long Factorials
from math import factorial


def extra_long_factorials(n: int) -> int:
    """Use Python's arbitrary-precision ints to compute n! directly."""
    # Time: O(n)   Space: O(n)  (digits of the result grow with n)
    # Python ints are arbitrary precision, so no BigInteger needed.
    return factorial(n)


def test() -> None:
    assert extra_long_factorials(5) == 120
    assert extra_long_factorials(0) == 1
    assert extra_long_factorials(25) == 15511210043330985984000000
