# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Sort, then take the larger of the three-largest product and the two-smallest-times-largest product."""
    # Time: O(n log n)   Space: O(n)
    A = sorted(A)
    return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])


def test() -> None:
    assert solution([-3, 1, 2, -2, 5, 6]) == 60
    assert solution([-5, -6, -4, -7, -10]) == -120
    assert solution([1, 2, 3]) == 6
