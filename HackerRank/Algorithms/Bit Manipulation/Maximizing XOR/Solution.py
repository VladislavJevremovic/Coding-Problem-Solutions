# https://www.hackerrank.com/challenges/maximizing-xor/problem
# HackerRank: Maximizing XOR


def maximizing_xor(l: int, r: int) -> int:
    """Return the maximum value of a ^ b for l <= a <= b <= r."""
    # Time: O((r - l)^2)   Space: O(1)
    return max(a ^ b for a in range(l, r + 1) for b in range(a, r + 1))


def test() -> None:
    assert maximizing_xor(10, 15) == 7  # 10 ^ 13 = 7
    assert maximizing_xor(5, 6) == 3  # 5 ^ 6 = 3
    # Edge case: l == r -> only pair is (l, l) giving 0.
    assert maximizing_xor(8, 8) == 0
