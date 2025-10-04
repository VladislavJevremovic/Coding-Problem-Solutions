# https://www.hackerrank.com/challenges/picking-numbers/problem
# HackerRank: Picking Numbers
from collections import Counter
from typing import List


def picking_numbers(a: List[int]) -> int:
    """Best pair of adjacent values maximizes count[x] + count[x+1]."""
    # Time: O(n)   Space: O(n)
    # Longest subset where any two differ by at most 1 => count[x] + count[x+1].
    freq = Counter(a)
    return max(freq[x] + freq[x + 1] for x in freq)


def test() -> None:
    assert picking_numbers([4, 6, 5, 3, 3, 1]) == 3  # {4,3,3} or {5,4}? -> 3,3,4 -> 3
    assert picking_numbers([1, 2, 2, 3, 1, 2]) == 5  # 2,2,3,1,2 within {1,2} -> count
    assert picking_numbers([1, 1, 1, 1]) == 4
