# https://app.codility.com/programmers/lessons/6-sorting/distinct/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Count distinct values by collapsing the list into a set."""
    # Time: O(n)   Space: O(n)
    return len(set(A))


def test() -> None:
    assert solution([2, 1, 1, 2, 3, 1]) == 3
    assert solution([]) == 0
    assert solution([5]) == 1
    assert solution([-3, -3, 7, 7, 7]) == 2
