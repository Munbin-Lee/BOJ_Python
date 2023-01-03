from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for comb in combinations_with_replacement(range(1, n+1), m):
    for i in comb:
        print(i, end=" ")
    print()
