# https://www.hackerrank.com/challenges/balanced-brackets/problem
# HackerRank: Balanced Brackets


def isBalanced(s):
    """Push openers onto a stack and pop on a matching closer; balanced iff the stack empties."""
    # Time: O(n)   Space: O(n)
    d = {"}": "{", ")": "(", "]": "["}
    stack = []
    for c in s:
        if not stack or c not in d:
            stack.append(c)
        elif d[c] == stack[-1]:
            stack.pop()
        else:
            return "NO"

    return "YES" if len(stack) == 0 else "NO"


def test():
    assert isBalanced("{[()]}") == "YES"
    assert isBalanced("{[(])}") == "NO"
    assert isBalanced("{{[[(())]]}}") == "YES"
    # Unmatched opening bracket.
    assert isBalanced("(") == "NO"
    # Empty string is trivially balanced.
    assert isBalanced("") == "YES"
    # Wrong closing order.
    assert isBalanced("([)]") == "NO"
