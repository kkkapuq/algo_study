n = int(input())
line = [0] * 101
for _ in range(n):
    l, p = input().split()
    l = int(l)
    if p == 'G':
        line[l] = 1
    elif p == 'H':
        line[l] = 2

answer = 0

for i in range(100):
    gCnt = 0
    hCnt = 0
    for j in range(i, 100):
        if line[j] == '1':
            gCnt += 1
        elif line[j] == '2':
            hCnt += 1
        if gCnt == hCnt:
            answer = max(answer, abs(i-j))

print(answer)