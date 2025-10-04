# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Subtract the array sum from the expected 1..N+1 sum to recover the missing element."""
    # Time: O(n)   Space: O(1)
    n = len(A)
    expected = (n + 1) * (n + 2) // 2
    return expected - sum(A)


def test() -> None:
    assert solution([2, 3, 1, 5]) == 4
    assert solution([]) == 1
    assert solution([1]) == 2
    assert solution([2]) == 1
