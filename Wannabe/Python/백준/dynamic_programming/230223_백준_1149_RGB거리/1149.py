import sys
si = sys.stdin.readline

n = int(si().strip())
dp = [[0, 0, 0] for _ in range(n+1)]
cost = [list(map(int, si().strip().split())) for _ in range(n)]
for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i-1][2]
print(min(dp[-1]))