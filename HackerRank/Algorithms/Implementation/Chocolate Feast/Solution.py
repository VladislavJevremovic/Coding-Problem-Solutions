# https://www.hackerrank.com/challenges/chocolate-feast/problem
# HackerRank: Chocolate Feast


def chocolate_feast(n: int, c: int, m: int) -> int:
    """Buy bars with money, then keep trading m wrappers for extra bars."""
    # Time: O(log n)   Space: O(1)
    bars = n // c
    total = bars
    wrappers = bars
    while wrappers >= m:
        traded, wrappers = divmod(wrappers, m)
        total += traded
        wrappers += traded
    return total


def test() -> None:
    # 10 money, cost 2, 5 wrappers -> 5 bars, trade 5 wrappers -> 1 more = 6
    assert chocolate_feast(10, 2, 5) == 6
    # 12 money, cost 4, 4 wrappers -> 3 bars, no trade (3<4) = 3
    assert chocolate_feast(12, 4, 4) == 3
    # 6 money, cost 2, 2 wrappers -> 3 bars, 3//2=1 +1wrap=2 ->1 more =>5
    assert chocolate_feast(6, 2, 2) == 5
    # Edge: can't afford any bar
    assert chocolate_feast(1, 2, 2) == 0
