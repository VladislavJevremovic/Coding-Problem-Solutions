# https://www.hackerrank.com/challenges/equality-in-a-array/problem
# HackerRank: Equalize the Array
from collections import Counter


def equalize_array(arr: list[int]) -> int:
    """Keep the most frequent value; deletions equal the rest of the array."""
    # Time: O(n)   Space: O(n)
    if not arr:
        return 0
    most_common = max(Counter(arr).values())
    return len(arr) - most_common


def test() -> None:
    assert equalize_array([3, 3, 2, 1, 3]) == 2  # keep three 3's, remove 2 and 1
    assert equalize_array([1, 2, 3, 4]) == 3  # keep one element
    # Edge: all identical
    assert equalize_array([5, 5, 5]) == 0
    # Edge: empty
    assert equalize_array([]) == 0
