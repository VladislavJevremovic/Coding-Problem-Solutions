# https://www.hackerrank.com/challenges/mars-exploration/problem
# HackerRank: Mars Exploration


def mars_exploration(s: str) -> int:
    """Count characters that differ from the repeated 'SOS' pattern."""
    # Time: O(n)   Space: O(n)
    pattern = "SOS" * (len(s) // 3)
    return sum(a != b for a, b in zip(s, pattern))


def test() -> None:
    assert mars_exploration("SOSSPSSQSSOR") == 3
    assert mars_exploration("SOSSOT") == 1
    assert mars_exploration("SOSSOSSOS") == 0
