from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

for i in product(ls, repeat=m):
    for j in i:
        print(j, end=' ')
    print()
