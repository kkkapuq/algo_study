import sys
from collections import deque
se = sys.stdin.readline
n, m, v = map(int, se().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, se().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# dfs
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
dfs(v)
# 사용한 visited 초기화
visited = [False] * (n+1)
print()

# bfs
def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        temp = q.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

bfs(v)
        