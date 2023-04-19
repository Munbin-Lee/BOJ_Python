import re
from collections import defaultdict


def isDigit(s):
    return '0' <= s[-1] <= '9'


class UnionFind:
    NULL = 10987654321
    parent = {}  # any to any
    const = defaultdict(lambda: UnionFind.NULL)  # any to num

    def isConstProper(self, a, b):
        if self.const[a] == self.NULL or self.const[b] == self.NULL:
            return True
        else:
            return self.const[a] == self.const[b]

    def isConstDifferent(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if self.const[a] == self.NULL or self.const[b] == self.NULL:
            return False
        else:
            return self.const[a] != self.const[b]

    def find_rec(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x

        if self.parent[x] == x:
            return x

        self.parent[x] = self.find_rec(self.parent[x])
        return self.parent[x]

    def find(self, x):
        if isDigit(x):
            self.const[x] = int(x)

        if x not in self.parent:
            self.parent[x] = x
            return x

        tmp_x = x
        # p = self.find_rec(x)

        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        p = x

        self.const[p] = min(self.const[p], self.const[tmp_x])
        return p

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        self.const[a] = min(self.const[a], self.const[b])
        self.const[b] = self.const[a]

        if len(a) < len(b):
            self.parent[b] = a
        else:
            self.parent[a] = b


def solve():
    input = open(0).read().rstrip()
    output = ''

    unionFind = UnionFind()
    equals = []
    inequals = []

    for left, exp, right, _ in re.findall('(.*?)(==|!=)(.*?)(&&|$)', input):
        ls = [left, right]

        if exp == '==':
            equals.append(ls)
        else:
            inequals.append(ls)

    equalProcesses = set()

    for left, right in equals:
        left = unionFind.find(left)
        right = unionFind.find(right)

        if left == right:
            continue

        if not unionFind.isConstProper(left, right):
            return '0==1'

        equalProcesses.add(left)
        equalProcesses.add(right)
        unionFind.union(left, right)

    for process in equalProcesses:
        p = unionFind.find(process)
        if (p == process):
            continue

        output += p + '==' + process + '&&'

    inequalProcesses = set()

    for left, right in inequals:
        left = unionFind.find(left)
        right = unionFind.find(right)

        if left == right:
            return '0==1'

        if unionFind.isConstDifferent(left, right):
            continue

        if left > right:
            left, right = right, left

        process = left + '!=' + right + '&&'
        inequalProcesses.add(process)

    for process in inequalProcesses:
        output += process

    if not output:
        return '1==1'
    else:
        return output[:-2]


print(solve())
