# design : 1. 중력에 의해 이동하는 특정위치의 정보
# 2. 완전탐색 - 4방향으로 기울여 각 경우에 대해 4방향으로 기울여 본다 반복
# 2-0(중요): 반복해보면서 되고 안되고를 봐야하므로 기울인다음에는 이전 상태를 복원해줘야한다.
# 2-1. 출구라면 둘다빠지는 경우와 파란색만 빠지는 경우에는 종료
# 2-2. 출구가 아니라면 파란색/빨간색은 겹치지 않음
# 2-3. 기울여가면서 나왔던 배치가 또 나오면 거기서는 더 탐색하지 않기로 한다.
import sys

sys.setrecursionlimit(int(1e4))

si = sys.stdin.readline

N, M = map(int, si().strip().split())
mxVal = max(M, N)
T = [list(si().strip()) for _ in range(N)]
ans = 11

BLOCK = 0
EXIT = 1
BLANK = 2
RED = 3
BLUE = 4


def exist(k):
    return any([k in row for row in T])


def blue_exists():
    return exist(BLUE)


def red_exists():
    return exist(RED)


def can_go(x, y):
    return T[x][y] == EXIT or T[x][y] == BLANK


def move(x, y, side):
    dirx, diry = [-1, 0, 1, 0], [0, 1, 0, -1]
    while True:
        nx, ny = x + dirx[side], y + diry[side]

        # if nx, ny cannot be located with bead, stop moving
        if not can_go(nx, ny):
            break
        # if it arrives exit pt, remove(replace num with blank)
        if T[nx][ny] == EXIT:
            T[x][y] = BLANK
            break

        # move bead
        T[nx][ny] = T[x][y]
        T[x][y] = BLANK

        x, y = nx, ny


def tilt(side):
    # 어떤 사탕부터 옮길 것인가 - 기울이는 방향에 따라 - 예를 들어 왼쪽이면 왼쪽에 있는 사탕부터 옮겨야 된다
    if side == 0 or side == 3:  # 북 아니면 서
        for i in range(N):
            for j in range(M):
                if T[i][j] == RED or T[i][j] == BLUE:
                    move(i, j, side)

    if side == 1 or side == 2:  # 동 아니면 남
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if T[i][j] == RED or T[i][j] == BLUE:
                    move(i, j, side)


def helper(cnt):
    global ans, T
    # 만약 파란구슬이 지도에 존재하지 않는다면
    if not blue_exists():
        return  # 탐색할 가치없음
    # if cnt is greater than 10,
    if cnt >= 10:
        return  # no need to search further
    # if red bead does not exist, then we update the ans
    if not red_exists():
        ans = min(ans, cnt)
        return

    for i in range(4):  # 0:북 1:동 2:남 3:서
        tempT = [row[:] for row in T]
        tilt(i)
        helper(cnt + 1)  # 기울인 결과에서 또 다른 기울기를 탐색음
        T = tempT  # 돌아왔다면 원래대로 돌려놓


def chrToNum(ch):
    if ch == '#':
        return BLOCK
    elif ch == 'O':
        return EXIT
    elif ch == '.':
        return BLANK
    elif ch == 'R':
        return RED
    elif ch == 'B':
        return BLUE


if __name__ == "__main__":
    T = [list(map(chrToNum, row)) for row in T]
    helper(0)

    if ans == 11:
        print(-1)
    else:
        print(ans)