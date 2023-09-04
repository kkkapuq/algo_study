n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

# dfs
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            global cnt
            cnt += 1
            dfs(i)
dfs(1)
print(cnt)