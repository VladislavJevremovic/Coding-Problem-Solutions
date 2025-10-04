# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Sweep once, tracking the minimum price so far and the best profit against it."""
    # Time: O(n)   Space: O(1)
    max_profit = 0
    min_value = float("inf")

    for day in A:
        min_value = min(min_value, day)
        max_profit = max(max_profit, day - min_value)

    return max_profit


def test() -> None:
    assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356
    assert solution([]) == 0
    assert solution([5, 4, 3, 2, 1]) == 0
    assert solution([1, 5]) == 4
