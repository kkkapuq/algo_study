n, k = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for i in range(n-k+18):
    tempSum = 0
    for j in range(i, i+k):
        tempSum += nums[j]
    answer = max(answer, tempSum)
print(answer)