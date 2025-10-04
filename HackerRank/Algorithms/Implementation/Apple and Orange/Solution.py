# https://www.hackerrank.com/challenges/apple-and-orange/problem
# HackerRank: Apple and Orange
from typing import List, Tuple


def count_apples_and_oranges(
    s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]
) -> Tuple[int, int]:
    """Count fruits whose tree position plus distance lands within [s, t]."""
    # Time: O(n + m)   Space: O(1)
    apple_count = sum(1 for d in apples if s <= a + d <= t)
    orange_count = sum(1 for d in oranges if s <= b + d <= t)
    return apple_count, orange_count


def test() -> None:
    assert count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]) == (1, 1)
    # apples land at 6,7,0 -> 1 in [7,10]; oranges land at 15,10,8 -> 2 in [7,10]
    assert count_apples_and_oranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4]) == (1, 2)
