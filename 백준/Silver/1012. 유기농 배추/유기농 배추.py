'''
문제 : 유기농 배추
링크 : https://www.acmicpc.net/problem/1012
소요시간 : 13:40~
'''
import sys
sys.setrecursionlimit(10000)
t = int(input())
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

for tc in range(t):
    m, n, k = map(int, input().split())

    graph = [[0 for _ in range(m)] for __ in range(n)]

    def dfs(r, c):
        # 방문처리 (visited 안쓰기)
        graph[r][c] = 0
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]

            # 범위 밖 제외
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if graph[nr][nc] == 0:
                continue

            if graph[nr][nc] == 1:
                dfs(nr, nc)

    for _ in range(k):
        c, r = map(int, input().split())
        graph[r][c] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1
    print(answer)