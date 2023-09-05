'''
문제 : 단지 번호
링크 : https://www.acmicpc.net/problem/2667
소요시간 : 30분
'''
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
apart = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(r, c, cnt):
    graph[r][c] = 0
    if r < 0 or r >= n or c < 0 or c >= n:
        return
    
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        # 범위 밖은 탐색 제외
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 1:
            # 방문한 곳은 0으로 넣어서 방문처리
            graph[nx][ny] = 0
            cnt = dfs(nx, ny, cnt+1)
    return cnt
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            apart.append(dfs(i, j, 1))
            
apart.sort()
print(len(apart))
for i in apart:
    print(i)