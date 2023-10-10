import sys
from collections import deque

# node 1~1000000개
"""
노드가 트리형태로 연결되어있으므로
루트부터 탐색이 가능한데
얼리어답터(EA)가 아닌 노드를 EA로 만들기 위해서는 
연결된 모든 노드가 EA여야 하므로
루트를 찾고, 루트가 EA일때와 그렇지 않을때 트리를 탐색하면서
EA인 부모를 가지면 자식은 EA체크하지 않고
EA가 아닌 부모를 가지면 자식은 EA체크하면서 EA수를 카운트해준다. 
"""
# input = sys.stdin.readline
# N = int(input().strip())
# edges = [[] for _ in range(N + 1)]
# for _ in range(N - 1):
#     a, b = tuple(map(int, input().strip().split()))
#     edges[a].append(b)
#     edges[b].append(a)
#
#
# # init node from 1 , ea is also array that checks node is ea or not
# def bfs(node, odd_ea=True):
#     q = deque([(node, 0)])
#     while q:
#         node, dis = q.popleft()
#         for adj in edges[node]:
#             if not visited[adj]:
#                 if odd_ea:
#                     if (dis + 1) % 2 != 0:
#                         ea[adj] = 1
#                 else:
#                     if (dis + 1) % 2 == 0:
#                         ea[adj] = 1
#                 visited[adj] = 1
#                 q.append((adj, dis + 1))
#     return sum([i for i in ea])
#
#
# answer = N
# ea = [0 for _ in range(N + 1)]
# visited = [0 for _ in range(N + 1)]
# visited[1] = 1
# answer = min(answer, bfs(1))
# ea = [0 for _ in range(N + 1)]
# visited = [0 for _ in range(N + 1)]
# ea[1], visited[1] = 1, 1
# answer = min(answer, bfs(1, False))
# print(answer)


"""
입력 받고 dfs탐색하면서 리프노드에서 함수종료후
dp 처리하는 방식으로 
dp처리: dp[node][0] -> 탐색중 node가 ea가 아닐때 leaf부터 현재까지 정해진 ea 최소값
       dp[node][1] -> 탐색중 node가 ea일때 leaf부터 현재까지 정해진 ea최소값
"""

input = sys.stdin.readline
N = int(input().strip())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = tuple(map(int, input().strip().split()))
    edges[a].append(b)
    edges[b].append(a)

dp = [[0, 0] for _ in range(N + 1)]
visited = [0] * (N + 1)


def dfs(node):
    for nxt in edges[node]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt)
            visited[nxt] = 0
            dp[node][1] += min(dp[nxt][1], dp[nxt][0])
            dp[node][0] += dp[nxt][1]
    dp[node][1] += 1


visited[1] = 1
dfs(1)

print(min(dp[1][0], dp[1][1]))
