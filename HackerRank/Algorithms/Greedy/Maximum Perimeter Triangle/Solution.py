# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
# HackerRank: Maximum Perimeter Triangle


def maximum_perimeter_triangle(sticks: list[int]) -> list[int]:
    """Return the sides of the max-perimeter non-degenerate triangle.

    Prefers the longest sides; among equal perimeters prefers the one with the
    longest maximum side. Returns [-1] if no valid triangle exists.
    """
    # Time: O(n log n)   Space: O(n)
    s = sorted(sticks)
    for i in range(len(s) - 3, -1, -1):
        if s[i] + s[i + 1] > s[i + 2]:
            return [s[i], s[i + 1], s[i + 2]]
    return [-1]


def test() -> None:
    assert maximum_perimeter_triangle([1, 1, 1, 3, 3]) == [1, 3, 3]
    assert maximum_perimeter_triangle([1, 2, 3]) == [-1]  # degenerate
    assert maximum_perimeter_triangle([2, 3, 4, 5, 10]) == [3, 4, 5]
    # Edge case: exactly three valid sticks.
    assert maximum_perimeter_triangle([5, 5, 5]) == [5, 5, 5]
