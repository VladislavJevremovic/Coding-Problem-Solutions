# https://www.hackerrank.com/challenges/sock-merchant/problem
# HackerRank: Sock Merchant
from collections import Counter


def sock_merchant(n: int, ar: list[int]) -> int:
    """Sum half of each color's count to total the matching sock pairs."""
    # Time: O(n)   Space: O(n)
    return sum(count // 2 for count in Counter(ar).values())


def test() -> None:
    assert sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
    assert sock_merchant(0, []) == 0
    # Edge: odd counts
    assert sock_merchant(3, [1, 1, 1]) == 1
