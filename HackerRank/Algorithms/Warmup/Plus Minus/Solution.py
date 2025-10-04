# https://www.hackerrank.com/challenges/plus-minus/problem
# HackerRank: Plus Minus
from typing import List, Tuple


def plus_minus(arr: List[int]) -> Tuple[str, str, str]:
    """Return the fractions of positive, negative, and zero values, each to 6 decimals."""
    # Time: O(n)   Space: O(1)
    n = len(arr)
    pos = sum(1 for v in arr if v > 0)
    neg = sum(1 for v in arr if v < 0)
    zero = sum(1 for v in arr if v == 0)
    return f"{pos / n:.6f}", f"{neg / n:.6f}", f"{zero / n:.6f}"


def test() -> None:
    assert plus_minus([1, 1, 0, -1, -1]) == ("0.400000", "0.400000", "0.200000")
    assert plus_minus([-4, 3, -9, 0, 4, 1]) == ("0.500000", "0.333333", "0.166667")
