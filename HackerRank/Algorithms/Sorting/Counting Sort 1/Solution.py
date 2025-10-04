# https://www.hackerrank.com/challenges/counting-sort-1/problem
# HackerRank: Counting Sort 1


def counting_sort(arr: list[int]) -> list[int]:
    """Return a frequency array of size 100 counting each value in arr."""
    # Time: O(n)   Space: O(1)
    counts = [0] * 100
    for value in arr:
        counts[value] += 1
    return counts


def test() -> None:
    result = counting_sort([1, 1, 3, 2, 1])
    assert len(result) == 100
    assert result[1] == 3
    assert result[2] == 1
    assert result[3] == 1
    assert result[0] == 0

    # Edge case: empty input -> all zeros.
    assert counting_sort([]) == [0] * 100
