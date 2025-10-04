# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
# HackerRank: The Love-Letter Mystery


def the_love_letter_mystery(s: str) -> int:
    """Return the minimum number of operations to make s a palindrome.

    Each operation decrements a single character by one (e.g. 'd' -> 'c').
    """
    # Time: O(n)   Space: O(1)
    n = len(s)
    return sum(abs(ord(s[i]) - ord(s[n - 1 - i])) for i in range(n // 2))


def test() -> None:
    assert the_love_letter_mystery("abc") == 2  # c->a costs 2
    assert the_love_letter_mystery("abcba") == 0  # already a palindrome
    assert the_love_letter_mystery("abcd") == 4  # |a-d| + |b-c| = 3 + 1
    assert the_love_letter_mystery("cba") == 2
    # Edge case: single character is already a palindrome.
    assert the_love_letter_mystery("z") == 0
