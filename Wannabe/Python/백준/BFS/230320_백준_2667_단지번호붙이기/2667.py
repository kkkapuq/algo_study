import sys
from collections import deque

si = sys.stdin.readline

N = int(si().strip())
grid = [list(map(int, list(si().strip()))) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visit = [[1] * N for _ in range(N)]
cities = []


def bfs(x, y):
    cnt = 0
    visit[x][y] = 0
    q = deque([(x, y)])
    while q:
        x1, y1 = q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x1 + dir[i][0], y1 + dir[i][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:    continue
            if visit[nx][ny] and grid[nx][ny] == 1:
                q.append((nx, ny))
                visit[nx][ny] = 0
    return cnt


for i in range(N):
    for j in range(N):
        if visit[i][j] and grid[i][j] == 1:
            num = bfs(i, j)
            cities.append(num)

print(len(cities))
print(*sorted(cities), sep='\n')
