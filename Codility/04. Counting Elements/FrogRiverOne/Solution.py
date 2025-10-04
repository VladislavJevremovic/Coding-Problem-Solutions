# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# Painless

from typing import List


def solution(X: int, A: List[int]) -> int:
    """Track the set of still-missing positions, returning the time it becomes empty."""
    # Time: O(n + X)   Space: O(X)
    needed = set(range(1, X + 1))

    for time, pos in enumerate(A):
        needed.discard(pos)
        if not needed:
            return time

    return -1


def test() -> None:
    assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
    assert solution(1, [1]) == 0
    assert solution(2, [1, 1, 1]) == -1
