def isBalanced(s):
    d = { '}': '{', ')': '(', ']': '[' }
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        elif c not in d:
            stack.append(c)
        elif d[c] == stack[-1]:
            stack.pop()
        else:
            return "NO"
    
    return "YES" if len(stack) == 0 else "NO"