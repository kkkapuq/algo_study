n = int(input())

points = [ tuple(map(int, input().split())) for _ in range(n)]

answer = 999999

for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        # 각 사분면 별로 점이 어떻게 분포되어있는지 확인한다.
        # 각각 1, 2, 3, 4분면
        pointCnt = [0, 0, 0, 0]

        for x, y in points:
            if x > i and y > j:
                pointCnt[0] += 1
            elif x < i and y > j:
                pointCnt[1] += 1
            elif x < i and y < j:
                pointCnt[2] += 1
            else:
                pointCnt[3] += 1
        
        answer = min(answer, max(pointCnt))

print(answer)
