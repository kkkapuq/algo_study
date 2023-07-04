import copy
n = int(input())
arr = list(map(int, input().split()))

answer = 999999

for i in range(n):
    temp = copy.deepcopy(arr)
    temp[i] *= 2

    for j in range(len(temp)):
        removed = temp[:j] + temp[j+1:]

        tempSum = 0

        for k in range(len(removed)-1):
            tempSum += abs( removed[k] - removed[k+1] )
        
        answer = min(tempSum, answer)

print(answer)
