# https://www.hackerrank.com/challenges/caesar-cipher/problem
# HackerRank: Caesar Cipher
from string import ascii_lowercase, ascii_uppercase


def caesar_cipher(s: str, k: int) -> str:
    """Shift every letter forward by k positions, wrapping within its case."""
    # Time: O(n)   Space: O(n)
    k %= 26

    def shift(c: str) -> str:
        if c in ascii_lowercase:
            return chr((ord(c) - ord("a") + k) % 26 + ord("a"))
        if c in ascii_uppercase:
            return chr((ord(c) - ord("A") + k) % 26 + ord("A"))
        return c

    return "".join(shift(c) for c in s)


def test() -> None:
    assert caesar_cipher("middle-Outz", 2) == "okffng-Qwvb"
    assert caesar_cipher("abc", 26) == "abc"
    assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"
