# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/
# Painless

from typing import List


def solution(K: int, A: List[int]) -> int:
    """Greedily accumulate consecutive ropes, closing a group once its length reaches K."""
    # Time: O(n)   Space: O(1)
    count = 0
    current = 0

    for rope in A:
        current += rope
        if current >= K:
            count += 1
            current = 0

    return count


def test() -> None:
    assert solution(4, [1, 2, 3, 4, 1, 1, 3]) == 3
    assert solution(5, [1, 1, 1]) == 0
    assert solution(1, [1, 1, 1]) == 3
