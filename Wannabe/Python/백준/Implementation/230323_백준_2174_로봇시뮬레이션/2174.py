import sys
si = sys.stdin.readline

dir = 'NESW'
mvm = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# position on grid starts from bottom-left
# dir defined as 0123(NWES)
# grid only updates robot id at position x, y, (1-M)
# robot info 2d array: element has [x, y, dir]
# update by repeated movment
A, B = map(int, si().strip().split())
N, M = map(int, si().strip().split())

grid = [[0]*A for _ in range(B)]
info = []
for i in range(N):
    temp = si().strip().split()
    xy = list(map(int, temp[:2]))                                   # x, y는 가로 세로 순서로 주어짐
    xyp = [B-xy[1], xy[0]-1]
    grid[xyp[0]][xyp[1]] = i+1
    info.append(xyp+[list(dir).index(temp[2])])

def move(robot, cmd, rep):
    cx, cy, di = info[robot-1]
    nx, ny = cx, cy
    if cmd == 'L':
        rep %= 4
        di -= rep
        if di < 0:
            di += 4
        info[robot-1][2] = di
    elif cmd == 'R':
        rep %= 4
        di += rep
        if di >= 3:
            di -= 4
        info[robot-1][2] = di
    else:
        for _ in range(rep):
            nx, ny = nx+mvm[di][0], ny+mvm[di][1]
            if nx < 0 or nx >= B or ny < 0 or ny >= A:
                return f'Robot {robot} crashes into the wall'
            if grid[nx][ny]:
                return f'Robot {robot} crashes into robot {grid[nx][ny]}'
        grid[cx][cy] = 0
        grid[nx][ny] = robot
        info[robot-1][:2] = [nx, ny]
    return ''
for _ in range(M):
    a, b, c = si().strip().split()
    ret = move(int(a), b, int(c))
    if ret:
        break
else:
    print('OK')
    exit(0)
print(ret)

"""Robot 2 crashes into the wall
3 3
2 2
1 1 S
3 3 N
1 L 1
2 F 1
"""
"""Robot 1 crashes into robot 2
3 3
2 6
1 1 S
3 3 N
1 L 1
2 L 1
1 F 1
2 F 1
1 L 1
1 F 2
"""