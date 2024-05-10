'''
문제 : 1차원 윷놀이
소요 시간 : 30분
링크 : https://www.codetree.ai/missions/2/problems/yutnori-1d/description
'''

import sys
se = sys.stdin.readline

n, m, k = map(int, se().split())
scores = list(map(int, se().split()))
yuts = [1 for _ in range(k)]

answer = 0

def calc():
    global answer
    temp = 0
    for yut in yuts:
        if yut >= m:
            temp += 1
    return temp

def recursion(cnt):
    global answer
    answer = max(answer, calc())

    if cnt == n:
        return

    for i in range(k):
        if yuts[i] >= m:
            continue
        yuts[i] += scores[cnt]
        recursion(cnt+1)
        yuts[i] -= scores[cnt]


recursion(0)
print(answer)