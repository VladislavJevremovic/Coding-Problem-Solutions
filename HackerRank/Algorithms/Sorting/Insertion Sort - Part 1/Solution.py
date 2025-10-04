# https://www.hackerrank.com/challenges/insertion-sort-part-1/problem
# HackerRank: Insertion Sort - Part 1


def insertion_sort_1(arr: list[int]) -> list[int]:
    """Insert the last element of an otherwise-sorted list into position.

    Returns the fully sorted list.
    """
    # Time: O(n)   Space: O(n)
    a = list(arr)
    n = len(a)
    last = a[n - 1]
    p = n - 1
    while p > 0 and a[p - 1] > last:
        a[p] = a[p - 1]
        p -= 1
    a[p] = last
    return a


def test() -> None:
    assert insertion_sort_1([2, 4, 6, 8, 3]) == [2, 3, 4, 6, 8]
    # Last element is already the largest -> unchanged.
    assert insertion_sort_1([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Edge case: single element.
    assert insertion_sort_1([9]) == [9]
    # Last element is the smallest -> moves to front.
    assert insertion_sort_1([3, 5, 7, 1]) == [1, 3, 5, 7]
