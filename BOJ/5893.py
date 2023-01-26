import sys
input = sys.stdin.readline

n = int(input(), 2)
n *= 17
print(bin(n)[2:])
