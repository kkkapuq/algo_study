import sys
si = sys.stdin.readline



def dfs(prev, node):
    visited[node] = True
    for n in edges[node]:
        if n == prev:            # 이전 노드를 돌아가는건 무시
            continue
        if visited[n]:           # 이전 노드가 아닌 다른 노드를 가는데 이미 간곳을 간다면 사이클
            return False
        if not dfs(node, n):
            return False
    return True

tc = 0
while True:
    tc += 1
    n, m = map(int, si().strip().split())
    if [n, m] == [0, 0]:
        exit()
    visited = [False] * (n + 1)
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, si().strip().split())
        edges[a].append(b)
        edges[b].append(a)
    ans = 0        
    for i in range(1, n+1):
        if not visited[i]:
            if dfs(0, i):
                ans += 1
    if ans == 0:
        print(f"Case {tc}: No trees.")
    elif ans == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: A forest of {ans} trees.")
