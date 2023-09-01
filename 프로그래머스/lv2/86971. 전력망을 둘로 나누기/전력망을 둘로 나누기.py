'''
문제 : 전력망을 둘로 나누기
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/86971
'''
from collections import deque
def bfs(start, graph, visited, isCut):
    cnt = 1
    visited[start] = True
    
    q = deque([start])
    while q:
        v = q.popleft()

        for i in graph[v]:
            if not isCut[v][i] and not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

def solution(n, wires):
    answer = 100
    
    # 해당 줄이 끊어졌는지 체크하는 리스트
    isCut = [[False] * (n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [False] * (n+1)
        
        # a - b 송전탑 끊기
        isCut[a][b] = True
        aCnt = bfs(a, graph, visited, isCut)
        bCnt = bfs(b, graph, visited, isCut)
        # 끊은거 복구
        isCut[a][b] = False
        answer = min(answer, abs(aCnt - bCnt))
    
    return answer