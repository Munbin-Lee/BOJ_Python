stdin = open(0)


def solve():
    line = stdin.readline()
    r, c, data = line.rsplit(' ', 2)
    r = int(r)
    c = int(c)
    message = [[0 for i in range(c)] for j in range(r)]
    curRow = 0
    curCol = 0

    def newLine():
        curRow += 1
        curCol = 0
        if (curRow > r):
            return "TOO BIG"

    for dataIdx in range(0, data):
        pass

    for a in message:
        for b in a:
            print(b, end='')
        print()


n = int(stdin.readline())
for i in range(1, n + 1):
    print(i)
    print(solve())
