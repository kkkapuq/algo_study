n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    # x = 부모, y = 자식
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

arr = [0] * (n+1)
# 예제에서, 3->1, 1->2, 2->7 해서 3촌이다. 이 cnt 조건을 어떻게 할건가?
# a에서 시작해서 b를 만날때까지 계속 cnt를 쌓는다.
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            arr[i] = arr[v] + 1
            dfs(i)

dfs(a)
print(-1 if arr[b] == 0 else arr[b])