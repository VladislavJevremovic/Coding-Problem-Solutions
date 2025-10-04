# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
# HackerRank: Jumping on the Clouds
from typing import List


def jumping_on_clouds(c: List[int]) -> int:
    """Greedily jump two clouds when the landing is safe, else one, counting jumps."""
    # Time: O(n)   Space: O(1)
    jumps = 0
    pos = 0
    last = len(c) - 1
    while pos < last:
        # Prefer a jump of 2 if it lands on a safe cloud (0), else jump 1.
        if pos + 2 <= last and c[pos + 2] == 0:
            pos += 2
        else:
            pos += 1
        jumps += 1
    return jumps


def test() -> None:
    assert jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]) == 4
    assert jumping_on_clouds([0, 0, 0, 0, 1, 0]) == 3
    assert jumping_on_clouds([0, 0, 0, 1, 0, 0]) == 3
