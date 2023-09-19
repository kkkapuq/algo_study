'''
문제 : 파일정리
링크 : https://www.acmicpc.net/problem/20291
소요시간 : 13분
'''
import sys
se = sys.stdin.readline

n = int(input())
cows = {}
cnt = 0

for _ in range(n):
    cow, num = map(int, se().strip().split())
    if cow in cows:
        if cows[cow] != num:
            cnt += 1
        cows[cow] = num
    else:
        cows[cow] = num

print(cnt)