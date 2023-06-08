# 들어오는 방향 좌표는 dir = 0 북, dir = 1 동, dir = 2 남, dir = 3 서 으로 잡는다.
# / 은 북, 동, 남, 서 는 서, 남, 동, 북 으로 튕겨주고
# \ 은 북, 동, 남, 서 는 동, 북, 서, 남 으로 튕겨준다.

# 들어오는 방향에 따라 방향좌표를 바꿔주는 맵 /과 \가 따로있다

slashDir = {
    0: 3,
    1: 2,
    2: 1,
    3: 0
}
reSlashDir = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2
}

# 1) \와 / 입장에서 보면 동쪽에서 쏜건 서쪽에서 쏜거임.
# 2) 따라서 slashDir과 reSlashDir 에 "이거 여기서 쏜겁니다" 라는 의미를 전달해줄 방향좌표가 필요함
# 3) 예를들어서, k == 3이라고 했을 때, 첫 cDir 은 0, 북에서 쏜거다. 이건 유지해줘야됨.
# 4) 근데 이제 그 다음에 2) 에서 말한걸 slashDir에 넣어줘서 방향좌표를 알고, 어떻게 움직여야 할 지 알아야됨

attckedDir = {
    0 : 2,
    1 : 3,
    2 : 0,
    3 : 1
}

# /가 사용할 dx, dy를 만들어준다.
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

n = int(input())
grid = []
cnt = 0

for i in range(n):
    grid.append(list(input()))

k = int(input())

# 레이저 포인터 시작방향 정해주기
cDir = 0
# r, c 행렬 좌표
r, c = 0, 0

# 주어지는 k 값에 따라 방향과 좌표를 설정해준다.
if k <= n:
    cDir = 0
    r, c = 0, k-1
elif k > n and k <= 2*n:
    cDir = 1
    r, c = k-n-1, n-1
elif k > 2*n and k <= 3*n:
    cDir = 2
    r, c = n-1, 3*n-k
elif k > 3*n:
    cDir = 3
    r, c = 4*n -k, 0

# 좌표가 허용범위 내라면 while문 돈다.
while r >= 0 and r < n and c >= 0 and c < n:
    # 레이저가 빛을 쏘고, 해당 위치로 r, c를 이동시켜준다.
    if cnt == 0:
        if grid[r][c] == '/':
            cDir = slashDir[cDir]
        elif grid[r][c] == '\\':
            cDir = reSlashDir[cDir]
    else:
        if grid[r][c] == '/':
            cDir = slashDir[attckedDir[cDir]]
        elif grid[r][c] == '\\':
            cDir = reSlashDir[attckedDir[cDir]]
    r, c = r + dx[cDir], c + dy[cDir]
    cnt += 1

print(cnt)