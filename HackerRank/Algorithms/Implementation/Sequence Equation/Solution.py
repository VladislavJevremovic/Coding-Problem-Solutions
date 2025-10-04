# https://www.hackerrank.com/challenges/permutation-equation/problem
# HackerRank: Sequence Equation
from typing import List


def permutation_equation(p: List[int]) -> List[int]:
    """Build value->position map, then resolve y = pos[pos[x]] for each x."""
    # Time: O(n)   Space: O(n)
    # pos[value] = 1-based position of value in p.
    pos = {value: i + 1 for i, value in enumerate(p)}
    # For each x in 1..n, find y such that p[p[y]] = x  =>  y = pos[pos[x]].
    return [pos[pos[x]] for x in range(1, len(p) + 1)]


def test() -> None:
    assert permutation_equation([2, 3, 1]) == [2, 3, 1]
    assert permutation_equation([4, 3, 5, 1, 2]) == [1, 3, 5, 4, 2]
