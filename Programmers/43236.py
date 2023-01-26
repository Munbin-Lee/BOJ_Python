from itertools import combinations


def removeRock(diff, idxs):
    d = diff[:]
    cnt = 0
    for idx in idxs:
        tmp = d.pop(idx-cnt)
        d[idx-cnt] += tmp
        cnt += 1
    return d


def solution(distance, rocks, n):
    rocks.sort()
    rocks.insert(0, 0)
    rocks.append(distance)
    diff = []

    for i in range(1, len(rocks)):
        diff.append(rocks[i]-rocks[i-1])

    mx = 0
    for ls in list(combinations(range(len(diff)-1), n)):
        mx = max(mx, min(removeRock(diff, ls)))
    return mx


d = 25
r = [2, 11, 14, 17, 21]
n = 2
res = solution(d, r, n)
print(res)
