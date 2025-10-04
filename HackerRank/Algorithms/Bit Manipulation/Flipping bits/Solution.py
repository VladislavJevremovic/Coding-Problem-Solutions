# https://www.hackerrank.com/challenges/flipping-bits/problem
# HackerRank: Flipping bits


def flipping_bits(n: int) -> int:
    """Flip all 32 bits of an unsigned integer and return the result."""
    # Time: O(1)   Space: O(1)
    return n ^ 0xFFFFFFFF


def test() -> None:
    assert flipping_bits(2147483647) == 2147483648
    assert flipping_bits(1) == 4294967294
    assert flipping_bits(0) == 4294967295
    assert flipping_bits(4294967295) == 0
