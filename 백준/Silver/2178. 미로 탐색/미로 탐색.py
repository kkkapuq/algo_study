from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(r, c):
    q = deque([(r, c)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어날 경우 제외
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            # 벽인 경우 제외
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

bfs(0, 0)
print(graph[-1][-1])