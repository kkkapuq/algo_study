from collections import deque

n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(map(int, input())))

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

# bfs
def bfs(r, c):
    global cnt
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr > n-1 or nc < 0 or nc > m-1:
                continue
            elif grid[nr][nc] != 1:
                continue
            else:
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
    
bfs(0, 0)
print(grid[n-1][m-1])