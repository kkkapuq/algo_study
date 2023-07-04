
n = int(input())
arr = list(map(int, input().split()))

answer = 999999

def score(removed_idx):
    sum_val = 0
    prev = -1

    for i in range(n):
        if i == removed_idx:
            continue
        if prev != -1:
            sum_val += abs(arr[i] - prev)
        prev = arr[i]

for i in range(n):
    arr[i] *= 2

    for j in range(n):
        answer = min(answer, score(j))

    arr[i] //= 2

print(answer)