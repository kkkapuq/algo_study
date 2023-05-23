n = int(input())
people = list(map(int, input().split()))
minDistance = float('inf')

for i in range(n):
    tempSum = 0
    for j in range(n):
        # 1. i번째 집으로 모이는 경우 중에서 거리를 계산하는 방법은 abs(j - i) 다.
        distance = abs(j - i)
        # 2. 사람들의 수와 거리를 곱한 값을 tempSum에 더해준다.
        tempSum += (distance * people[j])
    minDistance = min(minDistance, tempSum)

print(minDistance)
