# https://app.codility.com/programmers/lessons/99-future_training/str_symmetry_point/
# Painless


def solution(S: str) -> int:
    """An odd-length string has a symmetry point only if it reads as a palindrome around its center."""
    # Time: O(n)   Space: O(1)
    n = len(S)
    if n % 2 == 0:
        return -1

    mid = n // 2
    for i in range(mid):
        if S[i] != S[n - 1 - i]:
            return -1

    return mid


def test() -> None:
    assert solution("racecar") == 3
    assert solution("x") == 0
    assert solution("abcd") == -1
    assert solution("abca") == -1
