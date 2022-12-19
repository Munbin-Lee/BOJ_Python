import sys
input = sys.stdin.readline

n = int(input())
lefts = list(map(int, input().split()))
rights = list(map(int, input().split()))
dp = [[-1]*(n+1) for j in range(n+1)]


def DP(l, r):
    if l == n or r == n:
        return 0
    if dp[l][r] == -1:
        dp[l][r] = 0
        if lefts[l] > rights[r]:
            dp[l][r] = max(dp[l][r+1] + rights[r], dp[l+1][r], dp[l+1][r+1])
            dp[l][r] += rights[r]+DP(l, r+1)
        else:
            dp[l][r] += max(DP(l+1, r), DP(l+1, r+1))
    return dp[l][r]


print(DP(0, 0))
