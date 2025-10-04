# https://www.hackerrank.com/challenges/greedy-florist/problem
# HackerRank: Greedy Florist


def get_minimum_cost(k: int, c: list[int]) -> int:
    """Minimum cost for k friends to buy all flowers in c.

    Each flower's price is multiplied by (previous purchases by that buyer + 1).
    Buying the most expensive flowers first minimizes total cost.
    """
    # Time: O(n log n)   Space: O(n)
    prices = sorted(c, reverse=True)
    return sum(((i // k) + 1) * price for i, price in enumerate(prices))


def test() -> None:
    # 3 flowers, 3 friends: each buys one at base price.
    assert get_minimum_cost(3, [2, 5, 6]) == 13
    # 3 flowers, 2 friends: 6 + 5 + 2*2 = 15.
    assert get_minimum_cost(2, [2, 5, 6]) == 15
    # 1 friend buys all: 3 + 2*2 + 3*1 = 3 + 4 + 3 = 10.
    assert get_minimum_cost(1, [1, 3, 2]) == 10
    # Edge case: single flower at base price.
    assert get_minimum_cost(1, [7]) == 7
