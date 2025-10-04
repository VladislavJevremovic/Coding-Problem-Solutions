# https://www.hackerrank.com/challenges/pairs/problem
# HackerRank: Pairs


def pairs(k: int, arr: list[int]) -> int:
    """Count the number of pairs whose difference equals k."""
    # Time: O(n log n)   Space: O(n)
    a = sorted(arr)
    i = 0
    j = 1
    count = 0
    while j < len(a):
        diff = a[j] - a[i]
        if diff == k:
            count += 1
            j += 1
        elif diff > k:
            i += 1
        else:
            j += 1
    return count


def test() -> None:
    # arr = [1, 5, 3, 4, 2], k = 2 -> pairs: (1,3),(5,3),(4,2),(3,1?) -> {(3,1),(5,3),(4,2)} = 3
    assert pairs(2, [1, 5, 3, 4, 2]) == 3
    # consecutive integers, k = 1 -> every adjacent pair: 4 pairs
    assert pairs(1, [1, 2, 3, 4, 5]) == 4
    # no pair matches
    assert pairs(10, [1, 2, 3]) == 0
    # edge case: single element, no pair possible
    assert pairs(1, [5]) == 0
