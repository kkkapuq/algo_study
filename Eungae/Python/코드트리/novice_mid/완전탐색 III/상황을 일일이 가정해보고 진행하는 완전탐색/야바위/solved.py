n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range(1, 4):
    cnt = 0
    ball = i
    for j in arr:
        if ball == j[0]:
            ball = j[1]
        elif ball == j[1]:
            ball = j[0]
        if ball == j[2]:
            cnt += 1
    answer = max(cnt, answer)
print(answer)
