# https://app.codility.com/programmers/lessons/6-sorting/triangle/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Sort, then check consecutive triplets since any valid triangle appears among adjacent sorted values."""
    # Time: O(n log n)   Space: O(n)
    if len(A) < 3:
        return 0

    A = sorted(A)
    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0


def test() -> None:
    assert solution([10, 2, 5, 1, 8, 20]) == 1
    assert solution([10, 50, 5, 1]) == 0
    assert solution([1, 2]) == 0
    assert solution([5, 5, 5]) == 1
