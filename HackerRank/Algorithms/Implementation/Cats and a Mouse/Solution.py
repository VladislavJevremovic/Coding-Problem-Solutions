# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# HackerRank: Cats and a Mouse
def cat_and_mouse(x: int, y: int, z: int) -> str:
    """Compare each cat's distance to the mouse; equal distances mean it escapes."""
    # Time: O(1)   Space: O(1)
    dist_a = abs(x - z)
    dist_b = abs(y - z)
    if dist_a < dist_b:
        return "Cat A"
    if dist_b < dist_a:
        return "Cat B"
    return "Mouse C"


def test() -> None:
    assert cat_and_mouse(1, 2, 3) == "Cat B"
    assert cat_and_mouse(1, 3, 2) == "Mouse C"
    assert cat_and_mouse(2, 5, 3) == "Cat A"
