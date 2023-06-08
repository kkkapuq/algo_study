n, m = map(int, input().split())
grid = [ [0 for _ in range(n+1)] for _ in range(n+1) ] 
# 북, 남, 동, 서 y, x값
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

for _ in range(m):
    r, c = map(int, input().split())
    grid[r][c] = 1
    cnt = 0
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if nx >= 0 and nx <= n and ny >= 0 and ny <= n and grid[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)
