import math
from collections import deque
from pprint import pprint
import sys

si = sys.stdin.readline
N, M = map(int, si().strip().split())
grid = [list(map(int, si().strip().split())) for _ in range(N)]
visit = [[1] * N for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
score = 0


def bfs(x, y, block):
    rlocs = []
    cnt, rainbow, locs = 1, 0, [(x, y, block)]
    q = deque([(x, y)])
    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            x2, y2 = x1 + dir[i][0], y1 + dir[i][1]
            if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N:
                continue
            if visit[x2][y2] and (grid[x2][y2] == block or grid[x2][y2] == 0):
                visit[x2][y2] = 0
                if grid[x2][y2] == 0:
                    rainbow += 1
                    rlocs.append((x2, y2))
                locs.append((x2, y2, grid[x2][y2]))
                q.append((x2, y2))
                cnt += 1

    return cnt, rainbow, rlocs, locs


def arrange_group():
    global visit
    visit = [[1] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0 and grid[i][j] != -1 and grid[i][j] != -99:
                if visit[i][j]:
                    visit[i][j] = 0
                    r, zeros, rds, locs = bfs(i, j, grid[i][j])
                    if r > 1:
                        groups.append((r, zeros, locs))
                    for k, l in rds:
                        visit[k][l] = 1
    return groups


def remove(locs):
    for i, j, v in locs:
        grid[i][j] = -99


def gravity():
    for i in range(N):
        j = N - 1
        while True:
            while j > 0:
                if grid[j][i] == -99:
                    break
                j -= 1
            k = j - 1
            while k >= 0:
                if grid[k][i] == -1:
                    j = k
                    break
                if grid[k][i] != -99 and grid[k][i] != -1:
                    grid[k][i], grid[j][i] = grid[j][i], grid[k][i]
                    break
                k -= 1
            if j == 0 or k == -1:
                break
            j -= 1


def rotate_ccw():
    r = math.ceil(N / 2)
    for i in range(r):
        for j in range(N // 2):
            temp = grid[i][j]
            grid[i][j] = grid[j][N - 1 - i]
            grid[j][N - 1 - i] = grid[N - 1 - i][N - 1 - j]
            grid[N - 1 - i][N - 1 - j] = grid[N - 1 - j][i]
            grid[N - 1 - j][i] = temp


while True:
    groups = arrange_group()
    if not groups:
        break
    groups = sorted(groups, key=lambda x: (x[0], x[1], x[2][0][0], x[2][0][1]), reverse=True)
    cnt, zeros, locs = groups[0]
    remove(locs)
    pprint('removed.')
    pprint(grid)
    score += cnt ** 2
    gravity()
    print('gravitated.')
    pprint(grid)
    rotate_ccw()
    print('rotated.')
    pprint(grid)
    gravity()
    print('gravitated.')
    pprint(grid)

print(score)
"""793
6 3
1 1 1 0 0 0
1 1 1 0 0 0
1 1 3 0 0 0
0 0 0 2 2 2
0 0 0 2 2 2
0 0 0 2 2 2
"""
"""74
5 3
0 0 0 0 1
-1 -1 0 -1 0
-1 -1 3 -1 -1
-1 -1 0 -1 -1
0 0 2 0 0
"""
"""58
5 4
1 0 -1 0 0
2 0 -1 0 0
3 0 -1 0 0
4 0 -1 -1 -1
4 4 1 1 1
"""