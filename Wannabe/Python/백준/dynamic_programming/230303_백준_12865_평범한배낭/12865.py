# n, k 물건의 개수, k까지 넣을수 있는 가방
# n줄에 거쳐 해당 무게와 가치 (w v) 형태로 주어짐 (weight에 저장)
# 설계: dp[i][j] => 제한이 j일때 i번 물체까지 넣을수 있다면 최대가치
# 점화식: dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i][0]]+weight[i][1]
import sys
si = sys.stdin.readline

n, k = map(int, si().split())
weights = [list(map(int, si().split())) for _ in range(n)]


dp = [[0]*(k+1) for _ in range(n)]
for i in range(1, k+1):
    dp[0][i] = weights[0][1] if i >= weights[0][0] else 0 
for i in range(1, n):
    for j in range(1, k+1):
        if j >= weights[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i][0]]+weights[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n-1][k])