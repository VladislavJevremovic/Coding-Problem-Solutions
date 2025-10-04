# https://www.hackerrank.com/challenges/cavity-map/problem
# HackerRank: Cavity Map


def cavity_map(grid: list[str]) -> list[str]:
    """Mark each interior cell strictly greater than all four neighbors as a cavity."""
    # Time: O(n^2)   Space: O(n^2)  (n = grid side length)
    n = len(grid)
    result: list[str] = []
    for i in range(n):
        if i < 1 or i > n - 2:
            result.append(grid[i])
            continue

        chars = list(grid[i])
        for j in range(1, n - 1):
            center = int(grid[i][j])
            up = int(grid[i - 1][j])
            down = int(grid[i + 1][j])
            left = int(grid[i][j - 1])
            right = int(grid[i][j + 1])
            if center > up and center > down and center > left and center > right:
                chars[j] = "X"
        result.append("".join(chars))

    return result


def test() -> None:
    grid = ["1112", "1912", "1892", "1234"]
    assert cavity_map(grid) == ["1112", "1X12", "18X2", "1234"]
    # Edge: 1x1 grid stays unchanged (borders)
    assert cavity_map(["5"]) == ["5"]
    # Edge: no interior cell qualifies
    assert cavity_map(["111", "111", "111"]) == ["111", "111", "111"]
