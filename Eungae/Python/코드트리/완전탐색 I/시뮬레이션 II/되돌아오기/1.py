import sys
si = sys.stdin.readline

# 1. dx, dy 는 동,서,남,북 으로 둔다.
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
x, y = 0, 0
answer = -1

dic = {
    'E' : 0,
    'W' : 1,
    'S' : 2,
    'N' : 3
}

n = int(input())
temp = 0

def move(move_dir, dist):
    global x, y
    global answer, temp

    for _ in range(dist):
        x, y =x + dx[move_dir], y + dy[move_dir]

        temp += 1

        if x == 0 and y == 0:
            answer = temp
            return True
    return False

for _ in range(n):
    op, cnt = si().split()
    cnt = int(cnt)
    
    done = move(dic[op], cnt)

    if done:
        break

print(answer)