# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
# HackerRank: Sherlock and Squares
import math


def squares(a: int, b: int) -> int:
    """Count perfect squares in [a, b] via floor(sqrt(b)) - ceil(sqrt(a)) + 1."""
    # Time: O(1)   Space: O(1)
    # Count of perfect squares in [a, b]. isqrt is exact for integers.
    lo = math.isqrt(a)
    if lo * lo < a:  # smallest integer whose square is >= a
        lo += 1
    hi = math.isqrt(b)  # largest integer whose square is <= b
    return hi - lo + 1


def test() -> None:
    assert squares(3, 9) == 2  # 4, 9
    assert squares(17, 24) == 0
    assert squares(1, 100) == 10
