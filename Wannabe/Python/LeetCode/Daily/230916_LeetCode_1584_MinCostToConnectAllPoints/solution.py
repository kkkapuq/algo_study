from collections import deque
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        max_x, max_y = 0, 0
        for x, y in points:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        m, n = max_x, max_y

        pts = set(map(tuple, points))
        visit = [[0] * n for _ in range(m)]
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        total_dist = 0

        def bfs(r, c, visit):
            nonlocal pts
            q = deque([(r, c, 0)])
            visit[r][c] = 0
            while q:
                r0, c0, d = q.popleft()
                if (r0, c0) in pts:
                    pts.remove((r0, c0))
                    return r0, c0, d
                for i in range(4):
                    nr, nc = r0 + dir[i][0], c0 + dir[i][1]
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if visit[nr][nc]:
                        visit[nr][nc] = 0
                        q.append((nr, nc, d + 1))

        def helper(x, y):
            nonlocal pts, total_dist
            if (x, y) != tuple(points[0]) and (x, y) not in pts:
                return

            visit = [[1] * n for _ in range(m)]
            nx, ny, d = bfs(x, y, visit)
            total_dist += d

            helper(nx, ny)

        pts.remove(tuple(points[0]))
        helper(*points[0])

        return total_dist

print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))