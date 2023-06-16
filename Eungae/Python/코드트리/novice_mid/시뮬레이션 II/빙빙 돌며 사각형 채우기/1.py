# 1. A부터 시작한다.
# 2. A~Z 까지 배열을 만들고, 뭘 넣을지는 % len(list) 해서 결정한다.
# 3. 동-남-서-북 순으로 0, 1, 2, 3 방향좌표를 설정해준다.

n, m = map(int, input().split())
# 남, 동, 북, 서 dxdy 값
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cDir = 0
grid = [ [0 for _ in range(m)] for _ in range(n)]
r, c = 0, 0
grid[r][c] = 'A'
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for i in range(1, n*m):
    nx, ny = r + dx[cDir], c + dy[cDir]

    if inRange(nx, ny) and grid[nx][ny] == 0:
        r, c = r + dx[cDir], c + dy[cDir] 
        grid[r][c] = alphabet[i%len(alphabet)]
    else:
        cDir = (cDir + 1) % 4
        r, c = r + dx[cDir], c + dy[cDir] 
        grid[r][c] = alphabet[i%len(alphabet)]

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()