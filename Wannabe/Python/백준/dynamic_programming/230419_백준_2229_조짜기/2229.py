import sys

si = sys.stdin.readline
n = int(si().strip())
score = [0]+list(map(int, si().strip().split()))

dp = [0] * (n + 1)
for i in range(2, n + 1):
    maxVal = 0
    for j in range(i):
        rsplit = score[i - j:i + 1]
        maxVal = max(maxVal, max(rsplit) - min(rsplit) + dp[i - j - 1])
    dp[i] = maxVal
print(dp[n])
