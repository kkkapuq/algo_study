# 입력
N, M, K = map(int, input().split())

graph = [ [0 for _  in range(N+1)] for __ in range(N+1) ]

for i in range(1, N+1):
    graph[i][1:] = list(map(int, input().split()))

# 참가자들 정보
r = [ 0 for _ in range(M+1) ]
c = [ 0 for _ in range(M+1) ]
is_escape = [ False for _ in range(M+1) ]
# 참가자가 이동한 거리
dist = [ 0 for _ in range(M+1) ]
# 출구 좌표
out_r = 0
out_c = 0

for i in range(1, M+1):
    tr, tc = map(int, input().split())
    r[i] = tr
    c[i] = tc

out_r, out_c = map(int, input().split())
turn = 0

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
# 가장 작은 정사각형을 구한다, 각각 좌상단 좌표와 우하단 좌표
square_lr = 0
square_lc = 0
square_rr = 0
square_rc = 0
# 회전의 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의해줍니다.
next_board = [
    [0] * (N + 1) for _ in range(N + 1)
]


def check_escape():
    global is_escape
    for i in range(1, len(is_escape)):
        if not is_escape[i]:
            return False
    return True

def get_distance_to_out(r, c):
    global out_r, out_c
    return abs(r - out_r) + abs(c - out_c)

def move_available(user):
    global r, c, dist, graph
    flag = -1
    closest = get_distance_to_out(r[user], c[user])
    for dir in range(4):
        nr = r[user] + dr[dir]
        nc = c[user] + dc[dir]

        # 맵을 벗어난다면 움직이지 않는다.
        if nr < 1 or nr > N or nc < 1 or nc > N:
            continue
        # 벽이 있다면 해당 방향으로 움직일 수 없다.
        if graph[nr][nc] != 0:
            continue
        
        # 현재 거리에서 더 가까워질 수 없다면 움직이지 않는다.
        distance = get_distance_to_out(nr, nc)
        if closest <= distance:
            continue

        # 위 조건들을 통과한다면 해당 방향으로 이동이 가능하다는 의미이므로, 플래그값 갱신
        flag = dir
        break
    return flag

def move_users():
    global r, c, dist
    for user in range(1, M+1):
        # 특정 방향으로 이동할 수 있다면, 이동시켜준다.
        dir = move_available(user)
        if dir != -1:
            r[user] += dr[dir]
            c[user] += dc[dir]
            # 유저가 이동한 거리를 더해준다.
            dist[user] += 1

            # 만약 이동한곳이 탈출구라면 탈출 처리를 해준다.
            if r[user] == out_r and c[user] == out_c:
                is_escape[user] = True

def check_square():
    global graph, square_lc, square_lr, square_rc, square_rr

    for size in range(2, N+1):
        for tr in range(1, N-size+2):
            # 이번 사각형에서 최소 1명의 유저와 탈출구를 포함하는지 여부 확인
            is_user, is_out = False, False
            for tc in range(1, N-size+2):
                square_lr = tr
                square_lc = tc
                square_rr = square_lr + size - 1
                square_rc = square_lc + size - 1

                # 출구가 없으면 다음 사각형 찾기
                if not (out_r >= square_lr and out_r <= square_rr and out_c >= square_lc and out_c <= square_rc):
                    continue

                is_out = True

                # 사각형 안에 참가자가 존재하는지 확인
                for user in range(1, M+1):
                    if is_escape[user]:
                        continue
                    if (r[user] >= square_lr and r[user] <= square_rr and c[user] >= square_lc and c[user] <= square_rc):
                        is_user = True
                        break
                
                if is_user and is_out:
                    return
                
def rotate_square():
    global graph
    size = square_rc - square_lc + 1
    # 회전하는 구간... 로직이 이해가 잘 안감
    for r in range(square_lr, square_rr + 1):
        for c in range(square_lc, square_rc + 1):
            tr, tc = r - square_lr, c - square_lc
            rr, rc = tc, size - tr - 1
            next_board[rr + square_lr][rc + square_lc] = graph[r][c]

    # next_board를 현재 graph에 옮겨주는 작업
    for r in range(square_lr, square_rr + 1):
        for c in range(square_lc, square_rc + 1):
            graph[r][c] = next_board[r][c]
            # 회전하면서 내구도 감소 시켜주기
            if graph[r][c] > 0:
                graph[r][c] -= 1

def rotate_user_and_exit():
    global r, c, out_r, out_c
    # 참가자가 정사각형 안에 있다면 회전시켜준다.
    size = square_rc - square_lc + 1
    for user in range(1, M+1):
        tx, ty = r[user], c[user]
        # 해당 참가자가 정사각형 범주 내라면 회전
        if square_lr <= tx and tx <= square_rr and square_lc <= ty and ty <= square_rc:
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
            ox, oy = tx - square_lr, ty - square_lc
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            r[user] = rx + square_lr
            c[user] = ry + square_lc
    
    if square_lr <= out_r and out_r <= square_rr and square_lc <= out_c and out_c <= square_rc:
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
            ox, oy = out_r - square_lr, out_c - square_lc
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            out_r = rx + square_lr
            out_c = ry + square_lc


for turn in range(K):
    if check_escape():
        break
    turn += 1
    # 모든 참가자들을 한 번에 이동시킨다. 이 때, 출구와 가까워질 수 없다면 이동시키지 않음
    move_users()
    if check_escape():
        break
    # 가장 작은 사각형을 구한다.
    check_square()
    # 벽들을 회전시키고 내구도를 소모한다.
    rotate_square()
    # 유저와 탈출구를 회전시킨다
    rotate_user_and_exit()

answer = sum(dist[1:])
print(answer)
print(out_r, end=" ")
print(out_c)