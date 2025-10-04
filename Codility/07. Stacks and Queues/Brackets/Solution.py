# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
# Painless


def solution(S: str) -> int:
    """Push openers on a stack and pop on closers, requiring a matching opener for balance."""
    # Time: O(n)   Space: O(n)
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for c in S:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or stack.pop() != pairs[c]:
                return 0

    return 1 if not stack else 0


def test() -> None:
    assert solution("{[()()]}") == 1
    assert solution("([)()]") == 0
    assert solution("") == 1
    assert solution("(") == 0
    assert solution(")(") == 0
