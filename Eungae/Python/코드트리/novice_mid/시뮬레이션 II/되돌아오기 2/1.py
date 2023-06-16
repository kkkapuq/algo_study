import sys
# 0, 1, 2, 3 -> 북 동 남 서 로 잡기
currDir = 0
answer = -1
x, y = 0, 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

strs = sys.stdin.readline().strip()

for i in range(len(strs)):
    if strs[i] == 'L':
        currDir = (currDir - 1 + 4) % 4
    elif strs[i] == 'L':
        currDir = (currDir + 1) % 4
    else:
        x, y = x + dx[currDir], y + dy[currDir]
    if x == 0 and y == 0:
        answer = i+1
        break

print(answer)