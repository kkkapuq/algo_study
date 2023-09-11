'''
문제 : 주유소
링크 : https://www.acmicpc.net/problem/13305
소요시간 : 19:00~분
'''
n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# 최소 가격
minCost = price[0]
# 총합 가격
cost = distance[0] * price[0]
# 현재까지 온 거리
dist = 0
for i in range(1, n-1):
    if price[i] < minCost:
        minCost = price[i]
        cost += dist * minCost
        dist = distance[i]
    else:
        dist += distance[i]
    
    if i == n-2:
        cost += minCost * dist

print(cost)