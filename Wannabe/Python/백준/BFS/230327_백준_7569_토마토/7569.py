import sys
from collections import deque

si = sys.stdin.readline
dir = [(0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (-1, 0, 0), (1, 0, 0)]

n, m, h = map(int, si().strip().split())
grid = []
n_app = 0
day = 0
latest_active = deque([])


def bfs():
    global n_app, day
    while latest_active:
        for _ in range(len(latest_active)):
            t, r, c = latest_active.popleft()
            for u in range(6):
                nt, nr, nc = t + dir[u][0], r + dir[u][1], c + dir[u][2]
                if nt < 0 or nt >= h or nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if grid[nt][nr][nc] == 0:
                    latest_active.append((nt, nr, nc))
                    grid[nt][nr][nc] = 1
                    n_app -= 1
                    if n_app == 0:
                        day += 1
                        return
        day += 1


for i in range(h):
    area = []
    for j in range(m):
        line = list(map(int, si().strip().split()))
        for k in range(n):
            if line[k] == 0:
                n_app += 1
            elif line[k] == 1:
                latest_active.append((i, j, k))
        area.append(line)
    grid.append(area)

if latest_active and n_app:
    bfs()

if n_app > 0:
    print(-1)
elif n_app == 0 and day == 0:
    print(0)
else:
    print(day)