# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# HackerRank: Compare the Triplets
from typing import List


def compare_triplets(a: List[int], b: List[int]) -> List[int]:
    """Award a point per category to whoever's score is higher; return [alice, bob]."""
    # Time: O(n)   Space: O(1)
    alice = sum(x > y for x, y in zip(a, b))
    bob = sum(x < y for x, y in zip(a, b))
    return [alice, bob]


def test() -> None:
    assert compare_triplets([5, 6, 7], [3, 6, 10]) == [1, 1]
    assert compare_triplets([17, 28, 30], [99, 16, 8]) == [2, 1]
    assert compare_triplets([1, 2, 3], [1, 2, 3]) == [0, 0]
