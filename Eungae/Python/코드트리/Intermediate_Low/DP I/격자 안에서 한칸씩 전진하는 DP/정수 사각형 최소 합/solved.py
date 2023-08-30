import sys
se = sys.stdin.readline
n = int(input())
arr = []
# 1열과 1행은 별도로 처리해준다.
for i in range(n):
    arr.append(list(map(int, se().split())))

if n == 1:
    print(arr[0][0])
    exit()

dp = [[0 for j in range(n)] for i in range(n)]
dp[0][-1] = arr[0][-1]

for i in range(n):
    for j in range(n-1, -1, -1):
        if i == 0 and j == n-1:
            continue
        if i == 0 and j < n-1:
            dp[i][j] = dp[i][j+1] + arr[i][j]
        elif i > 0 and j == n-1:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + arr[i][j]

print(dp[n-1][0])
