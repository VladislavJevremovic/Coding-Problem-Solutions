# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
# Painless


def solution(N: int) -> int:
    """Take the binary string, strip trailing zeros, and measure the longest zero run between ones."""
    # Time: O(log n)   Space: O(log n)
    # Split on '1' boundaries; the longest run of zeros bounded by ones is the gap.
    gaps = bin(N)[2:].strip("0").split("1")
    return max((len(gap) for gap in gaps), default=0)


def test() -> None:
    assert solution(1041) == 5
    assert solution(32) == 0
    assert solution(9) == 2
    assert solution(529) == 4
    assert solution(20) == 1
    assert solution(15) == 0
