# https://www.hackerrank.com/challenges/manasa-and-stones/problem
# HackerRank: Manasa and the Stones


def stones(n: int, a: int, b: int) -> list[int]:
    """Enumerate every i*a + (n-1-i)*b last-stone total and return them sorted."""
    # Time: O(n log n)   Space: O(n)
    # The last stone value is sum of (n-1) steps, each step either a or b.
    # Possible totals: i*a + (n-1-i)*b for i in 0..n-1.
    return sorted({i * a + (n - 1 - i) * b for i in range(n)})


def test() -> None:
    assert stones(3, 1, 2) == [2, 3, 4]
    assert stones(4, 10, 100) == [30, 120, 210, 300]
    # Edge: single stone -> always starts at 0
    assert stones(1, 5, 7) == [0]
    # Edge: a == b collapses to one value
    assert stones(3, 2, 2) == [4]
