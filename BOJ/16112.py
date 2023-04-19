stdin = open(0)
n, k = map(int, stdin.readline().rsplit())
exps = sorted(map(int, stdin.readline().rsplit()))

numStone = 0
sumExp = 0
for exp in exps:
    sumExp += exp * numStone
    numStone = min(numStone + 1, k)

print(sumExp)
