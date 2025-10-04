# https://www.hackerrank.com/challenges/find-the-median/problem
# HackerRank: Find the Median


def find_median(arr: list[int]) -> int:
    """Return the median (middle element) of an odd-length list."""
    # Time: O(n log n)   Space: O(n)
    return sorted(arr)[(len(arr) - 1) // 2]


def test() -> None:
    assert find_median([0, 1, 2, 4, 6, 5, 3]) == 3
    # Edge case: single element.
    assert find_median([7]) == 7
    assert find_median([5, 3, 1, 2, 4]) == 3
