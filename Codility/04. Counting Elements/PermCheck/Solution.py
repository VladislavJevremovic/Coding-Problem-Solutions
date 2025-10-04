# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
# Painless

from typing import List


def solution(A: List[int]) -> int:
    """Compare the value set against the full 1..N range to confirm it is a permutation."""
    # Time: O(n)   Space: O(n)
    return 1 if set(A) == set(range(1, len(A) + 1)) else 0


def test() -> None:
    assert solution([4, 1, 3, 2]) == 1
    assert solution([4, 1, 3]) == 0
    assert solution([1]) == 1
    assert solution([2, 2]) == 0
