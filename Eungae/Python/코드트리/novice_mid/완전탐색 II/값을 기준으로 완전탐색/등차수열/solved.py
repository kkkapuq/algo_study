n = int(input())

arr = list(map(int, input().split()))
ans = 0

for x in range(1, 101):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == 2*x:
                cnt += 1
    ans = max(ans, cnt)
print(ans)