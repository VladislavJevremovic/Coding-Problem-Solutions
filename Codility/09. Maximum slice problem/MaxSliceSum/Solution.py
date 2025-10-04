# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Apply Kadane's algorithm, tracking the best slice ending here and the best slice overall."""
    # Time: O(n)   Space: O(1)
    max_ending = A[0]
    max_slice = A[0]

    for a in A[1:]:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)

    return max_slice


def test() -> None:
    assert solution([3, 2, -6, 4, 0]) == 5
    assert solution([-10]) == -10
    assert solution([-2, -3, -1, -4]) == -1
