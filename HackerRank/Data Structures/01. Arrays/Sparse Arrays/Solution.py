# https://www.hackerrank.com/challenges/sparse-arrays/problem
# HackerRank: Sparse Arrays
from collections import Counter


def matching_strings(strings: list[str], queries: list[str]) -> list[int]:
    """Count occurrences of each query string via a Counter built once over the inputs."""
    # Time: O(n + q)   Space: O(n)  (n = len(strings), q = len(queries))
    counts = Counter(strings)
    return [counts[query] for query in queries]


def test() -> None:
    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]
    assert matching_strings(strings, queries) == [2, 1, 0]
    # edge case: empty strings list
    assert matching_strings([], ["a", "b"]) == [0, 0]
    # edge case: empty queries
    assert matching_strings(["a", "a"], []) == []
