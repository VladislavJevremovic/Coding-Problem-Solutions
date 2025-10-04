# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
# HackerRank: HackerRank in a String!


def hackerrank_in_string(s: str) -> str:
    """Return "YES" if "hackerrank" is a subsequence of s, else "NO"."""
    # Time: O(n)   Space: O(1)
    mask = "hackerrank"
    position = 0
    for c in s:
        if position < len(mask) and c == mask[position]:
            position += 1
    return "YES" if position == len(mask) else "NO"


def test() -> None:
    assert hackerrank_in_string("hereiamstackerrank") == "YES"
    assert hackerrank_in_string("hackerworld") == "NO"
    assert hackerrank_in_string("hhaacckkekrarannk") == "YES"
    # Edge case: empty string can't contain the subsequence.
    assert hackerrank_in_string("") == "NO"
