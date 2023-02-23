'''
문제 : RGB거리
난이도 : 실버 1
링크 : https://www.acmicpc.net/problem/1149
'''
import sys
n = int(input())

house = []
for i in range(n):
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    #빨강
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    #초록
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    #파랑
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]
    
print(min(house[-1]))