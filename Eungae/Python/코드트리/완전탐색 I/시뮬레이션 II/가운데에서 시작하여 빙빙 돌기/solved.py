# 1. 언제 방향을 틀어줘야 되는가?
# 1-1. cnt만큼 횟수를 채웠을 때
# 2. 예제를 기준으로 전진하는 칸 수를 처음부터 보면 다음과 같다.
# 동 1 -> 북 1
# 서 2 -> 남 2
# 동 3 -> 북 3
# 서 4 -> 남 4
# 즉, n 칸을 가는게 2개 세트로 이루어져 있따.
# 따라서, 몇 칸 전진해야 하는지 를 분기점으로 삼을 cnt를 두고, 이게 2가 될 때마다 0으로 초기화 시켜준 다음, 다시 2까지 ++ 시켜준다.
# cnt == 0, 동쪽으로 1칸 전진, cnt++
# cnt == 1, 북쪽으로 1칸 전진, cnt++
# cnt == 2, cnt를 0으로 만들어줌, cnt = 0, 서쪽으로 2칸 전진, cnt++
# cnt == 1, 남쪽으로 2칸 전진, cnt++
# .. 이런식으로 하면 몇 칸 전진해야 하는지가 나온다.
# 왼쪽이나 오른쪽으로 이동할 때, cnt++ 해주고 그 외 방향은 cnt만큼 이동했으면 방향전환 해준다.

n = int(input())

#방향좌표와 몇 칸 전진해야 하는지 알려주는 변수
moveDir, moveNum = 0, 1

grid = [ [0 for _ in range(n)] for _ in range(n)]

# 중앙 좌표 설정
r, c = n//2, n//2

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 현재 몇 칸 째 전진 중인지 저장하는 임의의 수
temp = 0

def move():
    global r, c

    # cDir = 0, 1, 2, 3 순으로 동, 북, 서, 남
    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
    r, c = r + dx[moveDir], c + dy[moveDir]

def end():
    return not inRange(r, c)

cnt = 1 
while not end():
    for _ in range(cnt):
        grid[r][c] = cnt
        cnt += 1

        move()

        if end():
            break

    moveDir = (moveDir + 1) % 4
    if moveDir == 0 or moveDir == 2:
        moveNum += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()