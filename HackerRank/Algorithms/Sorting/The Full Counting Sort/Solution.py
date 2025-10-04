# https://www.hackerrank.com/challenges/the-full-counting-sort/problem
# HackerRank: The Full Counting Sort


def count_sort(arr: list[list[str]]) -> list[str]:
    """Counting sort by the integer key in column 0.

    Strings in the first half of the input are replaced with "-".
    Returns the resulting list of strings (stable within each key bucket).
    """
    # Time: O(n)   Space: O(n)
    buckets: list[list[str]] = [[] for _ in range(100)]
    n = len(arr)
    for i, (key, value) in enumerate(arr):
        label = "-" if i < n // 2 else value
        buckets[int(key)].append(label)

    return [s for bucket in buckets for s in bucket]


def test() -> None:
    arr = [
        ["0", "ab"],
        ["6", "cd"],
        ["0", "ef"],
        ["6", "gh"],
    ]
    # First half (indices 0,1) become "-", sorted by key 0,6,0,6 -> stable.
    assert count_sort(arr) == ["-", "ef", "-", "gh"]

    # Edge case: single element (still in first half since 0 < 0 is False -> kept).
    assert count_sort([["3", "x"]]) == ["x"]
