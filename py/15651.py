from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for i in product(range(1, n+1), repeat=m):
    for j in i:
        print(j, end=' ')
    print()
