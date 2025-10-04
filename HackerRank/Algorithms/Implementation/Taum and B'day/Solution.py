# HackerRank: Taum and B'day


def taumBday(b: int, w: int, bc: int, wc: int, z: int) -> int:
    """Buy each color at its own price or convert via z, whichever is cheaper."""
    # Time: O(1)   Space: O(1)
    if bc > wc + z:
        return b * (wc + z) + w * wc
    elif wc > bc + z:
        return b * bc + (bc + z) * w
    else:
        return b * bc + w * wc


def test():
    # Buy black at white+z when black is more expensive than converting.
    # b=10, w=10, bc=1, wc=1, z=1 -> no conversion helps: 10*1 + 10*1 = 20
    assert taumBday(10, 10, 1, 1, 1) == 20
    # Black costlier than white+z: buy black as white+z.
    # b=5, w=9, bc=5, wc=1, z=1 -> 5*(1+1) + 9*1 = 10 + 9 = 19
    assert taumBday(5, 9, 5, 1, 1) == 19
    # White costlier than black+z: buy white as black+z.
    # b=3, w=6, bc=1, wc=5, z=1 -> 3*1 + (1+1)*6 = 3 + 12 = 15
    assert taumBday(3, 6, 1, 5, 1) == 15
    # Zero gifts costs nothing.
    assert taumBday(0, 0, 100, 100, 100) == 0
