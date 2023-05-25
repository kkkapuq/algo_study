n, k = map(int, input().split())
maximum = 10000
arr = [0] * (maximum + 1)

# 알파벳 리스트 입력
for _ in range(n):
    p, a = map(str, input().split())
    p = int(p)
    
    arr[p] = 1 if a == 'G' else 2

maxSum = 0
for i in range(maximum - k + 1):
    tempSum = 0
    for j in range(i, i+k+1):
        tempSum += arr[j]
    
    maxSum = max(maxSum, tempSum)

print(maxSum)

