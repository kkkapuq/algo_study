import sys
N = int(input())
room = [int(input()) for _ in range(N)]

answer = sys.maxsize
# N = 5, 4번 인덱스에서 시작한다고 하면
# 5, 1, 2, 3, 4 순으로 돌아야 하는데 for문 조건을 어떻게 구하지?
for i in range(N):
    distance = 0
    for j in range(N):
        temp = (j + N - i) % N
        distance += temp * room[j]
    answer = min(answer, distance)

print(answer)
