# https://www.hackerrank.com/challenges/minimum-distances/problem
# HackerRank: Minimum Distances
from typing import List


def minimum_distances(a: List[int]) -> int:
    """Track each value's last index to find the smallest gap between duplicates."""
    # Time: O(n)   Space: O(n)
    last_seen: dict[int, int] = {}
    best = -1
    for i, value in enumerate(a):
        if value in last_seen:
            d = i - last_seen[value]
            if best == -1 or d < best:
                best = d
        last_seen[value] = i
    return best


def test() -> None:
    assert minimum_distances([3, 2, 1, 2, 3]) == 2
    assert minimum_distances([7, 1, 3, 4, 1, 7]) == 3
    assert minimum_distances([1, 2, 3, 4]) == -1
