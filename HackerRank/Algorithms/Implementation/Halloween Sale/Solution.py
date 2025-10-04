# https://www.hackerrank.com/challenges/halloween-sale/problem
# HackerRank: Halloween Sale


def how_many_games(p: int, d: int, m: int, s: int) -> int:
    """Buy games while affordable, dropping the price by d down to floor m."""
    # Time: O(g)   Space: O(1)  (g = games bought)
    count = 0
    funds = s
    price = p
    while funds >= price:
        funds -= price
        count += 1
        price = max(price - d, m)
    return count


def test() -> None:
    # p=20,d=3,m=6,s=80: 20,17,14,11,8,6 sum=76<=80 next 6 -> 82>80 => 6 games
    assert how_many_games(20, 3, 6, 80) == 6
    # Not enough for the first game
    assert how_many_games(20, 3, 6, 19) == 0
    # Floor m reached, keeps buying at m
    assert how_many_games(20, 3, 6, 85) == 7
