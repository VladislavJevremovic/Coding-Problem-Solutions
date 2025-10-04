# https://www.hackerrank.com/challenges/alternating-characters/problem
# HackerRank: Alternating Characters


def alternating_characters(s: str) -> int:
    """Return the number of deletions needed so no two adjacent chars match."""
    # Time: O(n)   Space: O(n)
    return sum(1 for a, b in zip(s, s[1:]) if a == b)


def test() -> None:
    assert alternating_characters("AAAA") == 3
    assert alternating_characters("BBBBB") == 4
    assert alternating_characters("ABABABAB") == 0
    assert alternating_characters("AABBABAB") == 2
    # Edge case: single character needs no deletions.
    assert alternating_characters("A") == 0
