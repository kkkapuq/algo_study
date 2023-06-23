n = int(input())

times = [ tuple(map(int, input().split())) for _ in range(n) ]

answer = 0

for i in range(n):
    lines = [0 for _ in range(1001)]
    temp = times[:i] + times[i+1:]
    cnt = 0
    for j in temp:
        for k in range(j[0]+1, j[1]+1):
            lines[k] = 1
    cnt += sum(lines)
    answer = max(answer, cnt)

print(answer)