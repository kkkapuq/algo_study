MAX_NUM = 100

# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    a, x = tuple(map(int, input().split()))
    arr[x] += a
	
# 모든 구간의 시작점을 잡아봅니다.
max_sum = 0
for i in range(MAX_NUM):
	# 해당 구간 내 원소의 합을 구합니다.
	sum_all = 0
	for j in range(i - k, i + k + 1):
		if j >= 0 and j <= MAX_NUM:
			sum_all += arr[j]
        
    # 최댓값을 구합니다.
	max_sum = max(max_sum, sum_all)
                        
print(max_sum)