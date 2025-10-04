# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# Painless

import math


def solution(X: int, Y: int, D: int) -> int:
    """Compute the jump count as the ceiling of the remaining distance divided by the jump length."""
    # Time: O(1)   Space: O(1)
    return math.ceil((Y - X) / D)


def test() -> None:
    assert solution(10, 85, 30) == 3
    assert solution(10, 10, 5) == 0
    assert solution(1, 5, 2) == 2
