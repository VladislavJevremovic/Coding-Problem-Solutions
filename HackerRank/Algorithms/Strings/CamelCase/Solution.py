# https://www.hackerrank.com/challenges/camelcase/problem
# HackerRank: CamelCase


def camelcase(s: str) -> int:
    """Number of words in a camelCase string: one plus the count of uppercase letters."""
    # Time: O(n)   Space: O(1)
    return 1 + sum(c.isupper() for c in s)


def test() -> None:
    assert camelcase("saveChangesInTheEditor") == 5
    assert camelcase("oneWord") == 2
    assert camelcase("oneword") == 1
