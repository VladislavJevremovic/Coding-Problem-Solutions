#!/bin/python3

from heapq import heappop, heappush, heapify

[n, k] = [int(x) for x in input().split()]
cookies = [int(x) for x in input().split()]

heapify(cookies)

op_count = 0
try:
    while cookies[0] < k:
        op_count += 1
        c1 = heappop(cookies)
        c2 = heappop(cookies)
        new_cookie = (1 * c1) + (2 * c2)
        heappush(cookies, new_cookie)
    print(op_count)
except:
    print("-1")
