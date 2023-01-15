import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    s = input().rstrip()
    print("%d. %s" % (i, s))
