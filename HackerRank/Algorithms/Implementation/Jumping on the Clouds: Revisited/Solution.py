# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# HackerRank: Jumping on the Clouds: Revisited


def jumping_on_clouds(c: list[int], k: int) -> int:
    """Hop by k around the circle, spending energy until returning to the start."""
    # Time: O(n)   Space: O(1)
    energy = 100
    i = 0
    while True:
        i = (i + k) % len(c)
        energy -= 1
        if c[i] == 1:
            energy -= 2
        if i == 0:
            break
    return energy


def test() -> None:
    # Sample: c=[0,0,1,0,0,1,1,0], k=2 -> 92
    assert jumping_on_clouds([0, 0, 1, 0, 0, 1, 1, 0], 2) == 92
    # All zero clouds, k=1, n=8 -> 8 jumps, no thunder -> 92
    assert jumping_on_clouds([0] * 8, 1) == 92
    # k divides back immediately to start with one thunderhead
    assert jumping_on_clouds([0, 0], 2) == 99  # i:0->0 after one jump, c[0]=0
