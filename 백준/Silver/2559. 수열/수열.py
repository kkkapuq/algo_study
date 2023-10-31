import sys
se = sys.stdin.readline

n, k = map(int, se().split())
arr = list(map(int, se().split()))

temp = sum(arr[:k])
answer = temp

for i in range(n-k):
    temp += arr[i+k] - arr[i]
    if answer < temp:
        answer = temp

print(answer)