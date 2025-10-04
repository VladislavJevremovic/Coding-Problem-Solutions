# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Count east-bound cars seen so far and add that running count at each west-bound car."""
    # Time: O(n)   Space: O(1)
    east = 0
    pairs = 0

    for a in A:
        if a == 0:
            east += 1
        else:
            pairs += east

        if pairs > 1_000_000_000:
            return -1

    return pairs


def test() -> None:
    assert solution([0, 1, 0, 1, 1]) == 5
    assert solution([]) == 0
    assert solution([1, 1, 1]) == 0
    assert solution([0, 0, 0]) == 0
