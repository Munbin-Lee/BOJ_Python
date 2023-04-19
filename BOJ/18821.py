stdin = open(0)
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    res = n % 2 and 'E' or 'O'
    print(res)
