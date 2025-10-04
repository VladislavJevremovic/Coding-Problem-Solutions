# https://www.hackerrank.com/challenges/utopian-tree/problem
# HackerRank: Utopian Tree
def utopian_tree(n: int) -> int:
    """Simulate n cycles, doubling height each spring and adding one each summer."""
    # Time: O(n)   Space: O(1)
    height = 1
    for cycle in range(1, n + 1):
        if cycle % 2 == 1:  # spring: doubles
            height *= 2
        else:  # summer: grows by 1
            height += 1
    return height


def test() -> None:
    assert utopian_tree(0) == 1
    assert utopian_tree(1) == 2
    assert utopian_tree(4) == 7
    assert utopian_tree(5) == 14
