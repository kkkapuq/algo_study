n = int(input())
nxny = { 'N' : [0, 1],
         'S' : [0, -1],
         'E' : [1, 0],
         'W' : [-1, 0]}

p = [0, 0]
for i in range(n):
    op, cnt = map(str, input().split())
    cnt = int(cnt)
    dx = nxny[op][0] * cnt
    dy = nxny[op][1] * cnt
    p[0] = p[0] + dx
    p[1] = p[1] + dy

print(' '.join(map(str, p)))