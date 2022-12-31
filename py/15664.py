from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

res = set()
for i in combinations(ls, m):
    res.add(i)
res = sorted(res)

for i in res:
    for j in i:
        print(j, end=' ')
    print()
