import re

isFirst = True
for line in open(0).read().rsplit():
    if isFirst:
        isFirst = False
        continue
    res = re.fullmatch('(100+1+|01)+', line) and "YES" or "NO"
    print(res)
