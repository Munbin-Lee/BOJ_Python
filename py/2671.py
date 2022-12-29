import re
import sys
input = sys.stdin.readline

pat = re.compile("(100+1+|01)+")


def solve(s):
    if pat.fullmatch(s):
        return True
    return False


s = input().rstrip()
print(solve(s) and "SUBMARINE" or "NOISE")
