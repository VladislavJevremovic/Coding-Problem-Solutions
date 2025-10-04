# https://www.hackerrank.com/challenges/beautiful-triplets/problem
# HackerRank: Beautiful Triplets
from collections import Counter


def beautiful_triplets(d: int, a: list[int]) -> int:
    """Count values x whose arithmetic partners x+d and x+2d both appear."""
    # Time: O(n)   Space: O(n)
    counts = Counter(a)
    return sum(1 for x in a if counts[x + d] > 0 and counts[x + 2 * d] > 0)


def test() -> None:
    # 1,2,4,5,7,8,10 with d=3: triplets (1,4,7),(2,5,8),(4,7,10),(5,8,?no 11)
    # starting values with both x+3 and x+6 present: 1->4,7 yes; 2->5,8 yes;
    # 4->7,10 yes; 5->8,11 no; 7->10,13 no; 8,10 no => 3
    assert beautiful_triplets(3, [1, 2, 4, 5, 7, 8, 10]) == 3
    # No beautiful triplets
    assert beautiful_triplets(1, [2, 2, 3, 4, 5]) == 3  # 2->3,4;2->3,4;3->4,5
    # Edge: empty input
    assert beautiful_triplets(1, []) == 0
    # Edge: d=0, every element counts (x, x, x all present)
    assert beautiful_triplets(0, [5, 5]) == 2
