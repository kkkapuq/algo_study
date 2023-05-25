n, m = map(int, input().split())
strings = [list(input()) for _ in range(n)]
cnt = 0

# 방향배열
dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]
for i in range(n):
    for j in range(m):
        if strings[i][j] == 'L':
            for dx, dy in zip(dxs, dys):
                curt = 1
                curx = i
                cury = j
                while True:
                    nx = curx + dx
                    ny = cury + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    if  strings[nx][ny] != 'E':
                        break
                    curt += 1
                    curx = nx
                    cury = ny
                
                if curt >= 3:
                    cnt += 1

print(cnt)