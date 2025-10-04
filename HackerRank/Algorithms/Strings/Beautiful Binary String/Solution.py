# https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# HackerRank: Beautiful Binary String


def beautiful_binary_string(s: str) -> int:
    """Minimum substitutions to remove every '010' substring (greedy non-overlapping)."""
    # Time: O(n)   Space: O(1)
    count = 0
    i = 0
    while i < len(s) - 2:
        if s[i : i + 3] == "010":
            count += 1
            i += 3
        else:
            i += 1
    return count


def test() -> None:
    assert beautiful_binary_string("0101010") == 2
    assert beautiful_binary_string("01100") == 0
    assert beautiful_binary_string("010") == 1
    assert beautiful_binary_string("0100101010") == 3
