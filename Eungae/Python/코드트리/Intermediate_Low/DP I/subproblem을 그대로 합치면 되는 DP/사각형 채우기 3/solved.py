MOD = 1000000007

# 변수 선언 및 입력:
n = int(input())

dp = [0] * (n + 1)

# 초기 조건 설정
dp[0] = 1
dp[1] = 2

# 점화식에 따라 dp값 채우기
# dp[i] = dp[i - 1] * 2 + dp[i - 2] * 3 +
#         (dp[i - 3] + dp[i - 4] + dp[i - 5] + ... dp[0]) * 2
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % MOD
    for j in range(i - 3, -1, -1):
        dp[i] = (dp[i] + dp[j] * 2) % MOD

print(dp[n])