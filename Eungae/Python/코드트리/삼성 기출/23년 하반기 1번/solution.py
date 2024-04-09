def check_santa_alive(santa_info):
    for i in range(1, len(santa_info)):
        if santa_info[i][0] == 1:
            return True
    return False

def rudolf_search(rudolf_position, santa_position):
    closest_santa = 0
    global rdr, rdc
    closest = 10000

    r = rudolf_position[0]
    c = rudolf_position[1]

    for i in range(1, len(santa_position)):
        if santa_info[i][0] == 1:
            santa_r = santa_position[i][0]
            santa_c = santa_position[i][1]
            distance = (r - santa_r) ** 2 + (c - santa_c) ** 2
            
            # 만약 최단거리 산타라면 갱신
            if closest > distance:
                closest_santa = i
                closest = distance

            # 만약 최단거리 산타가 여러명이라면 r, c 순으로 큰 값인 산타를 우선순위 지정
            elif closest == distance:
                closest_santa_r = santa_position[closest_santa][0]
                closest_santa_c = santa_position[closest_santa][1]

                if closest_santa_r < santa_r:
                    closest_santa = i
                elif closest_santa_r == santa_r and closest_santa_c < santa_c:
                    closest_santa = i

    return closest_santa

def rudolf_move(rudolf_position, santa_position):
    r = rudolf_position[0]
    c = rudolf_position[1]

    santa_r = santa_position[0]
    santa_c = santa_position[1]

    global rudolf_dir
    closest = 10000

    for i in range(8):
        nr = r + rdr[i]
        nc = c + rdc[i]

        if nr < 1 or nr > N or nc < 1 or nc > N:
            continue

        distance = (nr - santa_r) ** 2 + (nc - santa_c) ** 2
        
        if closest > distance:
            rudolf_dir = i
            closest = distance
    
    rudolf_position[0] = r + rdr[rudolf_dir]
    rudolf_position[1] = c + rdc[rudolf_dir]
    graph[r][c] = 0
    graph[r + rdr[rudolf_dir]][c + rdc[rudolf_dir]] = -1

    return rudolf_position

def santa_knockback(knockbacked_santa, dir, by_rudolf):
    global graph, santa_info, santa_position, turn

    r = santa_position[knockbacked_santa][0]
    c = santa_position[knockbacked_santa][1]

    # 루돌프가 움직여서 산타가 넉백됐을 떄
    if by_rudolf == 0:    
        nr = r + (rdr[dir] * C)
        nc = c + (rdc[dir] * C)
    # 산타가 움직여서 넉백됐을 때
    elif by_rudolf == 1:
        nr = r + (rdr[dir] * (D-1))
        nc = c + (rdc[dir] * (D-1))
    # 다른 산타에 의해서 넉백됐을 때
    elif by_rudolf == 2:
        nr = r + rdr[dir]
        nc = c + rdc[dir]

    # 게임판 밖으로 밀려나게 되면 죽는다.
    if nr < 1 or nr > N or nc < 1 or nc > N:
        santa_info[knockbacked_santa][0] = 0
        santa_position[knockbacked_santa][0] = nr
        santa_position[knockbacked_santa][1] = nc
        if by_rudolf != 0:
            graph[r][c] = 0
        return
    
    # 재귀 탈출 조건
    elif graph[nr][nc] == 0:
        santa_position[knockbacked_santa][0] = nr
        santa_position[knockbacked_santa][1] = nc
        graph[nr][nc] = knockbacked_santa
        return
    
    # 튕겨져 나갈 때 다른 산타와 부딪히면 연쇄적으로 상호작용한다.
    if graph[nr][nc] != -1 and graph[nr][nc] != 0:
        santa_knockback(graph[nr][nc], dir, 2)
        graph[nr][nc] = knockbacked_santa
        santa_position[knockbacked_santa][0] = nr
        santa_position[knockbacked_santa][1] = nc

def santa_move(rudolf, santa):
    global graph, santa_info, santa_position, turn, D

    dir = 0

    r = santa_position[santa][0]
    c = santa_position[santa][1]

    rudolf_r = rudolf[0]
    rudolf_c = rudolf[1]

    closest = (r - rudolf_r) ** 2 + (c - rudolf_c) ** 2
    # 루돌프와 가까워질 수 없을 때 판별하기 위한 플래그
    flag = False
    
    # 루돌프와 가장 가까운 방향으로 이동한다. 상우하좌 우선순으로 이동
    for i in range(0, 8, 2):
        nr = r + rdr[i]
        nc = c + rdc[i]
        
        # 게임판 밖이거나 해당위치에 다른 산타가 있다면 해당방향은 패스한다.
        if nr < 1 or nr > N or nc < 1 or nc > N or (graph[nr][nc] != -1 and graph[nr][nc] != 0):
            continue

        distance = (nr - rudolf_r) ** 2 + (nc - rudolf_c) ** 2

        # 상우하좌 우선순으로 이동할 거리를 정한다.
        if closest > distance:
            dir = i
            closest = distance
            # 최단거리로 어딘가로 이동 가능하니 플래그값 갱신
            flag = True
        elif closest == distance:
            dir = i if i < dir else dir
    # 루돌프와 가까워질 수 없다면 이동하지 않는다.
    if not flag:
        return

    # 해당 위치에 루돌프가 있다면 점수를 얻고 넉백한다.
    if graph[r + rdr[dir]][c + rdc[dir]] == -1:
        santa_info[santa][2] += D
        santa_info[santa][1] = turn + 1
        if dir == 0:
            dir = 4
        elif dir == 2:
            dir = 6
        elif dir == 4:
            dir = 0
        else:
            dir = 2
        # 산타의 자리는 계산을 위해 갱신하지 않는다.
        graph[r][c] = 0
        santa_knockback(santa, dir, 1)
    else:
        santa_position[santa][0] = r + rdr[dir]
        santa_position[santa][1] = c + rdc[dir]
        graph[r][c] = 0
        graph[r + rdr[dir]][c + rdc[dir]] = santa

def santa_score_up():
    global santa_info
    for i in range(1, len(santa_info)):
        if santa_info[i][0] == 1:
            santa_info[i][2] += 1


# 입력 및 초기정보 세팅
N, M, P, C, D = map(int, input().split())
graph = [ [0 for _ in range(N+1)] for _ in range(N+1) ]

# 루돌프 위치 입력
rudolf = list(map(int, input().split()))
graph[rudolf[0]][rudolf[1]] = -1
# 루돌프가 돌진하는 방향을 전역변수로 설정
rudolf_dir = 0

# 산타정보 = [생존여부, 기절한 턴, 점수]
santa_info = [[1, 0, 0] for _ in range(P+1)]
santa_position = [[0, 0] for _ in range(P+1)]

for i in range(P):
    n, r, c = map(int, input().split())
    santa_position[n] = [r, c]
    graph[r][c] = n

# 루돌프가 사용할 8방향 탐색 dr, dc
rdr, rdc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

# 산타가 사용할 4방향 탐색 dr, dc
sdr, sdc = [-1, 0, 1, 0], [0, 1, 0, -1]

# 현재 턴 수
turn = 0

for _ in range(M):
    turn += 1
    # 산타가 모두 죽어있다면 게임 종료
    if not check_santa_alive(santa_info):
        break
    # 턴이 모두 종료된다면 게임 종료
    if turn > M:
        break

    # 루돌프 턴 시작
    # 8방향으로 bfs를 시작해서 최단거리에 있는 산타를 골라낸다.
    close_santa = rudolf_search(rudolf, santa_position)
    # 해당 방향으로 루돌프를 이동시킨다.
    rudolf = rudolf_move(rudolf, santa_position[close_santa])
    # 만약 해당 방향에 산타가 존재한다면, 상호작용을 발생시킨다.
    if rudolf[0] == santa_position[close_santa][0] and rudolf[1] == santa_position[close_santa][1]:
        # 먼저 해당 산타에게 점수 부여
        santa_info[close_santa][2] += C
        santa_info[close_santa][1] = turn + 1
        # 산타를 튕겨보낸다.
        santa_knockback(close_santa, rudolf_dir, 0)

    # 산타 턴 시작
    for i in range(1, len(santa_info)):
        # 죽거나 기절한 산타는 움직일 수 없다.
        if santa_info[i][0] == 0 or santa_info[i][1] >= turn:
            continue

        # 산타 이동
        santa_move(rudolf, i)

    # 살아남은 산타들 점수 부여
    santa_score_up()

for i in range(1, len(santa_info)):
    print(santa_info[i][2], end=' ')