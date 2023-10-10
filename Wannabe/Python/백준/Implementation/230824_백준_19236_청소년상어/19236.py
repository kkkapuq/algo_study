import sys
from copy import deepcopy

input = sys.stdin.readline
"""
4x4 격자 - (r, c)
each 칸에 물고기 한마리 - 물고기의 번호는 1-16인데 제각각 다른번호임
방향은 8가지로 움직임 (상하좌우 대각선)
청소년상어 - (0, 0)에서 시작 (먼저 먹고 방향은 있던 물고기를 따라함)
물고기의 이동 - 작은 순서부터 이동하기 시작 - 한칸이동
가능한 이동 - 다른 물고기가 있거나(이럴땐 위치교환) , 빈칸
이동이 불가능한 경우 - 상어 혹은 격자바깥
이동이 가능할때까지 45도씩 회전하며 , 이후 한칸 이동 < 그래도 이동할 칸이 없다면> 이동하지 않음
상어가 이동 (물고기 이동이 끝나면)
 - 상어는 향한 방향기준 여러칸 이동 가능 , 이동경로의 물고기는 안먹고 도착지점의 물고기만 먹음
 - 빈칸으로는 이동이 불가능하다
 - 가능한 칸이 없으면 종료
물고기 이동(상어가 끝나면) , 상어이동 (물고기가 끝나면) - 반복
목표: 상어가 먹을수 있는 물고기 번호 합의 최대값
"""
'''
debugging 
- 물고기 kill_fish후 shark이동가능한 loc받는게 아니라
- loc을 다 받고 이동가능하다면 그 경우에 대해 기존 위치 -1로 업데이트(상어가 떠나고 남은 자리표시) 후 kill fish를 각 경우에 대해 해주는것이다.
- round함수는 종료할때 어떤 수도 반환하지 않는다. 우리는 최대값(전역변수)를 업데이트하는 것.
- deepcopy, copy 사용 
  - import copy -> copy.copy(원하는 객체)가 반환하는 걸 사용한다.
  - from copy import copy, deepcopy => deepcopy(obj)가 반환하는 걸 사용한다. 
'''
aqua = [[0] * 4 for _ in range(4)]
fish = [0] * 17
loc = dict()
for i in range(4):
    row = list(map(int, input().strip().split()))
    for j in range(4):
        aqua[i][j] = row[j * 2]  # aqua has only number of fish - shark:0  died: -1
        fish[row[j * 2]] = row[j * 2 + 1] - 1  # fish index points direction
        loc[row[j * 2]] = [i, j]  # 번호 - 위치 저장
# 0, 2, 4, .. < number of fish/ 1, 3, 5, .. < way fish head
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def get_next_locs(sx, sy, sway, aqua):
    # input: current x, y(row, column)
    # output: available location to move
    nexts = []
    for i in range(1, 5):
        nx, ny = sx + dir[sway][0] * i, sy + dir[sway][1] * i
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break
        if aqua[nx][ny] == -1:
            continue
        nexts.append((nx, ny))
    return nexts


def move_fish(aqua, loc, fish):
    for i in range(1, 17):
        if fish[i] == -1:
            continue
        fway = fish[i]
        fx, fy = loc[i]
        cw = fway
        for j in range(8):
            nway = (cw + j) % 8
            nx, ny = fx + dir[nway][0], fy + dir[nway][1]  # 현재 위치의 고유화(-1) 45도 반시계-> -1
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            if aqua[nx][ny] == 0:
                continue
            if aqua[nx][ny] == -1:
                aqua[nx][ny] = i
                aqua[fx][fy] = -1
                loc[i] = [nx, ny]
                fish[i] = nway
                break
            else:
                fish[i] = nway                             # 반시계방향으로 회전한 방향을 부여
                other = aqua[nx][ny]                       # 움직일 방향에 존재하는 물고기 번호
                loc[i], loc[other] = [nx, ny], [fx, fy]    # 번호에 따른 위치를 교환하는 연산
                aqua[nx][ny] = i                           # 위치에 따른 바뀐 번호를 할당하는 연산(기준 물고기)
                aqua[fx][fy] = other                       # 위치에 따른 번호를 할당 (상대 물고기 기준)
                break


def kill_fish(sx, sy, count, aqua, loc, fish):
    loc[0] = [sx, sy]  # 상어위치 입력 인자로 update
    fnum = aqua[sx][sy]  # sx, sy 위치의 물고기번호
    aqua[sx][sy] = 0  # 상어표시
    count += fnum  # 먹은 물고기 번호 합산
    fish[0] = fish[fnum]  # 상어방향 update(기존물고기방향으로)
    fish[fnum] = -1  # 물고기 제거표시
    return count


def round(sx, sy, count, aqua, fish, loc):
    global maxCnt
    move_fish(aqua, loc, fish)  # change aqua status

    locs = get_next_locs(sx, sy, fish[0], aqua)

    if not locs:
        maxCnt = max(count, maxCnt)
        return

    aqua[sx][sy] = -1           # there's no fish when shark leave for new grid
    for lx, ly in locs:
        aquacopy = deepcopy(aqua)
        loccopy = deepcopy(loc)
        fishcopy = deepcopy(fish)
        nxt = kill_fish(lx, ly, count, aquacopy, loccopy, fishcopy)
        round(lx, ly, nxt, aquacopy, fishcopy, loccopy)


if __name__ == "__main__":
    # 상어는 0번, 물고기 1-16번
    # 물고기 정보를 배열에 저장
    # 물고기가 먹히면 배열에서 제거
    maxCnt, count = 0, 0  # 답, 개수 초기화
    nxt = kill_fish(0, 0, count, aqua, loc, fish)

    round(0, 0, nxt, aqua, fish, loc)
    print(maxCnt)
