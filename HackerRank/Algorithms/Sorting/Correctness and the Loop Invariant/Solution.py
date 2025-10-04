# https://www.hackerrank.com/challenges/correctness-and-the-loop-invariant/problem
# HackerRank: Correctness and the Loop Invariant
from typing import List


def insertion_sort(a: List[int]) -> List[int]:
    """In-place insertion sort; returns the sorted list."""
    # Time: O(n^2)   Space: O(1)
    for i in range(1, len(a)):
        value = a[i]
        j = i
        while j > 0 and a[j - 1] > value:
            a[j] = a[j - 1]
            j -= 1
        a[j] = value
    return a


def test() -> None:
    assert insertion_sort([7, 4, 3, 5, 6, 2]) == [2, 3, 4, 5, 6, 7]
    assert insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert insertion_sort([1]) == [1]
    assert insertion_sort([]) == []
