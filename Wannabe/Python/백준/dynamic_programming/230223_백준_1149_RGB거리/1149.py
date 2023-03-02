import sys
si = sys.stdin.readline

# 입력
n = int(si().strip())
colors = [list(map(int, si().strip().split())) for _ in range(n)]
# dp[i][j] => 0~i번째 집을 빨강(0), 초록(1), 파랑(2)으로 칠했을때 현재까지 든 비용 
dp = [[0, 0, 0] for _ in range(n)]    # dp초기화
dp[0] = colors[0]                     # dp초기화

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+colors[i][0]                #빨강으로 칠했을때는 전위치의 초록 파랑의 결과중 적은 경우에 현재 빨강 비용을 더한다
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+colors[i][1]                #초록으로 칠했을때는 전위치의 빨강 파랑의 결과중 적은 경우에 현재 초록 비용을 더한다
    dp[i][2] = min(dp[i-1][0], dp[i-1][1])+colors[i][2]                #파랑으로 칠했을때는 전위치의 빨강 초록의 결과중 적은 경우에 현재 파랑 비용을 더한다
    
print(min(dp[-1]))    # 마지막 위치에서의 최소값을 반환한다.