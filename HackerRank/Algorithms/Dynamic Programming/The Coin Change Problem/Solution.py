# https://www.hackerrank.com/challenges/the-coin-change-problem/problem
# HackerRank: The Coin Change Problem


def get_ways(n: int, coins: list[int]) -> int:
    """Count the number of ways to make change for n using the given coins."""
    # Time: O(n * len(coins))   Space: O(n)
    ways = [0] * (n + 1)
    ways[0] = 1
    for coin in coins:
        for amount in range(coin, n + 1):
            ways[amount] += ways[amount - coin]
    return ways[n]


def test() -> None:
    # make 4 with {1, 2, 3}: {1,1,1,1},{1,1,2},{2,2},{1,3} = 4 ways
    assert get_ways(4, [1, 2, 3]) == 4
    # make 10 with {2, 5, 3, 6}: 5 ways
    assert get_ways(10, [2, 5, 3, 6]) == 5
    # edge case: amount 0 -> exactly one way (use no coins)
    assert get_ways(0, [1, 2]) == 1
    # coin larger than n is ignored
    assert get_ways(3, [5]) == 0
