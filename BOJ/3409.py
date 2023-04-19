import re
from collections import defaultdict


def isConst(s):
    return 'a' <= s[0] <= 'z'


def find(x):
    if not dict[x]:
        sumLeft, sumRight = lazy[x]
        dict[x] = find(sumLeft) + find(sumRight)
    return dict[x]


def isSubsequence(a, b):
    it = iter(b)
    return all(c in it for c in a)


stdin = open(0)
n = int(stdin.readline())
dict = None
lazy = None

for i in range(n):
    numExp = int(stdin.readline())
    dict = defaultdict(str)
    lazy = defaultdict(list)
    for j in range(numExp):
        exp = stdin.readline().rstrip()
        left, right = re.fullmatch('(.*) = (.*)', exp).groups()
        if isConst(right):
            dict[left] = right
        else:
            sumLeft, sumRight = re.fullmatch('(.*) \+ (.*)', right).groups()
            if dict[sumLeft] and dict[sumRight]:
                dict[left] = sumLeft + sumRight
                continue
            lazy[left] = [sumLeft, sumRight]
    t, p = stdin.read().rsplit()
    t = find(t)
    res = isSubsequence(p, t) and "YES" or "NO"
    print(res)
