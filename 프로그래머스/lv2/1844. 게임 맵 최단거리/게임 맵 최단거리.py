from collections import deque

def solution(maps):
    answer = 0
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    n, m = len(maps), len(maps[0])
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 맵 외는 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # 벽이라면 무시
            if maps[nx][ny] == 0:
                continue
            
            # 처음 도달하는 곳이라면
            if maps[nx][ny] == 1:
                # 다음에 탐색하기 위해 q에 넣어주기
                q.append((nx, ny))
                # 내가 다음에 갈곳(nx, ny)는 현재 위치(x, y) 거리의 +1 해서 갱신해준다.
                maps[nx][ny] = maps[x][y] + 1
    answer = maps[n-1][m-1]
    
    
    return -1 if answer == 1 else answer