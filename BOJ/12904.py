from collections import deque


def myReverse(s):
    return s[::-1]


def solve():
    s, t = open(0).read().splitlines()
    dq = deque()
    dq.append(t)
    while dq:
        cur = dq.popleft()
        if not cur:
            continue
        if cur == s:
            return 1
        if cur[-1] == 'A':
            dq.append(cur[:-1])
        else:
            dq.append(myReverse(cur[:-1]))
    return 0


print(solve())
