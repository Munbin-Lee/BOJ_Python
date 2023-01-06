import sys
input = sys.stdin.readline

for i in range(3):
    n = int(input())
    s = 0
    for j in range(n):
        s += int(input())
    if (s > 0):
        print('+')
    elif (s < 0):
        print('-')
    else:
        print(0)
