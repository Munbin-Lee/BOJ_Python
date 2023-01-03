from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

res = set()
for i in combinations_with_replacement(ls, m):
    res.add(i)

res = sorted(res)
for i in res:
    for j in i:
        print(j, end=' ')
    print()
