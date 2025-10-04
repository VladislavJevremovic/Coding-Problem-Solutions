# https://www.hackerrank.com/challenges/repeated-string/problem
# HackerRank: Repeated String


def repeated_string(s: str, n: int) -> int:
    """Count a's per full copy of s, then add a's in the leftover prefix."""
    # Time: O(L)   Space: O(1)  (L = len(s))
    if not s:
        return 0
    per_copy = s.count("a")
    full, remainder = divmod(n, len(s))
    return per_copy * full + s[:remainder].count("a")


def test() -> None:
    assert repeated_string("aba", 10) == 7  # "abaabaabaa" -> 7 a's
    assert repeated_string("a", 1_000_000_000_000) == 1_000_000_000_000
    # n smaller than the string length
    assert repeated_string("abcac", 10) == 4  # "abcacabcac" -> 4 a's
    # No 'a' at all
    assert repeated_string("bcd", 100) == 0
