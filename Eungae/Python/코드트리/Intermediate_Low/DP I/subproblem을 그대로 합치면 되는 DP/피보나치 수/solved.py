import sys
se = sys.stdin.readline

n = int(se().strip())
dp = [0] * n

if n <= 2:
    print(1)
    exit()
dp[0] = 1
dp[1] = 1

for i in range(2, n):
    dp[i] = dp[i-2] - dp[i-1]

print(dp[n-1])