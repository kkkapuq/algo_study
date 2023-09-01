def dfs(v, graph, visited, isCut):
    cnt = 1
    visited[v] = True
    
    for i in graph[v]:
        # 방문한 적이 없고, a-b로 끊겨져 있는 선이 아니라면 탐색
        if not isCut[v][i] and not visited[i]:
            cnt += dfs(i, graph, visited, isCut)
    
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
        aCnt = dfs(a, graph, visited, isCut)
        bCnt = dfs(b, graph, visited, isCut)
        # 끊은거 복구
        isCut[a][b] = False
        answer = min(answer, abs(aCnt - bCnt))
    
    return answer