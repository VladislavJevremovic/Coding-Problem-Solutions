# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/
# Painless


def solution(S: str) -> int:
    """Track a single nesting-depth counter, failing if it ever goes negative or ends nonzero."""
    # Time: O(n)   Space: O(1)
    depth = 0

    for c in S:
        if c == "(":
            depth += 1
        else:
            if depth == 0:
                return 0
            depth -= 1

    return 1 if depth == 0 else 0


def test() -> None:
    assert solution("(()(())())") == 1
    assert solution("())") == 0
    assert solution("") == 1
    assert solution("(") == 0
