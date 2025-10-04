# https://www.hackerrank.com/challenges/quicksort-1-partition/problem
# HackerRank: Quicksort 1 - Partition


def partition(arr: list[int]) -> list[int]:
    """Partition arr around its first element (the pivot).

    Returns a list with all elements smaller than the pivot first, then the
    pivot, then all elements larger, preserving relative order within groups.
    """
    # Time: O(n)   Space: O(n)
    pivot = arr[0]
    rest = arr[1:]
    less = [x for x in rest if x < pivot]
    greater = [x for x in rest if x >= pivot]
    return less + [pivot] + greater


def test() -> None:
    assert partition([4, 5, 3, 7, 2]) == [3, 2, 4, 5, 7]
    # Pivot already smallest -> everything goes after.
    assert partition([1, 3, 2]) == [1, 3, 2]
    # Edge case: single element.
    assert partition([9]) == [9]
