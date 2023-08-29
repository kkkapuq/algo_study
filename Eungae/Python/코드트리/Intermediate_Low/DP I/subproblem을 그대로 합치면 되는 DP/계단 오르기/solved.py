n = int(input())

dp = [0] * n

if n <= 4:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, n):
        dp[i] = dp[i-3] + dp[i-2]

    print(dp[n-1] % 10007)