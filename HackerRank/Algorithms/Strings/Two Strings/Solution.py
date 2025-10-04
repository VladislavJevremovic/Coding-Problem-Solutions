# https://www.hackerrank.com/challenges/two-strings/problem
# HackerRank: Two Strings


def twoStrings(s1: str, s2: str) -> str:
    """'YES' if the two strings share any character, else 'NO'."""
    # Time: O(n)   Space: O(n)
    return "YES" if set(s1) & set(s2) else "NO"


def test():
    # Share common substring 'a' (single char counts).
    assert twoStrings("hello", "world") == "YES"
    # No common character.
    assert twoStrings("hi", "world") == "NO"
    # Identical strings share everything.
    assert twoStrings("abc", "abc") == "YES"
    # Empty string shares nothing.
    assert twoStrings("", "abc") == "NO"
