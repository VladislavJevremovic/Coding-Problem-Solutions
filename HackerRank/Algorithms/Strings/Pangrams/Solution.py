# https://www.hackerrank.com/challenges/pangrams/problem
# HackerRank: Pangrams
from string import ascii_lowercase


def pangrams(s: str) -> str:
    """'pangram' if s contains every letter of the alphabet, else 'not pangram'."""
    # Time: O(n)   Space: O(1)
    letters = {c for c in s.lower() if c in ascii_lowercase}
    return "pangram" if len(letters) == 26 else "not pangram"


def test() -> None:
    assert (
        pangrams("We promptly judged antique ivory buckles for the next prize")
        == "pangram"
    )
    assert (
        pangrams("We promptly judged antique ivory buckles for the prize")
        == "not pangram"
    )
    assert pangrams("The quick brown fox jumps over the lazy dog") == "pangram"
