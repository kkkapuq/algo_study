'''
문제 : 영역 구하기
링크 : https://www.acmicpc.net/problem/2583
소요시간 : 40분
'''
import sys
sys.setrecursionlimit(10000)
se = sys.stdin.readline

# n = 가로, m = 세로, k = 직사각형 수
m, n, k = map(int, se().split())
graph = [[0 for j in range(n)] for _ in range(m)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(r, c, cnt):
    # 방문처리
    graph[r][c] = 1
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 1:
            continue
        if graph[nx][ny] == 0:
            cnt = dfs(nx, ny, cnt)
    return cnt + 1

for _ in range(k):
    x1, y1, x2, y2 = map(int, se().split())
    # 이렇게 하면 모양이 상하 반전이 됨. 이 문제에선 무관할듯..?
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

    # 모양 그대로 유지하고 싶다면 이렇게
    # for i in range(m - y2, m - y1):
    #     for j in range(x1, x2):
    #         graph[i][j] = 1

sizes = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            sizes.append(dfs(i, j, 0))

sizes.sort()
print(len(sizes))
print(' '.join(map(str, sizes)))