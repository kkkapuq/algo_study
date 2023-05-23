N = int(input())

# day, lateness limt by 2(non-contiguous) , absent defined by 3 contiguous days
dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)]
M = 1000000
dp[1][0] = [1, 1, 0]
dp[1][1] = [1, 0, 0]

for i in range(2, N + 1):
    for j in range(2):
        for k in range(3):
            # this code block illustrates pass condition
            # if current status is normal
            dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k])%M

            # if current status is late (j == 1)
            if j > 0:
                dp[i][j][0] = (dp[i][j][0] + dp[i - 1][0][k])%M

            # if current state is absent (allowed contiguous # of absentness is 1 or 2)
            if k > 0:
                dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1])%M

print(sum(dp[N][j][k] for j in range(2) for k in range(3))%M)