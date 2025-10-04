# https://www.hackerrank.com/challenges/service-lane/problem
# HackerRank: Service Lane
from typing import List, Tuple


def service_lane(width: List[int], cases: List[Tuple[int, int]]) -> List[int]:
    """For each segment, the widest vehicle equals its minimum lane width."""
    # Time: O(sum of segment lengths)   Space: O(1)
    # Widest vehicle that fits a segment is the minimum width in that segment.
    return [min(width[a : b + 1]) for a, b in cases]


def test() -> None:
    width = [2, 3, 1, 2, 3, 2, 3, 3]
    assert service_lane(width, [(0, 3), (4, 6), (6, 7), (3, 5), (0, 7)]) == [
        1,
        2,
        3,
        2,
        1,
    ]
    assert service_lane([1, 2, 2, 2, 1], [(2, 3)]) == [2]
