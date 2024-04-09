from collections import deque

# 전역 변수 정의
MAX_N = 31
MAX_L = 41
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]

# 정보를 인덱스 기준으로 기사별로 관리
bef_k = [0 for _ in range(MAX_N)]
r = [0 for _ in range(MAX_N)]
c = [0 for _ in range(MAX_N)]
h = [0 for _ in range(MAX_N)]
w = [0 for _ in range(MAX_N)]
k = [0 for _ in range(MAX_N)]
nr = [0 for _ in range(MAX_N)]
nc = [0 for _ in range(MAX_N)]
dmg = [0 for _ in range(MAX_N)]
is_moved = [False for _ in range(MAX_N)]

def try_movement(idx, dir):
    q = deque()
    
    # 초기화 작업
    for i in range(1, n+1):
        dmg[i] = 0
        is_moved[i] = False
        nr[i] = r[i]
        nc[i] = c[i]

    q.append(idx)
    is_moved[idx] = True

    while q:
        x = q.popleft()

        nr[x] += dr[dir]
        nc[x] += dc[dir]

        # 경계 벗어나는지 체크
        if nr[x] < 1 or nc[x] < 1 or nr[x] + h[x] - 1 > l or nc[x] + w[x] - 1 > l:
            return False
    
        # 대상 기사가 다른 기사나 장애물과 충돌하는지 검사
        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if info[i][j] == 1:
                    dmg[x] += 1
                if info[i][j] == 2:
                    return False
                
        # 다른 기사와 충돌한다면, 해당 기사도 같이 이동
        for i in range(1, n+1):
            # 이미 움직인 조각이거나, 죽은 기사는 넘김
            if is_moved[i] or k[i] <= 0:
                continue
            # 세로가 겹치는지 확인
            if r[i] > nr[x] + h[x] - 1 or nr[x] > r[i] + h[i] -1:
                continue
            # 가로가 겹치는지 확인
            if c[i] > nc[x] + w[x] - 1 or nc[x] > c[i] + w[i] - 1:
                continue

            is_moved[i] = True
            q.append(i)
    
    dmg[idx] = 0
    return True


# 특정 조각을 지정된 방향으로 이동시키는 함수입니다.
def move_piece(idx, move_dir):
    if k[idx] <= 0:
        return

    # 이동이 가능한 경우, 실제 위치와 체력을 업데이트합니다.
    if try_movement(idx, move_dir):
        for i in range(1, n + 1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= dmg[i]

# 입력값을 받습니다.
l, n, q = map(int, input().split())
for i in range(1, l + 1):
    info[i][1:] = map(int, input().split())
for i in range(1, n + 1):
    r[i], c[i], h[i], w[i], k[i] = map(int, input().split())
    bef_k[i] = k[i]

for _ in range(q):
    idx, d = map(int, input().split())
    move_piece(idx, d)

# 결과를 계산하고 출력합니다.
ans = sum([bef_k[i] - k[i] for i in range(1, n + 1) if k[i] > 0])
print(ans)