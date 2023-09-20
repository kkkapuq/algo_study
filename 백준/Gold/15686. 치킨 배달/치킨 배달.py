'''
문제 : 치킨 배달
링크 : https://www.acmicpc.net/problem/15686
소요시간 : 
'''
from itertools import combinations
n, m = map(int, input().split())
graph = []
answer = 99999999

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 사람이 사는곳과 치킨집 좌표를 가져오자
house, chicken = [], []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

# 조합으로 다 구하기
for i in combinations(chicken, m):
    # 도시의 치킨거리
    dist = 0

    # 각 집마다 각 치킨집까지의 치킨거리를 계산하고, 최소값으로 업데이트 해준다.
    for j in house:
        minDist = 99999999
        for k in i:
            temp = abs(j[0] - k[0]) + abs(j[1] - k[1])
            minDist = min(temp, minDist)
        dist += minDist
    
    answer = min(dist, answer)

print(answer)