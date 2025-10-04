# https://www.hackerrank.com/challenges/solve-me-first/problem
# HackerRank: Solve Me First


def solve_me_first(a: int, b: int) -> int:
    """Return the sum of two integers."""
    # Time: O(1)   Space: O(1)
    return a + b


def test() -> None:
    assert solve_me_first(2, 3) == 5
    assert solve_me_first(100, 200) == 300
    assert solve_me_first(-1, 1) == 0
