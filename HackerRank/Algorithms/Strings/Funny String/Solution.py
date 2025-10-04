# https://www.hackerrank.com/challenges/funny-string/problem
# HackerRank: Funny String


def funny_string(s: str) -> str:
    """'Funny' if abs-diffs of adjacent chars match those of the reversed string."""
    # Time: O(n)   Space: O(n)
    r = s[::-1]
    forward = [abs(ord(s[i + 1]) - ord(s[i])) for i in range(len(s) - 1)]
    backward = [abs(ord(r[i + 1]) - ord(r[i])) for i in range(len(r) - 1)]
    return "Funny" if forward == backward else "Not Funny"


def test() -> None:
    assert funny_string("acxz") == "Funny"
    assert funny_string("bcxz") == "Not Funny"
    assert funny_string("ivvkxq") == "Not Funny"
