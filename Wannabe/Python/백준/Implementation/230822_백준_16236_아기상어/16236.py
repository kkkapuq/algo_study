import sys
from collections import deque

"""
NxN 격자에
물고기 M마리, 아기상어 1마리
한칸에 물고기는 최대 한마리
아기상어의 크기 (초기: 2) / 물고기의 크기
아기상어의 이동 (1초에 상하좌우 1칸) / 자기보다 큰 물고기를 지나갈 수 없음 / 자기보다 작은 물고기만 먹을 수 있음
/같은 물고기는 먹을 수 없다 , 지나갈수는 있음
1. 물고기가 공간에 없다 2. 먹을수있는 물고기가 1마리 3. 먹을수있는 물고기가 1마리 이상
거리가 가장 가까운 물고기: 지나야하는 개수의 최소값(거리) 거리최소1순위-> 방향2순위(가장위, 가장 왼쪽)
이동 시간 1초, 먹는시간 없음 
물고기를 먹으면 빈칸처리
크기 1 증가 (자기와 같은 크기의 수의 물고기를 먹엇을 경우)
질문: 더이상 먹을수 없는 상황일때까지 몇초가 걸리는가
0: empty, 1-6: size of fish, 9: baby shark
"""

input = sys.stdin.readline
N = int(input().strip())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(x, y, visit):
    """
    아기상어 위치 (x, y)기준으로 가장 가까운 물고기를 탐색하는 메소드
    이동 경로 상의 물고기 상태 변화, 아기상어 상태 변화 (바깥에서)
    :param x: 행위치
    :param y: 열위치
    :return: loc, time (목적지 [(행, 열)], 시간)
    """
    visit[x][y] = 1
    q = deque([(x, y, 0)])
    loc = []
    while q:
        x0, y0, t = q.popleft()
        for i in range(4):
            x1, y1 = x0 + dir[i][0], y0 + dir[i][1]
            if x1 < 0 or x1 >= N or y1 < 0 or y1 >= N: continue
            if not visit[x1][y1]:
                if 0 < grid[x1][y1] < size:
                    loc.append((x1, y1, t + 1))
                    visit[x1][y1] = 1
                    continue
                if grid[x1][y1] == 0 or grid[x1][y1] == size:
                    q.append((x1, y1, t + 1))
                    visit[x1][y1] = 1
    return loc


def change_status(locs):
    global grid, size, eaten, answer
    locs = sorted(locs, key=lambda x: (x[2], x[0], x[1])) # 거리 행 열 (조건추가)
    # (무)지성 소트 (안먹히는 상황은 어떤 상황일까...)
    ## 구현이 안되는 경우가 있다.ㅇ . ㅇ
    ## 객체가 의미하는 게 잘 안보인당 -
    ## 코드가 복잡해지면 코드를 다 수정해야됨...
    x, y, t = locs[0]
    grid[x][y] = 0
    eaten += 1
    answer += t
    if size == eaten:
        size += 1
        eaten = 0
    return x, y


def find_shark():
    global grid
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                return i, j


if __name__ == "__main__":
    # 1. 시작 위치에서 먹을수있는 물고기 생길때까지 탐색
    # 먹고 grid상태 업데이트 - 물고기 및 아기상어 위치
    # 반복 (못먹을때까지)
    size, eaten = 2, 0
    answer = 0
    x0, y0 = find_shark()
    while True:
        visit = [[0] * N for _ in range(N)]
        loc = bfs(x0, y0, visit)
        if not loc:
            break
        grid[x0][y0] = 0
        x0, y0 = change_status(loc)
    print(answer)
