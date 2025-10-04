# https://www.hackerrank.com/challenges/stock-maximize/problem
# HackerRank: Stock Maximize


def stock_max(prices: list[int]) -> int:
    """Maximum profit obtainable by buying/selling with perfect foresight."""
    # Time: O(n)   Space: O(1)
    profit = 0
    max_so_far = 0
    for price in reversed(prices):
        max_so_far = max(max_so_far, price)
        profit += max_so_far - price
    return profit


def test() -> None:
    # prices strictly decreasing -> never profitable
    assert stock_max([5, 3, 2]) == 0
    # prices strictly increasing -> buy all, sell at peak
    # [1,2,100]: buy 1, buy 2, sell both at 100 -> (100-1)+(100-2) = 197
    assert stock_max([1, 2, 100]) == 197
    # mixed [1, 3, 1, 2]: from the right, future-max is 2,2,3,3
    # profit = (2-2)+(2-1)+(3-3)+(3-1) = 3
    assert stock_max([1, 3, 1, 2]) == 3
    # edge case: single price -> no profit
    assert stock_max([10]) == 0
