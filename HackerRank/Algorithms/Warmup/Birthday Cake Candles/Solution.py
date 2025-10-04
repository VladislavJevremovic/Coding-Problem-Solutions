# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# HackerRank: Birthday Cake Candles
from typing import List


def birthday_cake_candles(ar: List[int]) -> int:
    """Count how many candles have the maximum height."""
    # Time: O(n)   Space: O(1)
    tallest = max(ar)
    return ar.count(tallest)


def test() -> None:
    assert birthday_cake_candles([3, 2, 1, 3]) == 2
    assert birthday_cake_candles([4, 4, 1, 3]) == 2
    assert birthday_cake_candles([18]) == 1
