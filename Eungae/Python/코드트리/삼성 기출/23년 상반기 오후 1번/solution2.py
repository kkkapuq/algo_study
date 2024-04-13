N, M, K = map(int, input().split())

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

user_position = [ (0, 0) for _ in range(M+1) ]
out_position = (0, 0)
board = [ [0 for _ in range(N+1)] for __ in range(N+1) ]
next_board = [ [0 for _ in range(N+1)] for __ in range(N+1) ]
dist = [ 0 for _ in range(M+1)]
is_escape = [ False for _ in range(M+1) ]

# 가장 작은 사각형의 좌상단 좌표와 크기
sr, sc, ssize = 0, 0, 0

# 맵 입력
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    board[i][1:] = temp
    next_board[i][1:] = temp

# 유저 위치 입력
for i in range(1, M+1):
    temp = tuple(map(int, input().split()))
    user_position[i] = temp

out_position = tuple(map(int, input().split()))

def check_escape():
    global is_escape
    for i in range(1, M+1):
        # 살아있는 사람이 한명이라도 있다면 False
        if not is_escape[i]:
            return False
    return True

def get_distance_to_out(r, c):
    global user_position, out_position
    out_r, out_c = out_position[0], out_position[1]
    return abs(r - out_r) + abs(c - out_c)

def move_available(user):
    global user_position, out_position
    dir = -1

    r, c = user_position[user]
    closest = get_distance_to_out(r, c)

    # 상하좌우로 탐색해서 가까워질 수 있는지 체크한다.
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        distance = get_distance_to_out(nr, nc)

        # 범위 밖이거나 벽은 패스한다.
        if nr < 1 or nr > N or nc < 1 or nc > N or board[nr][nc] > 0:
            continue
        
        # 가까워질 수 없다면 패스한다.
        if closest <= distance:
            continue
        else:
            dir = i
            break
    return dir


def move_users():
    global user_position, board, out_position
    
    for user in range(1, M+1):
        # 이미 탈출한 유저는 패스한다.
        if is_escape[user]:
            continue
        # 어느쪽으로 움직일 지 정한다, dir이 -1이면 출구와 가까워질 수 없으므로 움직이지 않는다.
        dir = move_available(user)
        if dir == -1:
            continue
        r, c = user_position[user]
        nr, nc = r + dr[dir], c + dc[dir]
        user_position[user] = (nr, nc)
        dist[user] += 1

        # 탈출했다면 탈출자 리스트에 넣어주기
        out_r, out_c = out_position
        if out_r == nr and out_c == nc:
            is_escape[user] = True

def check_square():
    global user_position, out_position, board, sr, sc, ssize
    out_r, out_c = out_position
    for size in range(2, N+1):
        for r in range(1, N - size + 2):
            for c in range(1, N - size + 2):
                # 출구가 존재하지 않으면 패스
                if not (r <= out_r and out_r < r + size and c <= out_c and out_c < c + size):
                    continue

                # 유저가 존재하는지 체크
                for user in range(1, M+1):
                    if is_escape[user]:
                        continue
                    user_r, user_c = user_position[user]
                    # 유저가 한명이라도 존재한다면 위치 갱신시켜주고 return
                    if r <= user_r and user_r < r + size and c <= user_c and user_c < c + size:
                        sr, sc, ssize = r, c, size
                        return
                    
def rotate_square():
    global board, next_board, sr, sc, ssize, out_position
    is_moved = [ False for _ in range(M+1) ]
    out_moved = False
    # 벽 회전
    for r in range(ssize):
        for c in range(ssize):
            nr, nc = sr + c, sc + ssize - r - 1
            next_board[nr][nc] = board[sr+r][sc+c]
            # 회전하면서 내구도 소모
            if next_board[nr][nc] > 0:
                next_board[nr][nc] -= 1
            # 유저 위치와 탈출구도 회전
            for user in range(1, M+1):
                # 이미 탈출하거나 본 회전에서 회전된 유저는 건들지 않는다.
                if is_escape[user] or is_moved[user]:
                    continue
                user_r, user_c = user_position[user]
                # 만약 돌리는 위치에 유저가 포함되어 있다면 돌려준다.
                if user_r == sr+r and user_c == sc+c:
                    user_position[user] = (nr, nc)
                    is_moved[user] = True
            # 탈출구를 회전시켜준다. 
            out_r, out_c = out_position
            if out_r == sr+r and out_c == sc+c and not out_moved:
                out_position = (nr, nc)
                out_moved = True
    
    # 회전하고나서 board를 갱신해준다.
    for r in range(sr, sr + ssize):
        for c in range(sc, sc + ssize):
            board[r][c] = next_board[r][c]
    
    

for turn in range(1, K+1):
    # 살아있는 유저가 있다면 이동시키기
    if check_escape():
        break
    move_users()
    if check_escape():
        break
    # 정사각형 크기 구하기
    check_square()
    # 정사각형 회전시켜주기
    rotate_square()

print(sum(dist[1:]))
print(out_position[0], end=' ')
print(out_position[1])