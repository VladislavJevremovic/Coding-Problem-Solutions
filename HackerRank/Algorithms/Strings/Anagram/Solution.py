# https://www.hackerrank.com/challenges/anagram/problem
# HackerRank: Anagram
from collections import Counter


def anagram(s: str) -> int:
    """Min character changes to make the two halves anagrams; -1 if length is odd."""
    # Time: O(n)   Space: O(1)
    if len(s) % 2 != 0:
        return -1
    half = len(s) // 2
    diff = Counter(s[:half])
    diff.subtract(Counter(s[half:]))
    return sum(abs(v) for v in diff.values()) // 2


def test() -> None:
    assert anagram("aaabbb") == 3
    assert anagram("ab") == 1
    assert anagram("abc") == -1
    assert anagram("mnop") == 2
    assert anagram("xyyx") == 0
