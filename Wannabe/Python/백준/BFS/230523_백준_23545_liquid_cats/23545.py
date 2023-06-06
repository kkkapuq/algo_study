import sys
from collections import deque

si = sys.stdin.readline

N, M, K = map(int, si().strip().split())
grid = [list(si().strip()) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW


def bfs(x, y, threshold):
    ret = x
    occupied = 1
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        if occupied == K:
            ret = min(cx, ret)
        for i in range(4):
            nx, ny = cx + dir[i][0], cy + dir[i][1]
            if nx < 0 or nx >= N or nx <= threshold or ny < 0 or ny >= M: continue
            if visit[nx][ny] and grid[nx][ny] == '.' and occupied < K:
                q.append((nx, ny))
                visit[nx][ny] = 0
                occupied += 1
    if occupied < K:
        return -1
    else:
        return ret


if __name__ == "__main__":
    ans = -1
    threshold = 0
    while threshold < N:
        visit = [[1] * M for _ in range(N)]
        for i in range(N-1, N-1-(threshold+1), -1):
            for j in range(M):
                if visit[i][j] and grid[i][j] == '.':
                    visit[i][j] = 0
                    height = bfs(i, j, N-1-(threshold+1))
                    if height != -1:
                        ans = max(ans, height)

        print(*visit, sep="\n")
        print("-"*10)
        if ans != -1:
            break
        threshold += 1
    if ans != -1:
        print(ans + 1)
    else:
        print(ans)