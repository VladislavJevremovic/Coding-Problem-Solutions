# https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/
# Painless

from typing import List


def solution(A: List[int], B: List[int]) -> int:
    """Greedily take each segment whose start clears the last chosen segment's end (input pre-sorted by end)."""
    # Time: O(n)   Space: O(1)
    if not A:
        return 0

    count = 1
    end = B[0]

    for i in range(1, len(A)):
        if A[i] > end:
            count += 1
            end = B[i]

    return count


def test() -> None:
    assert solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]) == 3
    assert solution([], []) == 0
    assert solution([1], [2]) == 1
