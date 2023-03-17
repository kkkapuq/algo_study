from collections import deque
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
grid = [list(si()) for _ in range(m)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
w, b = 0, 0
visit = [[1] * n for _ in range(m)]


def bfs(x, y, ch):
    visit[x][y] = 0
    q = deque([(x, y)])
    cnt = 1
    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            x2, y2 = x1 + dir[i][0], y1 + dir[i][1]
            if x2 < 0 or x2 >= m or y2 < 0 or y2 >= n:    continue
            if visit[x2][y2] and grid[x2][y2] == ch:
                visit[x2][y2] = 0
                q.append((x2, y2))
                cnt += 1
    return cnt


for i in range(m):
    for j in range(n):
        if grid[i][j] == 'W' and visit[i][j]:
            x = bfs(i, j, grid[i][j]) ** 2
            w += x
        elif grid[i][j] == 'B' and visit[i][j]:
            x = bfs(i, j, grid[i][j]) ** 2
            b += x

print(w, b)
