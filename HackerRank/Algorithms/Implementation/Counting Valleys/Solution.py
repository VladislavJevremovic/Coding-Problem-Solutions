# https://www.hackerrank.com/challenges/counting-valleys/problem
# HackerRank: Counting Valleys
def counting_valleys(steps: int, path: str) -> int:
    """Track altitude; count each time an upstep returns to sea level."""
    # Time: O(n)   Space: O(1)
    level = 0
    valleys = 0
    for step in path:
        if step == "U":
            level += 1
            # Surfacing from below sea level back to 0 ends a valley.
            if level == 0:
                valleys += 1
        else:  # 'D'
            level -= 1
    return valleys


def test() -> None:
    assert counting_valleys(8, "UDDDUDUU") == 1
    assert counting_valleys(12, "DDUUDDUDUUUD") == 2
    assert counting_valleys(4, "UUUU") == 0
