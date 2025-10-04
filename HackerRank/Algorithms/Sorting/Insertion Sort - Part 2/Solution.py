# https://www.hackerrank.com/challenges/insertion-sort-part-2/problem
# HackerRank: Insertion Sort - Part 2


def insertion_sort_2(arr: list[int]) -> list[int]:
    """Sort the list using insertion sort and return the fully sorted list."""
    # Time: O(n^2)   Space: O(n)
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        p = i
        while p > 0 and a[p - 1] > key:
            a[p] = a[p - 1]
            p -= 1
        a[p] = key
    return a


def test() -> None:
    assert insertion_sort_2([3, 4, 7, 5, 6, 2, 1]) == [1, 2, 3, 4, 5, 6, 7]
    assert insertion_sort_2([1, 4, 3, 5, 6, 2]) == [1, 2, 3, 4, 5, 6]
    # Already sorted.
    assert insertion_sort_2([1, 2, 3]) == [1, 2, 3]
    # Edge case: single element.
    assert insertion_sort_2([5]) == [5]
