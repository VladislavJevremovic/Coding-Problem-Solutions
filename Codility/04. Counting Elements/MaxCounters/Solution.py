# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
# Respectable

from typing import List


def solution(N: int, A: List[int]) -> List[int]:
    """Apply increments directly and defer max-counter ops via a lazy floor raised to the running max."""
    # Time: O(n + N)   Space: O(N)
    counters = [0] * N
    current_max = 0
    floor = 0  # value all counters are lazily raised to on a max-counter op

    for op in A:
        if op <= N:
            idx = op - 1
            counters[idx] = max(counters[idx], floor) + 1
            current_max = max(current_max, counters[idx])
        else:
            floor = current_max

    return [max(c, floor) for c in counters]


def test() -> None:
    assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
    assert solution(3, [4, 4, 4]) == [0, 0, 0]
    assert solution(2, [1, 1, 2]) == [2, 1]
