# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Sweep a running prefix sum and track the smallest absolute gap between the two tape parts."""
    # Time: O(n)   Space: O(1)
    total = sum(A)
    result = float("inf")
    first = 0

    for i in range(len(A) - 1):
        first += A[i]
        second = total - first
        result = min(result, abs(first - second))

    return result


def test() -> None:
    assert solution([3, 1, 2, 4, 3]) == 1
    assert solution([1, 1]) == 0
    assert solution([-1000, 1000]) == 2000
