'''
문제 : 안전 영역
링크 : https://www.acmicpc.net/problem/2468
소요시간 : 13:45
'''
import sys
import copy
se = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, se().split())))

# min부터 max까지 케이스별로 dfs를 돌려본다.
minH, maxH = 101, 0

# min과 max 탐색
for i in graph:
    for j in i:
        minH = min(minH, j)
        maxH = max(maxH, j)

answer = 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(r, c, temp):
    # 방문처리
    temp[r][c] = 0
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if temp[nx][ny] == 0:
            continue
        else:
            dfs(nx, ny, temp)

for i in range(maxH+1):
    # 그래프 복사
    temp = copy.deepcopy(graph)
    # i 이하인 지역은 다 0으로 만들기
    for j in range(n):
        for k in range(n):
            if graph[j][k] <= i:
                temp[j][k] = 0

    # 해당 케이스에서 나올 수 있는 영역의 수
    cnt = 0
    for j in range(n):
        for k in range(n):
            if temp[j][k] != 0:
                cnt += 1
                dfs(j, k, temp)
    answer = max(answer, cnt)

print(answer)