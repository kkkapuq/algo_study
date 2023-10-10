import sys
from collections import deque

input = sys.stdin.readline

""" 오답 코드 - 중간에 많이 꺾어가는 경로대비 적게 꺾어도 같은 목적지에 도달가능
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 987654321
c, r = tuple(map(int, input().strip().split()))
grid = [list(input().strip()) for _ in range(r)]

# 1. C의 위치를 찾는다(두개 존재)
# 2. 하나의 위치에서 탐색을 시작하는데
# 3. * 만나면 탐색불가능
# 4. 이전 진행경로를 저장 (0~3: 북동남서)
# 5. 꺾인 경로를 저장
# 6. 다른 C에 도달할시 꺾인 경로의 수 업데이트
visited = [[0] * c for _ in range(r)]


def bfs(x, y):
    global answer, visited
    visited[x][y] = 1
    # rindex, cindex, prev_dir(-1: initial), cnt
    q = deque([(x, y, -1, 0)])
    while q:
        x0, y0, prev_dir, cnt = q.popleft()
        if (x0, y0) != pt[0] and grid[x0][y0] == 'C':
            answer = min(answer, cnt)
        for i in range(4):
            nx, ny = x0 + dir[i][0], y0 + dir[i][1]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if grid[nx][ny] == '*':
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                if prev_dir != i and prev_dir != -1:
                    q.append((nx, ny, i, cnt + 1))
                else:
                    q.append((nx, ny, i, cnt))
                visited


pt = []
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'C':
            pt.append((i, j))

bfs(*pt[0])
print(answer-1)
"""
W, H = tuple(map(int, input().strip().split()))
grid = [list(input().strip()) for _ in range(H)]
matrix = [[float('inf')] * W for _ in range(H)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# find loc C
def get_init():
    cloc = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'C':
                cloc.append(i)
                cloc.append(j)
    return cloc


# bfs in straight way - 경로에 상관없이 최소사용횟수가 적은쪽으로 업데이트
def bfs(x, y, fx, fy):
    matrix[x][y] = 0
    q = deque([(x, y, -1)])  # time:mirror used
    while q:
        cx, cy, time = q.popleft()
        if cx == fx and cy == fy:
            return time
        for i in range(4):
            k = 1
            while True:
                nx, ny = cx + dir[i][0] * k, cy + dir[i][1] * k
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    break
                if grid[nx][ny] == "*":
                    break
                if matrix[nx][ny] > time + 1:
                    matrix[nx][ny] = time + 1
                    q.append((nx, ny, time + 1))
                k += 1


starts = get_init()
answer = bfs(*starts)
print(answer)
