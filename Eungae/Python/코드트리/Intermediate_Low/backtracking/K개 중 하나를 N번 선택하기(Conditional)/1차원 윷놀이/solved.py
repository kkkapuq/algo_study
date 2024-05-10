'''
문제 : 1차원 윷놀이
소요 시간 : 30분
링크 : https://www.codetree.ai/missions/2/problems/yutnori-1d/description
'''

import sys
se = sys.stdin.readline

n, m, k = map(int, se().split())
scores = list(map(int, se().split()))
yuts = []
positions = []

answer = 0

def calc():
    global answer
    positions = [1 for i in range(len(yuts))]
    # 최초로 m을 넘었는지 판별하는 리스트
    overed = [False for i in range(len(yuts))]
    temp = 0
    for idx, i in enumerate(yuts):
        positions[i-1] += scores[idx]
        if positions[i-1] >= m and not overed[i-1]:
            overed[i-1] = True
            temp += 1
    answer = max(answer, temp)

def recursion(cnt):
    if cnt == n:
        calc()
        return

    for i in range(k):
        yuts.append(i)
        recursion(cnt+1)
        yuts.pop()


recursion(0)
print(answer)