'''
1. dfs로 걍 풀면될듯..?
2. 예제 1에선 2랑 5가 각각 (1, 5), (2, 1) 이랑 연결되어있으므로 두개, 양 끝이 연결된 친구를 찾으면된다.
3. bfs로도 풀어보기
'''

import sys
sys.setrecursionlimit(10000)
from collections import deque

# dfs, bfs 처리에 필요한 친구들 생성
count = 0
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# dfs 도는 함수
def dfs(start):
    # 해당 노드 방문처리
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# bfs 도는 함수



# 방문처리 리스트
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 탐색
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)