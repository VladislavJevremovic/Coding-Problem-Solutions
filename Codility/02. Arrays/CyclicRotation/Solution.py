# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# Painless

from typing import List


def solution(A: List[int], K: int) -> List[int]:
    """Rotate right by slicing the array at the K-mod-length boundary and swapping the two parts."""
    # Time: O(n)   Space: O(n)
    if not A:
        return A

    k = K % len(A)
    return A[-k:] + A[:-k] if k else A[:]


def test() -> None:
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]
    assert solution([], 5) == []
    assert solution([5], 7) == [5]
