import sys
from collections import deque

si = sys.stdin.readline
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(si().strip())


def bfs(i, j):
    global visit, N, M, grid
    q = deque([(i, j)])
    visit[i][j] = 0
    while q:
        i1, j1 = q.popleft()
        for k in range(4):
            ni, nj = i1 + dir[k][0], j1 + dir[k][1]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if visit[ni][nj] and grid[ni][nj] == 1:
                visit[ni][nj] = 0
                q.append((ni, nj))


for i in range(T):
    cnt = 0
    M, N, K = map(int, si().strip().split())
    grid = [[0] * M for _ in range(N)]
    visit = [[1] * M for _ in range(N)]
    for _ in range(K):
        k, j = map(int, si().strip().split())
        grid[j][k] = 1
    for j in range(N):
        for k in range(M):
            if grid[j][k] == 1 and visit[j][k]:
                bfs(j, k)
                cnt += 1
    print(cnt)
