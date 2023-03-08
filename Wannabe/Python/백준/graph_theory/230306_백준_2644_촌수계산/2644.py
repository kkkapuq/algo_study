import sys

sys.setrecursionlimit(int(1e6))
si = sys.stdin.readline

n = int(si().strip())
g = [[0] * (n + 1) for _ in range(n + 1)]
n1, n2 = map(int, si().strip().split())
k = int(si().strip())
for _ in range(k):
    c1, c2 = map(int, si().strip().split())
    g[c1][c2] = 1
    g[c2][c1] = 1
visit = [0] * (n + 1)


def dfs(s, dist):
    global n1, n2, visit
    for i in range(1, n + 1):
        if g[s][i] and not visit[i]:
            if i == n2:
                return dist+1
            visit[i] = 1
            ks = dfs(i, dist + 1)
            if ks != -1:
                return ks
    return -1


visit[n1] = 1
ret = dfs(n1, 0)
if ret == -1:
    print(-1)
else:
    print(ret)