import sys
si = sys.stdin.readline

n = int(si().strip())
arr = [int(si().strip()) for _ in range(n)]
score = []

# 계단별로 그 계단까지 올랐을 때 오를 수 있는 점수의 최대값을 갱신해나가자.
# 3번째까진 수기로 넣어주기

if n == 1:
    print(arr[0])
    exit()
elif n == 2:
    print(arr[0] + arr[1])
    exit()

score.append(arr[0])
score.append(arr[0] + arr[1])
score.append(max(arr[0] + arr[2], arr[1] + arr[2]))

# 3번 연속해서 밟을 수 없기 때문에, i번째 계단의 최대값이 될 수 있는건 둘 중 하나다.
# i가 4번째 계단이라고 가정해보자.
# - 1, 2, 4번 계단을 밟거나 (마지막 전 계단 안밟는 루트)
# - 1, 3, 4번 계단을 밟거나 (마지막 전 계단 밟는 루트)
# score에는 계단별로 최대값이 저장된다. 따라서 
# 이를 점화식으로 만들면 (i-3, i-1, i), (i-2, i-1)
for i in range(3, n):
    score.append(max(score[i-3] + arr[i-1] + arr[i], score[i-2] + arr[i]))

# 마지막 인덱스 출력
print(score[n-1])