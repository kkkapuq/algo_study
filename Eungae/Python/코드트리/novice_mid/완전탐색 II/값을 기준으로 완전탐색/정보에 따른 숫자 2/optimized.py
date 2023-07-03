import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
t, a, b = tuple(map(int, input().split()))

sn_data = [
    tuple(input().split())
    for _ in range(t)
]

ans = 0

# 각 숫자에 대해
# s에 더 가까운지 n에 더 가까운지 판단합니다.
for i in range(a, b + 1):
	# 숫자 i에서부터 s로부터의 거리와
    # n으로부터의 거리를 확인합니다.
    distance_s = INT_MAX
    distance_n = INT_MAX

    for p, q in sn_data:
        q = int(q)

        if p == 'S':
            distance_s = min(distance_s, abs(q - i))
        else:
            distance_n = min(distance_n, abs(q - i))
  
    if distance_s <= distance_n:
        ans += 1
    
print(ans)