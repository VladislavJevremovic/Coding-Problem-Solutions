# https://www.hackerrank.com/challenges/xor-strings/problem
# HackerRank: XOR Strings


def strings_xor(s: str, t: str) -> str:
    """Bitwise XOR of two equal-length binary strings: '0' where chars match, '1' otherwise."""
    # Time: O(n)   Space: O(n)
    return "".join("0" if cs == ct else "1" for cs, ct in zip(s, t))


def test() -> None:
    assert strings_xor("10101", "00101") == "10000"
    assert strings_xor("1110", "1010") == "0100"
    assert strings_xor("000", "000") == "000"
