# https://www.hackerrank.com/challenges/counting-sort-2/problem
# HackerRank: Counting Sort 2


def counting_sort(arr: list[int]) -> list[int]:
    """Sort values (0..99) using counting sort and return the sorted list."""
    # Time: O(n)   Space: O(n)
    counts = [0] * 100
    for value in arr:
        counts[value] += 1

    return [value for value, count in enumerate(counts) for _ in range(count)]


def test() -> None:
    assert counting_sort([1, 1, 3, 2, 1]) == [1, 1, 1, 2, 3]
    assert counting_sort([4, 0, 2, 0]) == [0, 0, 2, 4]
    # Edge case: empty input.
    assert counting_sort([]) == []
