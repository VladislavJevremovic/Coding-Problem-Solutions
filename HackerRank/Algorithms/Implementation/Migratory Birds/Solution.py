# https://www.hackerrank.com/challenges/migratory-birds/problem
# HackerRank: Migratory Birds
from collections import Counter
from typing import List


def migratory_birds(arr: List[int]) -> int:
    """Tally sightings and return the most-sighted id, breaking ties by smallest."""
    # Time: O(n)   Space: O(n)
    counts = Counter(arr)
    # Most frequent; ties broken by smallest id.
    max_count = max(counts.values())
    return min(bird for bird, c in counts.items() if c == max_count)


def test() -> None:
    assert migratory_birds([1, 4, 4, 4, 5, 3]) == 4
    assert migratory_birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]) == 3
    assert migratory_birds([1, 1, 2, 2, 3]) == 1
