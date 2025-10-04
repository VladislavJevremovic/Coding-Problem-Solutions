# https://www.hackerrank.com/challenges/jim-and-the-orders/problem
# HackerRank: Jim and the Orders


def jim_orders(orders: list[list[int]]) -> list[int]:
    """Return customer numbers (1-indexed) in the order their food is served.

    Each order is [order_time, prep_time]; serve time is their sum. Ties are
    broken by the original customer number (stable sort preserves this).
    """
    # Time: O(n log n)   Space: O(n)
    indexed = sorted(
        range(len(orders)),
        key=lambda i: orders[i][0] + orders[i][1],
    )
    return [i + 1 for i in indexed]


def test() -> None:
    # serve times: c1=8, c2=8, c3=8 -> tie broken by order number.
    assert jim_orders([[8, 1], [4, 2], [5, 6]]) == [2, 1, 3]
    # serve times: c1=3, c2=6, c3=8 -> already in order.
    assert jim_orders([[1, 2], [3, 3], [4, 4]]) == [1, 2, 3]
    # Edge case: single order.
    assert jim_orders([[5, 5]]) == [1]
