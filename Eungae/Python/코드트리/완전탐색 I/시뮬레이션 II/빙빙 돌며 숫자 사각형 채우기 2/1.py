# 1. 1 부터 n*m+1 만큼 for문을 돈다.
# 2. 방향좌표는 아래부터 시작한다. 남, 동, 북, 서 를 각각 0 1 2 3 으로 잡는다.
# 3. 격자를 0으로 다 채워주고, 방문하면 1로 만들어준다.
# 4. 방문하는 곳이 1이거나, 격자 끝의 좌표라면 방향을 틀어준다.

n, m = map(int, input().split())
# 남, 동, 북, 서 dxdy 값
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
cDir = 0
grid = [ [0 for _ in range(m)] for _ in range(n)]
r, c = 0, 0
grid[r][c] = 1

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for i in range(1, n*m):
    nx, ny = r + dx[cDir], c + dy[cDir]

    if inRange(nx, ny) and grid[nx][ny] == 0:
        r, c = r + dx[cDir], c + dy[cDir] 
        grid[r][c] = i+1
    else:
        cDir = (cDir + 1) % 4
        r, c = r + dx[cDir], c + dy[cDir] 
        grid[r][c] = i+1

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()