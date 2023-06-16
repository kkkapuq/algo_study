n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                # 두 격자가 겹치는 경우엔 무효 처리
                if i == k and abs(j - l) <= 2:
                    continue
                
                cnt1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                cnt2 = grid[k][l] + grid[k][l+1] + grid[k][l+2]
                answer = max(answer, cnt1+cnt2)

print(answer)