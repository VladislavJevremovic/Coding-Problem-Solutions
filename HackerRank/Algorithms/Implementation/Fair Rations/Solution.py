# https://www.hackerrank.com/challenges/fair-rations/problem
# HackerRank: Fair Rations


def fair_rations(b: list[int]) -> str:
    """Sweep left to right, pushing each odd parity rightward via paired loaves."""
    # Time: O(n)   Space: O(1)
    n = len(b)
    loaves = 0
    carry = 0
    for i in range(n):
        if (b[i] + carry) % 2 == 1:
            if i == n - 1:
                return "NO"
            loaves += 2
            carry = 1
        else:
            carry = 0
    return str(loaves)


def test() -> None:
    assert fair_rations([2, 3, 4, 5, 6]) == "4"
    assert fair_rations([1, 2]) == "NO"  # single odd at the end can't be fixed
    assert fair_rations([1, 1]) == "2"  # give to both -> all even
    # Edge: already all even
    assert fair_rations([2, 4, 6]) == "0"
