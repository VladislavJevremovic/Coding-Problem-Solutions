# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# HackerRank: Divisible Sum Pairs
from itertools import combinations
from typing import List


def divisible_sum_pairs(n: int, k: int, ar: List[int]) -> int:
    """Count index pairs whose element sum is divisible by k, over all pairs."""
    # Time: O(n^2)   Space: O(1)
    return sum(1 for x, y in combinations(ar, 2) if (x + y) % k == 0)


def test() -> None:
    assert divisible_sum_pairs(6, 3, [1, 3, 2, 6, 1, 2]) == 5
    assert divisible_sum_pairs(6, 5, [1, 2, 3, 4, 5, 6]) == 3
