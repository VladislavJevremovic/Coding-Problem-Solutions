# https://www.hackerrank.com/challenges/the-birthday-bar/problem
# HackerRank: Birthday Chocolate


def birthday(s: list[int], d: int, m: int) -> int:
    """Count length-m contiguous segments of s whose values sum to d."""
    # Time: O(n * m)   Space: O(1)
    n = len(s)
    if m > n:
        return 0
    return sum(1 for i in range(n - m + 1) if sum(s[i : i + m]) == d)


def test() -> None:
    assert birthday([1, 2, 1, 3, 2], 3, 2) == 2  # [1,2] and [1,?]; [1,2],[1,3->no]
    assert birthday([1, 1, 1, 1, 1, 1], 3, 2) == 0  # all pairs sum to 2
    assert birthday([4], 4, 1) == 1
    # Edge: segment longer than bar
    assert birthday([1, 2], 5, 3) == 0
