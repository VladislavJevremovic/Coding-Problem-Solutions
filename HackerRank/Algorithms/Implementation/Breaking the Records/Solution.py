# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# HackerRank: Breaking the Records
from typing import List, Tuple


def breaking_records(scores: List[int]) -> Tuple[int, int]:
    """Scan once, counting how often a new running max or min is set."""
    # Time: O(n)   Space: O(1)
    highest = lowest = scores[0]
    most = least = 0
    for score in scores[1:]:
        if score > highest:
            highest = score
            most += 1
        elif score < lowest:
            lowest = score
            least += 1
    return most, least


def test() -> None:
    assert breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]) == (2, 4)
    assert breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]) == (4, 0)
