# https://www.hackerrank.com/challenges/electronics-shop/problem
# HackerRank: Electronics Shop


def get_money_spent(keyboards: list[int], drives: list[int], b: int) -> int:
    """Try every keyboard/drive pair, keeping the priciest total within budget b."""
    # Time: O(n * m)   Space: O(1)
    best = -1
    for kb in keyboards:
        for drive in drives:
            total = kb + drive
            if total <= b and total > best:
                best = total
    return best


def test() -> None:
    assert get_money_spent([3, 1], [5, 2, 8], 10) == 9  # 1+8
    assert get_money_spent([4], [5], 5) == -1  # nothing affordable
    assert get_money_spent([40, 50], [5, 12], 60) == 55  # 50+5
