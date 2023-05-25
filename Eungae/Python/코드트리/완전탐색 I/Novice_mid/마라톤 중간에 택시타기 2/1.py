import sys, copy
N = int(input())
point = [list(map(int, input().split())) for _ in range(N) ]
answer = sys.maxsize

for i in range(1, N-1):
    temp = copy.deepcopy(point)
    del temp[i]
    tempSum = 0
    for j in range(len(temp)-1):
        # 시작지점 0부터 끝까지 거리구하기
        tempSum += abs(temp[j][0] - temp[j+1][0]) + abs(temp[j][1] - temp[j+1][1])
    answer = min(answer, tempSum)

print(answer)