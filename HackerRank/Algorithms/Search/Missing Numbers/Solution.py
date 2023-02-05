def missingNumbers(arr, brr):
    d = {}

    for b in brr:
        if b not in d:
            d[b] = 0
        d[b] += 1

    for a in arr:
        if a not in d:
            d[b] = 0
        d[a] -= 1

    return sorted([k for k, v in d.items() if v != 0])