import sys, copy
n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 가장 높은 밭의 높이를 가장 낮은 밭의 높이로 이동시켜준다.
# 2. while문을 돌면서, t번이상 h높이이상으로 나오는지 체크하고 답 주면 끝
answer = sys.maxsize

for i in range(n):
    cost = 0
    temp = sys.maxsize
    farm = copy.deepcopy(arr)
    while True:
        for j in range(i, i+t):
            if farm[j] < h:
                farm[j] += 1
                cost += 1
            elif farm[j] > h:
                farm[j] -= 1
                cost += 1
            if sum(farm[i:i+t]) % h == 0 and sum(farm[i:i+t]) / h == t:
                temp = min(temp, cost)
                break
        if cost == temp:
            break
    answer = min(temp, answer)

print(cost)