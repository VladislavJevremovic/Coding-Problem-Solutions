def topView(root):
    q = Queue()
    m = {}

    if root:
        root.level = 0
        q.put(root)

    while not q.empty():
        n = q.get()

        level = n.level
        if not level in m:
            m[level] = n.info

        if n.left:
            n.left.level = level - 1
            q.put(n.left)
        if n.right:
            n.right.level = level + 1
            q.put(n.right)

    for k in sorted(m):
        print(m[k], end=' ')