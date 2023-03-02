import sys
si = sys.stdin.readline

n = int(si().strip())
info = [list(map(int, si().strip().split())) for _ in range(n)]
dp = [[0]*i for i in range(1, n+1)]
dp[0][0] = info[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]+info[i][j]
            continue
        elif j == i:
            dp[i][j] = dp[i-1][j-1]+info[i][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + info[i][j]
        
print(max(dp[n-1]))