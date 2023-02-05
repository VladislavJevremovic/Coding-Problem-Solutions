def dynamic_array(n, queries):
    r = []
    seq_list = [[] for i in range(n)]
    last_answer = 0
    for query in queries:
        (c, x, y) = (query[0], query[1], query[2])
        if c == 1:
            seq_list[(x ^ last_answer) % n].append(y)
        elif c == 2:
            seq = seq_list[(x ^ last_answer) % n]
            size = len(seq)
            last_answer = seq[y % size]
            r.append(last_answer)

    return r