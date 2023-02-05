stack = []
n = int(input())
for _ in range(n):
    cmd = list(map(int, input().split()))
    c = cmd[0]
    if c == 1:
        x = cmd[1]
        current_max = stack[-1][1] if len(stack) > 0 else 0
        e = (x, max(x, current_max))
        stack.append(e)
    elif c == 2:
        stack.pop()
    elif c == 3:
        print(stack[-1][1])