# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
# Respectable


def solution(A: int, B: int, K: int) -> int:
    """Count multiples of K in [A, B] via floor-division differences, handling A == 0 separately."""
    # Time: O(1)   Space: O(1)
    return B // K - (A - 1) // K if A > 0 else B // K + 1


def test() -> None:
    assert solution(6, 11, 2) == 3
    assert solution(0, 0, 11) == 1
    assert solution(0, 14, 2) == 8
    assert solution(11, 345, 17) == 20
