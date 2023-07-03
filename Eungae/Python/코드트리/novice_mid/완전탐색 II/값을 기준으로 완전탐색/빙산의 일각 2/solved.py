import copy

n = int(input())
arr = [int(input()) for _ in range(n)]

answer = 0

for i in range(1, 1001):
    cnt = 0
    if arr[0] > i:
        cnt += 1

    for j in range(1, n):
        if arr[j] > i and arr[j-1] <= i:
            cnt += 1
    answer = max(answer, cnt)
print(answer)