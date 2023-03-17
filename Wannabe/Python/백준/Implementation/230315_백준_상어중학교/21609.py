import math
from collections import deque
from typing import List, Tuple
from pprint import pprint
import sys

si = sys.stdin.readline

N, M = map(int, si().strip().split())
grid = [list(map(int, si().strip().split())) for _ in range(N)]
visit = [[1]*N for _ in range(N)]
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

def arrange_group() -> List[Tuple]:
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
def remove(locs):
    # get cnt**2 as score
    for i, j in locs:
        grid[i][j] = None

def gravity():
    for i in range(N):
        j = N-1
        # from bottom, skip nonzero/minus one, locate first zero as fixed index (k) after which nonzero number will replace
        while True:
            while j > 0:
                if grid[j][i] == 0:
                    break
                j -= 1
            k = j-1
            while k >= 0:
                if grid[k][i] == -1:
                    j = k
                    break
                if grid[k][i] != 0 and grid[k][i] != -1:
                    grid[k][i], grid[j][i] = grid[j][i], grid[k][i]
                    break
                k -= 1
            if j == 0 or k == -1:
                break
            j -= 1

def rotate_ccw():
    r = math.ceil(N/2)
    for i in range(r):
        for j in range(N//2):
            temp = grid[i][j]
            grid[i][j] = grid[j][N-1-i]
            grid[j][N-1-i] = grid[N-1-i][N-1-j]
            grid[N-1-i][N-1-j] = grid[N-1-j][i]
            grid[N-1-j][i] = temp

while True:
    groups = arrange_group()
    cnt, base, locs = groups[0]
    score += cnt**2
    remove(locs)