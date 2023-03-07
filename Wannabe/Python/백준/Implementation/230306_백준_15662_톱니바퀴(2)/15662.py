import sys
from collections import deque

si = sys.stdin.readline

T = int(si().strip())
g = [deque(map(int, list(si().strip()))) for _ in range(T)]
K = int(si().strip())
ans = 0


def rotate(idx, cw):
    global T, g
    rot = [0] * T
    rot[idx] = cw
    mid, turn = idx, cw
    while mid > 0 and g[mid][6] ^ g[mid - 1][2]:
        turn *= -1
        rot[mid - 1] = turn
        mid -= 1
    mid = idx
    turn = cw
    while mid < T - 1 and g[mid][2] ^ g[mid + 1][6]:
        turn *= -1
        rot[mid + 1] = turn
        mid += 1
    for i, w in enumerate(rot):
        if w != 0:
            g[i].rotate(w)


def cnt_zero_of_idx_zero():
    global T, ans
    for i in range(T):
        if g[i][0] == 1:
            ans += 1


for i in range(K):
    gnum, cw = map(int, si().strip().split())
    rotate(gnum-1, cw)

cnt_zero_of_idx_zero()
print(ans)
