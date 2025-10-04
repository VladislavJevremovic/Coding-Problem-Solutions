# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
# Respectable

from typing import List


def solution(A: List[int]) -> int:
    """Build a lookup set, then scan upward from 1 for the first integer not present."""
    # Time: O(n)   Space: O(n)
    seen = set(A)
    candidate = 1
    while candidate in seen:
        candidate += 1
    return candidate


def test() -> None:
    assert solution([1, 3, 6, 4, 1, 2]) == 5
    assert solution([1, 2, 3]) == 4
    assert solution([-1, -3]) == 1
    assert solution([]) == 1
