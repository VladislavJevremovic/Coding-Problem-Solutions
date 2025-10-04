# https://www.hackerrank.com/challenges/game-of-thrones-i/problem
# HackerRank: Game of Thrones - I
from collections import Counter


def game_of_thrones(s: str) -> str:
    """'YES' if some permutation of s is a palindrome (at most one odd letter count)."""
    # Time: O(n)   Space: O(1)
    odds = sum(count % 2 for count in Counter(s).values())
    return "YES" if odds <= 1 else "NO"


def test() -> None:
    assert game_of_thrones("aaabbbb") == "YES"
    assert game_of_thrones("cdefghmnopqrstuvw") == "NO"
    assert game_of_thrones("cdcdcdcdeeeef") == "YES"
