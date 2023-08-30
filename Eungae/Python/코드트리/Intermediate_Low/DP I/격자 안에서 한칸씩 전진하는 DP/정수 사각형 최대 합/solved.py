import sys
se = sys.stdin.readline
n = int(input())
arr = []
# 1열과 1행은 별도로 처리해준다.
for i in range(n):
    arr.append(list(map(int, se().split())))

dp = [[0 for j in range(n)] for i in range(n)]
dp[0][0] = arr[0][0]
answer = dp[0][0]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i == 0 and j > 0:
            dp[i][j] = dp[i][j-1] + arr[i][j]
        elif i > 0 and j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i][j]
        answer = max(answer, dp[i][j])

print(answer)
