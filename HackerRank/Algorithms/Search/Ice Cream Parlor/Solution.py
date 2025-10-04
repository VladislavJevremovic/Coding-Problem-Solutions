# https://www.hackerrank.com/challenges/ice-cream-parlor/problem
# HackerRank: Ice Cream Parlor


def icecream_parlor(m: int, arr: list[int]) -> list[int]:
    """Return the 1-based indices of the two flavors whose costs sum to m."""
    # Time: O(n)   Space: O(n)
    seen: dict[int, int] = {}
    for i, cost in enumerate(arr):
        if cost >= m:
            continue
        if cost in seen:
            return [seen[cost] + 1, i + 1]
        seen[m - cost] = i
    return []


def test() -> None:
    # costs [1, 4, 5, 3, 2], money 4 -> 1 + 3 at indices 1 and 4
    assert icecream_parlor(4, [1, 4, 5, 3, 2]) == [1, 4]
    # costs [2, 2, 4, 3], money 4 -> 2 + 2 at indices 1 and 2
    assert icecream_parlor(4, [2, 2, 4, 3]) == [1, 2]
    # edge case: no valid pair
    assert icecream_parlor(100, [1, 2, 3]) == []
