# https://www.hackerrank.com/challenges/kangaroo/problem
# HackerRank: Kangaroo
def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    """They meet iff the lead kangaroo is faster and the gap divides the speed diff."""
    # Time: O(1)   Space: O(1)
    # They meet when (x2 - x1) is divisible by the closing speed (v1 - v2).
    if v1 <= v2:
        return "NO"
    return "YES" if (x2 - x1) % (v1 - v2) == 0 else "NO"


def test() -> None:
    assert kangaroo(0, 3, 4, 2) == "YES"
    assert kangaroo(0, 2, 5, 3) == "NO"
    assert kangaroo(43, 2, 70, 2) == "NO"
