from collections import deque
from typing import List, tuple
import sys

si = sys.stdin.readline

N, M = map(int, si().strip().split())
grid = [list(map(int, si().strip().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
score = 0

def bfs(x, y, block):
    cnt, locs = 1, [(x, y, block)]
    q = deque([(x, y)])
    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            x2, y2 = x1+dir[i][0], y1+dir[i][1]
            if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N:
                continue
            if visit[x2][y2] and (grid[x2][y2] == block or grid[x2][y2] == 0):
                visit[x2][y2] = 0
                locs.append((x2, y2, grid[x2][y2]))
                q.append((x2, y2))
                cnt += 1
    locs = sorted(locs, key=lambda x: (x[2] != 0, x[0], x[1]))

    return cnt, (locs[0][0], locs[0][1]), locs

def arrange_group() -> List[tuple]:
    visit = [[1]*N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0 and grid[i][j] != -1:
                if visit[i][j]:
                    visit[i][j] = 0
                    # 블록수, 기준위치(튜플), 블록들좌표
                    r, base, locs = bfs(i, j, grid[i][j])
                    groups.append((r, base, locs))
    return groups
def remove():
    # get cnt**2 as score
    pass

def gravity():
    pass

def rotate_ccw():
    pass

