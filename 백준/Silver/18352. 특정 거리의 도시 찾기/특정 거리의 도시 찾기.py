'''
문제 : 특정 거리의 도시 찾기
링크 : https://www.acmicpc.net/problem/18352
소요시간 : 12:02~
'''
import sys
from collections import deque
se = sys.stdin.readline

# n = 도시 갯수, m = 도로 갯수, k = 거리 정보, x = 출발 도시 번호
n, m, k, x = map(int, se().split())
graph = [[] for _ in range(n+1)]

# 그래프 셋팅
for i in range(m):
    a, b = map(int, se().split())
    graph[a].append(b)
    # 이거 있으면 안된다, 양방향 그래프가 아님!!!
    # graph[b].append(a)

def bfs(v):
    answer = []
    
    q = deque([v])
    # 각 도시별 거리를 저장
    distance = [0] * (n+1)
    visited = [False] * (n+1)
    # 방문처리
    visited[v] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                # 방문한 도시까지의 거리를 저장
                distance[i] = distance[x] + 1

                if distance[i] == k:
                    answer.append(i)

    # x번째 도시 출발, k거리에 있는 도시를 모두 찾기, 오름차순으로 정렬
    if not answer:
        print(-1)
    else:
        answer.sort()
        print('\n'.join(map(str, answer)))

bfs(x)