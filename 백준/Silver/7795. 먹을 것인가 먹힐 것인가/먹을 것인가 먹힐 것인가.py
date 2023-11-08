'''
문제 : 먹을 것인가 먹힐 것인가
난이도 : 실버 3
소요 시간 : 
'''
import sys
se = sys.stdin.readline
t = int(se().rstrip())

for _ in range(t):
    a, b = se().split()
    a = list(map(int, se().split()))
    b = list(map(int, se().split()))

    # 이분탐색을 위한 정렬
    a.sort()
    b.sort()
    answer = 0

    for i in a:
        # a[i]보다 작은 b의 개수
        result = -1
        l, r = 0, len(b)-1
        while l <= r:
            mid = (l+r) // 2
            if i > b[mid]:
                # a[i]보다 작으면 해당 인덱스 개수만큼은 모두 a[i] 보다 작다는 뜻
                result = mid
                l = mid + 1
            elif i <= b[mid]:
                r = mid - 1
        answer += result + 1
    
    print(answer)
        